import subprocess
from datetime import datetime, timedelta

def get_month_ago_date():
    # Oblicz datę sprzed miesiąca
    today = datetime.today()
    one_month_ago = today - timedelta(days=30)
    return one_month_ago.strftime("%Y-%m-%d")

def get_old_commits():
    # Pobierz listę commitów starszych niż miesiąc
    command = f'git log --before="{get_month_ago_date()}" --format=%H'
    output = subprocess.check_output(command, shell=True)
    return output.decode("utf-8").strip().split("\n")

def remove_old_commits(commits):
    # Usuń wybrane commity za pomocą interaktywnego trybu rebase
    for commit in commits:
        command = f'git rebase -p --onto {commit}~ {commit}'
        subprocess.run(command, shell=True)

def main():
    try:
        old_commits = get_old_commits()
        if not old_commits:
            print("Nie znaleziono commitów do usunięcia.")
            return

        print("Znalezione commity starsze niż miesiąc:")
        for commit in old_commits:
            print(commit)

        confirmation = input("Czy na pewno chcesz usunąć te commity? (tak/nie): ").strip().lower()
        if confirmation == "tak":
            remove_old_commits(old_commits)
            print("Commity zostały usunięte.")
        else:
            print("Operacja anulowana.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()
