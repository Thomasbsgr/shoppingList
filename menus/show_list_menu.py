from app.utils import clear
import time
from menus.open_list_menu import OPEN_LIST_MENU
from app.menu import Menu
from menus.open_list_menu import add_product, delete_product, show_products, back

def show_list(db, question: str = "Séléctionnez une liste: "):
    clear()
    DB = db.execute("SELECT `name` FROM list")
    list_db = DB.fetchall()
    for i, l in enumerate(list_db, start=1):
        print(f"{i}. {l[0].capitalize()}")

    while True:
        list_name = input("\n" + question).strip()
        if list_name == "":
            return
        if list_name.isdigit():
            idx = int(list_name) - 1
            if 0 <= idx < len(list_db):
                list_name = list_db[idx][0]
                return list_name
        else:
                print("Erreur : choix invalide.")
                time.sleep(0.5)
                return False

def rename_list(db):
    selected_list_name = show_list(db, "Sélectionnez une liste à renommer (ou entrée pour quitter): ")

    if not selected_list_name:
        return

    while True:
        new_name = input(f"\nEntrez le nouveau nom pour la liste '{selected_list_name}'\n(ou entrée pour quitter): ").strip()
        if new_name == "":
            return
        else:
            db.execute(f"UPDATE `list` SET `name` = '{new_name}' WHERE `name` = '{selected_list_name}'")
            print(f"Liste '{selected_list_name}' renommée en '{new_name}'.")
            time.sleep(0.5)
            return
            
def open_list(db):
    selected_list_name = show_list(db, "Sélectionnez une liste à ouvrir (ou entrée pour quitter): ")

    if not selected_list_name:
        return
    
    OPEN_LIST_MENU.insert(0, f"=== Liste de course '{selected_list_name.capitalize()}' ===")
    open_list_menu = Menu(OPEN_LIST_MENU)
    choice = open_list_menu.show_menu()
    open_list_menu_action = {
    "ajouterUnProduit": lambda: add_product(db),
    "supprimerUnProduit": lambda: delete_product(db),
    "afficherLesProduits": lambda: show_products(db),
    "retour": back
    }

    if choice in open_list_menu_action:
        open_list_menu_action[choice]()


def back():
    return

SHOW_LIST_MENU = [
    "========================",
    "Renommer une liste",
    "Ouvrir une liste",
    "Retour"
]