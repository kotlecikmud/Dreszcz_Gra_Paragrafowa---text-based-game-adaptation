import random
import pickle # For serializing PlayerCharacter instances

def roll_k6(num_dice=1):
    """Rolls num_dice six-sided dice and returns the sum."""
    return sum(random.randint(1, 6) for _ in range(num_dice))

class PlayerCharacter:
    def __init__(self, is_new_character: bool = True):
        if is_new_character:
            # Initialize stats for a new character
            Z = roll_k6(1) + 6
            W = roll_k6(2) + 12
            S = roll_k6(1) + 6

            self.stats = {'dexterity': Z, 'stamina': W, 'luck': S}
            self.initial_stats = self.stats.copy()

            print("--- Tworzenie Postaci ---")
            print(f"Początkowa Zręczność (Z): {self.stats['dexterity']} (rzut 1K6+6)")
            print(f"Początkowa Wytrzymałość (W): {self.stats['stamina']} (rzut 2K6+12)")
            print(f"Początkowe Szczęście (S): {self.stats['luck']} (rzut 1K6+6)")

            # Elixir selection
            valid_elixirs = {
                "ZRĘCZNOŚCI": "ZRĘCZNOŚCI", "Z": "ZRĘCZNOŚCI",
                "WYTRZYMAŁOŚCI": "WYTRZYMAŁOŚCI", "W": "WYTRZYMAŁOŚCI", "WYTRZYMALOSCI": "WYTRZYMAŁOŚCI",
                "SZCZĘŚCIA": "SZCZĘŚCIA", "S": "SZCZĘŚCIA", "SZCZESCIA": "SZCZĘŚCIA"
            }
            while True:
                elixir_choice_input = input("Wybierz eliksir (dostępne: Zręczności (Z), Wytrzymałości (W), Szczęścia (S)): ").strip().upper()
                if elixir_choice_input in valid_elixirs:
                    self.elixir_type = valid_elixirs[elixir_choice_input]
                    break
                else:
                    print("Nieprawidłowy wybór. Wpisz Z, W, S lub pełną nazwę (np. 'Zręczności').")

            self.elixir_uses_left = 2
            self.inventory = ["miecz", "tarcza", "plecak na Prowiant", "latarnia", f"eliksir {self.elixir_type.lower()}"]
            self.provisions = 8
            self.gold = 0
            self.current_paragraph_id = 1 # Default starting paragraph for new characters
            
            print(f"Wybrano eliksir: {self.elixir_type.capitalize()}. Masz {self.elixir_uses_left} użycia.")
            print("-------------------------")
        else:
            # This path is taken if is_new_character=False, meaning the object is being
            # re-initialized by pickle or similar, or we intend to populate it from loaded data.
            # Ensure essential attributes exist if they weren't set by the loading mechanism itself.
            # However, pickle will restore all attributes, so this 'else' block might only be
            # relevant if one were to call PlayerCharacter(is_new_character=False) manually
            # without immediately populating it from a loaded state.
            # For pickle, __init__ is typically NOT called on unpickling if the object was pickled
            # normally. If it IS called (e.g. due to specific __getnewargs__ or custom unpickling),
            # then we must ensure vital attributes are at least initialized to default/empty states.
            # Given standard pickling, this 'else' might not be strictly necessary for load_game.
            if not hasattr(self, 'stats'):
                self.stats = {}
            if not hasattr(self, 'initial_stats'):
                self.initial_stats = {}
            if not hasattr(self, 'elixir_type'):
                self.elixir_type = "" # Default empty value
            if not hasattr(self, 'elixir_uses_left'):
                self.elixir_uses_left = 0
            if not hasattr(self, 'inventory'):
                self.inventory = []
            if not hasattr(self, 'provisions'):
                self.provisions = 0
            if not hasattr(self, 'gold'):
                self.gold = 0
            if not hasattr(self, 'current_paragraph_id'):
                self.current_paragraph_id = 1 # Or some other safe default

    def display_stats(self):
        # Ensure initial_stats exists for display, especially if character was loaded
        # and somehow __init__(is_new_character=False) path was taken and didn't fully init.
        # This is a defensive check. For standard pickle, initial_stats would be restored.
        dex_initial = self.initial_stats.get('dexterity', self.stats.get('dexterity', 0))
        sta_initial = self.initial_stats.get('stamina', self.stats.get('stamina', 0))
        luc_initial = self.initial_stats.get('luck', self.stats.get('luck', 0))

        print("\n=== TWOJA POSTAĆ ===")
        print(f"  Zręczność (Z):    {self.stats.get('dexterity', 0):<2} / {dex_initial}")
        print(f"  Wytrzymałość (W): {self.stats.get('stamina', 0):<2} / {sta_initial}")
        print(f"  Szczęście (S):    {self.stats.get('luck', 0):<2} / {luc_initial}")
        print(f"  Prowiant:         {self.provisions}")
        print(f"  Złoto:            {self.gold}")

        elixir_info = f"Eliksir {self.elixir_type.capitalize()} ({self.elixir_uses_left} użyć)" if self.elixir_uses_left > 0 else "Brak eliksiru"
        inventory_for_display = [item for item in self.inventory if not item.startswith("eliksir ")]
        if self.elixir_uses_left > 0 and f"eliksir {self.elixir_type.lower()}" not in inventory_for_display :
             # This case should ideally not happen if inventory is managed correctly with elixir uses
             pass # Elixir info string already covers it

        print(f"  {elixir_info}")
        print(f"  Ekwipunek:        {', '.join(inventory_for_display) if inventory_for_display else 'brak'}")
        print("====================")

    def use_elixir(self):
        elixir_inventory_name = f"eliksir {self.elixir_type.lower()}"
        if self.elixir_uses_left <= 0:
            print("Nie masz więcej użyć eliksiru.")
            return
        if elixir_inventory_name not in self.inventory :
             print(f"Nie posiadasz już eliksiru {self.elixir_type.capitalize()} w ekwipunku.") # Should align with uses_left
             return

        print(f"Używasz eliksiru {self.elixir_type.capitalize()}...")
        if self.elixir_type == "ZRĘCZNOŚCI":
            self.stats['dexterity'] = self.initial_stats['dexterity']
            print(f"Twoja Zręczność została przywrócona do {self.stats['dexterity']}.")
        elif self.elixir_type == "WYTRZYMAŁOŚCI":
            self.stats['stamina'] = self.initial_stats['stamina']
            print(f"Twoja Wytrzymałość została przywrócona do {self.stats['stamina']}.")
        elif self.elixir_type == "SZCZĘŚCIA":
            self.stats['luck'] = self.initial_stats['luck'] + 1
            print(f"Twoje Szczęście zostało przywrócone i podniesione do {self.stats['luck']}.")

        self.elixir_uses_left -= 1
        print(f"Pozostało użyć eliksiru: {self.elixir_uses_left}.")

        if self.elixir_uses_left == 0:
            try:
                self.inventory.remove(elixir_inventory_name)
                print(f"Zużyłeś ostatnią porcję eliksiru {self.elixir_type.capitalize()}. Eliksir został usunięty z ekwipunku.")
            except ValueError:
                pass

        # Ensure stats (except luck's special rule) don't exceed initial values
        self.stats['dexterity'] = min(self.stats['dexterity'], self.initial_stats['dexterity'])
        self.stats['stamina'] = min(self.stats['stamina'], self.initial_stats['stamina'])
        # Szczęście po użyciu eliksiru szczęścia może być initial_luck + 1.
        # Inne efekty nie powinny tego przekroczyć.
        max_luck = self.initial_stats['luck'] + 1 if self.elixir_type == "SZCZĘŚCIA" else self.initial_stats['luck']
        self.stats['luck'] = min(self.stats['luck'], max_luck)


    def eat_provision(self):
        if self.provisions > 0:
            self.stats['stamina'] = min(self.initial_stats['stamina'], self.stats['stamina'] + 4)
            self.provisions -= 1
            print(f"Zjadłeś prowiant. Twoja Wytrzymałość: {self.stats['stamina']}. Pozostało prowiantu: {self.provisions}.")
        else:
            print("Nie masz więcej prowiantu.")

    def change_stat(self, stat_name, value):
        """
        Changes a player's stat (dexterity, stamina, luck, gold, provisions).
        Ensures stamina and luck do not go below 0.
        Ensures dexterity, stamina, luck do not exceed initial values (except luck with elixir).
        """
        stat_name = stat_name.lower()
        if stat_name in self.stats:
            self.stats[stat_name] += value
            # Clamping
            if stat_name == 'stamina' or stat_name == 'luck':
                self.stats[stat_name] = max(0, self.stats[stat_name])

            if stat_name == 'dexterity':
                 self.stats[stat_name] = min(self.stats[stat_name], self.initial_stats['dexterity'])
            elif stat_name == 'stamina':
                 self.stats[stat_name] = min(self.stats[stat_name], self.initial_stats['stamina'])
            elif stat_name == 'luck': # Luck can be initial_luck + 1 due to elixir
                 self.stats[stat_name] = min(self.stats[stat_name], self.initial_stats['luck'] + 1 if self.elixir_type == "SZCZĘŚCIA" else self.initial_stats['luck'])

            print(f"Zmieniono {stat_name}: {value:+}. Nowa wartość: {self.stats[stat_name]}")

        elif stat_name == 'gold':
            self.gold += value
            self.gold = max(0, self.gold)
            print(f"Zmieniono złoto: {value:+}. Nowa ilość: {self.gold}")
        elif stat_name == 'proviant': # Using 'proviant' to match JSON action details
            self.provisions += value
            self.provisions = max(0, self.provisions)
            print(f"Zmieniono prowiant: {value:+}. Nowa ilość: {self.provisions}")
        else:
            print(f"Próba zmiany nieznanej statystyki/zasobu: {stat_name}")

    def add_item(self, item_name, quantity=1):
        """Adds an item or gold to the player."""
        item_name_lower = item_name.lower()
        if "złoto" in item_name_lower or "sztuk złota" in item_name_lower:
            # Extract amount if specified like "10 sztuk złota"
            amount_match = re.search(r'(\d+)', item_name)
            if amount_match:
                actual_quantity = int(amount_match.group(1))
            else:
                actual_quantity = quantity # Default if parsing fails

            self.gold += actual_quantity
            print(f"Otrzymano {actual_quantity} złota. Aktualne złoto: {self.gold}")
        else:
            # For simplicity, inventory items are unique strings. Quantity > 1 handled by multiple entries if needed.
            # Or, for stackable items, inventory could be a dict: self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity
            # Current implementation uses a list, so just add.
            if item_name not in self.inventory:
                self.inventory.append(item_name)
                print(f"Otrzymano: {item_name}.")
            else:
                # If item is already there, maybe it's stackable or a duplicate
                print(f"Już posiadasz {item_name}, otrzymano kolejny.")
                self.inventory.append(item_name) # Example: allow multiple of same named item if not unique

    def remove_item(self, item_name, quantity=1):
        """Removes an item or gold from the player."""
        item_name_lower = item_name.lower()
        if "złoto" in item_name_lower or "sztuk złota" in item_name_lower:
            amount_match = re.search(r'(\d+)', item_name)
            if amount_match:
                actual_quantity = int(amount_match.group(1))
            else:
                actual_quantity = quantity

            if self.gold >= actual_quantity:
                self.gold -= actual_quantity
                print(f"Stracono {actual_quantity} złota. Pozostało złota: {self.gold}")
            else:
                print(f"Nie masz wystarczająco złota, by stracić {actual_quantity}. Tracisz wszystko ({self.gold}).")
                self.gold = 0
        else:
            if item_name in self.inventory:
                try:
                    # For items with quantity > 1, this would need adjustment if inventory was a dict
                    self.inventory.remove(item_name)
                    print(f"Stracono: {item_name}.")
                except ValueError:
                     pass # Should not happen if "in self.inventory" is true for list.
            else:
                print(f"Nie posiadasz w ekwipunku: {item_name} (do stracenia).")


