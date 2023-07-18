# DRESZCZ

**Original author**: Jacek Ciesielski  
**Adaptation developer**: Filip Pawłowski (2023) - filippawlowski2012@gmail.com

GitHub
Repository: https://github.com/kotlecikmud/Dreszcz_Gra_Paragrafowa---text-based-game-adaptation.git

## Description

This is my first extensive project and serves as an entry point for learning Python programming. The goal is to create
an interactive version of the original game, which is heavily based on a paper book game created by Jacek Ciesielski, a
Polish nonlinear writer, in 1987. Translations are in works; mainly focusing on Polish and English.

"DRESZCZ" is a text-based adventure game developed in Python. It offers an immersive gameplay experience through a
captivating story presented in a choose-your-own-adventure style. Players make choices that determine the outcome of the
game, encountering various challenges, puzzles, and branching storylines along the way. The game features a main menu
with multiple options, including starting a new game, loading a saved game, accessing game rules, adjusting game
settings, and exiting the game. The main menu loop continuously prompts the player for input and performs actions based
on the selected menu option.

Additional functionality is available in developer mode, allowing developers to access test paragraphs, configure setup
files, view project documentation, and restore default setup files. The game incorporates various modules and files,
including `gamebook.py` (containing the main storybook), `paragraphs.py` (containing paragraph-specific
logic), `functions.py` (containing utility functions), `constants.py` (containing game constants), and the `colorama`
library for colored text output.

The code is organized into functions, each serving a specific purpose such as displaying menus, handling user input,
managing game state, and performing game actions. Docstrings are provided for key functions to describe their
functionality, parameters, and return values. The game also includes a start sequence with introductory messages and
background music, which can be toggled in the setup parameters.

## Developer Mode

Developer mode provides additional features and information for developers working on the game. It can be activated
temporarily by entering 'rayman' in the main menu to enable developer mode or 'mario' to disable it. In developer mode,
useful information such as setup parameters, documentation path, and debug messages are displayed.

## Setup Parameters

The game utilizes a setup file (`setup.json`) to store and retrieve various game parameters and settings. Developers can
modify the setup file manually to customize the game behavior or configure it using the main menu configuration option
file. The loaded setup parameters are displayed in developer mode.

## Documentation

