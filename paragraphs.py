import random
import gamebook as gb
import entities as ent
import functions as func
import constants as cnst


# placeholder
def _xx():
    while True:
        func.debug_message("--placeholder function--")
        odp = input(f"{cnst.def_txt_clr}\
        \nenter a paragraph number you want to jump to:\
        \n{cnst.input_sign}{cnst.def_txt_clr}")

        if odp == 'exit':
            exit()

        func.get_music('main', 1200)  # loading background music
        try:
            if len(odp) > 0:
                eval("_" + odp + "()")
        except NameError as e:
            func.error_message("NameError", e)


# - - - - - - - - -
# /// PARAGRAPHS
# - - - - - - - - -
def _00():
    func.dub_play('00a', 'adam')

    while True:  # elixir choice menu
        func.dub_play('elxr_chc', 'adam', False)
        choice = input(f'{cnst.input_sign}{cnst.def_txt_clr}')

        if choice == '1':
            cnst.potion = 'z'
            break
        elif choice == '2':
            cnst.potion = 'w'
            break
        elif choice == '3':
            cnst.potion = 's'
            break
        else:
            func.clear_terminal()
            print(cnst.special_txt_clr, gb.gameboook[cnst.setup_params["translation"]]['wrong_input'])

    func.get_game_state('s', new_game=True)

    func.loading(1.4)
    func.clear_terminal()

    func.dub_play('00b', 'adam')
    path_strings = [f'Ruszaj {cnst.input_sign}']
    actions = ['prg._01()']
    func.pth_selector(path_strings, actions)


def _01():
    func.dub_play('01', 'adam')
    path_strings = []
    actions = ['prg._25()']
    func.pth_selector(path_strings, actions)


def _02():
    func.dub_play('02', 'adam')
    # initiate combat with entity_002
    func.combat_main(ent.entity_002, ent.entity_002.state, ent.entity_002.esc_possible, 'prg._372(', '',
                     'prg._380()')


def _03():
    func.dub_play('03', 'adam')
    path_strings = ['Spróbuj jeszcze raz (wymagane conajmniej 13 sztuk złota)', 'Wyciągnij z plecaka linę',
                    'Podejdź do mostu', 'Spróbuj przeskoczyć przez rozpadlinę (przynajmniej 18W i 9Z)']
    actions = ['prg._136()', 'prg._13()', 'prg._269()', 'prg._74()', 'prg._110()']
    func.pth_selector(path_strings, actions)


def _04():
    func.dub_play('04', 'adam')
    path_strings = ['Chwytasz za miecz i atakujesz', 'Postanawiasz czekać dalej']
    actions = ['prg._318()', 'prg._295()']
    func.pth_selector(path_strings, actions)


