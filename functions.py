import random, time, pygame, os, subprocess, keyboard
import constants, obj_class, paragraphs
import gamebook as gb
from colorama import Fore


def loading(duration):  # loading 'animation'
    while duration > 0:
        print('.', end='')
        time.sleep(0.3)
        duration -= 1


def debug_message(msg):
    if constants.dev_mode:
        print(f'{constants.debug_txt_clr}DEBUG: {msg}{constants.def_txt_clr}')


def error_message(error_name, msg):
    if constants.dev_mode:
        if error_name == '':
            error_name = 'ERROR'
        print(f'{constants.error_txt_clr}{error_name}{constants.debug_txt_clr} || {msg}{constants.def_txt_clr}')


def clear_terminal():
    if constants.dev_mode:
        debug_message('function clear_terminal() is disabled for debugging purposes')
    else:
        subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)


def dub_play(string_id, audio_file_id, voice=None):
    audio_path = None
    if not voice:  # default 'Dunmer' voice
        audio_path = constants.assets_audio_pth
    elif voice.lower() == 'adam':
        audio_path = constants.assets_audio_pth_adam
    elif voice.lower() == 'fx':
        audio_path = constants.assets_audio_effects_pth

    try:
        current_sound = pygame.mixer.Sound(f'{audio_path}/{audio_file_id}')

    except FileNotFoundError:
        error_message('FileNotFoundError', f'Could not find: {audio_file_id}')
        current_sound = pygame.mixer.Sound(f'{constants.assets_audio_effects_pth}/click_snd.mp3')

    pygame.mixer.stop()
    current_sound.set_volume(constants.def_action_volume)

    # find empty channel
    channel = None
    for i in range(pygame.mixer.get_num_channels()):
        if not pygame.mixer.Channel(i).get_busy():
            channel = pygame.mixer.Channel(i)
            break
    if channel is None:
        debug_message('Could not find empty channel.')
        return

    # play sound on found channel
    channel.play(current_sound)
    if len(string_id) > 0:
        if len(string_id) <= 4:
            gameboook = gb.get_translation(constants.translation)
            print(gameboook[string_id])
        else:
            print(string_id)

    # wait until audio stops playing
    if constants.allow_skip_dub:
        input(f'pomiń {constants.input_sign}')
        pygame.mixer.stop()

    elif constants.skip_dub:
        channel.play(pygame.mixer.Sound(f'{constants.assets_audio_effects_pth}/click_snd.mp3'))
        time.sleep(1)
    else:
        while channel.get_busy():
            continue
    return


def name_randomizer():
    first_parts = ['Bogdan', 'Dobrosław', 'Jarosław', 'Grzesiu', 'Mścisław', 'Radosław', 'Sławomir',
                   'Zbyszko z Bogdańca', 'Władysław', 'Zbigniew', 'Stanisław']
    last_parts = ['z Levygradu', 'Mądry', 'Odważny', 'z Małomorza', 'Prawy', 'Sprawiedliwy', 'Słomka', 'Wielki',
                  'Zacny', 'Zuchwały', 'Pyzdra']

    first_name = random.choice(first_parts)
    last_name = ''
    if first_name == 'Zbyszko z Bogdańca':  # meme for ya (probabbly only poles could understand, sorry)
        audio_file_id = f"{constants.assets_audio_effects_pth}/zbych.mp3"
        try:
            def_action_volume = constants.def_action_volume
            current_sound = pygame.mixer.Sound(audio_file_id)
            current_sound.set_volume(def_action_volume)
            channel = pygame.mixer.find_channel()
            if channel is None:
                debug_message('Could not find empty channel.')
                return
            channel.play(current_sound)
        except FileNotFoundError:
            print(f'{Fore.LIGHTRED_EX}FileNotFoundError{constants.def_txt_clr} || Could not find: {audio_file_id}')
            return
        time.sleep(2.7)
        clear_terminal()
        print(constants.and_his_name_is)
        time.sleep(5.6)
    else:
        last_name = random.choice(last_parts)
    player_name = f'{Fore.LIGHTYELLOW_EX}{first_name} {last_name}{constants.def_txt_clr}'
    print(player_name)
    time.sleep(1)
    constants.player_name = player_name
    return constants.player_name


def update_bool_variable(variable, change):
    variable = change
    return variable


def update_num_variable(variable, change):
    variable += change
    return variable


