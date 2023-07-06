import random
import time
import pygame
import os
import subprocess
import json
import datetime
import constants
import gamebook as gb
import constants as cnst
# paragraphs must be imported
import paragraphs as prg
from colorama import Fore


def debug_message(msg):
    if cnst.dev_mode:
        print(f'{cnst.debug_txt_clr}DEBUG: {msg}{cnst.def_txt_clr}')


def error_message(error_name, msg):
    if cnst.dev_mode:
        if error_name == '':
            error_name = 'ERROR'
        print(f'{cnst.error_txt_clr}{error_name}{cnst.debug_txt_clr} || {msg}{cnst.def_txt_clr}')


def clear_terminal():
    if cnst.dev_mode:
        debug_message('if dev_mode; clear_terminal() is disabled')
    else:
        subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)


def loading(duration, message=None):
    animation_signs = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    sign_index = 0

    if message:
        print(message, end='')  # Display message if one is given

    print(Fore.YELLOW, end='\r')
    while time.time() < end_time:
        print('- ' + animation_signs[sign_index % len(animation_signs)] + ' -', end='\r')
        time.sleep(0.1)
        sign_index += 1
    print(cnst.def_txt_clr)


def update_setup_file():
    with open(cnst.setup_file_path, 'w') as json_file:  # Save the setup data to a JSON file
        json.dump(cnst.setup_data, json_file)
    debug_message('setup.json has been updated')


def get_music(category=None, fadeout=None):
    if constants.get_music:
        if category:
            rnd_choice = None
            if fadeout:
                pygame.mixer.music.fadeout(fadeout)

            if category == 'main':
                rnd_choice = random.choice(cnst.music_main)  # randomizing music from list

            elif category == 'combat':
                rnd_choice = random.choice(cnst.music_combat)

            elif category == 'menu':
                rnd_choice = random.choice(cnst.music_menu)

            else:
                # rnd_choice = random.choice(cnst.music_other) # unused for now
                pass

            if constants.dev_mode:
                debug_message(f'Playing {category}: {rnd_choice}')
            pygame.mixer.music.load(rnd_choice)
            pygame.mixer.music.set_volume(cnst.bckg_volume)
            pygame.mixer.music.play(-1)  # loop
        else:
            if constants.dev_mode:
                debug_message('Playing: None of music was selected')
    else:
        if constants.dev_mode:
            debug_message('if dev_mode; get_music() is disabled')


def dub_play(string_id, voice=None, skippable=True):
    # building file path based on voice, translation and string_id
    audio_path = None
    if voice.lower() == 'adam':
        audio_path = f'{cnst.assets_audio_pth}/Adam'
    elif voice.lower() == 'xxx':  # placeholder for future use
        audio_path = f'{cnst.assets_audio_pth}/xxx'
    elif voice.lower() == 'fx':
        audio_path = cnst.assets_audio_effects_pth

    audio_file_id = f'{audio_path}/{cnst.translation}/audiobook_{voice.lower()}_{cnst.translation}_{string_id}{cnst.audio_ext}'

    try:
        current_sound = pygame.mixer.Sound(audio_file_id)
        debug_message(f'Now playing: {audio_file_id}')

    except FileNotFoundError:
        error_message('FileNotFoundError', f'Could not find: {audio_file_id}')
        current_sound = pygame.mixer.Sound(f'{cnst.assets_audio_effects_pth}/click_snd.mp3')

    pygame.mixer.stop()
    current_sound.set_volume(cnst.action_volume)

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
    try:
        if len(string_id) > 0:
            print(gb.gameboook[cnst.translation][string_id])
    except KeyError:
        channel.play(pygame.mixer.Sound(f'{cnst.assets_audio_effects_pth}/click_snd.mp3'))
        error_message('KeyError', f'Could not find string: {string_id}')

    # wait until audio stops playing
    if skippable:
        if cnst.allow_skip_dub:
            input(f'skip {cnst.input_sign}')
            pygame.mixer.stop()

    elif cnst.auto_skip_dub:
        loading(1, 'skipping...')

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
        audio_file_id = f"{cnst.assets_audio_effects_pth}/zbych.mp3"
        try:
            current_sound = pygame.mixer.Sound(audio_file_id)
            current_sound.set_volume(cnst.action_volume)
            channel = pygame.mixer.find_channel()
            if channel is None:
                debug_message('Could not find empty channel.')
                return
            channel.play(current_sound)
        except FileNotFoundError:
            print(f'{Fore.LIGHTRED_EX}FileNotFoundError{cnst.def_txt_clr} || Could not find: {audio_file_id}')
            return
        # zbyszko z bogdańca easteregg
        time.sleep(2.7)
        clear_terminal()
        print(cnst.and_his_name_is)
        time.sleep(5.6)
    else:
        last_name = random.choice(last_parts)
    player_name = f'{Fore.LIGHTYELLOW_EX}{first_name} {last_name}{cnst.def_txt_clr}'
    print(player_name)
    time.sleep(1)
    cnst.player_name = player_name
    return cnst.player_name


