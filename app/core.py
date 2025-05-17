from app.menu import Menu
from menus.main_menu import MAIN_MENU
from database.db_manager import DatabaseManager
from app.utils import DB_CONFIG
from menus.main_menu import create_list, delete_list, show_list

class App:
    def __init__(self):
        self.db = DatabaseManager(DB_CONFIG)
        self.main_menu = Menu(MAIN_MENU)
        self.main_menu_actions = {
            "creerUneListe": lambda: create_list(self.db),
            "supprimerUneListe": lambda: delete_list(self.db),
            "afficherLesListes": lambda: show_list(self.db)
        }

    def run(self):
        while True:
            choice = self.main_menu.show_menu()
            if choice in self.main_menu_actions:
                self.main_menu_actions[choice]()