def rpar():
    constants.z_init = constants.z_count = random.randint(1, 6) + 6
    constants.w_init = constants.w_count = random.randint(2, 12) + 12
    constants.s_init = constants.s_count = random.randint(1, 6) + 6
    return constants.z_init, constants.z_count, constants.w_init, constants.w_count, constants.s_init, constants.s_count


def pth_selector(path_strings=[], actions=[], visit_check=False, room_id=0):
    if room_id != 0:  # add visit count if room number was given
        room_id.visit_count = update_num_variable(room_id.visit_count, 1)
        debug_message(f'added visit: visit count of room number {room_id.room_num} = {room_id.visit_count}')

    if not visit_check:
        debug_message(f'actions: {actions}')

        if len(actions) != 1:  # if there is more than one path, display choice menu

            for i, path in enumerate(path_strings):
                print(f'{i + 1} · {path}')
                time.sleep(constants.delay)

            while True:
                odp = input(f'{constants.input_sign}')

                try:
                    odp = int(odp)

                    if odp == 0:
                        print(f'/!/ {constants.special_txt_clr}Wybór nie może być równy zeru.{constants.def_txt_clr}')
                    elif odp < 0:
                        print(f'/!/ {constants.special_txt_clr}Wybór nie może być ujemny.{constants.def_txt_clr}')
                    elif odp > len(path_strings):
                        print(f'/!/ {constants.special_txt_clr}Nie ma wyboru o numerze: {odp}{constants.def_txt_clr}')
                    elif odp == '':
                        print(f'/!/ {constants.special_txt_clr}Nie wpisano numeru: {odp}{constants.def_txt_clr}')
                    else:
                        break

                except ValueError:
                    print(f'/!/ {constants.special_txt_clr}Wybierz numer z listy.{constants.def_txt_clr}')

            clear_terminal()
            pygame.mixer.stop()  # abort any dubbing currently playing
            eval(actions[odp - 1])

        else:  # if there is only one path, continue automatically
            clear_terminal()
            odp = 1
            eval(actions[odp - 1])

    else:
        if room_id.room_state:  # if open

            dub_play(
                f'Drzwi {constants.special_txt_clr}{room_id.room_num}{constants.def_txt_clr} są {constants.special_txt_clr}otwarte{constants.def_txt_clr}.',
                'infobook_adam_door_open.mp3', 'adam')

            if not room_id.visit_count - 1 >= room_id.max_visit_count:  # Player is visiting the room more times than the allowed number.
                if room_id.visit_count == 1:  # Player first time in room
                    debug_message(f'eval: {actions[1]}')
                    eval(actions[1])

                elif room_id.visit_count >= 2:  # Player has already visited the room before, but did not exceed the allowed number of visits.
                    debug_message(f'eval: {actions[0]}')
                    eval(actions[0])

            else:
                print('Nie masz tu czego szukać')

        else:  # if close
            dub_play(
                f'Drzwi {constants.special_txt_clr}{room_id.room_num}{constants.def_txt_clr} są {constants.special_txt_clr}zamknięte{constants.def_txt_clr}.',
                'infobook_adam_door_closed.mp3', 'adam')
            debug_message(f'eval: {actions[1]}')
            eval(actions[1])


# /// mechaniki
def kill():
    pygame.mixer.music.fadeout(1200)
    input("Koniec gry")
    exit()


def win():
    pygame.mixer.music.fadeout(1200)
    input("GRATULACJE, WYGRAŁEŚ!!!")
    exit()


def check_for_luck():
    print(f'{constants.special_txt_clr}Sprawdzam czy masz szczęście:')
    loading(2)
    cfl_val = random.randint(2, 12)

    if cfl_val <= constants.s_count:
        print('\rUff, masz szczęscie.\
        \n')
        constants.p_luck = True
    elif cfl_val > constants.s_count:
        print('\rNie masz szczęścia!\
        \n')
        constants.p_luck = False

    constants.s_count -= 1
    time.sleep(1)

    return constants.p_luck, constants.s_count


def check_for_gold_amount(true_path, false_path, req_amount):
    if constants.gold_amount >= req_amount:
        eval(true_path)
    else:
        print('Nie masz wystarczającej ilości złota.')
        eval(false_path)


