import os
import unicodedata
import re
import json
import mysql.connector

while True:
    try:
        CONN = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="shopping_list_app"
        )
        break
    except mysql.connector.Error as e:
        print(f"[ERREUR CONNEXION DB] {e}")
        input()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def toCamelCase(text):
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    parts = text.strip().split()

    if not parts:
        return ""

    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])

def charger_liste(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

def sauvegarder_liste(path, liste):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(liste, f, indent=4)

def execute_db(query):
    while True:
        try:
            db = CONN.cursor()
            db.execute(query)
            if query.strip().split(" ")[0].upper() != "SELECT":
                CONN.commit()
            return db
        except mysql.connector.Error as err:
            print(f"[ERREUR SQL] {err}")
            input("Appuyez sur Entrée pour continuer...")