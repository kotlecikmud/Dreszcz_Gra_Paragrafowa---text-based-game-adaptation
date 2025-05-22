"""
"DRESZCZ" - GRA PARAGRAFOWA

Author: Jacek Ciesielski (1987)
Developer: Filip Pawłowski (2024) - filippawlowski2012@gmail.com
GitHub Repository: https://github.com/kotlecikmud/Dreszcz_Gra_Paragrafowa---text-based-game-adaptation.git
"""

import os
import time
import pygame
import subprocess
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
import gamebook as gb
import paragraphs as prg
import functions as func
import constants as cnst
from colorama import Fore, Style
import json # Added for loading save files


def main_menu():
    """Displays the main menu of the game and handles user input. Menu is not accesible during gameplay (for now, becasue I don't know how top implement it with subprocess)

    Description:
        Provides several options for the player to interact with the game:\n
        1. Continue - Provides the ability to continue a previously saved game.
        2. New game - Allows the player to begin a new game from the beginning.
        3. Load game: Provides the ability to load saved game.
        4. Game rules: Displays the submenu for rules and instructions for playing the game.
        5. Settings: Displays the submenu for several in-game settings. Allows the player to modify various game settings,
           such as language, difficulty, audio, etc.
        6. Exit the game: Terminates the game.

    Notes:
        The function continuously loops, displaying the main menu and prompting the player for input.
        It handles the user's input and performs different actions based on the selected menu option.
        Menu options can be temporairly disabled by simply commenting out desired position.
        Menu titles are retrioved from dictiopnary named infobook located in gamebook.py module.
        Game automatically displays text in right language, which can be changed in settings under language option, if player wishes so.

        There are some additional developer options, that provide user with easy testing capabilities.
        Type in main menu:
        rayman - to enable and show additional options
        mario - to disable and hide additional options

    Returns:
        None
    """

    func.log_event("main.py ENTRY POINT")

    if cnst.setup_params['enable_GUI']:
        def center_window(window, width=None, height=None):
            """Centers the given window on the screen.

            Args:
                window: The tkinter window object to center.
                width (int, optional): The width of the window. 
                                       Defaults to cnst.GUI_WINDOW_WIDTH or window's current width.
                height (int, optional): The height of the window. 
                                        Defaults to cnst.GUI_WINDOW_HEIGHT or window's current height.
            """
            window.update_idletasks() # Update dimensions
            win_width = width if width is not None else getattr(cnst, 'GUI_WINDOW_WIDTH', window.winfo_width())
            win_height = height if height is not None else getattr(cnst, 'GUI_WINDOW_HEIGHT', window.winfo_height())
            
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            
            x_coordinate = int((screen_width / 2) - (win_width / 2))
            y_coordinate = int((screen_height / 2) - (win_height / 2))
            
            window.geometry(f"{win_width}x{win_height}+{x_coordinate}+{y_coordinate}")

        def update_buttons_position(window, buttons, spacing_y=None, offset_y=0):
            """
            Positions a list of buttons in a single centered column.

            Args:
                window: The parent tkinter window or frame.
                buttons (list): A list of tkinter Button objects.
                spacing_y (int, optional): Vertical spacing between buttons. 
                                           Defaults to cnst.GUI_BUTTON_SPACING_Y or 70.
                offset_y (int): Vertical offset for the entire button group from the center.
                                 Positive values move buttons down, negative values move them up.
                                 Defaults to 0.
            """
            if not buttons:
                return

            _spacing_y = spacing_y if spacing_y is not None else getattr(cnst, 'GUI_BUTTON_SPACING_Y', 70)
            
            window.update_idletasks()  # Ensure window dimensions are up-to-date
            
            total_buttons_height = sum(button.winfo_reqheight() for button in buttons) + (len(buttons) - 1) * _spacing_y
            start_y = (window.winfo_height() / 2) - (total_buttons_height / 2) + offset_y

            current_y = start_y
            for button in buttons:
                button_width = button.winfo_reqwidth()
                x_position = (window.winfo_width() / 2) - (button_width / 2)
                button.place(x=x_position, y=current_y)
                current_y += button.winfo_reqheight() + _spacing_y

        def on_enter(event):
            """Changes button background on mouse hover."""
            hover_color = getattr(cnst, 'GUI_BUTTON_HOVER_COLOR', '#e0e0e0') # Fallback light gray
            try:
                event.widget['background'] = hover_color
            except tk.TclError: # Widget might be destroyed
                pass


        def on_leave(event):
            """Restores button background when mouse leaves."""
            bckg_color = getattr(cnst, 'GUI_BCKG_COLOR', '#c0c0c0') # Fallback standard gray
            try:
                event.widget['background'] = bckg_color
            except tk.TclError: # Widget might be destroyed
                pass

        def fade_transition(window, fade_out=True, duration=0.3, target_fps=30):
            """
            Applies a fade-in or fade-out transition to the window using an overlay.
            Fade-out makes the screen go to black.
            Fade-in makes the screen emerge from black.

            Args:
                window: The tkinter window object.
                fade_out (bool): True for fade-out (to black), False for fade-in (from black). Defaults to True.
                duration (float): The duration of the fade in seconds. Defaults to 0.3 for quicker fades.
                target_fps (int): Target frames per second for the animation. Defaults to 30.
            """
            # For fade_out (to black), overlay starts white (transparent-like) and goes to black.
            # For fade_in (from black), overlay starts black and goes to white, then disappears.
            initial_gray_val = 255 if fade_out else 0
            
            # Ensure overlay is created on the top-level window to cover everything
            top_level_window = window.winfo_toplevel()
            overlay = tk.Label(top_level_window, bg=f'#{initial_gray_val:02x}{initial_gray_val:02x}{initial_gray_val:02x}')
            overlay.place(x=0, y=0, relwidth=1, relheight=1)
            overlay.lift()

            start_time = time.time()
            num_steps = int(duration * target_fps)
            if num_steps <= 0: num_steps = 1
            sleep_interval = duration / num_steps

            for i in range(num_steps + 1):
                progress = i / num_steps # Linear progress from 0 to 1

                if fade_out:  # Overlay fades from White (255) to Black (0)
                    current_gray = int((1 - progress) * 255)
                else:  # Overlay fades from Black (0) to White (255)
                    current_gray = int(progress * 255)
                
                try:
                    overlay.configure(bg=f'#{current_gray:02x}{current_gray:02x}{current_gray:02x}')
                    top_level_window.update_idletasks()
                except tk.TclError: # Window or overlay might have been destroyed
                    return # End transition if widget is gone
                
                time.sleep(sleep_interval)

            if not fade_out:  # If fading IN, destroy the overlay (now white) to reveal content
                try:
                    overlay.destroy()
                except tk.TclError:
                    pass # Overlay might have been destroyed already
            # For fade_out, the overlay (now black) remains, obscuring the window content.
            # It should be manually destroyed or covered by the next screen.

        def create_button(window, text, command, state=tk.NORMAL, width=None, font_size=None, style="default"):
            """
            Creates a styled button for the GUI, allowing for different styles.

            Args:
                window: The parent tkinter window or frame.
                text (str): The text to display on the button.
                command (callable): The function to call when the button is clicked.
                state (tk.NORMAL, tk.DISABLED, etc.): The initial state of the button. Defaults to tk.NORMAL.
                width (int, optional): Specific width for the button in text units. 
                                       If None, width is determined by text length. Defaults to None.
                font_size (int, optional): Font size for the button text. 
                                           Defaults to cnst.GUI_FONT_SIZE_BUTTON or 24.
                style (str): "default", "small", "back_button", etc. (Currently only affects font size if not default)
                             Future: Could load different color schemes or padding based on style.

            Returns:
                tkinter.Button: The created button object.
            """
            # Default values from constants or fallbacks
            bckg_color = getattr(cnst, 'GUI_BCKG_COLOR', '#c0c0c0')
            font_color = getattr(cnst, 'GUI_FONT_COLOR', '#000000')
            active_color = getattr(cnst, 'GUI_BUTTON_ACTIVE_COLOR', '#a0a0a0')
            main_font_family = getattr(cnst, 'GUI_MAIN_FONT', 'Georgia')
            default_font_size = getattr(cnst, 'GUI_FONT_SIZE_BUTTON', 24)
            
            current_font_size = font_size if font_size is not None else default_font_size
            if style == "small": # Example of style-specific modification
                current_font_size = font_size if font_size is not None else getattr(cnst, 'GUI_FONT_SIZE_SMALL_BUTTON', 18)
            elif style == "back_button":
                 current_font_size = font_size if font_size is not None else getattr(cnst, 'GUI_FONT_SIZE_BACK_BUTTON', 20)


            button = Button(window,
                            text=text,
                            font=(main_font_family, current_font_size, "italic"),
                            bg=bckg_color,
                            fg=font_color,
                            relief=getattr(cnst, 'GUI_BUTTON_RELIEF', 'raised'), 
                            activebackground=active_color,
                            command=command,
                            state=state,
                            width=width,
                            padx=getattr(cnst, 'GUI_BUTTON_PADDING_X', 10),
                            pady=getattr(cnst, 'GUI_BUTTON_PADDING_Y', 5))
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)
            return button

        def set_background(window, image_filename="menu_background.png"):
            """
            Sets the background image for the given window.

            Args:
                window: The tkinter window object.
                image_filename (str): The filename of the background image located in
                                      cnst.GRAPHICS_PLATES_DIR. Defaults to "menu_background.png".

            Returns:
                tkinter.Label or None: The background label widget if successful, None otherwise.
            """
            try:
                graphics_dir = getattr(cnst, 'GRAPHICS_PLATES_DIR', 'Assets/Graphics/plates')
                image_path = os.path.join(graphics_dir, image_filename)

                if not os.path.exists(image_path):
                    func.log_event(f"Error: Background image not found at {image_path}", event_type="ERROR")
                    fallback_bg = getattr(cnst, 'GUI_BCKG_COLOR', '#333333')
                    window.configure(bg=fallback_bg)
                    return None

                win_width = getattr(cnst, 'GUI_WINDOW_WIDTH', window.winfo_width())
                win_height = getattr(cnst, 'GUI_WINDOW_HEIGHT', window.winfo_height())
                if win_width <= 1 or win_height <= 1: # Window not yet sized
                    win_width = getattr(cnst, 'GUI_WINDOW_WIDTH', 512) # Default if not sized
                    win_height = getattr(cnst, 'GUI_WINDOW_HEIGHT', 512)


                background_image = Image.open(image_path)
                background_image = background_image.resize((win_width, win_height), Image.Resampling.LANCZOS)
                background_photo = ImageTk.PhotoImage(background_image)

                # If a background label already exists, update it. Otherwise, create it.
                # This requires storing the label, e.g., on the window object, or finding it.
                # For simplicity, we'll destroy old ones if any, assuming clear_window isn't selective.
                # A more robust way would be to pass a persistent label if updates are frequent.
                
                # Check if a label with 'background_label' name exists and destroy it
                for child in window.winfo_children():
                    if child.winfo_name() == 'background_label_widget':
                        child.destroy()
                        break

                background_label = tk.Label(window, image=background_photo, name='background_label_widget')
                background_label.image = background_photo  # Keep a reference
                background_label.place(x=0, y=0, relwidth=1, relheight=1)
                background_label.lower() 
                return background_label
            except Exception as e:
                func.log_event(f"Error setting background for {image_filename}: {e}", event_type="ERROR")
                fallback_bg = getattr(cnst, 'GUI_BCKG_COLOR', '#333333')
                try:
                    window.configure(bg=fallback_bg)
                except tk.TclError: # Window might be destroyed
                    pass
                return None

        def clear_window(window):
            """
            Removes all widgets from the given window.
            If a special background label (named 'background_label_widget') exists and
            we want to preserve it across clears (e.g. if it's managed by a higher level),
            this function would need to be smarter. For now, it clears everything.

            Args:
                window: The tkinter window object.
            """
            children = list(window.winfo_children()) # Make a copy as list changes during iteration
            for widget in children:
                try:
                    widget.destroy()
                except tk.TclError:
                    # Widget might have been destroyed already by cascading destroys
                    pass

        # --- Translation Helper ---
        _translation_cache = {} # Cache for gamebook/infobook texts

        def _get_gui_text(key, book_type='infobook', fallback_text=""):
            """
            Fetches text from gb.infobook or gb.gameboook based on current translation.
            Caches results for minor efficiency.
            """
            if key in _translation_cache and _translation_cache[key]['lang'] == cnst.setup_params.get('translation'):
                return _translation_cache[key]['text']

            translation_id = cnst.setup_params.get('translation')
            source_book = None
            if book_type == 'infobook':
                source_book = getattr(gb, 'infoboook', {})
            elif book_type == 'gamebook':
                source_book = getattr(gb, 'gameboook', {})

            text_to_return = fallback_text
            if source_book and translation_id and isinstance(source_book, dict) and \
               translation_id in source_book and isinstance(source_book[translation_id], dict):
                text_to_return = source_book[translation_id].get(key, fallback_text)
            
            _translation_cache[key] = {'lang': translation_id, 'text': text_to_return}
            return text_to_return

        # --- New Game Sequence Functions ---
        def show_new_game_difficulty_selection(window):
            """Displays screen for selecting game difficulty."""
            fade_transition(window, fade_out=True, duration=0.1)
            clear_window(window)
            set_background(window)

            title_text = _get_gui_text('difficulty_title', 'infobook', "Select Difficulty")
            Label(window, text=title_text, font=(cnst.GUI_MAIN_FONT, 30, "bold"), 
                  bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', cnst.GUI_BCKG_COLOR), 
                  fg=getattr(cnst, 'GUI_FONT_COLOR_TITLE', cnst.GUI_FONT_COLOR)).pack(pady=(30, 20))

            difficulty_frame = Frame(window, bg=getattr(cnst, 'GUI_BCKG_COLOR', '#c0c0c0'))
            difficulty_frame.pack(pady=20)
            
            # Difficulties: Key from cnst.difficulty_levels, Text for button
            difficulties_map = {
                "easy": _get_gui_text('difficulty_easy', 'infobook', "Easy"),
                "medium": _get_gui_text('difficulty_medium', 'infobook', "Normal"),
                "hard": _get_gui_text('difficulty_hard', 'infobook', "Hard"),
            }

            buttons = []
            for diff_key, diff_text in difficulties_map.items():
                # Pass the key (e.g., "easy") to the next screen
                btn = create_button(difficulty_frame, diff_text, 
                                    lambda k=diff_key: show_elixir_choice_screen(window, k),
                                    style="default")
                btn.pack(pady=10, ipadx=10, ipady=5)
                buttons.append(btn)

            back_btn_text = _get_gui_text('back_button', 'infobook', "Back")
            back_button = create_button(window, back_btn_text, 
                                        lambda: show_main_menu(window), style="back_button")
            back_button.place(relx=0.05, rely=0.95, anchor=SW)
            
            fade_transition(window, fade_out=False)

        def show_elixir_choice_screen(window, selected_difficulty_key):
            """Displays screen for choosing an elixir after difficulty selection."""
            fade_transition(window, fade_out=True, duration=0.1)
            clear_window(window)
            set_background(window)

            title_text = _get_gui_text('elixir_choice_title', 'infobook', "Choose Your Elixir")
            Label(window, text=title_text, font=(cnst.GUI_MAIN_FONT, 30, "bold"),
                  bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', cnst.GUI_BCKG_COLOR), 
                  fg=getattr(cnst, 'GUI_FONT_COLOR_TITLE', cnst.GUI_FONT_COLOR)).pack(pady=(30,10))

            intro_text_00a = _get_gui_text('00a', 'gamebook', 
                                         "Before you venture forth, choose an elixir to aid you:")
            Label(window, text=intro_text_00a, font=(cnst.GUI_MAIN_FONT, 16), wraplength=cnst.GUI_WINDOW_WIDTH - 100,
                  bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', cnst.GUI_BCKG_COLOR),
                  fg=cnst.GUI_FONT_COLOR).pack(pady=(0, 20))

            elixir_var = tk.StringVar(value='z') # Default to Dexterity ('z')

            # Elixir names from gb.gameboook[...]['elxr_chc']
            # Default: ["Eliksir Zręczności", "Eliksir Wytrzymałości", "Eliksir Szczęścia"]
            elixir_choices_text = _get_gui_text('elxr_chc', 'gamebook', 
                                                ["Dexterity Elixir", "Endurance Elixir", "Luck Elixir"])
            if not isinstance(elixir_choices_text, list) or len(elixir_choices_text) < 3:
                 elixir_choices_text = ["Dexterity Elixir", "Endurance Elixir", "Luck Elixir"] # Fallback

            elixir_options = [
                (elixir_choices_text[0], 'z'), # Zręczność
                (elixir_choices_text[1], 'w'), # Wytrzymałość
                (elixir_choices_text[2], 's')  # Szczęście
            ]
            
            radio_frame = Frame(window, bg=getattr(cnst, 'GUI_BCKG_COLOR', '#c0c0c0'))
            radio_frame.pack(pady=10)

            for text, value in elixir_options:
                rb = tk.Radiobutton(radio_frame, text=text, variable=elixir_var, value=value,
                                    font=(cnst.GUI_MAIN_FONT, 18), 
                                    bg=getattr(cnst, 'GUI_BCKG_COLOR_RADIO', cnst.GUI_BCKG_COLOR),
                                    fg=cnst.GUI_FONT_COLOR, 
                                    selectcolor=getattr(cnst, 'GUI_RADIO_SELECT_COLOR', '#555555'),
                                    activebackground=getattr(cnst, 'GUI_BCKG_COLOR_RADIO_ACTIVE', cnst.GUI_BCKG_COLOR),
                                    activeforeground=cnst.GUI_FONT_COLOR,
                                    indicatoron=0, # Makes it look more like a button
                                    relief='raised',
                                    padx=15, pady=8,
                                    width=20,
                                    anchor='w')
                rb.pack(pady=5, fill='x')


            confirm_btn_text = _get_gui_text('confirm_elixir_button', 'infobook', "Start Adventure")
            confirm_button = create_button(window, confirm_btn_text, 
                                           lambda: _confirm_elixir_and_start_game(window, selected_difficulty_key, elixir_var.get()),
                                           style="default")
            confirm_button.pack(pady=20, ipady=5)

            back_btn_text = _get_gui_text('back_button', 'infobook', "Back")
            back_button = create_button(window, back_btn_text, 
                                        lambda: show_new_game_difficulty_selection(window), style="back_button")
            back_button.place(relx=0.05, rely=0.95, anchor=SW)

            fade_transition(window, fade_out=False)

        def _confirm_elixir_and_start_game(window, difficulty_key, chosen_elixir_value):
            """Sets game parameters, saves state, shows final intro, then launches console game."""
            
            # 1. Set difficulty constants
            cnst.difficulty = difficulty_key # "easy", "medium", or "hard"
            cnst.entity_hit_mult = cnst.difficulty_levels.get(difficulty_key, cnst.difficulty_levels["medium"])
            func.log_event(f"Difficulty set to: {cnst.difficulty} (Multiplier: {cnst.entity_hit_mult})")

            # 2. Set chosen potion
            cnst.potion = chosen_elixir_value
            func.log_event(f"Elixir chosen: {cnst.potion}")

            # 3. Initialize and save game state (includes resetting player stats for new game)
            func.get_game_state('s', new_game=True) 
            func.log_event("New game state initialized and saved.")

            # 4. UI Feedback: Show final intro text
            fade_transition(window, fade_out=True, duration=0.2)
            clear_window(window)
            set_background(window)
            
            intro_text_00b = _get_gui_text('00b', 'gamebook', "Your adventure begins...")
            Label(window, text=intro_text_00b, font=(cnst.GUI_MAIN_FONT, 18, "italic"), wraplength=cnst.GUI_WINDOW_WIDTH - 50,
                  bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', cnst.GUI_BCKG_COLOR),
                  fg=cnst.GUI_FONT_COLOR).pack(pady=(50, 20))
            
            start_msg = _get_gui_text('game_starting_console_msg', 'infobook', "Game starting in console...")
            Label(window, text=start_msg, font=(cnst.GUI_MAIN_FONT, 16),
                  bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', cnst.GUI_BCKG_COLOR),
                  fg=cnst.GUI_FONT_COLOR).pack(pady=20)
            
            fade_transition(window, fade_out=False, duration=0.2)
            window.update_idletasks()

            # 5. Close GUI and launch console game
            def launch_game():
                try:
                    if window.winfo_exists(): # Check if window still exists
                        window.destroy()
                except tk.TclError:
                    pass # Window might already be gone
                
                # This is the crucial call to start the console-based game from paragraph 01
                try:
                    func.pth_selector(actions=['01'])
                except Exception as e:
                    # Fallback if pth_selector fails catastrophically
                    # This is tricky because the GUI is gone. Log and exit.
                    print(f"CRITICAL ERROR trying to start game via pth_selector: {e}")
                    func.error_message(str(e), "CRITICAL: Failed to launch pth_selector from GUI")
                    # Attempt to show main menu in console as a last resort if GUI failed before this.
                    # However, if pth_selector itself fails, the game might be in an unstable state.
                    # For now, just exit.
                    exit(1) # Exit with an error code

            # Schedule the launch_game function to run after a delay
            # This allows the user to see the "Game starting..." message.
            window.after(2500, launch_game) # 2.5 seconds delay

