import random
import gamebook as gb
import entities as ent
import functions as func
import constants as cnst


# jump paragraph
def _xx():
    while True:
        func.debug_message("--jump paragraph--")
        odp = input(f"{cnst.DEFAULT_COLOR}\
        \nenter number of a paragraph you want to jump to or type 'exit'\
        \n{cnst.INPUT_SIGN}{cnst.DEFAULT_COLOR}")

        if odp == 'exit':
            func.clear_terminal()
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
        func.dub_play('elxr_chc', 'adam', False, r_robin=5)
        choice = input(f'{cnst.INPUT_SIGN}{cnst.DEFAULT_COLOR}')

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
            print(cnst.SPECIAL_COLOR, gb.gameboook[cnst.setup_params["translation"]]['wrong_input'])

    func.get_game_state('s', new_game=True)
    func.clear_terminal()

    func.dub_play('00b', 'adam')
    path_strings = [f'Ruszaj {cnst.INPUT_SIGN}']
    actions = ['01']
    func.pth_selector(path_strings, actions)


def _01():
    func.dub_play('01', 'adam')

    actions = ['25']
    func.pth_selector(actions=actions)


def _02():
    func.dub_play('02', 'adam')
    # initiate combat with entity_002
    func.combat_main(ent.entity_002, ent.entity_002.state, ent.entity_002.esc_possible, '372', '', '380')


def _03():
    func.dub_play('03', 'adam')
    path_strings = ['Spróbuj jeszcze raz (wymagane conajmniej 13 sztuk złota)', 'Wyciągnij z plecaka linę',
                    'Podejdź do mostu', 'Spróbuj przeskoczyć przez rozpadlinę (przynajmniej 18W i 9Z)']
    actions = ['136', '13', '269', '74', '110']
    func.pth_selector(path_strings, actions)


def _04():
    func.dub_play('04', 'adam')
    path_strings = ['Chwytasz za miecz i atakujesz', 'Postanawiasz czekać dalej']
    actions = ['318', '295']
    func.pth_selector(path_strings, actions)


def _05():
    func.dub_play('05', 'dunmer')
    path_strings = ['tak', 'nie']
    actions = ['312', '140']
    func.pth_selector(path_strings, actions)


def _06a():
    func.stats_change('Szczęście', cnst.s_count, 1)

    actions = ['06b']
    func.pth_selector(actions=actions)


def _06b():
    func.dub_play('06', 'adam')

    actions = ['115']
    func.pth_selector(actions=actions)


def _07():
    func.dub_play('07', 'adam')

    actions = ['219']
    func.pth_selector(actions=actions)


def _08():
    func.dub_play('08', 'adam')
    path_strings = ['Walcz u boku prześladowanego stwora przeciw zgrai jego współplemieńców', 'Ratuj się Ucieczką']
    actions = ['210', '98']
    func.pth_selector(path_strings, actions)


def _09():
    func.dub_play('09', 'adam')
    path_strings = ['Sprzedaj kamień krasnalowi', 'Nie sprzedawaj kamienia']
    actions = ['289', '375']
    func.pth_selector(path_strings, actions)


def _10():
    func.dub_play('10', 'adam')
    _xx()


def _11():
    func.dub_play('11', 'dunmer')
    path_strings = ['idziesz od razu po wodę', 'dobierasz się do stwora']
    actions = ['45', '192']
    func.pth_selector(path_strings, actions)


def _12():
    func.dub_play('12', 'adam')

    actions = ['288']
    func.pth_selector(actions=actions)


def _13():
    func.dub_play('13', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -2)
    print('Ale to tylko chwila. Wielkimi susami biegniesz w kierunku potwora')

    actions = ['126']
    func.pth_selector(actions=actions)


def _14():
    func.dub_play('14', 'adam')
    path_strings = ['Wychodzisz północnymi drzwiami', 'Wychodzisz wschodnimi drzwiami']
    actions = ['197', '39']
    func.pth_selector(path_strings, actions)


def _15():
    func.dub_play('15', 'adam')
    path_strings = ['Rezygnujesz z przepłynięcia jeziora', 'Decydujesz się podjąć próbę przepłynięcia jeziora']
    actions = ['241', '113']
    func.pth_selector(path_strings, actions)
    # print('Jeśli rezygnujesz z przepłynięcia jeziora - patrz 241\
    # \nNatomiast jeśli decydujesz się podjąć próbę przepłynięcia jeziora, zapisz numer niniejszego paragrafu i patrz 113')


def _16a():
    func.dub_play('16a', 'adam')
    func.eatables()
    print(gb.gameboook[cnst.setup_params["translation"]]['16b'])

    actions = ['80']
    func.pth_selector(actions=actions)


def _17():
    path_strings = ['Zobacz co za nimi jest', 'Wycofaj się']
    actions = ['265', '50']
    func.pth_selector(path_strings, actions)


