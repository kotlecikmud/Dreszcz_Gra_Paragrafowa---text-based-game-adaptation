# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
# 'DRESZCZ'
# GRA PARAGRAFOWA
# author: Jacek Ciesielski 1987
# programmer: Filip Pawłowski 2023 (filippawlowski2012@gmail.com)
# github repo: https://github.com/kotlecikmud/Dreszcz_Gra_Paragrafowa.git
# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
import time, pygame, os

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
        if cnst.ver_num != '':
            print(f'ver.{cnst.debug_txt_clr}{cnst.ver_num}')
            time.sleep(2)

        func.clear_terminal()
        if cnst.player_name:
            print(f"{cnst.def_txt_clr}{gb.infoboook[cnst.translation]['Mmenu0']} {cnst.player_name}!")
        print(f"{cnst.special_txt_clr}{gb.infoboook[cnst.translation]['Mmenu_headline']}{cnst.def_txt_clr}")
        time.sleep(cnst.delay)

        choices_main_menu = [
            (gb.infoboook[cnst.translation]['Mmenu1'], ''),
            (gb.infoboook[cnst.translation]['Mmenu2'], ''),
            (gb.infoboook[cnst.translation]['Mmenu3'], ''),
            (gb.infoboook[cnst.translation]['Mmenu4'], ''),
        ]

        if cnst.dev_mode:
            choices_main_menu.append(
                ('eval()', f'bypass to any paragraph - {Fore.LIGHTRED_EX}for testing only!!!{Style.RESET_ALL}'))

        for i, (choice_main_menu, description) in enumerate(choices_main_menu, 1):  # displaying list in main menu
            print(cnst.template.format(i, choice_main_menu, description))

        usr_input = input(f'{cnst.input_sign}{cnst.special_txt_clr} ').strip()

        if usr_input.isdigit():  # is digit
            index = int(usr_input) - 1
            if 0 <= index < len(choices_main_menu):  # is digit in range
                usr_input = choices_main_menu[index][0]

        for choice_main_menu, description in choices_main_menu:  # displaying list
            if usr_input == choice_main_menu:

                # play game
                if choice_main_menu == gb.infoboook[cnst.translation]['Mmenu1']:
                    func.clear_terminal()
                    print(f"/ {choice_main_menu}{cnst.def_txt_clr}")
                    time.sleep(cnst.delay)
                    pygame.mixer.music.fadeout(1800)
                    prg._00()

                # Rules
                elif choice_main_menu == choice_main_menu == gb.infoboook[cnst.translation]['Mmenu2']:
                    while True:
                        func.clear_terminal()
                        print(f"{cnst.special_txt_clr}/ {choice_main_menu}{cnst.def_txt_clr}")
                        time.sleep(cnst.delay)

                        choices_rules = [
                            (gb.infoboook[cnst.translation]['Mmenu1_sub1'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu1_sub2'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu1_sub3'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu1_sub4'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu1_sub5'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu1_sub6'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu1_sub7'], ''),
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
                                time.sleep(cnst.delay)

                                # Equipment and attributes
                                if choice_rules == gb.infoboook[cnst.translation]['Mmenu1_sub1']:
                                    print(gb.infoboook[cnst.translation]['Mmenu1_sub1_1a'])

                                    func.show_equipment_list()  # show equipment list

                                    print(gb.infoboook[cnst.translation]['Mmenu1_sub1_1b'])

                                # Combat
                                elif choice_rules == gb.infoboook[cnst.translation]['Mmenu1_sub2']:
                                    print(gb.infoboook[cnst.translation]['Mmenu1_sub1_2'])

                                # Escape
                                elif choice_rules == gb.infoboook[cnst.translation]['Mmenu1_sub3']:
                                    print(gb.infoboook[cnst.translation]['Mmenu1_sub1_3'])

                                # Luck
                                elif choice_rules == gb.infoboook[cnst.translation]['Mmenu1_sub4']:
                                    print(gb.infoboook[cnst.translation]['Mmenu1_sub1_4'])

                                # Leveling up attributes
                                elif choice_rules == gb.infoboook[cnst.translation]['Mmenu1_sub5']:
                                    print(gb.infoboook[cnst.translation]['Mmenu1_sub1_5'])

                                # Provisions
                                elif choice_rules == gb.infoboook[cnst.translation]['Mmenu1_sub6']:
                                    print(gb.infoboook[cnst.translation]['Mmenu1_sub1_6'])

                                # Purpose of the expedition
                                elif choice_rules == gb.infoboook[cnst.translation]['Mmenu1_sub7']:
                                    print(gb.infoboook[cnst.translation]['Mmenu1_sub1_7'])

                                elif choice_rules == gb.infoboook[cnst.translation]['return']:
                                    # print('POWODZENIA!')
                                    # time.sleep(cnst.delay)
                                    main_menu()

                                input(f'{cnst.input_sign}')

                # Settings
                elif choice_main_menu == gb.infoboook[cnst.translation]['Mmenu3']:
                    while True:
                        func.clear_terminal()
                        print(f"{cnst.special_txt_clr}/ {choice_main_menu}{cnst.def_txt_clr}")
                        time.sleep(cnst.delay)

                        choices_settings = [
                            (gb.infoboook[cnst.translation]['Mmenu3_sub1'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu3_sub2'], ''),
                            # (gb.infoboook[cnst.translation]['Mmenu3_sub3'], ''),  # currently unfinished
                            (gb.infoboook[cnst.translation]['Mmenu3_sub4'], ''),
                            (gb.infoboook[cnst.translation]['Mmenu3_sub5'], ''),
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
                                    'Mmenu3_sub1']:  # Language settings
                                    availableLocales = []
                                    for key in gb.gameboook:
                                        availableLocales.append(key)

                                    translation = str(input(
                                        f"{cnst.def_txt_clr}{gb.infoboook[cnst.translation]['Mmenu3_sub1_1']} {availableLocales}\
                                    \n{cnst.input_sign}")).lower()
                                    gb.get_translation(translation)  # update localization dictionaries
                                    func.debug_message(
                                        f"{gb.infoboook[cnst.translation]['Mmenu3_sub1_2']}: {cnst.translation}")

                                if choice_settings == gb.infoboook[cnst.translation][
                                    'Mmenu3_sub2']:  # Difficulty level settings
                                    func.clear_terminal()
                                    print(f"{cnst.special_txt_clr}// {choice_settings}{cnst.def_txt_clr}")
                                    time.sleep(cnst.delay)

                                    choices_difficulty_lvl = [
                                        (gb.infoboook[cnst.translation]['Mmenu3_sub1_3'], ''),
                                        (gb.infoboook[cnst.translation]['Mmenu3_sub1_4'], ''),
                                        (gb.infoboook[cnst.translation]['Mmenu3_sub1_5'], '')
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

                                            if choice_difficulty_lvl == gb.infoboook[cnst.translation]['Mmenu3_sub1_1']:
                                                difficulty_lvl = cnst.d_lvl_e

                                            elif choice_difficulty_lvl == gb.infoboook[cnst.translation][
                                                'Mmenu3_sub1_2']:
                                                difficulty_lvl = cnst.d_lvl_m

                                            elif choice_difficulty_lvl == gb.infoboook[cnst.translation][
                                                'Mmenu3_sub1_3']:
                                                difficulty_lvl = cnst.d_lvl_h

                                            cnst.e_mult_choice = difficulty_lvl


                                elif choice_settings == gb.infoboook[cnst.translation]['Mmenu3_sub3']:  # Audio settings

                                    func.clear_terminal()
                                    print(f"{cnst.special_txt_clr}// {choice_settings}{cnst.def_txt_clr}")
                                    time.sleep(cnst.delay)

                                    choices_sound_settings = [
                                        (gb.infoboook[cnst.translation]['Mmenu3_sub3_1'], ''),
                                        (gb.infoboook[cnst.translation]['Mmenu3_sub3_2'], ''),
                                        (gb.infoboook[cnst.translation]['Mmenu3_sub3_3'], ''),
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
                                                cnst.def_action_volume = new_volume

                                            elif choice_sound_settings == gb.infoboook[cnst.translation][
                                                'Mmenu3_sub3_2']:
                                                cnst.def_sfx_volume = new_volume

                                            elif choice_sound_settings == gb.infoboook[cnst.translation][
                                                'Mmenu3_sub3_3']:
                                                cnst.def_bckg_volume = new_volume
                                                pygame.mixer.music.set_volume(new_volume)

                                            elif choice_sound_settings == gb.infoboook[cnst.translation]['return']:
                                                main_menu()

                                elif choice_settings == gb.infoboook[cnst.translation]['Mmenu3_sub4']:  # Name setting
                                    time.sleep(cnst.delay)

                                    name = input(
                                        f"{gb.infoboook[cnst.translation]['Mmenu3_sub4_1']}{cnst.input_sign}")
                                    cnst.player_name = f"{Fore.LIGHTYELLOW_EX}{name}{cnst.def_txt_clr}"

                                    if name == '':
                                        func.name_randomizer()

                                elif choice_settings == gb.infoboook[cnst.translation][
                                    'Mmenu3_sub5']:  # Randomize atributes
                                    time.sleep(cnst.delay)
                                    print(gb.infoboook[cnst.translation][
                                              'Mmenu3_sub5_1'])
                                    func.loading(20)
                                    func.rpar()
                                    func.show_player_stats()
                                    input(f'\r{cnst.input_sign}')

                                elif choice_settings == gb.infoboook[cnst.translation]['return']:
                                    main_menu()

                # Exit game
                elif choice_main_menu == gb.infoboook[cnst.translation]['Mmenu4']:
                    choice2 = input(f"{gb.infoboook[cnst.translation]['Mmenu4_sub1_1']} [Y/N]:").lower()
                    if choice2.upper() == "Y":
                        func.clear_terminal()
                        time.sleep(cnst.delay)
                        pygame.mixer.music.fadeout(2200)
                        func.loading(10)
                        exit()

                elif choice_main_menu == 'eval()':  # only for dev purposes; evaluating functions in paragraphs.py
                    time.sleep(cnst.delay)
                    prg._xx()  # calling placeholder function


# main menu
func.get_music('main')  # loading background music
func.rpar()  # loading player parameters
os.system('cls')

if cnst.dev_mode:
    gb.get_translation('pl')  # default language for dev_mode
else:
    gb.get_translation('en')  # default language for normal game
main_menu()  # entry point
