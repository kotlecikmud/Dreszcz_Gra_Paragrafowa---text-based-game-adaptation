import os
import shutil
from constants import VER_FILE
from datetime import datetime as dt

ICON_FILE = r"_designs/face/icon.ico"

if not os.path.isfile(ICON_FILE):
    print("\n<!> No icon file found")
    exit(1)
else:
    print(f"\nIcon file found: {ICON_FILE}")

# read version number
with open(VER_FILE, 'r') as ver_f:
    __version__ = ver_f.readline()

build_number = dt.now().strftime("%d%m%y%H%M%S")

print(f"\nCompiling to file: Dreszcz_{__version__}_{build_number}")

os.system(
    f'pyinstaller --onefile --icon {ICON_FILE} -n Dreszcz_{__version__}_{build_number} menu.py functions.py constants.py paragraphs.py entities.py obj_class.py gamebook.py')
