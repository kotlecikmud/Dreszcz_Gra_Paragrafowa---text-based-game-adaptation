import time, random
import constants, functions, entities
from obj_class import *
import gamebook as gb


# - - - - - - - - -
# /// PARAGRAPHS
# - - - - - - - - -
def _xx():  # placeholder
    pygame.mixer.music.fadeout(1200)
    while True:
        odp = input(f"--placeholder function--\
                \n\
                \npress enter to return to _64()\
                \nor type any command here:\
                \n{constants.input_sign}")

        rnd_choice = random.choice(constants.music_main)  # losowanie muzyki z listy
        pygame.mixer.music.load(rnd_choice)
        pygame.mixer.music.set_volume(constants.def_bckg_volume)
        pygame.mixer.music.play(-1)

        if len(odp) > 0:
            eval(odp)

        else:
            print('returning to _64()')
            time.sleep(1.5)
            _64()


# - - - - - - - - -
def par_00():
    functions.dub_play(gb.gameboook_00a, 'audiobook_adam_000a.mp3', 'adam')

    while True:
        functions.dub_play(f'{constants.special_txt_clr}Wybierz eliksir:\
            \n1. Zręczności\
            \n2. Wytrzymałości\
            \n3. Szczęścia', 'audiobook_adam_elxr_choice.mp3', 'adam')
        choice = input(f'{constants.input_sign}')

        if choice == '1':
            potion = 'zręczności'
            break
        elif choice == '2':
            potion = 'wytrzymałości'
            break
        elif choice == '3':
            potion = 'szczęścia'
            break
        else:
            functions.clear_terminal()
            print(f"{constants.special_txt_clr}Niepoprawny wybór.")

    functions.loading(1)
    functions.clear_terminal()
    print(f"/// eliksir {potion} = {constants.count_potion}/2\
            \n{constants.def_txt_clr}")
    time.sleep(2)

    rnd_choice = random.choice(constants.music_main)  # losowanie muzyki z listy
    pygame.mixer.music.load(rnd_choice)
    pygame.mixer.music.set_volume(constants.def_bckg_volume)
    pygame.mixer.music.play(-1)

    functions.clear_terminal()
    functions.dub_play(gb.gameboook_00b, 'audiobook_adam_000b.mp3', 'adam')
    path_strings = [f'Ruszaj {constants.input_sign}']
    actions = ['paragraphs._01()']
    functions.pth_selector(path_strings, actions)


def _01():
    functions.dub_play(gb.gameboook_01, 'audiobook_adam_001.mp3', 'adam')
    path_strings = []
    actions = ['paragraphs._25()']
    functions.pth_selector(path_strings, actions)


def _02():
    functions.dub_play(gb.gameboook_03, 'audiobook_adam_002.mp3', 'adam')
    # initiate combat with entity_002
    functions.combat_init(entities.entity_002, True, entities.entity_002.esc_possible, 'paragraphs._372(', '',
                          'paragraphs._380()')


def _03():
    functions.dub_play(gb.gameboook_03, 'audiobook_adam_003.mp3', 'adam')
    path_strings = ['Spróbuj jeszcze raz (wymagane conajmniej 13 sztuk złota)', 'Wyciągnij z plecaka linę',
                    'Podejdź do mostu', 'Spróbuj przeskoczyć przez rozpadlinę (przynajmniej 18W i 9Z)']
    actions = ['paragraphs._136()', 'paragraphs._13()', 'paragraphs._269()', 'paragraphs._74()', 'paragraphs._110()']
    functions.pth_selector(path_strings, actions)


def _04():
    functions.dub_play(gb.gameboook_04, 'audiobook_adam_004.mp3', 'adam')
    path_strings = ['Chwytasz za miecz i atakujesz', 'Postanawiasz czekać dalej']
    actions = ['paragraphs._318()', 'paragraphs._295()']
    functions.pth_selector(path_strings, actions)