if __name__ == '__main__':
    # Example Usage
    import re # Added for add_item/remove_item gold parsing
    player = PlayerCharacter()
    player.display_stats()

    print("\nTest użycia eliksiru Zręczności:")
    player.stats['dexterity'] -= 2 # Lower it first
    player.elixir_type = "ZRĘCZNOŚCI" # ensure type for test
    player.inventory.append("eliksir zręczności") # ensure item for test
    player.use_elixir()
    player.display_stats()

    print("\nTest jedzenia prowiantu:")
    player.stats['stamina'] = player.initial_stats['stamina'] - 6 # Lower stamina to test eating
    player.eat_provision()
    player.display_stats()

    print("\nTest zmiany statystyk:")
    player.change_stat('luck', -3)
    player.change_stat('gold', 10)
    player.change_stat('proviant', -1)
    player.display_stats()
    player.change_stat('stamina', 100) # Test cap
    player.display_stats()

    print("\nTest dodawania/usuwania przedmiotów:")
    player.add_item("magiczny miecz")
    player.add_item("100 sztuk złota")
    player.add_item("złoto", 5)
    player.display_stats()
    player.remove_item("tarcza")
    player.remove_item("50 sztuk złota")
    player.remove_item("złoto", 2)
    player.display_stats()
    player.remove_item("nieistniejacy przedmiot")
    player.remove_item("1000 sztuk złota") # Test removing more than available
    player.display_stats()
