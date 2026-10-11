"""
Test de connexion a l'API Trello : cree une carte dans le tableau "Test Copilote",
liste "A faire". Lit la cle et le token depuis le fichier .env (jamais dans le code).

Usage :
    pip install requests python-dotenv
    python test_trello.py
"""

import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("TRELLO_API_KEY")
TOKEN = os.environ.get("TRELLO_TOKEN")
BASE_URL = "https://api.trello.com/1"

BOARD_NAME = "Test Copilote"
LIST_KEYWORD = "faire"  # trouve la liste "A faire" quelle que soit l'accentuation


def check_credentials():
    if not API_KEY or not TOKEN:
        sys.exit(
            "ERREUR : TRELLO_API_KEY ou TRELLO_TOKEN introuvable.\n"
            "Verifie ton fichier .env (a la racine du projet) : deux lignes, sans guillemets."
        )


def trello_get(path, **params):
    params.update({"key": API_KEY, "token": TOKEN})
    r = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
    r.raise_for_status()
    return r.json()


def trello_post(path, **params):
    params.update({"key": API_KEY, "token": TOKEN})
    r = requests.post(f"{BASE_URL}{path}", params=params, timeout=15)
    r.raise_for_status()
    return r.json()


def main():
    check_credentials()

    # 1. Verifier que les identifiants fonctionnent
    me = trello_get("/members/me", fields="username")
    print(f"Connecte a Trello en tant que : {me['username']}")

    # 2. Trouver le tableau
    boards = trello_get("/members/me/boards", fields="name")
    board = next((b for b in boards if b["name"] == BOARD_NAME), None)
    if not board:
        names = [b["name"] for b in boards]
        sys.exit(f"Tableau '{BOARD_NAME}' introuvable. Tableaux trouves : {names}")
    print(f"Tableau trouve : {board['name']}")

    # 3. Trouver la liste "A faire"
    lists = trello_get(f"/boards/{board['id']}/lists", fields="name")
    todo = next((l for l in lists if LIST_KEYWORD in l["name"].lower()), None)
    if not todo:
        names = [l["name"] for l in lists]
        sys.exit(f"Liste contenant '{LIST_KEYWORD}' introuvable. Listes trouvees : {names}")
    print(f"Liste trouvee : {todo['name']}")

    # 4. Creer une carte de test
    card = trello_post(
        "/cards",
        idList=todo["id"],
        name="Carte de test creee par Python",
        desc="Premiere carte creee automatiquement par le projet Copilote.",
    )
    print("Carte creee avec succes !")
    print(f"Lien : {card['url']}")


if __name__ == "__main__":
    main()
