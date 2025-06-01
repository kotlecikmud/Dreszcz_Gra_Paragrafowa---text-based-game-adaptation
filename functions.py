import os
import json
import time
import random
import msvcrt
import platform
import datetime
import subprocess

import pygame
from colorama import Fore

import gamebook as gb
import constants as cnst
import entities as ent
# import paragraphs as prg # Removed

# Global cache for paragraph data
_ALL_PARAGRAPHS_DATA = None
# Define path for JSON relative to the project structure.
# Assuming functions.py is in the root directory or Assets/game_files is accessible from cwd.
# A more robust solution might use cnst.ROOT_DIR if available and reliable.
JSON_PATH = os.path.join('Assets', 'game_files', 'paragraphs.json')


# Helper function to get a specific paragraph's data from the loaded JSON
def _get_paragraph_data(paragraph_id, all_paragraphs_data):
    str_paragraph_id = str(paragraph_id) # Ensure ID comparison is string-to-string
    for p_data in all_paragraphs_data:
        if p_data.get("id") == str_paragraph_id:
            return p_data
    return None

# Helper function to evaluate conditions from JSON
def _evaluate_condition(condition_obj):
    condition_type = condition_obj.get("type")
    # Scope for eval: includes cnst, ent, random, and functions in this module (globals())
    # Provide access to entities via 'ent' and constants via 'cnst'
    eval_globals = {
        "cnst": cnst,
        "ent": ent,
        "random": random,
        "func": globals(), # Allows calling functions like check_for_luck from eval string
         # Add any other specific modules or values needed by condition_string eval here
    }
    # For direct attribute access like cnst.w_count or ent.some_entity.property
    # these modules (cnst, ent) must be imported in functions.py

    try:
        if condition_type == "stat_check":
            # stat_ref should be like "cnst.w_count" or "ent.player.strength"
            # It's evaluated to get the current value.
            stat_value = eval(condition_obj['stat_ref'], eval_globals)
            operator = condition_obj['operator']
            target_value = condition_obj['value']
            return eval(f"{stat_value} {operator} {target_value}")
        elif condition_type == "item_check":
            item_present = condition_obj['item_name'] in cnst.main_eq
            return item_present if condition_obj.get('has_item', True) else not item_present
        elif condition_type == "gold_check":
            op = condition_obj.get('operator', '>=')
            return eval(f"cnst.gold_amount {op} {condition_obj['value']}")
        elif condition_type == "eval_condition":
            # condition_string is a Python expression string
            return bool(eval(condition_obj['condition_string'], eval_globals))
        else:
            error_message("_evaluate_condition", f"Unknown condition type: {condition_type}")
            return False
    except Exception as e:
        error_message("_evaluate_condition", f"Error evaluating {condition_obj}: {e}")
        return False

# Placeholder for paragraph _269 logic - to be implemented if needed
def _handle_paragraph_269_choices():
    debug_message("Executing placeholder for _handle_paragraph_269_choices. Needs full implementation.")
    # This would contain the complex logic from original _269 to determine choices,
    # then it would call pth_selector with the chosen next paragraph_id based on that logic.
    jump_paragraph_xx() # Fallback behavior

# Helper function to execute actions from JSON
def _execute_action(action_obj, current_paragraph_id_str):
    action_type = action_obj.get("type")
    value = action_obj.get("value")

    eval_globals = {
        "cnst": cnst,
        "ent": ent,
        "random": random,
        "func": globals(), # Gives access to all functions in this module
        "gb": gb, # gamebook for text, though ideally actions don't print directly
        "pygame": pygame, # For mixer functions if any eval needs it
        # Add specific functions if globals() is too broad:
        # "update_variable": update_variable, "check_for_luck": check_for_luck, etc.
    }
    exec_locals = {} # For exec statements if they assign new local variables

    next_paragraph_id = None
    action_performed = True
    terminate_processing = False

    debug_message(f"Executing action: {action_type} with value: {value} for paragraph {current_paragraph_id_str}")

    try:
        if action_type == "play_audio":
            vo = value
            dub_play(vo.get('file_id'), vo.get('category'), vo.get('skippable', True),
                       vo.get('with_text', False), # Usually on_load_action audio is supplementary
                       vo.get('round_robin'))
        elif action_type == "stat_change":
            stat_ref_str = value['stat_ref'] # e.g., "cnst.w_count"
            module_str, var_name = stat_ref_str.split('.', 1)
            module = eval(module_str, eval_globals)

            current_val = getattr(module, var_name)
            limit_val_str = value.get('limit_ref')
            limit_val = eval(limit_val_str, eval_globals) if limit_val_str else None

            # Use the existing stats_change for its print logic and value capping
            new_val = stats_change(value.get('attribute_name', var_name), current_val, value['amount'], limit_val)
            setattr(module, var_name, new_val)

        elif action_type == "item_add":
            item_name = str(value['item_name']) # Ensure it's a string
            # Simplified gold handling
            if "gold" in item_name.lower() or "sztuk złota" in item_name.lower():
                try: # Try to parse amount, e.g. "10 gold"
                    amount = int(item_name.split()[0])
                    cnst.gold_amount = update_variable(cnst.gold_amount, amount) # update_variable handles the addition
                except: # Fallback if parsing fails, treat as regular item
                     if item_name not in cnst.main_eq: cnst.main_eq.append(item_name)
            elif item_name not in cnst.main_eq:
                cnst.main_eq.append(item_name)
            # Original eq_change function included an input() call for notification.
            # This should ideally be handled by the UI layer based on an event.
            # For now, we can call a simplified notification or rely on debug messages.
            debug_message(f"Item added/Gold changed: {item_name}")
            # If a visual notification like original eq_change is needed:
            # eq_change(item_name) # But this halts for input.

        elif action_type == "item_remove":
            item_name = str(value['item_name'])
            if item_name in cnst.main_eq: cnst.main_eq.remove(item_name)
            debug_message(f"Item removed: {item_name}")

        elif action_type == "variable_set":
            var_ref_str = value['var_ref'] # e.g., "ent.room_364.room_state" or "cnst.some_flag"
            new_value = value['new_value']

            if '.' in var_ref_str:
                obj_path, attr_name = var_ref_str.rsplit('.', 1)
                target_obj = eval(obj_path, eval_globals)
                setattr(target_obj, attr_name, new_value)
            else: # Assume it's a variable in 'cnst' or globals for direct modification via exec
                exec(f"{var_ref_str} = {repr(new_value)}", eval_globals) # repr to handle strings correctly

        elif action_type == "variable_change":
            var_ref_str = value['var_ref']
            change = value['change_amount']

            current_val = eval(var_ref_str, eval_globals)
            updated_val = update_variable(current_val, change) # update_variable handles the logic + debug print

            if '.' in var_ref_str:
                obj_path, attr_name = var_ref_str.rsplit('.', 1)
                target_obj = eval(obj_path, eval_globals)
                setattr(target_obj, attr_name, updated_val)
            else:
                exec(f"{var_ref_str} = {repr(updated_val)}", eval_globals)

        elif action_type == "conditional_jump":
            condition_met = any(_evaluate_condition(cond) for cond in action_obj.get('conditions', []))

            if condition_met and action_obj.get('true_target'):
                next_paragraph_id = str(action_obj['true_target'])
            elif not condition_met and action_obj.get('false_target'):
                next_paragraph_id = str(action_obj['false_target'])

            if next_paragraph_id: terminate_processing = True

        elif action_type == "conditional_actions":
            condition_met = any(_evaluate_condition(cond) for cond in value.get('conditions', []))
            actions_to_run = value.get('true_actions', []) if condition_met else value.get('false_actions', [])
            for sub_action in actions_to_run:
                result = _execute_action(sub_action, current_paragraph_id_str)
                if result.get('terminate_processing'):
                    next_paragraph_id = result.get('next_paragraph_id', next_paragraph_id) # Propagate jump
                    terminate_processing = True; break

        elif action_type == "combat":
            entity = eval(value['entity_id_ref'], eval_globals)
            # entity_state and esc_possible are often direct booleans or references to entity attributes
            entity_state = eval(str(value['entity_state_ref']), eval_globals) if isinstance(value['entity_state_ref'], str) else value['entity_state_ref']
            esc_possible = eval(str(value['escape_possible_ref']), eval_globals) if isinstance(value['escape_possible_ref'], str) else value['escape_possible_ref']

            # combat_main itself will eventually call pth_selector with the outcome paragraph ID.
            combat_main(entity, entity_state, esc_possible,
                        str(value['escape_paragraph_id']),      # escape_id in combat_main
                        str(value.get('win_paragraph_id')),     # stay_id in combat_main (normal win)
                        str(value.get('lose_paragraph_id', 'xx'))) # win_path in combat_main (player HP death)
            terminate_processing = True

        elif action_type == "eval_function":
            eval(value['function_string'], eval_globals, exec_locals) # Locals can capture results if needed

        elif action_type == "special_event":
            event_val = value['value']
            if event_val == "jump_prompt_xx":
                jump_paragraph_xx(); terminate_processing = True
            elif event_val == "elixir_choice_sequence":
                # This logic is from original _00
                while True:
                    dub_play('elxr_chc', 'adam', False, r_robin=5)
                    choice = input(f'{cnst.INPUT_SIGN}{cnst.DEFAULT_COLOR}')
                    if choice == '1': cnst.potion = 'z'; break
                    elif choice == '2': cnst.potion = 'w'; break
                    elif choice == '3': cnst.potion = 's'; break
                    else: clear_terminal(); print(cnst.SPECIAL_COLOR, gb.gameboook[cnst.setup_params["translation"]]['wrong_input'])
                # After choice, the original _00 sets game state, clears terminal, dub_plays 00b, then jumps to 01.
                # The current paragraph (_00) JSON should have a choice leading to 00b/01.
                # This event just sets the potion. Processing continues in current paragraph.
                terminate_processing = False
            elif event_val == "paragraph_269_logic":
                _handle_paragraph_269_choices(); terminate_processing = True
            else: error_message("special_event", f"Unknown event value: {event_val}")

        elif action_type == "visit_check_jump": # This action type performs an immediate jump based on room state
            room = eval(value['room_id_ref'], eval_globals)
            # visit_count is assumed to be incremented by pth_selector for the *current* room
            # This action is for jumping based on the state of a (possibly different) room.
            if room.room_state: # open
                # visit_count for the target room_id_ref is not incremented by this action itself
                # This needs careful thought: is visit_count for current room or target room?
                # For now, assume it checks target room's current visit_count
                # This implies target room's visit_count should be accurate.
                if not hasattr(room, 'visit_count') or room.visit_count == 0 : # Target room never visited or count is 0
                    next_paragraph_id = str(value['new_visit_target'])
                else: # Target room already visited
                    next_paragraph_id = str(value['revisit_target'])
            else: # closed
                next_paragraph_id = str(value['closed_target'])
            if next_paragraph_id: terminate_processing = True

        elif action_type == "jump":
            next_paragraph_id = str(value)
            terminate_processing = True

        elif action_type == "compound_action":
            for sub_action_obj in value.get('actions', []):
                result = _execute_action(sub_action_obj, current_paragraph_id_str)
                if result.get('terminate_processing'):
                    next_paragraph_id = result.get('next_paragraph_id', next_paragraph_id)
                    terminate_processing = True; break
        else:
            error_message("_execute_action", f"Unknown action type: {action_type}")
            action_performed = False

    except Exception as e:
        error_message(f"_execute_action ({action_type})", f"Error: {e} while processing paragraph {current_paragraph_id_str}")
        action_performed = False

    return {"next_paragraph_id": next_paragraph_id, "action_performed": action_performed, "terminate_processing": terminate_processing}

