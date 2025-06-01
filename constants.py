import os
import json
import pygame
import subprocess
from colorama import Fore

"""
/// PATHS
This section contains path definitions and lists of audio files used in the game.

Paths:
- ASSETS_DIR: Main directory where assets and game files are stored.
- GAME_FILES_DIR: Directory for game-specific files within the root directory.
- LOG_NAME: Path to the log file for recording game logs.
- CFG_NAME: Path to the setup script file.
- DUMMY_GAMESTATE_NAME: Path to the dummy game state file.
- AUDIO_VOICE_DIR: Directory containing voice lines audio files.
- AUDIO_FX_DIR: Directory containing sound effects audio files.
- AUDIO_MUSIC_DIR: Directory containing music audio files.
- GAMESTATE_DIR: Directory for storing game state saves.
- AUDIO_EXTENSION: Extension used for audio files.
"""

# extensions
GAMESTATE_EXTENSION = ".gmsf"
AUDIO_EXTENSION = '.mp3'  # extension of voice and fx files, other will be ignored

# directories
ASSETS_DIR = "Assets"
GAME_FILES_DIR = os.path.join(ASSETS_DIR, "game_files")
AUDIO_ASSETS_DIR = os.path.join(ASSETS_DIR, "Audio")  # Path to audio assets
GRAPHICS_ASSETS_DIR = os.path.join(ASSETS_DIR, "Graphics")  # Path to graphics assets
GRAPHICS_MISC_DIR = os.path.join(GRAPHICS_ASSETS_DIR, "misc")  # Path to misc graphics like icons, buttons etc.
GRAPHICS_PLATES_DIR = os.path.join(GRAPHICS_ASSETS_DIR, "plates")  # Path to background graphics
AUDIO_VOICE_DIR = os.path.join(AUDIO_ASSETS_DIR, "voice")  # Path to voice lines audio files
AUDIO_FX_DIR = os.path.join(AUDIO_ASSETS_DIR, "fx")  # Path to sound effects
AUDIO_MUSIC_DIR = os.path.join(AUDIO_ASSETS_DIR, "music")  # Path to music
DOCUMENTATION_DIR = os.path.join(ASSETS_DIR, "Documentation")  # Path to documentation of project
# For GAMESTATE_DIR, os.path.expanduser already handles '~' correctly.
# The subdirectory part should also use os.path.join for consistency if it were multi-level.
# However, "Jacek Ciesielski - Dreszcz\saves" is a single component here after expansion.
# For full cross-platform compatibility, if user's home might not be on a drive supporting backslashes (unlikely for Documents),
# this could be made more robust, but it's often fine as is for typical desktop systems.
GAMESTATE_DIR = os.path.join(os.path.expanduser('~'), "Documents", "Jacek Ciesielski - Dreszcz", "saves") # Path for managings gamestate (gmsf) files

# paths
LOG_NAME = os.path.join(GAME_FILES_DIR, ".log")
CFG_NAME = os.path.join(GAME_FILES_DIR, "config.json")
VER_FILE = os.path.join(GAME_FILES_DIR, ".ver")
CHLOG_NAME = os.path.join(GAME_FILES_DIR, "changelog.json")
DUMMY_GAMESTATE_NAME = os.path.join(GAMESTATE_DIR, f"dreszcz_dummy{GAMESTATE_EXTENSION}")

# GUI settings
GUI_BCKG_COLOR = "#ac733c"  # sepia
GUI_MAIN_FONT = "Arial"
GUI_WINDOW_WIDTH = 1280
GUI_WINDOW_HEIGHT = 720

###########
INPUT_SIGN = '>>> '  # sign indicating that the user should provide an input
TIME_DELAY = .15  # time delay in seconds between printing each character in text
DEFAULT_COLOR = Fore.LIGHTWHITE_EX  # default text color
ENTITY_COLOR = Fore.LIGHTRED_EX  # color for entities
SPECIAL_COLOR = Fore.LIGHTMAGENTA_EX  # color for headlines and particular special texts
COMBAT_COLOR = Fore.LIGHTCYAN_EX  # color for combat text
DEBUG_COLOR = Fore.LIGHTBLACK_EX  # color for debug messages
ERR_COLOR = Fore.RED  # color for error messages

