"""
This script serves as a prototype for a GUI application for a game called Dreszcz.
"""

__version__ = "00.01.00.00"

import tkinter as tk

# Constants for resolutions and other settings
RESOLUTIONS = {
    "1280x720": "1280x720",
    "1920x1080": "1920x1080",
    "Fullscreen": True,
}

# Create the main window
root = tk.Tk()
root.title("Game Menu")
root.geometry("1280x720")  # Set default resolution to 1280x720

# Create a label for debug messages
debug_label = tk.Label(root, text="", anchor="w")
debug_label.pack(side="left", padx=10, pady=10)


# Functions
def update_debug_message(message):
    # Update the debug message label with a new message
    debug_label.config(text=message)


def start_new_game():
    update_debug_message("Starting a new game...")


def load_saved_game():
    update_debug_message("Loading a saved game...")


def exit_game():
    update_debug_message("Exiting game...")
    root.quit()


def change_resolution():
    # Create a new window for resolution settings
    resolution_window = tk.Toplevel(root)
    resolution_window.title("Change Resolution")

    # Define a callback function for button clicks
    def set_resolution(resolution):
        if resolution == True:
            # Enable fullscreen mode
            root.attributes("-fullscreen", True)
        else:
            # Set the desired resolution
            root.geometry(resolution)
        update_debug_message(f"Resolution changed to {resolution}.")
        resolution_window.destroy()  # Close the settings window

    # Create buttons for each resolution option
    for resolution, value in RESOLUTIONS.items():
        button = tk.Button(resolution_window, text=resolution, command=lambda v=value: set_resolution(v))
        button.pack(padx=10, pady=5)


def change_volume():
    update_debug_message("Changing volume...")


def change_controls():
    update_debug_message("Changing controls...")


def return_to_main_menu():
    # Switch back to the main menu
    show_main_menu()


def show_main_menu():
    # Hide all settings buttons and show main menu buttons
    new_game_button.grid(row=0, column=0)
    load_game_button.grid(row=1, column=0)
    exit_button.grid(row=2, column=0)
    settings_button.grid(row=3, column=0)

    resolution_button.grid_remove()
    volume_button.grid_remove()
    controls_button.grid_remove()
    return_button.grid_remove()


def show_settings_menu():
    # Hide main menu buttons and show settings buttons
    new_game_button.grid_remove()
    load_game_button.grid_remove()
    exit_button.grid_remove()
    settings_button.grid_remove()

    resolution_button.grid(row=0, column=0)
    volume_button.grid(row=1, column=0)
    controls_button.grid(row=2, column=0)
    return_button.grid(row=3, column=0)


# Create a frame for the menu buttons
menu_frame = tk.Frame(root)
menu_frame.pack(pady=20)

# Create main menu buttons
new_game_button = tk.Button(menu_frame, text="New Game", command=start_new_game, width=15, height=2)
load_game_button = tk.Button(menu_frame, text="Load Game", command=load_saved_game, width=15, height=2)
exit_button = tk.Button(menu_frame, text="Exit", command=exit_game, width=15, height=2)
settings_button = tk.Button(menu_frame, text="Settings", command=show_settings_menu, width=15, height=2)

# Add main menu buttons to the frame initially
new_game_button.grid(row=0, column=0)
load_game_button.grid(row=1, column=0)
settings_button.grid(row=2, column=0)
exit_button.grid(row=3, column=0)

# Create settings submenu buttons
resolution_button = tk.Button(menu_frame, text="Resolution", command=change_resolution, width=15, height=2)
volume_button = tk.Button(menu_frame, text="Volume", command=change_volume, width=15, height=2)
controls_button = tk.Button(menu_frame, text="Controls", command=change_controls, width=15, height=2)
return_button = tk.Button(menu_frame, text="Return", command=return_to_main_menu, width=15, height=2)

# Initially hide settings buttons
resolution_button.grid_remove()
volume_button.grid_remove()
controls_button.grid_remove()
return_button.grid_remove()

# Start the main event loop
root.mainloop()