# class LoadingAnimation:
#     def __init__(self):
#         self.animation_signs = ['|', '/', '-', '\\']
#         self.sign_index = 0
#         self.finished = False
# 
#     def start(self):
#         import threading
#         self.finished = False
#         threading.Thread(target=self._animate).start()
# 
#     def stop(self):
#         self.finished = True
# 
#     def _animate(self):
#         while not self.finished:
#             print('- ' + self.animation_signs[self.sign_index % len(self.animation_signs)] + ' -', end='\r')
#             time.sleep(.1)
#             self.sign_index += 1


def log_event(entry):
    if cnst.setup_params['logging']:
        current_user = os.getlogin()
        time_stamp = datetime.datetime.now().strftime('[%d-%m-%y %H:%M:%S.%f]')

        with open(cnst.LOG_NAME, 'a') as f:
            f.write(
                f"{time_stamp} | v.{cnst.__version__} | user:{current_user} |> {entry}\n")  # write to log file


def debug_message(msg):
    if cnst.setup_params['debug_msg']:
        print(f"{cnst.DEBUG_COLOR}DEBUG: {msg}{cnst.DEFAULT_COLOR}")
        log_event(msg)


def error_message(error_name="", msg=""):
    if cnst.setup_params['dev_mode']:
        if error_name == '':
            error_name = 'ERROR'
        print(f'{cnst.ERR_COLOR}{error_name}{cnst.DEBUG_COLOR} || {msg}{cnst.DEFAULT_COLOR}')
        log_entry = error_name + msg
        log_event(log_entry)


def clear_terminal():
    if not cnst.setup_params['debug_msg']:
        subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)


def check_for_update():
    try:
        debug_message("checking for updates...")

        pull_output = subprocess.check_output("git pull", shell=True, text=True).strip()
        current_hash = subprocess.check_output("git rev-parse HEAD", shell=True, text=True).strip()
        debug_message(f"Hash: {current_hash}")

        if "Already up to date." in pull_output:
            return False

        else:
            debug_message("Repo updated - Restart game to see the changes")
            return True

    except subprocess.CalledProcessError as e:
        error_message(f"Error while checking for update {str(e)}")


def get_music(category=None, fadeout=None, update=None):
    """
    Play music based on the provided category.

    Args:
        category (str, optional): The category of music to play. Valid values are 'main', 'combat', or 'menu'.
                                 If not provided or set to None, no music will be played. Defaults to None.
        fadeout (int, optional): The duration in milliseconds for the fadeout effect before playing the new music.
                                 If not provided or set to None, no fadeout effect will be applied. Defaults to None.
        update (bool, optional): If True, update the background music volume to the value specified in cnst.setup_params["bckg_volume"].
                                 If False or not provided, the volume will not be updated. Defaults to None.

    Returns:
        None

    Raises:
        None

    Note:
        - The function requires the Pygame library to be imported and initialized before calling this function.
        - The music tracks for each category should be defined in the cnst.music_tracks dictionary.

    Example usage:
        # Play main music with a fadeout effect
        get_music(category='main', fadeout=1000)

        # Update the background music volume
        get_music(update=True)
    """

    if update:
        pygame.mixer.music.set_volume(cnst.setup_params["bckg_volume"])

    elif cnst.setup_params["get_music"]:
        if category in ['main', 'combat', 'menu']:
            random_track = random.choice(cnst.music_tracks[category])

            if fadeout:
                pygame.mixer.music.fadeout(fadeout)

            debug_message(f"Playing {category}: {random_track}")

            pygame.mixer.music.load(random_track)
            pygame.mixer.music.set_volume(cnst.setup_params["bckg_volume"])

            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)  # play in loop --> (-1)

    elif cnst.setup_params["dev_mode"]:
        debug_message(f"get_music() disabled - wanted to play: {category}")