def update_bool_variable(variable, change):
    variable = change
    return variable


def update_num_variable(variable, change):
    variable += change
    return variable


def get_player_par():
    cnst.z_init = cnst.z_count = random.randint(1, 6) + 6
    cnst.w_init = cnst.w_count = random.randint(2, 12) + 12
    cnst.s_init = cnst.s_count = random.randint(1, 6) + 6
    return cnst.z_init, cnst.z_count, cnst.w_init, cnst.w_count, cnst.s_init, cnst.s_count


def get_game_state(action, last_paragraph='prg.00a', new_game=None):
    folder_path = os.path.join(os.path.expanduser("~/Documents"), cnst.game_state_dir_name)
    # folder path for saving json file

    json_files = []
    # list of json files in folder_path

    if os.path.exists(folder_path):  # check if .json file exist
        game_states = os.listdir(folder_path)
        json_files = [file for file in game_states if file.endswith(".json")]

    else:  # create dir if it doesn't exists
        os.makedirs(folder_path)
        debug_message(f'Folder {folder_path} created')

    if action == 's':
        if new_game:
            # Create new file path and update active gameplay file_path
            cnst.active_gameplay = os.path.join(folder_path, f"dreszcz_{datetime.datetime.now().strftime('%y-%m-%d_%S')}.json")
            print(cnst.active_gameplay)

        # Save game state to variable
        game_state = {
            "last_paragraph": last_paragraph,
            "player_name": cnst.player_name,
            "difficulty": cnst.difficulty,
            "s_count": cnst.s_count,
            "w_count": cnst.w_count,
            "z_count": cnst.z_count,
            "s_init": cnst.s_init,
            "w_init": cnst.w_init,
            "z_init": cnst.z_init,
            "equipment": cnst.main_eq,
            "potion": cnst.potion,
            "count_potion": cnst.count_potion,
            "eatables_count": cnst.eatables_count,
            "gold_amount": cnst.gold_amount
        }

        # Saving game state as json file
        with open(cnst.active_gameplay, "w") as f:
            json.dump(game_state, f)
        debug_message(f'Game saved to: {cnst.active_gameplay}')


    elif action == 'l':

        if len(json_files) > 0:
            print("Saved game states:")  # List of JSON files
            for i, file in enumerate(json_files, start=1):
                print(f"{i}. {file}")

            while True:
                file_number = input(f"\nChoose game state to load\
                \n{cnst.input_sign}")
                try:
                    file_number = int(file_number)

                    if 1 <= file_number <= len(json_files):
                        selected_file = json_files[file_number - 1]
                        cnst.active_gameplay = os.path.join(folder_path, selected_file)
                        with open(cnst.active_gameplay, "r") as f:
                            game_state = json.load(f)
                        debug_message(f'Game state loaded from: {selected_file}')
                        break
                    else:
                        debug_message("Incorrect file number provided.")

                except ValueError:
                    debug_message("Incorrect file number provided.")

            # Assigning the loaded data back to variables.
            last_paragraph = game_state.get("last_paragraph")
            cnst.player_name = game_state.get("player_name")
            cnst.difficulty = game_state.get("difficulty")
            cnst.s_count = game_state.get("s_count")
            cnst.w_count = game_state.get("w_count")
            cnst.z_count = game_state.get("z_count")
            cnst.s_count = game_state.get("s_init")
            cnst.w_count = game_state.get("w_init")
            cnst.z_count = game_state.get("z_init")
            cnst.main_eq = game_state.get("equipment")
            cnst.potion = game_state.get("potion")
            cnst.count_potion = game_state.get("count_potion")
            cnst.eatables_count = game_state.get("eatables_count")
            cnst.gold_amount = game_state.get("gold_amount")

        else:
            debug_message("No saved game states found.")

    elif action == 'c':  # continue
        with open(cnst.active_gameplay, "r") as f:
            game_state = json.load(f)

            debug_message(f'Game state loaded from: {cnst.active_gameplay}')

            # Assigning the loaded data back to variables.
            last_paragraph = game_state.get("last_paragraph")
            cnst.player_name = game_state.get("player_name")
            cnst.difficulty = game_state.get("difficulty")
            cnst.s_count = game_state.get("s_count")
            cnst.w_count = game_state.get("w_count")
            cnst.z_count = game_state.get("z_count")
            cnst.s_count = game_state.get("s_init")
            cnst.w_count = game_state.get("w_init")
            cnst.z_count = game_state.get("z_init")
            cnst.main_eq = game_state.get("equipment")
            cnst.potion = game_state.get("potion")
            cnst.count_potion = game_state.get("count_potion")
            cnst.eatables_count = game_state.get("eatables_count")
            cnst.gold_amount = game_state.get("gold_amount")

    elif action == 'init':  # check if any game states exist
        if len(json_files) > 0:
            cnst.game_state_exists = True

        else:
            cnst.game_state_exists = False

        return cnst.game_state_exists

    return last_paragraph


