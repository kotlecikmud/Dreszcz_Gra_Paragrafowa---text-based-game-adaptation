import unittest
import os
import shutil
import json
from ai_rework import profiles # Import the module directly to modify its globals

# Store original PROFILES_DIR and PROFILES_METADATA_FILE to restore them later
ORIG_PROFILES_DIR = profiles.PROFILES_DIR
ORIG_PROFILES_METADATA_FILE = profiles.PROFILES_METADATA_FILE

class TestProfiles(unittest.TestCase):

    def setUp(self):
        # Create a temporary test directory for profiles
        self.test_dir = "temp_test_profiles_dir"
        os.makedirs(self.test_dir, exist_ok=True)

        # Override global variables in the profiles module
        profiles.PROFILES_DIR = self.test_dir
        profiles.PROFILES_METADATA_FILE = os.path.join(self.test_dir, "test_profiles.json")

    def tearDown(self):
        # Restore original global variables in the profiles module
        profiles.PROFILES_DIR = ORIG_PROFILES_DIR
        profiles.PROFILES_METADATA_FILE = ORIG_PROFILES_METADATA_FILE
        
        # Remove the temporary test directory and its contents
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_create_profile_new(self):
        profile_name = "test_user_1"
        self.assertTrue(profiles.create_profile(profile_name))
        profile_path = os.path.join(self.test_dir, profile_name)
        self.assertTrue(os.path.isdir(profile_path))
        
        loaded_data = profiles.load_profiles()
        self.assertIn(profile_name, loaded_data)
        self.assertEqual(loaded_data[profile_name]["path"], profile_path)
        self.assertEqual(loaded_data[profile_name]["name"], profile_name)

    def test_create_profile_existing(self):
        profile_name = "test_user_2"
        profiles.create_profile(profile_name) # Create it once
        self.assertFalse(profiles.create_profile(profile_name)) # Try to create again

    def test_create_profile_invalid_name_empty(self):
        self.assertFalse(profiles.create_profile("")) # Empty name
    
    def test_create_profile_invalid_name_spaces(self):
        self.assertFalse(profiles.create_profile("   ")) # Just spaces

    def test_create_profile_sanitized(self):
        profile_name = "Test User/\\:*?\"<>|3"
        sanitized_name = "Test User3"
        self.assertTrue(profiles.create_profile(profile_name))
        profile_path = os.path.join(self.test_dir, sanitized_name)
        self.assertTrue(os.path.isdir(profile_path))
        loaded_data = profiles.load_profiles()
        self.assertIn(sanitized_name, loaded_data)

    def test_load_profiles_no_file(self):
        # Ensure the metadata file does not exist
        if os.path.exists(profiles.PROFILES_METADATA_FILE):
            os.remove(profiles.PROFILES_METADATA_FILE)
        self.assertEqual(profiles.load_profiles(), {})

    def test_load_profiles_empty_file(self):
        # Create an empty metadata file
        with open(profiles.PROFILES_METADATA_FILE, 'w') as f:
            pass # Just create it empty
        self.assertEqual(profiles.load_profiles(), {})

    def test_load_profiles_invalid_json_file(self):
        # Create an invalid JSON metadata file
        with open(profiles.PROFILES_METADATA_FILE, 'w') as f:
            f.write("{invalid_json_}")
        self.assertEqual(profiles.load_profiles(), {})

    def test_load_profiles_valid(self):
        profile_name1 = "user_a"
        profile_name2 = "user_b"
        profiles.create_profile(profile_name1)
        profiles.create_profile(profile_name2)
        
        loaded_data = profiles.load_profiles()
        self.assertIn(profile_name1, loaded_data)
        self.assertIn(profile_name2, loaded_data)
        self.assertEqual(loaded_data[profile_name1]["path"], os.path.join(self.test_dir, profile_name1))

    def test_select_profile_exists(self):
        profile_name = "select_test_user"
        profiles.create_profile(profile_name)
        loaded_data = profiles.load_profiles()
        
        expected_path = os.path.join(self.test_dir, profile_name)
        self.assertEqual(profiles.select_profile(profile_name, loaded_data), expected_path)

    def test_select_profile_not_exists(self):
        loaded_data = profiles.load_profiles() # Should be empty or from other tests
        self.assertIsNone(profiles.select_profile("non_existent_user", loaded_data))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