from tkinter import ttk, messagebox # Added for Combobox, Scale, messagebox

        # Store references to Tkinter control variables (StringVar, BooleanVar, etc.)
        settings_vars = {}

        def _save_settings_action(window_ref, refresh_ui=False):
            """Saves all current settings from control variables to cnst and config file."""
            global settings_vars
            func.log_event("Attempting to save settings from GUI.")

            # Language
            if 'language' in settings_vars:
                selected_lang_code = settings_vars['language'].get()
                if cnst.setup_params.get('translation') != selected_lang_code:
                    cnst.setup_params['translation'] = selected_lang_code
                    gb.get_translation(selected_lang_code) # Update runtime translation
                    _translation_cache.clear() # Clear text cache
                    func.log_event(f"Language changed to: {selected_lang_code}")
            
            # Difficulty
            if 'difficulty' in settings_vars:
                selected_difficulty_key = settings_vars['difficulty'].get() # This should store 'easy', 'medium', 'hard'
                cnst.setup_params['difficulty_level'] = selected_difficulty_key
                cnst.difficulty = selected_difficulty_key # Ensure cnst.difficulty is also updated
                cnst.entity_hit_mult = cnst.difficulty_levels.get(selected_difficulty_key, cnst.difficulty_levels["medium"])
                func.log_event(f"Difficulty level set to: {selected_difficulty_key}")

            # Sound Volumes
            volume_types = ['action_volume', 'sfx_volume', 'bckg_volume']
            for vol_type in volume_types:
                if vol_type in settings_vars:
                    # Scale widgets might store float or int, ensure float division
                    new_volume = float(settings_vars[vol_type].get()) / 100.0 
                    cnst.setup_params[vol_type] = new_volume
                    if vol_type == 'bckg_volume' and pygame.mixer.get_init():
                        pygame.mixer.music.set_volume(new_volume)
                    func.log_event(f"{vol_type} set to: {new_volume}")
            
            # Character Name
            if 'player_name' in settings_vars:
                current_name = settings_vars['player_name'].get().strip()
                if not current_name and (not cnst.player_name or cnst.player_name == _get_gui_text('default_player_name', 'infobook', "Adventurer")):
                    current_name = func.name_randomizer()
                    settings_vars['player_name'].set(current_name) # Update Entry widget as well
                cnst.player_name = current_name
                cnst.setup_params['player_name'] = current_name # Ensure it's saved in setup_params too
                func.log_event(f"Player name set to: {current_name}")

            # Dev Mode Toggles
            dev_toggle_keys = ['debug_msg', 'use_dummy', 'logging', 'start_sequence', 
                               'manual_battle', 'dubbing', 'get_music', 'enable_GUI']
            for key in dev_toggle_keys:
                if key in settings_vars:
                    cnst.setup_params[key] = settings_vars[key].get()
                    func.log_event(f"Dev toggle {key} set to: {cnst.setup_params[key]}")
            
            try:
                func.update_config_file()
                func.log_event("Settings saved to config file.")
                if not refresh_ui: # Don't show if we are about to redraw the whole UI
                     messagebox.showinfo(_get_gui_text("settings_saved_title", "infobook", "Settings Saved"),
                                        _get_gui_text("settings_saved_msg", "infobook", "Your settings have been saved."),
                                        parent=window_ref)
            except Exception as e:
                func.error_message(str(e), "Error saving settings")
                messagebox.showerror(_get_gui_text("settings_save_error_title", "infobook", "Save Error"),
                                     _get_gui_text("settings_save_error_msg", "infobook", f"Could not save settings: {e}"),
                                     parent=window_ref)

            if refresh_ui:
                show_settings_ui(window_ref)


        def _save_and_go_back(window_ref):
            global settings_vars
            _save_settings_action(window_ref, refresh_ui=False) # Save without refresh, then go back
            show_main_menu(window_ref)


        def settings(window): # Renamed from 'settings' to 'show_settings_ui' conceptually, actual 'settings' is this
            """Displays the main settings UI with various controls."""
            global settings_vars
            settings_vars = {} # Reset for this screen instance

            fade_transition(window, fade_out=True, duration=0.1)
            clear_window(window)
            set_background(window)

            # --- Main Title ---
            title_lbl = Label(window, text=_get_gui_text('Mmenu4', 'infobook', "Settings"), 
                  font=(cnst.GUI_MAIN_FONT, 30, "bold"),
                  bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', cnst.GUI_BCKG_COLOR),
                  fg=getattr(cnst, 'GUI_FONT_COLOR_TITLE', cnst.GUI_FONT_COLOR))
            title_lbl.pack(pady=(15, 10))

            # --- Bottom Buttons Frame (Save, Back) ---
            bottom_frame = Frame(window, bg=getattr(cnst, 'GUI_BCKG_COLOR', '#333333'))
            bottom_frame.pack(side=BOTTOM, fill=X, pady=10, padx=20)

            save_btn = create_button(bottom_frame, _get_gui_text('save_settings_btn', 'infobook', "Save Settings"),
                                     lambda: _save_settings_action(window, refresh_ui=True), style="default")
            save_btn.pack(side=LEFT, padx=(0,10), expand=True)
            
            back_btn = create_button(bottom_frame, _get_gui_text('back_button', 'infobook', "Back to Menu"),
                                     lambda: _save_and_go_back(window), style="back_button")
            back_btn.pack(side=RIGHT, padx=(10,0), expand=True)
            
            # --- Scrollable Area for Settings ---
            canvas_frame = Frame(window, bg=getattr(cnst, 'GUI_BCKG_COLOR', '#333333'))
            canvas_frame.pack(fill=BOTH, expand=True, padx=20, pady=5)

            settings_canvas = Canvas(canvas_frame, bg=getattr(cnst, 'GUI_SCROLL_CANVAS_BG', '#444444'), highlightthickness=0)
            scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=settings_canvas.yview)
            scrollable_content_frame = Frame(settings_canvas, bg=getattr(cnst, 'GUI_SCROLL_FRAME_BG', '#444444'))

            scrollable_content_frame.bind("<Configure>", lambda e: settings_canvas.configure(scrollregion=settings_canvas.bbox("all")))
            canvas_window_id = settings_canvas.create_window((0, 0), window=scrollable_content_frame, anchor="nw")
            
            def _configure_canvas_window(event): # Ensure content frame matches canvas width
                 settings_canvas.itemconfig(canvas_window_id, width=event.width)
            settings_canvas.bind("<Configure>", _configure_canvas_window)

            settings_canvas.configure(yscrollcommand=scrollbar.set)
            settings_canvas.pack(side=LEFT, fill=BOTH, expand=True)
            scrollbar.pack(side=RIGHT, fill=Y)
            # --- End Scrollable Area ---

            # Helper to create a consistent setting row
            def create_setting_row(parent, label_text):
                row_frame = Frame(parent, bg=getattr(cnst, 'GUI_SCROLL_FRAME_BG', '#444444'), pady=5)
                row_frame.pack(fill=X, padx=10)
                label = Label(row_frame, text=label_text, font=(cnst.GUI_MAIN_FONT, 16), 
                              bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', parent.cget('bg')), 
                              fg=cnst.GUI_FONT_COLOR, width=20, anchor='w') # Fixed width for alignment
                label.pack(side=LEFT, padx=(0,10))
                return row_frame

            # --- Language Setting ---
            lang_frame = create_setting_row(scrollable_content_frame, _get_gui_text('Mmenu4_sub1', 'infobook', "Language:"))
            lang_map = {"en": "English", "pl": "Polski"} # Should be dynamically from gb.infobook if more langs
            available_langs_display = [lang_map.get(k, k) for k in gb.infoboook.keys() if isinstance(gb.infoboook.get(k), dict)]
            lang_codes = [k for k in gb.infoboook.keys() if isinstance(gb.infoboook.get(k), dict)]
            
            settings_vars['language_display'] = tk.StringVar()
            settings_vars['language'] = tk.StringVar() # To store actual code 'en', 'pl'

            current_lang_code = cnst.setup_params.get('translation', 'en')
            settings_vars['language'].set(current_lang_code)
            settings_vars['language_display'].set(lang_map.get(current_lang_code, current_lang_code))

            lang_combo = ttk.Combobox(lang_frame, textvariable=settings_vars['language_display'], 
                                     values=available_langs_display, state="readonly", width=25,
                                     font=(cnst.GUI_MAIN_FONT, 14))
            lang_combo.pack(side=LEFT, fill=X, expand=True)
            
            def _on_lang_select(event): # Update the actual code var when display name changes
                selected_display_name = settings_vars['language_display'].get()
                for code, display in lang_map.items():
                    if display == selected_display_name:
                        settings_vars['language'].set(code)
                        break
            lang_combo.bind("<<ComboboxSelected>>", _on_lang_select)


            # --- Difficulty Setting ---
            diff_frame = create_setting_row(scrollable_content_frame, _get_gui_text('Mmenu4_sub2', 'infobook', "Difficulty:"))
            difficulty_map = { # Storing key -> display_text
                "easy": _get_gui_text('difficulty_easy', 'infobook', "Easy"),
                "medium": _get_gui_text('difficulty_medium', 'infobook', "Normal"),
                "hard": _get_gui_text('difficulty_hard', 'infobook', "Hard")
            }
            settings_vars['difficulty_display'] = tk.StringVar() # For display in combobox
            settings_vars['difficulty'] = tk.StringVar() # For actual key 'easy', 'medium', 'hard'
            
            current_diff_key = cnst.setup_params.get('difficulty_level', 'medium')
            settings_vars['difficulty'].set(current_diff_key)
            settings_vars['difficulty_display'].set(difficulty_map.get(current_diff_key, "Normal"))

            diff_combo = ttk.Combobox(diff_frame, textvariable=settings_vars['difficulty_display'], 
                                      values=list(difficulty_map.values()), state="readonly", width=25,
                                      font=(cnst.GUI_MAIN_FONT, 14))
            diff_combo.pack(side=LEFT, fill=X, expand=True)

            def _on_diff_select(event):
                selected_display_name = settings_vars['difficulty_display'].get()
                for key, display in difficulty_map.items():
                    if display == selected_display_name:
                        settings_vars['difficulty'].set(key)
                        break
            diff_combo.bind("<<ComboboxSelected>>", _on_diff_select)


            # --- Character Name ---
            name_frame = create_setting_row(scrollable_content_frame, _get_gui_text('Mmenu4_sub4', 'infobook', "Character Name:"))
            settings_vars['player_name'] = tk.StringVar(value=cnst.player_name if cnst.player_name else _get_gui_text('default_player_name', 'infobook', "Adventurer"))
            name_entry = tk.Entry(name_frame, textvariable=settings_vars['player_name'], width=27,
                                  font=(cnst.GUI_MAIN_FONT, 14))
            name_entry.pack(side=LEFT, fill=X, expand=True)


            # --- Sound Settings Section Title ---
            sound_title_lbl = Label(scrollable_content_frame, text=_get_gui_text('Mmenu4_sub3', 'infobook', "Sound Volumes"), 
                                    font=(cnst.GUI_MAIN_FONT, 18, "bold"), anchor='w',
                                    bg=getattr(cnst, 'GUI_SCROLL_FRAME_BG', '#444444'), fg=cnst.GUI_FONT_COLOR)
            sound_title_lbl.pack(fill=X, padx=10, pady=(15,5))

            # Volume Sliders (Dialogs, SFX, Music)
            volume_configs = [
                ('Mmenu4_sub3_1', 'action_volume', "Dialogs"), # Dialogs
                ('Mmenu4_sub3_2', 'sfx_volume', "Sound Effects"),    # Effects
                ('Mmenu4_sub3_3', 'bckg_volume', "Music")     # Music
            ]
            for label_key, param_key, fallback_label in volume_configs:
                vol_frame = create_setting_row(scrollable_content_frame, _get_gui_text(label_key, 'infobook', fallback_label)+":")
                current_val = int(cnst.setup_params.get(param_key, 0.8) * 100) # Scale 0-100
                settings_vars[param_key] = tk.IntVar(value=current_val)
                
                # Value Label
                val_label = Label(vol_frame, textvariable=settings_vars[param_key], width=4,
                                  font=(cnst.GUI_MAIN_FONT, 14), anchor='e',
                                  bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', vol_frame.cget('bg')), fg=cnst.GUI_FONT_COLOR)
                val_label.pack(side=RIGHT, padx=(5,0))

                scale = tk.Scale(vol_frame, from_=0, to=100, orient=HORIZONTAL, showvalue=0,
                                 variable=settings_vars[param_key], length=200, resolution=1,
                                 bg=getattr(cnst, 'GUI_SCALE_BG', '#C0C0C0'), 
                                 troughcolor=getattr(cnst, 'GUI_SCALE_TROUGH', '#808080'),
                                 activebackground=getattr(cnst, 'GUI_SCALE_ACTIVE_BG', '#A0A0A0'),
                                 highlightthickness=0)
                if param_key == 'bckg_volume' and pygame.mixer.get_init(): # Immediate feedback for music
                    scale.config(command=lambda v, pk=param_key: pygame.mixer.music.set_volume(float(settings_vars[pk].get()) / 100.0))
                elif param_key == 'sfx_volume': # Immediate feedback for SFX
                    def _sfx_scale_change(v): # v is current scale value as string
                        pygame.mixer.Sound(os.path.join(cnst.AUDIO_FX_DIR, "audiobook_click_snd.mp3")).set_volume(float(v) / 100.0)
                        pygame.mixer.Sound(os.path.join(cnst.AUDIO_FX_DIR, "audiobook_click_snd.mp3")).play()
                    scale.config(command=_sfx_scale_change)

                scale.pack(side=LEFT, fill=X, expand=True)

            # --- Other Buttons (Randomize Attr, Check Updates) ---
            action_buttons_frame = Frame(scrollable_content_frame, bg=getattr(cnst, 'GUI_SCROLL_FRAME_BG', '#444444'), pady=10)
            action_buttons_frame.pack(fill=X, padx=10, pady=(15,5))

            # Randomize Attributes
            s_val, w_val, z_val = tk.StringVar(), tk.StringVar(), tk.StringVar()
            def _update_attr_labels():
                s_val.set(f"S: {cnst.s_count}")
                w_val.set(f"W: {cnst.w_count}")
                z_val.set(f"Z: {cnst.z_count}")
            _update_attr_labels()

            attr_frame = Frame(action_buttons_frame, bg=getattr(cnst, 'GUI_SCROLL_FRAME_BG', '#444444'))
            attr_frame.pack(fill=X, pady=5)
            rand_attr_btn = create_button(attr_frame, _get_gui_text('Mmenu4_sub5', 'infobook', "Randomize Attributes"),
                                       lambda: (func.get_player_par(force_random=True), _update_attr_labels()), style="default")
            rand_attr_btn.pack(side=LEFT, padx=(0,10))
            
            attr_display_frame = Frame(attr_frame, bg=getattr(cnst, 'GUI_SCROLL_FRAME_BG', '#444444'))
            attr_display_frame.pack(side=LEFT)
            Label(attr_display_frame, textvariable=s_val, font=(cnst.GUI_MAIN_FONT, 12), bg=attr_display_frame.cget('bg'), fg=cnst.GUI_FONT_COLOR).pack(side=LEFT, padx=3)
            Label(attr_display_frame, textvariable=w_val, font=(cnst.GUI_MAIN_FONT, 12), bg=attr_display_frame.cget('bg'), fg=cnst.GUI_FONT_COLOR).pack(side=LEFT, padx=3)
            Label(attr_display_frame, textvariable=z_val, font=(cnst.GUI_MAIN_FONT, 12), bg=attr_display_frame.cget('bg'), fg=cnst.GUI_FONT_COLOR).pack(side=LEFT, padx=3)


            # Check for Updates
            updates_frame = Frame(action_buttons_frame, bg=getattr(cnst, 'GUI_SCROLL_FRAME_BG', '#444444'))
            updates_frame.pack(fill=X, pady=5)
            update_btn = create_button(updates_frame, _get_gui_text('Mmenu4_sub6', 'infobook', "Check for Updates"),
                                     lambda: messagebox.showinfo(
                                         _get_gui_text('update_check_title', 'infobook', "Update Check"),
                                         func.check_for_update(), parent=window), 
                                     style="default")
            update_btn.pack(side=LEFT)

            # --- Dev Mode Toggles (Conditional) ---
            if cnst.setup_params.get('dev_mode', False):
                dev_title_lbl = Label(scrollable_content_frame, text=_get_gui_text('dev_options_title', 'infobook', "Developer Options"), 
                                    font=(cnst.GUI_MAIN_FONT, 18, "bold"), anchor='w',
                                    bg=getattr(cnst, 'GUI_SCROLL_FRAME_BG', '#444444'), fg=cnst.GUI_FONT_COLOR)
                dev_title_lbl.pack(fill=X, padx=10, pady=(20,5))

                dev_toggle_keys_map = { # param_key: Label Text Key
                    'debug_msg': 'dev_debug_msg', 'use_dummy': 'dev_use_dummy', 
                    'logging': 'dev_logging', 'start_sequence': 'dev_start_sequence',
                    'manual_battle': 'dev_manual_battle', 'dubbing': 'dev_dubbing', 
                    'get_music': 'dev_get_music', 'enable_GUI': 'dev_enable_gui'
                }
                # Create two columns for dev toggles
                dev_cols_frame = Frame(scrollable_content_frame, bg=getattr(cnst, 'GUI_SCROLL_FRAME_BG', '#444444'))
                dev_cols_frame.pack(fill=X, padx=10)
                dev_col1 = Frame(dev_cols_frame, bg=getattr(cnst, 'GUI_SCROLL_FRAME_BG', '#444444'))
                dev_col1.pack(side=LEFT, fill=X, expand=True, anchor=N)
                dev_col2 = Frame(dev_cols_frame, bg=getattr(cnst, 'GUI_SCROLL_FRAME_BG', '#444444'))
                dev_col2.pack(side=RIGHT, fill=X, expand=True, anchor=N)
                
                col_idx = 0
                for key, label_key in dev_toggle_keys_map.items():
                    parent_col = dev_col1 if col_idx % 2 == 0 else dev_col2
                    settings_vars[key] = tk.BooleanVar(value=cnst.setup_params.get(key, False))
                    chk = tk.Checkbutton(parent_col, text=_get_gui_text(label_key, 'infobook', key.replace('_', ' ').title()),
                                         variable=settings_vars[key], font=(cnst.GUI_MAIN_FONT, 12), anchor='w',
                                         bg=getattr(cnst, 'GUI_CHECKBUTTON_BG', parent_col.cget('bg')), 
                                         fg=cnst.GUI_FONT_COLOR, 
                                         selectcolor=getattr(cnst, 'GUI_CHECKBUTTON_SELECT', '#555555'),
                                         activebackground=getattr(cnst, 'GUI_CHECKBUTTON_ACTIVE_BG', parent_col.cget('bg')))
                    chk.pack(fill=X, pady=2)
                    col_idx +=1
            
            # Ensure scroll region is updated after all widgets are packed
            scrollable_content_frame.update_idletasks()
            settings_canvas.config(scrollregion=settings_canvas.bbox("all"))

            fade_transition(window, fade_out=False)


        def show_not_implemented(window, option):
            label = Label(window, text=f"{option}: Not implemented", bg='black', fg='white',
                          font=(cnst.GUI_MAIN_FONT, 18))
            label.place(relx=0.5, rely=0.5, anchor=CENTER)
            window.after(1000, label.destroy)

        def exit_game(window):
            fade_transition(window)
            clear_window(window)
            set_background(window)

            exit_frame = Frame(window, bg=cnst.GUI_BCKG_COLOR)
            exit_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

            Label(exit_frame, text="Are you sure you want to exit?", font=(cnst.GUI_MAIN_FONT, 18),
                  bg=cnst.GUI_BCKG_COLOR).pack(pady=20)

            yes_button = create_button(exit_frame, "Yes", lambda: exit(0))
            no_button = create_button(exit_frame, "No", lambda: show_main_menu(window))

            yes_button.pack(side=LEFT, padx=10)
            no_button.pack(side=LEFT, padx=10)

            fade_transition(window, fade_out=False)

        def execute_load_game(window, save_filename):
            save_file_path = os.path.join(cnst.GAMESTATE_DIR, save_filename)
            cnst.setup_params['active_gameplay'] = save_file_path
            func.log_event(f"Attempting to load game: {save_filename}")

            try:
                with open(save_file_path, "r") as f:
                    game_state = json.load(f)
            except Exception as e:
                func.error_message(str(e), f"Error loading save file {save_filename}")
                fade_transition(window)
                clear_window(window)
                set_background(window)
                Label(window, text=f"Error loading file: {save_filename}", font=(cnst.GUI_MAIN_FONT, 18), bg=cnst.GUI_BCKG_COLOR, fg="white").pack(pady=20)
                create_button(window, "Back", lambda: load_game_action(window)).pack(pady=10)
                fade_transition(window, fade_out=False)
                return

            cnst.player_name = game_state.get("player_name", "Unknown Player")
            
            difficulty_setting_loaded = game_state.get("difficulty_setting", "Normal").lower()
            cnst.difficulty = difficulty_setting_loaded 
            cnst.entity_hit_mult = cnst.difficulty_levels.get(cnst.difficulty, cnst.difficulty_levels["medium"])
            func.log_event(f"Loaded game with difficulty setting: {cnst.difficulty} (multiplier: {cnst.entity_hit_mult})")

            cnst.s_count = game_state.get("s_count", 10)
            cnst.w_count = game_state.get("w_count", 20)
            cnst.z_count = game_state.get("z_count", 10)
            cnst.s_init = game_state.get("s_init", 10)
            cnst.w_init = game_state.get("w_init", 20)
            cnst.z_init = game_state.get("z_init", 10)
            cnst.main_eq = game_state.get("equipment", {})
            cnst.potion = game_state.get("potion")
            cnst.potion_count = game_state.get("potion_count", 0)
            cnst.meal_count = game_state.get("meal_count", 0)
            cnst.gold_amount = game_state.get("gold_amount", 0)
            start_paragraph = game_state.get("last_paragraph", "00")
            
            func.update_config_file()

            fade_transition(window)
            clear_window(window)
            set_background(window)
            Label(window, text=f"Loading game {save_filename}...", font=(cnst.GUI_MAIN_FONT, 18), bg=cnst.GUI_BCKG_COLOR, fg="white").pack(pady=20)
            window.update_idletasks()
            time.sleep(1)
            window.withdraw()
            try:
                func.pth_selector([], [f'{start_paragraph}'])
            except Exception as e:
                func.error_message(str(e), f"Error during game execution from {start_paragraph}")
                if window.winfo_exists():
                    window.deiconify()
                show_main_menu(window)
            else:
                exit(0)

        # --- START OF NEW ACTION STUBS ---
        def new_game_action(window):
            # This is the entry point for "New Game" from the main menu.
            # It now calls the first screen of the new game sequence.
            show_new_game_difficulty_selection(window)

        def continue_game_action(window):
            """Handles the action for the 'Continue' button in the GUI."""
            func.log_event("GUI: 'Continue' button clicked.")
            
            # Attempt to load the game state. 
            # func.get_game_state('c') loads from cnst.setup_params["active_gameplay"],
            # updates cnst variables, and returns the last_paragraph.
            last_paragraph = func.get_game_state('c')

            if last_paragraph and last_paragraph != '00': # '00' might indicate a fresh or reset state
                func.log_event(f"Successfully loaded game state. Last paragraph: {last_paragraph}. Preparing to launch console game.")
                
                fade_transition(window, fade_out=True, duration=0.2)
                clear_window(window)
                set_background(window) # Optional: can set a specific "loading" background
                
                continue_msg = _get_gui_text('continue_loading_msg', 'infobook', f"Continuing from paragraph {last_paragraph}...")
                Label(window, text=continue_msg,
                      font=(getattr(cnst, 'GUI_MAIN_FONT', 'Georgia'), 18, "italic"),
                      bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', getattr(cnst, 'GUI_BCKG_COLOR', '#333333')),
                      fg=getattr(cnst, 'GUI_FONT_COLOR', '#FFFFFF')).pack(pady=(150, 20))
                
                start_msg = _get_gui_text('game_starting_console_msg', 'infobook', "Game starting in console...")
                Label(window, text=start_msg, 
                      font=(getattr(cnst, 'GUI_MAIN_FONT', 'Georgia'), 16),
                      bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', getattr(cnst, 'GUI_BCKG_COLOR', '#333333')),
                      fg=getattr(cnst, 'GUI_FONT_COLOR', '#FFFFFF')).pack(pady=20)

                fade_transition(window, fade_out=False, duration=0.2) # Fade in the message
                window.update_idletasks()

                def launch_console_game_from_continue():
                    try:
                        if window.winfo_exists():
                            window.destroy()
                    except tk.TclError:
                        pass # Window might already be gone
                    
                    try:
                        func.pth_selector(actions=[f'{last_paragraph}'])
                    except Exception as e:
                        # This is a critical failure post-GUI. Log and exit.
                        print(f"CRITICAL ERROR trying to start continued game via pth_selector: {e}")
                        func.error_message(str(e), "CRITICAL: Failed to launch pth_selector for continued game")
                        exit(1) # Exit with an error code

                window.after(2000, launch_console_game_from_continue) # 2-second delay

            else:
                # This case should ideally be rare if the "Continue" button is properly disabled.
                # However, if get_game_state('c') fails (e.g., file corrupt, or returns '00')
                func.log_event("Failed to load game state for continue or no valid last paragraph found.", event_type="WARNING")
                
                fade_transition(window, fade_out=True, duration=0.1)
                clear_window(window)
                set_background(window)

                error_msg = _get_gui_text('continue_error_msg', 'infobook', "Error: Could not continue game.")
                Label(window, text=error_msg,
                      font=(getattr(cnst, 'GUI_MAIN_FONT', 'Georgia'), 18, "bold"),
                      bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', getattr(cnst, 'GUI_BCKG_COLOR', '#333333')),
                      fg=getattr(cnst, 'GUI_FONT_COLOR_ERROR', 'red')).pack(pady=(150, 20))
                
                back_btn_text = _get_gui_text('back_button', 'infobook', "Back to Menu")
                back_button = create_button(window, back_btn_text, 
                                            lambda: show_main_menu(window), style="default")
                back_button.pack(pady=30)
                
                fade_transition(window, fade_out=False, duration=0.2)

        def _parse_save_filename_for_display(filename):
            """Helper to create a display name from filename.
               Example: dreszcz_2023-10-27_153045.gmsf -> Save (2023-10-27 15:30:45)
            """
            if filename.startswith("dreszcz_") and filename.endswith(cnst.GAMESTATE_EXTENSION):
                parts = filename.replace("dreszcz_", "").replace(cnst.GAMESTATE_EXTENSION, "").split('_')
                if len(parts) == 2:
                    date_part = parts[0]
                    time_part_raw = parts[1]
                    if len(time_part_raw) == 6: # HHMMSS
                        time_part = f"{time_part_raw[0:2]}:{time_part_raw[2:4]}:{time_part_raw[4:6]}"
                        return f"Save ({date_part} {time_part})"
            return filename # Fallback to raw filename

        def _fetch_detailed_save_files():
            """
            Simulates func.list_save_files_details().
            Lists save files from cnst.GAMESTATE_DIR, attempts to read metadata.
            Returns a list of dictionaries, sorted by modification time (newest first).
            """
            save_files_details = []
            if not os.path.exists(cnst.GAMESTATE_DIR):
                func.log_event(f"Save directory not found: {cnst.GAMESTATE_DIR}", "WARNING")
                return []

            for filename in os.listdir(cnst.GAMESTATE_DIR):
                if filename.startswith("dreszcz_") and filename.endswith(cnst.GAMESTATE_EXTENSION):
                    filepath = os.path.join(cnst.GAMESTATE_DIR, filename)
                    details = {'filepath': filepath, 'display_name': filename, 'player_name': 'N/A', 'last_paragraph': 'N/A', 'save_time': None}
                    try:
                        details['save_time'] = os.path.getmtime(filepath)
                        with open(filepath, 'r') as f:
                            data = json.load(f)
                        details['player_name'] = data.get('player_name', 'N/A')
                        details['last_paragraph'] = data.get('last_paragraph', 'N/A')
                        
                        # Construct a more informative display name
                        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(details['save_time']))
                        details['display_name'] = f"{time_str} - {details['player_name']} (Para: {details['last_paragraph']})"

                    except Exception as e:
                        func.log_event(f"Error reading metadata from {filename}: {e}", "WARNING")
                        # Use basic display name if metadata read fails
                        details['display_name'] = _parse_save_filename_for_display(filename) + " (metadata error)"
                    
                    save_files_details.append(details)
            
            # Sort by save_time (modification time), newest first
            save_files_details.sort(key=lambda x: x.get('save_time', 0), reverse=True)
            return save_files_details

        def _execute_gui_load_specific_game(window, filepath):
            """
            Loads game state from a specific filepath and updates cnst variables.
            This replaces the old execute_load_game and is more direct.
            Returns last_paragraph on success, None on failure.
            """
            func.log_event(f"GUI: Attempting to load game from: {filepath}")
            if not os.path.exists(filepath):
                func.error_message(f"File not found: {filepath}", "GUI Load Error")
                return None
            
            try:
                with open(filepath, "r") as f:
                    game_state = json.load(f)
            except Exception as e:
                func.error_message(str(e), f"Error loading/parsing JSON from {filepath}")
                return None

            # Set active gameplay path
            cnst.setup_params['active_gameplay'] = filepath
            
            # Update cnst variables from game_state
            cnst.player_name = game_state.get("player_name", _get_gui_text('unknown_player', 'infobook', "Unknown Player"))
            
            # Difficulty (ensure it's in lowercase as keys in cnst.difficulty_levels)
            difficulty_setting_loaded = game_state.get("difficulty_setting", "medium").lower()
            cnst.difficulty = cnst.difficulty_levels.get(difficulty_setting_loaded, cnst.difficulty_levels["medium"]) # Store the multiplier
            cnst.entity_hit_mult = cnst.difficulty # For consistency, entity_hit_mult IS the multiplier
            # Store the string key for display/logic if needed elsewhere
            cnst.difficulty_str_repr = difficulty_setting_loaded 

            func.log_event(f"Loaded game with difficulty: {cnst.difficulty_str_repr} (Multiplier: {cnst.entity_hit_mult})")

            # Player stats
            cnst.s_count = game_state.get("s_count", 10)
            cnst.w_count = game_state.get("w_count", 20)
            cnst.z_count = game_state.get("z_count", 10)
            cnst.s_init = game_state.get("s_init", cnst.s_count) # Ensure init stats are also loaded
            cnst.w_init = game_state.get("w_init", cnst.w_count)
            cnst.z_init = game_state.get("z_init", cnst.z_count)
            
            # Inventory and other game variables
            cnst.main_eq = game_state.get("equipment", {})
            cnst.potion = game_state.get("potion", None) # Elixir type 'z', 'w', or 's'
            cnst.potion_count = game_state.get("potion_count", 0)
            cnst.meal_count = game_state.get("meal_count", 0)
            cnst.gold_amount = game_state.get("gold_amount", 0)
            
            # Special items / flags
            # (Add any other specific game state variables that need loading)

            last_paragraph = game_state.get("last_paragraph", "00")
            if not last_paragraph or last_paragraph == '00': # Should not happen for a valid save
                func.error_message(f"Invalid start paragraph '00' in save file: {filepath}", "GUI Load Error")
                return None

            func.update_config_file() # Save changes to config (like active_gameplay)
            func.log_event(f"Game state loaded successfully from {filepath}. Last paragraph: {last_paragraph}")
            return last_paragraph

        def _initiate_load_and_launch(window, filepath):
            """Handles the GUI transition and calls the console launcher after loading."""
            last_paragraph = _execute_gui_load_specific_game(window, filepath)

            if last_paragraph:
                fade_transition(window, fade_out=True, duration=0.2)
                clear_window(window)
                set_background(window)
                
                load_success_msg = _get_gui_text('load_success_msg', 'infobook', f"Successfully loaded. Starting from paragraph {last_paragraph}...")
                Label(window, text=load_success_msg,
                      font=(getattr(cnst, 'GUI_MAIN_FONT', 'Georgia'), 18, "italic"),
                      bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', getattr(cnst, 'GUI_BCKG_COLOR', '#333333')),
                      fg=getattr(cnst, 'GUI_FONT_COLOR', '#FFFFFF')).pack(pady=(150, 20))
                
                start_msg = _get_gui_text('game_starting_console_msg', 'infobook', "Game starting in console...")
                Label(window, text=start_msg, 
                      font=(getattr(cnst, 'GUI_MAIN_FONT', 'Georgia'), 16),
                      bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', getattr(cnst, 'GUI_BCKG_COLOR', '#333333')),
                      fg=getattr(cnst, 'GUI_FONT_COLOR', '#FFFFFF')).pack(pady=20)

                fade_transition(window, fade_out=False, duration=0.2)
                window.update_idletasks()

                def launch_game():
                    try:
                        if window.winfo_exists(): window.destroy()
                    except tk.TclError: pass
                    func.pth_selector(actions=[f'{last_paragraph}'])
                
                window.after(2500, launch_game)
            else:
                # Error occurred during load, _execute_gui_load_specific_game handled logging.
                # Display error on the current Load Game screen.
                # For simplicity, we might just show a temporary error label on top of the list.
                # A more robust UI would integrate this error more smoothly.
                error_label = Label(window, text=_get_gui_text('load_failed_msg', 'infobook', "Error: Failed to load selected game."),
                                    font=(getattr(cnst, 'GUI_MAIN_FONT', 'Georgia'), 16, "bold"),
                                    bg="red", fg="white")
                error_label.place(relx=0.5, rely=0.1, anchor=CENTER)
                window.after(3000, error_label.destroy) # Show error for 3 seconds


        def load_game_action(window):
            """Displays the 'Load Game' screen with a list of saved games."""
            fade_transition(window, fade_out=True, duration=0.1)
            clear_window(window)
            set_background(window)

            title_text = _get_gui_text('load_game_title', 'infobook', "Load Game")
            Label(window, text=title_text, font=(cnst.GUI_MAIN_FONT, 30, "bold"),
                  bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', cnst.GUI_BCKG_COLOR),
                  fg=getattr(cnst, 'GUI_FONT_COLOR_TITLE', cnst.GUI_FONT_COLOR)).pack(pady=(20, 10))

            # This part simulates func.list_save_files_details()
            save_files = _fetch_detailed_save_files() # Get sorted list with details

            if not save_files:
                no_saves_msg = _get_gui_text('no_saves_found_msg', 'infobook', "No saved games found.")
                Label(window, text=no_saves_msg, 
                      font=(cnst.GUI_MAIN_FONT, 18), 
                      bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', cnst.GUI_BCKG_COLOR), 
                      fg=cnst.GUI_FONT_COLOR).pack(pady=50)
            else:
                # --- Scrollable Frame Setup ---
                list_canvas_frame = Frame(window, bg=getattr(cnst, 'GUI_BCKG_COLOR', '#333333'))
                list_canvas_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

                canvas = tk.Canvas(list_canvas_frame, 
                                   bg=getattr(cnst, 'GUI_SCROLL_CANVAS_BG', '#444444'),
                                   highlightthickness=0)
                scrollbar = tk.Scrollbar(list_canvas_frame, orient="vertical", command=canvas.yview,
                                         troughcolor=getattr(cnst, 'GUI_SCROLLBAR_TROUGH_COLOR', '#555555'))
                scrollable_frame = tk.Frame(canvas, bg=getattr(cnst, 'GUI_SCROLL_FRAME_BG', '#444444'))

                scrollable_frame.bind(
                    "<Configure>",
                    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
                )
                canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                canvas.configure(yscrollcommand=scrollbar.set)

                canvas.pack(side="left", fill="both", expand=True)
                scrollbar.pack(side="right", fill="y")
                
                # Adjust canvas window width on canvas configure
                def _configure_canvas_window(event):
                    canvas.itemconfig(canvas_window, width=event.width)
                canvas.bind("<Configure>", _configure_canvas_window)
                # --- End Scrollable Frame Setup ---

                for save_info in save_files:
                    entry_frame = tk.Frame(scrollable_frame, bg=getattr(cnst, 'GUI_LIST_ITEM_BG', '#505050'), relief='raised', borderwidth=1)
                    entry_frame.pack(fill=tk.X, pady=5, padx=5)
                    
                    display_text = save_info.get('display_name', _parse_save_filename_for_display(save_info['filepath']))
                    
                    info_label = Label(entry_frame, text=display_text, 
                                       font=(cnst.GUI_MAIN_FONT, 14), 
                                       bg=getattr(cnst, 'GUI_LIST_ITEM_BG', '#505050'), 
                                       fg=getattr(cnst, 'GUI_LIST_ITEM_FG', '#DDDDDD'), anchor='w', justify=LEFT)
                    info_label.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill=tk.X)
                    
                    load_btn_text = _get_gui_text('load_button', 'infobook', "Load")
                    load_button = create_button(entry_frame, load_btn_text,
                                                lambda sp=save_info['filepath']: _initiate_load_and_launch(window, sp),
                                                style="small") # Using "small" style for these buttons
                    load_button.pack(side=tk.RIGHT, padx=10, pady=5)

            back_btn_text = _get_gui_text('back_button', 'infobook', "Back")
            back_button_frame = Frame(window, bg=getattr(cnst, 'GUI_BCKG_COLOR', '#333333')) # Match main bg
            back_button_frame.pack(fill=X, pady=(5,15))
            back_button = create_button(back_button_frame, back_btn_text,
                                        lambda: show_main_menu(window), style="back_button")
            back_button.pack() # Centered by default in its own frame

            fade_transition(window, fade_out=False)

        # --- Game Rules Section ---
        RULES_CONFIG = {
            'eq_attr': {
                'title_key': 'Mmenu3_sub1', 'fallback_title': "Equipment and Attributes",
                'text_keys': ['Mmenu3_sub1_1a', 'Mmenu3_sub1_1b', 'Mmenu3_sub1_1c', 'Mmenu3_sub1_1d', 'Mmenu3_sub1_1e', 'Mmenu3_sub1_1f', 'Mmenu3_sub1_1g'],
                'is_equipment_rule': True
            },
            'combat': {
                'title_key': 'Mmenu3_sub2', 'fallback_title': "Combat",
                'text_keys': ['Mmenu3_sub2_1a', 'Mmenu3_sub2_1b', 'Mmenu3_sub2_1c', 'Mmenu3_sub2_1d', 'Mmenu3_sub2_1e'],
                'is_equipment_rule': False
            },
            'escape': {
                'title_key': 'Mmenu3_sub3', 'fallback_title': "Escape",
                'text_keys': ['Mmenu3_sub3_1a', 'Mmenu3_sub3_1b'], # Assuming fewer keys for brevity
                'is_equipment_rule': False
            },
            'luck': {
                'title_key': 'Mmenu3_sub4', 'fallback_title': "Luck",
                'text_keys': ['Mmenu3_sub4_1a', 'Mmenu3_sub4_1b'],
                'is_equipment_rule': False
            },
            'leveling': {
                'title_key': 'Mmenu3_sub5', 'fallback_title': "Leveling Up Attributes",
                'text_keys': ['Mmenu3_sub5_1a', 'Mmenu3_sub5_1b'],
                'is_equipment_rule': False
            },
            'provisions': {
                'title_key': 'Mmenu3_sub6', 'fallback_title': "Provisions",
                'text_keys': ['Mmenu3_sub6_1a', 'Mmenu3_sub6_1b'],
                'is_equipment_rule': False
            },
            'purpose': {
                'title_key': 'Mmenu3_sub7', 'fallback_title': "Purpose of the Expedition",
                'text_keys': ['Mmenu3_sub7_1a', 'Mmenu3_sub7_1b'],
                'is_equipment_rule': False
            }
        }

        def show_specific_rule_screen(window, rule_config):
            """Displays a specific rule's title and text, with optional equipment list."""
            fade_transition(window, fade_out=True, duration=0.1)
            clear_window(window)
            set_background(window)

            rule_title = _get_gui_text(rule_config['title_key'], 'infobook', rule_config['fallback_title'])
            Label(window, text=rule_title, font=(cnst.GUI_MAIN_FONT, 26, "bold"),
                  bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', cnst.GUI_BCKG_COLOR),
                  fg=getattr(cnst, 'GUI_FONT_COLOR_TITLE', cnst.GUI_FONT_COLOR)).pack(pady=(20, 15))

            text_frame = Frame(window, bg=getattr(cnst, 'GUI_TEXT_AREA_BG', '#e0e0e0'))
            text_frame.pack(padx=20, pady=10, fill=BOTH, expand=True)
            
            text_widget = tk.Text(text_frame, wrap=WORD, 
                                  font=(cnst.GUI_MAIN_FONT, 14),
                                  bg=getattr(cnst, 'GUI_TEXT_AREA_BG', '#e0e0e0'),
                                  fg=getattr(cnst, 'GUI_TEXT_AREA_FG', '#000000'),
                                  padx=10, pady=10, relief=FLAT, borderwidth=0)
            scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview,
                                     troughcolor=getattr(cnst, 'GUI_SCROLLBAR_TROUGH_COLOR', '#555555'))
            text_widget['yscrollcommand'] = scrollbar.set

            scrollbar.pack(side=RIGHT, fill=Y)
            text_widget.pack(side=LEFT, fill=BOTH, expand=True)

            full_rule_text = ""
            for text_key in rule_config['text_keys']:
                segment = _get_gui_text(text_key, 'infobook', f"Text for {text_key} not found.\n")
                full_rule_text += segment + "\n\n"
            
            if rule_config.get('is_equipment_rule', False):
                eq_title = _get_gui_text('current_equipment_title', 'infobook', "\n--- Current Equipment ---")
                full_rule_text += f"\n{eq_title}\n"
                if cnst.main_eq and any(v for v in cnst.main_eq.values()): # Check if any equipment has a truthy value
                    for item_key, value in cnst.main_eq.items():
                        if value: # Only display if True or count > 0
                            item_name = _get_gui_text(item_key, 'gamebook', item_key.replace('_', ' ').title())
                            if isinstance(value, bool) and value:
                                full_rule_text += f"- {item_name}\n"
                            elif isinstance(value, int) and value > 0:
                                full_rule_text += f"- {item_name}: {value}\n"
                else:
                    no_eq_text = _get_gui_text('no_equipment_text', 'infobook', "No equipment to display.")
                    full_rule_text += no_eq_text + "\n"
            
            text_widget.insert(tk.END, full_rule_text.strip())
            text_widget.config(state=tk.DISABLED) # Make read-only

            back_btn_text = _get_gui_text('back_button', 'infobook', "Back to Rules Menu")
            back_button = create_button(window, back_btn_text,
                                        lambda: show_rules_menu(window), style="back_button")
            back_button.pack(pady=15)

            fade_transition(window, fade_out=False)


        def show_rules_menu(window):
            """Displays the main menu for game rules."""
            fade_transition(window, fade_out=True, duration=0.1)
            clear_window(window)
            set_background(window)

            title_text = _get_gui_text('Mmenu3', 'infobook', "Game Rules") # Main title for rules section
            Label(window, text=title_text, font=(cnst.GUI_MAIN_FONT, 30, "bold"),
                  bg=getattr(cnst, 'GUI_BCKG_COLOR_LABEL', cnst.GUI_BCKG_COLOR),
                  fg=getattr(cnst, 'GUI_FONT_COLOR_TITLE', cnst.GUI_FONT_COLOR)).pack(pady=(20, 15))
            
            buttons_frame = Frame(window, bg=getattr(cnst, 'GUI_BCKG_COLOR', '#c0c0c0'))
            buttons_frame.pack(pady=10)

            buttons_list = []
            # Order of rules as specified in the task
            rule_order = ['eq_attr', 'combat', 'escape', 'luck', 'leveling', 'provisions', 'purpose']

            for rule_key in rule_order:
                config = RULES_CONFIG[rule_key]
                button_text = _get_gui_text(config['title_key'], 'infobook', config['fallback_title'])
                # Using a partial or a nested lambda with default argument to capture current config
                btn = create_button(buttons_frame, button_text,
                                    lambda c=config: show_specific_rule_screen(window, c),
                                    style="default", width=30) # Ensure buttons have a decent width
                btn.pack(pady=6)
                buttons_list.append(btn)

            back_btn_text = _get_gui_text('back_button', 'infobook', "Back to Main Menu")
            back_button = create_button(window, back_btn_text,
                                        lambda: show_main_menu(window), style="back_button")
            # Place back button at the bottom, can use pack or place
            back_button.pack(pady=(20,10)) # Add some space before it

            fade_transition(window, fade_out=False)

        def show_settings_menu(window):
            # This function seems to be the intended action for the "Settings" button.
            # The 'settings(window)' function which has the detailed settings UI logic should be called by this.
            # If 'settings(window)' is the actual UI display function, then this is correct.
            # Based on current structure, 'settings(window)' IS the UI display function.
            settings(window)

        def test_paragraph_action(window):
            fade_transition(window)
            clear_window(window)
            set_background(window)
            text = "Test Paragraph (Action Stub - To be fully implemented)"
            label = tk.Label(window, text=text, font=(cnst.GUI_MAIN_FONT, 18), bg=cnst.GUI_BCKG_COLOR, fg="white")
            label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            back_button = create_button(window, "Back", lambda: show_main_menu(window))
            back_button.place(relx=0.95, rely=0.95, anchor=tk.SE)
            fade_transition(window, fade_out=False)
        # --- END OF NEW ACTION STUBS ---

        def show_main_menu(window):
            """
            Displays the main menu GUI, including standard game options and conditional developer tools.
            Buttons are dynamically created, localized, and positioned.
            """
            fade_transition(window, fade_out=True, duration=0.1) # Quick fade out of previous screen
            clear_window(window)
            set_background(window, image_filename="menu_background.png") # Ensure default background
    
            buttons_data = [] # To store (text, command, state, style) tuples
            
            # Determine if a translation is loaded and available in infobook
            translation_key = cnst.setup_params.get('translation')
            translation_available = translation_key and hasattr(gb, 'infoboook') and \
                                    isinstance(gb.infoboook, dict) and \
                                    translation_key in gb.infoboook and \
                                    isinstance(gb.infoboook[translation_key], dict)

            def get_menu_text(key, fallback_text):
                if translation_available:
                    return gb.infoboook[translation_key].get(key, fallback_text)
                return fallback_text

            # 1. New Game Button
            new_game_text = get_menu_text('Mmenu1', "New Game")
            new_game_state = tk.DISABLED if cnst.setup_params.get('use_dummy', False) else tk.NORMAL
            buttons_data.append((new_game_text, lambda: new_game_action(window), new_game_state, "default"))

            # 2. Continue Button
            continue_text = get_menu_text('Mmenu0', "Continue")
            # Check if a game state exists and there's an active gameplay file
            can_continue = cnst.game_state_exists and cnst.setup_params.get('active_gameplay')
            continue_state = tk.NORMAL if can_continue else tk.DISABLED
            buttons_data.append((continue_text, lambda: continue_game_action(window), continue_state, "default"))

            # 3. Load Game Button
            load_game_text = get_menu_text('Mmenu2', "Load Game")
            # For now, always enable. load_game_action handles "no saves".
            # To disable if no saves: needs a quick check like `len(func.get_save_files_list()) > 0`
            # This might be too slow here, so deferring to the action handler.
            load_game_state = tk.NORMAL if not cnst.setup_params.get('use_dummy', False) else tk.DISABLED
            buttons_data.append((load_game_text, lambda: load_game_action(window), load_game_state, "default"))
            
            # 4. Settings Button
            settings_text = get_menu_text('Mmenu4', "Settings")
            buttons_data.append((settings_text, lambda: show_settings_menu(window), tk.NORMAL, "default"))

            # 5. Game Rules Button
            rules_text = get_menu_text('Mmenu3', "Game Rules") # Mmenu3 is correct for infobook key
            buttons_data.append((rules_text, lambda: show_rules_menu(window), tk.NORMAL, "default"))

            # Developer Options (Conditional)
            if cnst.setup_params.get('dev_mode', False):
                dev_button_style = "small" # Use smaller buttons for dev options
                buttons_data.append(
                    (get_menu_text('Mdev_testp', "[DEV] Test Paragraph"), 
                     lambda: test_paragraph_action(window), tk.NORMAL, dev_button_style)
                )
                buttons_data.append(
                    (get_menu_text('Mdev_config', "[DEV] Configure Setup"), 
                     lambda: func.update_config_file(True), tk.NORMAL, dev_button_style)
                )
                buttons_data.append(
                    (get_menu_text('Mdev_docs', "[DEV] Project Docs"), 
                     lambda: func.open_dir(cnst.DOCUMENTATION_DIR), tk.NORMAL, dev_button_style)
                )
                buttons_data.append(
                    (get_menu_text('Mdev_saves', "[DEV] Gamestate Dir"), 
                     lambda: func.open_dir(cnst.GAMESTATE_DIR), tk.NORMAL, dev_button_style)
                )
                buttons_data.append(
                    (get_menu_text('Mdev_restorecfg', "[DEV] Restore Config"), 
                     lambda: func.update_config_file(backup=True), tk.NORMAL, dev_button_style)
                )
            
            # 6. Exit Button
            exit_text = get_menu_text('Mmenu5', "Exit")
            buttons_data.append((exit_text, lambda: exit_game(window), tk.NORMAL, "default"))

            # Create and place buttons
            buttons = []
            for text, command, state, style in buttons_data:
                # Use smaller font size for dev buttons if style is "small"
                # The create_button function now handles the 'style' argument.
                button = create_button(window, text, command, state=state, style=style)
                buttons.append(button)
            
            # Adjust spacing based on number of buttons
            # Base spacing can be defined in constants, e.g., cnst.GUI_BUTTON_SPACING_Y_DEFAULT
            default_spacing = getattr(cnst, 'GUI_BUTTON_SPACING_Y_DEFAULT', 60)
            small_spacing = getattr(cnst, 'GUI_BUTTON_SPACING_Y_SMALL', 45)
            current_spacing = small_spacing if len(buttons) > 7 else default_spacing
            
            update_buttons_position(window, buttons, spacing_y=current_spacing) 
            
            fade_transition(window, fade_out=False, duration=0.3) # Fade in the new menu

        def main():
            window = tk.Tk()
            center_window(window, width=cnst.GUI_WINDOW_WIDTH, height=cnst.GUI_WINDOW_HEIGHT)
            window.title("Dreszcz")

            icon = PhotoImage(file=f"{cnst.GRAPHICS_MISC_DIR}/simple.png")
            window.iconphoto(True, icon)

            show_main_menu(window)

            window.mainloop()

        if __name__ == '__main__':
            main()

    else:  # terminal based interface
        while True:
            func.clear_terminal()

            if cnst.player_name:
                print(
                    f"{cnst.DEFAULT_COLOR}{gb.infoboook[cnst.setup_params['translation']]['Mmenu_h']} {cnst.player_name}!")
            print(
                f"{cnst.SPECIAL_COLOR}{gb.infoboook[cnst.setup_params['translation']]['Mmenu_headline']}{cnst.DEFAULT_COLOR}")

            if cnst.__version__:
                print(f"{cnst.DEBUG_COLOR}ver.{cnst.__version__}{cnst.DEFAULT_COLOR}")

            choices_main_menu = [
                (gb.infoboook[cnst.setup_params['translation']]['Mmenu0'], cnst.setup_params['active_gameplay']),
                (gb.infoboook[cnst.setup_params['translation']]['Mmenu1'], ''), 
                (gb.infoboook[cnst.setup_params['translation']]['Mmenu2'], ''), 
                (gb.infoboook[cnst.setup_params['translation']]['Mmenu3'], ''), 
                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4'], ''), 
                (gb.infoboook[cnst.setup_params['translation']]['Mmenu5'], ''), 
            ]

            if not cnst.game_state_exists:
                choices_main_menu.remove(
                    (gb.infoboook[cnst.setup_params['translation']]['Mmenu0'], cnst.setup_params['active_gameplay']))
                choices_main_menu.remove((gb.infoboook[cnst.setup_params['translation']]['Mmenu2'], ''))

            if cnst.setup_params['dev_mode']:
                choices_main_menu.append(
                    (f'{cnst.SPECIAL_COLOR}test_paragraph{cnst.DEFAULT_COLOR}',
                     f'bypass to any paragraph'))
                choices_main_menu.append(
                    (f'{cnst.SPECIAL_COLOR}configure setup file{cnst.DEFAULT_COLOR}', 'config wizard'))
                choices_main_menu.append(
                    (f'{cnst.SPECIAL_COLOR}project documentation{cnst.DEFAULT_COLOR}',
                     'pdf scan of original book, HTML adaptation from http://www.dudziarz.net'))
                choices_main_menu.append(
                    (f'{cnst.SPECIAL_COLOR}show gamestate directory{cnst.DEFAULT_COLOR}',
                     'open directory that holds game_state files'))
                choices_main_menu.append(
                    (f'{cnst.SPECIAL_COLOR}restore default config{cnst.DEFAULT_COLOR}', 'ALL CHANGES WILL BE LOST!!!'))

            if cnst.setup_params['use_dummy']:
                choices_main_menu.remove((gb.infoboook[cnst.setup_params['translation']]['Mmenu1'], ''))
                choices_main_menu.remove((gb.infoboook[cnst.setup_params['translation']]['Mmenu2'], ''))

            for i, (choice_main_menu, description) in enumerate(choices_main_menu, 1):
                print(template.format(i, choice_main_menu, description))

            usr_input = input(f'{cnst.INPUT_SIGN}').strip()

            if usr_input == 'rayman':
                cnst.setup_params['dev_mode'] = True
                cnst.template = "({}) {} - {}"
            elif usr_input == 'mario':
                cnst.setup_params['dev_mode'] = False
                cnst.template = "({}) {}"

            if usr_input.isdigit():
                index = int(usr_input) - 1
                if 0 <= index < len(choices_main_menu):
                    usr_input = choices_main_menu[index][0]

            for choice_main_menu, description in choices_main_menu:
                if usr_input == choice_main_menu:
                    if choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu0']:
                        last_paragraph = func.get_game_state('c')
                        func.pth_selector(actions=[f'{last_paragraph}'])
                    elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu1']:
                        func.clear_terminal()
                        print(f"/ {choice_main_menu}{cnst.DEFAULT_COLOR}")
                        prg._00()
                    elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu2']:
                        func.clear_terminal()
                        print(f"/ {choice_main_menu}{cnst.DEFAULT_COLOR}")
                        last_paragraph = func.get_game_state('l')
                        if not last_paragraph == '00':
                            func.pth_selector([], [f'{last_paragraph}'])
                    elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu3']:
                        while True: 
                            func.clear_terminal()
                            print(f"{cnst.SPECIAL_COLOR}/ {choice_main_menu}{cnst.DEFAULT_COLOR}")
                            choices_rules = [
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub2'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub3'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub4'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub5'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub6'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub7'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['return'], '')
                            ]
                            for i, (choice_rules, desc) in enumerate(choices_rules, 1):
                                print(template.format(i, choice_rules, desc))
                            
                            usr_input_rules = input(f'{cnst.INPUT_SIGN}').strip()
                            if usr_input_rules.isdigit():
                                idx_rules = int(usr_input_rules) - 1
                                if 0 <= idx_rules < len(choices_rules):
                                    usr_input_rules = choices_rules[idx_rules][0]

                            if usr_input_rules == gb.infoboook[cnst.setup_params['translation']]['return']:
                                break 
                            input(f'{cnst.INPUT_SIGN}') 
                    elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu4']:
                        while True:
                            func.clear_terminal()
                            print(f"{cnst.SPECIAL_COLOR}/ {choice_main_menu}{cnst.DEFAULT_COLOR}")
                            choices_settings = [
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub2'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub3'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub4'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub5'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub6'], ''),
                                (gb.infoboook[cnst.setup_params['translation']]['return'], '')
                            ]
                            for i, (choice_settings_item, description_settings) in enumerate(choices_settings, 1):
                                print(template.format(i, choice_settings_item, description_settings))
                            
                            usr_input_settings = input(f'{cnst.INPUT_SIGN}').strip()
                            if usr_input_settings.isdigit():
                                index_settings = int(usr_input_settings) - 1
                                if 0 <= index_settings < len(choices_settings):
                                    usr_input_settings = choices_settings[index_settings][0]

                            if usr_input_settings == gb.infoboook[cnst.setup_params['translation']]['return']:
                                break 
                            input(f'{cnst.INPUT_SIGN}') 

                    elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu5']:
                        choice2 = input(
                            f"{gb.infoboook[cnst.setup_params['translation']]['Mmenu5_sub1_1']} [Y/N]:").lower()
                        if choice2.lower() == "y":
                            pygame.mixer.music.fadeout(800)
                            func.clear_terminal()
                            exit(0)
                    # ... (dev options logic)