def _18():
    func.dub_play('18', 'adam')
    path_strings = ['Jeśli tak, pamiętaj że musisz mieć przynajmniej 5 sztuk złota', 'Wycofujesz się']
    actions = ['211', '286']
    func.pth_selector(path_strings, actions)


def _19():
    func.dub_play('19', 'adam')
    func.stats_change('Prowiant', cnst.meal_count, 1)
    func.stats_change('Szczęście', cnst.s_count, 2)

    actions = ['141']
    func.pth_selector(actions=actions)


def _20():
    func.dub_play('20', 'adam')

    actions = ['238a']
    func.pth_selector(actions=actions)


def _21():
    path_strings = ['Zobacz co jest za drzwiami', 'Zawróć']
    actions = ['332', '212']
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
    actions = ['200', '44']
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

    actions = ['116a']
    func.pth_selector(actions=actions)


def _30():
    func.dub_play('30', 'adam')
    _xx()


def _31():
    func.dub_play('31', 'adam')

    actions = ['119']
    func.pth_selector(actions=actions)


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
        _115()
    else:
        _68()


def _38():
    func.dub_play('38', 'adam')
    _xx()


def _39():
    func.dub_play('39', 'adam')
    path_strings = ['zachód', 'północ', 'południe']
    actions = ['331', '228', '146']
    func.pth_selector(path_strings, actions)


def _40():
    func.dub_play('40', 'adam')
    _xx()


def _41():
    func.dub_play('41', 'adam')
    _xx()


def _42():
    func.dub_play('42', 'adam')
    _xx()


def _43():
    func.dub_play('43', 'adam')
    _xx()


def _44():
    func.dub_play('44', 'adam')
    path_strings = ['Rezygnujesz', 'Wyważasz drzwi']
    actions = ['75', '105']
    func.pth_selector(path_strings, actions)


def _45():
    func.dub_play('45', 'adam')
    func.stats_change('Szczęscie', cnst.s_count, 2)

    actions = ['251']
    func.pth_selector(actions=actions)


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
    actions = ['310', '130', '64']
    func.pth_selector(path_strings, actions)


def _51():
    func.dub_play('51', 'adam')
    _xx()


def _52():
    func.dub_play('52', 'adam')
    _xx()


def _53():
    func.dub_play('53', 'adam')
    _xx()


def _54():
    func.dub_play('54', 'adam')
    _xx()


def _55():
    func.dub_play('55', 'adam')
    _xx()


def _56():
    func.dub_play('56', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -1)

    actions = ['75']
    func.pth_selector(actions=actions)


def _57():
    func.dub_play('57', 'adam')
    _xx()


def _58():
    func.dub_play('58', 'adam')
    _xx()