def _05():
    functions.dub_play(gb.gameboook_05, 'audiobook_adam_005.mp3', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['paragraphs._312()', 'paragraphs._140()']
    functions.pth_selector(path_strings, actions)


def _06a():
    functions.stats_change('Szczęście', constants.s_count, 1)
    path_strings = []
    actions = ['paragraphs._06b()']
    functions.pth_selector(path_strings, actions)


def _06b():
    functions.dub_play(gb.gameboook_06, 'audiobook_adam_006.mp3', 'adam')
    path_strings = []
    actions = ['paragraphs._115()']
    functions.pth_selector(path_strings, actions)


def _07():
    functions.dub_play(gb.gameboook_07, 'audiobook_adam_007.mp3', 'adam')
    path_strings = []
    actions = ['paragraphs._219()']
    functions.pth_selector(path_strings, actions)


def _08():
    functions.dub_play(gb.gameboook_08, 'audiobook_adam_008.mp3', 'adam')
    path_strings = ['Walcz u boku prześladowanego stwora przeciw zgrai jego współplemieńców', 'Ratuj się Ucieczką']
    actions = ['paragraphs._210()', 'paragraphs._98()']
    functions.pth_selector(path_strings, actions)


def _09():
    functions.dub_play(gb.gameboook_09, 'audiobook_adam_009.mp3', 'adam')
    path_strings = ['Sprzedaj kamień krasnalowi', 'Nie sprzedawaj kamienia']
    actions = ['paragraphs._289()', 'paragraphs._375()']
    functions.pth_selector(path_strings, actions)


def _10():
    functions.dub_play(gb.gameboook_10, 'audiobook_adam_010.mp3', 'adam')
    _xx()


def _11():
    pygame.mixer.music.fadeout(2600)
    music = f'{constants.assets_audio_music_pth}/scene_11_background.mp3'
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(constants.def_bckg_volume)
    pygame.mixer.music.play(-1)

    functions.dub_play(gb.gameboook_11, 'dreszcz_p_011.mp3')
    path_strings = ['idziesz od razu po wodę', 'dobierasz się do stwora']
    actions = ['paragraphs._45()', 'paragraphs._192()']
    functions.pth_selector(path_strings, actions)


def _12():
    functions.dub_play(gb.gameboook_12, 'audiobook_adam_012.mp3', 'adam')
    path_strings = []
    actions = ['paragraphs._288()']
    functions.pth_selector(path_strings, actions)


def _13():
    functions.dub_play(gb.gameboook_13, 'audiobook_adam_013.mp3', 'adam')
    functions.stats_change('Wytrzymałość', constants.w_count, -2)
    print('Ale to tylko chwila. Wielkimi susami biegniesz w kierunku potwora')
    path_strings = []
    actions = ['paragraphs._126()']
    functions.pth_selector(path_strings, actions)


def _14():
    path_strings = ['Wychodzisz północnymi drzwiami', 'Wychodzisz wschodnimi drzwiami']
    actions = ['paragraphs._197()', 'paragraphs._39()']
    functions.pth_selector(path_strings, actions)


def _15():
    path_strings = ['Rezygnujesz z przepłynięcia jeziora', 'Decydujesz się podjąć próbę przepłynięcia jeziora']
    actions = ['paragraphs._241()', 'paragraphs._113()']
    functions.pth_selector(path_strings, actions)
    # print('Jeśli rezygnujesz z przepłynięcia jeziora - patrz 241\
    # \nNatomiast jeśli decydujesz się podjąć próbę przepłynięcia jeziora, zapisz numer niniejszego paragrafu i patrz 113')


def _16():
    functions.dub_play(gb.gameboook_16a, 'audiobook_adam_016a.mp3', 'adam')
    functions.eatables()
    print(gb.gameboook_16b)
    path_strings = []
    actions = ['paragraphs._80()']
    functions.pth_selector(path_strings, actions)


def _17():
    path_strings = ['Zobacć co za nimi jest', 'Wycofaj się']
    actions = ['paragraphs._265()', 'paragraphs._50()']
    functions.pth_selector(path_strings, actions)


def _18():
    functions.dub_play(gb.gameboook_18, 'audiobook_adam_018.mp3', 'adam')
    path_strings = ['Jeśli tak, pamiętaj że musisz mieć przynajmniej 5 sztuk złota', 'Wycofujesz się']
    actions = ['paragraphs._211()', 'paragraphs._286()']
    functions.pth_selector(path_strings, actions)


def _19():
    functions.dub_play(gb.gameboook_19, 'audiobook_adam_019.mp3', 'adam')
    functions.stats_change('Prowiant', constants.eatables_count, 1)
    functions.stats_change('Szczęście', constants.s_count, 2)
    path_strings = []
    actions = ['paragraphs._141()']
    functions.pth_selector(path_strings, actions)


def _20():
    functions.dub_play(gb.gameboook_20, 'audiobook_adam_020.mp3', 'adam')
    path_strings = []
    actions = ['paragraphs._238a()']
    functions.pth_selector(path_strings, actions)


def _21():
    path_strings = ['Zobacz co jest za drzwiami', 'Zawróć']
    actions = ['paragraphs._332()', 'paragraphs._212()']
    functions.pth_selector(path_strings, actions)


def _22():
    functions.dub_play(gb.gameboook_22, 'audiobook_adam_022.mp3', 'adam')
    _xx()


def _23():
    functions.dub_play(gb.gameboook_23, 'audiobook_adam_023.mp3', 'adam')
    _xx()


def _24():
    functions.dub_play(gb.gameboook_24, 'audiobook_adam_024.mp3', 'adam')
    _xx()


def _25():
    functions.dub_play(gb.gameboook_25, 'audiobook_adam_025.mp3', 'adam')
    path_strings = ['Idziesz na zachód', 'Wybierasz drogę prowadzącą na wschód']
    actions = ['paragraphs._200()', 'paragraphs._44()']
    functions.pth_selector(path_strings, actions)


def _26():
    functions.dub_play(gb.gameboook_26, 'audiobook_adam_026.mp3', 'adam')
    _xx()


def _27():
    functions.dub_play(gb.gameboook_27, 'audiobook_adam_027.mp3', 'adam')
    _xx()


def _28():
    functions.dub_play(gb.gameboook_28, 'audiobook_adam_028.mp3', 'adam')
    if constants.w_count >= 18:
        _177()
    else:
        _330()


def _29():
    functions.dub_play(gb.gameboook_29, 'dreszcz_p_029.mp3')
    path_strings = []
    actions = ['paragraphs._116a()']
    functions.pth_selector(path_strings, actions)


def _30():
    functions.dub_play(gb.gameboook_30, 'dreszcz_p_30.mp3')
    _xx()


def _31():
    functions.dub_play(gb.gameboook_31, 'dreszcz_p_31.mp3')
    path_strings = []
    actions = ['paragraphs._119()']
    functions.pth_selector(path_strings, actions)


def _32():
    functions.dub_play(gb.gameboook_32, 'dreszcz_p_32.mp3')
    _xx()


def _33():
    functions.dub_play(gb.gameboook_33, 'dreszcz_p_33.mp3')
    _xx()


def _34():
    functions.dub_play(gb.gameboook_34, 'dreszcz_p_34.mp3')
    _xx()


def _35():
    functions.dub_play(gb.gameboook_35, 'dreszcz_p_35.mp3')
    _xx()


def _36():
    functions.dub_play(gb.gameboook_36, 'dreszcz_p_36.mp3')
    _xx()


def _37():
    functions.update_num_variable(constants.choice_count, 1)
    if constants.choice_count < 3:
        eval('_115()')
    else:
        eval('_68()')


def _38():
    functions.dub_play(gb.gameboook_38, 'dreszcz_p_38.mp3')
    _xx()


def _39():
    functions.dub_play(gb.gameboook_39, 'dreszcz_p_039.mp3')
    path_strings = ['zachód', 'północ', 'południe']
    actions = ['paragraphs._331()', 'paragraphs._228()', 'paragraphs._146()']
    functions.pth_selector(path_strings, actions)


def _43():
    functions.dub_play(gb.gameboook_43, 'dreszcz_p_43.mp3')
    _xx()


def _44():
    functions.dub_play(gb.gameboook_44, 'audiobook_adam_044.mp3', 'adam')
    path_strings = ['Rezygnujesz', 'Wyważasz drzwi']
    actions = ['paragraphs._75()', 'paragraphs._105()']
    functions.pth_selector(path_strings, actions)


def _45():
    functions.dub_play(gb.gameboook_45, 'audiobook_adam_045.mp3', 'adam')
    functions.stats_change('Szczęscie', constants.s_count, 2)
    path_strings = []
    actions = ['paragraphs._251()']
    functions.pth_selector(path_strings, actions)


def _46():
    functions.dub_play(gb.gameboook_46, 'dreszcz_p_46.mp3')
    _xx()


def _47():
    functions.dub_play(gb.gameboook_47, 'dreszcz_p_47.mp3')
    _xx()


def _48():
    functions.dub_play(gb.gameboook_48, 'dreszcz_p_48.mp3')
    _xx()


def _49():
    functions.dub_play(gb.gameboook_49, 'dreszcz_p_49.mp3')
    _xx()


def _50():
    functions.dub_play(gb.gameboook_50, 'dreszcz_p_50.mp3')
    path_strings = ['północ', 'wschód', 'zachód']
    actions = ['paragraphs._310()', 'paragraphs._130()', 'paragraphs._64()']
    functions.pth_selector(path_strings, actions)


def _56():
    functions.dub_play(gb.gameboook_56, 'dreszcz_p_056.mp3')
    functions.stats_change('Wytrzymałość', constants.w_count, -1)
    path_strings = []
    actions = ['paragraphs._75()']
    functions.pth_selector(path_strings, actions)


def _59():
    functions.dub_play(gb.gameboook_59, 'dreszcz_p_59.mp3')
    path_strings = ['tak', 'nie']
    actions = ['paragraphs._14()', 'paragraphs._70()']
    functions.pth_selector(path_strings, actions)


def _67():
    functions.dub_play(gb.gameboook_64, 'audiobook_adam_067.mp3', 'adam')
    path_strings = ['Musisz się wycofać.']
    actions = ['paragraphs._50()']
    functions.pth_selector(path_strings, actions)


def _64():
    functions.dub_play(gb.gameboook_64, 'audiobook_adam_064.mp3', 'adam')
    path_strings = ['zachód', 'północ', 'wschód', 'południe']
    actions = ['paragraphs._296()', 'paragraphs._264()', 'paragraphs._284()', 'paragraphs._224()']
    functions.pth_selector(path_strings, actions)


def _69a():
    functions.dub_play(gb.gameboook_69a, 'dreszcz_p_69a.mp3')
    functions.combat_init(entities.entity_069_1, True, entities.entity_069_1.esc_possible, '', '', 'paragraphs._69b()')


def _69b():
    functions.dub_play(gb.gameboook_69b, 'dreszcz_p_69b.mp3')
    functions.combat_init(entities.entity_069_2, True, entities.entity_069_2.esc_possible, '', '', 'paragraphs._69c()')


def _69c():
    functions.dub_play(gb.gameboook_69c, 'dreszcz_p_69c.mp3')
    path_strings = ['tak', 'nie']
    actions = ['paragraphs._305()', 'paragraphs._291()']
    functions.pth_selector(path_strings, actions)


def _70():
    functions.dub_play(gb.gameboook_70, 'dreszcz_p_70.mp3')
    _xx()


def _75():
    functions.dub_play(gb.gameboook_75, 'dreszcz_p_075.mp3')
    path_strings = []
    actions = ['paragraphs._200()']
    functions.pth_selector(path_strings, actions)


def _76():
    functions.dub_play(gb.gameboook_76, 'dreszcz_p_76.mp3')
    _xx()


def _82():
    functions.dub_play(gb.gameboook_82, 'dreszcz_p_82.mp3')
    _xx()


def _89():
    functions.dub_play(gb.gameboook_89a, 'dreszcz_p_089a.mp3')
    functions.stats_change('Szczęscie', constants.s_count, 2)
    functions.stats_change('Złoto', constants.gold_amount, 3)
    functions.dub_play(gb.gameboook_89b, 'dreszcz_p_089b.mp3')
    path_strings = []
    actions = ['paragraphs._120()']
    functions.pth_selector(path_strings, actions)


def _95():
    functions.update_num_variable(constants.choice_count, 1)
    if constants.choice_count < 3:
        eval('_115()')
    else:
        eval('_68()')


def _100():
    functions.dub_play(gb.gameboook_100, 'dreszcz_p_100.mp3')
    _xx()


def _101():
    print(f'{entities.entity_184.name} prosi o łaskę.')
    path_strings = ['Darujesz mu życie', 'Walczysz aż do końca']
    actions = ['paragraphs._362()', 'paragraphs._234()']
    functions.pth_selector(path_strings, actions)


def _102():
    functions.dub_play(gb.gameboook_102, 'dreszcz_p_102.mp3')
    path_strings = ['zachód', 'północ', 'wschód', 'południe']
    actions = ['paragraphs._123()', 'paragraphs._268()', 'paragraphs._374()', 'paragraphs._351()']
    functions.pth_selector(path_strings, actions)


def _103():
    functions.dub_play(gb.gameboook_103, 'dreszcz_p_103.mp3')
    path_strings = []
    actions = ['paragraphs._345()']
    functions.pth_selector(path_strings, actions)


def _104():
    functions.dub_play(gb.gameboook_104, 'dreszcz_p_104.mp3')
    path_strings = []
    actions = ['paragraphs._121()']
    functions.pth_selector(path_strings, actions)


def _105():
    functions.dub_play(gb.gameboook_105, 'audiobook_adam_105.mp3', 'adam')
    functions.stats_change('Wytrzymałość', constants.w_count, -1)
    print('Czy chcesz ponowić próbę?')
    path_strings = ['tak', 'nie']
    actions = ['paragraphs._56()', 'paragraphs._75()']
    functions.pth_selector(path_strings, actions)


def _106():
    functions.dub_play(gb.gameboook_106, 'dreszcz_p_106.mp3')
    path_strings = ['Broń się mieczem', 'Masz jedno albo drugie', 'Masz jedno i drugie']
    actions = ['_213()', '_24()', '_292()']
    functions.pth_selector(path_strings, actions)


def _107():
    # initiate combat with entity_107
    functions.combat_init(entities.entity_107, True, entities.entity_107.esc_possible, '', '', '_23()')


def _112():
    value = random.randint(4, 48)
    if value >= 18:
        print('Szczęście ci sprzyja')
        _28()
    else:
        print('Szczęście ci nie sprzyja')
        _291()


def _113():
    functions.dub_play(gb.gameboook_113, 'dreszcz_p_113.mp3')
    path_strings = ['blank', 'blank']
    actions = ['paragraphs._xx()', 'paragraphs._xx()']
    functions.pth_selector(path_strings, actions)


def _115():
    functions.debug_message(f'constants.choice_count = {constants.choice_count}')

    functions.dub_play(gb.gameboook_115, 'dreszcz_p_115.mp3')

    constants.choice_count = 0

    while True:
        for i, (choice, action) in enumerate(constants.choices_115.items(), 1):
            print(f"{i}. {choice}")

        usr_input = input("Wybierz opcję: ").strip()

        if usr_input.isdigit():
            index = int(usr_input) - 1
            if 0 <= index < len(constants.choices_115):
                usr_input = list(constants.choices_115.keys())[index]

        if usr_input in constants.choices_115:
            break
        else:
            print("Nieprawidłowy wybór.")

    constants.main_eq.append(usr_input)

    functions.eq_change(usr_input)

    eval(constants.choices_115[usr_input])


def _116a():
    functions.dub_play(gb.gameboook_116a, 'dreszcz_p_116a.mp3')
    functions.combat_init(entities.entity_116, entities.entity_116.state, entities.entity_116.esc_possible, '', '',
                          'paragraphs._116b()')


def _116b():
    functions.dub_play(gb.gameboook_116b, 'dreszcz_p_116b.mp3')
    path_strings = ['Rozejrzyj się', 'Opuść pieczarę']
    actions = ['paragraphs._89()', 'paragraphs._120()']
    functions.pth_selector(path_strings, actions)


def _119():
    functions.dub_play(gb.gameboook_119, 'dreszcz_p_119.mp3')
    path_strings = ['Przeszukaj ciało', 'Opuść komnatę']
    actions = ['paragraphs._31()', 'paragraphs._102()']
    functions.pth_selector(path_strings, actions)


def _120():
    functions.dub_play(gb.gameboook_120, 'dreszcz_p_120.mp3')
    path_strings = []
    actions = ['paragraphs._64()']
    functions.pth_selector(path_strings, actions)


def _123():
    functions.dub_play(gb.gameboook_123, 'dreszcz_p_123.mp3')
    path_strings = []
    actions = ['paragraphs._39()']
    functions.pth_selector(path_strings, actions)


def _128():
    functions.dub_play(gb.gameboook_128, 'dreszcz_p_128.mp3')
    _xx()


def _130():
    functions.dub_play(gb.gameboook_130, 'dreszcz_p_130.mp3')
    path_strings = []
    actions = ['paragraphs._212()']
    functions.pth_selector(path_strings, actions)


def _132():
    functions.dub_play(gb.gameboook_132, 'dreszcz_p_132.mp3')
    path_strings = ['Tak', 'Nie']
    actions = ['paragraphs._233()', 'paragraphs._128()']
    functions.pth_selector(path_strings, actions)


def _136():
    functions.dub_play(gb.gameboook_136, 'dreszcz_p_136.mp3')
    path_strings = []
    actions = ['paragraphs._186()']
    functions.pth_selector(path_strings, actions)


def _146():
    functions.dub_play(gb.gameboook_146, 'dreszcz_p_146.mp3')
    path_strings = []
    actions = ['paragraphs._64()']
    functions.pth_selector(path_strings, actions)


def _153():
    functions.dub_play(gb.gameboook_153, 'dreszcz_p_153.mp3')

    functions.stats_change('Szczęście', constants.s_count, 1)
    functions.update_num_variable(constants.p_hit_val_, constants.p_hit_val_ + 1)

    path_strings = []
    actions = ['paragraphs._115()']
    functions.pth_selector(path_strings, actions)


def _158():
    functions.dub_play(gb.gameboook_158, 'dreszcz_p_158.mp3')
    path_strings = ['Jeszcze raz spróbuj(wymagane przynajmniej 10 sztuk złota) ze Smokiem', 'nie chcesz']
    actions = ["check_for_gold_amount(_64(),_false_path(), 10)", '_269()']
    functions.pth_selector(path_strings, actions)


def _160():
    functions.dub_play(gb.gameboook_160, 'dreszcz_p_160.mp3')
    path_strings = []
    actions = ['paragraphs._10()']
    functions.pth_selector(path_strings, actions)


def _170():
    functions.dub_play(gb.gameboook_170, 'dreszcz_p_170.mp3')
    path_strings = ['północ', 'wschód', 'południe']
    actions = ['paragraphs._84()', 'paragraphs._319()', 'paragraphs._357()']
    functions.pth_selector(path_strings, actions)


def _175():
    path_strings = []
    actions = ['paragraphs._373()']
    functions.pth_selector(path_strings, actions)


def _176():
    functions.dub_play(gb.gameboook_176, 'dreszcz_p_176.mp3')
    path_strings = ['północ', 'wschód']
    actions = ['paragraphs._27()', 'paragraphs._230()']
    functions.pth_selector(path_strings, actions)


def _177():
    functions.dub_play(gb.gameboook_177, 'dreszcz_p_177.mp3')
    functions.stats_change('Szczęście', constants.s_count, 4)
    path_strings = []
    actions = ['paragraphs._330()']
    functions.pth_selector(path_strings, actions)


def _178():
    functions.dub_play(gb.gameboook_178, 'dreszcz_p_178.mp3')
    path_strings = []
    actions = ['paragraphs._15()']
    functions.pth_selector(path_strings, actions)


def _179():
    path_strings = []
    actions = ['paragraphs._373()']
    functions.pth_selector(path_strings, actions)


def _180():
    if entities.room_364.visit_count <= 2:
        functions.dub_play(gb.gameboook_180, 'dreszcz_p_180.mp3')

        constants.keys_eq.append('45')

        functions.eq_change("klucz z liczbą '45'")

    path_strings = []
    actions = ['paragraphs._120()']
    functions.pth_selector(path_strings, actions)


def _181():
    functions.dub_play(gb.gameboook_181, 'dreszcz_p_181.mp3')
    path_strings = ['Masz linę', 'Nie masz liny']
    actions = ['paragraphs._329()', 'paragraphs._32()']
    functions.pth_selector(path_strings, actions)


def _182():
    functions.dub_play(gb.gameboook_182, 'dreszcz_p_182.mp3')
    path_strings = ['tak', 'nie']
    actions = ['paragraphs._30()', 'paragraphs._259()']
    functions.pth_selector(path_strings, actions)


def _183():
    functions.dub_play(gb.gameboook_183, 'dreszcz_p_183.mp3')
    _xx()


def _184():
    functions.dub_play(gb.gameboook_184, 'dreszcz_p_184.mp3')
    # initiate combat with entity_184
    functions.combat_init(entities.entity_184, True, entities.entity_184.esc_possible, '_385(', '_226(', '_234()')


def _185():
    functions.dub_play(gb.gameboook_185, 'dreszcz_p_185.mp3')
    path_strings = []
    actions = ['paragraphs._252()']
    functions.pth_selector(path_strings, actions)


def _186():
    functions.dub_play(gb.gameboook_186, 'dreszcz_p_186.mp3')
    path_strings = ['A', 'B', 'C']
    actions = ['paragraphs._368()', 'paragraphs._117()', 'paragraphs._360()']
    functions.pth_selector(path_strings, actions)


def _187():
    print(gb.gameboook_187)
    _xx()


def _190():
    functions.dub_play(gb.gameboook_190, 'dreszcz_p_190.mp3')
    path_strings = []
    actions = ['paragraphs._115()']
    functions.pth_selector(path_strings, actions)


def _192():
    functions.dub_play(gb.gameboook_192, 'audiobook_adam_192.mp3', 'adam')
    path_strings = ['Wybierasz wodę', 'Wybierz przedmiot']
    actions = ['paragraphs._306()', 'paragraphs._220()']
    functions.pth_selector(path_strings, actions)
    # Żeby nabrać wody musisz mieć naczynie. Jeśli masz, ale jest pełne, zastanów się: może warto wylać jego zawartość.


def _197():
    print(gb.gameboook_197)
    _xx()


def _198():
    print(gb.gameboook_198)
    _xx()


def _199():
    print(gb.gameboook_199)
    _xx()


def _200():
    functions.dub_play(gb.gameboook_200, 'dreszcz_p_200.mp3')
    path_strings = []
    actions = ['paragraphs._120()', 'paragraphs._301()']
    functions.pth_selector(path_strings, actions, True, entities.room_364)


def _212():
    functions.dub_play(gb.gameboook_212, 'dreszcz_p_212.mp3')
    path_strings = ['zachód', 'północ', 'zachód', 'połódnie']
    actions = ['paragraphs._287()', 'paragraphs._38()', 'paragraphs._82()', 'paragraphs._336()']
    functions.pth_selector(path_strings, actions)


def _224():
    functions.dub_play(gb.gameboook_224, 'audiobook_adam_224.mp3', 'adam')
    path_strings = []
    actions = ['paragraphs._180()', 'paragraphs._301()']
    functions.pth_selector(path_strings, actions, True, entities.room_364)


def _226():
    functions.dub_play(gb.gameboook_226, 'dreszcz_p_226.mp3')
    path_strings = ['tak', 'nie']
    actions = [
        'paragraphs._101(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path(',
        'paragraphs._385()']
    functions.pth_selector(path_strings, actions)


def _228():
    functions.dub_play(gb.gameboook_228, 'dreszcz_p_228.mp3')
    path_strings = []
    actions = ['paragraphs._102()']
    functions.pth_selector(path_strings, actions)


def _232():
    functions.update_num_variable(constants.choice_count, 1)
    if constants.choice_count < 3:
        eval('_271()')
    else:
        eval('_68()')


def _233():
    functions.dub_play(gb.gameboook_233, 'dreszcz_p_233.mp3')
    _xx()


def _234():
    functions.dub_play(gb.gameboook_234, 'dreszcz_p_234.mp3')
    path_strings = ['tak', 'nie']
    actions = ['paragraphs._205()', 'paragraphs._199()']
    functions.pth_selector(path_strings, actions)


def _238a():
    functions.dub_play(gb.gameboook_238a, 'dreszcz_p_238a.mp3')
    functions.combat_init(entities.entity_238_1, entities.entity_238_1.state, entities.entity_238_1.esc_possible,
                          'paragraphs._316(', 'paragraphs._238b(', 'paragraphs._xx()')


def _238b():
    functions.combat_init(entities.entity_238_2, entities.entity_238_2.state, entities.entity_238_2.esc_possible,
                          'paragraphs._316(', 'paragraphs._238c(', 'paragraphs._xx()')


def _238c():
    functions.combat_init(entities.entity_238_3, entities.entity_238_3.state, entities.entity_238_3.esc_possible,
                          'paragraphs._316(', 'paragraphs._238d(', 'paragraphs._xx()')


def _238d():
    functions.combat_init(entities.entity_238_4, entities.entity_238_4.state, entities.entity_238_4.esc_possible,
                          'paragraphs._316(', 'paragraphs._238e(', 'paragraphs._xx()')


def _238e():
    functions.combat_init(entities.entity_238_5, entities.entity_238_5.state, entities.entity_238_5.esc_possible,
                          'paragraphs._316(', 'paragraphs._xx(', 'paragraphs._xx()')


def _241():
    functions.dub_play(gb.gameboook_241, 'dreszcz_p_241.mp3')
    path_strings = []
    actions = ['paragraphs._132()']
    functions.pth_selector(path_strings, actions)


def _242():
    path_strings = []
    actions = ['action']
    functions.pth_selector(path_strings, actions)


def _251():
    pygame.mixer.music.fadeout(1500)

    rnd_choice = random.choice(constants.music_main)  # losowanie muzyki z listy
    pygame.mixer.music.load(rnd_choice)
    pygame.mixer.music.set_volume(constants.def_bckg_volume)
    pygame.mixer.music.play(-1)

    functions.dub_play(gb.gameboook_251, 'dreszcz_p_251.mp3')
    path_strings = []
    actions = ['paragraphs._39()']
    functions.pth_selector(path_strings, actions)


def _264():
    functions.dub_play(gb.gameboook_264, 'dreszcz_p_264.mp3')
    path_strings = []
    actions = ['paragraphs._102()']
    functions.pth_selector(path_strings, actions)


def _265():
    functions.dub_play(gb.gameboook_265, 'dreszcz_p_265.mp3')
    _xx()


def _268():
    functions.dub_play(gb.gameboook_268, 'dreszcz_p_268.mp3')
    functions.pth_selector(entities.room_310, entities.room_310, 'paragraphs._317a()', 'paragraphs._102()')


def _269():
    functions.dub_play(gb.gameboook_269, 'dreszcz_p_269.mp3')
    functions.stats_change('Wytrzymałosć', constants.w_count, -2)
    path_strings = ['Zapłać według taryfy(przynajmniej 10 sztuk złota)', 'Podejdź do mostu',
                    'Spróbuj przeskoczyć przez rozpadlinę(przynajmniej 18W i 9Z)', 'Ponów próbę z liną']
    actions = ['check_for_gold_amount((_35(), pass, _10()', '_110()', '_358()']
    functions.pth_selector(path_strings, actions)


def _271():
    functions.dub_play(gb.gameboook_271a, 'dreszcz_p_271a.mp3')
    functions.stats_change('Wytrzymałosć', constants.w_count, -1)
    functions.dub_play(gb.gameboook_271b, 'dreszcz_p_271b.mp3')

    path_strings = ['wymień', 'nie wymieniaj']
    actions = ['paragraphs._190()', 'paragraphs._153()']
    functions.pth_selector(path_strings, actions)


def _284():
    functions.dub_play(gb.gameboook_284, 'dreszcz_p_284.mp3')
    functions.check_for_luck()

    if not constants.p_luck:
        functions.stats_change('Wytrzymałość', constants.w_count, -2)

    path_strings = []
    actions = ['paragraphs._50()']
    functions.pth_selector(path_strings, actions)


def _287():
    functions.dub_play(gb.gameboook_287, 'dreszcz_p_287.mp3')
    _xx()


def _291():
    functions.dub_play(gb.gameboook_291, 'dreszcz_p_291.mp3')
    functions.stats_change('Wytrzymałość', constants.w_count, -2)
    path_strings = []
    actions = ['paragraphs._330()']
    functions.pth_selector(path_strings, actions)


def _296():
    functions.dub_play(gb.gameboook_296, 'dreszcz_p_296a.mp3')
    functions.eatables()
    functions.dub_play('Idziesz dalej. Przed sobą widzisz skrzyżowanie.', 'dreszcz_p_296b.mp3')
    path_strings = []
    actions = ['paragraphs._39()']
    functions.pth_selector(path_strings, actions)


def _298():
    functions.update_num_variable(constants.choice_count, 1)
    if constants.choice_count < 3:
        eval('_115()')
    else:
        eval('_68()')


def _301():
    functions.dub_play(gb.gameboook_301, 'dreszcz_p_301.mp3')
    path_strings = ['Spróbuj otworzyć drzwi', 'Zawróć']
    actions = ['paragraphs._364()', 'paragraphs._120()']
    functions.pth_selector(path_strings, actions)


def _305():
    functions.dub_play(gb.gameboook_305, 'dreszcz_p_305.mp3')
    path_strings = ['zdaj się na los', 'sprawdź czy masz szczęście']
    actions = ['paragraphs._112()', 'paragraphs._381()']
    functions.pth_selector(path_strings, actions)


def _310():
    functions.dub_play(gb.gameboook_310, 'dreszcz_p_310.mp3')
    path_strings = []
    actions = ['paragraphs._67()', 'paragraphs._17()']
    functions.pth_selector(path_strings, actions, True, entities.room_310)


def _316():
    functions.dub_play(gb.gameboook_316, 'dreszcz_p_316.mp3')
    path_strings = []
    actions = ['paragraphs._176()']
    functions.pth_selector(path_strings, actions)


def _317a():
    functions.dub_play(gb.gameboook_317a, 'dreszcz_p_317a.mp3')
    functions.combat_init(entities.entity_317, entities.entity_317.state, entities.entity_317.esc_possible, '', '',
                          'paragraphs._317b()')
    # combat_init(entity, state, esc_possible, escape_id, stay_id, win_path_id):


def _317b():
    functions.dub_play(gb.gameboook_317b, 'dreszcz_p_317b.mp3')
    path_strings = ['Rozejrzyj się chociaż po ścianch', 'Nie brzydzę się']
    actions = ['paragraphs._119()', 'paragraphs._31()']
    functions.pth_selector(path_strings, actions)


def _324():
    functions.update_num_variable(constants.choice_count, 1)
    if constants.choice_count < 3:
        eval('_115()')
    else:
        eval('_68()')


def _330():
    functions.dub_play(gb.gameboook_330, 'dreszcz_p_330.mp3')
    path_strings = []
    actions = ['paragraphs._170()']
    functions.pth_selector(path_strings, actions)


def _331():
    functions.dub_play(gb.gameboook_331, 'dreszcz_p_331a.mp3')
    path_strings = []
    actions = ['paragraphs._59()', 'paragraphs._11()']
    functions.pth_selector(path_strings, actions, True, entities.room_331)


def _332():
    functions.dub_play(gb.gameboook_332a, 'audiobook_adam_332a.mp3', 'adam')
    functions.stats_change('Wytrzymałość', constants.w_count, -2)
    functions.dub_play(gb.gameboook_332b, 'audiobook_adam_332b.mp3', 'adam')
    functions.combat_init(entities.entity_332, True, entities.entity_332.esc_possible, '', '', 'paragraphs._06a()')


def _336():
    functions.dub_play(gb.gameboook_336, 'audiobook_adam_336.mp3', 'adam')
    path_strings = []
    actions = ['paragraphs._06b()', 'paragraphs._21()']
    functions.pth_selector(path_strings, actions, True, entities.room_336)


def _344():
    functions.dub_play(gb.gameboook_344, 'audiobook_adam_344.mp3', 'adam')
    functions.combat_init(entities.entity_344, True, entities.entity_344.esc_possible, '', '', "paragraphs._23()")


def _345():
    functions.dub_play(gb.gameboook_345, 'audiobook_adam_345.mp3', 'adam')
    path_strings = ['zachód', 'północ']
    actions = ['_218()', '_267()']
    functions.pth_selector(path_strings, actions)


def _349():
    functions.dub_play(gb.gameboook_349, 'audiobook_adam_349.mp3', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['_385(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count)', '_48()']
    functions.pth_selector(path_strings, actions)


def _351():
    functions.dub_play(gb.gameboook_351, 'audiobook_adam_351.mp3', 'adam')
    path_strings = []
    actions = ['paragraphs._64()']
    functions.pth_selector(path_strings, actions)


def _358():
    functions.dub_play(gb.gameboook_358, 'audiobook_adam_358.mp3', 'adam')
    path_strings = []
    actions = ['paragraphs._xx()']
    functions.pth_selector(path_strings, actions)


def _364():
    functions.debug_message(f'entities.room_364.visit_count = {entities.room_364.visit_count}')

    entities.room_364.room_state = functions.update_bool_variable(entities.room_364.room_state, True)
    functions.debug_message(f'entities.room_364.room_state = {entities.room_364.room_state}')

    functions.dub_play(gb.gameboook_364, 'audiobook_adam_364.mp3', 'adam')
    path_strings = ['Próbujesz zabrać ukradkiem pudełko', 'Decydujesz się podjąć walkę']
    actions = ['paragraphs._29()', 'paragraphs._116a()']
    functions.pth_selector(path_strings, actions, '', entities.room_364)


def _372():
    functions.dub_play(gb.gameboook_372, 'audiobook_adam_372.mp3', 'adam')
    path_strings = []
    actions = ['paragraphs._xx()']
    functions.pth_selector(path_strings, actions)


def _374():
    functions.dub_play(gb.gameboook_374, 'audiobook_adam_374.mp3', 'adam')
    functions.eatables()
    path_strings = []
    actions = ['paragraphs._178()']
    functions.pth_selector(path_strings, actions)


def _381():
    functions.check_for_luck()
    if constants.p_luck:
        _28()
    else:
        _291()


def _385():
    functions.dub_play(gb.gameboook_385, 'audiobook_adam_385.mp3', 'adam')
    path_strings = ['Wybierz drzwi zachodnie', 'Wybierz drzwi wschodnie']
    actions = ['_345()', '_242()']
    functions.pth_selector(path_strings, actions)