def eatables():
    if constants.eatables_count != 0:
        if constants.w_count != constants.w_init:
            dub_play(f'{constants.special_txt_clr}Czy chcesz zjeśc prowiant? (+4 Wytrzymałość) (tak/nie)',
                     f'{constants.assets_audio_pth}/eatables.mp3')
            print(f"/// Wytrzymałość: {constants.w_count}/{constants.w_init}")
            print(f"/// Prowiant: {constants.eatables_count}/{constants.init_eatables_count}")
            odp = input(f"{constants.input_sign}\
            \n")
            if odp.lower() in {'tak', 't', 'y', 'yes'}:
                if constants.w_count < constants.w_init:
                    constants.eatables_count += -1
                    if constants.eatables_count >= 0:
                        if constants.w_count == constants.w_init - 1:
                            # + 1
                            print(f"Wytrzymałość + {constants.eatable_W_load - 3}")
                            constants.w_count += constants.eatable_W_load - 3
                        elif constants.w_count == constants.w_init - 2:
                            # + 2
                            print(f"Wytrzymałość + {constants.eatable_W_load - 2}")
                            constants.w_count += constants.eatable_W_load - 2
                        elif constants.w_count == constants.w_init - 3:
                            # + 3
                            print(f"Wytrzymałość + {constants.eatable_W_load - 1}")
                            constants.w_count += constants.eatable_W_load - 1
                        else:
                            # + 4
                            print(f"Wytrzymałość + {constants.eatable_W_load}")
                            constants.w_count += constants.eatable_W_load
                        print(f"/// Wytrzymałość: {constants.w_count}/{constants.w_init}")
                        time.sleep(constants.delay)
                        print(
                            f"/// Prowiant: {constants.eatables_count}/{constants.init_eatables_count}{constants.def_txt_clr}")
                        time.sleep(constants.delay)
                        print(f"{constants.def_txt_clr}")

            elif odp.lower() in {'nie', 'n', 'no'}:
                print("Zostawiasz prowiant na później")
                time.sleep(constants.delay)
                print(f"{constants.def_txt_clr}")
            else:
                print("Wpisz tak/nie")
                time.sleep(constants.delay)
                eatables()

            return constants.w_count, constants.eatables_count


def show_equipment_list():
    for i in constants.main_eq:
        print(f'- {i}')
    input(f"{constants.input_sign} ")
    time.sleep(constants.delay)


def eq_change(new_item_name):
    input(f"/// {constants.special_txt_clr}Zdobyto nowy przedmiot: {new_item_name}{constants.def_txt_clr}\
    \n{constants.input_sign}")


def show_player_stats():
    print(f'\
    \n{constants.def_txt_clr}Statystyki {Fore.LIGHTYELLOW_EX}{constants.player_name}{constants.combat_txt_clr}:\
        \nWytrzymałość: {constants.w_count}/{constants.w_init}\
        \nZręczność: {constants.z_count}/{constants.z_init}\
        \nSzczęście: {constants.s_count}/{constants.s_init}{constants.def_txt_clr}')
    time.sleep(constants.delay)


def show_entity_stats(entity):
    print(f'\
        \nStatystyki {entity.name}{constants.combat_txt_clr}:\
        \nWytrzymałość: {entity.entity_w_count}/{entity.entity_w_init}\
        \nZręczność: {entity.entity_z_count}/{entity.entity_z_init}')
    time.sleep(2 * constants.delay)


def stats_change(attribute_name, updated_variable, amount):
    updated_variable += amount

    if amount < 0:
        inter = ''
    else:
        inter = '+'

    # because of non compatibility with source material, this block is disabled for now
    #
    # if variable == constants.s_count:
    #     if constants.s_count == constants.s_init:
    #         constants.s_count += 1
    #     elif constants.s_count < constants.s_init + 1:
    #         new_count = min(constants.s_count + amount, constants.s_init + 1)
    #         constants.s_count = new_count

    print(f'{constants.special_txt_clr}/// {attribute_name} {inter}{amount} >>> {updated_variable + amount}{constants.def_txt_clr}')
    time.sleep(constants.delay)

    return updated_variable


# - - - - - - - - -
# /// COMBAT
# - - - - - - - - -
def combat_init(entity, state, esc_possible, escape_id, stay_id, win_path_id):
    pygame.mixer.music.fadeout(1500)

    rnd_choice = random.choice(constants.music_combat)  # randomize music from list
    pygame.mixer.music.load(rnd_choice)
    pygame.mixer.music.set_volume(constants.def_bckg_volume)
    pygame.mixer.music.play(-1)

    constants.round_count = 0
    win_path = win_path_id
    p_w_count = constants.w_count
    e_w_count = entity.entity_w_count
    to_the_end = False

    show_player_stats()
    show_entity_stats(entity)

    input(f'\
    \n{constants.combat_txt_clr}Rozpocznij walkę! {constants.input_sign}')
    combat_main(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path)


