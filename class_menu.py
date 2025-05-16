from utils import clear, toCamelCase
import time

class Menu:
    def __init__(self, menu: list = None):
        if menu is None:
            print("ERREUR: pas de menu encodé.")
            exit()
        self.menu = menu[:] + ["Exit"]
        self.title = self.menu[0] + "\n"

    def _display_options(self):
        for i, label in enumerate(self.menu[1:], start=1):
            if label == self.menu[-1]:
                print()
                print(f"E. {label}")
            else:
                print(f"{i}. {label}")

    def show_menu(self, clear_before: bool = True):
        while True:
            if clear_before:
                clear()
            print(self.title)
            self._display_options()
            choice = input("Votre choix : ").strip()
            if choice.isdigit():
                idx = int(choice)
                if 0 < idx < len(self.menu) - 1:
                    return toCamelCase(self.menu[idx])
            elif choice.lower() == "e":
                exit()
            print("Erreur : choix invalide.")
            time.sleep(0.5)