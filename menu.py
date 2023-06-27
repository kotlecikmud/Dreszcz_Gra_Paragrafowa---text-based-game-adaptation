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
import time, pygame, msvcrt, os, random
import functions, constants, paragraphs
import gamebook as gb
from colorama import Fore, Style

# check if the assets audio path exists, and if not, display an error message and exit the program
if not os.path.exists(constants.assets_audio_pth):
    functions.error_message('', 'assets path not found')
    input('press any key to exit...')
    exit()


def main_menu():
    while True:
        if constants.ver_num != '':
            print(f'ver.{constants.debug_txt_clr}{constants.ver_num}')
            time.sleep(2)

        functions.clear_terminal()
        print(f'{constants.def_txt_clr}Witaj {constants.player_name}!\
        \n{constants.special_txt_clr}MENU GŁÓWNE{constants.def_txt_clr}')
        time.sleep(constants.delay)

        choices_main_menu = [
            ('Graj', 'play'),
            ('Zasady Gry', 'read the rules'),
            ('Ustawienia', 'settings'),
            ('Wyjdź z gry', 'exit game'),
        ]

        if constants.dev_mode:
            choices_main_menu.append(
                ('eval()', f'{Fore.LIGHTRED_EX}evaluating paragraph functions, for dev only{Style.RESET_ALL}'))

        for i, (choice_main_menu, description) in enumerate(choices_main_menu, 1):  # displaying list in main menu
            print(constants.template.format(i, choice_main_menu, description))

        usr_input = input(f'{constants.input_sign}{constants.special_txt_clr} ').strip()

        if usr_input.isdigit():  # is digit
            index = int(usr_input) - 1
            if 0 <= index < len(choices_main_menu):  # is digit in range
                usr_input = choices_main_menu[index][0]

        for choice_main_menu, description in choices_main_menu:  # displaying list
            if usr_input == choice_main_menu:

                if choice_main_menu == 'Graj':  # Play
                    functions.clear_terminal()
                    print(f"/ {choice_main_menu}{constants.def_txt_clr}")
                    time.sleep(constants.delay)
                    pygame.mixer.music.fadeout(1800)
                    paragraphs.par_00()

                elif choice_main_menu == 'Zasady Gry':  # Rules
                    while True:
                        functions.clear_terminal()
                        print(f"{constants.special_txt_clr}/ {choice_main_menu}{constants.def_txt_clr}")
                        time.sleep(constants.delay)

                        choices_rules = [
                            ('Wyposażenie i cechy', 'Equipment and attributes'),
                            ('Walka', 'Combat'),
                            ('Ucieczka', 'Escape'),
                            ('Szczęście', 'Luck'),
                            ('Podwyższanie poziomu cech', 'Leveling up attributes'),
                            ('Prowiant', 'Provisions'),
                            ('Cel wyprawy', 'Purpose of the expedition'),
                            ('wróć', 'go back')
                        ]

                        for i, (choice_rules, description) in enumerate(choices_rules, 1):
                            print(constants.template.format(i, choice_rules, description))

                        usr_input = input(f'{constants.special_txt_clr} ').strip()

                        if usr_input.isdigit():
                            index = int(usr_input) - 1
                            if 0 <= index < len(choices_rules):
                                usr_input = choices_rules[index][0]

                        for choice_rules, description in choices_rules:
                            if usr_input == choice_rules:
                                functions.clear_terminal()
                                print(f"{constants.special_txt_clr}// {choice_rules}{constants.def_txt_clr}")
                                time.sleep(constants.delay)

                                if choice_rules == 'Wyposażenie i cechy':
                                    print('Jesteś Śmiałkiem.\
                                        \n\
                                        \nTwój ekwipunek to:')

                                    functions.show_equipment_list()  # show equipment list

                                    print(f'Wędrując po podziemiach będziesz znajdował inne rodzaje broni i przedmioty.\
                                        \nPamiętaj, że - poza mieczem - każda broń może być wykorzystana tylko raz.\
                                        \nPodobnie, znajdowane przedmioty są jednorazowego użytku.\
                                        \nMożesz zabrać ze sobą jedną butelkę eliksiru.\
                                        \nWybierasz spośród eliksirów: {constants.special_txt_clr}ZRĘCZNOŚCI{constants.def_txt_clr}, {constants.special_txt_clr}WYTRZYMAŁOŚCI{constants.def_txt_clr} i {constants.special_txt_clr}SZCZĘŚCIA{constants.def_txt_clr}.\
                                        \nMożna wypić go w dowolnym momencie, ale tylko dwukrotnie podczas przygody.\
                                        \n{constants.def_txt_clr}Twoje cechy to: ZRĘCZNOŚĆ, WYTRZYMAŁOŚĆ i SZCZĘŚCIE.\
                                        \nPrzed zejściem do podziemi losowane są początkowe poziomy tych cech.\
                                        \nIch poziom będzie się nieustannie zmieniał podczas wędrówki,\
                                        \nale nie może przekroczyć poziomu początkowego.')

                                elif choice_rules == 'Walka':
                                    print(f'Będziesz walczył z potworami. Ich cechy (ZRĘCZNOŚĆ i WYTRZYMAŁOŚĆ) są indywidualne dla każdego wroga.\
                                        \nW bieżącej wersji gry walki są wykonywane automatycznie. Do końca walki nie ma możliwości interackji,\
                                        \nchyba że tekst przewiduje możliwość ucieczki.')

                                elif choice_rules == 'Ucieczka':
                                    print('Będąc w niebezpieczeństwie możesz ratować się Ucieczką, o ile tekst to przewiduje.\
                                        \nJeśli uciekasz, potwór zadaje ci ranę: odejmij 2 od swojej WYTRZYMAŁOŚCI.\
                                        \nPodczas Ucieczki (przed walką lub w jej trakcie) możesz zastosować SSS w opisany niżej sposób.')

                                elif choice_rules == 'Szczęście':
                                    print('Podczas wędrówki sprawdzasz, czy szczęście ci sprzyja. Robisz to w następujący sposób:\
                                        \nRzucasz 2K. Jeśli wynik jest równy lub mniejszy od aktualnego poziomu SZCZĘŚCIA, to masz SZCZĘŚCIE.\
                                        \nJeśli wynik jest większy, nie masz SZCZĘŚCIA.\
                                        \nTa procedura nazywa się Sprawdzanie Swojego Szczęścia (SSS).\
                                        \nPo każdym SSS - niezależnie od wyniku - należy odjąć 1 od aktualnego poziomu SZCZĘŚCIA.\
                                        \nSSS trzeba zrobić, gdy przewiduje to tekst, a także można zrobić podczas walki.\
                                        \nPodczas walki SSS robi się w odpowiednim momencie rundy (patrz wyżej), a jego wynik stosuje się tylko do tej rundy.\
                                        \nOto jakie znaczenie dla przebiegu walki ma SSS:\
                                        \n\
                                        \n1. Gdy zadałeś ranę potworowi\
                                        \n- jeśli masz SZCZĘŚCIE, to odejmujesz dodatkowo 2 od WYTRZYMAŁOŚCI potwora (łącznie -4).\
                                        \n- jeśli nie masz SZCZĘŚCIA, to odejmujesz łącznie 1.\
                                        \n2. Gdy potwór zadał ci ranę\
                                        \n- jeśli masz SZCZĘŚCIE, to odejmujesz łącznie 1 od swojej WYTRZYMAŁOŚCI\
                                        \n- jeśli nie masz SZCZĘŚCIA, to odejmujesz łącznie 3.')

                                elif choice_rules == 'Podwyższanie poziomu cech':
                                    print(f'Podczas wędrówki, dzięki przygodom i walce, zmienia się poziom twoich cech.\
                                        \n1. ZRĘCZNOŚĆ - niewiele się zmienia\
                                        \n- zaczarowana broń podwyższa ZRĘCZNOŚĆ\
                                        \n- eliksir ZRĘCZNOŚCI przywraca poziom początkowy\
                                        \n2. WYTRZYMAŁOŚĆ - nieustannie się zmienia\
                                        \n- każdy posiłek (masz ich na starcie {constants.eatables_count}) dodaje {constants.eatable_W_load} punkty\
                                        \n- eliksir WYTRZYMAŁOŚCI przywraca poziom początkowy\
                                        \n3. SZCZĘŚCIE\
                                        \n- udane przygody dodają punkty\
                                        \n- eliksir SZCZĘŚCIA przywraca poziom początkowy, a nawet podnosi go o 1.\
                                        \nPoza tym przypadkiem, ZRĘCZNOŚĆ, WYTRZYMAŁOŚĆ i SZCZĘŚCIE nie mogą przekroczyć poziomu początkowego.')

                                elif choice_rules == 'Prowiant':
                                    print(f'W plecaku masz Prowiant, który wystarcza na {constants.eatables_count} posiłków. Posiłek można zjeść TYLKO wówczas, gdy przewiduje to tekst.\
                                        \nZa jednym razem można zjeść tylko jeden posiłek. Spożywszy posiłek, dostajesz {constants.eatable_W_load} do swojej WYTRZYMAŁOŚCI.')

                                elif choice_rules == 'Cel wyprawy':
                                    print('Twoim celem jest dotarcie do skarbca. Będziesz wędrował przez labirynt korytarzy.\
                                        \nOdwiedzisz wiele komnat, w których żyją różne istoty. Spotkają cię rozmaite niespodzianki.\
                                        \nZapewne wpadniesz w jakieś pułapki.\
                                        \nZnalezienie właściwej drogi i pokonanie potworów nie będzie łatwe.\
                                        \nZapewne będziesz musiał podjąć kilka wypraw, zanim uda ci się dotrzeć do celu.\
                                        \nZa każdym razem rysuj mapę podziemi. Bardzo ci pomoże.')

                                elif choice_rules == 'wróć':
                                    print('POWODZENIA!')
                                    time.sleep(constants.delay)
                                    main_menu()

                                input(f'{constants.input_sign}')


                elif choice_main_menu == 'Ustawienia':  # Settings main
                    while True:
                        functions.clear_terminal()
                        print(f"{constants.special_txt_clr}/ {choice_main_menu}{constants.def_txt_clr}")
                        time.sleep(constants.delay)

                        choices_settings = [
                            ('Język', 'change language'),
                            ('Poziom trudności', 'set difficulty level'),
                            # ('Dźwięk', 'change sound levels'),  # currently broken, planning to solve issue with this later
                            ('Imię postaci', 'change characters name'),
                            ('Losuj nowe atrybuty postaci', 'randomize player stats'),
                            ('wróć', 'go back')
                        ]

                        for i, (choice_settings, description) in enumerate(choices_settings, 1):
                            print(constants.template.format(i, choice_settings, description))

                        usr_input = input(f'{constants.special_txt_clr} ').strip()

                        if usr_input.isdigit():
                            index = int(usr_input) - 1
                            if 0 <= index < len(choices_settings):
                                usr_input = choices_settings[index][0]

                        for choice_settings, description in choices_settings:
                            if usr_input == choice_settings:

                                if choice_settings == 'Język':  # Language settings
                                    availableLocales = []
                                    for key in gb.gameboook:
                                        availableLocales.append(key)

                                    translation = str(input(f'{constants.def_txt_clr}Choose language {availableLocales}\
                                    \n{constants.input_sign}')).lower()
                                    gb.get_translation(translation)
                                    functions.debug_message(f'wybrałeś: {constants.translation}')

                                if choice_settings == 'Poziom trudności':
                                    functions.clear_terminal()
                                    print(f"{constants.special_txt_clr}// {choice_settings}{constants.def_txt_clr}")
                                    time.sleep(constants.delay)

                                    choices_difficulty_lvl = [
                                        ('łatwy', 'easy'),
                                        ('średni', 'medium'),
                                        ('trudny', 'hard')
                                    ]

                                    for i, (choice_difficulty_lvl, description) in enumerate(choices_difficulty_lvl, 1):
                                        print(constants.template.format(i, choice_difficulty_lvl, description))

                                    usr_input = input(f'{constants.special_txt_clr} ').strip()

                                    if usr_input.isdigit():
                                        index = int(usr_input) - 1
                                        if 0 <= index < len(choices_difficulty_lvl):
                                            usr_input = choices_difficulty_lvl[index][0]

                                    difficulty_lvl = None
                                    for choice_difficulty_lvl, description in choices_difficulty_lvl:
                                        if usr_input == choice_difficulty_lvl:

                                            if choice_difficulty_lvl == 'łatwy':
                                                difficulty_lvl = constants.d_lvl_e

                                            elif choice_difficulty_lvl == 'średni':
                                                difficulty_lvl = constants.d_lvl_m

                                            elif choice_difficulty_lvl == 'trudny':
                                                difficulty_lvl = constants.d_lvl_h

                                            constants.e_mult_choice = difficulty_lvl


                                elif choice_settings == 'Dźwięk':  # Audio settings

                                    functions.clear_terminal()
                                    print(f"{constants.special_txt_clr}// {choice_settings}{constants.def_txt_clr}")
                                    time.sleep(constants.delay)

                                    choices_sound_settings = [
                                        ('Dialogi', 'Adjusts the volume of dialogues.'),
                                        ('Efekty', 'Adjusts the volume of sound effects.'),
                                        ('Muzyka', 'Adjusts the volume of background music.'),
                                        ('wróć', 'Return to the main menu.')
                                    ]

                                    for i, (choice_sound_settings, description) in enumerate(choices_sound_settings, 1):
                                        print(constants.template.format(i, choice_sound_settings, description))

                                    usr_input = input(f'{constants.special_txt_clr} ').strip()

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

                                            if choice_sound_settings == 'Dialogi':
                                                constants.def_action_volume = new_volume

                                            elif choice_sound_settings == 'Efekty':
                                                constants.def_sfx_volume = new_volume

                                            elif choice_sound_settings == 'Muzyka':
                                                constants.def_bckg_volume = new_volume
                                                pygame.mixer.music.set_volume(new_volume)

                                            elif choice_sound_settings == 'wróć':
                                                main_menu()


                                elif choice_settings == 'Imię postaci':  # Name setting
                                    time.sleep(constants.delay)

                                    name = input(
                                        f"Wybierz imię bohatera (wpisz 'los' aby wylosować imię){constants.input_sign}")
                                    constants.player_name = f"{Fore.LIGHTYELLOW_EX}{name}{constants.def_txt_clr}"

                                    if name == 'los':
                                        functions.name_randomizer()

                                elif choice_settings == 'Losuj nowe atrybuty postaci':  # Randomize atributes
                                    time.sleep(constants.delay)
                                    print(f"Losowanie początkowych statystyk bohatera")
                                    functions.loading(2)
                                    functions.rpar()
                                    functions.show_player_stats()
                                    input(f'\r{constants.input_sign}')

                                elif choice_settings == 'wróć':
                                    main_menu()

                elif choice_main_menu == 'Wyjdź z gry':
                    choice2 = input("Czy na pewno? [T/N]: ")
                    if choice2.upper() == "T":
                        functions.clear_terminal()
                        time.sleep(constants.delay)
                        pygame.mixer.music.fadeout(2200)
                        functions.loading(2.2)
                        exit()

                elif choice_main_menu == 'eval()':  # only for dev purposes; evaluating functions in paragraphs.py
                    time.sleep(constants.delay)
                    paragraphs._xx()  # calling placeholder function


# loading background music
rnd_choice = random.choice(constants.music_main)  # losowanie muzyki z listy
pygame.mixer.music.load(rnd_choice)
pygame.mixer.music.set_volume(constants.def_bckg_volume)
pygame.mixer.music.play(-1)  # loop

# main menu
functions.rpar()  # loading player parameters
os.system('cls')

if constants.dev_mode:
    gb.get_translation('en')
else:
    gb.get_translation('pl')

main_menu()  # enterance point
