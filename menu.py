"""
"DRESZCZ" - GRA PARAGRAFOWA

Author: Jacek Ciesielski (1987)
Developer: Filip Pawłowski (2023) - filippawlowski2012@gmail.com
GitHub Repository: https://github.com/kotlecikmud/Dreszcz_Gra_Paragrafowa---text-based-game-adaptation.git
"""

import os
import time
import pygame
import platform
import subprocess
import gamebook as gb
import paragraphs as prg
import functions as func
import constants as cnst
from colorama import Fore, Style


def ask_for_user_input(message=None):
    input_message = message or ''
    choice = input(f'{input_message.strip()}{cnst.input_sign}{cnst.special_txt_clr}').strip()
    return choice


def main_menu():
    """Displays the main menu of the game and handles user input.

    Description:
        The main menu provides several options for the player to interact with the game:

        1. Start a new game: Allows the player to begin a new game from the beginning.
        2. Load a saved game: Provides the ability to continue a previously saved game.
        3. Access game rules: Displays the rules and instructions for playing the game.
        4. Adjust game settings: Allows the player to modify various game settings,
           such as language, difficulty, audio, etc.
        5. Exit the game: Terminates the game and returns to the operating system.

        The function continuously loops, displaying the main menu and prompting the player for input.
        It handles the user's input and performs different actions based on the selected menu option.

    Returns:
        None
    """

    while True:
        if cnst.setup_params['ver_num']:
            print(f"ver.{cnst.debug_txt_clr}{cnst.setup_params['ver_num']}")
            time.sleep(2)

        func.clear_terminal()
        if cnst.player_name:
            print(f"{cnst.def_txt_clr}{gb.infoboook[cnst.setup_params['translation']]['Mmenu_h']} {cnst.player_name}!")
        print(
            f"{cnst.special_txt_clr}{gb.infoboook[cnst.setup_params['translation']]['Mmenu_headline']}{cnst.def_txt_clr}")

        choices_main_menu = [
            (gb.infoboook[cnst.setup_params['translation']]['Mmenu1'], ''),  # new game
            (gb.infoboook[cnst.setup_params['translation']]['Mmenu3'], ''),  # rules
            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4'], ''),  # settings
            (gb.infoboook[cnst.setup_params['translation']]['Mmenu5'], '')  # exit
        ]

        # if any game state exists, display corresponding menu options
        if cnst.game_state_exists:
            # continue last gameplay
            choices_main_menu.insert(0, (
                gb.infoboook[cnst.setup_params['translation']]['Mmenu0'],
                cnst.setup_params['active_gameplay']))

            # load game
            choices_main_menu.insert(2, (gb.infoboook[cnst.setup_params['translation']]['Mmenu2'], ''))

        # append developer mode options at the end of main menu list
        if cnst.setup_params['dev_mode']:
            choices_main_menu.append(
                (f'{cnst.special_txt_clr}test_paragraph{cnst.def_txt_clr}',
                 f'bypass to any paragraph'))

            choices_main_menu.append(
                (f'{cnst.special_txt_clr}configure setup file{cnst.def_txt_clr}', 'basic config wizard'))

            choices_main_menu.append(
                (f'{cnst.special_txt_clr}project documentation{cnst.def_txt_clr}',
                 'pdf scan of original book, HTML adaptation from http://www.dudziarz.net'))

            choices_main_menu.append(
                (f'{cnst.special_txt_clr}restore default setup file{cnst.def_txt_clr}', 'ALL CHANGES WILL BE LOST!!!'))

        if cnst.setup_params['use_dummy']:  # disable 'new game' and 'load game' option when using dummy
            choices_main_menu.remove(choices_main_menu[2])
            choices_main_menu.remove(choices_main_menu[1])

        # displaying list in main menu
        for i, (choice_main_menu, description) in enumerate(choices_main_menu, 1):
            print(template.format(i, choice_main_menu, description))

        usr_input = ask_for_user_input()

        if usr_input == 'rayman':  # temporarily enable dev_mode
            cnst.setup_params['dev_mode'] = True
            cnst.template = "({}) {} - {}"
        elif usr_input == 'mario':  # temporarily disable dev_mode
            cnst.setup_params['dev_mode'] = False
            cnst.template = "({}) {}"

        if usr_input.isdigit():
            index = int(usr_input) - 1
            if 0 <= index < len(choices_main_menu):  # is digit in range
                usr_input = choices_main_menu[index][0]

        for choice_main_menu, description in choices_main_menu:
            if usr_input == choice_main_menu:

                # continue last gameplay
                if choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu0']:
                    last_paragraph = func.get_game_state('c')
                    func.pth_selector([], [f'{last_paragraph}'])

                # new game
                elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu1']:
                    func.clear_terminal()
                    print(f"/ {choice_main_menu}{cnst.def_txt_clr}")
                    func.loading()
                    prg._00()

                # load game
                elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu2']:
                    func.clear_terminal()
                    print(f"/ {choice_main_menu}{cnst.def_txt_clr}")

                    last_paragraph = func.get_game_state('l')

                    if not last_paragraph == 'prg.00':
                        func.pth_selector([], [f'{last_paragraph}'])


                # rules
                elif choice_main_menu == choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu3']:
                    while True:
                        func.clear_terminal()
                        print(f"{cnst.special_txt_clr}/ {choice_main_menu}{cnst.def_txt_clr}")

                        choices_rules = [
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1'], ''),
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub2'], ''),
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub3'], ''),
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub4'], ''),
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub5'], ''),
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub6'], ''),
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub7'], ''),
                            (gb.infoboook[cnst.setup_params['translation']]['return'], '')
                        ]

                        for i, (choice_rules, description) in enumerate(choices_rules, 1):
                            print(template.format(i, choice_rules, description))

                        usr_input = ask_for_user_input()

                        if usr_input.isdigit():
                            index = int(usr_input) - 1
                            if 0 <= index < len(choices_rules):
                                usr_input = choices_rules[index][0]

                        for choice_rules, description in choices_rules:
                            if usr_input == choice_rules:
                                func.clear_terminal()
                                print(f"{cnst.special_txt_clr}// {choice_rules}{cnst.def_txt_clr}")

                                # Equipment and attributes
                                if choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1']:
                                    print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_1a'])

                                    # show equipment list
                                    func.show_equipment_list()

                                    print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_1b'])

                                # Combat
                                elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub2']:
                                    print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_2'])

                                # Escape
                                elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub3']:
                                    print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_3'])

                                # Luck
                                elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub4']:
                                    print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_4'])

                                # Leveling up attributes
                                elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub5']:
                                    print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_5'])

                                # Provisions
                                elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub6']:
                                    print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_6'])

                                # Purpose of the expedition
                                elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub7']:
                                    print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_7'])

                                elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['return']:
                                    main_menu()

                                input(f'{cnst.input_sign}')

                # Settings
                elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu4']:
                    while True:
                        func.clear_terminal()
                        print(f"{cnst.special_txt_clr}/ {choice_main_menu}{cnst.def_txt_clr}")

                        choices_settings = [
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1'], ''),
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub2'], ''),
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub3'], ''),
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub4'], ''),
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub5'], ''),
                            (gb.infoboook[cnst.setup_params['translation']]['return'], '')
                        ]

                        for i, (choice_settings, description) in enumerate(choices_settings, 1):
                            print(template.format(i, choice_settings, description))

                        usr_input = ask_for_user_input()

                        if usr_input.isdigit():
                            index = int(usr_input) - 1
                            if 0 <= index < len(choices_settings):
                                usr_input = choices_settings[index][0]

                        for choice_settings, description in choices_settings:
                            if usr_input == choice_settings:

                                # Language settings
                                if choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                    'Mmenu4_sub1']:

                                    # initialize list of Locales in gamebook
                                    availablelocales = []

                                    for key in gb.gameboook:
                                        availablelocales.append(key)

                                    translation = str(input(
                                        f"{cnst.def_txt_clr}{gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_1']} {availablelocales}\
                                    \n{cnst.input_sign}")).lower()

                                    # get localization dictionaries from gamebook
                                    gb.get_translation(translation)

                                    func.debug_message(
                                        f"{gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_2']}: {cnst.setup_params['translation']}")

                                # Difficulty level settings
                                if choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                    'Mmenu4_sub2']:
                                    func.clear_terminal()
                                    print(f"{cnst.special_txt_clr}// {choice_settings}{cnst.def_txt_clr}")

                                    choices_difficulty_lvl = [
                                        (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_3'], ''),
                                        (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_4'], ''),
                                        (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_5'], '')
                                    ]

                                    for i, (choice_difficulty_lvl, description) in enumerate(choices_difficulty_lvl, 1):
                                        print(template.format(i, choice_difficulty_lvl, description))

                                    usr_input = ask_for_user_input()

                                    if usr_input.isdigit():
                                        index = int(usr_input) - 1
                                        if 0 <= index < len(choices_difficulty_lvl):
                                            usr_input = choices_difficulty_lvl[index][0]

                                    dif_lvl_choice = None
                                    for choice_difficulty_lvl, description in choices_difficulty_lvl:
                                        if usr_input == choice_difficulty_lvl:
                                            if choice_difficulty_lvl == gb.infoboook[cnst.setup_params['translation']][
                                                'Mmenu4_sub1_1']:
                                                dif_lvl_choice = cnst.difficulty_levels["easy"]

                                            elif choice_difficulty_lvl == \
                                                    gb.infoboook[cnst.setup_params['translation']][
                                                        'Mmenu4_sub1_2']:
                                                dif_lvl_choice = cnst.difficulty_levels["medium"]

                                            elif choice_difficulty_lvl == \
                                                    gb.infoboook[cnst.setup_params['translation']][
                                                        'Mmenu4_sub1_3']:
                                                dif_lvl_choice = cnst.difficulty_levels["hard"]

                                            cnst.entity_hit_mult = dif_lvl_choice

                                # Audio settings
                                elif choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                    'Mmenu4_sub3']:

                                    func.clear_terminal()
                                    print(f"{cnst.special_txt_clr}// {choice_settings}{cnst.def_txt_clr}")

                                    choices_sound_settings = [
                                        (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub3_1'],
                                         str(int(cnst.setup_params['action_volume'] * 10)) + "/10"),
                                        (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub3_2'],
                                         str(int(cnst.setup_params['sfx_volume'] * 10)) + "/10"),
                                        (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub3_3'],
                                         str(int(cnst.setup_params['bckg_volume'] * 10)) + "/10"),
                                        (gb.infoboook[cnst.setup_params['translation']]['return'], '')
                                    ]

                                    for i, (choice_sound_settings, description) in enumerate(choices_sound_settings, 1):
                                        print(template.format(i, choice_sound_settings, description))

                                    usr_input = ask_for_user_input()

                                    if usr_input.isdigit():
                                        index = int(usr_input) - 1
                                        if 0 <= index < len(choices_sound_settings):
                                            usr_input = choices_sound_settings[index][0]

                                    for choice_sound_settings, description in choices_sound_settings:

                                        if usr_input == choice_sound_settings:
                                            while True:
                                                # 1-10 because it's easier to input whole numbers than float
                                                try:

                                                    new_volume = int(
                                                        input(gb.infoboook[cnst.setup_params['translation']][
                                                                  'Mmenu4_sub3_a']))
                                                    if 0 < new_volume <= 10:
                                                        break
                                                    else:
                                                        print(gb.infoboook[cnst.setup_params['translation']][
                                                                  'Mmenu4_sub3_b'])

                                                except ValueError:
                                                    print(
                                                        gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub3_c'])

                                            # divide by 10 to get value between 0 and 1
                                            new_volume = new_volume / 10

                                            # dialogs
                                            if choice_sound_settings == gb.infoboook[cnst.setup_params['translation']][
                                                'Mmenu4_sub3_1']:
                                                cnst.setup_params['action_volume'] = new_volume
                                                func.dub_play("opened", "adam", True, False)

                                            # effects
                                            elif choice_sound_settings == \
                                                    gb.infoboook[cnst.setup_params['translation']][
                                                        'Mmenu4_sub3_2']:
                                                cnst.setup_params['sfx_volume'] = new_volume
                                                func.dub_play("click_snd", "fx", True, False)

                                            # background music
                                            elif choice_sound_settings == \
                                                    gb.infoboook[cnst.setup_params['translation']][
                                                        'Mmenu4_sub3_3']:
                                                cnst.setup_params['bckg_volume'] = new_volume
                                                pygame.mixer.music.set_volume(new_volume)

                                            elif choice_sound_settings == \
                                                    gb.infoboook[cnst.setup_params['translation']]['return']:
                                                main_menu()

                                            func.get_music(update=True)

                                # Name setting
                                elif choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                    'Mmenu4_sub4']:

                                    name = input(
                                        f"{gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub4_1']}{cnst.input_sign}")
                                    cnst.player_name = f"{Fore.LIGHTYELLOW_EX}{name}{cnst.def_txt_clr}"

                                    # Randomize if name is empty
                                    if name == '':
                                        func.name_randomizer()

                                # Randomize atributes
                                elif choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                    'Mmenu4_sub5']:

                                    print(gb.infoboook[cnst.setup_params['translation']][
                                              'Mmenu4_sub5_1'])

                                    func.loading()
                                    func.get_player_par()  # get new randomized player stats
                                    func.show_player_stats()
                                    input(f'\r{cnst.input_sign}')

                                elif choice_settings == gb.infoboook[cnst.setup_params['translation']]['return']:
                                    main_menu()

                # Exit game
                elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu5']:
                    choice2 = input(f"{gb.infoboook[cnst.setup_params['translation']]['Mmenu5_sub1_1']} [Y/N]:").lower()
                    if choice2.lower() == "y":
                        pygame.mixer.music.fadeout(600)
                        func.clear_terminal()
                        func.loading()
                        exit()

                # ADDITIONAL DEV FUNCTIONALITY
                # evaluating functions in paragraphs.py
                elif choice_main_menu == f'{cnst.special_txt_clr}test_paragraph{cnst.def_txt_clr}':
                    prg._xx()  # calling placeholder function

                # configuring setup.json file
                elif choice_main_menu == f'{cnst.special_txt_clr}configure setup file{cnst.def_txt_clr}':
                    func.clear_terminal()
                    func.update_setup_file(True)

                elif choice_main_menu == f'{cnst.special_txt_clr}project documentation{cnst.def_txt_clr}':
                    func.clear_terminal()
                    documentation_path = os.path.join(os.path.abspath('.'), 'Assets', 'docs', "doc_dummy.txt")

                    if platform.system() == "Windows":
                        subprocess.Popen(f'explorer /select,"{documentation_path}"', shell=True)
                    elif platform.system() == "Linux":
                        subprocess.Popen(['xdg-open', documentation_path])
                    elif platform.system() == "Darwin":
                        subprocess.Popen(['open', documentation_path])

                elif choice_main_menu == f'{cnst.special_txt_clr}restore default setup file{cnst.def_txt_clr}':
                    func.clear_terminal()
                    func.update_setup_file(backup=True)


"""
ADDITIONAL LOGIC DEVELOPER MODE
If the dev_mode variable is set to True, some useful information is displayed,
including the setup parameters file name at the beggining, documentation path, debug messages and so on.
"""
if cnst.setup_params['dev_mode']:
    # Version with enabled annotations
    template = "({}) {} - {}"

    print(f"\n{cnst.special_txt_clr}Setup parameters loaded from file: {Fore.YELLOW}{cnst.setup_name}{Style.RESET_ALL}")

    # Find the length of the longest value in cnst.loaded_setup
    max_value_length = max(len(str(key)) for key in cnst.loaded_setup.keys())

    # Print the key-value pairs with variable length formatting
    for key, value in cnst.loaded_setup.items():
        print(f"- {key.ljust(max_value_length)} - {value}")

    print(
        f"\n{Fore.LIGHTBLUE_EX}Code is running in developer mode.\
        \nTo deactivate the dev_mode temporarily toggle in the main menu, enter 'rayman'-ON or 'mario'-OFF.\
        \nAlso, you can change the setup parameters in the setup file manually.{cnst.def_txt_clr}\
        \n\
        \nuseful stuff:\
        \nsetup parameters {cnst.input_sign}{cnst.setup_name}\
        \ndocumentation {cnst.input_sign}Assets/PDF&HTML/"
    )

    input(f"\ncontinue to the main menu {cnst.input_sign}")

else:
    # Version without enabled annotations
    template = "({}) {}"

# time for start sequence: 23.1 seconds
if cnst.setup_params['start_sequence']:
    # loading background music
    func.get_music('menu')

    # start sequence
    func.loading(1.4)
    messages = ['Jacek Ciesielski\r', 'Filip Pawłowski', 'presents...', 'DRESZCZ - GRA PARAGRAFOWA']
    for message in messages:
        print(message)
        time.sleep(5.4)
else:
    func.get_music('main')

# randomize new player parameters
func.get_player_par()

# hide the "continue" and "load game" options in the menu if no game states are found
func.get_game_state('init')

# --- --- --- --- entry point
main_menu()
