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
