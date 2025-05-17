from app.core import App

if __name__ == "__main__":
    app = App()
    app.run()


# --- app/core.py ---

from app.menu import Menu
from menus.main_menu import MAIN_MENU, create_list, delete_list, show_list
from database.db_manager import DatabaseManager
from app.utils import DB_CONFIG

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


# --- database/db_manager.py ---

import mysql.connector

class DatabaseManager:
    def __init__(self, config: dict):
        while True:
            try:
                self.conn = mysql.connector.connect(**config)
                break
            except mysql.connector.Error as e:
                print(f"[ERREUR CONNEXION DB] {e}")
                input("Réessayer ? (Entrée)")

    def execute(self, query: str, params: tuple = None):
        while True:
            try:
                cursor = self.conn.cursor()
                cursor.execute(query, params if params else ())
                if query.strip().upper().startswith("SELECT"):
                    return cursor
                self.conn.commit()
                return cursor
            except mysql.connector.Error as e:
                print(f"[ERREUR SQL] {e}")
                input("Appuyez sur Entrée pour continuer...")


# --- menus/main_menu.py ---

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
            db.execute("INSERT INTO `list` (`name`) VALUES (%s)", (list_name.lower()))
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


# --- menus/show_list_menu.py ---

from app.utils import clear
import time
from menus.open_list_menu import OPEN_LIST_MENU, add_product, delete_product, show_products, back
from app.menu import Menu

def select_list(db, question: str = "Séléctionnez une liste: "):
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

def rename_list(db):
    selected_list_name = select_list(db, "Sélectionnez une liste à renommer (ou entrée pour quitter): ")

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
    selected_list_name = select_list(db, "Sélectionnez une liste à ouvrir (ou entrée pour quitter): ")
    
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


# --- menus/open_list_menu.py ---

def add_product(db):
    print("Ajouter un produit")

def delete_product(db):
    print("Supprimer un produit")

def show_products(db):
    print("Afficher les produits")

def back():
    return

OPEN_LIST_MENU = [
    "Ajouter un produit",
    "Supprimer un produit",
    "Afficher les produits",
    "Retour"
]