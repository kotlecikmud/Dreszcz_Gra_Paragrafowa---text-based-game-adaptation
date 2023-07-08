# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# "DRESZCZ"
# GRA PARAGRAFOWA
# author: Jacek Ciesielski 1987
# programmer: Filip Pawłowski 2023 (filippawlowski2012@gmail.com)
# github repo: https://github.com/kotlecikmud/Dreszcz_Gra_Paragrafowa.git
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
import time
import pygame
import os
import json
import constants
import gamebook as gb
import paragraphs as prg
import functions as func
import constants as cnst
from colorama import Fore, Style

# check if the assets audio path exists, and if not, display an error message and exit the program
if not os.path.exists(cnst.assets_audio_pth):
    if constants.dev_mode:
        func.error_message('AssetsNotFound',
                           "The specified path for the audio assets is either non-existent or inaccessible. Check if /Assets exists.")
    exit()


def main_menu():
    while True:
        if cnst.ver_num != None:
            print(f'ver.{cnst.debug_txt_clr}{cnst.ver_num}')
            time.sleep(2)

        func.clear_terminal()
        if cnst.player_name:
            print(f"{cnst.def_txt_clr}{gb.infoboook[cnst.translation]['Mmenu_h']} {cnst.player_name}!")
        print(f"{cnst.special_txt_clr}{gb.infoboook[cnst.translation]['Mmenu_headline']}{cnst.def_txt_clr}")

        choices_main_menu = [
            (gb.infoboook[cnst.translation]['Mmenu1'], ''),  # new game
            (gb.infoboook[cnst.translation]['Mmenu3'], ''),  # rules
            (gb.infoboook[cnst.translation]['Mmenu4'], ''),  # settings
            (gb.infoboook[cnst.translation]['Mmenu5'], '')  # exit
        ]
        if cnst.game_state_exists:  # if any game state exists, display corresponding menu options
            choices_main_menu.insert(0, (gb.infoboook[cnst.translation]['Mmenu0'], ''))  # continue last gameplay
            choices_main_menu.insert(2, (gb.infoboook[cnst.translation]['Mmenu2'], ''))  # load game

        if cnst.dev_mode:  # append developer mode tools to main menu list
            choices_main_menu.append(
                ('eval()', f'bypass to any paragraph - {Fore.LIGHTRED_EX}for testing only!!!{Style.RESET_ALL}'))

        for i, (choice_main_menu, description) in enumerate(choices_main_menu, 1):  # displaying list in main menu
            print(cnst.template.format(i, choice_main_menu, description))

        usr_input = input(f'{cnst.input_sign}{cnst.special_txt_clr} ').strip()
        # play click
        # func.dub_play('click', 'fx')
        if usr_input.isdigit():  # is digit
            index = int(usr_input) - 1
            if 0 <= index < len(choices_main_menu):  # is digit in range
                usr_input = choices_main_menu[index][0]

        for choice_main_menu, description in choices_main_menu:  # displaying list
            if usr_input == choice_main_menu:

                # continue last gameplay
                if choice_main_menu == gb.infoboook[cnst.translation]['Mmenu0']:
                    last_paragraph = func.get_game_state('c')
                    func.pth_selector([], [f'{last_paragraph}'])

                # new game
                elif choice_main_menu == gb.infoboook[cnst.translation]['Mmenu1']:
                    func.clear_terminal()
                    print(f"/ {choice_main_menu}{cnst.def_txt_clr}")
                    pygame.mixer.music.fadeout(2500)
                    func.loading(2)
                    prg._00()

                # load game
                elif choice_main_menu == gb.infoboook[cnst.translation]['Mmenu2']:
                    func.clear_terminal()
                    print(f"/ {choice_main_menu}{cnst.def_txt_clr}")

                    last_paragraph = func.get_game_state('l')

                    if not last_paragraph == 'prg.00':
                        func.pth_selector([], [f'{last_paragraph}'])


                # Rules
                elif choice_main_menu == choice_main_menu == gb.infoboook[cnst.translation]['Mmenu3']:
                    while True:
                        func.clear_terminal()
                        print(f"{cnst.special_txt_clr}/ {choice_main_menu}{cnst.def_txt_clr}")

                        choices_rules = [
                            (gb.infoboook[cnst.translation]['Mmenu3_sub1'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu3_sub2'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu3_sub3'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu3_sub4'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu3_sub5'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu3_sub6'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu3_sub7'], ''),
                            (gb.infoboook[cnst.translation]['return'], '')
                        ]

                        for i, (choice_rules, description) in enumerate(choices_rules, 1):
                            print(cnst.template.format(i, choice_rules, description))

                        usr_input = input(f'{cnst.special_txt_clr} ').strip()

                        if usr_input.isdigit():
                            index = int(usr_input) - 1
                            if 0 <= index < len(choices_rules):
                                usr_input = choices_rules[index][0]

                        for choice_rules, description in choices_rules:
                            if usr_input == choice_rules:
                                func.clear_terminal()
                                print(f"{cnst.special_txt_clr}// {choice_rules}{cnst.def_txt_clr}")

                                # Equipment and attributes
                                if choice_rules == gb.infoboook[cnst.translation]['Mmenu3_sub1']:
                                    print(gb.infoboook[cnst.translation]['Mmenu3_sub1_1a'])

                                    func.show_equipment_list()  # show equipment list

                                    print(gb.infoboook[cnst.translation]['Mmenu3_sub1_1b'])

                                # Combat
                                elif choice_rules == gb.infoboook[cnst.translation]['Mmenu3_sub2']:
                                    print(gb.infoboook[cnst.translation]['Mmenu3_sub1_2'])

                                # Escape
                                elif choice_rules == gb.infoboook[cnst.translation]['Mmenu3_sub3']:
                                    print(gb.infoboook[cnst.translation]['Mmenu3_sub1_3'])

                                # Luck
                                elif choice_rules == gb.infoboook[cnst.translation]['Mmenu3_sub4']:
                                    print(gb.infoboook[cnst.translation]['Mmenu3_sub1_4'])

                                # Leveling up attributes
                                elif choice_rules == gb.infoboook[cnst.translation]['Mmenu3_sub5']:
                                    print(gb.infoboook[cnst.translation]['Mmenu3_sub1_5'])

                                # Provisions
                                elif choice_rules == gb.infoboook[cnst.translation]['Mmenu3_sub6']:
                                    print(gb.infoboook[cnst.translation]['Mmenu3_sub1_6'])

                                # Purpose of the expedition
                                elif choice_rules == gb.infoboook[cnst.translation]['Mmenu3_sub7']:
                                    print(gb.infoboook[cnst.translation]['Mmenu3_sub1_7'])

                                elif choice_rules == gb.infoboook[cnst.translation]['return']:
                                    # print('POWODZENIA!')
                                    # 
                                    main_menu()

                                input(f'{cnst.input_sign}')

                # Settings
                elif choice_main_menu == gb.infoboook[cnst.translation]['Mmenu4']:
                    while True:
                        func.clear_terminal()
                        print(f"{cnst.special_txt_clr}/ {choice_main_menu}{cnst.def_txt_clr}")

                        choices_settings = [
                            (gb.infoboook[cnst.translation]['Mmenu4_sub1'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu4_sub2'], ''),
                            # (gb.infoboook[cnst.translation]['Mmenu4_sub3'], ''),  # currently unfinished
                            (gb.infoboook[cnst.translation]['Mmenu4_sub4'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu4_sub5'], ''),
                            (gb.infoboook[cnst.translation]['return'], '')
                        ]

                        for i, (choice_settings, description) in enumerate(choices_settings, 1):
                            print(cnst.template.format(i, choice_settings, description))

                        usr_input = input(f'{cnst.special_txt_clr} ').strip()

                        if usr_input.isdigit():
                            index = int(usr_input) - 1
                            if 0 <= index < len(choices_settings):
                                usr_input = choices_settings[index][0]

                        for choice_settings, description in choices_settings:
                            if usr_input == choice_settings:

                                if choice_settings == gb.infoboook[cnst.translation][
                                    'Mmenu4_sub1']:  # Language settings
                                    availableLocales = []
                                    for key in gb.gameboook:
                                        availableLocales.append(key)

                                    translation = str(input(
                                        f"{cnst.def_txt_clr}{gb.infoboook[cnst.translation]['Mmenu4_sub1_1']} {availableLocales}\
                                    \n{cnst.input_sign}")).lower()
                                    gb.get_translation(translation)  # update localization dictionaries
                                    func.debug_message(
                                        f"{gb.infoboook[cnst.translation]['Mmenu4_sub1_2']}: {cnst.translation}")

                                if choice_settings == gb.infoboook[cnst.translation][
                                    'Mmenu4_sub2']:  # Difficulty level settings
                                    func.clear_terminal()
                                    print(f"{cnst.special_txt_clr}// {choice_settings}{cnst.def_txt_clr}")

                                    choices_difficulty_lvl = [
                                        (gb.infoboook[cnst.translation]['Mmenu4_sub1_3'], ''),
                                        (gb.infoboook[cnst.translation]['Mmenu4_sub1_4'], ''),
                                        (gb.infoboook[cnst.translation]['Mmenu4_sub1_5'], '')
                                    ]

                                    for i, (choice_difficulty_lvl, description) in enumerate(choices_difficulty_lvl, 1):
                                        print(cnst.template.format(i, choice_difficulty_lvl, description))

                                    usr_input = input(f'{cnst.special_txt_clr} ').strip()

                                    if usr_input.isdigit():
                                        index = int(usr_input) - 1
                                        if 0 <= index < len(choices_difficulty_lvl):
                                            usr_input = choices_difficulty_lvl[index][0]

                                    difficulty_lvl = None
                                    for choice_difficulty_lvl, description in choices_difficulty_lvl:
                                        if usr_input == choice_difficulty_lvl:

                                            if choice_difficulty_lvl == gb.infoboook[cnst.translation]['Mmenu4_sub1_1']:
                                                difficulty_lvl = cnst.d_lvl_e

                                            elif choice_difficulty_lvl == gb.infoboook[cnst.translation][
                                                'Mmenu4_sub1_2']:
                                                difficulty_lvl = cnst.d_lvl_m

                                            elif choice_difficulty_lvl == gb.infoboook[cnst.translation][
                                                'Mmenu4_sub1_3']:
                                                difficulty_lvl = cnst.d_lvl_h

                                            cnst.e_mult_choice = difficulty_lvl


                                elif choice_settings == gb.infoboook[cnst.translation]['Mmenu4_sub3']:  # Audio settings

                                    func.clear_terminal()
                                    print(f"{cnst.special_txt_clr}// {choice_settings}{cnst.def_txt_clr}")

                                    choices_sound_settings = [
                                        (gb.infoboook[cnst.translation]['Mmenu4_sub3_1'], ''),
                                        (gb.infoboook[cnst.translation]['Mmenu4_sub3_2'], ''),
                                        (gb.infoboook[cnst.translation]['Mmenu4_sub3_3'], ''),
                                        (gb.infoboook[cnst.translation]['return'], '')
                                    ]

                                    for i, (choice_sound_settings, description) in enumerate(choices_sound_settings, 1):
                                        print(cnst.template.format(i, choice_sound_settings, description))

                                    usr_input = input(f'{cnst.special_txt_clr} ').strip()

                                    if usr_input.isdigit():
                                        index = int(usr_input) - 1
                                        if 0 <= index < len(choices_sound_settings):
                                            usr_input = choices_sound_settings[index][0]

                                    for choice_sound_settings, description in choices_sound_settings:

                                        if usr_input == choice_sound_settings:

                                            while True:

                                                try:
                                                    new_volume = int(input('Podaj nowy poziom głośności (1-10): '))
                                                    if 0 <= new_volume <= 10:
                                                        break

                                                except ValueError:
                                                    print("Podano nieprawidłową wartość. Wprowadź liczbę (1-10).")

                                            if choice_sound_settings == gb.infoboook[cnst.translation]['Mmenu3_sub3_1']:
                                                cnst.action_volume = new_volume

                                            elif choice_sound_settings == gb.infoboook[cnst.translation][
                                                'Mmenu4_sub3_2']:
                                                cnst.sfx_volume = new_volume

                                            elif choice_sound_settings == gb.infoboook[cnst.translation][
                                                'Mmenu4_sub3_3']:
                                                cnst.bckg_volume = new_volume
                                                pygame.mixer.music.set_volume(new_volume)

                                            elif choice_sound_settings == gb.infoboook[cnst.translation]['return']:
                                                main_menu()

                                elif choice_settings == gb.infoboook[cnst.translation]['Mmenu4_sub4']:  # Name setting

                                    name = input(
                                        f"{gb.infoboook[cnst.translation]['Mmenu4_sub4_1']}{cnst.input_sign}")
                                    cnst.player_name = f"{Fore.LIGHTYELLOW_EX}{name}{cnst.def_txt_clr}"

                                    if name == '':
                                        func.name_randomizer()

                                elif choice_settings == gb.infoboook[cnst.translation][
                                    'Mmenu4_sub5']:  # Randomize atributes

                                    print(gb.infoboook[cnst.translation][
                                              'Mmenu4_sub5_1'])
                                    func.loading(2)
                                    func.get_player_par()
                                    func.show_player_stats()
                                    input(f'\r{cnst.input_sign}')

                                elif choice_settings == gb.infoboook[cnst.translation]['return']:
                                    main_menu()

                # Exit game
                elif choice_main_menu == gb.infoboook[cnst.translation]['Mmenu5']:
                    choice2 = input(f"{gb.infoboook[cnst.translation]['Mmenu5_sub1_1']} [Y/N]:").lower()
                    if choice2.lower() == "y":
                        pygame.mixer.music.fadeout(600)
                        func.clear_terminal()
                        func.loading(1)
                        exit()

                elif choice_main_menu == 'eval()':  # only for dev purposes; evaluating functions in paragraphs.py

                    prg._xx()  # calling placeholder function


# --- --- --- --- entry point
if not cnst.dev_mode:
    if cnst.show_start_sequence:  # time: 23.1 seconds
        func.get_music('menu')  # loading background music
        func.loading(1.4)  # loading screen
        messages = ['Jacek Ciesielski\r', 'Filip Pawłowski', 'presents...', 'DRESZCZ - GRA PARAGRAFOWA']
        for message in messages:
            print(message)
            time.sleep(5.4)

    else:
        func.get_music('main')

func.get_player_par()  # loading player parameters
func.clear_terminal()  # clearing terminal

func.get_game_state('init')  # omit the "load game" menu option from being displayed if no game states found
main_menu()