def _59():
    func.dub_play('59', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['14', '70']
    func.pth_selector(path_strings, actions)


def _60():
    func.dub_play('60', 'adam')
    _xx()


def _61():
    func.dub_play('61', 'adam')
    _xx()


def _64():
    func.dub_play('64', 'adam')
    path_strings = ['zachód', 'północ', 'wschód', 'południe']
    actions = ['296', '264', '284', '224']
    func.pth_selector(path_strings, actions)


def _65():
    func.dub_play('65', 'adam')
    _xx()


def _66():
    func.dub_play('66', 'adam')
    _xx()


def _67():
    func.dub_play('67', 'adam')
    path_strings = ['Musisz się wycofać.']
    actions = ['50']
    func.pth_selector(path_strings, actions)


def _68():
    func.dub_play('68', 'adam')

    actions = ['212']
    func.pth_selector(actions=actions)


def _69a():
    func.dub_play('69a', 'adam')
    func.combat_main(ent.entity_069_1, True, ent.entity_069_1.esc_possible, '', '', '69b')


def _69b():
    func.dub_play('69b', 'adam')
    func.combat_main(ent.entity_069_2, True, ent.entity_069_2.esc_possible, '', '', '69c')


def _69c():
    func.dub_play('69c', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['305', '291']
    func.pth_selector(path_strings, actions)


def _70():
    func.dub_play('70', 'adam')
    _xx()


def _71():
    func.dub_play('71', 'adam')
    _xx()


def _72():
    func.dub_play('72', 'adam')
    _xx()


def _73():
    func.dub_play('73', 'adam')
    _xx()


def _74():
    func.dub_play('74', 'adam')
    _xx()


def _75():
    func.dub_play('75', 'adam')

    actions = ['200']
    func.pth_selector(actions=actions)


def _76():
    func.dub_play('76', 'adam')
    _xx()


def _77():
    func.dub_play('77', 'adam')
    _xx()


def _78():
    func.dub_play('78', 'adam')
    _xx()


def _79():
    func.dub_play('79', 'adam')
    _xx()


def _80():
    func.dub_play('80', 'adam')
    _xx()


def _81():
    func.dub_play('81', 'adam')
    _xx()


def _82():
    func.dub_play('82', 'adam')
    _xx()


def _83():
    func.dub_play('83', 'adam')
    _xx()


def _84():
    func.dub_play('84', 'adam')
    _xx()


def _85():
    func.dub_play('85', 'adam')
    _xx()


def _86():
    func.dub_play('86', 'adam')
    _xx()


def _87():
    func.dub_play('87', 'adam')
    _xx()


def _88():
    func.dub_play('88', 'adam')
    _xx()


def _89():
    func.dub_play('89a', 'adam')
    cnst.s_count = func.stats_change('Szczęscie', cnst.s_count, 2, cnst.s_init)
    cnst.gold_amount = func.stats_change('Złoto', cnst.gold_amount, 3)
    func.dub_play('89b', 'adam')

    actions = ['120']
    func.pth_selector(actions=actions)


def _90():
    func.dub_play('90', 'adam')
    _xx()


def _91():
    func.dub_play('01', 'adam')
    _xx()


def _92():
    func.dub_play('92', 'adam')
    _xx()


def _93():
    func.dub_play('93', 'adam')
    _xx()


def _94():
    func.dub_play('94', 'adam')
    _xx()


def _95():
    func.update_variable(cnst.choice_count, 1)
    if cnst.choice_count < 3:
        _115()  # are these correct number
    else:
        _68()


def _96():
    func.dub_play('96', 'adam')
    _xx()


def _97():
    func.dub_play('97', 'adam')
    _xx()


def _98():
    func.dub_play('98', 'adam')
    _xx()


def _99():
    func.dub_play('99', 'adam')
    _xx()


def _100():
    func.dub_play('100', 'adam')
    _xx()


def _101():
    print(f'{ent.entity_184.name} prosi o łaskę.')
    path_strings = ['Darujesz mu życie', 'Walczysz aż do końca']
    actions = ['362', '234']
    func.pth_selector(path_strings, actions)


def _102():
    func.dub_play('102', 'adam')
    path_strings = ['zachód', 'północ', 'wschód', 'południe']
    actions = ['123', '268', '374', '351']
    func.pth_selector(path_strings, actions)


def _103():
    func.dub_play('103', 'adam')

    actions = ['345']
    func.pth_selector(actions=actions)


def _104():
    func.dub_play('104', 'adam')

    actions = ['121']
    func.pth_selector(actions=actions)


def _105():
    func.dub_play('105', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -1)
    print('Czy chcesz ponowić próbę?')
    path_strings = ['tak', 'nie']
    actions = ['56', '75']
    func.pth_selector(path_strings, actions)


def _106():
    func.dub_play('106', 'adam')
    path_strings = ['Broń się mieczem', 'Masz jedno albo drugie', 'Masz jedno i drugie']
    actions = ['213', '24', '292']
    func.pth_selector(path_strings, actions)


def _107():
    # initiate combat with entity_107
    func.combat_main(ent.entity_107, True, ent.entity_107.esc_possible, '', '', '23')


def _108():
    func.dub_play('108', 'adam')
    _xx()


def _109():
    func.dub_play('109', 'adam')
    _xx()


def _110():
    func.dub_play('110', 'adam')
    _xx()


def _111():
    func.dub_play('111', 'adam')
    _xx()


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
    _xx()


def _114():
    func.dub_play('114', 'adam')
    _xx()


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
                     '116b')


def _116b():
    func.dub_play('116b', 'adam')
    path_strings = ['Rozejrzyj się', 'Opuść pieczarę']
    actions = ['89', '120']
    func.pth_selector(path_strings, actions)


def _117():
    func.dub_play('117', 'adam')
    _xx()


def _118():
    func.dub_play('118', 'adam')
    _xx()


def _119():
    func.dub_play('119', 'adam')
    path_strings = ['Przeszukaj ciało', 'Opuść komnatę']
    actions = ['31', '102']
    func.pth_selector(path_strings, actions)


def _120():
    func.dub_play('120', 'adam')

    actions = ['64']
    func.pth_selector(actions=actions)


def _121():
    func.dub_play('121', 'adam')
    _xx()


def _122():
    func.dub_play('122', 'adam')
    _xx()


def _123():
    func.dub_play('123', 'adam')

    actions = ['39']
    func.pth_selector(actions=actions)


def _124():
    func.dub_play('124', 'adam')
    _xx()


def _125():
    func.dub_play('125', 'adam')
    _xx()


def _126():
    func.dub_play('126', 'adam')
    _xx()


def _127():
    func.dub_play('127', 'adam')
    _xx()


def _128():
    func.dub_play('128', 'adam')
    _xx()


def _129():
    func.dub_play('129', 'adam')
    _xx()


def _130():
    func.dub_play('130', 'adam')

    actions = ['212']
    func.pth_selector(actions=actions)


def _131():
    func.dub_play('131', 'adam')
    _xx()


def _132():
    func.dub_play('132', 'adam')
    path_strings = ['Tak', 'Nie']
    actions = ['233', '128']
    func.pth_selector(path_strings, actions)


def _133():
    func.dub_play('133', 'adam')
    _xx()


def _134():
    func.dub_play('134', 'adam')
    _xx()


def _135():
    func.dub_play('135', 'adam')
    _xx()


def _136():
    func.dub_play('136', 'adam')

    actions = ['186']
    func.pth_selector(actions=actions)


def _137():
    func.dub_play('137', 'adam')
    _xx()


def _138():
    func.dub_play('138', 'adam')
    _xx()


def _139():
    func.dub_play('139', 'adam')
    _xx()


def _140():
    func.dub_play('140', 'adam')
    _xx()


def _141():
    func.dub_play('141', 'adam')
    _xx()


def _142():
    func.dub_play('142', 'adam')
    _xx()


def _143():
    func.dub_play('143', 'adam')
    _xx()


def _144():
    func.dub_play('144', 'adam')
    _xx()


def _145():
    func.dub_play('145', 'adam')
    _xx()


def _146():
    func.dub_play('146', 'adam')

    actions = ['64']
    func.pth_selector(actions=actions)


def _147():
    func.dub_play('147', 'adam')
    _xx()


def _148():
    func.dub_play('148', 'adam')
    _xx()


def _149():
    func.dub_play('149', 'adam')
    _xx()


def _150():
    func.dub_play('150', 'adam')
    _xx()


def _151():
    func.dub_play('151', 'adam')
    _xx()


def _152():
    func.dub_play('152', 'adam')
    _xx()


def _153():
    func.dub_play('153', 'adam')

    func.stats_change('Szczęście', cnst.s_count, 1)
    func.update_variable(cnst.p_hit_val_, cnst.p_hit_val_ + 1)

    actions = ['115']
    func.pth_selector(actions=actions)


def _154():
    func.dub_play('154', 'adam')
    _xx()


def _155():
    func.dub_play('155', 'adam')
    _xx()


def _156():
    func.dub_play('156', 'adam')
    _xx()


def _157():
    func.dub_play('157', 'adam')
    _xx()


def _158():
    func.dub_play('158', 'adam')
    path_strings = ['Jeszcze raz spróbuj ze Smokiem (10 sztuk złota)', 'nie chcesz']
    actions = ['64', '269']
    func.pth_selector(path_strings, actions)


def _159():
    func.dub_play('159', 'adam')
    _xx()


def _160():
    func.dub_play('160', 'adam')

    actions = ['10']
    func.pth_selector(actions=actions)


def _161():
    func.dub_play('161', 'adam')
    _xx()


def _162():
    func.dub_play('162', 'adam')
    _xx()


def _163():
    func.dub_play('163', 'adam')
    _xx()


def _164():
    func.dub_play('164', 'adam')
    _xx()


def _165():
    func.dub_play('165', 'adam')
    _xx()


def _166():
    func.dub_play('166', 'adam')
    _xx()


def _167():
    func.dub_play('167', 'adam')
    _xx()


def _168():
    func.dub_play('168', 'adam')
    _xx()


def _169():
    func.dub_play('169', 'adam')
    _xx()


def _170():
    func.dub_play('170', 'adam')
    path_strings = ['północ', 'wschód', 'południe']
    actions = ['84', '319', '357']
    func.pth_selector(path_strings, actions)


def _171():
    func.dub_play('171', 'adam')
    _xx()


def _172():
    func.dub_play('172', 'adam')
    _xx()


def _173():
    func.dub_play('173', 'adam')
    _xx()


def _174():
    func.dub_play('174', 'adam')
    _xx()


def _175():
    actions = ['373']
    func.pth_selector(actions=actions)


def _176():
    func.dub_play('176', 'adam')
    path_strings = ['północ', 'wschód']
    actions = ['27', '230']
    func.pth_selector(path_strings, actions)


def _177():
    func.dub_play('177', 'adam')
    func.stats_change('Szczęście', cnst.s_count, 4)

    actions = ['330']
    func.pth_selector(actions=actions)


def _178():
    func.dub_play('178', 'adam')

    actions = ['15']
    func.pth_selector(actions=actions)


def _179():
    actions = ['373']
    func.pth_selector(actions=actions)


def _180():
    if ent.room_364.visit_count <= 2:
        func.dub_play('180', 'adam')

        cnst.main_eq.append('key;45')

        func.eq_change("klucz z liczbą '45'")

    actions = ['120']
    func.pth_selector(actions=actions)


def _181():
    func.dub_play('181', 'adam')
    path_strings = ['Masz linę', 'Nie masz liny']
    actions = ['329', '32']
    func.pth_selector(path_strings, actions)


def _182():
    func.dub_play('182', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['30', '259']
    func.pth_selector(path_strings, actions)


def _183():
    func.dub_play('183', 'adam')
    _xx()


def _184():
    func.dub_play('184', 'adam')
    # initiate combat with entity_184
    func.combat_main(ent.entity_184, True, ent.entity_184.esc_possible, '385', '226', '234')


def _185():
    func.dub_play('185', 'dreszcz_p_185.mp3')

    actions = ['252']
    func.pth_selector(actions=actions)


def _186():
    func.dub_play('186', 'adam')
    path_strings = ['A', 'B', 'C']
    actions = ['368', '117', '360']
    func.pth_selector(path_strings, actions)


def _187():
    func.dub_play('187', 'adam')
    _xx()


def _188():
    func.dub_play('188', 'adam')
    _xx()


def _189():
    func.dub_play('189', 'adam')
    _xx()


def _190():
    func.dub_play('190', 'adam')

    actions = ['115']
    func.pth_selector(actions=actions)


def _191():
    func.dub_play('191', 'adam')
    _xx()


def _192():
    func.dub_play('192', 'adam')
    path_strings = ['Wybierasz wodę', 'Wybierz przedmiot']
    actions = ['306', '220']
    func.pth_selector(path_strings, actions)
    # Żeby nabrać wody musisz mieć naczynie.
    # Jeśli masz, ale jest pełne, zastanów się:
    # może warto wylać jego zawartość.


def _193():
    func.dub_play('193', 'adam')
    _xx()


def _194():
    func.dub_play('194', 'adam')
    _xx()


def _195():
    func.dub_play('195', 'adam')
    _xx()


def _196():
    func.dub_play('196', 'adam')
    _xx()


def _197():
    func.dub_play('197', 'adam')
    _xx()


def _198():
    func.dub_play('198', 'adam')
    _xx()


def _199():
    func.dub_play('199', 'adam')
    _xx()


def _200():
    func.dub_play('200', 'adam')

    actions = ['120', '301']
    func.pth_selector(actions=actions, visit_check=True, room_id=ent.room_364)


def _201():
    func.dub_play('201', 'adam')
    _xx()


def _202():
    func.dub_play('202', 'adam')
    _xx()


def _203():
    func.dub_play('203', 'adam')
    _xx()


def _204():
    func.dub_play('204', 'adam')
    _xx()


def _205():
    func.dub_play('205', 'adam')
    _xx()


def _206():
    func.dub_play('206', 'adam')
    _xx()


def _207():
    func.dub_play('207', 'adam')
    _xx()


def _208():
    func.dub_play('208', 'adam')
    _xx()


def _209():
    func.dub_play('209', 'adam')
    _xx()


def _210():
    func.dub_play('210', 'adam')
    _xx()


def _211():
    func.dub_play('211', 'adam')
    _xx()


def _212():
    func.dub_play('212', 'adam')
    path_strings = ['zachód', 'północ', 'wschód', 'połódnie']
    actions = ['287', '38', '82', '336']
    func.pth_selector(path_strings, actions)


def _213():
    func.dub_play('213', 'adam')
    _xx()


def _214():
    func.dub_play('214', 'adam')
    _xx()


def _215():
    func.dub_play('215', 'adam')
    _xx()


def _216():
    func.dub_play('216', 'adam')
    _xx()


def _217():
    func.dub_play('217', 'adam')
    _xx()


def _218():
    func.dub_play('218', 'adam')
    _xx()


def _219():
    func.dub_play('219', 'adam')
    _xx()


def _220():
    func.dub_play('220', 'adam')
    _xx()


def _221():
    func.dub_play('221', 'adam')
    _xx()


def _222():
    func.dub_play('222', 'adam')
    _xx()


def _223():
    func.dub_play('223', 'adam')
    _xx()


def _224():
    func.dub_play('224', 'adam')

    actions = ['180', '301']
    func.pth_selector(actions=actions, visit_check=True, room_id=ent.room_364)


def _225():
    func.dub_play('225', 'adam')
    _xx()


def _226():
    func.dub_play('226', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['101', '385']
    func.pth_selector(path_strings, actions)


def _227():
    func.dub_play('227', 'adam')
    _xx()


def _228():
    func.dub_play('228', 'adam')

    actions = ['102']
    func.pth_selector(actions=actions)


def _229():
    func.dub_play('229', 'adam')
    _xx()


def _230():
    func.dub_play('230', 'adam')
    _xx()


def _231():
    func.dub_play('231', 'adam')
    _xx()


def _232():
    func.update_variable(cnst.choice_count, 1)
    if cnst.choice_count < 3:
        _271()
    else:
        _68()


def _233():
    func.dub_play('233', 'adam')
    _xx()


def _234():
    func.dub_play('234', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['205', '199']
    func.pth_selector(path_strings, actions)


def _235():
    func.dub_play('235', 'adam')
    _xx()


def _236():
    func.dub_play('236', 'adam')
    _xx()


def _237():
    func.dub_play('237', 'adam')
    _xx()


def _238a():
    func.dub_play('238a', 'adam')
    func.combat_main(ent.entity_238_1, ent.entity_238_1.state, ent.entity_238_1.esc_possible,
                     '316', '238b', 'xx')


def _238b():
    func.combat_main(ent.entity_238_2, ent.entity_238_2.state, ent.entity_238_2.esc_possible,
                     '316', '238c', 'xx')


def _238c():
    func.combat_main(ent.entity_238_3, ent.entity_238_3.state, ent.entity_238_3.esc_possible,
                     '316', '238d', 'xx')


def _238d():
    func.combat_main(ent.entity_238_4, ent.entity_238_4.state, ent.entity_238_4.esc_possible,
                     '316', '238e', 'xx')


def _238e():
    func.combat_main(ent.entity_238_5, ent.entity_238_5.state, ent.entity_238_5.esc_possible,
                     '316', 'xx', 'xx')


def _239():
    func.dub_play('239', 'adam')
    _xx()


def _240():
    func.dub_play('240', 'adam')
    _xx()


def _241():
    func.dub_play('241', 'adam')

    actions = ['132']
    func.pth_selector(actions=actions)


def _242():
    func.dub_play('242', 'adam')
    _xx()


def _243():
    func.dub_play('243', 'adam')
    _xx()


def _244():
    func.dub_play('244', 'adam')
    _xx()


def _245():
    func.dub_play('245', 'adam')
    _xx()


def _246():
    func.dub_play('246', 'adam')
    _xx()


def _247():
    func.dub_play('247', 'adam')
    _xx()


def _248():
    func.dub_play('248', 'adam')
    _xx()


def _249():
    func.dub_play('249', 'adam')
    _xx()


def _250():
    func.dub_play('250', 'adam')
    _xx()


def _251():
    func.get_music('main', 1500)  # loading background music

    func.dub_play('251', 'adam')

    actions = ['39']
    func.pth_selector(actions=actions)


def _252():
    func.dub_play('252', 'adam')
    _xx()


def _253():
    func.dub_play('253', 'adam')
    _xx()


def _254():
    func.dub_play('254', 'adam')
    _xx()


def _255():
    func.dub_play('255', 'adam')
    _xx()


def _256():
    func.dub_play('256', 'adam')

    actions = ['378']
    func.pth_selector(actions=actions)


def _257():
    func.dub_play('257', 'adam')
    _xx()


def _258():
    func.dub_play('258', 'adam')
    _xx()


def _259():
    func.dub_play('259', 'adam')
    _xx()


def _260():
    func.dub_play('260', 'adam')
    _xx()


def _261():
    func.dub_play('261', 'adam')
    _xx()


def _262():
    func.dub_play('262', 'adam')
    _xx()


def _263():
    func.dub_play('263', 'adam')
    _xx()


def _264():
    func.dub_play('264', 'adam')

    actions = ['102']
    func.pth_selector(actions=actions)


def _265():
    func.dub_play('265', 'adam')
    _xx()


def _266():
    func.dub_play('266', 'adam')
    _xx()


def _267():
    func.dub_play('267', 'adam')
    _xx()


def _268():
    func.dub_play('268', 'adam')
    path_strings = ["Jeśli jeszcze za nimi nie byłeś, możesz wejść.", "Wolisz zawrócić"]
    actions = ['317a', '102']
    func.pth_selector(path_strings, actions)


def _269():
    func.dub_play('269', 'adam')
    func.stats_change('Wytrzymałosć', cnst.w_count, -2)

    # Check conditions
    cond1 = func.get_state(10, cnst.gold_amount)
    print(cond1, cnst.gold_amount)
    cond2 = func.get_state(18, cnst.w_count)
    print(cond2, cnst.w_count)
    cond3 = func.get_state(9, cnst.z_count)
    print(cond3, cnst.z_count)

    # Set default values
    path_strings = ["Podejdź do mostu", 'Ponów próbę z liną']
    actions = ['10', '358']

    # Update values based on conditions
    if cond1:
        path_strings[0:1] = ["Zapłać według taryfy (10 sztuk złota)", "Podejdź do mostu"]
        actions[0:1] = ['35', '10']
        if cond2 and cond3:
            path_strings[2:3] = ["Spróbuj przeskoczyć przez rozpadlinę", 'Ponów próbę z liną']
            actions[2:3] = ['110', '358']
        else:
            path_strings[2:3] = ['Ponów próbę z liną']
            actions[2:3] = ['358']
    else:
        path_strings = ["Podejdź do mostu", 'Ponów próbę z liną']
        actions = ['10', '358']

    func.pth_selector(path_strings, actions)


def _270():
    func.dub_play('270', 'adam')
    _xx()


def _271():
    func.dub_play('271a', 'adam')
    func.stats_change('Wytrzymałosć', cnst.w_count, -1)
    func.dub_play('271b', 'dreszcz_p_271b.mp3')

    path_strings = ['wymień', 'nie wymieniaj']
    actions = ['190', '153']
    func.pth_selector(path_strings, actions)


def _272():
    func.dub_play('272', 'adam')
    _xx()


def _273():
    func.dub_play('273', 'adam')
    _xx()


def _274():
    func.dub_play('274', 'adam')
    _xx()


def _275():
    func.dub_play('275', 'adam')
    _xx()


def _276():
    func.dub_play('276', 'adam')
    _xx()


def _277():
    func.dub_play('277', 'adam')
    _xx()


def _278():
    func.dub_play('278', 'adam')
    _xx()


def _279():
    func.dub_play('279', 'adam')
    _xx()


def _280():
    func.dub_play('280', 'adam')
    _xx()


def _281():
    func.dub_play('281', 'adam')
    _xx()


def _282():
    func.dub_play('282', 'adam')
    _xx()


def _283():
    func.dub_play('283', 'adam')
    _xx()


def _284():
    func.dub_play('284', 'adam')

    if not func.check_for_luck():
        func.stats_change('Wytrzymałość', cnst.w_count, -2)

    actions = ['50']
    func.pth_selector(actions=actions)


def _285():
    func.dub_play('285', 'adam')
    _xx()


def _286():
    func.dub_play('286', 'adam')
    _xx()


def _287():
    func.dub_play('287', 'adam')
    _xx()


def _288():
    func.dub_play('288', 'adam')
    _xx()


def _289():
    func.dub_play('289', 'adam')
    _xx()


def _290():
    func.dub_play('290', 'adam')
    _xx()


def _291():
    func.dub_play('291', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -2)

    actions = ['330']
    func.pth_selector(actions=actions)


def _292():
    func.dub_play('292', 'adam')
    _xx()


def _293():
    func.dub_play('293', 'adam')
    _xx()


def _294():
    func.dub_play('294', 'adam')
    _xx()


def _295():
    func.dub_play('295', 'adam')
    _xx()


def _296():
    func.dub_play('296a', 'dunmer')
    func.eatables()
    func.dub_play('296b', 'dunmer')

    actions = ['39']
    func.pth_selector(actions=actions)


def _297():
    func.dub_play('297', 'adam')
    _xx()


def _298():
    func.update_variable(cnst.choice_count, 1)
    if cnst.choice_count < 3:
        _115()
    else:
        _68()


def _299():
    func.dub_play('299', 'adam')
    _xx()


def _300():
    func.dub_play('300', 'adam')
    _xx()


def _301():
    func.dub_play('301', 'adam')
    path_strings = ['Spróbuj otworzyć drzwi', 'Zawróć']
    actions = ['364', '120']
    func.pth_selector(path_strings, actions)


def _302():
    func.dub_play('302', 'adam')
    _xx()


def _303():
    func.dub_play('303', 'adam')
    _xx()


def _304():
    func.dub_play('304', 'adam')
    _xx()


def _305():
    func.dub_play('305', 'adam')
    path_strings = ['zdaj się na los', 'sprawdź czy masz szczęście']
    actions = ['112', '381']
    func.pth_selector(path_strings, actions)


def _306():
    func.dub_play('306', 'adam')
    _xx()


def _307():
    func.dub_play('307', 'adam')
    _xx()


def _308():
    func.dub_play('308', 'adam')
    _xx()


def _309():
    func.dub_play('309', 'adam')
    _xx()


def _310():
    func.dub_play('310', 'adam')

    actions = ['67', '17']
    func.pth_selector(actions=actions, visit_check=True, room_id=ent.room_310)


def _311():
    func.dub_play('311', 'adam')
    _xx()


def _312():
    func.dub_play('312', 'adam')
    _xx()


def _313():
    func.dub_play('313', 'adam')
    _xx()


def _314():
    func.dub_play('314', 'adam')
    _xx()


def _315():
    func.dub_play('315', 'adam')
    _xx()


def _316():
    func.dub_play('316', 'adam')

    actions = ['176']
    func.pth_selector(actions=actions)


def _317a():
    func.dub_play('317a', 'adam')
    func.combat_main(ent.entity_317, ent.entity_317.state, ent.entity_317.esc_possible, '', '',
                     '317b')


def _317b():
    func.dub_play('317b', 'adam')
    path_strings = ['Rozejrzyj się chociaż po ścianch', 'Nie brzydzę się']
    actions = ['119', '31']
    func.pth_selector(path_strings, actions)


def _318():
    func.dub_play('318', 'adam')
    _xx()


def _319():
    func.dub_play('319', 'adam')
    _xx()


def _320():
    func.dub_play('320', 'adam')
    _xx()


def _321():
    func.dub_play('321', 'adam')
    _xx()


def _322():
    func.dub_play('322', 'adam')
    _xx()


def _323():
    func.dub_play('323', 'adam')
    _xx()


def _324():
    func.update_variable(cnst.choice_count, 1)
    if cnst.choice_count < 3:
        _115()
    else:
        _68()


def _325():
    func.dub_play('325', 'adam')
    _xx()


def _326():
    func.dub_play('326', 'adam')
    _xx()


def _327():
    func.dub_play('327', 'adam')
    _xx()


def _328():
    func.dub_play('328', 'adam')
    _xx()


def _329():
    func.dub_play('329', 'adam')
    _xx()


def _330():
    func.dub_play('330', 'adam')

    actions = ['170']
    func.pth_selector(actions=actions)


def _331():
    func.dub_play('331', 'adam')

    actions = ['59', '11']
    func.pth_selector(actions=actions, visit_check=True, room_id=ent.room_331)


def _332():
    func.dub_play('332a', 'adam')
    func.stats_change('Wytrzymałość', cnst.w_count, -2)
    func.dub_play('332b', 'adam')
    func.combat_main(ent.entity_332, True, ent.entity_332.esc_possible, '', '', '06a')


def _333():
    func.dub_play('333', 'adam')
    _xx()


def _334():
    func.dub_play('334', 'adam')
    _xx()


def _335():
    func.dub_play('335', 'adam')
    _xx()


def _336():
    func.dub_play('336', 'adam')

    actions = ['06b', '21']
    func.pth_selector(actions=actions, visit_check=True, room_id=ent.room_336)


def _337():
    func.dub_play('337', 'adam')
    _xx()


def _338():
    func.dub_play('338', 'adam')
    _xx()


def _339():
    func.dub_play('339', 'adam')
    _xx()


def _340():
    func.dub_play('340', 'adam')
    _xx()


def _341():
    func.dub_play('341', 'adam')
    _xx()


def _342():
    func.dub_play('342', 'adam')
    _xx()


def _343():
    func.dub_play('343', 'adam')
    _xx()


def _344():
    func.dub_play('344', 'adam')
    func.combat_main(ent.entity_344, True, ent.entity_344.esc_possible, '', '', '23')


def _345():
    func.dub_play('345', 'adam')
    path_strings = ['zachód', 'północ']
    actions = ['218', '267']
    func.pth_selector(path_strings, actions)


def _346():
    func.dub_play('346', 'adam')
    _xx()


def _347():
    func.dub_play('347', 'adam')
    _xx()


def _348():
    func.dub_play('348', 'adam')
    _xx()


def _349():
    func.dub_play('349', 'adam')
    path_strings = ['tak', 'nie']
    actions = ['385', '48']
    func.pth_selector(path_strings, actions)


def _350():
    func.dub_play('350', 'adam')
    _xx()


def _351():
    func.dub_play('351', 'adam')

    actions = ['64']
    func.pth_selector(actions=actions)


def _352():
    func.dub_play('352', 'adam')
    _xx()


def _353():
    func.dub_play('353', 'adam')
    _xx()


def _354():
    func.dub_play('354', 'adam')
    _xx()


def _355():
    func.dub_play('355', 'adam')
    _xx()


def _356():
    func.dub_play('356', 'adam')
    _xx()


def _357():
    func.dub_play('357', 'adam')
    _xx()


def _358():
    func.dub_play('358', 'adam')
    _xx()


def _359():
    func.dub_play('359', 'adam')
    _xx()


def _360():
    func.dub_play('360', 'adam')
    _xx()


def _361():
    func.dub_play('361', 'adam')
    _xx()


def _362():
    func.dub_play('362', 'adam')
    _xx()


def _363():
    func.dub_play('363', 'adam')
    _xx()


def _364():
    # change door state to "open"
    ent.room_364.room_state = func.update_variable(ent.room_364.room_state, True)

    func.dub_play('364', 'adam')
    path_strings = ['Próbujesz zabrać ukradkiem pudełko', 'Decydujesz się podjąć walkę']
    actions = ['29', '116a']
    func.pth_selector(path_strings, actions, True, ent.room_364)


def _365():
    func.dub_play('365', 'adam')
    _xx()


def _366():
    func.dub_play('366', 'adam')
    _xx()


def _367():
    func.dub_play('367', 'adam')
    _xx()


def _368():
    func.dub_play('368', 'adam')
    _xx()


def _369():
    func.dub_play('369', 'adam')
    _xx()


def _370():
    func.dub_play('370', 'adam')
    _xx()


def _371():
    func.dub_play('371', 'adam')
    _xx()


def _372():
    func.dub_play('372', 'adam')
    _xx()


def _373():
    func.dub_play('373', 'adam')
    _xx()


def _374():
    func.dub_play('374', 'adam')
    func.eatables()

    actions = ['178']
    func.pth_selector(actions=actions)


def _375():
    func.dub_play('375', 'adam')
    _xx()


def _376():
    func.dub_play('376', 'adam')
    _xx()


def _377():
    func.dub_play('377', 'adam')
    _xx()


def _378():
    func.dub_play('378', 'adam')
    _xx()


def _379():
    func.dub_play('379', 'adam')
    _xx()


def _380():
    func.dub_play('380', 'adam')
    _xx()


def _381():
    if func.check_for_luck():
        _28()
    else:
        _291()


def _382():
    func.dub_play('382', 'adam')
    _xx()


def _383():
    func.dub_play('383', 'adam')
    _xx()


def _384():
    func.dub_play('384', 'adam')
    _xx()


def _385():
    func.dub_play('385', 'adam')
    path_strings = ['Wybierz drzwi zachodnie', 'Wybierz drzwi wschodnie']
    actions = ['345', '242']
    func.pth_selector(path_strings, actions)
