import pickle
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .player import PlayerCharacter # For type hinting to avoid circular imports

SAVE_FILE_NAME = "savegame.dat"

def save_game(player_character_instance: 'PlayerCharacter', profile_path: str) -> bool:
    """
    Saves the PlayerCharacter instance to a file within the profile directory.

    Args:
        player_character_instance: The instance of PlayerCharacter to save.
        profile_path: The directory path of the active profile.

    Returns:
        True if saving was successful, False otherwise.
    """
    if not os.path.isdir(profile_path):
        print(f"Error: Profile path '{profile_path}' is not a valid directory.")
        return False

    save_file_path = os.path.join(profile_path, SAVE_FILE_NAME)

    try:
        # Serialize the player character instance to bytes
        game_data_bytes = pickle.dumps(player_character_instance)
        
        # Write the bytes to the save file
        with open(save_file_path, "wb") as f:
            f.write(game_data_bytes)
        
        print(f"Gra zapisana pomyślnie w '{save_file_path}'.")
        return True
    except pickle.PicklingError as e:
        print(f"Błąd podczas serializacji danych gry: {e}")
        return False
    except IOError as e:
        print(f"Błąd wejścia/wyjścia podczas zapisu gry: {e}")
        return False
    except Exception as e:
        print(f"Niespodziewany błąd podczas zapisu gry: {e}")
        return False

def load_game(profile_path: str) -> 'PlayerCharacter | None':
    """
    Loads a PlayerCharacter instance from a save file within the profile directory.

    Args:
        profile_path: The directory path of the active profile.

    Returns:
        The deserialized PlayerCharacter object if successful, None otherwise.
    """
    if not os.path.isdir(profile_path):
        # This check might be redundant if profile_path is always validated before call
        print(f"Error: Profile path '{profile_path}' for loading is not a valid directory.")
        return None

    save_file_path = os.path.join(profile_path, SAVE_FILE_NAME)

    if not os.path.exists(save_file_path):
        # print(f"Brak zapisanego stanu gry w '{save_file_path}'.") # Optional: main.py might handle this
        return None

    try:
        with open(save_file_path, "rb") as f:
            game_data_bytes = f.read()
        
        player_character_instance = pickle.loads(game_data_bytes)
        print(f"Gra wczytana pomyślnie z '{save_file_path}'.")
        return player_character_instance
    except FileNotFoundError: # Should be caught by os.path.exists, but good for robustness
        # print(f"Brak zapisanego stanu gry w '{save_file_path}'.")
        return None
    except (pickle.UnpicklingError, EOFError) as e:
        print(f"Błąd podczas deserializacji danych gry (plik może być uszkodzony lub pusty): {e}")
        return None
    except IOError as e:
        print(f"Błąd wejścia/wyjścia podczas wczytywania gry: {e}")
        return None
    except Exception as e:
        print(f"Niespodziewany błąd podczas wczytywania gry: {e}")
        return None