def pth_selector(path_strings=[], actions=[], visit_check=False, room_id=0):
    if room_id != 0:  # add visit count if room number was given
        room_id.visit_count = update_num_variable(room_id.visit_count, 1)
        debug_message(f'added visit: visit count of room number {room_id.room_num} = {room_id.visit_count}')

    if not visit_check:
        debug_message(f'evaluating action: {actions}')

        if len(actions) != 1:  # if there is more than one path, display choice menu
            for i, path in enumerate(path_strings):
                print(f'{i + 1} · {path}')
                time.sleep(cnst.delay)

            while True:
                odp = input(f'{cnst.input_sign}')

                try:
                    odp = int(odp)

                    if 0 < odp <= len(path_strings):
                        break

                except ValueError:
                    print(f'/!/ {cnst.special_txt_clr}Wybierz numer z listy.{cnst.def_txt_clr}')

            clear_terminal()
            pygame.mixer.stop()  # abort any dubbing currently playing
            get_game_state('s', actions[odp - 1])
            eval(actions[odp - 1])

        else:  # if there is only one path, continue automatically
            clear_terminal()
            odp = 1
            get_game_state('s', actions[odp - 1])
            eval(actions[odp - 1])

    else:
        if room_id.room_state:  # if open
            print(
                f"{gb.gameboook[cnst.translation]['door']} {cnst.special_txt_clr}{room_id.room_num}{cnst.def_txt_clr} {gb.gameboook[cnst.translation]['are']} {cnst.special_txt_clr}{gb.gameboook[cnst.translation]['opened']}{cnst.def_txt_clr}.")
            dub_play('opened', 'adam', False)

            if not room_id.visit_count - 1 >= room_id.max_visit_count:  # Player is visiting the room more times than the allowed number.
                if room_id.visit_count == 1:  # Player first time in room
                    debug_message(f'eval: {actions[1]}')
                    get_game_state('s', actions[1])
                    eval(actions[1])

                elif room_id.visit_count >= 2:  # Player has already visited the room before, but did not exceed the allowed number of visits.
                    debug_message(f'eval: {actions[0]}')
                    get_game_state('s', actions[0])
                    eval(actions[0])

            else:
                print('Nie masz tu czego szukać')

        else:  # if closed
            print(
                f"{gb.gameboook[cnst.translation]['door']} {cnst.special_txt_clr}{room_id.room_num}{cnst.def_txt_clr} {gb.gameboook[cnst.translation]['are']} {cnst.special_txt_clr}{gb.gameboook[cnst.translation]['closed']}{cnst.def_txt_clr}.")
            dub_play('closed', 'adam', False)
            debug_message(f'eval: {actions[1]}')
            eval(actions[1])


def kill():
    pygame.mixer.music.fadeout(1200)
    input("Koniec gry")
    exit()


def win():
    pygame.mixer.music.fadeout(1200)
    input("GRATULACJE, WYGRAŁEŚ!!!")
    exit()


def check_for_luck():
    print(f'{cnst.special_txt_clr}Sprawdzam czy masz szczęście:')
    loading(2)
    cfl_val = random.randint(2, 12)

    if cfl_val <= cnst.s_count:
        print('\rUff, masz szczęscie.\
        \n')
        cnst.p_luck = True
    elif cfl_val > cnst.s_count:
        print('\rNie masz szczęścia!\
        \n')
        cnst.p_luck = False

    cnst.s_count -= 1
    time.sleep(1)

    return cnst.p_luck, cnst.s_count


