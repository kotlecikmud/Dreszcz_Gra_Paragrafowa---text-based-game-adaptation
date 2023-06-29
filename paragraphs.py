import time, random
from obj_class import *
import gamebook as gb
import entities as ent
import functions as func
import constants as cnst


# - - - - - - - - -
# /// PARAGRAPHS
# - - - - - - - - -
def _xx():  # placeholder
    pygame.mixer.music.fadeout(1200)
    while True:
        odp = input(f"{cnst.special_txt_clr}--placeholder function--\
                \n\
                \npress enter to return to _64()\
                \nor type any command here:\
                \n{cnst.input_sign}{cnst.def_txt_clr}")

        rnd_choice = random.choice(cnst.music_main)  # randomizing music from list
        pygame.mixer.music.load(rnd_choice)
        pygame.mixer.music.set_volume(cnst.def_bckg_volume)
        pygame.mixer.music.play(-1)

        if len(odp) > 0:
            eval(odp)

        else:
            print('returning to _64()')
            time.sleep(1.5)
            _64()


# - - - - - - - - -
# - - - - - - - - -
# - - - - - - - - -
def par_00():
    func.dub_play('00a', 'adam')

    while True:  # elixir choice menu
        func.dub_play('elxr_chc', 'adam')
        choice = input(f'{cnst.input_sign}')

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
            func.clear_terminal()
            print(f"{cnst.special_txt_clr}Niepoprawny wybór.")

    func.loading(1)
    func.clear_terminal()
    print(f"/// eliksir {potion} = {cnst.count_potion}/2\
            \n{cnst.def_txt_clr}")
    time.sleep(1)

    rnd_choice = random.choice(cnst.music_main)  # randomizing music from list
    pygame.mixer.music.load(rnd_choice)
    pygame.mixer.music.set_volume(cnst.def_bckg_volume)
    pygame.mixer.music.play(-1)

    func.clear_terminal()
    func.dub_play('00b', 'adam')
    path_strings = [f'Ruszaj {cnst.input_sign}']
    actions = ['paragraphs._01()']
    func.pth_selector(path_strings, actions)


def _01():
    func.dub_play('01', 'adam')
    path_strings = []
    actions = ['paragraphs._25()']
    func.pth_selector(path_strings, actions)


def _02():
    func.dub_play('02', 'adam')
    # initiate combat with entity_002
    func.combat_init(ent.entity_002, True, ent.entity_002.esc_possible, 'paragraphs._372(', '',
                          'paragraphs._380()')


def _03():
    func.dub_play('03', 'adam')
    path_strings = ['Spróbuj jeszcze raz (wymagane conajmniej 13 sztuk złota)', 'Wyciągnij z plecaka linę',
                    'Podejdź do mostu', 'Spróbuj przeskoczyć przez rozpadlinę (przynajmniej 18W i 9Z)']
    actions = ['paragraphs._136()', 'paragraphs._13()', 'paragraphs._269()', 'paragraphs._74()', 'paragraphs._110()']
    func.pth_selector(path_strings, actions)


def _04():
    func.dub_play('04', 'adam')
    path_strings = ['Chwytasz za miecz i atakujesz', 'Postanawiasz czekać dalej']
    actions = ['paragraphs._318()', 'paragraphs._295()']
    func.pth_selector(path_strings, actions)


