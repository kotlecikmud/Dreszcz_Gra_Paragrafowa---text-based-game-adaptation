import os, shutil
from datetime import datetime as dt

version = dt.now().strftime("%d%m%y.%H%M%S")
os.system(
    f'pyinstaller --onefile --icon icon.ico -n Dreszcz_{version} menu.py functions.py constants.py entities.py obj_class.py gamebook.py')

src_path = f'e:/PycharmProjects/Dreszcz_Gra_Paragrafowa/dist/Dreszcz_{version}.exe'
dst_path = f'e:/PycharmProjects/Dreszcz_Gra_Paragrafowa/Dreszcz_{version}.exe'
dst_file_to_delete = f'e:/PycharmProjects/Dreszcz_Gra_Paragrafowa/Dreszcz_{version}.spec'

try:
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