if __name__ == '__main__':
    if cnst.setup_params['dev_mode']:
        template = "({}) {} - {}"
        print(f"\n{cnst.SPECIAL_COLOR}Setup parameters loaded from file: {Fore.YELLOW}{cnst.CFG_NAME}{Style.RESET_ALL}")
        for key, value in cnst.setup_params.items():
            print(f"- {key.ljust(max(len(str(k)) for k in cnst.setup_params.keys()))} - {value}")
        print(
            f"\n{Fore.LIGHTBLUE_EX}Code is running in developer mode.\
            \nTo deactivate the dev_mode temporarily toggle in the main menu, enter 'rayman'-ON or 'mario'-OFF.\
            \nAlso, you can change the setup parameters in the setup file manually.{cnst.DEFAULT_COLOR}\
            \n\
            \nuseful stuff:\
            \nsetup parameters {cnst.INPUT_SIGN}{cnst.CFG_NAME}\
            \ndocumentation {cnst.INPUT_SIGN}Assets\\docs\\"
        )
        input(f"\ncontinue by pressing enter {cnst.INPUT_SIGN}")
    else:
        template = "({}) {}"

    if cnst.setup_params['start_sequence']:
        func.get_music('menu')
        time.sleep(1.4)
        messages = ['Jacek Ciesielski\r', 'Filip Pawłowski', 'presents...', 'DRESZCZ - GRA PARAGRAFOWA']
        for message in messages:
            print(message)
            time.sleep(5.4)
    else:
        func.get_music('main')

    func.get_player_par()
    func.get_game_state('init')

    try:
        with open(cnst.CFG_NAME, 'r') as json_file:
            _ = json_file.readable()
    except FileNotFoundError as e:
        func.error_message(str(e), f"An error occurred while updating the setup file")
        func.debug_message("config.json not found, restoring...")
        func.update_config_file(manual=False, backup=True)

    main_menu()

[end of menu.py]
