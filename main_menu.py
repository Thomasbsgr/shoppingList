from utils import execute_db, clear
import time
from class_menu import Menu
from show_list_menu import SHOW_LIST_MENU, SHOW_LIST_MENU_ACTIONS

def createList():
    clear()
    print("=== Création d'une liste de course ===\n")
    name = input("Nom de la liste (entrée pour annuler): ").strip()
    if name == "":
        return
    elif len(name) > 32:
        print("Erreur : choix invalide.")
        time.sleep(0.5)
        return
    execute_db(f"INSERT INTO `list` (`name`) VALUES ('{name}')")
    showList()

def deleteList():
    clear()
    execute_db("DELETE FROM `list`")  
  
def showList():
    DB = execute_db("SELECT `name` FROM list")
    list = DB.fetchall()

    if len(list) == 0:
        print("Aucune liste de course trouvée.")
        time.sleep(0.5)
        return

    clear()
    print("=== Listes de course ===\n")
    for l in list:
        print("•", l[0].capitalize())
    print()
    showListMenu = Menu(SHOW_LIST_MENU)
    choice = showListMenu.show_menu(False)

    if choice in SHOW_LIST_MENU_ACTIONS:
        SHOW_LIST_MENU_ACTIONS[choice]()


MAIN_MENU = [
    "=== Menu Listes de Courses ===",
    "Créer une liste",
    "Supprimer une liste",
    "Afficher les listes"
]

MAIN_MENU_ACTIONS = {
    "creerUneListe": createList,
    "supprimerUneListe": deleteList,
    "afficherLesListes": showList
}