def dub_play(string_id, category=None, skippable=True, with_text=True, r_robin=None):
    """
    Play an audio file associated with the provided string identifier.

    Args:
        string_id (str): The identifier of the audio file to be played.
        category (str, optional): The category of the audio file. Defaults to None.
        skippable (bool, optional): Indicates whether the audio file can be skipped. Defaults to True.
        with_text (bool, optional): Indicates whether to display the associated gamebook identifier as text. Defaults to True.
        r_robin (int, optional): An additional parameter for modifying the audio file identifier. Defaults to None.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified audio file is not found.
        KeyError: If the string identifier is not found in the gamebook.

    Notes:
        - This function plays audio files using the Pygame library.
        - The audio file path is constructed based on the provided parameters.
        - If dubbing is disabled, the user is prompted to continue with a specific input sign.
    """
    if r_robin:
        r_robin = "_" + str(random.randint(1, r_robin))

    else:
        r_robin = "_"

    is_voice = None
    audio_path = None
    audio_file_id = None

    if category:
        category = category.lower()
        if category == 'adam' or category == 'dub':
            audio_path = f'{cnst.AUDIO_VOICE_DIR}\\Adam'
            is_voice = True

        elif category == 'dunmer' or category == 'dub':
            audio_path = f'{cnst.AUDIO_VOICE_DIR}\\Dunmer'
            is_voice = True

        elif category == 'fx':
            audio_file_id = f'{cnst.AUDIO_FX_DIR}\\audiobook_{string_id}{r_robin}{cnst.AUDIO_EXTENSION}'

        if is_voice:
            audio_file_id = f'{audio_path}\\{cnst.setup_params["translation"]}\\audiobook_{category}_{cnst.setup_params["translation"]}_{string_id}{r_robin}{cnst.AUDIO_EXTENSION}'

    try:
        current_sound = pygame.mixer.Sound(audio_file_id)

    except FileNotFoundError:
        error_message('FileNotFoundError ', f'Could not find: {audio_file_id}')

        if is_voice:
            current_sound = pygame.mixer.Sound(f'{cnst.AUDIO_FX_DIR}\\AudioFileUnavailable.mp3')
        else:
            current_sound = pygame.mixer.Sound(f'{cnst.AUDIO_FX_DIR}\\audiobook_click_snd.mp3')

    pygame.mixer.stop()  # stop any sound currently being played
    current_sound.set_volume(cnst.setup_params["action_volume"])  # ensure that volume is on default

    # find empty channel
    channel = None
    for i in range(pygame.mixer.get_num_channels()):
        if not pygame.mixer.Channel(i).get_busy():
            channel = pygame.mixer.Channel(i)
            break

    if channel is None:
        debug_message('Could not find empty channel.')
        return

    if with_text:  # display currently selected gamebook identifier as text
        try:
            if len(string_id) > 0:
                print(gb.gameboook[cnst.setup_params["translation"]][string_id])

        except KeyError:
            channel.play(pygame.mixer.Sound(f'{cnst.AUDIO_FX_DIR}\\audiobook_click_snd.mp3'))
            error_message('KeyError', f'Could not find string: {string_id}')

    # if dubbing is enabled
    if cnst.setup_params["dubbing"]:
        # play the sound on the found channel
        channel.play(current_sound)
        debug_message(f'Now playing: {audio_file_id}')

        if skippable:
            # print a message indicating that we're skipping the input sign
            print(f"skip {cnst.INPUT_SIGN}")

            # continue looping while the channel is busy playing a sound
            while channel.get_busy():
                # check if any key is pressed
                if msvcrt.kbhit():
                    pygame.mixer.stop()  # stop any sound currently being played
                    break

    else:
        debug_message(f"dubbing disabled: {cnst.CFG_NAME}")
        input(f"continue {cnst.INPUT_SIGN}")
        time.sleep(.5)


def name_randomizer():
    # These parts will be changed for future translation versions. They must be implemented first as a sub-dictionary in gamebook.py for the variable gamebook={}
    first_parts = ['Bogdan', 'Dobrosław', 'Jarosław', 'Grzesiu', 'Mścisław', 'Radosław', 'Sławomir',
                   'Zbyszko z Bogdańca', 'Władysław', 'Zbigniew', 'Stanisław']
    last_parts = ['z Levygradu', 'Mądry', 'Odważny', 'z Małomorza', 'Prawy', 'Sprawiedliwy', 'Słomka', 'Wielki',
                  'Zacny', 'Zuchwały', 'Pyzdra']

    first_name = random.choice(first_parts)
    last_name = None

    # 'zbyszko z bogdańca' easteregg mechanic
    if first_name == 'Zbyszko z Bogdańca':  # meme for ya (probably only poles could understand, sorry)
        dub_play("zbych", "fx", True, False)
        time.sleep(2.7)
        clear_terminal()
        print(cnst.and_his_name_is)
        time.sleep(5.6)
    else:
        last_name = random.choice(last_parts)
    player_name = f'{Fore.LIGHTYELLOW_EX}{first_name} {last_name}{cnst.DEFAULT_COLOR}'
    print(player_name)
    time.sleep(1)
    cnst.player_name = player_name
    return cnst.player_name


def update_variable(variable, change, par_name=None):
    if isinstance(variable, bool):
        new_variable = change
    elif isinstance(variable, int) or isinstance(variable, float):
        new_variable = variable + change
    else:
        # Handling other variable types
        new_variable = variable

    if par_name:
        print(f"{par_name}: {variable} + {change} = {new_variable}")
    else:
        debug_message(f"no par_name; update_variable: {variable} + {change} = {new_variable}")

    return new_variable


def get_player_par():
    cnst.z_init = cnst.z_count = random.randint(1, 6) + 6
    cnst.w_init = cnst.w_count = random.randint(2, 12) + 12
    cnst.s_init = cnst.s_count = random.randint(1, 6) + 6
    return cnst.z_init, cnst.z_count, cnst.w_init, cnst.w_count, cnst.s_init, cnst.s_count


def open_dir(_path):
    if platform.system() == 'Windows':
        os.startfile(_path)
    elif platform.system() == 'Darwin':  # macOS
        subprocess.Popen(['open', _path])
    else:  # Linux
        subprocess.Popen(['xdg-open', _path])


