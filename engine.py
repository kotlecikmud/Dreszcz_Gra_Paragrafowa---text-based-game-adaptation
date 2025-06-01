import time # For potential pauses, if desired
from player import PlayerCharacter, roll_k6
from game_data import load_game_data, get_paragraph

def perform_sss(player_character: PlayerCharacter):
    """
    Performs a 'Sprawdzenie Swojego Szczęścia' (SSS) test.
    Returns True if lucky, False otherwise.
    Modifies player's luck stat.
    """
    print("\n--- Test Szczęścia (SSS) ---")
    if player_character.stats['luck'] <= 0:
        print("Twoje SZCZĘŚCIE jest na zerowym poziomie lub poniżej! Automatyczna porażka w teście SSS.")
        player_character.stats['luck'] = 0 # Ensure it's not negative
        return False

    dice_roll = roll_k6(2)
    current_luck_val = player_character.stats['luck']

    # According to rules: "Po każdym SSS - niezależnie od wyniku - należy odjąć 1 od aktualnego poziomu SZCZĘŚCIA."
    player_character.stats['luck'] -= 1 # This is the cost of performing SSS.

    print(f"Rzut 2K6: {dice_roll}")
    print(f"Twój poziom SZCZĘŚCIA (przed rzutem, po odjęciu 1 za próbę): {player_character.stats['luck']}")
    # current_luck_val was the value *before* subtracting 1 for the test itself.
    # The test is against the value *before* this mandatory deduction.

    if dice_roll <= current_luck_val:
        print(f"Wynik rzutu ({dice_roll}) <= Poziom SZCZĘŚCIA przed próbą ({current_luck_val}). Udało się! Masz SZCZĘŚCIE!")
        print("-----------------------------")
        return True
    else:
        print(f"Wynik rzutu ({dice_roll}) > Poziom SZCZĘŚCIA przed próbą ({current_luck_val}). Niestety, nie masz SZCZĘŚCIA.")
        print("-----------------------------")
        return False

import re # For parsing details in handle_actions

