import pygame
from colorama import Fore

ver_num = ''

dev_mode = True  # Toggle for developer mode; enables debug information, error indicators and other information while playing

# /// settings
allow_skip_dub = False  # Determines whether dubbing can be skipped.
skip_dub = False  # Determines whether dubbing has been skipped.
automatic_battle = True  # Determines whether battles are automatic.

# /// initiators
translation = None  # container for language option
count = 0  # Counter
count_potion = 2  # Number of available potions
choice_count = 0  # Number of choices
d_lvl_e = 1  # Difficulty level: easy
d_lvl_m = d_lvl_e * 1.3  # Difficulty level: medium
d_lvl_h = d_lvl_e * 1.6  # Difficulty level: hard
p_luck = None  # Player's luck
player_name = f'{Fore.LIGHTYELLOW_EX}Śmiałek{Fore.LIGHTWHITE_EX}'  # Player's name
round_count = 0  # Round counter
s_count = s_init = 0  # Action points counter: luck
w_count = w_init = 0  # Action points counter: stamina
z_count = z_init = 0  # Action points counter: dexterity
init_eatables_count = eatables_count = 8  # Initial number of meals
eatable_W_load = 4  # How many load of stamina in one meal
gold_amount = 0  # Initial number of gold pieces
init_round_count = 0  # Initial number of rounds

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
special_txt_clr = Fore.LIGHTMAGENTA_EX  # color for special text
combat_txt_clr = Fore.LIGHTCYAN_EX  # color for combat text
debug_txt_clr = Fore.LIGHTBLACK_EX  # color for debug messages
error_txt_clr = Fore.LIGHTRED_EX  # color for error messages

template = "({}) {} - {}" if dev_mode else "({}) {}"  # template for list printing

# /// paths
assets_audio_pth = 'Assets/Audio/Dunmer'  # Path to Dunmer audio files
assets_audio_effects_pth = 'Assets/Audio/fx'  # Path to sound effects
assets_audio_music_pth = 'Assets/Audio/music'  # Path to music

assets_audio_pth_adam = 'Assets/Audio/ElevenLabs/Adam'  # Path to Adam's audio files

music_combat = [f'{assets_audio_music_pth}/music_combat_1.mp3',  # List of combat music tracks
                f'{assets_audio_music_pth}/music_combat_2.mp3']

music_main = [f'{assets_audio_music_pth}/music_main_1.mp3',  # List of main music tracks
              f'{assets_audio_music_pth}/music_main_2.mp3',
              f'{assets_audio_music_pth}/dark_strings_15_11_2020.wav']

# /// sound mixing
pygame.mixer.init(frequency=44100, size=-16, channels=1,
                  buffer=2 ** 12)  # Initialize the mixer module with the specified settings
def_action_volume = 1  # Default volume for action sounds
def_sfx_volume = 0.8  # Default volume for sound effects
def_bckg_volume = 0.8  # Default volume for background music

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