def update_config_file(manual=False, backup=False):
    """
    Updates the setup file with user-defined or default values.

    Params:
        - manual (bool): If True, prompts the user to input new values for specific keys.
        - backup (bool): If True, uses a predefined backup data dictionary to update the setup file.

    Returns:
        None

    Description:
        - If manual is True, prompts the user to enter values for different keys.
        It displays the key name and expected input format.
        - If backup is True, uses a predefined backup data dictionary to update the setup file.
        - If both manual and backup are False, initializes the setup data dictionary with default values.
        - Saves the setup data dictionary to a JSON file named 'cnst.setup_name'.
        - Prints a debug message indicating that the setup file has been updated.
        - If manual is True, prompts the user to restart the game for some changes to take effect.
    """

    if manual:
        print("Leave empty for no changes:")
        setup_data = {}
        keys_list = [
            "active_gameplay",
            "translation",
            "action_volume",
            "sfx_volume",
            "bckg_volume",
            "dev_mode",
            "debug_msg",
            "use_dummy",
            "logging",
            "start_sequence",
            "manual_battle",
            "dubbing",
            "get_music",
            "enable_GUI"
        ]

        for key in keys_list:
            print()  # spacing between options

            if key == "active_gameplay":
                print('(path)')

            elif key == "translation":
                # list all the availale locales
                print(", ".join(list(gb.gameboook.keys())))

            elif key in ["dev_mode",
                         "debug_msg",
                         "use_dummy",
                         "logging",
                         "start_sequence",
                         "manual_battle",
                         "dubbing",
                         "get_music",
                         "enable_GUI"]:

                print('(True/False)')

            elif key in ["action_volume", "sfx_volume", "bckg_volume"]:
                print('int from 0.1 to 1.0')

            value = input(f"{key}: ")  # if user makes typo, config will get "None" value

            if value != '':
                try:
                    value = eval(value)
                except:
                    value = str(value)

                if value is True or value is False or value is None:
                    setup_data[key] = value

                elif isinstance(value, int):
                    setup_data[key] = int(value)

                else:
                    setup_data[key] = str(value)
            else:
                setup_data[key] = cnst.__dict__[key]

    elif backup:
        setup_data = {
            "active_gameplay": None,
            "translation": "en",
            "action_volume": 1,
            "sfx_volume": .7,
            "bckg_volume": .6,
            "dev_mode": False,
            "debug_msg": True,
            "use_dummy": True,
            "logging": True,
            "start_sequence": False,
            "manual_battle": False,
            "dubbing": True,
            "get_music": True,
            "enable_GUI": False
        }
        debug_message('restored backup setup')

    else:
        setup_data = {
            "active_gameplay": cnst.setup_params["active_gameplay"],
            "translation": cnst.setup_params["translation"],
            "action_volume": cnst.setup_params["action_volume"],
            "sfx_volume": cnst.setup_params["sfx_volume"],
            "bckg_volume": cnst.setup_params["bckg_volume"],
            "dev_mode": cnst.setup_params["dev_mode"],
            "debug_msg": cnst.setup_params['debug_msg'],
            "use_dummy": cnst.setup_params["use_dummy"],
            "logging": cnst.setup_params["logging"],
            "start_sequence": cnst.setup_params["start_sequence"],
            "manual_battle": cnst.setup_params["manual_battle"],
            "dubbing": cnst.setup_params["dubbing"],
            "get_music": cnst.setup_params["get_music"],
            "enable_GUI": cnst.setup_params["enable_GUI"]
        }

    # Save the setup data to a JSON file
    with open(cnst.CFG_NAME, 'w') as json_file:
        json.dump(setup_data, json_file)
    debug_message("config.json has been updated")

    if backup or manual:
        input(
            f"{cnst.SPECIAL_COLOR}Please restart the game for the changes to take effect.\
            \n{cnst.INPUT_SIGN}{cnst.DEFAULT_COLOR}")


def get_game_state(action, last_paragraph='00', new_game=None):
    """
    Retrieves or initializes the game state based on the specified action.

    Parameters:
        action (str): The action to perform. Possible values: 's' (save), 'l' (load), 'c' (continue), 'init' (initialize).
        last_paragraph (str): The last paragraph visited in the game (default: 'prg.00').
        new_game (bool): Indicates whether a new game is being created (default: None).

    Returns:
        str: The last visited paragraph.

    Actions:
        - 's': Saves the current game state to a JSON file.
        - 'l': Loads a game state from a JSON file.
        - 'c': Continues the game from the last saved state saved in config.json.
        - 'init': Checks if any game states exist and optionally initializes a dummy game state.

    Notes:
        - The 's' action saves the current game state to a JSON file based on the 'last_paragraph' and 'new_game' parameters.
        - The 'l' action allows the user to select a saved game state from a list and loads it.
        - The 'c' action loads the last saved game state.
        - The 'init' action checks if any game states exist. If none exist and the 'cnst.use_dummy' flag is True,
          it initializes a dummy game state and saves it to a JSON file.
        - The game state includes various variables such as player name, difficulty level, item counts, and gold amount.

    Raises:
        ValueError: If an incorrect file number is provided during the 'l' action.

    """
    # list of json files in folder_path
    valid_json_files = []

    debug_message(f"Looking for game states in '~\\Documents' folder path for saving json file")
    if os.path.exists(cnst.GAMESTATE_DIR):
        json_files = [file for file in os.listdir(cnst.GAMESTATE_DIR) if file.endswith(cnst.GAMESTATE_EXTENSION)]

        for file_name in json_files:
            if file_name.startswith('dreszcz_'):
                debug_message(f"{file_name} is valid game state file")
                valid_json_files.append(file_name)
            else:
                debug_message(f"{file_name} is not a valid game state file")

    else:
        os.makedirs(cnst.GAMESTATE_DIR)
        debug_message(f'Game_state directory not present, created new one: {cnst.GAMESTATE_DIR}')

    if action == 's':
        if new_game:
            # Create new file path and update active gameplay file_path
            cnst.setup_params['active_gameplay'] = os.path.join(cnst.GAMESTATE_DIR,
                                                                f"dreszcz_{datetime.datetime.now().strftime('%y-%m-%d_%S')}{cnst.GAMESTATE_EXTENSION}")
        # Load game state to variables
        game_state = {
            "last_paragraph": last_paragraph,
            "player_name": cnst.player_name,
            "difficulty": cnst.DIFFICULTY,
            "s_count": cnst.s_count,
            "w_count": cnst.w_count,
            "z_count": cnst.z_count,
            "s_init": cnst.s_init,
            "w_init": cnst.w_init,
            "z_init": cnst.z_init,
            "equipment": cnst.main_eq,
            "potion": cnst.potion,
            "potion_count": cnst.potion_count,
            "meal_count": cnst.meal_count,
            "gold_amount": cnst.gold_amount,
            "version": cnst.__version__,
            # save information abaut version number that game state was generated in
        }

        # Saving game state as json file
        with open(cnst.setup_params['active_gameplay'], "w") as f:
            json.dump(game_state, f)
        debug_message(f'Game saved to: {cnst.setup_params["active_gameplay"]}')

    elif action == 'l':
        # List of JSON files
        if len(valid_json_files) > 0:
            print("Saved game states:")

            for i, file in enumerate(valid_json_files, start=1):
                print(f"{i}. {file}")

            while True:
                file_number = input(f"\nChoose game state to load (leave empty to return to main menu)\
                \n{cnst.INPUT_SIGN}")

                if not file_number.isdigit():
                    return  # Return to main menu if input is not a number

                try:
                    file_number = int(file_number)

                    if 1 <= file_number <= len(valid_json_files):
                        selected_file = valid_json_files[file_number - 1]
                        cnst.setup_params['active_gameplay'] = os.path.join(cnst.GAMESTATE_DIR, selected_file)
                        with open(cnst.setup_params['active_gameplay'], "r") as f:
                            game_state = json.load(f)
                        debug_message(f'Game state loaded from: {selected_file}')
                        break

                except ValueError:
                    debug_message("Incorrect file number provided.")

            # Assigning the loaded data back to variables.
            last_paragraph = game_state.get("last_paragraph")
            cnst.player_name = game_state.get("player_name")
            cnst.difficulty = game_state.get("difficulty")
            cnst.s_count = game_state.get("s_count")
            cnst.s_count = game_state.get("s_count")
            cnst.w_count = game_state.get("w_count")
            cnst.z_count = game_state.get("z_count")
            cnst.s_init = game_state.get("s_init")
            cnst.w_init = game_state.get("w_init")
            cnst.z_init = game_state.get("z_init")
            cnst.main_eq = game_state.get("equipment")
            cnst.potion = game_state.get("potion")
            cnst.potion_count = game_state.get("potion_count")
            cnst.meal_count = game_state.get("meal_count")
            cnst.gold_amount = game_state.get("gold_amount")

        else:
            debug_message("No saved game states found.")

    elif action == 'c':  # continue
        with open(cnst.setup_params["active_gameplay"], "r") as f:
            game_state = json.load(f)

            # Assigning the loaded data back to variables.
            last_paragraph = game_state.get("last_paragraph")
            cnst.player_name = game_state.get("player_name")
            cnst.difficulty = game_state.get("difficulty")
            cnst.s_count = game_state.get("s_count")
            cnst.w_count = game_state.get("w_count")
            cnst.z_count = game_state.get("z_count")
            cnst.s_init = game_state.get("s_init")
            cnst.w_init = game_state.get("w_init")
            cnst.z_init = game_state.get("z_init")
            cnst.main_eq = game_state.get("equipment")
            cnst.potion = game_state.get("potion")
            cnst.potion_count = game_state.get("potion_count")
            cnst.meal_count = game_state.get("meal_count")
            cnst.gold_amount = game_state.get("gold_amount")

        debug_message(f'Game state loaded from: {cnst.setup_params["active_gameplay"]}')

    elif action == 'init':  # check if any game states exist
        if int(len(valid_json_files)) > 0:
            cnst.game_state_exists = True

            if cnst.setup_params['use_dummy']:
                cnst.setup_params["active_gameplay"] = str(cnst.DUMMY_GAMESTATE_NAME)
                debug_message("active_gameplay set to dummy")

        else:
            if cnst.setup_params['use_dummy']:
                game_state = {
                    "last_paragraph": "xx",
                    "player_name": "dummy_player",
                    "difficulty": 1,
                    "s_count": 20,
                    "w_count": 20,
                    "z_count": 20,
                    "s_init": 20,
                    "w_init": 20,
                    "z_init": 20,
                    "equipment": {
                        "plecak na Prowiant": "",
                        "prowiant": 8,
                        "tarcza": True,
                        "miecz": True
                    },
                    "potion": "w",
                    "potion_count": 2,
                    "meal_count": 8,
                    "gold_amount": 0,
                    "version": cnst.__version__
                }

                # Saving dummy game state if one doesn't exist
                with open(os.path.join(os.path.expanduser('~\\Documents'), cnst.DUMMY_GAMESTATE_NAME), "w") as f:
                    json.dump(game_state, f)

                cnst.setup_params["active_gameplay"] = str(cnst.DUMMY_GAMESTATE_NAME)
                debug_message(f"Dummy game_state file restored")
                debug_message(f"active_gameplay has been updated -> {cnst.setup_params['active_gameplay']}")

                cnst.game_state_exists = True

            else:
                cnst.game_state_exists = False

        return

    update_config_file()  # dump all setup to json file
    print(cnst.DEFAULT_COLOR)  # reset text color

    return last_paragraph