def handle_actions(player: PlayerCharacter, paragraph_actions: list, current_paragraph_data: dict, game_paragraphs: list):
    """
    Handles special actions defined in a paragraph.
    Returns a tuple: (action_taken_by_event, game_should_end, paragraph_allows_eating_provision)
    - action_taken_by_event: True if an action directly leads to a new paragraph or ends game.
    - game_should_end: True if the game should terminate.
    - paragraph_allows_eating_provision: True if an action in the paragraph explicitly allows eating.
    """
    action_taken_by_event = False
    game_should_end = False
    paragraph_allows_eating_provision = False

    if not paragraph_actions:
        return False, False, False

    print("\n--- Akcje Specjalne w Paragrafie ---")
    for action in paragraph_actions:
        action_type = action.get('type', '').lower()
        details = action.get('details', {})

        if isinstance(details, str):
            parsed_details_str = details
            temp_details_dict = {}
            # Basic parsing for string details (less ideal than structured JSON)
            if action_type == 'stat_change':
                match = re.match(r'(lose|tracisz|gain|zyskujesz|otrzymujesz|dostajesz|\+|-)\s*(\d+)\s*([a-zA-ZĄĆĘŁŃÓŚŹŻ\s]+)', details, re.IGNORECASE)
                if match:
                    op_type, val_str, stat_str_full = match.groups()
                    amount = int(val_str)
                    if op_type.lower() in ['lose', 'tracisz', '-']:
                        amount = -amount
                    # Attempt to map common Polish terms to stat keys
                    stat_str_cleaned = stat_str_full.strip().lower()
                    stat_map_simple = {'z': 'dexterity', 'w': 'stamina', 's': 'luck',
                                       'prowiantu': 'proviant', 'złota': 'gold', 'sztuk złota': 'gold'}
                    stat_key = stat_str_cleaned
                    for k,v in stat_map_simple.items():
                        if k in stat_str_cleaned:
                            stat_key = v
                            break
                    temp_details_dict = {'stat': stat_key, 'amount': amount, 'original_detail': parsed_details_str}
                else: # Fallback if regex fails
                    temp_details_dict = {'original_detail': parsed_details_str} # Store original to avoid losing info
            elif action_type in ['get_item', 'item_gain', 'lose_item', 'item_loss', 'item_check']:
                 temp_details_dict = {'item_name': details, 'original_detail': parsed_details_str}
            elif action_type == 'eat_proviant':
                 action_type = 'eat_provision_prompt'
                 temp_details_dict = {'original_detail': parsed_details_str}
            details = temp_details_dict
            print(f"  Typ: {action_type.replace('_', ' ').capitalize()} (info: \"{parsed_details_str}\")")
        else:
            print(f"  Typ: {action_type.replace('_', ' ').capitalize()} (detale: {details})")


        if action_type == 'stat_change':
            stat_name_from_json = details.get('stat', '').lower()
            amount = details.get('amount', 0)
            if amount == 0 and 'original_detail' in details: # If parsing failed to get amount
                 print(f"    Nie udało się przetworzyć wartości dla zmiany statystyk: {details.get('original_detail')}")
                 continue
            player.change_stat(stat_name_from_json, amount) # player.change_stat has mapping

        elif action_type == 'get_item' or action_type == 'item_gain':
            item_name = details.get('item_name')
            quantity = details.get('quantity', 1)
            if item_name:
                player.add_item(item_name, quantity)
            else:
                print("    Błąd w akcji GET_ITEM: brak 'item_name' w 'details'.")

        elif action_type == 'lose_item' or action_type == 'item_loss':
            item_name = details.get('item_name')
            if item_name:
                player.remove_item(item_name)
            else:
                print("    Błąd w akcji LOSE_ITEM: brak 'item_name' w 'details'.")

        elif action_type == 'item_check':
            item_name = details.get('item_name')
            has_item_paragraph_id = details.get('has_item_paragraph_id')
            no_item_paragraph_id = details.get('no_item_paragraph_id')

            if not item_name:
                print("    Błąd w akcji ITEM_CHECK: brak 'item_name' w 'details'.")
                continue

            print(f"    Sprawdzanie czy posiadasz: {item_name}...")
            # Gold check needs specific handling if item_name is "złoto" and a threshold is implied
            has_item = False
            if "złot" in item_name.lower(): # e.g. "10 sztuk złota" or "złoto"
                gold_amount_match = re.search(r'(\d+)', item_name)
                required_gold = int(gold_amount_match.group(1)) if gold_amount_match else 1 # Assume 1 if no number
                if player.gold >= required_gold:
                    has_item = True
            elif item_name in player.inventory:
                has_item = True

            if has_item:
                print(f"    Posiadasz '{item_name}'.")
                if has_item_paragraph_id is not None:
                    player.current_paragraph_id = has_item_paragraph_id
                    action_taken_by_event = True
            else:
                print(f"    Nie posiadasz '{item_name}'.")
                if no_item_paragraph_id is not None:
                    player.current_paragraph_id = no_item_paragraph_id
                    action_taken_by_event = True
            if action_taken_by_event: break

        elif action_type == 'attribute_test':
            attribute_from_json = details.get('attribute', '').lower()
            threshold = details.get('threshold')
            success_paragraph_id = details.get('success_paragraph_id')
            failure_paragraph_id = details.get('failure_paragraph_id')

            if not attribute_from_json or threshold is None or success_paragraph_id is None or failure_paragraph_id is None:
                print("    Błąd w akcji ATTRIBUTE_TEST: niekompletne dane w 'details'.")
                continue

            stat_map = {'zręczność': 'dexterity', 'z': 'dexterity',
                        'wytrzymałość': 'stamina', 'w': 'stamina',
                        'szczęście': 'luck', 's': 'luck'}
            attribute = stat_map.get(attribute_from_json, attribute_from_json)

            player_value = player.stats.get(attribute)
            if player_value is None:
                print(f"    Błąd w ATTRIBUTE_TEST: nieznany atrybut gracza '{attribute}'.")
                continue

            print(f"    Test Atrybutu: Twoja {attribute.capitalize()} ({player_value}) vs Próg ({threshold}).")
            if player_value >= threshold:
                print("    Test udany!")
                player.current_paragraph_id = success_paragraph_id
            else:
                print("    Test nieudany.")
                player.current_paragraph_id = failure_paragraph_id
            action_taken_by_event = True
            break

        elif action_type == 'dice_roll_event':
            dice_count = details.get('dice_count', 1)
            outcomes = details.get('outcomes', {})

            if not outcomes:
                print("    Błąd w DICE_ROLL_EVENT: brak 'outcomes' w 'details'.")
                continue

            roll_result = roll_k6(dice_count)
            print(f"    Rzut {dice_count}K6: Wynik = {roll_result}")

            next_paragraph_id = outcomes.get(str(roll_result))
            if next_paragraph_id is None: next_paragraph_id = outcomes.get(roll_result)
            if next_paragraph_id is None: next_paragraph_id = outcomes.get('default')

            if next_paragraph_id is not None:
                print(f"    Wynik rzutu prowadzi do paragrafu {next_paragraph_id}.")
                player.current_paragraph_id = next_paragraph_id
                action_taken_by_event = True
                break
            else:
                print("    Wynik rzutu nie prowadzi do zmiany paragrafu (brak pasującej definicji w 'outcomes').")

        elif action_type == 'dice_roll':
            dice_count = 1
            detail_text_for_dice = details.get("original_detail", str(details)) # Use original string if parsed
            if "dwiema kostkami" in detail_text_for_dice:
                dice_count = 2
            roll_result = roll_k6(dice_count)
            print(f"    Rzut {dice_count}K6: Wynik = {roll_result}. (Tekst paragrafu wyjaśni znaczenie)")

        elif action_type == 'luck_test':
            sss_success = perform_sss(player)
            success_paragraph_id = details.get('success_paragraph_id')
            failure_paragraph_id = details.get('failure_paragraph_id')
            if sss_success and success_paragraph_id is not None:
                player.current_paragraph_id = success_paragraph_id
                action_taken_by_event = True
            elif not sss_success and failure_paragraph_id is not None:
                player.current_paragraph_id = failure_paragraph_id
                action_taken_by_event = True
            if action_taken_by_event: break

        elif action_type == 'eat_provision_prompt':
            paragraph_allows_eating_provision = True
            print("    (Możesz teraz zjeść prowiant, wybierając odpowiednią opcję.)")

        elif action_type == 'monster_encounter':
            if current_paragraph_data and current_paragraph_data.get('monster'):
                # This action type is now primarily a trigger; actual combat initiation moved to start_game
                print(f"    Uwaga: W tym miejscu jest {current_paragraph_data['monster']['name']}!")
                # Combat itself is initiated in start_game loop based on monster presence
            else:
                print("    Błąd: Akcja monster_encounter, ale brak danych potwora lub kontekstu paragrafu.")

        if player.stats['stamina'] <= 0:
            print(f"    Twoja Wytrzymałość spadła do {player.stats['stamina']} lub poniżej. Umierasz!")
            game_should_end = True
            action_taken_by_event = True
            break
    print("--- Koniec Akcji Specjalnych ---")
    return action_taken_by_event, game_should_end, paragraph_allows_eating_provision


