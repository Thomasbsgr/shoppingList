from utils import execute_db, clear
import time

def rename_list():
    clear()
    DB = execute_db("SELECT `name` FROM list")
    list_db = DB.fetchall()
    for i, l in enumerate(list_db, start=1):
        print(f"{i}. {l[0].capitalize()}")
    
    while True:
        list = input("\nSélectionnez une liste à renommer (ou entrée pour quitter): ").strip()
        if list == "":
            return
        if list.isdigit():
            idx = int(list) - 1
            if 0 <= idx < len(list_db):
                list = list_db[idx][0]
                while True:
                    new_name = input(f"\nEntrez le nouveau nom pour la liste '{list}'\n(ou entrée pour quitter): ").strip()
                    if new_name == "":
                        return
                    else:
                        execute_db(f"UPDATE `list` SET `name` = '{new_name}' WHERE `name` = '{list}'")
                        print(f"Liste '{list}' renommée en '{new_name}'.")
                        time.sleep(0.5)
                        return
            else:
                print("Erreur : choix invalide.")
                time.sleep(0.5)
def open_list():
    return

def back():
    return

SHOW_LIST_MENU = [
    "========================",
    "Renommer une liste",
    "Ouvrir une liste",
    "Retour"
]

SHOW_LIST_MENU_ACTIONS = {
    "renommerUneListe": rename_list,
    "ouvrirUneListe": open_list,
    "retour": back
}