DIFFICULTY = 1  # defoult difficulty level
INIT_MEAL_COUNT = meal_count = 8  # Initial number of meals
STAMINA_PER_MEAL = 4  # How many load of stamina in one meal
"""
- version naming scheme: '00.00.00.00' -> release.increment.hotfix.small
- release - fully working version of game with tested behaviour, ready to use by player
- increment - incremental number indicating progress of work
- hotfix - quick updates that fixes game breaking bugs
- small - small updates, typo fixes etc.
"""
# load version number
with open(VER_FILE, 'r') as ver_f:
    __version__ = ver_f.readline()


def load_config():
    # declare empty params
    keys_list = [
        "active_gameplay",
        "translation",
        "action_volume",
        "sfx_volume",
        "bckg_volume",
        "dev_mode",
        "debug_msg",
        "use_dummy",
        "logging",
        "start_sequence",
        "manual_battle",
        "dubbing",
        "get_music",
        "enable_GUI"
    ]

    _config = {param: None for param in keys_list}

    try:
        # load setup data from json file
        with open(CFG_NAME, "r") as f:
            config_ = json.load(f)

        # assign values from _config to setup_params dictionary
        for param in _config:
            _config[param] = config_.get(param)

        # unpack setup_params dictionary into individual variables
        globals().update(_config)

    except Exception:
        subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)  # to get rid of pygame init message
        print(f"DIR not present: {CFG_NAME} has been restored.")

    return _config


setup_params = load_config()

# /// constants and variables
game_state_exists = None
potion = None
count = 0  # Counter
potion_count = 2  # num of potions
choice_count = 0  # num of choices (universal)
gold_amount = 12  # initial gold amount
player_name = None  # Player's name
init_round_count = 0  # Initial num of rounds
s_count = s_init = 0  # Action points counter: luck
w_count = w_init = 0  # Action points counter: stamina
z_count = z_init = 0  # Action points counter: dexterity
and_his_name_is = '''
        ZZZZZZZ    BBBBBB       YYY     YYY     SSSSSS      ZZZZZZZZ      K     K     OOOOO     
              Z     B     B      YYY   YYY     S                  Z       K    K     O     O    
             Z      B     B       YYY YYY       SSS              Z        K   K     O       O    
            Z       BBBBBB         YYYYY            S           Z          KKK      O       O    
          Z         B     B         YYY             SSS        Z          K   K     O       O    
         Z          B     B         YYY              S        Z           K    K     O     O    
        ZZZZZZZ    BBBBBB           YYY        SSSSSS        ZZZZZZZZ     K     K     OOOOO     
        '''

entity_hit_mult = 1  # multiplier for entity level
p_hit_val_ = -2 * entity_hit_mult  # - 1000  # player hit value (-1000 to always win in one shot, for development only)
e_hit_val_ = -2 * entity_hit_mult  # enemy hit value

# /// pygame mixer setup
# Initialize the mixer module with the specified settings
try:
    pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=2 ** 12)
except Exception as e:
    input(f"\
    \n{DEBUG_COLOR}Exception while initializing pygame mixer\
    \n{ERR_COLOR} - {str(e)}\
    \n{DEBUG_COLOR}exit {INPUT_SIGN}")
    exit()

# /// equipment list

# main equipment
main_eq = {"plecak na Prowiant": "",
           "prowiant": meal_count,
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

difficulty_levels = {"easy": 1, "medium": 1.3, "hard": 1.6}

# /// music lists
# create lists of existing files within given categories
music_categories = ['menu', 'main', 'combat']
music_tracks = {}

"""
If 'get_music' is set to True in 'setup_params', this code initializes a dictionary called 'music_tracks'.
It then iterates through 'music_categories' and, for each category, finds and stores the file paths of music tracks
located in the corresponding category folder within the 'AUDIO_MUSIC_PATH' directory.
The music tracks are organized by category in the 'music_tracks' dictionary.
"""

if setup_params['get_music']:
    for category in music_categories:
        category_path = os.path.join(AUDIO_MUSIC_DIR, category)
        music_tracks[category] = []

        for filename in os.listdir(category_path):
            file_path = os.path.join(category_path, filename)
            if os.path.isfile(file_path):
                music_tracks[category].append(file_path)
