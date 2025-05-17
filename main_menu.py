from utils import execute_db, clear
import time
from class_menu import Menu
from show_list_menu import SHOW_LIST_MENU, SHOW_LIST_MENU_ACTIONS

def create_list():
    clear()
    print("=== Création d'une liste de course ===\n")
    list_name = input("Nom de la liste (entrée pour annuler): ").strip()
    if list_name == "":
        return
    elif len(list_name) > 32:
        print("Erreur : choix invalide.")
        time.sleep(0.5)
        return
    execute_db(f"INSERT INTO `list` (`name`) VALUES ('{list_name}')")
    show_list()

def delete_list():
    clear()
    execute_db("DELETE FROM `list`")  
  
def show_list():
    DB = execute_db("SELECT `name` FROM list")
    list_name = DB.fetchall()

    if len(list_name) == 0:
        print("Aucune liste de course trouvée.")
        time.sleep(0.5)
        return

    clear()
    print("=== Listes de course ===\n")
    for l in list_name:
        print("•", l[0].capitalize())
    print()
    show_list_menu = Menu(SHOW_LIST_MENU)
    choice = show_list_menu.show_menu(False)

    if choice in SHOW_LIST_MENU_ACTIONS:
        SHOW_LIST_MENU_ACTIONS[choice]()


MAIN_MENU = [
    "=== Menu Listes de Courses ===",
    "Créer une liste",
    "Supprimer une liste",
    "Afficher les listes"
]

MAIN_MENU_ACTIONS = {
    "creerUneListe": create_list,
    "supprimerUneListe": delete_list,
    "afficherLesListes": show_list
}