from app.utils import clear
import time
from app.menu import Menu
from menus.show_list_menu import SHOW_LIST_MENU, rename_list, open_list, back

def create_list(db):
    clear()
    print("=== Création d'une liste de course ===\n")
    while True:
        list_name = input("Nom de la liste (entrée pour annuler): ").strip()
        cursor = db.execute("SELECT `name` FROM list")
        existing_lists = cursor.fetchall()
        if list_name == "":
            break
        elif len(list_name) > 32:
            print("Erreur : choix invalide.")
            time.sleep(0.5)
            break
        elif list_name.lower() in [l[0] for l in existing_lists]:
            print("Erreur : cette liste existe déjà.")
            time.sleep(0.5)
        else:
            db.execute(f"INSERT INTO `list` (`name`) VALUES ('{list_name.lower()}')")
            print(f"Liste '{list_name.capitalize()}' créée avec succès.")
            time.sleep(0.5)
            show_list(db)
            break

def delete_list(db):
    clear()
    db.execute("DELETE FROM `list`")  
  
def show_list(db):
    cursor = db.execute("SELECT `name` FROM list")
    list_name = cursor.fetchall()

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

    show_list_menu_action = {
    "renommerUneListe": lambda: rename_list(db),
    "ouvrirUneListe": lambda: open_list(db),
    "retour": back
    }

    if choice in show_list_menu_action:
        show_list_menu_action[choice]()


MAIN_MENU = [
    "=== Menu Listes de Courses ===",
    "Créer une liste",
    "Supprimer une liste",
    "Afficher les listes"
]