def combat_main(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path):
    if e_w_count <= 0:  # if enemy dead
        pygame.mixer.music.fadeout(1500)
        rnd_choice = random.choice(constants.music_main)  # randomize music from list
        pygame.mixer.music.load(rnd_choice)
        pygame.mixer.music.set_volume(constants.def_bckg_volume)
        pygame.mixer.music.play(-1)

        state = False

        # obj_class.Entity.die(pygame.mixer.Sound(f'{constants.assets_audio_pth}/placeholder.mp3'))

        dub_play(f'\
        \n{constants.combat_txt_clr}Pokonałeś {Fore.LIGHTRED_EX}{entity.name}{constants.combat_txt_clr}!\
        \n', 'audiobook_adam_combat_true.mp3', 'adam')

        time.sleep(constants.delay)
        show_player_stats()
        clear_terminal()

        if esc_possible:

            # /// choice of escape or not
            ecape_opt = "{0}{1}".format(escape_id, (
                "entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count)"))
            stay_opt = "{0}{1}".format(stay_id, (
                "entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path)"))

            print(
                f"{constants.def_txt_clr}Uciekasz czy zostajesz i walczczysz dalej? {constants.special_txt_clr}/Wytrzymałość - 2/{constants.def_txt_clr}:\
                  \nuciekasz        = <enter>\
                  \nwalczysz dalej  = wpisz cokolwiek")

            odp = input(f"tak/nie {constants.input_sign} \
            \n")
            if len(odp) == 0:
                print(
                    f"{constants.special_txt_clr}Wytrzymałość: {constants.w_count} {constants.input_sign} {constants.w_count - 2}{constants.def_txt_clr}\
                \n")
                constants.w_count -= 2
                eval(ecape_opt)
            elif len(odp) > 0:
                eval(stay_opt)

        else:
            eval(win_path)

    elif p_w_count <= 0:  # if player dead
        print()
        dub_play(f'Zostałeś zabity przez {Fore.LIGHTRED_EX}{entity.name}{constants.combat_txt_clr}!\
        \n', 'combat_die.wav')
        kill()

    else:  # if both player and enemy are alive
        combat_round(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path)

    return state, constants.w_count, constants.count


def combat_round(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path):
    constants.round_count += 1
    print(f'\
    \n{constants.combat_txt_clr}Runda: {constants.round_count}{constants.combat_txt_clr}')
    p_w_count = constants.w_count
    e_w_count = entity.entity_w_count

    if constants.automatic_battle:
        a = random.randint(2, 12) + entity.entity_z_count * constants.e_mult_choice
        b = random.randint(2, 12) + constants.z_count
    else:
        a = input(f"Podaj wartość 'a' rzucając dwiema kośćmi{constants.input_sign}")
        b = input(f"Podaj wartość 'b' rzucając dwiema kośćmi{constants.input_sign}")

    if state:
        loading(1)
        if a > b:  # if enemy won

            if constants.w_count > 0:
                if e_w_count <= 0:
                    state = False
                    combat_main(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count,
                                win_path)
                constants.w_count += constants.e_hit_val_
                print(f"{Fore.LIGHTRED_EX}{entity.name}{constants.combat_txt_clr} zadał cios!\
                \n{constants.special_txt_clr}/// Wytrzymałość {Fore.LIGHTYELLOW_EX}{constants.player_name}{constants.special_txt_clr}: {constants.w_count}/{constants.w_init}")
                dub_play('', 'audiobook_adam_round_false.mp3', 'adam')

                constants.w_count = max(constants.w_count, 0)

        elif a < b:  # if player won

            if entity.entity_w_count > 0:
                entity.entity_w_count += constants.p_hit_val_
                print(f"{Fore.LIGHTYELLOW_EX}{constants.player_name}{constants.combat_txt_clr} zadał cios!\
                \n{constants.special_txt_clr}/// Wytrzymałość {Fore.LIGHTRED_EX}{entity.name}{constants.special_txt_clr}: {entity.entity_w_count}/{entity.entity_w_init}")
                dub_play('', 'audiobook_adam_round_true.mp3', 'adam')

                entity.entity_w_count = max(entity.entity_w_count, 0)

        else:  # if remis
            print(f'{constants.special_txt_clr}Remis!')
            dub_play('', 'audiobook_adam_round_none.mp3', 'adam')

        if constants.allow_skip_dub:  # If the option to skip the dubbing is enabled
            time.sleep(2 * constants.delay)

    combat_main(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path)
