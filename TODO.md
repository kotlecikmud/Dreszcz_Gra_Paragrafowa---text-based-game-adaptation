# Project To-Do List

Put 'x' in square brackets when entry completed: <b>[x]</b>

# `GLOBAL:`

- Implement new translations sub-dictionary for action choices
- Implement new sub-dictionary for translations for all strings printed to player during the game in functions.py
- Implement infinite background audio playlist randomizer in subprocess

# `MODULE SPECIFIC:`

### `menu.py`

- ---

### `paragraphs.py`

- fix room_364 visit counting (1 additional not needed when deciding if user wants to enter)

### `functions.py`

- implement LoadingAnimation class to be used instead of functions.loading()
- fix bounciness of pth_selector skipping and combat_main problem that was probably caused by removing loading()

### `constants.py`

- add translations to equipment and choices dictionaries (maybe think on more elegant way if possible)
- change constants name to upper case (includes changing this across whole project)

### `obj_class.py`

-

### `gamebook.py`

- Fill missing gameboook{} entrys (for now in Polish sub-dictionary; to be translated when everything works)

### `entities.py`

- Rework entities to be inside of dictionary insetad of separate objects (not sure if this will work, but worth a
  try)