def _05():
    func.dub_play('05', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['paragraphs._312()', 'paragraphs._140()']
    func.pth_selector(path_strings, actions)


def _06a():
    func.stats_change('Szczęście', cnst.s_count, 1)
    path_strings = []
    actions = ['paragraphs._06b()']
    func.pth_selector(path_strings, actions)


def _06b():
    func.dub_play('06', 'adam')
    path_strings = []
    actions = ['paragraphs._115()']
    func.pth_selector(path_strings, actions)


def _07():
    func.dub_play('07', 'adam')
    path_strings = []
    actions = ['paragraphs._219()']
    func.pth_selector(path_strings, actions)


def _08():
    func.dub_play('08', 'adam')
    path_strings = ['Walcz u boku prześladowanego stwora przeciw zgrai jego współplemieńców', 'Ratuj się Ucieczką']
    actions = ['paragraphs._210()', 'paragraphs._98()']
    func.pth_selector(path_strings, actions)


def _09():
    func.dub_play('09', 'adam')
    path_strings = ['Sprzedaj kamień krasnalowi', 'Nie sprzedawaj kamienia']
    actions = ['paragraphs._289()', 'paragraphs._375()']
    func.pth_selector(path_strings, actions)


def _10():
    func.dub_play('10', 'adam')
    _xx()


def _11():
    pygame.mixer.music.fadeout(2600)
    music = f'{cnst.assets_audio_music_pth}/scene_11_background.mp3'
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(cnst.def_bckg_volume)
    pygame.mixer.music.play(-1)

    func.dub_play('11', 'adam')
    path_strings = ['idziesz od razu po wodę', 'dobierasz się do stwora']
    actions = ['paragraphs._45()', 'paragraphs._192()']
    func.pth_selector(path_strings, actions)


def _12():
    func.dub_play('12', 'adam')
    path_strings = []
    actions = ['paragraphs._288()']
    func.pth_selector(path_strings, actions)


def _13():
    func.dub_play('13', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -2)
    print('Ale to tylko chwila. Wielkimi susami biegniesz w kierunku potwora')
    path_strings = []
    actions = ['paragraphs._126()']
    func.pth_selector(path_strings, actions)


def _14():
    func.dub_play('14', 'adam')
    path_strings = ['Wychodzisz północnymi drzwiami', 'Wychodzisz wschodnimi drzwiami']
    actions = ['paragraphs._197()', 'paragraphs._39()']
    func.pth_selector(path_strings, actions)


def _15():
    func.dub_play('15', 'adam')
    path_strings = ['Rezygnujesz z przepłynięcia jeziora', 'Decydujesz się podjąć próbę przepłynięcia jeziora']
    actions = ['paragraphs._241()', 'paragraphs._113()']
    func.pth_selector(path_strings, actions)
    # print('Jeśli rezygnujesz z przepłynięcia jeziora - patrz 241\
    # \nNatomiast jeśli decydujesz się podjąć próbę przepłynięcia jeziora, zapisz numer niniejszego paragrafu i patrz 113')


def _16a():
    func.dub_play('16a', 'adam')
    func.eatables()
    print(gb.gameboook[cnst.translation]['16b'])
    path_strings = []
    actions = ['paragraphs._80()']
    func.pth_selector(path_strings, actions)


def _17():
    path_strings = ['Zobacz co za nimi jest', 'Wycofaj się']
    actions = ['paragraphs._265()', 'paragraphs._50()']
    func.pth_selector(path_strings, actions)


def _18():
    func.dub_play('18', 'adam')
    path_strings = ['Jeśli tak, pamiętaj że musisz mieć przynajmniej 5 sztuk złota', 'Wycofujesz się']
    actions = ['paragraphs._211()', 'paragraphs._286()']
    func.pth_selector(path_strings, actions)


def _19():
    func.dub_play('19', 'adam')
    func.stats_change('Prowiant', cnst.eatables_count, 1)
    func.stats_change('Szczęście', cnst.s_count, 2)
    path_strings = []
    actions = ['paragraphs._141()']
    func.pth_selector(path_strings, actions)


def _20():
    func.dub_play('20', 'adam')
    path_strings = []
    actions = ['paragraphs._238a()']
    func.pth_selector(path_strings, actions)


def _21():
    path_strings = ['Zobacz co jest za drzwiami', 'Zawróć']
    actions = ['paragraphs._332()', 'paragraphs._212()']
    func.pth_selector(path_strings, actions)


def _22():
    func.dub_play('22', 'adam')
    _xx()


def _23():
    func.dub_play('23', 'adam')
    _xx()


def _24():
    func.dub_play('24', 'adam')
    _xx()


def _25():
    func.dub_play('25', 'adam')
    path_strings = ['Idziesz na zachód', 'Wybierasz drogę prowadzącą na wschód']
    actions = ['paragraphs._200()', 'paragraphs._44()']
    func.pth_selector(path_strings, actions)


def _26():
    func.dub_play('26', 'adam')
    _xx()


def _27():
    func.dub_play('27', 'adam')
    _xx()


def _28():
    func.dub_play('28', 'adam')
    if cnst.w_count >= 18:
        _177()
    else:
        _330()


def _29():
    func.dub_play('29', 'adam')
    path_strings = []
    actions = ['paragraphs._116a()']
    func.pth_selector(path_strings, actions)


def _30():
    func.dub_play('30', 'adam')
    _xx()


def _31():
    func.dub_play('31', 'adam')
    path_strings = []
    actions = ['paragraphs._119()']
    func.pth_selector(path_strings, actions)


def _32():
    func.dub_play('32', 'adam')
    _xx()


def _33():
    func.dub_play('33', 'adam')
    _xx()


def _34():
    func.dub_play('34', 'adam')
    _xx()


def _35():
    func.dub_play('35', 'adam')
    _xx()


def _36():
    func.dub_play('36', 'adam')
    _xx()


def _37():
    func.update_num_variable(cnst.choice_count, 1)
    if cnst.choice_count < 3:
        eval('_115()')
    else:
        eval('_68()')


def _38():
    func.dub_play('38', 'adam')
    _xx()


def _39():
    func.dub_play('39', 'adam')
    path_strings = ['zachód', 'północ', 'południe']
    actions = ['paragraphs._331()', 'paragraphs._228()', 'paragraphs._146()']
    func.pth_selector(path_strings, actions)


def _43():
    func.dub_play('43', 'adam')
    _xx()


def _44():
    func.dub_play('44', 'adam')
    path_strings = ['Rezygnujesz', 'Wyważasz drzwi']
    actions = ['paragraphs._75()', 'paragraphs._105()']
    func.pth_selector(path_strings, actions)


def _45():
    func.dub_play('45', 'adam')
    func.stats_change('Szczęscie', cnst.s_count, 2)
    path_strings = []
    actions = ['paragraphs._251()']
    func.pth_selector(path_strings, actions)


def _46():
    func.dub_play('46', 'adam')
    _xx()


def _47():
    func.dub_play('47', 'adam')
    _xx()


def _48():
    func.dub_play('48', 'adam')
    _xx()


def _49():
    func.dub_play('49', 'adam')
    _xx()


def _50():
    func.dub_play('50', 'adam')
    path_strings = ['północ', 'wschód', 'zachód']
    actions = ['paragraphs._310()', 'paragraphs._130()', 'paragraphs._64()']
    func.pth_selector(path_strings, actions)


def _56():
    func.dub_play('56', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -1)
    path_strings = []
    actions = ['paragraphs._75()']
    func.pth_selector(path_strings, actions)


def _59():
    func.dub_play('59', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['paragraphs._14()', 'paragraphs._70()']
    func.pth_selector(path_strings, actions)


def _64():
    func.dub_play('64', 'adam')
    path_strings = ['zachód', 'północ', 'wschód', 'południe']
    actions = ['paragraphs._296()', 'paragraphs._264()', 'paragraphs._284()', 'paragraphs._224()']
    func.pth_selector(path_strings, actions)


def _67():
    func.dub_play('67', 'adam')
    path_strings = ['Musisz się wycofać.']
    actions = ['paragraphs._50()']
    func.pth_selector(path_strings, actions)


def _69a():
    func.dub_play('69a', 'adam')
    func.combat_init(ent.entity_069_1, True, ent.entity_069_1.esc_possible, '', '', 'paragraphs._69b()')


def _69b():
    func.dub_play('69b', 'adam')
    func.combat_init(ent.entity_069_2, True, ent.entity_069_2.esc_possible, '', '', 'paragraphs._69c()')


def _69c():
    func.dub_play('69c', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['paragraphs._305()', 'paragraphs._291()']
    func.pth_selector(path_strings, actions)


def _70():
    func.dub_play('70', 'adam')
    _xx()


def _75():
    func.dub_play('75', 'adam')
    path_strings = []
    actions = ['paragraphs._200()']
    func.pth_selector(path_strings, actions)


def _76():
    func.dub_play('76', 'adam')
    _xx()


def _82():
    func.dub_play('82', 'adam')
    _xx()


def _89():
    func.dub_play('89a', 'adam')
    func.stats_change('Szczęscie', cnst.s_count, 2)
    func.stats_change('Złoto', cnst.gold_amount, 3)
    func.dub_play('89b', 'adam')
    path_strings = []
    actions = ['paragraphs._120()']
    func.pth_selector(path_strings, actions)


def _95():
    func.update_num_variable(cnst.choice_count, 1)
    if cnst.choice_count < 3:
        eval('_115()')
    else:
        eval('_68()')


def _100():
    func.dub_play('100', 'adam')
    _xx()


def _101():
    print(f'{ent.entity_184.name} prosi o łaskę.')
    path_strings = ['Darujesz mu życie', 'Walczysz aż do końca']
    actions = ['paragraphs._362()', 'paragraphs._234()']
    func.pth_selector(path_strings, actions)


def _102():
    func.dub_play('102', 'adam')
    path_strings = ['zachód', 'północ', 'wschód', 'południe']
    actions = ['paragraphs._123()', 'paragraphs._268()', 'paragraphs._374()', 'paragraphs._351()']
    func.pth_selector(path_strings, actions)


def _103():
    func.dub_play('103', 'adam')
    path_strings = []
    actions = ['paragraphs._345()']
    func.pth_selector(path_strings, actions)


def _104():
    func.dub_play('104', 'adam')
    path_strings = []
    actions = ['paragraphs._121()']
    func.pth_selector(path_strings, actions)


def _105():
    func.dub_play('105', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -1)
    print('Czy chcesz ponowić próbę?')
    path_strings = ['tak', 'nie']
    actions = ['paragraphs._56()', 'paragraphs._75()']
    func.pth_selector(path_strings, actions)


def _106():
    func.dub_play('106', 'adam')
    path_strings = ['Broń się mieczem', 'Masz jedno albo drugie', 'Masz jedno i drugie']
    actions = ['_213()', '_24()', '_292()']
    func.pth_selector(path_strings, actions)


def _107():
    # initiate combat with entity_107
    func.combat_init(ent.entity_107, True, ent.entity_107.esc_possible, '', '', '_23()')


def _112():
    value = random.randint(4, 48)
    if value >= 18:
        print('Szczęście ci sprzyja')
        _28()
    else:
        print('Szczęście ci nie sprzyja')
        _291()


def _113():
    func.dub_play('113', 'adam')
    path_strings = ['blank', 'blank']
    actions = ['paragraphs._xx()', 'paragraphs._xx()']
    func.pth_selector(path_strings, actions)


def _115():
    func.debug_message(f'cnst.choice_count = {cnst.choice_count}')

    func.dub_play('115', 'adam')

    cnst.choice_count = 0

    while True:
        for i, (choice, action) in enumerate(cnst.choices_115.items(), 1):
            print(f"{i}. {choice}")

        usr_input = input("Wybierz opcję: ").strip()

        if usr_input.isdigit():
            index = int(usr_input) - 1
            if 0 <= index < len(cnst.choices_115):
                usr_input = list(cnst.choices_115.keys())[index]

        if usr_input in cnst.choices_115:
            break
        else:
            print("Nieprawidłowy wybór.")

    cnst.main_eq.append(usr_input)

    func.eq_change(usr_input)

    eval(cnst.choices_115[usr_input])


def _116a():
    func.dub_play('116a', 'adam')
    func.combat_init(ent.entity_116, ent.entity_116.state, ent.entity_116.esc_possible, '', '',
                          'paragraphs._116b()')


def _116b():
    func.dub_play('116b', 'adam')
    path_strings = ['Rozejrzyj się', 'Opuść pieczarę']
    actions = ['paragraphs._89()', 'paragraphs._120()']
    func.pth_selector(path_strings, actions)


def _119():
    func.dub_play('119', 'adam')
    path_strings = ['Przeszukaj ciało', 'Opuść komnatę']
    actions = ['paragraphs._31()', 'paragraphs._102()']
    func.pth_selector(path_strings, actions)


def _120():
    func.dub_play('120', 'adam')
    path_strings = []
    actions = ['paragraphs._64()']
    func.pth_selector(path_strings, actions)


def _123():
    func.dub_play('123', 'adam')
    path_strings = []
    actions = ['paragraphs._39()']
    func.pth_selector(path_strings, actions)


def _128():
    func.dub_play('128', 'adam')
    _xx()


def _130():
    func.dub_play('130', 'adam')
    path_strings = []
    actions = ['paragraphs._212()']
    func.pth_selector(path_strings, actions)


def _132():
    func.dub_play('132', 'adam')
    path_strings = ['Tak', 'Nie']
    actions = ['paragraphs._233()', 'paragraphs._128()']
    func.pth_selector(path_strings, actions)


def _136():
    func.dub_play('136', 'adam')
    path_strings = []
    actions = ['paragraphs._186()']
    func.pth_selector(path_strings, actions)


def _146():
    func.dub_play('146', 'adam')
    path_strings = []
    actions = ['paragraphs._64()']
    func.pth_selector(path_strings, actions)


def _153():
    func.dub_play('153', 'adam')

    func.stats_change('Szczęście', cnst.s_count, 1)
    func.update_num_variable(cnst.p_hit_val_, cnst.p_hit_val_ + 1)

    path_strings = []
    actions = ['paragraphs._115()']
    func.pth_selector(path_strings, actions)


def _158():
    func.dub_play('158', 'adam')
    path_strings = ['Jeszcze raz spróbuj(wymagane przynajmniej 10 sztuk złota) ze Smokiem', 'nie chcesz']
    actions = ["check_for_gold_amount(_64(),_false_path(), 10)", '_269()']
    func.pth_selector(path_strings, actions)


def _160():
    func.dub_play('160', 'adam')
    path_strings = []
    actions = ['paragraphs._10()']
    func.pth_selector(path_strings, actions)


def _170():
    func.dub_play('170', 'adam')
    path_strings = ['północ', 'wschód', 'południe']
    actions = ['paragraphs._84()', 'paragraphs._319()', 'paragraphs._357()']
    func.pth_selector(path_strings, actions)


def _175():
    path_strings = []
    actions = ['paragraphs._373()']
    func.pth_selector(path_strings, actions)


def _176():
    func.dub_play('176', 'adam')
    path_strings = ['północ', 'wschód']
    actions = ['paragraphs._27()', 'paragraphs._230()']
    func.pth_selector(path_strings, actions)


def _177():
    func.dub_play('177', 'adam')
    func.stats_change('Szczęście', cnst.s_count, 4)
    path_strings = []
    actions = ['paragraphs._330()']
    func.pth_selector(path_strings, actions)


def _178():
    func.dub_play('178', 'adam')
    path_strings = []
    actions = ['paragraphs._15()']
    func.pth_selector(path_strings, actions)


def _179():
    path_strings = []
    actions = ['paragraphs._373()']
    func.pth_selector(path_strings, actions)


def _180():
    if ent.room_364.visit_count <= 2:
        func.dub_play('180', 'adam')

        cnst.keys_eq.append('45')

        func.eq_change("klucz z liczbą '45'")

    path_strings = []
    actions = ['paragraphs._120()']
    func.pth_selector(path_strings, actions)


def _181():
    func.dub_play('181', 'adam')
    path_strings = ['Masz linę', 'Nie masz liny']
    actions = ['paragraphs._329()', 'paragraphs._32()']
    func.pth_selector(path_strings, actions)


def _182():
    func.dub_play('182', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['paragraphs._30()', 'paragraphs._259()']
    func.pth_selector(path_strings, actions)


def _183():
    func.dub_play('183', 'adam')
    _xx()


def _184():
    func.dub_play('184', 'adam')
    # initiate combat with entity_184
    func.combat_init(ent.entity_184, True, ent.entity_184.esc_possible, '_385(', '_226(', '_234()')


def _185():
    func.dub_play('185', 'dreszcz_p_185.mp3')
    path_strings = []
    actions = ['paragraphs._252()']
    func.pth_selector(path_strings, actions)


def _186():
    func.dub_play('186', 'adam')
    path_strings = ['A', 'B', 'C']
    actions = ['paragraphs._368()', 'paragraphs._117()', 'paragraphs._360()']
    func.pth_selector(path_strings, actions)


def _187():
    print(gb.gameboook[cnst.translation]['187'])
    _xx()


def _190():
    func.dub_play('190', 'adam')
    path_strings = []
    actions = ['paragraphs._115()']
    func.pth_selector(path_strings, actions)


def _192():
    func.dub_play('192', 'adam')
    path_strings = ['Wybierasz wodę', 'Wybierz przedmiot']
    actions = ['paragraphs._306()', 'paragraphs._220()']
    func.pth_selector(path_strings, actions)
    # Żeby nabrać wody musisz mieć naczynie. Jeśli masz, ale jest pełne, zastanów się: może warto wylać jego zawartość.


def _197():
    print(gb.gameboook['197'])
    _xx()


def _198():
    print(gb.gameboook['198'])
    _xx()


def _199():
    print(gb.gameboook['199'])
    _xx()


def _200():
    func.dub_play('200', 'adam')
    path_strings = []
    actions = ['paragraphs._120()', 'paragraphs._301()']
    func.pth_selector(path_strings, actions, True, ent.room_364)


def _210():
    print(gb.gameboook['210'])
    _xx()


def _212():
    func.dub_play('212', 'adam')
    path_strings = ['zachód', 'północ', 'zachód', 'połódnie']
    actions = ['paragraphs._287()', 'paragraphs._38()', 'paragraphs._82()', 'paragraphs._336()']
    func.pth_selector(path_strings, actions)


def _220():
    print(gb.gameboook['220'])
    _xx()


def _224():
    func.dub_play('224', 'adam')
    path_strings = []
    actions = ['paragraphs._180()', 'paragraphs._301()']
    func.pth_selector(path_strings, actions, True, ent.room_364)


def _226():
    func.dub_play('226', 'adam')
    path_strings = ['tak', 'nie']
    actions = [
        'paragraphs._101(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path(',
        'paragraphs._385()']
    func.pth_selector(path_strings, actions)


def _228():
    func.dub_play('228', 'adam')
    path_strings = []
    actions = ['paragraphs._102()']
    func.pth_selector(path_strings, actions)


def _232():
    func.update_num_variable(cnst.choice_count, 1)
    if cnst.choice_count < 3:
        eval('_271()')
    else:
        eval('_68()')


def _233():
    func.dub_play('233', 'adam')
    _xx()


def _234():
    func.dub_play('234', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['paragraphs._205()', 'paragraphs._199()']
    func.pth_selector(path_strings, actions)


def _238a():
    func.dub_play('238a', 'adam')
    func.combat_init(ent.entity_238_1, ent.entity_238_1.state, ent.entity_238_1.esc_possible,
                          'paragraphs._316(', 'paragraphs._238b(', 'paragraphs._xx()')


def _238b():
    func.combat_init(ent.entity_238_2, ent.entity_238_2.state, ent.entity_238_2.esc_possible,
                          'paragraphs._316(', 'paragraphs._238c(', 'paragraphs._xx()')


def _238c():
    func.combat_init(ent.entity_238_3, ent.entity_238_3.state, ent.entity_238_3.esc_possible,
                          'paragraphs._316(', 'paragraphs._238d(', 'paragraphs._xx()')


def _238d():
    func.combat_init(ent.entity_238_4, ent.entity_238_4.state, ent.entity_238_4.esc_possible,
                          'paragraphs._316(', 'paragraphs._238e(', 'paragraphs._xx()')


def _238e():
    func.combat_init(ent.entity_238_5, ent.entity_238_5.state, ent.entity_238_5.esc_possible,
                          'paragraphs._316(', 'paragraphs._xx(', 'paragraphs._xx()')


def _241():
    func.dub_play('241', 'adam')
    path_strings = []
    actions = ['paragraphs._132()']
    func.pth_selector(path_strings, actions)


def _242():
    path_strings = []
    actions = ['action']
    func.pth_selector(path_strings, actions)


def _251():
    pygame.mixer.music.fadeout(1500)

    rnd_choice = random.choice(cnst.music_main)  # losowanie muzyki z listy
    pygame.mixer.music.load(rnd_choice)
    pygame.mixer.music.set_volume(cnst.def_bckg_volume)
    pygame.mixer.music.play(-1)

    func.dub_play('251', 'adam')
    path_strings = []
    actions = ['paragraphs._39()']
    func.pth_selector(path_strings, actions)


def _264():
    func.dub_play('264', 'adam')
    path_strings = []
    actions = ['paragraphs._102()']
    func.pth_selector(path_strings, actions)


def _265():
    func.dub_play('265', 'adam')
    _xx()


def _268():
    func.dub_play('268', 'adam')
    func.pth_selector(ent.room_310, ent.room_310, 'paragraphs._317a()', 'paragraphs._102()')


def _269():
    func.dub_play('269', 'adam')
    func.stats_change('Wytrzymałosć', cnst.w_count, -2)
    path_strings = ['Zapłać według taryfy(przynajmniej 10 sztuk złota)', 'Podejdź do mostu',
                    'Spróbuj przeskoczyć przez rozpadlinę(przynajmniej 18W i 9Z)', 'Ponów próbę z liną']
    actions = ['check_for_gold_amount((_35(), pass, _10()', '_110()', '_358()']
    func.pth_selector(path_strings, actions)


def _271():
    func.dub_play('271a', 'adam')
    func.stats_change('Wytrzymałosć', cnst.w_count, -1)
    func.dub_play('271b', 'dreszcz_p_271b.mp3')

    path_strings = ['wymień', 'nie wymieniaj']
    actions = ['paragraphs._190()', 'paragraphs._153()']
    func.pth_selector(path_strings, actions)


def _284():
    func.dub_play('284', 'adam')
    func.check_for_luck()

    if not cnst.p_luck:
        func.stats_change('Wytrzymałość', cnst.w_count, -2)

    path_strings = []
    actions = ['paragraphs._50()']
    func.pth_selector(path_strings, actions)


def _287():
    func.dub_play('287', 'adam')
    _xx()


def _291():
    func.dub_play('291', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -2)
    path_strings = []
    actions = ['paragraphs._330()']
    func.pth_selector(path_strings, actions)


def _296():
    func.dub_play('296', 'adam')
    func.eatables()
    func.dub_play('Idziesz dalej. Przed sobą widzisz skrzyżowanie.', 'dreszcz_p_296b.mp3')
    path_strings = []
    actions = ['paragraphs._39()']
    func.pth_selector(path_strings, actions)


def _298():
    func.update_num_variable(cnst.choice_count, 1)
    if cnst.choice_count < 3:
        eval('_115()')
    else:
        eval('_68()')


def _301():
    func.dub_play('301', 'adam')
    path_strings = ['Spróbuj otworzyć drzwi', 'Zawróć']
    actions = ['paragraphs._364()', 'paragraphs._120()']
    func.pth_selector(path_strings, actions)


def _305():
    func.dub_play('305', 'adam')
    path_strings = ['zdaj się na los', 'sprawdź czy masz szczęście']
    actions = ['paragraphs._112()', 'paragraphs._381()']
    func.pth_selector(path_strings, actions)


def _310():
    func.dub_play('310', 'adam')
    path_strings = []
    actions = ['paragraphs._67()', 'paragraphs._17()']
    func.pth_selector(path_strings, actions, True, ent.room_310)


def _316():
    func.dub_play('316', 'adam')
    path_strings = []
    actions = ['paragraphs._176()']
    func.pth_selector(path_strings, actions)


def _317a():
    func.dub_play('317a', 'adam')
    func.combat_init(ent.entity_317, ent.entity_317.state, ent.entity_317.esc_possible, '', '',
                          'paragraphs._317b()')
    # combat_init(entity, state, esc_possible, escape_id, stay_id, win_path_id):


def _317b():
    func.dub_play('317b', 'adam')
    path_strings = ['Rozejrzyj się chociaż po ścianch', 'Nie brzydzę się']
    actions = ['paragraphs._119()', 'paragraphs._31()']
    func.pth_selector(path_strings, actions)


def _324():
    func.update_num_variable(cnst.choice_count, 1)
    if cnst.choice_count < 3:
        eval('_115()')
    else:
        eval('_68()')


def _330():
    func.dub_play('330', 'adam')
    path_strings = []
    actions = ['paragraphs._170()']
    func.pth_selector(path_strings, actions)


def _331():
    func.dub_play('331', 'adam')
    path_strings = []
    actions = ['paragraphs._59()', 'paragraphs._11()']
    func.pth_selector(path_strings, actions, True, ent.room_331)


def _332():
    func.dub_play('332a', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -2)
    func.dub_play('332b', 'adam')
    func.combat_init(ent.entity_332, True, ent.entity_332.esc_possible, '', '', 'paragraphs._06a()')


def _336():
    func.dub_play('336', 'adam')
    path_strings = []
    actions = ['paragraphs._06b()', 'paragraphs._21()']
    func.pth_selector(path_strings, actions, True, ent.room_336)


def _344():
    func.dub_play('344', 'adam')
    func.combat_init(ent.entity_344, True, ent.entity_344.esc_possible, '', '', "paragraphs._23()")


def _345():
    func.dub_play('345', 'adam')
    path_strings = ['zachód', 'północ']
    actions = ['_218()', '_267()']
    func.pth_selector(path_strings, actions)


def _349():
    func.dub_play('349', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['_385(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count)', '_48()']
    func.pth_selector(path_strings, actions)


def _351():
    func.dub_play('351', 'adam')
    path_strings = []
    actions = ['paragraphs._64()']
    func.pth_selector(path_strings, actions)


def _358():
    func.dub_play('358', 'adam')
    path_strings = []
    actions = ['paragraphs._xx()']
    func.pth_selector(path_strings, actions)


def _364():
    func.debug_message(f'ent.room_364.visit_count = {ent.room_364.visit_count}')

    ent.room_364.room_state = func.update_bool_variable(ent.room_364.room_state, True)
    func.debug_message(f'ent.room_364.room_state = {ent.room_364.room_state}')

    func.dub_play('364', 'adam')
    path_strings = ['Próbujesz zabrać ukradkiem pudełko', 'Decydujesz się podjąć walkę']
    actions = ['paragraphs._29()', 'paragraphs._116a()']
    func.pth_selector(path_strings, actions, '', ent.room_364)


def _372():
    func.dub_play('372', 'adam')
    path_strings = []
    actions = ['paragraphs._xx()']
    func.pth_selector(path_strings, actions)


def _374():
    func.dub_play('374', 'adam')
    func.eatables()
    path_strings = []
    actions = ['paragraphs._178()']
    func.pth_selector(path_strings, actions)


def _381():
    func.check_for_luck()
    if cnst.p_luck:
        _28()
    else:
        _291()


def _385():
    func.dub_play('385', 'adam')
    path_strings = ['Wybierz drzwi zachodnie', 'Wybierz drzwi wschodnie']
    actions = ['_345()', '_242()']
    func.pth_selector(path_strings, actions)
