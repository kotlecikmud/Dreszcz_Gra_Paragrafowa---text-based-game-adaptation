from engine import start_game
from profiles import load_profiles, create_profile, select_profile
from game_io import load_game  # Added for loading game
from player import PlayerCharacter  # Added for creating new player instance
import os

if __name__ == "__main__":
    print("Witaj w grze paragrafowej DRESZCZ!")
    print("====================================")

    profiles_data = load_profiles()
    active_profile_path = None
    active_profile_name = None

    while True:  # Loop until a profile is set or user quits
        if profiles_data:
            print("\nDostępne profile:")
            for idx, name in enumerate(profiles_data.keys()):
                print(f"  {idx + 1}. {name}")

            action = (
                input(
                    "Wybierz profil, utwórz nowy, lub zakończ (wpisz numer, 'nowy', 'koniec'): "
                )
                .strip()
                .lower()
            )

            if action.isdigit():
                try:
                    profile_idx = int(action) - 1
                    profile_names = list(profiles_data.keys())
                    if 0 <= profile_idx < len(profile_names):
                        chosen_name = profile_names[profile_idx]
                        path = select_profile(chosen_name, profiles_data)
                        if path:
                            active_profile_name = chosen_name
                            active_profile_path = path
                            print(f"Wybrano profil: {active_profile_name}")
                            break
                        else:  # Should not happen if keys are from profiles_data
                            print("Błąd: Nie udało się wybrać profilu.")
                    else:
                        print("Nieprawidłowy numer profilu.")
                except ValueError:
                    print(
                        "Nieprawidłowe dane wejściowe."
                    )  # Should be caught by isdigit already
            elif action == "nowy":
                # Fall through to creation logic
                pass
            elif action == "koniec":
                print("Zamykanie gry.")
                exit()
            else:
                print("Nieznana akcja.")
                continue  # Restart loop

        # Creation logic (if no profiles or user chose 'nowy')
        if not active_profile_path:  # Check if profile not yet selected
            if not profiles_data:
                print("\nNie znaleziono istniejących profili.")
                create_choice = (
                    input("Czy chcesz utworzyć nowy profil? (tak/nie): ")
                    .strip()
                    .lower()
                )
                if create_choice != "tak":
                    print("Zamykanie gry, brak profilu do załadowania/utworzenia.")
                    exit()

            new_profile_name_input = input("Podaj nazwę dla nowego profilu: ").strip()
            if not new_profile_name_input:
                print("Nazwa profilu nie może być pusta.")
                continue  # Or ask again, or exit

            # create_profile handles sanitization and printing success/error
            if create_profile(new_profile_name_input):
                # Need to get the potentially sanitized name used by create_profile
                # For simplicity, assume input name is usable or create_profile uses it if valid
                # A robust way: create_profile could return the name it used.
                # For now, we re-load and try to select with the input name,
                # or use the input name directly if sanitization is minimal.
                profiles_data = load_profiles()  # Refresh data

                # Attempt to select the newly created profile
                # The name in profiles_data keys will be the sanitized one.
                # We need to find it if new_profile_name_input was sanitized.
                # For now, assume user enters a valid name or create_profile uses it.
                # A better approach: create_profile could return the actual name used.
                # Let's try to find it based on the input:
                created_profile_actual_name = None
                for p_name in profiles_data.keys():
                    # This is a simple check; might need more robust matching if sanitization is complex
                    if (
                        new_profile_name_input.lower() == p_name.lower()
                        or new_profile_name_input.replace(" ", "_")
                        == p_name.replace(" ", "_")
                    ):  # Basic heuristic
                        created_profile_actual_name = p_name
                        break

                if (
                    not created_profile_actual_name
                    and new_profile_name_input in profiles_data
                ):
                    created_profile_actual_name = new_profile_name_input

                if created_profile_actual_name:
                    path = select_profile(created_profile_actual_name, profiles_data)
                    if path:
                        active_profile_name = created_profile_actual_name
                        active_profile_path = path
                        # Message printed by create_profile, then:
                        print(f"Aktywny profil: {active_profile_name}")
                        break
                    else:
                        print(
                            f"Błąd: Nie udało się automatycznie wybrać nowo utworzonego profilu '{created_profile_actual_name}'. Spróbuj wybrać ręcznie."
                        )
                        # Loop will continue, user can select manually
                else:
                    # If create_profile succeeded but we can't find the name, something is off or sanitization changed it significantly.
                    # The user will be prompted to select from the list again in the next iteration if it was indeed created.
                    print(
                        f"Profil mógł zostać utworzony z inną nazwą z powodu sanitacji. Sprawdź listę."
                    )

            else:
                # Creation failed, message printed by create_profile
                try_again = (
                    input("Czy chcesz spróbować utworzyć profil ponownie? (tak/nie): ")
                    .strip()
                    .lower()
                )
                if try_again != "tak":
                    print("Zamykanie gry.")
                    exit()
                # else loop continues

    player_instance_to_start = None
    if active_profile_path and active_profile_name:
        print(
            f"\nAktywny profil: {active_profile_name} (Dane w: {active_profile_path})"
        )

        loaded_player = load_game(active_profile_path)
        if loaded_player:
            print("Znaleziono zapisany stan gry dla tego profilu.")
            while True:
                choice = (
                    input(
                        "Czy chcesz kontynuować (k) poprzednią grę, czy rozpocząć nową (n)? (k/n): "
                    )
                    .strip()
                    .lower()
                )
                if choice == "k":
                    player_instance_to_start = loaded_player
                    print("Wznawianie zapisanej gry...")
                    break
                elif choice == "n":
                    print("Rozpoczynanie nowej gry dla tego profilu...")
                    player_instance_to_start = PlayerCharacter(is_new_character=True)
                    break
                else:
                    print("Nieprawidłowy wybór. Wpisz 'k' lub 'n'.")
        else:
            print(
                "Brak zapisanego stanu gry dla tego profilu. Rozpoczynanie nowej gry..."
            )
            player_instance_to_start = PlayerCharacter(is_new_character=True)

        if player_instance_to_start:
            start_game(active_profile_path, player_instance_to_start)
        else:
            # This case should ideally not be reached if logic above is correct
            print("Nie udało się przygotować gracza. Zamykanie gry.")

    else:
        print("\nNie wybrano żadnego profilu. Zamykanie gry.")

    print("\n====================================")
    print("Dziękujemy za grę!")