def check_for_gold_amount(true_path, false_path, req_amount):
    if cnst.gold_amount >= req_amount:
        eval(true_path)
    else:
        print("Nie masz wystarczającej ilości złota.")  # You don't have enough gold.
        eval(false_path)


def eatables():
    if cnst.eatables_count != 0:
        while True:
            if cnst.w_count != cnst.w_init:
                dub_play("eatables", "adam", False)
                print(f"/// Wytrzymałość: {cnst.w_count}/{cnst.w_init}")
                print(f"/// Prowiant: {cnst.eatables_count}/{cnst.init_eatables_count}")
                odp = input(f"{cnst.input_sign}")
                loading(1)
                if odp.lower() in {'tak', 't', 'y', 'yes'}:
                    if cnst.w_count < cnst.w_init:
                        cnst.eatables_count -= 1
                        wzrost_wytrzymalosci = min(cnst.eatable_W_load, cnst.w_init - cnst.w_count)
                        cnst.w_count += wzrost_wytrzymalosci
                        print(f"Wytrzymałość + {wzrost_wytrzymalosci}")
                        print(f"/// Wytrzymałość: {cnst.w_count}/{cnst.w_init}")
                        print(f"/// Prowiant: {cnst.eatables_count}/{cnst.init_eatables_count}{cnst.def_txt_clr}")
                        print(f"{cnst.def_txt_clr}")
                        break

                elif odp.lower() in {'nie', 'n', 'no'}:
                    print("Zostawiasz prowiant na później")
                    print(f"{cnst.def_txt_clr}")
                    break

                else:
                    print("Wpisz tak/nie")

                return cnst.w_count, cnst.eatables_count


def show_equipment_list():
    for i in cnst.main_eq:
        print(f'- {i}')
    input(f"{cnst.input_sign} ")


def eq_change(new_item_name):
    input(f"/// {cnst.special_txt_clr}Zdobyto nowy przedmiot: {new_item_name}{cnst.def_txt_clr}\
    \n{cnst.input_sign}")


def show_player_stats():
    print(f'{cnst.def_txt_clr}\
    \nWytrzymałość: {cnst.w_count}/{cnst.w_init} \
    \nZręczność: {cnst.z_count}/{cnst.z_init} \
    \nSzczęście: {cnst.s_count}/{cnst.s_init}')


def show_entity_stats(entity):
    print(f'{cnst.def_txt_clr}\
    \nStatystyki {entity.name}:\
    \nWytrzymałość: {entity.entity_w_count}/{entity.entity_w_init}\
    \nZręczność: {entity.entity_z_count}/{entity.entity_z_init}')


def stats_change(attribute_name, updated_variable, amount):
    updated_variable += amount / 2  # /2 is temporary fix

    if amount < 0:
        inter = ''
    else:
        inter = '+'

    # because of non compatibility with source material, this block is disabled for now
    #
    # if variable == cnst.s_count:
    #     if cnst.s_count == cnst.s_init:
    #         cnst.s_count += 1
    #     elif cnst.s_count < cnst.s_init + 1:
    #         new_count = min(cnst.s_count + amount, cnst.s_init + 1)
    #         cnst.s_count = new_count

    print(
        f'{cnst.special_txt_clr}/// {attribute_name} {inter}{amount} {constants.input_sign} {updated_variable + amount}{cnst.def_txt_clr}')

    return updated_variable


def use_potion():
    if cnst.count_potion > 0:
        potion_attributes = {
            'w': (cnst.w_count, cnst.w_init),
            'z': (cnst.z_count, cnst.z_init),
            's': (cnst.s_count, cnst.s_init + 1)
        }
        if cnst.potion in potion_attributes:
            attr_name, attr_value = potion_attributes[cnst.potion]
            setattr(cnst, attr_name, attr_value)
        cnst.count_potion -= 1


# - - - - - - - - -
# /// COMBAT
# - - - - - - - - -
def combat_init(entity, state, esc_possible, escape_id, stay_id, win_path_id):
    pygame.mixer.music.fadeout(1500)

    get_music('combat')  # loading background music

    # /// setting up the combat
    cnst.round_count = 0
    win_path = win_path_id
    p_w_count = cnst.w_count
    e_w_count = entity.entity_w_count
    to_the_end = False

    show_player_stats()
    show_entity_stats(entity)

    input(f"\
    \n{cnst.combat_txt_clr}{gb.gameboook[cnst.translation]['combat_init']} {cnst.input_sign}")
    combat_main(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path)


