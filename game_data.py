import json

def load_game_data(filepath="parsed_game_data.json"):
    """
    Reads the JSON file and returns the list of paragraph objects.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            game_data = json.load(f)
        # Ensure all paragraph IDs are integers for consistent lookup
        for paragraph in game_data:
            if isinstance(paragraph.get('id'), str):
                try:
                    paragraph['id'] = int(paragraph['id'])
                except ValueError:
                    print(f"Warning: Could not convert paragraph ID '{paragraph['id']}' to int.")
        return game_data
    except FileNotFoundError:
        print(f"Error: Game data file not found at {filepath}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}")
        return []

def get_paragraph(paragraph_id, game_data):
    """
    Retrieves a specific paragraph by its ID from the loaded data.
    Handles integer or string IDs from the input `paragraph_id`.
    """
    try:
        # Attempt to convert incoming paragraph_id to int for comparison,
        # as we've standardized IDs in game_data to integers during load.
        lookup_id = int(paragraph_id)
    except ValueError:
        print(f"Warning: Invalid paragraph_id format: {paragraph_id}. Must be convertible to an integer.")
        return None

    for paragraph in game_data:
        if paragraph.get('id') == lookup_id:
            return paragraph
    return None

if __name__ == '__main__':
    # Example Usage
    data = load_game_data()
    if data:
        print(f"Loaded {len(data)} paragraphs.")
        para_1 = get_paragraph(1, data)
        if para_1:
            print(f"\nParagraph 1: {para_1['text'][:50]}...")
        else:
            print("Paragraph 1 not found.")

        para_387 = get_paragraph("387", data) # Test with string ID
        if para_387:
            print(f"\nParagraph 387: {para_387['text'][:50]}...")
        else:
            print("Paragraph 387 not found.")

        non_existent = get_paragraph(999, data)
        if not non_existent:
            print("\nCorrectly did not find paragraph 999.")
    else:
        print("Failed to load game data.")