# get_game_state("init") # Called from menu.py

def jump_paragraph_xx():
    # Moved logic from prg._xx()
    # This function now serves as a fallback or explicit jump mechanism
    while True:
        debug_message("-- User Jump Prompt (_xx) --")
        # Ensure any previous paragraph audio is stopped
        pygame.mixer.stop()
        odp = input(f"{cnst.DEFAULT_COLOR}\nEnter paragraph ID to jump to (or 'exit'): {cnst.INPUT_SIGN}{cnst.DEFAULT_COLOR}")

        if odp.lower() == 'exit':
            clear_terminal()
            # Consider a more graceful exit or returning a special marker to the main game loop
            print("Exiting game via _xx.")
            exit()

        if odp.strip().isalnum(): # Check if it's a valid looking ID (alphanumeric)
            # Save game state before jumping via xx, with the target paragraph ID
            # This assumes get_game_state can handle potentially invalid 'odp' if user types junk
            get_game_state('s', odp)
            pth_selector(odp) # Call the new pth_selector with the ID
            break # Exit the while loop as pth_selector will take over or return
        else:
            error_message("jump_paragraph_xx", f"Invalid paragraph ID format: '{odp}'. Please enter alphanumeric ID.")


def pth_selector(current_paragraph_id_str): # Expects string ID
    all_paragraphs = load_all_paragraphs_data()
    if not all_paragraphs: # Critical error if JSON is missing/corrupt
        print(f"{cnst.ERR_COLOR}CRITICAL ERROR: Paragraph data is missing or corrupt. Cannot continue.{cnst.DEFAULT_COLOR}")
        # A more robust game would try to return to a main menu or safe state here
        exit()

    current_paragraph_id_str = str(current_paragraph_id_str).strip() # Ensure string ID and no whitespace
    paragraph_data = _get_paragraph_data(current_paragraph_id_str, all_paragraphs)

    if paragraph_data is None:
        error_message("pth_selector", f"Paragraph ID '{current_paragraph_id_str}' not found in JSON.")
        jump_paragraph_xx() # Fallback to user jump prompt
        return

    # Increment visit count for the current paragraph if it's a room entity
    # This requires 'ent' to be structured such that 'ent.room_XYZ' exists if XYZ is a room ID.
    try:
        # Attempt to find a room entity matching the paragraph ID (e.g., ent.room_1, ent.room_364)
        room_entity = eval(f"ent.room_{current_paragraph_id_str}", {"ent": ent})
        if room_entity and hasattr(room_entity, 'visit_count'):
            # update_variable is a global function in this module
            room_entity.visit_count = update_variable(room_entity.visit_count, 1)
            debug_message(f"Incremented visit count for room {current_paragraph_id_str} to {room_entity.visit_count}")
    except (AttributeError, NameError, SyntaxError): # If not a room or ent.room_XYZ doesn't exist
        pass # Not all paragraphs correspond to rooms with visit counts

    debug_message(f"--- Processing Paragraph: {current_paragraph_id_str} (Text Key: {paragraph_data.get('text_key', 'N/A')}) ---")
    clear_terminal()

    # 1. Process on_load_actions
    if 'on_load_actions' in paragraph_data:
        for action_obj in paragraph_data['on_load_actions']:
            result = _execute_action(action_obj, current_paragraph_id_str)
            if result.get('terminate_processing'):
                if result.get('next_paragraph_id'):
                    get_game_state('s', result['next_paragraph_id'])
                    pth_selector(result['next_paragraph_id'])
                return # Stop further processing for this paragraph

    # 2. Handle main audio_cue (from 'audio_cue' field in JSON)
    # Check if audio was already played by an on_load_action (e.g. conditional_actions)
    audio_played_in_on_load = False
    if 'on_load_actions' in paragraph_data:
        for action_obj in paragraph_data.get('on_load_actions',[]):
            if action_obj.get("type") == "play_audio": # Explicitly played audio
                audio_played_in_on_load = True; break
            if action_obj.get("type") == "conditional_actions": # Conditional actions might play audio
                # This is a simplification; true_actions/false_actions would need inspection
                # For now, assume if conditional_actions exists, it handles its audio if any.
                # A more robust check would see if 'play_audio' is in the executed branch.
                pass # Let's assume conditional_actions handles its audio, so don't play main audio_cue if it exists

    main_audio_cue = paragraph_data.get('audio_cue')
    main_text_key_associated_with_audio = None

    if main_audio_cue and not audio_played_in_on_load:
         main_text_key_associated_with_audio = main_audio_cue.get('file_id') # Used to link audio to text_key
         dub_play(
             main_audio_cue.get('file_id'),
             main_audio_cue.get('category'),
             main_audio_cue.get('skippable', True),
             main_audio_cue.get('with_text', True), # Main audio usually prints its associated text
             main_audio_cue.get('round_robin')
         )

    # 3. Display primary paragraph text (from 'text_key' field)
    # Only print if not already handled by the main audio_cue's with_text=True
    if 'text_key' in paragraph_data:
        should_print_main_text = True
        if main_audio_cue and main_audio_cue.get('with_text', True) and not audio_played_in_on_load:
            # If main audio was played and IT handled text, don't print again IF text_keys match
            if paragraph_data['text_key'] == main_text_key_associated_with_audio:
                 should_print_main_text = False

        if should_print_main_text:
            # Fallback to text_key itself if not found in gamebook (e.g. for "xxx_no_text")
            text_content = gb.gameboook[cnst.setup_params['translation']].get(paragraph_data['text_key'], paragraph_data['text_key'])
            # Avoid printing keys like "xxx_no_text" or if content is identical to key
            if text_content and text_content != paragraph_data['text_key'] or not paragraph_data['text_key'].endswith("_no_text"):
                 print(text_content)
            elif not gb.gameboook[cnst.setup_params['translation']].get(paragraph_data['text_key']):
                 debug_message(f"Main text_key '{paragraph_data['text_key']}' not found in gamebook, using key as text if not a control key.")


    # 4. Display supplementary texts
    if 'supplementary_text_keys' in paragraph_data:
        for key in paragraph_data['supplementary_text_keys']:
            text_content = gb.gameboook[cnst.setup_params['translation']].get(key, key)
            print(text_content)

    # 5. Process and Display Choices
    actual_choices = []
    # Standard choices from "choices" array
    if 'choices' in paragraph_data:
        for choice_obj in paragraph_data['choices']:
            conditions_pass = True # Assume true unless conditions exist and fail
            if 'conditions' in choice_obj: # Check for inline conditions for a choice
                conditions_pass = all(_evaluate_condition(cond) for cond in choice_obj['conditions'])
            if conditions_pass:
                actual_choices.append(choice_obj)

    # Conditional choice sets from "conditional_choices" array (for complex branching like _269)
    if not actual_choices and 'conditional_choices' in paragraph_data: # Only if no standard choices were resolved
        for choice_set in paragraph_data['conditional_choices']:
            all_set_conditions_met = True # Default to true for a set with empty/no conditions (fallback)
            if choice_set.get('conditions'):
                all_set_conditions_met = all(_evaluate_condition(cond) for cond in choice_set['conditions'])

            if all_set_conditions_met: # Found the first matching set of choices
                actual_choices.extend(choice_set['choices'])
                break

    # Special handling for paragraph _115 choices (if its JSON structure relies on this)
    if current_paragraph_id_str == '115' and hasattr(cnst, 'choices_115'):
        debug_message("Paragraph 115: Dynamically populating choices from cnst.choices_115.")
        actual_choices = [] # Override any static choices in JSON for _115 if cnst.choices_115 is used
        for text, target_func_name in cnst.choices_115.items():
            target_para_id = target_func_name.replace("_", "")
            actual_choices.append({
                "text_key": text,
                "action": {
                    "type": "compound_action",
                    "actions": [
                        {"type": "item_add", "value": {"item_name": text}},
                        {"type": "jump", "value": target_para_id}
                    ]
                }
            })

    if not actual_choices: # No choices resolved from any source
        debug_message(f"No available choices for paragraph {current_paragraph_id_str}. Game may end or need fallback.")
        # This might be an end-of-path, or might require a jump_paragraph_xx() if it's an error state.
        # For now, if a paragraph is designed to have no choices (e.g., it only has on_load_actions that jump), this is fine.
        return

    # Display choices
    for i, choice_obj in enumerate(actual_choices):
        choice_text_key = choice_obj.get('text_key', f"Choice_{i+1}")
        choice_text = gb.gameboook[cnst.setup_params['translation']].get(choice_text_key, choice_text_key)
        print(f'{i + 1} · {choice_text}')
        time.sleep(cnst.TIME_DELAY) # Original behavior

    # Get player input
    selected_index = -1
    while True:
        usr_input_str = input(f'{cnst.INPUT_SIGN}{cnst.DEFAULT_COLOR}')
        try:
            usr_input_idx = int(usr_input_str)
            if 1 <= usr_input_idx <= len(actual_choices):
                selected_index = usr_input_idx - 1; break
        except ValueError: pass
        print(f'/!/ {cnst.SPECIAL_COLOR}Choose number from list{cnst.DEFAULT_COLOR}')

    chosen_choice_obj = actual_choices[selected_index]

    # Handle audio for the chosen choice itself, if specified
    if 'audio_cue' in chosen_choice_obj:
        vo_choice = chosen_choice_obj['audio_cue']
        dub_play(vo_choice.get('file_id'), vo_choice.get('category'),
                   vo_choice.get('skippable', True), vo_choice.get('with_text', False),
                   vo_choice.get('round_robin'))

    # pygame.mixer.stop() # Stop narration before processing action. dub_play already does this.

    # Execute chosen action
    chosen_action_obj = chosen_choice_obj['action']
    result = _execute_action(chosen_action_obj, current_paragraph_id_str)

    if result.get('next_paragraph_id'):
        get_game_state('s', result['next_paragraph_id'])
        pth_selector(result['next_paragraph_id'])
    # If no next_paragraph_id from action, current path of game logic ends.
    # Could add a check here: if not result.get('terminate_processing'), maybe re-show current paragraph (though risky for loops)