def initiate_combat(player_character: PlayerCharacter, monster_data: dict, current_paragraph_data: dict, game_paragraphs: list):
    """
    Manages a combat encounter between the player and a monster.
    Returns 'victory', 'defeat', or 'fled'.
    """
    # Create a mutable copy of monster_data for combat
    monster = dict(monster_data)
    print(f"\n!!! ROZPOCZYNA SIĘ WALKA Z {monster['name']} (Z:{monster['dexterity']} W:{monster['stamina']}) !!!")

    temp_player_dex_bonus = 0
    # Example: if "hełm" in player_character.inventory and "jakiś tekst o bonusie" in current_paragraph_data['text']:
    #     temp_player_dex_bonus = 1 # Or some other bonus value

    while True:
        if player_character.stats['stamina'] <= 0:
            # player.change_stat already prints death message if stamina hits 0
            return 'defeat'
        if monster['stamina'] <= 0:
            print(f"{monster['name']} ({monster['stamina']}W) został pokonany!")
            return 'victory'

        print("\n--- NOWA RUNDA WALKI ---")

        monster_attack_strength = roll_k6(2) + monster['dexterity']
        print(f"Siła Ataku Potwora ({monster['name']}): {monster_attack_strength} (2K6 + Z:{monster['dexterity']})")

        player_attack_strength = roll_k6(2) + player_character.stats['dexterity'] + temp_player_dex_bonus
        print(f"Twoja Siła Ataku: {player_attack_strength} (2K6 + Z:{player_character.stats['dexterity']})")

        if monster_attack_strength > player_attack_strength:
            print(f"Potwór ({monster_attack_strength}) trafia Ciebie ({player_attack_strength})!")
            damage_taken_initial = 2

            sss_choice = input("  Otrzymałeś obrażenia. Użyć SZCZĘŚCIA (SSS)? (tak/nie): ").strip().lower()
            actual_damage_taken = damage_taken_initial
            if sss_choice == 'tak' or sss_choice == 't':
                sss_result = perform_sss(player_character)
                if sss_result:
                    actual_damage_taken = 1
                    print("  Dzięki SZCZĘŚCIU, tracisz tylko 1 punkt Wytrzymałości w tej rundzie!")
                else:
                    actual_damage_taken = 3
                    print("  Pech! Tracisz dodatkowo 1 punkt Wytrzymałości (łącznie 3 punkty) w tej rundzie!")
            else:
                 print(f"  Tracisz {actual_damage_taken} punkty Wytrzymałości.")
            player_character.change_stat('stamina', -actual_damage_taken)

        elif player_attack_strength > monster_attack_strength:
            print(f"Ty ({player_attack_strength}) trafiasz potwora ({monster_attack_strength})!")
            damage_dealt_initial = 2

            sss_choice = input("  Zadałeś obrażenia. Użyć SZCZĘŚCIA (SSS)? (tak/nie): ").strip().lower()
            actual_damage_dealt = damage_dealt_initial
            if sss_choice == 'tak' or sss_choice == 't':
                sss_result = perform_sss(player_character)
                if sss_result:
                    actual_damage_dealt = 4
                    print(f"  Dzięki SZCZĘŚCIU, {monster['name']} traci dodatkowo 2 punkty Wytrzymałości (łącznie 4 punkty)!")
                else:
                    actual_damage_dealt = 1
                    print(f"  Pech! {monster['name']} traci tylko 1 punkt Wytrzymałości w tej rundzie.")
            else:
                print(f"  {monster['name']} traci {actual_damage_dealt} punkty Wytrzymałości.")
            monster['stamina'] -= actual_damage_dealt

        else:
            print("Remis! Siły ataku równe. Runda się powtarza.")
            print(f"Twoja Wytrzymałość: {player_character.stats['stamina']}, Wytrzymałość Potwora ({monster['name']}): {monster['stamina']}")
            time.sleep(1)
            continue

        print(f"Twoja Wytrzymałość: {player_character.stats['stamina']}, Wytrzymałość Potwora ({monster['name']}): {monster['stamina']}")

        if player_character.stats['stamina'] <= 0:
            return 'defeat'
        if monster['stamina'] <= 0:
            print(f"{monster['name']} ({monster['stamina']}W) został pokonany!")
            return 'victory'

        flee_choice_info = None
        for choice_data in current_paragraph_data.get('choices', []):
            choice_text = choice_data.get('text', '').lower()
            if "uciek" in choice_text and ("patrz" in choice_text or "idź do" in choice_text or "ucieczk" in choice_text):
                flee_choice_info = choice_data
                break

        if flee_choice_info:
            flee_prompt = input(f"  Możesz spróbować ucieczki (tekst wyboru: \"{flee_choice_info['text']}\"). Uciec? (tak/nie): ").strip().lower()
            if flee_prompt == 'tak' or flee_prompt == 't':
                penalty = 2
                print(f"Uciekasz! Tracisz {penalty} punkty Wytrzymałości za próbę ucieczki.")
                player_character.change_stat('stamina', -penalty)
                if player_character.stats['stamina'] <= 0:
                    return 'defeat'
                player_character.current_paragraph_id = flee_choice_info['target_paragraph_id']
                return 'fled'

        time.sleep(0.5)


