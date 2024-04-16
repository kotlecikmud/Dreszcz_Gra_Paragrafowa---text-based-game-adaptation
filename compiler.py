import os, shutil
from datetime import datetime as dt

version = dt.now().strftime("%d%m%y.%H%M%S")
os.system(f'pyinstaller --onefile --icon icon.ico -n Dreszcz_{version} menu.py functions.py constants.py paragraphs.py entities.py obj_class.py gamebook.py')