def combat_main(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path):
    if e_w_count <= 0:  # if the enemy is dead
        pygame.mixer.music.fadeout(1500)
        get_music('main')  # load background music for main

        state = False

        print(f"\
        \n{cnst.combat_txt_clr}{gb.gameboook[cnst.translation]['combat_win_info']} {Fore.LIGHTRED_EX}{entity.name}{cnst.combat_txt_clr}!\
        \n")
        dub_play('xxx', 'adam', False)

        show_player_stats()

        if esc_possible:
            # Prompt the player to choose whether to escape or not
            ecape_opt = "{0}{1}".format(escape_id, (
                "entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count)"))
            stay_opt = "{0}{1}".format(stay_id, (
                "entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path)"))

            print(gb.gameboook[cnst.translation]['esc_choice'])

            odp = input(f"Y/N {cnst.input_sign} \
            \n")
            if len(odp) == 0:
                # Reduce player's endurance by 2 and proceed to escape option
                print(
                    f"{cnst.special_txt_clr}Wytrzymałość: {cnst.w_count} {cnst.input_sign} {cnst.w_count - 2}{cnst.def_txt_clr}\
                \n")
                cnst.w_count -= 2
                eval(ecape_opt)
            elif len(odp) > 0:
                eval(stay_opt)

        else:
            eval(win_path)

    elif p_w_count <= 0:  # if the player is dead
        print(f"\
        \n{gb.gameboook[cnst.translation]['combat_dead_info']} {Fore.LIGHTRED_EX}{entity.name}{cnst.combat_txt_clr}!\
        \n")
        dub_play('combat_die', 'adam', False)
        kill()

    else:  # if both player and enemy are alive
        combat_round(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path)

    return state, cnst.w_count, cnst.count


def combat_round(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path):
    cnst.round_count += 1
    print(f'\
    \n{cnst.combat_txt_clr}Runda: {cnst.round_count}{cnst.combat_txt_clr}')
    p_w_count = cnst.w_count
    e_w_count = entity.entity_w_count

    if cnst.automatic_battle:
        # Generate values 'a' and 'b' in automatic mode
        a = random.randint(2,
                           12) + entity.entity_z_count * cnst.e_mult_choice  # e_mult_choice acts as difficulty level affects the enemy's agility
        b = random.randint(2, 12) + cnst.z_count
    else:
        # Prompt the player to input values 'a' and 'b' manually by rolling two dice
        a = input(f"Enter the value of 'a' by rolling two dice{cnst.input_sign}")
        b = input(f"Enter the value of 'b' by rolling two dice{cnst.input_sign}")

    if state:
        loading(1)
        if a > b:  # if the enemy won

            if cnst.w_count > 0:
                if e_w_count <= 0:
                    state = False
                    # Proceed to combat_main function if the enemy is defeated
                    combat_main(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count,
                                win_path)
                cnst.w_count += cnst.e_hit_val_
                # Print the enemy's attack and update player's endurance
                print(f"{Fore.LIGHTRED_EX}{entity.name}{cnst.combat_txt_clr} landed a hit!\
                \n{cnst.special_txt_clr}/// Endurance {Fore.LIGHTYELLOW_EX}{cnst.player_name}{cnst.special_txt_clr}: {cnst.w_count}/{cnst.w_init}")
                dub_play('round_false', 'adam', False)

                cnst.w_count = max(cnst.w_count, 0)

        elif a < b:  # if the player won

            if entity.entity_w_count > 0:
                entity.entity_w_count += cnst.p_hit_val_
                # Print the player's attack and update enemy's endurance
                print(f"{Fore.LIGHTYELLOW_EX}{cnst.player_name}{cnst.combat_txt_clr} landed a hit!\
                \n{cnst.special_txt_clr}/// Endurance {Fore.LIGHTRED_EX}{entity.name}{cnst.special_txt_clr}: {entity.entity_w_count}/{entity.entity_w_init}")
                dub_play('round_true', 'adam', False)

                entity.entity_w_count = max(entity.entity_w_count, 0)

        else:  # if it's a draw
            print(f'{cnst.special_txt_clr}Draw!')
            dub_play('round_none', 'adam', False)

        if cnst.allow_skip_dub:  # If the option to skip the dubbing is enabled
            time.sleep(2 * cnst.delay)

    combat_main(entity, state, esc_possible, escape_id, stay_id, to_the_end, p_w_count, e_w_count, win_path)