def kill():
    """
    Parameters:
        path_strings (list[str], optional): A list of strings representing path descriptions.
        actions (list[str], optional): A list of strings representing actions to be executed.
        visit_check (bool, optional): A boolean flag indicating whether to perform a visit check.
        room_id (object, optional): An object representing the current room.

    Returns:
        None

    Raises:
        None

    Description:
        This function takes several parameters and performs different actions based on the conditions specified.

        If a `room_id` is provided, the function updates the `visit_count` variable of the room
        by incrementing it by 1.

        If `visit_check` is True, the function checks the state of the room. If the room is open,
        it prints a message indicating that the room is open. Based on the number of visits
        and the maximum allowed visits,
        it evaluates and executes the appropriate action from the `actions` list.

        If the room is closed, it prints a message indicating that the room is closed and
        executes the second action from the `actions` list.

        If `visit_check` is False, the function directly evaluates and executes the action(s) from the `actions` list.
        If there is more than one action, it displays a choice menu and waits for the user to input a valid choice.
        Once a valid choice is made, it executes the corresponding action. If there is only one action,
        it executes it automatically.

        The function does not return any value.
    """

    if path_strings is None:
        path_strings = []

    if room_id:  # add visit count if room number was given
        room_id.visit_count = update_variable(room_id.visit_count, 1)
        debug_message(f'added visit: visit count of room number {room_id.room_num} = {room_id.visit_count}')

    if visit_check:
        if room_id.room_state:  # if open
            print(
                f"{gb.gameboook[cnst.setup_params['translation']]['door']} {cnst.SPECIAL_COLOR}{room_id.room_num}{cnst.DEFAULT_COLOR} {gb.gameboook[cnst.setup_params['translation']]['are']} {cnst.SPECIAL_COLOR}{gb.gameboook[cnst.setup_params['translation']]['opened']}{cnst.DEFAULT_COLOR}.")
            dub_play('opened', 'adam', False, False)

            # Player is visiting the room more times than the allowed number.
            if not room_id.visit_count - 1 >= room_id.max_visit_count:
                if room_id.visit_count == 1:  # Player first time in room
                    get_game_state('s', actions[1])

                    debug_message(f'eval: {actions[1]}')
                    eval("prg._" + actions[1] + "()")

                # Player has already visited the room before, but did not exceed the allowed number of visits.
                elif room_id.visit_count >= 2:
                    get_game_state('s', actions[0])

                    debug_message(f'eval: {actions[0]}')
                    eval("prg._" + actions[0] + "()")

            else:
                print("Nothing to find here")

        else:  # if closed
            try:
                print(
                    f"{gb.gameboook[cnst.setup_params['translation']]['door']} {cnst.SPECIAL_COLOR}{room_id.room_num}{cnst.DEFAULT_COLOR} {gb.gameboook[cnst.setup_params['translation']]['are']} {gb.gameboook[cnst.setup_params['translation']]['closed']}{cnst.DEFAULT_COLOR}.")
            except KeyError:
                debug_message(f"this line does not exist in gamebook[{cnst.setup_params['translation']}]")
            dub_play('closed', 'adam', False, False, r_robin=1)

            debug_message(f'eval: {actions[1]}')
            eval("prg._" + actions[1] + "()")

    else:
        debug_message(f'list of available actions: {actions}')

        if len(actions) > 1:  # If there is more than one path, display the choice menu
            for i, path in enumerate(path_strings):
                print(f'{i + 1} · {path}')
                time.sleep(cnst.TIME_DELAY)

            while True:
                usr_input = input(f'{cnst.INPUT_SIGN}')

                try:
                    usr_input = int(usr_input)

                    if 0 < usr_input <= len(path_strings):
                        break

                except ValueError:
                    print(f'/!/ {cnst.SPECIAL_COLOR}Choose number from list{cnst.DEFAULT_COLOR}')

            clear_terminal()
            pygame.mixer.stop()  # Abort any dubbing currently being played
            get_game_state('s', actions[usr_input - 1])  # Save game_state to active one

            debug_message(f'evaluated: {actions[usr_input - 1]}')
            eval("prg._" + actions[usr_input - 1] + "()")

        else:  # If there is only one path, continue automatically
            clear_terminal()
            get_game_state('s', actions[0])  # Save game_state to active one

            debug_message(f'evaluated: {actions[0]}')
            eval("prg._" + actions[0] + "()")


