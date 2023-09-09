import pygame
import json
import os
from colorama import Fore

# /// initiators
game_state_exists = None
potion = None
count = 0  # Counter
potion_count = 2  # num of potions
choice_count = 0  # num of choices (universal)
gold_amount = 0  # initial gold amount
player_name = None  # Player's name
init_round_count = 0  # Initial num of rounds
round_count = 0  # Round counter
s_count = s_init = 0  # Action points counter: luck
w_count = w_init = 0  # Action points counter: stamina
z_count = z_init = 0  # Action points counter: dexterity
init_eatables_count = eatables_count = 8  # Initial number of meals
eatable_W_load = 4  # How many load of stamina in one meal

# /// constants
and_his_name_is = '''
        ZZZZZZZ    BBBBBB       YYY     YYY     SSSSSS      ZZZZZZZZ      K     K     OOOOO     
              Z     B     B      YYY   YYY     S                  Z       K    K     O     O    
             Z      B     B       YYY YYY       SSS              Z        K   K     O       O    
            Z       BBBBBB         YYYYY             S          Z          KKK      O       O    
          Z         B     B         YYY            SSSS        Z          K   K     O       O    
         Z          B     B         YYY              S        Z           K    K     O     O    
        ZZZZZZZ    BBBBBB           YYY        SSSSSS        ZZZZZZZZ     K     K     OOOOO     
        '''
input_sign = '>>> '  # sign indicating that the user should provide an input
delay = 0.2  # time delay in seconds between printing each character in text
entity_hit_mult = 1  # multiplier for entity level (default level is '1')
p_mult = 1  # player multiplier for damage calculation
p_hit_val_ = -2 * entity_hit_mult - 100  # player hit value (-100 for development only)
e_hit_val_ = -2 * entity_hit_mult  # enemy hit value
def_txt_clr = Fore.LIGHTWHITE_EX  # default text color
entity_txt_clr = Fore.LIGHTRED_EX  # color for entities
special_txt_clr = Fore.LIGHTMAGENTA_EX  # color for headlines and particular special texts
combat_txt_clr = Fore.LIGHTCYAN_EX  # color for combat text
debug_txt_clr = Fore.LIGHTBLACK_EX  # color for debug messages
error_txt_clr = Fore.RED  # color for error messages
root_dir = "Assets\\"

setup_name = rf"{root_dir}\_json_\setup.json"  # Get the setup script's name and or location

# /// pygame mixer setup
# Initialize the mixer module with the specified settings
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=2 ** 12)

# /// equipment list

# main equipment
main_eq = {"plecak na Prowiant": "",
           "prowiant": eatables_count,
           "tarcza": "",
           "miecz": "",
           }

# /// dictionaries
choices_115 = {'Miecz': '_232()',
               'Kościany kordelas': '_324()',
               'Rękawice': '_95()',
               'Tarcza': '_37()',
               'Hełm': '_298()',
               'Młot': '_324()',
               }

difficulty = 1  # default value
difficulty_levels = {"easy": 1, "medium": 1.3, "hard": 1.6}

# declare empty params
setup_params = {
    param: None for param in [
        "active_gameplay",
        "translation",
        "difficulty",
        "action_volume",
        "sfx_volume",
        "bckg_volume",
        "dev_mode",
        "debug_msg",
        "use_dummy",
        "start_sequence",
        "manual_battle",
        "dubbing",
        "get_music",
        "ver_num",
        "logging"
    ]
}


def setup():
    """
    /// SETUP ///

    The code defines and loads various setup parameters for a game from a JSON file.

    The loaded parameters include:

    active_gameplay: bool
        Stores the localization of the active game state file.

    translation: str
        Stores the translation setting.

    dev_mode: bool
        Enables exclusive mechanics while playing and additional debug information.

    debug_msg: bool
        Enables debug messages in between gameplay.

    use_dummy: bool
        Enables the use of dummy player and dummy data for testing purposes.

    start_sequence: bool
        Determines if the start sequence should be shown.

    manual_battle: bool
        If False, allows input of "a" and "b" values during combat round.

    category: str
        Stores the category information.

    allow_dialog_skipping: bool
        Determines whether dubbing will be skipped.

    get_music: bool
        Determines whether music playing is enabled.

    ver_num: str
        Stores the version number.

    difficulty: str
        Holds value used in combat mechanics as enemy hit multiplyer

    The setup data is loaded from the JSON file specified by the setup_name variable located in the ///PATHS section above.
    The values are assigned to their respective variables using the get() method of the loaded_setup dictionary.
    """

    # load setup data from json file
    with open(setup_name, "r") as f:
        loaded_setup = json.load(f)

    # assign values from loaded_setup to setup_params dictionary
    for param in setup_params:
        setup_params[param] = loaded_setup.get(param)

    # unpack setup_params dictionary into individual variables (optional)
    globals().update(setup_params)

    return loaded_setup


loaded_setup = setup()

paths_doc = """
/// PATHS
This section contains path definitions and lists of audio files used in the game.

Paths:
- assets_audio_effects_pth: Path to the directory containing sound effects.
- assets_audio_music_pth: Path to the directory containing music files.
- game_state_dir_name: Name of the directory used for game state saves.
- setup_name: Name of the setup script file.

/// Music Lists
- music_combat: List of music tracks used in combat.
- music_main: List of main music tracks.
- music_menu: List of menu music tracks.
"""

assets_audio_voice_pth = rf"{root_dir}Audio\Voice"  # Path to voice lines audio files
assets_audio_effects_pth = rf"{root_dir}Audio\fx"  # Path to sound effects
assets_audio_music_pth = fr"{root_dir}Audio\music"  # Path to music
game_state_dir_name = "dreszcz\\saves"  # Path to game_states/saves

audio_ext = '.mp3'  # extension of voice and fx files

# /// music lists
# create lists of existing files within given categories
music_categories = ['menu', 'main', 'combat']
music_tracks = {}

"""
If 'get_music' is set to True in 'setup_params', this code initializes a dictionary called 'music_tracks'.
It then iterates through 'music_categories' and, for each category, finds and stores the file paths of music tracks
located in the corresponding category folder within the 'assets_audio_music_pth' directory.
The music tracks are organized by category in the 'music_tracks' dictionary.
"""

if setup_params['get_music']:
    for category in music_categories:
        category_path = os.path.join(assets_audio_music_pth, category)
        music_tracks[category] = []

        for filename in os.listdir(category_path):
            file_path = os.path.join(category_path, filename)
            if os.path.isfile(file_path):
                music_tracks[category].append(file_path)
