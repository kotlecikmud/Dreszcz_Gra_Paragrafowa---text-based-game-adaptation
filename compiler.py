import os, shutil
from colorama import Fore, Style
from datetime import datetime as dt

version = dt.now().strftime("%d%m%y.%H%M%S")  # generate version number based on timestamp
os.system(
    f'pyinstaller --onefile --icon simple.ico -n Dreszcz_{version} menu.py functions.py constants.py entities.py obj_class.py gamebook.py')  # call system command for pyinstaller packer

src_path = f'e:/PycharmProjects/Dreszcz_Gra_Paragrafowa/dist/Dreszcz_{version}.exe'
dst_path = f'e:/PycharmProjects/Dreszcz_Gra_Paragrafowa/Dreszcz_{version}.exe'
dst_file_to_delete = f'e:/PycharmProjects/Dreszcz_Gra_Paragrafowa/Dreszcz_{version}.spec'

print(Fore.BLUE)  # change color of console output
try:  # logic for cleaning files after compilations
    shutil.move(src_path, dst_path)
    print("Plik został pomyślnie przeniesiony.")

    if os.path.exists(dst_file_to_delete):
        os.remove(dst_file_to_delete)
        print(f"Plik Dreszcz_{version}.spec został usunięty.")
    else:
        print(f"Plik Dreszcz_{version}.spec nie istnieje w lokalizacji docelowej.")

except FileNotFoundError:
    print("Nie można znaleźć pliku źródłowego.")
except PermissionError:
    print("Brak uprawnień do przeniesienia pliku.")
except Exception as e:
    print("Wystąpił błąd podczas przenoszenia pliku:", str(e))
print(Style.RESET_ALL)  # reset color of console output
