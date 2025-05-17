def add_product():
    print("Ajouter un produit")

def delete_product():
    print("Supprimer un produit")

def show_products():
    print("Afficher les produits")

def back():
    return

OPEN_LIST_MENU = [
    "Ajouter un produit",
    "Supprimer un produit",
    "Afficher les produits",
    "Retour"
]

OPEN_LIST_MENU_ACTIONS = {
    "ajouterUnProduit": add_product,
    "supprimerUnProduit": delete_product,
    "afficherLesProduits": show_products,
    "retour": back
}