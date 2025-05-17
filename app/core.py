from menu import Menu
from menus.main_menu import MAIN_MENU, MAIN_MENU_ACTIONS

class App:
    def __init__(self):
        self.main_menu = Menu(MAIN_MENU)
        self.main_menu_actions = MAIN_MENU_ACTIONS

    def run(self):
        while True:
            choice = self.main_menu.show_menu()
            if choice in self.main_menu_actions:
                self.main_menu_actions[choice]()