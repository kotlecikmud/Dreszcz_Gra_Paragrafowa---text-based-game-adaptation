"""
"DRESZCZ" - GRA PARAGRAFOWA

Author: Jacek Ciesielski (1987)
Developer: Filip Pawłowski (2024) - filippawlowski2012@gmail.com
GitHub Repository: https://github.com/kotlecikmud/Dreszcz_Gra_Paragrafowa---text-based-game-adaptation.git
"""

import os
import time
import pygame
import subprocess
import gamebook as gb
import paragraphs as prg
import functions as func
import constants as cnst
from colorama import Fore, Style


def main_menu():
    """Displays the main menu of the game and handles user input. Menu is not accesible during gameplay (for now, becasue I don't know how top implement it with subprocess)

    Description:
        Provides several options for the player to interact with the game:\n
        1. Continue - Provides the ability to continue a previously saved game.
        2. New game - Allows the player to begin a new game from the beginning.
        3. Load game: Provides the ability to load saved game.
        4. Game rules: Displays the submenu for rules and instructions for playing the game.
        5. Settings: Displays the submenu for several in-game settings. Allows the player to modify various game settings,
           such as language, difficulty, audio, etc.
        6. Exit the game: Terminates the game.

    Notes:
        The function continuously loops, displaying the main menu and prompting the player for input.
        It handles the user's input and performs different actions based on the selected menu option.
        Menu options can be temporairly disabled by simply commenting out desired position.
        Menu titles are retrioved from dictiopnary named infobook located in gamebook.py module.
        Game automatically displays text in right language, which can be changed in settings under language option, if player wishes so.

        There are some additional developer options, that provide user with easy testing capabilities.
        Type in main menu:
        rayman - to enable and show additional options
        mario - to disable and hide additional options

    Returns:
        None
    """

    func.log_event("main.py ENTRY POINT")
    while True:
        func.clear_terminal()

        if cnst.player_name:
            print(
                f"{cnst.DEFAULT_COLOR}{gb.infoboook[cnst.setup_params['translation']]['Mmenu_h']} {cnst.player_name}!")
        print(
            f"{cnst.SPECIAL_COLOR}{gb.infoboook[cnst.setup_params['translation']]['Mmenu_headline']}{cnst.DEFAULT_COLOR}")

        if cnst.__version__:
            print(f"{cnst.DEBUG_COLOR}ver.{cnst.__version__}{cnst.DEFAULT_COLOR}")

        choices_main_menu = [
            (gb.infoboook[cnst.setup_params['translation']]['Mmenu0'], cnst.setup_params['active_gameplay']),
            # continue
            (gb.infoboook[cnst.setup_params['translation']]['Mmenu1'], ''),  # new game
            (gb.infoboook[cnst.setup_params['translation']]['Mmenu2'], ''),  # load game
            (gb.infoboook[cnst.setup_params['translation']]['Mmenu3'], ''),  # rules
            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4'], ''),  # settings
            (gb.infoboook[cnst.setup_params['translation']]['Mmenu5'], ''),  # exit
        ]

        # if any game state exists, display corresponding menu options
        if not cnst.game_state_exists:
            # continue last gameplay
            choices_main_menu.remove(
                (gb.infoboook[cnst.setup_params['translation']]['Mmenu0'], cnst.setup_params['active_gameplay']))

            # load game
            choices_main_menu.remove((gb.infoboook[cnst.setup_params['translation']]['Mmenu2'], ''))

        # append developer mode options at the end of main menu list
        if cnst.setup_params['dev_mode']:
            choices_main_menu.append(
                (f'{cnst.SPECIAL_COLOR}test_paragraph{cnst.DEFAULT_COLOR}',
                 f'bypass to any paragraph'))

            choices_main_menu.append(
                (f'{cnst.SPECIAL_COLOR}configure setup file{cnst.DEFAULT_COLOR}', 'basic config wizard'))

            choices_main_menu.append(
                (f'{cnst.SPECIAL_COLOR}project documentation{cnst.DEFAULT_COLOR}',
                 'pdf scan of original book, HTML adaptation from http://www.dudziarz.net'))

            choices_main_menu.append(
                (f'{cnst.SPECIAL_COLOR}restore default config{cnst.DEFAULT_COLOR}', 'ALL CHANGES WILL BE LOST!!!'))

        if cnst.setup_params['use_dummy']:  # disable 'new game' and 'load game' option when using dummy
            choices_main_menu.remove((gb.infoboook[cnst.setup_params['translation']]['Mmenu1'], ''))  # new game
            # choices_main_menu.remove((gb.infoboook[cnst.setup_params['translation']]['Mmenu2'], ''))  # load game

        # displaying list in main menu
        for i, (choice_main_menu, description) in enumerate(choices_main_menu, 1):
            print(template.format(i, choice_main_menu, description))

        usr_input = input(f'{cnst.INPUT_SIGN}').strip()

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
                    func.pth_selector(actions=[f'{last_paragraph}'])

                # new game
                elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu1']:
                    func.clear_terminal()
                    print(f"/ {choice_main_menu}{cnst.DEFAULT_COLOR}")
                    prg._00()

                # load game
                elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu2']:
                    func.clear_terminal()
                    print(f"/ {choice_main_menu}{cnst.DEFAULT_COLOR}")

                    last_paragraph = func.get_game_state('l')

                    if not last_paragraph == '00':
                        func.pth_selector([], [f'{last_paragraph}'])


                # rules
                elif choice_main_menu == choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu3']:
                    while True:
                        func.clear_terminal()
                        print(f"{cnst.SPECIAL_COLOR}/ {choice_main_menu}{cnst.DEFAULT_COLOR}")

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

                        usr_input = input(f'{cnst.INPUT_SIGN}').strip()

                        if usr_input.isdigit():
                            index = int(usr_input) - 1
                            if 0 <= index < len(choices_rules):
                                usr_input = choices_rules[index][0]

                        for choice_rules, description in choices_rules:
                            if usr_input == choice_rules:
                                func.clear_terminal()
                                print(f"{cnst.SPECIAL_COLOR}// {choice_rules}{cnst.DEFAULT_COLOR}")

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

                                input(f'{cnst.INPUT_SIGN}')

                # Settings
                elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu4']:
                    while True:
                        func.clear_terminal()
                        print(f"{cnst.SPECIAL_COLOR}/ {choice_main_menu}{cnst.DEFAULT_COLOR}")

                        choices_settings = [
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1'], ''),  # Language
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub2'], ''),  # Difficulty level
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub3'], ''),  # Sound
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub4'], ''),  # Character name
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub5'], ''),  # Randomize attributes
                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub6'], ''),  # Check for updates
                            (gb.infoboook[cnst.setup_params['translation']]['return'], '')
                        ]

                        for i, (choice_settings, description) in enumerate(choices_settings, 1):
                            print(template.format(i, choice_settings, description))

                        usr_input = input(f'{cnst.INPUT_SIGN}').strip()

                        if usr_input.isdigit():
                            index = int(usr_input) - 1
                            if 0 <= index < len(choices_settings):
                                usr_input = choices_settings[index][0]

                        for choice_settings, description in choices_settings:
                            if usr_input == choice_settings:

                                # Language settings
                                if choice_settings == gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1']:

                                    # initialize list of Locales in gamebook
                                    availablelocales = []

                                    # prepare available languages and append to list
                                    for key in gb.gameboook:
                                        availablelocales.append(key)

                                    translation = str(input(
                                        f"{cnst.DEFAULT_COLOR}{gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_1']} {availablelocales}\
                                    \n{cnst.INPUT_SIGN}")).lower()

                                    # get localization dictionaries from gamebook
                                    gb.get_translation(translation)

                                    func.debug_message(
                                        f"{gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_2']}: {cnst.setup_params['translation']}")

                                # Difficulty level settings
                                if choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                    'Mmenu4_sub2']:
                                    func.clear_terminal()
                                    print(f"{cnst.SPECIAL_COLOR}// {choice_settings}{cnst.DEFAULT_COLOR}")

                                    choices_difficulty_lvl = [
                                        (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_3'], ''),
                                        (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_4'], ''),
                                        (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_5'], '')
                                    ]

                                    for i, (choice_difficulty_lvl, description) in enumerate(choices_difficulty_lvl, 1):
                                        print(template.format(i, choice_difficulty_lvl, description))

                                    usr_input = input(f'{cnst.INPUT_SIGN}').strip()

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

                                # Audio settings -> capped range -> (0,10)
                                elif choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                    'Mmenu4_sub3']:

                                    func.clear_terminal()
                                    print(f"{cnst.SPECIAL_COLOR}// {choice_settings}{cnst.DEFAULT_COLOR}")

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

                                    usr_input = input(f'{cnst.INPUT_SIGN}').strip()

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
                                                func.update_config_file()  # dump settings to setup file
                                                main_menu()

                                            func.get_music(update=True)

                                # Name setting
                                elif choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                    'Mmenu4_sub4']:

                                    name = input(
                                        f"{gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub4_1']}{cnst.INPUT_SIGN}")
                                    cnst.player_name = f"{Fore.LIGHTYELLOW_EX}{name}{cnst.DEFAULT_COLOR}"

                                    # Randomize if name is empty
                                    if name == '':
                                        func.name_randomizer()

                                # Randomize atributes
                                elif choice_settings == gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub5']:

                                    print(gb.infoboook[cnst.setup_params['translation']][
                                              'Mmenu4_sub5_1'])

                                    func.get_player_par()  # get new randomized player stats
                                    func.show_player_stats()
                                    input(f'\r{cnst.INPUT_SIGN}')

                                elif choice_settings == gb.infoboook[cnst.setup_params['translation']]['return']:
                                    main_menu()

                                # Check for updates
                                elif choice_settings == gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub6']:
                                    update_state = func.check_for_update()
                                    if update_state:
                                        print(gb.infoboook[cnst.setup_params['translation']][
                                                  'Mmenu4_sub6_1'])

                                    elif not update_state:
                                        print(gb.infoboook[cnst.setup_params['translation']][
                                                  'Mmenu4_sub6_2'])

                                    input(f'\r{cnst.INPUT_SIGN}')

                # Exit game
                elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu5']:
                    choice2 = input(f"{gb.infoboook[cnst.setup_params['translation']]['Mmenu5_sub1_1']} [Y/N]:").lower()
                    if choice2.lower() == "y":
                        pygame.mixer.music.fadeout(800)
                        func.clear_terminal()
                        exit()

                # ADDITIONAL DEV FUNCTIONALITY
                # evaluating functions in paragraphs.py
                elif choice_main_menu == f'{cnst.SPECIAL_COLOR}test_paragraph{cnst.DEFAULT_COLOR}':
                    if os.path.exists(cnst.DUMMY_GAMESTATE_NAME):
                        # set active gameplay to dummy file
                        cnst.setup_params["active_gameplay"] = str(cnst.DUMMY_GAMESTATE_NAME)
                        func.log_event(f"set active gameplay to {cnst.DUMMY_GAMESTATE_NAME}")

                        prg._xx()  # calling placeholder function
                    else:
                        func.error_message('', f"Dummy gamestate file was not found. Enable 'use_dummy' in config.\
                        \nPlease close game, modify {cnst.CFG_NAME} and try again.")
                        input(cnst.INPUT_SIGN)

                # configuring config.json file
                elif choice_main_menu == f'{cnst.SPECIAL_COLOR}configure setup file{cnst.DEFAULT_COLOR}':
                    func.clear_terminal()
                    func.update_config_file(True)

                # open documentation dir
                elif choice_main_menu == f'{cnst.SPECIAL_COLOR}project documentation{cnst.DEFAULT_COLOR}':
                    func.clear_terminal()
                    documentation_path = os.path.join(os.path.abspath('.'), 'Assets', 'docs', "doc_dummy.txt")

                    subprocess.Popen(f'explorer /select,"{documentation_path}"', shell=True)

                # restore default config
                elif choice_main_menu == f'{cnst.SPECIAL_COLOR}restore default config{cnst.DEFAULT_COLOR}':
                    func.clear_terminal()
                    func.update_config_file(backup=True)


if __name__ == '__main__':
    """
    ADDITIONAL LOGIC for DEVELOPER MODE
    If the dev_mode variable is set to True, some useful information is displayed,
    including the setup parameters file name at the beggining, documentation path, debug messages and so on.
    """
    if cnst.setup_params['dev_mode']:
        # Version of menu with enabled annotations
        template = "({}) {} - {}"

        print(f"\n{cnst.SPECIAL_COLOR}Setup parameters loaded from file: {Fore.YELLOW}{cnst.CFG_NAME}{Style.RESET_ALL}")

        # Print the key-value pairs with variable length formatting
        for key, value in cnst.setup_params.items():
            print(f"- {key.ljust(max(len(str(key)) for key in cnst.setup_params.keys()))} - {value}")

        print(
            f"\n{Fore.LIGHTBLUE_EX}Code is running in developer mode.\
            \nTo deactivate the dev_mode temporarily toggle in the main menu, enter 'rayman'-ON or 'mario'-OFF.\
            \nAlso, you can change the setup parameters in the setup file manually.{cnst.DEFAULT_COLOR}\
            \n\
            \nuseful stuff:\
            \nsetup parameters {cnst.INPUT_SIGN}{cnst.CFG_NAME}\
            \ndocumentation {cnst.INPUT_SIGN}Assets\\docs\\"
        )

        input(f"\ncontinue by pressing enter {cnst.INPUT_SIGN}")

    else:
        # Version of menu without enabled annotations
        template = "({}) {}"

    # time for start sequence: 23.1 seconds
    if cnst.setup_params['start_sequence']:
        # loading background music
        func.get_music('menu')

        # start sequence
        time.sleep(1.4)
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

    # if config.json not found, restore backup
    try:
        with open(cnst.CFG_NAME, 'r') as json_file:
            _ = json_file.readable()

    except FileNotFoundError:
        func.error_message("FileNotFoundError", f"An error occurred while updating the setup file")
        func.debug_message("config.json not found, restoring...")
        func.update_config_file(manual=False, backup=True)

    # enter main menu loop
    main_menu()
