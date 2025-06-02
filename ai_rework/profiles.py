import os
import json

PROFILES_DIR = "profiles"
PROFILES_METADATA_FILE = os.path.join(PROFILES_DIR, "profiles.json")

def load_profiles() -> dict:
    """
    Reads the profiles.json metadata file.
    Returns a dictionary of existing profiles (e.g., {"profile_name": {"path": "path/to/profile_dir"}}).
    Returns an empty dict if the file doesn't exist or is invalid.
    """
    if not os.path.exists(PROFILES_METADATA_FILE):
        return {}
    try:
        with open(PROFILES_METADATA_FILE, 'r') as f:
            profiles_data = json.load(f)
        return profiles_data
    except (json.JSONDecodeError, IOError):
        return {}

def create_profile(profile_name: str) -> bool:
    """
    Checks if a profile with profile_name already exists.
    If not, creates a directory for the profile (e.g., profiles/<profile_name>).
    Creates/updates profiles.json to store profile metadata.
    Returns True if successful, False otherwise.
    """
    if not profile_name or not profile_name.strip():
        print("Error: Profile name cannot be empty.")
        return False
    
    sanitized_profile_name = "".join(c for c in profile_name if c.isalnum() or c in (' ', '_', '-')).strip()
    if not sanitized_profile_name:
        print("Error: Profile name contains invalid characters or is empty after sanitization.")
        return False

    profiles_data = load_profiles()

    if sanitized_profile_name in profiles_data:
        print(f"Error: Profile '{sanitized_profile_name}' already exists.")
        return False

    profile_dir = os.path.join(PROFILES_DIR, sanitized_profile_name)

    try:
        os.makedirs(PROFILES_DIR, exist_ok=True) # Ensure base profiles directory exists
        os.makedirs(profile_dir, exist_ok=True) # Create profile-specific directory

        profiles_data[sanitized_profile_name] = {"path": profile_dir, "name": sanitized_profile_name}
        
        with open(PROFILES_METADATA_FILE, 'w') as f:
            json.dump(profiles_data, f, indent=4)
        
        print(f"Profile '{sanitized_profile_name}' created successfully at '{profile_dir}'.")
        return True
    except IOError as e:
        print(f"Error creating profile: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def select_profile(profile_name: str, profiles_data: dict) -> str | None:
    """
    Checks if profile_name exists in profiles_data.
    Returns the path to the profile directory if it exists, otherwise None.
    """
    profile_info = profiles_data.get(profile_name)
    if profile_info and "path" in profile_info:
        return profile_info["path"]
    return None

if __name__ == '__main__':
    # Simple test cases
    print("--- Testing Profile System ---")

    # Clean up before test
    if os.path.exists(PROFILES_METADATA_FILE):
        os.remove(PROFILES_METADATA_FILE)
    if os.path.exists(os.path.join(PROFILES_DIR, "test_user_1")):
        os.rmdir(os.path.join(PROFILES_DIR, "test_user_1"))
    if os.path.exists(os.path.join(PROFILES_DIR, "Test User 2")):
        os.rmdir(os.path.join(PROFILES_DIR, "Test User 2"))
    if os.path.exists(PROFILES_DIR) and not os.listdir(PROFILES_DIR):
         os.rmdir(PROFILES_DIR)


    print("\n1. Initial load (no profiles.json):")
    loaded = load_profiles()
    print(f"Loaded profiles: {loaded}")
    assert loaded == {}

    print("\n2. Create profile 'test_user_1':")
    result1 = create_profile("test_user_1")
    print(f"Creation result: {result1}")
    assert result1 is True
    assert os.path.exists(os.path.join(PROFILES_DIR, "test_user_1"))

    print("\n3. Load profiles again:")
    loaded = load_profiles()
    print(f"Loaded profiles: {loaded}")
    assert "test_user_1" in loaded
    assert loaded["test_user_1"]["path"] == os.path.join(PROFILES_DIR, "test_user_1")

    print("\n4. Try to create existing profile 'test_user_1':")
    result2 = create_profile("test_user_1")
    print(f"Creation result: {result2}")
    assert result2 is False

    print("\n5. Create profile 'Test User 2' (with space):")
    result3 = create_profile("Test User 2")
    print(f"Creation result: {result3}")
    assert result3 is True
    assert os.path.exists(os.path.join(PROFILES_DIR, "Test User 2"))
    
    loaded = load_profiles()
    print(f"Loaded profiles: {loaded}")
    assert "Test User 2" in loaded

    print("\n6. Select 'test_user_1':")
    path1 = select_profile("test_user_1", loaded)
    print(f"Path for 'test_user_1': {path1}")
    assert path1 == os.path.join(PROFILES_DIR, "test_user_1")

    print("\n7. Select 'NonExistentUser':")
    path2 = select_profile("NonExistentUser", loaded)
    print(f"Path for 'NonExistentUser': {path2}")
    assert path2 is None

    print("\n8. Create profile with invalid chars '!@#$%^&*()':")
    result_invalid = create_profile("!@#$%^&*()")
    print(f"Creation result for invalid: {result_invalid}")
    assert result_invalid is False # Sanitized name becomes empty

    print("\n9. Create profile with only spaces '   ':")
    result_spaces = create_profile("   ")
    print(f"Creation result for spaces: {result_spaces}")
    assert result_spaces is False


    print("\n--- Testing Complete ---")
    # Clean up after test
    if os.path.exists(PROFILES_METADATA_FILE):
        os.remove(PROFILES_METADATA_FILE)
    if os.path.exists(os.path.join(PROFILES_DIR, "test_user_1")):
        os.rmdir(os.path.join(PROFILES_DIR, "test_user_1"))
    if os.path.exists(os.path.join(PROFILES_DIR, "Test User 2")):
        os.rmdir(os.path.join(PROFILES_DIR, "Test User 2"))
    if os.path.exists(PROFILES_DIR) and not os.listdir(PROFILES_DIR):
         os.rmdir(PROFILES_DIR)

    # To run this test block:
    # Ensure this file is in ai_rework/profiles.py
    # Navigate to the directory containing ai_rework (e.g., your project root)
    # Run: python -m ai_rework.profiles
    # You might need to adjust PYTHONPATH or run as a module if imports fail.
    # Example: PYTHONPATH=. python ai_rework/profiles.py
    # (This structure assumes PROFILES_DIR is relative to where profiles.py is,
    # or where the main script calling it resides if paths are not absolute)
    # For the main.py integration, PROFILES_DIR will be relative to the project root.
    # The test block uses paths relative to where profiles.py is executed.
    # If profiles.py is in ai_rework/, then PROFILES_DIR="profiles" means "ai_rework/profiles/".
    # This should be fine for module usage.
    # When main.py (presumably in ai_rework/ or project root) calls these,
    # PROFILES_DIR needs to be relative to main.py's location or be an absolute path.
    # For simplicity, keeping PROFILES_DIR = "profiles" implies it's in the current working directory
    # where the main script is run.
    # So, if main.py is in project_root/ and calls functions from ai_rework/profiles.py,
    # "profiles" directory will be project_root/profiles/.

    # Final check on PROFILES_DIR location:
    # If main.py is in /app/ and it imports ai_rework.profiles,
    # and profiles.py defines PROFILES_DIR = "profiles",
    # then the "profiles" directory will be created/searched in /app/profiles/.
    # This is the desired behavior.
    pass