def start_game():
    game_paragraphs = load_game_data()
    if not game_paragraphs:
        print("Błąd krytyczny: Nie udało się załadować danych gry. Koniec programu.")
        return

    player = PlayerCharacter()
    paragraph_allows_eating_current_turn = False

    while True:
        current_paragraph_data = get_paragraph(player.current_paragraph_id, game_paragraphs)

        if not current_paragraph_data:
            print(f"BŁĄD KRYTYCZNY: Nie znaleziono paragrafu o ID {player.current_paragraph_id}! Kończenie gry.")
            break

        print(f"\n\n======================================================")
        print(f"                     Paragraf {current_paragraph_data['id']}                     ")
        print(f"======================================================\n")
        # Word wrap paragraph text for better readability
        text_lines = current_paragraph_data['text'].split('\n')
        for line in text_lines:
            # Simple wrap for now, could use textwrap module for more sophistication
            words = line.split(' ')
            current_line_text = ""
            for word in words:
                if len(current_line_text) + len(word) + 1 > 70: # Approx console width
                    print(current_line_text)
                    current_line_text = word
                else:
                    current_line_text += (" " + word) if current_line_text else word
            if current_line_text:
                print(current_line_text)
        print(f"\n------------------------------------------------------")

        player.display_stats()

        paragraph_allows_eating_current_turn = False

        if current_paragraph_data.get('monster'):
            print(f"\n!!! W tym miejscu czai się {current_paragraph_data['monster']['name']}!")
            combat_prompt = input("Czy chcesz zaatakować? (tak/nie, 'nie' oznacza próbę zignorowania jeśli możliwe): ").strip().lower()
            if combat_prompt == 'tak' or combat_prompt == 't':
                combat_result = initiate_combat(player, current_paragraph_data['monster'], current_paragraph_data, game_paragraphs)

                if combat_result == 'defeat':
                    # Game over message is usually handled by player.change_stat or combat function
                    # if it prints "stamina spadla do 0...". Ensure a generic one if not.
                    if player.stats['stamina'] > 0 : print("\nZOSTAŁEŚ POKONANY!") # if not already dead by stamina loss
                    print("--- KONIEC GRY ---")
                    break
                elif combat_result == 'fled':
                    print(f"Uciekłeś do paragrafu {player.current_paragraph_id}.")
                    time.sleep(0.5) # Brief pause before showing next paragraph
                    continue
                elif combat_result == 'victory':
                    print(f"Pokonałeś {current_paragraph_data['monster']['name']}! Rozglądasz się co dalej...")
            else:
                print(f"Decydujesz się nie atakować {current_paragraph_data['monster']['name']} w tym momencie.")

        action_taken_by_event, game_should_end, paragraph_allows_eating_current_turn = handle_actions(
            player, current_paragraph_data.get('actions', []), current_paragraph_data, game_paragraphs
        )

        if game_should_end:
            # Message about stamina is usually printed by player.change_stat or combat
            if player.stats['stamina'] > 0 and not action_taken_by_event : # If not dead by stamina and action didn't specify exact end
                 print("\n--- Koniec przygody napotkany przez akcję ---")
            print("--- KONIEC GRY ---")
            break

        if action_taken_by_event:
            time.sleep(0.5)
            continue

        if not current_paragraph_data['choices']:
            print("\n--- Koniec przygody? (Brak dostępnych wyborów w tym paragrafie) ---")
            print("--- KONIEC GRY ---")
            break

        print("\n=== Dostępne opcje ===")
        actual_choices_for_display = current_paragraph_data['choices']
        for i, choice_data in enumerate(actual_choices_for_display):
            choice_text = choice_data.get('text', '')
            target_id = choice_data['target_paragraph_id']
            # If choice text is just a number, or seems like a direct reference.
            if not choice_text or choice_text.isdigit() or (choice_text.lower().startswith("patrz") and choice_text.replace("patrz","").strip().isdigit()):
                display_text = f"Idź do paragrafu {target_id}"
            else:
                # Clean up "Patrz XYZ" if it's part of a longer description
                display_text = re.sub(r'\s*-\s*patrz\s+\d+\s*\.?$', '', choice_text, flags=re.IGNORECASE).strip()
                display_text = re.sub(r'\s*patrz\s+\d+\s*\.?$', '', display_text, flags=re.IGNORECASE).strip()
                if not display_text: display_text = f"Przejdź do paragrafu {target_id}" # Fallback
            print(f"  {i+1}. {display_text.strip()}")

        general_actions_menu = {}
        current_choice_offset = len(actual_choices_for_display) + 1

        general_actions_menu[current_choice_offset] = {"text": "Użyj eliksiru", "action": "use_elixir"}
        print(f"  {current_choice_offset}. Użyj eliksiru")
        current_choice_offset +=1

        if paragraph_allows_eating_current_turn:
            general_actions_menu[current_choice_offset] = {"text": "Zjedz prowiant", "action": "eat_provision"}
            print(f"  {current_choice_offset}. Zjedz prowiant")
            current_choice_offset +=1

        general_actions_menu[current_choice_offset] = {"text": "Pokaż statystyki ponownie", "action": "display_stats"}
        print(f"  {current_choice_offset}. Pokaż statystyki ponownie")


        while True:
            try:
                user_input_str = input("Co robisz? Wybierz numer opcji: ").strip()
                if not user_input_str: continue

                choice_num = int(user_input_str)

                num_paragraph_choices = len(actual_choices_for_display)

                if 1 <= choice_num <= num_paragraph_choices:
                    selected_choice_data = actual_choices_for_display[choice_num - 1]
                    player.current_paragraph_id = selected_choice_data['target_paragraph_id']
                    break
                elif choice_num in general_actions_menu:
                    chosen_general_action_key = general_actions_menu[choice_num]["action"]

                    if chosen_general_action_key == "use_elixir":
                        player.use_elixir()
                    elif chosen_general_action_key == "eat_provision":
                        if paragraph_allows_eating_current_turn:
                             player.eat_provision()
                        else:
                             print("W tym momencie nie możesz zjeść prowiantu (tekst paragrafu na to nie zezwala).")
                    elif chosen_general_action_key == "display_stats":
                        player.display_stats()

                    # Re-list choices for the current paragraph as these actions don't change paragraph
                    print("\n=== Dostępne opcje po akcji ===")
                    for i, choice_data_rep in enumerate(actual_choices_for_display):
                        choice_text_rep = choice_data_rep.get('text', '')
                        target_id_rep = choice_data_rep['target_paragraph_id']
                        if not choice_text_rep or choice_text_rep.isdigit() or (choice_text_rep.lower().startswith("patrz") and choice_text_rep.replace("patrz","").strip().isdigit()):
                            display_text_rep = f"Idź do paragrafu {target_id_rep}"
                        else:
                            display_text_rep = re.sub(r'\s*-\s*patrz\s+\d+\s*\.?$', '', choice_text_rep, flags=re.IGNORECASE).strip()
                            display_text_rep = re.sub(r'\s*patrz\s+\d+\s*\.?$', '', display_text_rep, flags=re.IGNORECASE).strip()
                            if not display_text_rep: display_text_rep = f"Przejdź do paragrafu {target_id_rep}"
                        print(f"  {i+1}. {display_text_rep.strip()}")

                    temp_offset_display = len(actual_choices_for_display) + 1
                    for gm_key_display in sorted(general_actions_menu.keys()):
                        if gm_key_display >= temp_offset_display:
                             print(f"  {gm_key_display}. {general_actions_menu[gm_key_display]['text']}")
                    continue
                else:
                    print(f"Nieprawidłowy wybór. Wpisz numer z listy dostępnych opcji.")
            except ValueError:
                print("Nieprawidłowe dane. Proszę wpisać numer opcji.")

        if player.stats['stamina'] <= 0:
            if not game_should_end :
                 # This message might be redundant if already printed by combat or action handler
                 # print("\nTwoja Wytrzymałość spadła do zera lub poniżej...")
                 print("--- KONIEC GRY ---")
            break

if __name__ == '__main__':
    pass
