# Project To-Do List

Put 'x' in square brackets when entry completed: <b>[x]</b>

# `GLOBAL:`

- [ ] Implement new translations sub-dictionary for action choices
- [ ] implement new sub-dictionary for translations for all strings printed to player during the game in functions.py

# `MODULE SPECIFIC:`

### `menu.py`

- [ ] ---

### `paragraphs.py`

- [x] Address a bug where the game becomes unresponsive when a player accesses prg.296(). Although the music continues
  to play, the game cannot progress beyond this point. (solved: missing else:break in eatables())
- [ ] fix room_364 visit counting (1 additional not needed when deciding if user wants to enter)

### `functions.py`

- [ ] implement mechanism for checking if active gameplay file saved in setup still exists, if not, disable option "
  Continue"
- [ ] implement LoadingAnimation class to be used instead of functions.loading()
- [ ] fix bounciness of pth_selector skipping and combat_main problem that was probably caused by removing loading()

### `constants.py`

- [ ] add translations to equipment and choices dictionaries (maybe think on more elegant way if possible)
- [ ] change constants name to upper case (includes changing this across whole project)

### `obj_class.py`

- [ ] Fix bad implementation problem with playing audio in obj_class.die()

### `gamebook.py`

- [ ] Fill missing gameboook{} entrys (for now in Polish sub-dictionary; to be translated when everything works)

### `entities.py`

- [ ] Rework entities to be inside of dictionary insetad of separate objects (not sure if this will work, but worth a
  try)