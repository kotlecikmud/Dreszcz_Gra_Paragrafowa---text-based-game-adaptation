import unittest
from unittest.mock import patch
import os
import shutil
import pickle
from ai_rework.game_io import save_game, load_game, SAVE_FILE_NAME
from ai_rework.player import PlayerCharacter # For type checking and instantiation

class TestGameIO(unittest.TestCase):

    def setUp(self):
        # Create a temporary test profile directory
        self.test_profile_dir = "temp_test_profile_for_io"
        os.makedirs(self.test_profile_dir, exist_ok=True)

        # Create a PlayerCharacter instance for testing
        # We need to mock input for elixir choice if is_new_character=True
        with patch('builtins.input', side_effect=['Z']): # Mock input to choose 'Z' for elixir
            self.player = PlayerCharacter(is_new_character=True)
        
        # Manually set some predictable values for easier assertion after load
        self.player.current_paragraph_id = 5
        self.player.stats['stamina'] = 15
        self.player.gold = 50

    def tearDown(self):
        # Remove the temporary test profile directory
        if os.path.exists(self.test_profile_dir):
            shutil.rmtree(self.test_profile_dir)

    def test_save_game_new(self):
        self.assertTrue(save_game(self.player, self.test_profile_dir))
        save_file_path = os.path.join(self.test_profile_dir, SAVE_FILE_NAME)
        self.assertTrue(os.path.exists(save_file_path))
        self.assertTrue(os.path.getsize(save_file_path) > 0)

    def test_save_game_error_profile_path(self):
        invalid_path = "non_existent_test_profile_path_for_io"
        self.assertFalse(save_game(self.player, invalid_path))

    def test_load_game_exists(self):
        # First, save the game
        save_game(self.player, self.test_profile_dir)
        
        # Now, load it
        loaded_player = load_game(self.test_profile_dir)
        self.assertIsNotNone(loaded_player)
        self.assertIsInstance(loaded_player, PlayerCharacter)
        
        # Compare some attributes
        self.assertEqual(loaded_player.current_paragraph_id, self.player.current_paragraph_id)
        self.assertEqual(loaded_player.stats['stamina'], self.player.stats['stamina'])
        self.assertEqual(loaded_player.gold, self.player.gold)
        self.assertEqual(loaded_player.elixir_type, self.player.elixir_type) # Elixir type chosen via mocked input
        self.assertEqual(loaded_player.inventory, self.player.inventory)


    def test_load_game_not_exists(self):
        # Attempt to load from a profile where no save file exists
        self.assertIsNone(load_game(self.test_profile_dir))

    def test_load_game_corrupted_file_empty(self):
        save_file_path = os.path.join(self.test_profile_dir, SAVE_FILE_NAME)
        # Create an empty save file
        with open(save_file_path, 'wb') as f:
            pass # Empty file
        
        loaded_player = load_game(self.test_profile_dir)
        self.assertIsNone(loaded_player)
        # Optionally, check for specific error print, but that's more complex.
        # The function itself prints errors, test focuses on return value.

    def test_load_game_corrupted_file_malformed(self):
        save_file_path = os.path.join(self.test_profile_dir, SAVE_FILE_NAME)
        # Create a malformed save file (not valid pickle format)
        with open(save_file_path, 'wb') as f:
            f.write(b"this is not pickle data")
        
        loaded_player = load_game(self.test_profile_dir)
        self.assertIsNone(loaded_player)

    def test_save_load_with_changed_player_state(self):
        # Modify player state after initial setup
        self.player.current_paragraph_id = 101
        self.player.stats['luck'] = 3
        self.player.inventory.append("magiczny klucz")
        self.player.provisions -=1

        self.assertTrue(save_game(self.player, self.test_profile_dir))
        loaded_player = load_game(self.test_profile_dir)
        
        self.assertIsNotNone(loaded_player)
        self.assertEqual(loaded_player.current_paragraph_id, 101)
        self.assertEqual(loaded_player.stats['luck'], 3)
        self.assertIn("magiczny klucz", loaded_player.inventory)
        self.assertEqual(loaded_player.provisions, self.player.provisions)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