def kill():
    print("You loose!!!")
    pygame.mixer.music.fadeout(2000)
    exit()


def win():
    print("You won!!!")
    pygame.mixer.music.fadeout(2000)
    exit()


def check_for_luck():
    update_variable(cnst.s_count, -1)

    print(f'{cnst.SPECIAL_COLOR}Sprawdzam czy masz szczęście:')  # Checking if you're lucky
    time.sleep(1)

    if random.randint(2, 12) <= cnst.s_count:
        print('Uff, masz szczęście.')  # Phew, you're lucky.
        p_luck = True

    else:
        print('Nie masz szczęścia!')  # No luck for you!
        p_luck = False

    return p_luck


def eatables():
    """
    Description:
        Interacts with the user to consume or save food supplies based on certain conditions.

        This function checks the value of `cnst.meal_count`, which represents the available
        count of eatables (food supplies).
        If the `meal_count` is not zero, the function enters a loop to interact with the user until
        a valid response is provided.

        During the interaction, the function displays the current status of the user's endurance (`cnst.w_count`)
        and the available eatables count (`cnst.meal_count`).
        The user is prompted to respond with either 'yes' or 'no' to indicate whether they want to consume the eatables
        or save them for later.

        If the user responds positively, the function updates the variables `cnst.meal_count` and `cnst.w_count`
        based on predefined rules.
        The function subtracts 1 from `meal_count` and increases the `w_count` (endurance) by a calculated value,
        which is the minimum between `cnst.STAMINA_PER_MEAL`
        and the remaining endurance needed to reach the initial endurance value (`cnst.w_init`).

        After performing the updates, the function prints the changes in endurance and the updated status of the
        endurance and eatables count.

        If the user responds negatively or provides an invalid response, the function prints appropriate messages and
        exits the loop.

    Params:
        None

    Returns:
        None
    """
    msg_1 = f"/// Wytrzymałość: {cnst.w_count}/{cnst.w_init}"
    msg_2 = f"/// Prowiant: {cnst.meal_count}/{cnst.INIT_MEAL_COUNT}"

    if cnst.meal_count != 0:
        while True:
            if cnst.w_count != cnst.w_init:
                dub_play("eatables", "adam", False)

                print(msg_1)
                print(msg_2)
                odp = input(f"{cnst.INPUT_SIGN}")
                if odp.lower() in {'tak', 't', 'y', 'yes'}:
                    if cnst.w_count < cnst.w_init:
                        update_variable(cnst.meal_count, -1)
                        inc_stamina = min(cnst.STAMINA_PER_MEAL, cnst.w_init - cnst.w_count)
                        update_variable(cnst.w_count, inc_stamina, "Wytrzymałość")
                        print(msg_1)
                        print(msg_2)
                        print(f"{cnst.DEFAULT_COLOR}")
                        break

                elif odp.lower() in {'nie', 'n', 'no'}:
                    print("Zostawiasz prowiant na później")
                    print(f"{cnst.DEFAULT_COLOR}")
                    break

                else:
                    print("Wpisz tak/nie")
            else:
                break


def show_equipment_list():
    for i in cnst.main_eq:
        print(f'- {i}')
    input(f"{cnst.INPUT_SIGN} ")


def eq_change(new_item_name):
    input(f"/// {cnst.SPECIAL_COLOR}Zdobyto nowy przedmiot: {new_item_name}{cnst.DEFAULT_COLOR}\
    \n{cnst.INPUT_SIGN}")


def get_state(req_amount, variable):
    if variable >= req_amount:
        state = True
    else:
        state = False

    return state


def show_player_stats():
    print(f"\
    \n{cnst.DEFAULT_COLOR}Gracz:\
    \nWytrzymałość: {cnst.w_count}/{cnst.w_init} \
    \nZręczność: {cnst.z_count}/{cnst.z_init} \
    \nSzczęście: {cnst.s_count}/{cnst.s_init}")


def show_entity_stats(entity):
    print(f"\
    \n{cnst.DEFAULT_COLOR}{entity.name}:\
    \nWytrzymałość: {entity.entity_w_count}/{entity.entity_w_init}\
    \nZręczność: {entity.entity_z_count}/{entity.entity_z_init}")


