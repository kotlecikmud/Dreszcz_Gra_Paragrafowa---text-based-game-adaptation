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
import functions as func
import constants as cnst
# import paragraphs as prg # Removed
from colorama import Fore, Style


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
        def center_window(window, width=512, height=512):
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            x_coordinate = int((screen_width / 2) - (width / 2))
            y_coordinate = int((screen_height / 2) - (height / 2))
            window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

        def update_buttons_position(window, buttons, spacing=70):
            window.update_idletasks()
            for i, button in enumerate(buttons):
                button.place(x=window.winfo_width() / 2 - button.winfo_reqwidth() / 2,
                             y=window.winfo_height() / 2 - (len(buttons) * spacing / 2) + i * spacing)

        def on_enter(event):
            event.widget['background'] = '#d1d1d1'

        def on_leave(event):
            event.widget['background'] = cnst.GUI_BCKG_COLOR

        def fade_transition(window, fade_out=True):
            overlay = tk.Label(window, bg='black')
            overlay.place(x=0, y=0, relwidth=1, relheight=1)

            for i in range(11):
                alpha = i / 10 if fade_out else (10 - i) / 10
                gray_value = int(alpha * 255)
                overlay.configure(bg=f'#{gray_value:02x}{gray_value:02x}{gray_value:02x}')
                window.update()
                time.sleep(0.05)

            if not fade_out:
                overlay.destroy()

        def create_button(window, text, command, state=NORMAL):
            button = Button(window,
                            text=text,
                            font=(cnst.GUI_MAIN_FONT, 24, "italic"),
                            bg=cnst.GUI_BCKG_COLOR,
                            fg="#bcbb8e",
                            relief='raised',
                            activebackground="#808080",
                            command=command,
                            state=state)
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)
            return button

        def set_background(window):
            # Load background image
            background_image = Image.open(f"{cnst.GRAPHICS_PLATES_DIR}/menu_background.png")
            background_image = background_image.resize((cnst.GUI_WINDOW_WIDTH, cnst.GUI_WINDOW_HEIGHT),
                                                       Image.Resampling.LANCZOS)
            background_photo = ImageTk.PhotoImage(background_image)

            background_label = tk.Label(window, image=background_photo)
            background_label.image = background_photo  # Keep a reference
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            return background_label

        def clear_window(window):
            for widget in window.winfo_children():
                widget.destroy()

        def new_game(window):
            fade_transition(window)
            clear_window(window)
            set_background(window)

            difficulty_frame = Frame(window, bg=cnst.GUI_BCKG_COLOR)
            difficulty_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

            difficulties = ["Easy", "Normal", "Hard"]
            for diff in difficulties:
                button = create_button(difficulty_frame, diff, lambda d=diff: start_new_game(window, d))
                button.pack(pady=10)

            back_button = create_button(window, "Back", lambda: show_main_menu(window))
            back_button.place(relx=0.95, rely=0.95, anchor=SE)

            fade_transition(window, fade_out=False)

        def start_new_game(window, difficulty):
            fade_transition(window)
            clear_window(window)
            set_background(window)

            game_frame = Frame(window, bg=cnst.GUI_BCKG_COLOR)
            game_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            Label(game_frame, text=f"Starting new game on {difficulty} difficulty",
                  font=(cnst.GUI_MAIN_FONT, 18)).pack()

            back_button = create_button(window, "Back", lambda: show_main_menu(window))
            back_button.place(relx=0.95, rely=0.95, anchor=SE)

            fade_transition(window, fade_out=False)

        def continue_game(window):
            fade_transition(window)
            clear_window(window)
            set_background(window)

            game_frame = Frame(window, bg=cnst.GUI_BCKG_COLOR)
            game_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            Label(game_frame, text="Continuing from last saved game", font=(cnst.GUI_MAIN_FONT, 18)).pack()

            back_button = create_button(window, "Back", lambda: show_main_menu(window))
            back_button.place(relx=0.95, rely=0.95, anchor=SE)

            fade_transition(window, fade_out=False)

        def load_game(window):
            fade_transition(window)
            clear_window(window)
            set_background(window)

            load_frame = Frame(window, bg=cnst.GUI_BCKG_COLOR)
            load_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

            # Dummy saved game data
            saved_games = [
                {"name": "Save1", "created": "2024-09-01", "last_save": "2024-09-05"},
                {"name": "Save2", "created": "2024-09-02", "last_save": "2024-09-06"},
                {"name": "Save3", "created": "2024-09-03", "last_save": "2024-09-07"},
            ]

            for game in saved_games:
                save_frame = Frame(load_frame, bg=cnst.GUI_BCKG_COLOR, relief=RAISED, borderwidth=2)
                save_frame.pack(fill=X, padx=5, pady=5)
                Label(save_frame, text=f"Name: {game['name']}", bg=cnst.GUI_BCKG_COLOR).pack(anchor=W)
                Label(save_frame, text=f"Created: {game['created']}", bg=cnst.GUI_BCKG_COLOR).pack(anchor=W)
                Label(save_frame, text=f"Last Save: {game['last_save']}", bg=cnst.GUI_BCKG_COLOR).pack(anchor=W)
                Button(save_frame, text="Load", command=lambda g=game: load_saved_game(window, g)).pack(side=RIGHT)

            back_button = create_button(window, "Back", lambda: show_main_menu(window))
            back_button.place(relx=0.95, rely=0.95, anchor=SE)

            fade_transition(window, fade_out=False)

        def load_saved_game(window, game):
            fade_transition(window)
            clear_window(window)
            set_background(window)

            game_frame = Frame(window, bg=cnst.GUI_BCKG_COLOR)
            game_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            Label(game_frame, text=f"Loading saved game: {game['name']}", font=(cnst.GUI_MAIN_FONT, 18)).pack()

            back_button = create_button(window, "Back", lambda: show_main_menu(window))
            back_button.place(relx=0.95, rely=0.95, anchor=SE)

            fade_transition(window, fade_out=False)

        def settings(window):
            fade_transition(window)
            clear_window(window)
            set_background(window)

            settings_frame = Frame(window, bg=cnst.GUI_BCKG_COLOR)
            settings_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

            settings_options = [
                "Language", "Difficulty level", "Sound",
                "Character name", "Randomize character attributes", "Check for updates"
            ]

            for option in settings_options:
                button = create_button(settings_frame, option, lambda o=option: show_not_implemented(window, o))
                button.pack(pady=5)

            back_button = create_button(window, "Back", lambda: show_main_menu(window))
            back_button.place(relx=0.95, rely=0.95, anchor=SE)

            fade_transition(window, fade_out=False)

        def show_not_implemented(window, option):
            label = Label(window, text=f"{option}: Not implemented", bg='black', fg='white',
                          font=(cnst.GUI_MAIN_FONT, 18))
            label.place(relx=0.5, rely=0.5, anchor=CENTER)
            window.after(1000, label.destroy)

        def about(window):
            fade_transition(window)
            clear_window(window)
            set_background(window)

            about_frame = Frame(window, bg=cnst.GUI_BCKG_COLOR)
            about_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

            about_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."""

            Label(about_frame, text="About Dreszcz", font=(cnst.GUI_MAIN_FONT, 24, "bold"),
                  bg=cnst.GUI_BCKG_COLOR).pack(pady=10)
            Label(about_frame, text=about_text, font=(cnst.GUI_MAIN_FONT, 12), bg=cnst.GUI_BCKG_COLOR,
                  wraplength=400).pack(pady=10)

            back_button = create_button(window, "Back", lambda: show_main_menu(window))
            back_button.place(relx=0.95, rely=0.95, anchor=SE)

            fade_transition(window, fade_out=False)

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

        def show_main_menu(window):
            fade_transition(window)
            clear_window(window)
            set_background(window)

            buttons_data = [
                ("New Game", lambda: new_game(window)),
                ("Continue", lambda: continue_game(window)),
                ("Load game", lambda: load_game(window)),
                ("Settings", lambda: settings(window)),
                ("About", lambda: about(window)),
                ("Exit", lambda: exit_game(window))
            ]

            buttons = []
            for text, command in buttons_data:
                button = create_button(window, text, command)
                buttons.append(button)
                button.place_forget()  # Hide the button initially

            update_buttons_position(window, buttons, spacing=70)

            dummy_label = Label(window, text="*this is dummy GUI*", font=(cnst.GUI_MAIN_FONT, 12, "italic"),
                                bg=cnst.GUI_BCKG_COLOR, fg="#bcbcbc")
            dummy_label.place(x=14, y=window.winfo_height() - 40)

            fade_transition(window, fade_out=False)

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
        # --- MODIFICATION: Directly call new game logic for testing ---
        print("Attempting to start a new game directly for testing...")
        func.pth_selector('00')
        # --- END MODIFICATION ---

        # Original menu loop (commented out or made unreachable for this test)
        if False: # This makes the original loop unreachable
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
                # continue
                (gb.infoboook[cnst.setup_params['translation']]['Mmenu1'], ''),  # new game
                (gb.infoboook[cnst.setup_params['translation']]['Mmenu2'], ''),  # load game
                (gb.infoboook[cnst.setup_params['translation']]['Mmenu3'], ''),  # rules
                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4'], ''),  # settings
                (gb.infoboook[cnst.setup_params['translation']]['Mmenu5'], ''),  # exit
            ]

            # if any game state exists, display corresponding menu options
            if not cnst.game_state_exists:
                # continue last gameplay
                choices_main_menu.remove(
                    (gb.infoboook[cnst.setup_params['translation']]['Mmenu0'], cnst.setup_params['active_gameplay']))

                # load game
                choices_main_menu.remove((gb.infoboook[cnst.setup_params['translation']]['Mmenu2'], ''))

            # append developer mode options at the end of main menu list
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

            if cnst.setup_params['use_dummy']:  # disable 'new game' and 'load game' option when using dummy
                choices_main_menu.remove((gb.infoboook[cnst.setup_params['translation']]['Mmenu1'], ''))  # new game
                choices_main_menu.remove((gb.infoboook[cnst.setup_params['translation']]['Mmenu2'], ''))  # load game

            # displaying list in main menu
            for i, (choice_main_menu, description) in enumerate(choices_main_menu, 1):
                print(template.format(i, choice_main_menu, description))

            usr_input = input(f'{cnst.INPUT_SIGN}').strip()

            if usr_input == 'rayman':  # temporarily enable dev_mode
                cnst.setup_params['dev_mode'] = True
                cnst.template = "({}) {} - {}"
            elif usr_input == 'mario':  # temporarily disable dev_mode
                cnst.setup_params['dev_mode'] = False
                cnst.template = "({}) {}"

            if usr_input.isdigit():
                index = int(usr_input) - 1
                if 0 <= index < len(choices_main_menu):  # is digit in range
                    usr_input = choices_main_menu[index][0]

            for choice_main_menu, description in choices_main_menu:
                if usr_input == choice_main_menu:

                    # continue last gameplay
                    if choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu0']:
                        last_paragraph = func.get_game_state('c')
                        # func.pth_selector(actions=[f'{last_paragraph}']) # Old call
                        if last_paragraph: # Ensure last_paragraph is not None
                            func.pth_selector(f'{last_paragraph}')
                        else: # Fallback if no last_paragraph (e.g. active_gameplay was null)
                            func.debug_message("No last paragraph found to continue.")
                            # Optionally, go to new game or show error. For now, just debug.

                    # new game
                    elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu1']:
                        func.clear_terminal()
                        print(f"/ {choice_main_menu}{cnst.DEFAULT_COLOR}")
                        # prg._00() # Old call
                        func.pth_selector('00') # Start with paragraph "00"

                    # load game
                    elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu2']:
                        func.clear_terminal()
                        print(f"/ {choice_main_menu}{cnst.DEFAULT_COLOR}")

                        last_paragraph = func.get_game_state('l')

                        # last_paragraph from get_game_state('l') might be None if user cancels load
                        if last_paragraph and last_paragraph != '00': # Original condition might have been to prevent loading into title screen
                            # func.pth_selector([], [f'{last_paragraph}']) # Old call
                            func.pth_selector(f'{last_paragraph}')
                        elif last_paragraph == '00': # If '00' is returned, it might mean main menu or new game
                            func.debug_message("Load game returned to main menu or start.")
                        else: # No file selected or error
                            func.debug_message("No game loaded or load was cancelled.")


                    # rules
                    elif choice_main_menu == choice_main_menu == gb.infoboook[cnst.setup_params['translation']][
                        'Mmenu3']:
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

                            for i, (choice_rules, description) in enumerate(choices_rules, 1):
                                print(template.format(i, choice_rules, description))

                            usr_input = input(f'{cnst.INPUT_SIGN}').strip()

                            if usr_input.isdigit():
                                index = int(usr_input) - 1
                                if 0 <= index < len(choices_rules):
                                    usr_input = choices_rules[index][0]

                            for choice_rules, description in choices_rules:
                                if usr_input == choice_rules:
                                    func.clear_terminal()
                                    print(f"{cnst.SPECIAL_COLOR}// {choice_rules}{cnst.DEFAULT_COLOR}")

                                    # Equipment and attributes
                                    if choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1']:
                                        print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_1a'])

                                        # show equipment list
                                        func.show_equipment_list()

                                        print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_1b'])

                                    # Combat
                                    elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub2']:
                                        print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_2'])

                                    # Escape
                                    elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub3']:
                                        print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_3'])

                                    # Luck
                                    elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub4']:
                                        print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_4'])

                                    # Leveling up attributes
                                    elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub5']:
                                        print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_5'])

                                    # Provisions
                                    elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub6']:
                                        print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_6'])

                                    # Purpose of the expedition
                                    elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub7']:
                                        print(gb.infoboook[cnst.setup_params['translation']]['Mmenu3_sub1_7'])

                                    elif choice_rules == gb.infoboook[cnst.setup_params['translation']]['return']:
                                        main_menu()

                                    input(f'{cnst.INPUT_SIGN}')

                    # Settings
                    elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu4']:
                        while True:
                            func.clear_terminal()
                            print(f"{cnst.SPECIAL_COLOR}/ {choice_main_menu}{cnst.DEFAULT_COLOR}")

                            choices_settings = [
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1'], ''),  # Language
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub2'], ''),  # Difficulty level
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub3'], ''),  # Sound
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub4'], ''),  # Character name
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub5'], ''),
                                # Randomize attributes
                                (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub6'], ''),
                                # Check for updates
                                (gb.infoboook[cnst.setup_params['translation']]['return'], '')
                            ]

                            for i, (choice_settings, description) in enumerate(choices_settings, 1):
                                print(template.format(i, choice_settings, description))

                            usr_input = input(f'{cnst.INPUT_SIGN}').strip()

                            if usr_input.isdigit():
                                index = int(usr_input) - 1
                                if 0 <= index < len(choices_settings):
                                    usr_input = choices_settings[index][0]

                            for choice_settings, description in choices_settings:
                                if usr_input == choice_settings:

                                    # Language settings
                                    if choice_settings == gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1']:

                                        # initialize list of Locales in gamebook
                                        availablelocales = []

                                        # prepare available languages and append to list
                                        for key in gb.gameboook:
                                            availablelocales.append(key)

                                        translation = str(input(
                                            f"{cnst.DEFAULT_COLOR}{gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_1']} {availablelocales}\
                                        \n{cnst.INPUT_SIGN}")).lower()

                                        # get localization dictionaries from gamebook
                                        gb.get_translation(translation)

                                        func.debug_message(
                                            f"{gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_2']}: {cnst.setup_params['translation']}")

                                    # Difficulty level settings
                                    if choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                        'Mmenu4_sub2']:
                                        func.clear_terminal()
                                        print(f"{cnst.SPECIAL_COLOR}// {choice_settings}{cnst.DEFAULT_COLOR}")

                                        choices_difficulty_lvl = [
                                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_3'], ''),
                                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_4'], ''),
                                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub1_5'], '')
                                        ]

                                        for i, (choice_difficulty_lvl, description) in enumerate(choices_difficulty_lvl,
                                                                                                 1):
                                            print(template.format(i, choice_difficulty_lvl, description))

                                        usr_input = input(f'{cnst.INPUT_SIGN}').strip()

                                        if usr_input.isdigit():
                                            index = int(usr_input) - 1
                                            if 0 <= index < len(choices_difficulty_lvl):
                                                usr_input = choices_difficulty_lvl[index][0]

                                        dif_lvl_choice = None
                                        for choice_difficulty_lvl, description in choices_difficulty_lvl:
                                            if usr_input == choice_difficulty_lvl:
                                                if choice_difficulty_lvl == \
                                                        gb.infoboook[cnst.setup_params['translation']][
                                                            'Mmenu4_sub1_1']:
                                                    dif_lvl_choice = cnst.difficulty_levels["easy"]

                                                elif choice_difficulty_lvl == \
                                                        gb.infoboook[cnst.setup_params['translation']][
                                                            'Mmenu4_sub1_2']:
                                                    dif_lvl_choice = cnst.difficulty_levels["medium"]

                                                elif choice_difficulty_lvl == \
                                                        gb.infoboook[cnst.setup_params['translation']][
                                                            'Mmenu4_sub1_3']:
                                                    dif_lvl_choice = cnst.difficulty_levels["hard"]

                                                cnst.entity_hit_mult = dif_lvl_choice

                                    # Audio settings -> capped range -> (0,10)
                                    elif choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                        'Mmenu4_sub3']:

                                        func.clear_terminal()
                                        print(f"{cnst.SPECIAL_COLOR}// {choice_settings}{cnst.DEFAULT_COLOR}")

                                        choices_sound_settings = [
                                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub3_1'],
                                             str(int(cnst.setup_params['action_volume'] * 10)) + "/10"),
                                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub3_2'],
                                             str(int(cnst.setup_params['sfx_volume'] * 10)) + "/10"),
                                            (gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub3_3'],
                                             str(int(cnst.setup_params['bckg_volume'] * 10)) + "/10"),
                                            (gb.infoboook[cnst.setup_params['translation']]['return'], '')
                                        ]

                                        for i, (choice_sound_settings, description) in enumerate(choices_sound_settings,
                                                                                                 1):
                                            print(template.format(i, choice_sound_settings, description))

                                        usr_input = input(f'{cnst.INPUT_SIGN}').strip()

                                        if usr_input.isdigit():
                                            index = int(usr_input) - 1
                                            if 0 <= index < len(choices_sound_settings):
                                                usr_input = choices_sound_settings[index][0]

                                        for choice_sound_settings, description in choices_sound_settings:

                                            if usr_input == choice_sound_settings:
                                                while True:
                                                    # 1-10 because it's easier to input whole numbers than float
                                                    try:

                                                        new_volume = int(
                                                            input(gb.infoboook[cnst.setup_params['translation']][
                                                                      'Mmenu4_sub3_a']))
                                                        if 0 < new_volume <= 10:
                                                            break
                                                        else:
                                                            print(gb.infoboook[cnst.setup_params['translation']][
                                                                      'Mmenu4_sub3_b'])

                                                    except ValueError:
                                                        print(
                                                            gb.infoboook[cnst.setup_params['translation']][
                                                                'Mmenu4_sub3_c'])

                                                # divide by 10 to get value between 0 and 1
                                                new_volume = new_volume / 10

                                                # dialogs
                                                if choice_sound_settings == \
                                                        gb.infoboook[cnst.setup_params['translation']][
                                                            'Mmenu4_sub3_1']:
                                                    cnst.setup_params['action_volume'] = new_volume
                                                    func.dub_play("opened", "adam", True, False)

                                                # effects
                                                elif choice_sound_settings == \
                                                        gb.infoboook[cnst.setup_params['translation']][
                                                            'Mmenu4_sub3_2']:
                                                    cnst.setup_params['sfx_volume'] = new_volume
                                                    func.dub_play("click_snd", "fx", True, False)

                                                # background music
                                                elif choice_sound_settings == \
                                                        gb.infoboook[cnst.setup_params['translation']][
                                                            'Mmenu4_sub3_3']:
                                                    cnst.setup_params['bckg_volume'] = new_volume
                                                    pygame.mixer.music.set_volume(new_volume)

                                                elif choice_sound_settings == \
                                                        gb.infoboook[cnst.setup_params['translation']]['return']:
                                                    func.update_config_file()  # dump settings to setup file
                                                    main_menu()

                                                func.get_music(update=True)

                                    # Name setting
                                    elif choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                        'Mmenu4_sub4']:

                                        name = input(
                                            f"{gb.infoboook[cnst.setup_params['translation']]['Mmenu4_sub4_1']}{cnst.INPUT_SIGN}")
                                        cnst.player_name = f"{Fore.LIGHTYELLOW_EX}{name}{cnst.DEFAULT_COLOR}"

                                        # Randomize if name is empty
                                        if name == '':
                                            func.name_randomizer()

                                    # Randomize atributes
                                    elif choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                        'Mmenu4_sub5']:

                                        print(gb.infoboook[cnst.setup_params['translation']][
                                                  'Mmenu4_sub5_1'])

                                        func.get_player_par()  # get new randomized player stats
                                        func.show_player_stats()
                                        input(f'\r{cnst.INPUT_SIGN}')

                                    elif choice_settings == gb.infoboook[cnst.setup_params['translation']]['return']:
                                        main_menu()

                                    # Check for updates
                                    elif choice_settings == gb.infoboook[cnst.setup_params['translation']][
                                        'Mmenu4_sub6']:
                                        update_state = func.check_for_update()
                                        if update_state:
                                            print(gb.infoboook[cnst.setup_params['translation']][
                                                      'Mmenu4_sub6_1'])

                                        elif not update_state:
                                            print(gb.infoboook[cnst.setup_params['translation']][
                                                      'Mmenu4_sub6_2'])

                                        input(f'\r{cnst.INPUT_SIGN}')

                    # Exit game
                    elif choice_main_menu == gb.infoboook[cnst.setup_params['translation']]['Mmenu5']:
                        choice2 = input(
                            f"{gb.infoboook[cnst.setup_params['translation']]['Mmenu5_sub1_1']} [Y/N]:").lower()
                        if choice2.lower() == "y":
                            pygame.mixer.music.fadeout(800)
                            func.clear_terminal()
                            exit(0)

                    # ADDITIONAL DEV FUNCTIONALITY
                    # evaluating functions in paragraphs.py
                    elif choice_main_menu == f'{cnst.SPECIAL_COLOR}test_paragraph{cnst.DEFAULT_COLOR}':
                        if os.path.exists(cnst.DUMMY_GAMESTATE_NAME):
                            # set active gameplay to dummy file
                            cnst.setup_params["active_gameplay"] = str(cnst.DUMMY_GAMESTATE_NAME)
                            func.log_event(f"set active gameplay to {cnst.DUMMY_GAMESTATE_NAME}")
                            # prg._xx()  # calling placeholder function # Old call
                            func.jump_paragraph_xx() # New call

                        else:
                            func.error_message('', f"Dummy gamestate file was not found. Enable 'use_dummy' in config.\
                            \nPlease close game, modify {cnst.CFG_NAME} and try again.")
                            input(cnst.INPUT_SIGN)

                    # configuring config.json file
                    elif choice_main_menu == f'{cnst.SPECIAL_COLOR}configure setup file{cnst.DEFAULT_COLOR}':
                        func.clear_terminal()
                        func.update_config_file(True)

                    # open documentation directory
                    elif choice_main_menu == f'{cnst.SPECIAL_COLOR}project documentation{cnst.DEFAULT_COLOR}':
                        func.clear_terminal()
                        func.open_dir(cnst.DOCUMENTATION_DIR)

                    # open gamestate directory
                    elif choice_main_menu == f'{cnst.SPECIAL_COLOR}show gamestate directory{cnst.DEFAULT_COLOR}':
                        func.clear_terminal()
                        func.open_dir(cnst.GAMESTATE_DIR)

                    # restore default config
                    elif choice_main_menu == f'{cnst.SPECIAL_COLOR}restore default config{cnst.DEFAULT_COLOR}':
                        func.clear_terminal()
                        func.update_config_file(backup=True)


if __name__ == '__main__':
    """
    ADDITIONAL LOGIC for DEVELOPER MODE
    If the dev_mode variable is set to True, some useful information is displayed,
    including the setup parameters file name at the beggining, documentation path, debug messages and so on.
    """
    if cnst.setup_params['dev_mode']:
        # Version of menu template with enabled annotations
        template = "({}) {} - {}"

        print(f"\n{cnst.SPECIAL_COLOR}Setup parameters loaded from file: {Fore.YELLOW}{cnst.CFG_NAME}{Style.RESET_ALL}")

        # Print the key-value pairs with variable length formatting
        for key, value in cnst.setup_params.items():
            print(f"- {key.ljust(max(len(str(key)) for key in cnst.setup_params.keys()))} - {value}")

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
        # Version of menu without enabled annotations
        template = "({}) {}"

    # time for start sequence: 23.1 seconds
    if cnst.setup_params['start_sequence']:
        # loading background music
        func.get_music('menu')

        # start sequence
        time.sleep(1.4)
        messages = ['Jacek Ciesielski\r', 'Filip Pawłowski', 'presents...', 'DRESZCZ - GRA PARAGRAFOWA']
        for message in messages:
            print(message)
            time.sleep(5.4)
    else:
        func.get_music('main')

    # randomize new player parameters
    func.get_player_par()

    # if no game states are found hide the "continue" and "load game" options in the menu
    func.get_game_state('init')

    # if config.json not found, restore backup
    try:
        with open(cnst.CFG_NAME, 'r') as json_file:
            _ = json_file.readable()

    except FileNotFoundError as e:
        func.error_message(str(e), f"An error occurred while updating the setup file")
        func.debug_message("config.json not found, restoring...")
        func.update_config_file(manual=False, backup=True)

    # enter main menu loop
    main_menu()