def _05():
    func.dub_play('05', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['prg._312()', 'prg._140()']
    func.pth_selector(path_strings, actions)


def _06a():
    func.stats_change('Szczęście', cnst.s_count, 1)
    path_strings = []
    actions = ['prg._06b()']
    func.pth_selector(path_strings, actions)


def _06b():
    func.dub_play('06', 'adam')
    path_strings = []
    actions = ['prg._115()']
    func.pth_selector(path_strings, actions)


def _07():
    func.dub_play('07', 'adam')
    path_strings = []
    actions = ['prg._219()']
    func.pth_selector(path_strings, actions)


def _08():
    func.dub_play('08', 'adam')
    path_strings = ['Walcz u boku prześladowanego stwora przeciw zgrai jego współplemieńców', 'Ratuj się Ucieczką']
    actions = ['prg._210()', 'prg._98()']
    func.pth_selector(path_strings, actions)


def _09():
    func.dub_play('09', 'adam')
    path_strings = ['Sprzedaj kamień krasnalowi', 'Nie sprzedawaj kamienia']
    actions = ['prg._289()', 'prg._375()']
    func.pth_selector(path_strings, actions)


def _10():
    func.dub_play('10', 'adam')
    _xx()


def _11():
    func.dub_play('11', 'adam')
    path_strings = ['idziesz od razu po wodę', 'dobierasz się do stwora']
    actions = ['prg._45()', 'prg._192()']
    func.pth_selector(path_strings, actions)


def _12():
    func.dub_play('12', 'adam')
    path_strings = []
    actions = ['prg._288()']
    func.pth_selector(path_strings, actions)


def _13():
    func.dub_play('13', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -2)
    print('Ale to tylko chwila. Wielkimi susami biegniesz w kierunku potwora')
    path_strings = []
    actions = ['prg._126()']
    func.pth_selector(path_strings, actions)


def _14():
    func.dub_play('14', 'adam')
    path_strings = ['Wychodzisz północnymi drzwiami', 'Wychodzisz wschodnimi drzwiami']
    actions = ['prg._197()', 'prg._39()']
    func.pth_selector(path_strings, actions)


def _15():
    func.dub_play('15', 'adam')
    path_strings = ['Rezygnujesz z przepłynięcia jeziora', 'Decydujesz się podjąć próbę przepłynięcia jeziora']
    actions = ['prg._241()', 'prg._113()']
    func.pth_selector(path_strings, actions)
    # print('Jeśli rezygnujesz z przepłynięcia jeziora - patrz 241\
    # \nNatomiast jeśli decydujesz się podjąć próbę przepłynięcia jeziora, zapisz numer niniejszego paragrafu i patrz 113')


def _16a():
    func.dub_play('16a', 'adam')
    func.eatables()
    print(gb.gameboook[cnst.translation]['16b'])
    path_strings = []
    actions = ['prg._80()']
    func.pth_selector(path_strings, actions)


def _17():
    path_strings = ['Zobacz co za nimi jest', 'Wycofaj się']
    actions = ['prg._265()', 'prg._50()']
    func.pth_selector(path_strings, actions)


def _18():
    func.dub_play('18', 'adam')
    path_strings = ['Jeśli tak, pamiętaj że musisz mieć przynajmniej 5 sztuk złota', 'Wycofujesz się']
    actions = ['prg._211()', 'prg._286()']
    func.pth_selector(path_strings, actions)


def _19():
    func.dub_play('19', 'adam')
    func.stats_change('Prowiant', cnst.eatables_count, 1)
    func.stats_change('Szczęście', cnst.s_count, 2)
    path_strings = []
    actions = ['prg._141()']
    func.pth_selector(path_strings, actions)


def _20():
    func.dub_play('20', 'adam', False)
    path_strings = []
    actions = ['prg._238a()']
    func.pth_selector(path_strings, actions)


def _21():
    path_strings = ['Zobacz co jest za drzwiami', 'Zawróć']
    actions = ['prg._332()', 'prg._212()']
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
    func.dub_play('25', 'adam', False)
    path_strings = ['Idziesz na zachód', 'Wybierasz drogę prowadzącą na wschód']
    actions = ['prg._200()', 'prg._44()']
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
    actions = ['prg._116a()']
    func.pth_selector(path_strings, actions)


def _30():
    func.dub_play('30', 'adam')
    _xx()


def _31():
    func.dub_play('31', 'adam')
    path_strings = []
    actions = ['prg._119()']
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
    func.update_variable(cnst.choice_count, 1)
    if cnst.choice_count < 3:
        eval('_115()')
    else:
        eval('_68()')


def _38():
    func.dub_play('38', 'adam')
    _xx()


def _39():
    func.dub_play('39', 'adam', False)
    path_strings = ['zachód', 'północ', 'południe']
    actions = ['prg._331()', 'prg._228()', 'prg._146()']
    func.pth_selector(path_strings, actions)


def _43():
    func.dub_play('43', 'adam')
    _xx()


def _44():
    func.dub_play('44', 'adam')
    path_strings = ['Rezygnujesz', 'Wyważasz drzwi']
    actions = ['prg._75()', 'prg._105()']
    func.pth_selector(path_strings, actions)


def _45():
    func.dub_play('45', 'adam')
    func.stats_change('Szczęscie', cnst.s_count, 2)
    path_strings = []
    actions = ['prg._251()']
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
    actions = ['prg._310()', 'prg._130()', 'prg._64()']
    func.pth_selector(path_strings, actions)


def _56():
    func.dub_play('56', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -1)
    path_strings = []
    actions = ['prg._75()']
    func.pth_selector(path_strings, actions)


def _59():
    func.dub_play('59', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['prg._14()', 'prg._70()']
    func.pth_selector(path_strings, actions)


def _64():
    func.dub_play('64', 'adam', False)
    path_strings = ['zachód', 'północ', 'wschód', 'południe']
    actions = ['prg._296()', 'prg._264()', 'prg._284()', 'prg._224()']
    func.pth_selector(path_strings, actions)


def _67():
    func.dub_play('67', 'adam')
    path_strings = ['Musisz się wycofać.']
    actions = ['prg._50()']
    func.pth_selector(path_strings, actions)


def _68():
    func.dub_play('68', 'adam')
    path_strings = []
    actions = ['prg._212()']
    func.pth_selector(path_strings, actions)


def _69a():
    func.dub_play('69a', 'adam')
    func.combat_main(ent.entity_069_1, True, ent.entity_069_1.esc_possible, '', '', 'prg._69b()')


def _69b():
    func.dub_play('69b', 'adam')
    func.combat_main(ent.entity_069_2, True, ent.entity_069_2.esc_possible, '', '', 'prg._69c()')


def _69c():
    func.dub_play('69c', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['prg._305()', 'prg._291()']
    func.pth_selector(path_strings, actions)


def _70():
    func.dub_play('70', 'adam')
    _xx()


def _75():
    func.dub_play('75', 'adam')
    path_strings = []
    actions = ['prg._200()']
    func.pth_selector(path_strings, actions)


def _76():
    func.dub_play('76', 'adam')
    _xx()


def _82():
    func.dub_play('82', 'adam')
    _xx()


def _89():
    func.dub_play('89a', 'adam', False)
    cnst.s_count = func.stats_change('Szczęscie', cnst.s_count, 2, cnst.s_init)
    cnst.gold_amount = func.stats_change('Złoto', cnst.gold_amount, 3)
    func.dub_play('89b', 'adam')
    path_strings = []
    actions = ['prg._120()']
    func.pth_selector(path_strings, actions)


def _95():
    func.update_variable(cnst.choice_count, 1)
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
    actions = ['prg._362()', 'prg._234()']
    func.pth_selector(path_strings, actions)


def _102():
    func.dub_play('102', 'adam')
    path_strings = ['zachód', 'północ', 'wschód', 'południe']
    actions = ['prg._123()', 'prg._268()', 'prg._374()', 'prg._351()']
    func.pth_selector(path_strings, actions)


def _103():
    func.dub_play('103', 'adam')
    path_strings = []
    actions = ['prg._345()']
    func.pth_selector(path_strings, actions)


def _104():
    func.dub_play('104', 'adam')
    path_strings = []
    actions = ['prg._121()']
    func.pth_selector(path_strings, actions)


def _105():
    func.dub_play('105', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -1)
    print('Czy chcesz ponowić próbę?')
    path_strings = ['tak', 'nie']
    actions = ['prg._56()', 'prg._75()']
    func.pth_selector(path_strings, actions)


def _106():
    func.dub_play('106', 'adam')
    path_strings = ['Broń się mieczem', 'Masz jedno albo drugie', 'Masz jedno i drugie']
    actions = ['_213()', '_24()', '_292()']
    func.pth_selector(path_strings, actions)


def _107():
    # initiate combat with entity_107
    func.combat_main(ent.entity_107, True, ent.entity_107.esc_possible, '', '', '_23()')


def _112():
    value = random.randint(4, 48)  # 4 dice auto randomizing
    if value >= 18:
        print('Szczęście ci sprzyja')
        _28()
    else:
        print('Szczęście ci nie sprzyja')
        _291()


def _113():
    func.dub_play('113', 'adam')
    path_strings = ['blank', 'blank']
    actions = ['prg._xx()', 'prg._xx()']
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
            print("Wrong input")

    cnst.main_eq.append(usr_input)
    func.eq_change(usr_input)
    eval(cnst.choices_115[usr_input])


def _116a():
    func.dub_play('116a', 'adam')
    func.combat_main(ent.entity_116, ent.entity_116.state, ent.entity_116.esc_possible, '', '',
                     'prg._116b()')


def _116b():
    func.dub_play('116b', 'adam', False)
    path_strings = ['Rozejrzyj się', 'Opuść pieczarę']
    actions = ['prg._89()', 'prg._120()']
    func.pth_selector(path_strings, actions)


def _119():
    func.dub_play('119', 'adam')
    path_strings = ['Przeszukaj ciało', 'Opuść komnatę']
    actions = ['prg._31()', 'prg._102()']
    func.pth_selector(path_strings, actions)


def _120():
    func.dub_play('120', 'adam')
    path_strings = []
    actions = ['prg._64()']
    func.pth_selector(path_strings, actions)


def _123():
    func.dub_play('123', 'adam')
    path_strings = []
    actions = ['prg._39()']
    func.pth_selector(path_strings, actions)


def _128():
    func.dub_play('128', 'adam')
    _xx()


def _130():
    func.dub_play('130', 'adam')
    path_strings = []
    actions = ['prg._212()']
    func.pth_selector(path_strings, actions)


def _132():
    func.dub_play('132', 'adam')
    path_strings = ['Tak', 'Nie']
    actions = ['prg._233()', 'prg._128()']
    func.pth_selector(path_strings, actions)


def _136():
    func.dub_play('136', 'adam')
    path_strings = []
    actions = ['prg._186()']
    func.pth_selector(path_strings, actions)


def _146():
    func.dub_play('146', 'adam')
    path_strings = []
    actions = ['prg._64()']
    func.pth_selector(path_strings, actions)


def _153():
    func.dub_play('153', 'adam')

    func.stats_change('Szczęście', cnst.s_count, 1)
    func.update_variable(cnst.p_hit_val_, cnst.p_hit_val_ + 1)

    path_strings = []
    actions = ['prg._115()']
    func.pth_selector(path_strings, actions)


def _158():
    func.dub_play('158', 'adam')
    path_strings = ['Jeszcze raz spróbuj(wymagane przynajmniej 10 sztuk złota) ze Smokiem', 'nie chcesz']
    actions = ["check_for_gold_amount(_64(),_false_path(), 10)", '_269()']
    func.pth_selector(path_strings, actions)


def _160():
    func.dub_play('160', 'adam')
    path_strings = []
    actions = ['prg._10()']
    func.pth_selector(path_strings, actions)


def _170():
    func.dub_play('170', 'adam')
    path_strings = ['północ', 'wschód', 'południe']
    actions = ['prg._84()', 'prg._319()', 'prg._357()']
    func.pth_selector(path_strings, actions)


def _175():
    path_strings = []
    actions = ['prg._373()']
    func.pth_selector(path_strings, actions)


def _176():
    func.dub_play('176', 'adam')
    path_strings = ['północ', 'wschód']
    actions = ['prg._27()', 'prg._230()']
    func.pth_selector(path_strings, actions)


def _177():
    func.dub_play('177', 'adam')
    func.stats_change('Szczęście', cnst.s_count, 4)
    path_strings = []
    actions = ['prg._330()']
    func.pth_selector(path_strings, actions)


def _178():
    func.dub_play('178', 'adam')
    path_strings = []
    actions = ['prg._15()']
    func.pth_selector(path_strings, actions)


def _179():
    path_strings = []
    actions = ['prg._373()']
    func.pth_selector(path_strings, actions)


def _180():
    if ent.room_364.visit_count <= 2:
        func.dub_play('180', 'adam')

        cnst.main_eq.append('key;45')

        func.eq_change("klucz z liczbą '45'")

    path_strings = []
    actions = ['prg._120()']
    func.pth_selector(path_strings, actions)


def _181():
    func.dub_play('181', 'adam')
    path_strings = ['Masz linę', 'Nie masz liny']
    actions = ['prg._329()', 'prg._32()']
    func.pth_selector(path_strings, actions)


def _182():
    func.dub_play('182', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['prg._30()', 'prg._259()']
    func.pth_selector(path_strings, actions)


def _183():
    func.dub_play('183', 'adam')
    _xx()


def _184():
    func.dub_play('184', 'adam')
    # initiate combat with entity_184
    func.combat_main(ent.entity_184, True, ent.entity_184.esc_possible, '_385(', '_226(', '_234()')


def _185():
    func.dub_play('185', 'dreszcz_p_185.mp3')
    path_strings = []
    actions = ['prg._252()']
    func.pth_selector(path_strings, actions)


def _186():
    func.dub_play('186', 'adam')
    path_strings = ['A', 'B', 'C']
    actions = ['prg._368()', 'prg._117()', 'prg._360()']
    func.pth_selector(path_strings, actions)


def _187():
    print(gb.gameboook[cnst.translation]['187'])
    _xx()


def _190():
    func.dub_play('190', 'adam')
    path_strings = []
    actions = ['prg._115()']
    func.pth_selector(path_strings, actions)


def _192():
    func.dub_play('192', 'adam')
    path_strings = ['Wybierasz wodę', 'Wybierz przedmiot']
    actions = ['prg._306()', 'prg._220()']
    func.pth_selector(path_strings, actions)
    # Żeby nabrać wody musisz mieć naczynie. Jeśli masz, ale jest pełne, zastanów się: może warto wylać jego zawartość.


def _197():
    print(gb.gameboook[cnst.translation]['197'])
    _xx()


def _198():
    print(gb.gameboook[cnst.translation]['198'])
    _xx()


def _199():
    print(gb.gameboook[cnst.translation]['199'])
    _xx()


def _200():
    func.dub_play('200', 'adam', False)
    path_strings = []
    actions = ['prg._120()', 'prg._301()']
    func.pth_selector(path_strings, actions, True, ent.room_364)


def _210():
    print(gb.gameboook[cnst.translation]['210'])
    _xx()


def _212():
    func.dub_play('212', 'adam')
    path_strings = ['zachód', 'północ', 'zachód', 'połódnie']
    actions = ['prg._287()', 'prg._38()', 'prg._82()', 'prg._336()']
    func.pth_selector(path_strings, actions)


def _220():
    print(gb.gameboook[cnst.translation]['220'])
    _xx()


def _224():
    func.dub_play('224', 'adam')
    path_strings = []
    actions = ['prg._180()', 'prg._301()']
    func.pth_selector(path_strings, actions, True, ent.room_364)


def _226():
    func.dub_play('226', 'adam')
    path_strings = ['tak', 'nie']
    actions = [
        'prg._101(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path(',
        'prg._385()']
    func.pth_selector(path_strings, actions)


def _228():
    func.dub_play('228', 'adam')
    path_strings = []
    actions = ['prg._102()']
    func.pth_selector(path_strings, actions)


def _232():
    func.update_variable(cnst.choice_count, 1)
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
    actions = ['prg._205()', 'prg._199()']
    func.pth_selector(path_strings, actions)


def _238a():
    func.dub_play('238a', 'adam')
    func.combat_main(ent.entity_238_1, ent.entity_238_1.state, ent.entity_238_1.esc_possible,
                     'prg._316(', 'prg._238b(', 'prg._xx()')


def _238b():
    func.combat_main(ent.entity_238_2, ent.entity_238_2.state, ent.entity_238_2.esc_possible,
                     'prg._316(', 'prg._238c(', 'prg._xx()')


def _238c():
    func.combat_main(ent.entity_238_3, ent.entity_238_3.state, ent.entity_238_3.esc_possible,
                     'prg._316(', 'prg._238d(', 'prg._xx()')


def _238d():
    func.combat_main(ent.entity_238_4, ent.entity_238_4.state, ent.entity_238_4.esc_possible,
                     'prg._316(', 'prg._238e(', 'prg._xx()')


def _238e():
    func.combat_main(ent.entity_238_5, ent.entity_238_5.state, ent.entity_238_5.esc_possible,
                     'prg._316(', 'prg._xx(', 'prg._xx()')


def _241():
    func.dub_play('241', 'adam')
    path_strings = []
    actions = ['prg._132()']
    func.pth_selector(path_strings, actions)


def _242():
    path_strings = []
    actions = ['action']
    func.pth_selector(path_strings, actions)


def _251():
    func.get_music('main', 1500)  # loading background music

    func.dub_play('251', 'adam')
    path_strings = []
    actions = ['prg._39()']
    func.pth_selector(path_strings, actions)


def _264():
    func.dub_play('264', 'adam')
    path_strings = []
    actions = ['prg._102()']
    func.pth_selector(path_strings, actions)


def _265():
    func.dub_play('265', 'adam')
    _xx()


def _268():
    func.dub_play('268', 'adam')
    path_strings = ["Jeśli jeszcze za nimi nie byłeś, możesz wejść.", "Wolisz zawrócić"]
    actions = ['prg._317a()', 'prg._102()']
    func.pth_selector(path_strings, actions)


def _269():
    func.dub_play('269', 'adam')
    func.stats_change('Wytrzymałosć', cnst.w_count, -2)
    path_strings = ["Zapłać według taryfy(przynajmniej 10 sztuk złota)", "Podejdź do mostu",
                    "Spróbuj przeskoczyć przez rozpadlinę(przynajmniej 18W i 9Z)", 'Ponów próbę z liną']
    actions = ['check_for_gold_amount((_35(), pass, _10()', '_110()', '_358()']
    func.pth_selector(path_strings, actions)


def _271():
    func.dub_play('271a', 'adam')
    func.stats_change('Wytrzymałosć', cnst.w_count, -1)
    func.dub_play('271b', 'dreszcz_p_271b.mp3')

    path_strings = ['wymień', 'nie wymieniaj']
    actions = ['prg._190()', 'prg._153()']
    func.pth_selector(path_strings, actions)


def _284():
    func.dub_play('284', 'adam')
    func.check_for_luck()

    if not cnst.p_luck:
        func.stats_change('Wytrzymałość', cnst.w_count, -2)

    path_strings = []
    actions = ['prg._50()']
    func.pth_selector(path_strings, actions)


def _287():
    func.dub_play('287', 'adam')
    _xx()


def _291():
    func.dub_play('291', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -2)
    path_strings = []
    actions = ['prg._330()']
    func.pth_selector(path_strings, actions)


def _296():
    func.dub_play('296a', 'adam', False)
    func.eatables()
    func.dub_play('296b', 'adam')
    path_strings = []
    actions = ['prg._39()']
    func.pth_selector(path_strings, actions)


def _298():
    func.update_variable(cnst.choice_count, 1)
    if cnst.choice_count < 3:
        eval('_115()')
    else:
        eval('_68()')


def _301():
    func.dub_play('301', 'adam', False)
    path_strings = ['Spróbuj otworzyć drzwi', 'Zawróć']
    actions = ['prg._364()', 'prg._120()']
    func.pth_selector(path_strings, actions)


def _305():
    func.dub_play('305', 'adam')
    path_strings = ['zdaj się na los', 'sprawdź czy masz szczęście']
    actions = ['prg._112()', 'prg._381()']
    func.pth_selector(path_strings, actions)


def _310():
    func.dub_play('310', 'adam')
    path_strings = []
    actions = ['prg._67()', 'prg._17()']
    func.pth_selector(path_strings, actions, True, ent.room_310)


def _316():
    func.dub_play('316', 'adam')
    path_strings = []
    actions = ['prg._176()']
    func.pth_selector(path_strings, actions)


def _317a():
    func.dub_play('317a', 'adam')
    func.combat_main(ent.entity_317, ent.entity_317.state, ent.entity_317.esc_possible, '', '',
                     'prg._317b()')


def _317b():
    func.dub_play('317b', 'adam')
    path_strings = ['Rozejrzyj się chociaż po ścianch', 'Nie brzydzę się']
    actions = ['prg._119()', 'prg._31()']
    func.pth_selector(path_strings, actions)


def _324():
    func.update_variable(cnst.choice_count, 1)
    if cnst.choice_count < 3:
        eval('_115()')
    else:
        eval('_68()')


def _330():
    func.dub_play('330', 'adam')
    path_strings = []
    actions = ['prg._170()']
    func.pth_selector(path_strings, actions)


def _331():
    func.dub_play('331', 'adam')
    path_strings = []
    actions = ['prg._59()', 'prg._11()']
    func.pth_selector(path_strings, actions, True, ent.room_331)


def _332():
    func.dub_play('332a', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -2)
    func.dub_play('332b', 'adam')
    func.combat_main(ent.entity_332, True, ent.entity_332.esc_possible, '', '', 'prg._06a()')


def _336():
    func.dub_play('336', 'adam')
    path_strings = []
    actions = ['prg._06b()', 'prg._21()']
    func.pth_selector(path_strings, actions, True, ent.room_336)


def _344():
    func.dub_play('344', 'adam')
    func.combat_main(ent.entity_344, True, ent.entity_344.esc_possible, '', '', "prg._23()")


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
    actions = ['prg._64()']
    func.pth_selector(path_strings, actions)


def _358():
    func.dub_play('358', 'adam')
    path_strings = []
    actions = ['prg._xx()']
    func.pth_selector(path_strings, actions)


def _364():
    # change door state to "open"
    ent.room_364.room_state = func.update_variable(ent.room_364.room_state, True)

    func.dub_play('364', 'adam', False)
    path_strings = ['Próbujesz zabrać ukradkiem pudełko', 'Decydujesz się podjąć walkę']
    actions = ['prg._29()', 'prg._116a()']
    func.pth_selector(path_strings, actions, '', ent.room_364)


def _372():
    func.dub_play('372', 'adam')
    path_strings = []
    actions = ['prg._xx()']
    func.pth_selector(path_strings, actions)


def _374():
    func.dub_play('374', 'adam')
    func.eatables()
    path_strings = []
    actions = ['prg._178()']
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
