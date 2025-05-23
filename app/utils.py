import os
import unicodedata
import re
import json

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "shopping_list_app"
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def to_camel_case(text):
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