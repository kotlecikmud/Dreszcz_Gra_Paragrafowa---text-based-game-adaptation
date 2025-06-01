import json
import re
from bs4 import BeautifulSoup

def parse_html_to_json(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs_data = []

    # First pass: Build a map of calibre_id to actual paragraph number and content div
    id_to_paragraph_map = {}
    all_page_divs = soup.find_all('div', attrs={'data-role': 'page'})

    # Temporary map for resolving hrefs that are just numbers like "#25"
    # This assumes that such an href refers to a paragraph whose <h2> contains "25."
    number_to_calibre_id_map = {}

    for page_div in all_page_divs:
        page_id_attr = page_div.get('id')
        if not page_id_attr:
            continue

        h2_tag = page_div.find('h2', class_=re.compile(r'calibre\d*')) # Relaxed class match
        if h2_tag:
            # Consolidate various ways text might be inside h2 (direct, in <p>, etc.)
            h2_text_parts = [t.strip() for t in h2_tag.find_all(string=True, recursive=True) if t.strip()]
            h2_text = " ".join(h2_text_parts)
            paragraph_num_match = re.search(r'^\s*(\d+)\.?', h2_text) # Match at the beginning
            if paragraph_num_match:
                actual_paragraph_id = int(paragraph_num_match.group(1))
                id_to_paragraph_map[page_id_attr] = {
                    "number": actual_paragraph_id,
                    "div": page_div
                }
                number_to_calibre_id_map[str(actual_paragraph_id)] = page_id_attr


    # Second pass: Extract details for each paragraph
    # Sort page_ids by their mapped paragraph number to process in order (optional, but good for debugging)
    sorted_page_ids = sorted(id_to_paragraph_map.keys(), key=lambda k: id_to_paragraph_map[k]["number"])

    for page_id_attr in sorted_page_ids:
        para_info = id_to_paragraph_map[page_id_attr]
        actual_paragraph_id = para_info["number"]
        page_div = para_info["div"]

        paragraph_entry = {
            'id': actual_paragraph_id,
            'text': '',
            'choices': [],
            'monster': None,
            'actions': []
        }

        # Extract text from <p class="calibre..."> tags
        text_parts = []
        # Iterate over all direct children of page_div to maintain order and context
        for content_item in page_div.contents:
            if content_item.name == 'p' and content_item.has_attr('class') and 'calibre' in "".join(content_item.get('class', [])):
                # Exclude <p> tags that are solely for choices or specific formatting like menu button
                if content_item.find('a', class_="ui-btn-right"): # Skip menu button
                    continue

                # More careful text extraction from p_tag
                current_p_text_parts = []
                for sub_content in content_item.contents:
                    if isinstance(sub_content, str): # NavigableString
                        current_p_text_parts.append(sub_content.strip())
                    elif sub_content.name == 'b' and sub_content.find(string=re.compile(r'Z:\d+\s+W:\d+')):
                        # This is likely monster text, skip here, handled later
                        continue
                    elif sub_content.name == 'a' and sub_content.has_attr('href'):
                        # This is likely a choice, skip here, handled later
                        continue
                    elif sub_content.name == 'i': # Italicized text
                         current_p_text_parts.append(sub_content.get_text(strip=True, separator=' '))
                    elif sub_content.name not in ['br']: # Avoid adding text from other complex children already handled
                        current_p_text_parts.append(sub_content.get_text(strip=True, separator=' '))

                cleaned_p_text = ' '.join(filter(None, current_p_text_parts)).strip()
                if cleaned_p_text:
                    text_parts.append(cleaned_p_text)
            # Capture text that might be directly under page_div or within other tags like <i> not in <p>
            elif isinstance(content_item, str) and content_item.strip():
                 text_parts.append(content_item.strip())
            elif content_item.name == 'i' and not content_item.find_parent('p', class_=re.compile(r'calibre\d*')):
                 text_parts.append(content_item.get_text(strip=True, separator=' '))


        full_text = ' '.join(text_parts).replace('\n', ' ').strip()
        full_text = re.sub(r'\s+', ' ', full_text) # Normalize whitespace
        paragraph_entry['text'] = full_text

        # Extract choices
        choice_links = page_div.find_all('a', href=True)
        processed_choices_for_para = set() # To avoid duplicate choices from same link text/target

        for link in choice_links:
            choice_text_raw = link.get_text(strip=True)
            choice_text = re.sub(r'\s+', ' ', choice_text_raw).strip().replace(".","") # Remove trailing dots

            href = link.get('href')
            target_paragraph_id = None

            # Skip non-game links
            if "globalpanel" in href or "karta_wyprawy" in href or not choice_text:
                if not (link.find('img') and "menu-small.png" in link.find('img').get('src','')): # allow menu buttons if they are the only thing
                    continue

            # If link is an image button without text, skip (e.g. menu button)
            if link.find('img') and not choice_text.strip():
                continue

            anchor = href.split('#')[-1]

            if anchor.isdigit(): # e.g. href="#25"
                # Try to find this number in our direct number_to_calibre_id_map
                if anchor in number_to_calibre_id_map:
                    target_page_id_attr = number_to_calibre_id_map[anchor]
                    if target_page_id_attr in id_to_paragraph_map:
                        target_paragraph_id = id_to_paragraph_map[target_page_id_attr]["number"]
                # If not found by direct number, sometimes choice_text itself is the target
                elif choice_text.isdigit():
                     numeric_choice_text = int(choice_text)
                     # Check if this number maps to a paragraph
                     if str(numeric_choice_text) in number_to_calibre_id_map:
                         target_page_id_attr = number_to_calibre_id_map[str(numeric_choice_text)]
                         if target_page_id_attr in id_to_paragraph_map:
                            target_paragraph_id = id_to_paragraph_map[target_page_id_attr]["number"]


            elif anchor in id_to_paragraph_map: # Anchor is a calibre_link-XYZ
                target_paragraph_id = id_to_paragraph_map[anchor]["number"]

            # Fallback: if target_paragraph_id is still None, and choice_text contains a number, try that
            if target_paragraph_id is None:
                # Look for "Patrz DDD" or just "DDD" in the choice text
                match_patrz = re.search(r'(?:Patrz|patrz)?\s*(\d+)', choice_text)
                if match_patrz:
                    num_in_text = match_patrz.group(1)
                    if num_in_text in number_to_calibre_id_map:
                        target_page_id_attr = number_to_calibre_id_map[num_in_text]
                        if target_page_id_attr in id_to_paragraph_map:
                            target_paragraph_id = id_to_paragraph_map[target_page_id_attr]["number"]

            if target_paragraph_id:
                # Clean choice text: remove "Patrz DDD", "DDD.", or just "DDD" if it's the target
                # and it's at the end of the string.
                cleaned_choice_text = choice_text
                # Try to remove "Patrz DDD" or "DDD" from the end more carefully
                escaped_target_str = str(target_paragraph_id)
                patterns_to_remove = [
                    r'\s*Patrz\s+' + escaped_target_str + r'\s*\.?$',
                    r'\s*' + escaped_target_str + r'\s*\.?$',
                ]
                for pat in patterns_to_remove:
                    cleaned_choice_text = re.sub(pat, '', cleaned_choice_text, flags=re.IGNORECASE).strip()

                if not cleaned_choice_text and choice_text.replace(".","").isdigit():
                    cleaned_choice_text = f"Idź do paragrafu {target_paragraph_id}"
                elif not cleaned_choice_text and choice_text: # If original text was not just a number but became empty
                    cleaned_choice_text = choice_text # Revert to original if cleaning removed everything meaningful

                choice_signature = (cleaned_choice_text, target_paragraph_id)
                if choice_signature not in processed_choices_for_para:
                    paragraph_entry['choices'].append({
                        'text': cleaned_choice_text,
                        'target_paragraph_id': target_paragraph_id
                    })
                    processed_choices_for_para.add(choice_signature)

        # Extract monster data
        monster_tag = page_div.find('b', class_=re.compile(r'calibre\d*'), string=re.compile(r'Z:\s*\d+\s+W:\s*\d+'))
        if monster_tag:
            monster_text_full = monster_tag.get_text(strip=True)
            # Regex to capture name, Z, and W, allowing for Polish characters and varied spacing
            monster_match = re.search(r'([\wĄĆĘŁŃÓŚŹŻ\s]+?)\s*Z:\s*(\d+)\s*W:\s*(\d+)', monster_text_full, re.IGNORECASE | re.UNICODE)
            if monster_match:
                name = monster_match.group(1).strip()
                # Exclude known non-monster bolded texts that match Z:W pattern
                if name.lower() not in ["i cechy", "ii. walka", "iii. ucieczka", "iv. szczęście", "v. podwyższanie poziomu cech", "vi. prowiant", "vii. zapis", "viii. cel wyprawy"]:
                    paragraph_entry['monster'] = {
                        'name': name,
                        'dexterity': int(monster_match.group(2)),
                        'stamina': int(monster_match.group(3))
                    }
                    # Attempt to remove monster text from main text, only if it was clearly separated
                    # This is tricky because sometimes it's inline.
                    # For now, we rely on the initial text extraction trying to separate it.

        # Extract special actions
        # Use the already extracted full_text for action parsing
        current_text_for_actions = paragraph_entry['text']

        if "SSS" in current_text_for_actions:
            paragraph_entry['actions'].append({'type': 'luck_test', 'details': 'SSS required'})
        if "Rzuć raz kostką" in current_text_for_actions or "Rzucasz raz kostką" in current_text_for_actions:
            paragraph_entry['actions'].append({'type': 'dice_roll', 'details': 'Rzuć raz kostką'})
        if "Rzuć dwiema kostkami" in current_text_for_actions or "Rzucasz dwiema kostkami" in current_text_for_actions:
            paragraph_entry['actions'].append({'type': 'dice_roll', 'details': 'Rzuć dwiema kostkami'})

        # Items and stats
        stat_keywords = {
            'ZRĘCZNOŚCI': 'dexterity', 'Z': 'dexterity',
            'WYTRZYMAŁOŚCI': 'stamina', 'W': 'stamina',
            'SZCZĘŚCIA': 'luck', 'S': 'luck',
            'Prowiantu': 'proviant', 'P': 'proviant', # 'P' might be too ambiguous
            'sztuk złota': 'gold'
        }

        # Loss patterns: "Tracisz X Y", "Odejmij X od swojej Y"
        loss_matches = re.findall(r'(Tracisz|-)\s*(\d+)\s*([ZWSP]|punkt[yów]?\s*(?:ZRĘCZNOŚCI|WYTRZYMAŁOŚCI|SZCZĘŚCIA|Prowiantu))', current_text_for_actions, re.IGNORECASE | re.UNICODE)
        for match in loss_matches:
            value = int(match[1])
            stat_full = match[2].upper()
            stat_name = "unknown"
            for keyword, name in stat_keywords.items():
                if keyword.upper() in stat_full:
                    stat_name = name
                    break
            if stat_name != "unknown":
                 paragraph_entry['actions'].append({'type': 'stat_change', 'details': f"lose {value} {stat_name}"})

        # Gain patterns: "Zyskujesz X Y", "Dodaj X do Y", "+X Y"
        gain_matches = re.findall(r'(Zyskujesz|Dodaj|Otrzymujesz|\+)\s*(\d+)\s*([ZWSP]|punkt[yów]?\s*(?:ZRĘCZNOŚCI|WYTRZYMAŁOŚCI|SZCZĘŚCIA|Prowiantu)|sztuk złota)', current_text_for_actions, re.IGNORECASE | re.UNICODE)
        for match in gain_matches:
            value = int(match[1])
            stat_full = match[2].upper() # Original text like "sztuk złota" or "Z"
            stat_name = "unknown_gain"

            if "ZŁOTA" in stat_full:
                stat_name = "gold"
            else:
                for keyword, name in stat_keywords.items():
                    # Check if the keyword (e.g., "ZRĘCZNOŚCI", "Z") is in the matched stat description
                    if keyword.upper() in stat_full.replace("PUNKTÓW ", "").replace("PUNKTY ", ""):
                        stat_name = name
                        break

            action_type = 'item_change' if stat_name == 'gold' else 'stat_change'
            if "unknown_gain" not in stat_name :
                paragraph_entry['actions'].append({'type': action_type, 'details': f"gain {value} {stat_name}"})

        if "Możesz zjeść Prowiant" in current_text_for_actions or "możesz zjeść coś z Prowiantu" in current_text_for_actions or "możesz usiąść i zjeść Prowiant" in current_text_for_actions :
             paragraph_entry['actions'].append({'type': 'eat_proviant', 'details': 'Możesz zjeść Prowiant'})

        # Item checks: "Jeśli masz X", "Jeśli posiadasz X"
        item_check_matches = re.findall(r'Jeśli (?:masz|posiadasz) ([^,.]+?)(?:,|\.|\s(?:albo|i|to|możesz|–|-|patrz|zapewni))', current_text_for_actions, re.IGNORECASE | re.UNICODE)
        for match in item_check_matches:
            item_name = match.strip()
            # Filter out very short or non-specific matches that might be stats
            if len(item_name) > 2 and item_name.lower() not in ["s", "w", "z", "p", "złota", "szczęście", "siły", "dość siły", "przynajmniej"] and not item_name.isdigit():
                paragraph_entry['actions'].append({'type': 'item_check', 'details': f"Check if player has {item_name}"})

        # Item acquisition: "Otrzymujesz X", "Znalazłeś X" (excluding stats)
        item_gain_matches = re.findall(r'(Otrzymujesz|Znalazłeś|Dostajesz|Masz|Zabierasz|Możesz wziąć|Możesz zabrać)\s+([^,.]+?)(?:,|\.|\s(?:i|albo|patrz|wpisz|dodaj))', current_text_for_actions, re.IGNORECASE | re.UNICODE)
        for match in item_gain_matches:
            item_name = match[1].strip()
            # Filter out stat gains already handled and very generic terms
            is_stat = False
            for keyword in stat_keywords.keys():
                if keyword.lower() in item_name.lower() or item_name.lower() in keyword.lower() :
                    is_stat = True
                    break
            if not is_stat and len(item_name) > 2 and item_name.lower() not in ["s", "w", "z", "p","złoto"] and not item_name.isdigit() and "sztuk złota" not in item_name.lower() and "punkty" not in item_name.lower():
                 paragraph_entry['actions'].append({'type': 'item_gain', 'details': f"Gain {item_name}"})


        # Deduplicate actions
        unique_actions = []
        seen_actions_repr = set()
        for action in paragraph_entry['actions']:
            action_repr = tuple(sorted(action.items())) # Make order-independent for dict comparison
            if action_repr not in seen_actions_repr:
                unique_actions.append(action)
                seen_actions_repr.add(action_repr)
        paragraph_entry['actions'] = unique_actions

        # Clean up text by removing choice prompts like "Patrz DDD" if they are still there.
        paragraph_entry['text'] = re.sub(r'\s*Patrz\s+\d+\s*\.?\s*$', '', paragraph_entry['text']).strip()
        paragraph_entry['text'] = re.sub(r'\s*-\s*patrz\s+\d+\s*\.?\s*$', '', paragraph_entry['text'], flags=re.IGNORECASE).strip()
        paragraph_entry['text'] = re.sub(r'\s*·\s*([^-\s]+)\s*-\s*patrz\s+\d+\s*,?', '', paragraph_entry['text'], flags=re.IGNORECASE).strip() # e.g. "· zachód - patrz 200,"
        paragraph_entry['text'] = re.sub(r'\s*,\s*$', '', paragraph_entry['text']).strip() # remove trailing commas
        paragraph_entry['text'] = re.sub(r'\s+', ' ', paragraph_entry['text']).strip() # Normalize whitespace

        paragraphs_data.append(paragraph_entry)

    # Sort by ID for consistent output
    paragraphs_data.sort(key=lambda p: p['id'])
    return paragraphs_data

if __name__ == '__main__':
    # This part is for local execution and will be run by the `run_in_bash_session` tool
    html_file_path = 'Assets/Other/HTML_version/DRESZCZ - Gra Paragrafowa.html'
    json_output_path = 'parsed_game_data.json'

    try:
        # Ensure BeautifulSoup is installed
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            print("BeautifulSoup4 is not installed. Please install it: pip install beautifulsoup4")
            exit(1)

        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        parsed_data = parse_html_to_json(html_content)

        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(parsed_data, f, ensure_ascii=False, indent=4)

        print(f"Successfully parsed HTML and saved to {json_output_path}")

    except FileNotFoundError:
        print(f"Error: HTML file not found at {html_file_path}")
    except Exception as e:
        import traceback
        print(f"An error occurred: {e}")
        print(traceback.format_exc())
