import pygame
from colorama import Fore, Style

ver_num = ''

# /// settings
dev_mode = False  # Toggle for developer mode; enables many debug information, error indicators and other exlusive machanics while playing

if dev_mode:
    skip_dub = True  # Determines whether dubbing has been skipped.
    get_music_enable = False
    input(
        f"{Fore.LIGHTBLUE_EX}Code is running in developer mode. Disable by going to constants.py and changing 'dev_mode' boolean to {Fore.YELLOW}False{Style.RESET_ALL}\
        \n>>> ")
else:
    skip_dub = False
    get_music_enable = True

automatic_battle = True  # Determines whether battles are automatic.
allow_skip_dub = False  # Determines whether dubbing can be skipped by hitting enter key

# /// initiators
active_gameplay = None
translation = None
potion = None
count = 0  # Counter
count_potion = 2  # num of potions
choice_count = 0  # num of choices (universal)
d_lvl_e = 1  # Difficulty level: easy
d_lvl_m = d_lvl_e * 1.3  # Difficulty level: medium
d_lvl_h = d_lvl_e * 1.6  # Difficulty level: hard
p_luck = None  # Player's luck
player_name = None  # Player's name
init_round_count = 0  # Initial num of rounds
round_count = 0  # Round counter
s_count = s_init = 0  # Action points counter: luck
w_count = w_init = 0  # Action points counter: stamina
z_count = z_init = 0  # Action points counter: dexterity
init_eatables_count = eatables_count = 8  # Initial number of meals
eatable_W_load = 4  # How many load of stamina in one meal
gold_amount = 0  # Initial num of gold

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
delay = 0.3  # time delay in seconds between printing each character in text
e_mult_choice = d_lvl_e  # multiplier for entity level (default level)
p_mult = 1  # player multiplier for damage calculation
p_hit_val_ = -2 * e_mult_choice  # player hit value
e_hit_val_ = -2 * e_mult_choice  # enemy hit value
def_txt_clr = Fore.LIGHTWHITE_EX  # default text color
entity_txt_clr = Fore.RED  # color for entities
special_txt_clr = Fore.LIGHTMAGENTA_EX  # color for headlines and particular special texts
combat_txt_clr = Fore.LIGHTCYAN_EX  # color for combat text
debug_txt_clr = Fore.LIGHTBLACK_EX  # color for debug messages
error_txt_clr = Fore.LIGHTRED_EX  # color for error messages

# template for list printing (if dev_mode: explainer lines)
template = "({}) {}"
# template = "({}) {} - {}" if dev_mode else "({}) {}"

# /// paths
assets_audio_pth = 'Assets/Audio'  # Path to audio files
assets_audio_effects_pth = 'Assets/Audio/fx'  # Path to sound effects
assets_audio_music_pth = 'Assets/Audio/music'  # Path to music

music_combat = [f'{assets_audio_music_pth}/combat/music_combat_1.mp3',  # List of combat music tracks
                f'{assets_audio_music_pth}/combat/music_combat_2.mp3']

music_main = [f'{assets_audio_music_pth}/main/music_main_1.mp3',  # List of main music tracks
              f'{assets_audio_music_pth}/main/music_main_2.mp3',
              f'{assets_audio_music_pth}/main/music_main_3.mp3']

# /// sound mixer setup
pygame.mixer.init(frequency=44100, size=-16, channels=1,
                  buffer=2 ** 12)  # Initialize the mixer module with the specified settings
action_volume = 1  # Default volume for action sounds
sfx_volume = 0.8  # Default volume for sound effects
bckg_volume = 0.8  # Default volume for background music

# /// ekwipunki

# główny ekwipunek
main_eq = ['plecak na Prowiant', f'prowiant ({eatables_count} porcji)', 'tarcza', 'miecz',
           f'złoto({gold_amount} sztuk)']

# /// słowniki wyborów
choices_115 = {'Miecz': '_232()',
               'Kościany kordelas': '_324()',
               'Rękawice': '_95()',
               'Tarcza': '_37()',
               'Hełm': '_298()',
               'Młot': '_324()',
               }