The project documentation includes a PDF scan of the original book and an HTML adaptation also available
at [http://www.dudziarz.net](http://www.dudziarz.net). The documentation can be accessed through the 'project
documentation' option in the main menu, which simply opens the directory with documentation files.

## Dependencies

- Python 3.x
- pygame
- colorama

## Usage

1. Run `play.bat` file to ensure that the dependencies are installed and the game can be launched successfully.
2. Double-click on the `play.bat` file.
3. Review the output of the previous commands.
4. The game will be launched automatically.

Make sure that you have Python installed and available in your system's PATH environment variable.

Note: The code may require additional setup and configuration depending on the environment and platform.

# DATA MODULES

## `constants.py`

This file contains various constants used in the game.

### Constants

- `game_state_exists`: Indicates whether a game state exists.
- `potion`: Placeholder for a potion.
- `count`: Counter variable.
- `potion_count`: Number of potions.
- `choice_count`: Number of choices (universal).
- `gold_amount`: Initial amount of gold.
- `player_name`: Name of the player.
- `init_round_count`: Initial number of rounds.
- `round_count`: Counter for rounds.
- `s_count`: Counter for action points (luck).
- `w_count`: Counter for action points (stamina).
- `z_count`: Counter for action points (dexterity).
- `init_eatables_count`: Initial number of meals.
- `eatable_W_load`: Stamina load per meal.
- `and_his_name_is`: ASCII art text for the easter-egg title.
- `input_sign`: Sign indicating that the user should provide an input.
- `delay`: Time delay in seconds between printing each character in text.
- `entity_hit_mult`: Multiplier for entity level (default level is '1').
- `p_mult`: Player multiplier for damage calculation.
- `p_hit_val_`: Player hit value (-100 for development only).
- `e_hit_val_`: Enemy hit value.
- `def_txt_clr`: Default text color.
- `entity_txt_clr`: Color for entities.
- `special_txt_clr`: Color for headlines and particular special texts.
- `combat_txt_clr`: Color for combat text.
- `debug_txt_clr`: Color for debug messages.
- `error_txt_clr`: Color for error messages.
- `paths_doc`: Documentation about path definitions and audio file lists.
- `assets_audio_voice_pth`: Path to voice lines audio files.
- `assets_audio_effects_pth`: Path to sound effects.
- `assets_audio_music_pth`: Path to music.
- `game_state_dir_name`: Name of the directory used for game state saves.
- `setup_name`: Name of the setup script file.
- `audio_ext`: Extension of voice and sound effect files.
- `music_categories`: List of music categories.
- `music_tracks`: Dictionary storing lists of music tracks.
- `main_eq`: Dictionary representing main equipment.
- `choices_115`: Dictionary representing choices.
- `difficulty`: Default difficulty value.
- `difficulty_levels`: Dictionary mapping difficulty levels to multiplier values.
- `setup_params`: Dictionary containing setup parameter names.
- `setup()`: Function to load and assign setup parameters from a JSON file.
- `loaded_setup`: Loaded setup data.

## `obc_class.py`

This file contains classes for building entities and rooms in the game.

### Entity Class

#### `Entity`

A class representing an entity in the game.

Attributes:

- `name`: Name of the entity.
- `entity_z_init`: Initial count for action points (dexterity) of the entity.
- `entity_z_count`: Current count for action points (dexterity) of the entity.
- `entity_w_init`: Initial count for action points (stamina) of the entity.
- `entity_w_count`: Current count for action points (stamina) of the entity.
- `state`: Current state of the entity (alive or dead).
- `esc_possible`: Boolean indicating if escape is possible for the entity.

Methods:

- `die()`: Perform the die action for the entity.

### Room Class

#### `Room`

A class representing a room in the game.

Attributes:

- `room_num`: Number of the room.
- `room_state`: Current state of the room.
- `max_visit_count`: Maximum number of times the room can be visited.
- `visit_count`: Current visit count of the room.

## `entities.py`

This file contains the declarations of entities and rooms used in the game.

### Entity Declarations

#### `Entity`

The following entities are declared:

- `entity_002`: GARAZAN
- `entity_032`: WILKOLUDY
- `entity_069_1`: UPIÓR(1)
- `entity_069_2`: UPIÓR(2)
- `entity_092`: MINOTAUR
- `entity_098`: HERSZT GOBLINÓW
- `entity_107`: STRAŻNIK TAJEMNICY
- `entity_109`: KARMAA
- `entity_116`: ORK
- `entity_184`: DEMON
- `entity_238_1`: GREMLIN(1)
- `entity_238_2`: LICHA(2)
- `entity_238_3`: BRONGO(3)
- `entity_238_4`: ORKONIK(4)
- `entity_238_5`: SAMASKÓRA(5)
- `entity_317`: OGRE
- `entity_332`: TROLL
- `entity_344`: STRAŻNIK TAJEMNICY

Each entity has initial and current action points for luck and stamina, a state, and an escape possibility.

### Room Declarations

#### `Room`

- `room_268`: Room with the ID '268'.
- `room_310`: Room with the ID '310'.
- `room_331`: Room with the ID '331' (already visited).
- `room_336`: Room with the ID '336'.
- `room_364`: Room with the ID '364' and a maximum visit count of 2.
- `room_xxx`: Placeholder room with the ID 'xxx'.

## Credits

- Jacek Ciesielski: original author
- Filip Pawłowski (me): adaptation developer (2023)

## Contact

For any questions or suggestions, please feel free to contact me via email at filippawlowski2012@gmail.com.

Enjoy playing "DRESZCZ" - GRA PARAGRAFOWA!

**Note:**

The description above was mostly generated using GPT-3.5, a text generation tool. GPT-3.5 utilizes advanced artificial
intelligence to generate coherent texts based on input data. It is important to note that the information contained in
the description may not be 100% accurate and requires verification.

In addition to the description provided above, please note that the
documentation is also available in .py files as doc_strings.