def stats_change(attribute_name, parameter, amount, limit=None):
    inter = '+' if amount >= 0 else ''

    if limit:  # for attributes that can't be increased above limit
        updated_parameter = min(parameter + amount, limit)

    else:  # for attributes that can be increased above limit
        updated_parameter = parameter + amount

    if parameter != limit:
        print(
            f'{cnst.SPECIAL_COLOR}/// {attribute_name}({parameter}) {inter} {amount} {cnst.INPUT_SIGN}{updated_parameter}{cnst.DEFAULT_COLOR}')

    return updated_parameter


def use_potion():
    updated_state = None
    if cnst.potion_count > 0:
        potion_attributes = {
            'w': (cnst.w_count, cnst.w_init),
            'z': (cnst.z_count, cnst.z_init),
            's': (cnst.s_count, cnst.s_init + 1)
        }
        if cnst.potion in potion_attributes:
            attr_name, attr_value = potion_attributes[cnst.potion]
            setattr(cnst, attr_name, attr_value)
        updated_state = cnst.potion_count - 1

    return updated_state


# - - - - - - - - -
# /// COMBAT
# - - - - - - - - -

def combat_main(entity, state, esc_possible, escape_id, stay_id, win_path):
    """
    Simulates a combat scenario in the game.

    Args:
        entity (Entity): The enemy entity object representing the opponent.
        state (bool): The state of the enemy entity, where True means the enemy is alive.
        esc_possible (bool): Indicates whether escape is possible in the combat scenario.
        escape_id (str): The identifier for the escape path.
        stay_id (str): The identifier for the stay path.
        win_path (str): The path to follow upon winning the combat scenario.

    Returns:
        None

    Raises:
        None

    Description:
        This function simulates a combat scenario in the game. It takes an enemy entity, state of the enemy,
        escape possibility, escape and stay options, and the path to follow upon winning as inputs.

        The function sets up the combat by fading out any currently playing music, loading the combat background
        music, and initializing the combat setup variables.

        It then displays the player and entity statistics and waits for user input to proceed with the combat.

        Inside the combat loop, a new round begins if the enemy is alive. The function prepares for the round by
        clearing the terminal, incrementing the round count, and displaying the current round ID.

        If manual battle is enabled, the function prompts the user to input the values of 'a' and 'b' by rolling
        two dice. Otherwise, random values are generated for 'a' and 'b' based on the enemy and player power.

        Depending on the values of 'a' and 'b', the function determines whether the enemy or the player lands a hit.
        If the enemy is stronger, the player's weapon count is reduced and a hit message is displayed. If the player
        is stronger, the enemy's weapon count is reduced and a hit message is displayed. If it's a draw, a message
        indicating a draw is printed to the console.

        After each round, the function displays the updated weapon counts for the player and entity, shows debug
        messages, and introduces a brief delay.

        If the enemy's weapon count reaches or falls below 0, it means the enemy is dead, and the combat loop breaks.

        If the player's weapon count reaches or falls below 0, it means the player is dead. The function prints a
        death message, plays a death sound, and terminates the program.

        Once the combat loop ends, the function fades out the combat music, loads the main background music,
        prints a victory message, plays a victory sound, shows the player's statistics, and presents the options
        to either escape or stay, depending on the escape possibility flag.

        If the player chooses to escape, their weapon count is reduced, and the escape option is evaluated.

        If the player chooses to stay or provides an invalid input, the stay option is evaluated.

        If escape is not possible, the win path is evaluated directly.
        """

    if state:
        # loading background music
        get_music('combat', 1500)

        # set round number to 0
        round_count = 0

        show_player_stats()
        show_entity_stats(entity)

        # press enter to start combat
        input(f"\n{cnst.COMBAT_COLOR}{gb.gameboook[cnst.setup_params['translation']]['combat_init']} {cnst.INPUT_SIGN}")

        while True:
            if state:  # if enemy is alive begin new round
                # preparing next round
                clear_terminal()
                round_count += 1

                print(f"\n{cnst.COMBAT_COLOR}Round: {round_count}{cnst.COMBAT_COLOR}")  # display round ID

                if cnst.setup_params["manual_battle"]:
                    a = input(f"Enter the value of 'a' by rolling two dice{cnst.INPUT_SIGN}")
                    b = input(f"Enter the value of 'b' by rolling two dice{cnst.INPUT_SIGN}")

                else:
                    a = random.randint(2, 12) + entity.entity_z_count * cnst.entity_hit_mult  # value of enemy power
                    b = random.randint(2, 12) + cnst.z_count  # value of player power

                ###########################

                if a > b:  # if the enemy is stronger
                    if cnst.w_count > 0:
                        cnst.w_count += cnst.e_hit_val_

                        dub_play("round_false", 'adam', False, False, r_robin=5)
                        cnst.w_count = max(cnst.w_count, 0)
                        print(f"{Fore.LIGHTRED_EX}{entity.name}{cnst.COMBAT_COLOR} landed a hit!")

                elif a < b:  # if the player is stronger
                    if entity.entity_w_count > 0:
                        entity.entity_w_count += cnst.p_hit_val_

                        dub_play("round_true", 'adam', False, False, r_robin=5)
                        entity.entity_w_count = max(entity.entity_w_count, 0)
                        print(f"{Fore.LIGHTYELLOW_EX}{cnst.player_name}{cnst.COMBAT_COLOR} landed a hit!")

                else:  # if it's a draw
                    print(f'{cnst.SPECIAL_COLOR}Draw!\
                        \nNobody got hurt!')

                    dub_play("round_none", 'adam', False, False, r_robin=5)

                time.sleep(1.5)  # time for dubbing

                ###########################

                print(
                    f"\
                        \n{Fore.LIGHTYELLOW_EX}{cnst.player_name}{cnst.SPECIAL_COLOR}: {cnst.w_count}/{cnst.w_init}\
                        \n{Fore.LIGHTRED_EX}{entity.name}{cnst.SPECIAL_COLOR}: {entity.entity_w_count}/{entity.entity_w_init}")

                if entity.entity_w_count <= 0:  # if the enemy is dead
                    break

                elif cnst.w_count <= 0:  # if the player is dead
                    print(
                        f"\n{gb.gameboook[cnst.setup_params['translation']]['combat_dead_info']} {Fore.LIGHTRED_EX}{entity.name}{cnst.COMBAT_COLOR}!")

                    dub_play("combat_false", 'adam', False, False, r_robin=5)
                    kill()

        pygame.mixer.music.fadeout(1500)
        get_music('main')

        print(
            f"\n{cnst.COMBAT_COLOR}{gb.gameboook[cnst.setup_params['translation']]['combat_win_info']} {Fore.LIGHTRED_EX}{entity.name}{cnst.COMBAT_COLOR}!")

        dub_play("combat_true", 'adam', False, False, r_robin=5)
        show_player_stats()

        ###########################

        if esc_possible:
            print(gb.gameboook[[cnst.setup_params['translation']]]['esc_choice'])
            odp = input(cnst.INPUT_SIGN)
            if len(odp) == 0:
                print(
                    f"{cnst.SPECIAL_COLOR}Wytrzymałość: {cnst.w_count} {cnst.INPUT_SIGN} {cnst.w_count - 2}{cnst.DEFAULT_COLOR}")
            cnst.w_count = update_variable(cnst.w_count, -2) # Use update_variable
            if escape_id: pth_selector(escape_id)
            else: jump_paragraph_xx()
        elif stay_id:
            pth_selector(stay_id)
        elif win_path: # Should be stay_id if it's main progression
             pth_selector(win_path)
        else:
            jump_paragraph_xx()
    elif win_path: # No escape possible, direct win_path
        pth_selector(win_path)
    else:
         jump_paragraph_xx()