if __name__ == '__main__':
    # Example Usage (requires a dummy PlayerCharacter and a profile directory)
    # Note: To test load_game properly, you need a PlayerCharacter class defined
    # or the dummy class needs to be known to pickle (e.g. defined globally in this script)
    # For this test, DummyPlayerCharacter is defined locally, which works for pickle if saved/loaded by same script.
    # If PlayerCharacter from player.py is used, ensure PYTHONPATH allows finding ai_rework.player

    # Dummy PlayerCharacter for testing
    class DummyPlayerCharacter:
        def __init__(self, name="TestPlayer", health=100):
            self.name = name
            self.health = health
            self.inventory = ["miecz", "tarcza"]
            self.current_paragraph_id = 10
            self.stats = {'dexterity': 10, 'stamina': 12, 'luck': 8}
            self.initial_stats = self.stats.copy()
            self.elixir_type = "ZRĘCZNOŚCI"
            self.elixir_uses_left = 1
            self.provisions = 5
            self.gold = 20


    print("--- Test game_io.save_game & game_io.load_game ---")
    
    # Create a dummy profile directory for testing
    test_profile_dir = os.path.join("profiles", "test_dummy_profile_io") # Make path os-agnostic
    if not os.path.exists(test_profile_dir):
        os.makedirs(test_profile_dir, exist_ok=True)

    dummy_player = DummyPlayerCharacter()
    print(f"Utworzono testowego gracza: {dummy_player.name}")

    # Test successful save
    print("\n1. Test poprawnego zapisu:")
    success = save_game(dummy_player, test_profile_dir)
    print(f"Wynik zapisu: {success}")
    assert success is True
    assert os.path.exists(os.path.join(test_profile_dir, SAVE_FILE_NAME))
    print(f"Plik zapisu powinien istnieć w '{os.path.join(test_profile_dir, SAVE_FILE_NAME)}'")

    # Test save with invalid profile path
    print("\n2. Test zapisu z nieprawidłową ścieżką profilu:")
    invalid_profile_dir = "profiles/non_existent_profile_XYZ"
    success_invalid_path = save_game(dummy_player, invalid_profile_dir)
    print(f"Wynik zapisu (nieprawidłowa ścieżka): {success_invalid_path}")
    assert success_invalid_path is False

    # Test pickling error (hard to simulate directly without a non-pickleable object)
    # For now, this test is conceptual. If PlayerCharacter had non-pickleable parts, it would fail.
    print("\n3. Test błędu serializacji (konceptualny):")
    # To truly test this, you'd need 'dummy_player_unpickleable' with e.g. a lambda or local class instance.
    # class Unpickleable: __slots__ = ['data']; def __init__(self): self.data = lambda: None
    # dummy_player_unpickleable = DummyPlayerCharacter()
    # dummy_player_unpickleable.unpickleable_attr = Unpickleable()
    # success_pickle_error = save_game(dummy_player_unpickleable, test_profile_dir)
    # print(f"Wynik zapisu (błąd serializacji): {success_pickle_error}")
    # assert success_pickle_error is False
    print("   (Symulacja błędu serializacji wymagałaby obiektu niemożliwego do spicklowania)")

    print("\n4. Test poprawnego wczytania:")
    if success: # Only try to load if save was successful
        loaded_player = load_game(test_profile_dir)
        print(f"Wynik wczytania: {'Sukces' if loaded_player else 'Porażka'}")
        assert loaded_player is not None
        if loaded_player:
            assert loaded_player.name == dummy_player.name
            assert loaded_player.health == dummy_player.health
            assert loaded_player.inventory == dummy_player.inventory
            assert loaded_player.current_paragraph_id == dummy_player.current_paragraph_id
            print(f"Wczytany gracz: {loaded_player.name}, Zdrowie: {loaded_player.health}, Paragraf: {loaded_player.current_paragraph_id}")

    print("\n5. Test wczytania z nieistniejącego pliku (nowy profil):")
    new_profile_dir = os.path.join("profiles", "test_new_profile_io")
    if not os.path.exists(new_profile_dir):
        os.makedirs(new_profile_dir, exist_ok=True)
    loaded_player_new = load_game(new_profile_dir)
    print(f"Wynik wczytania (nowy profil): {'Brak zapisu (oczekiwane)' if loaded_player_new is None else 'Błąd'}")
    assert loaded_player_new is None
    if os.path.exists(new_profile_dir) and not os.listdir(new_profile_dir): # Cleanup new_profile_dir if empty
        os.rmdir(new_profile_dir)


    print("\n--- Testy zakończone ---")
    
    # Clean up test save file and directory
    test_save_file = os.path.join(test_profile_dir, SAVE_FILE_NAME)
    if os.path.exists(test_save_file):
        os.remove(test_save_file)
    
    # Attempt to remove directories only if they exist and are empty
    for dir_path in [test_profile_dir, new_profile_dir]:
        if os.path.exists(dir_path) and not os.listdir(dir_path):
            try:
                os.rmdir(dir_path)
            except OSError as e:
                print(f"Could not remove {dir_path}: {e}")

    profiles_base_dir = "profiles"
    if os.path.exists(profiles_base_dir) and not os.listdir(profiles_base_dir):
        try:
            os.rmdir(profiles_base_dir)
        except OSError as e:
             print(f"Could not remove {profiles_base_dir}: {e}") # Might fail if other tests from profiles.py left things
    pass
