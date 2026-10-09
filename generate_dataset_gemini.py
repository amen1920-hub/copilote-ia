"""
Génère un dataset synthétique de paires (description de projet -> découpage en tâches)
pour entraîner l'Agent 1 (Cadrage). Utilise l'API Google Gemini (gratuite).

Le compte gratuit est limité à ~20 requêtes/jour sur gemini-3.8-flash.
Ce script sauvegarde sa progression : relance-le chaque jour, il reprend
automatiquement là où il s'était arrêté (pas de perte, pas de doublon).

Usage :
    pip install google-genai
    Crée ta clé sur https://aistudio.google.com/apikey
    PowerShell : $env:GEMINI_API_KEY="ta_clé_ici"
    python generate_dataset_gemini.py
"""

import json
import os
import time
from google import genai

# ---- Configuration ----
N_EXAMPLES = 100
OUTPUT_FILE = "data/raw/scoping_dataset.jsonl"
MODEL_NAME = "gemini-3.1-flash-lite"  # quota gratuit bien plus généreux (centaines/jour) que gemini-3.8-flash (20/jour)
DAILY_LIMIT = 100  # largement sous le quota réel de ce modèle (voir aistudio.google.com/rate-limit pour ton quota exact)

PROJECT_THEMES = [
    "application mobile de livraison de repas",
    "plateforme e-commerce B2C",
    "outil interne de gestion des congés",
    "site web vitrine pour une PME",
    "application de suivi de fitness",
    "chatbot de support client",
    "système de réservation pour un restaurant",
    "plateforme e-learning",
    "application de covoiturage",
    "outil de gestion de budget personnel",
    "réseau social pour une niche spécifique",
    "application de gestion de stock pour un entrepôt",
    "plateforme de freelance/marketplace de services",
    "application de méditation et bien-être",
    "outil CRM pour une petite entreprise",
    "application de recherche d'appartement",
    "plateforme de cours en ligne",
    "application de suivi de dépenses d'équipe",
    "site de petites annonces local",
    "application météo avec alertes personnalisées",
    "application de gestion de projet personnel",
    "plateforme de dons pour associations",
    "application de recettes de cuisine collaborative",
    "outil de suivi de maintenance industrielle",
    "application de covoiturage scolaire",
]
# Pour aller jusqu'à 100, on recycle les thèmes avec des variations d'indice
ALL_THEMES = [PROJECT_THEMES[i % len(PROJECT_THEMES)] for i in range(N_EXAMPLES)]

SYSTEM_PROMPT = """Tu es un chef de projet logiciel expérimenté. Pour une description de
projet donnée, tu dois produire un découpage en tâches réaliste.

Réponds UNIQUEMENT avec un JSON valide (pas de texte autour, pas de ```), au format exact :
{
  "tasks": [
    {"name": "...", "description": "...", "estimate_days": X, "category": "..."}
  ]
}

Règles :
- Entre 5 et 10 tâches par projet
- Des catégories variées : Backend, Frontend, Base de données, DevOps, Design, Tests, etc.
- Des estimations réalistes (entre 1 et 15 jours par tâche)
- Des tâches concrètes et actionnables, pas vagues
"""


def generate_one_example(client, theme: str) -> dict:
    user_prompt = f"{SYSTEM_PROMPT}\n\nProjet : une {theme}. Découpe-le en tâches."
    response = client.models.generate_content(model=MODEL_NAME, contents=user_prompt)
    raw_text = response.text.strip()
    raw_text = raw_text.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    tasks_json = json.loads(raw_text)
    return {
        "description": f"Je veux développer une {theme}.",
        "theme": theme,
        "tasks": tasks_json["tasks"],
    }


def count_existing_lines() -> int:
    if not os.path.exists(OUTPUT_FILE):
        return 0
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit(
            "ERREUR : variable d'environnement GEMINI_API_KEY manquante.\n"
            "PowerShell : $env:GEMINI_API_KEY='ta_clé'"
        )

    client = genai.Client(api_key=api_key)
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    already_done = count_existing_lines()
    if already_done >= N_EXAMPLES:
        print(f"Déjà {already_done}/{N_EXAMPLES} exemples générés. Rien à faire !")
        return

    print(f"Reprise : {already_done}/{N_EXAMPLES} déjà générés. On continue à partir de là.")

    generated_today = 0
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:  # mode "append" : on ajoute, on n'écrase pas
        idx = already_done
        while idx < N_EXAMPLES and generated_today < DAILY_LIMIT:
            theme = ALL_THEMES[idx]
            try:
                example = generate_one_example(client, theme)
                f.write(json.dumps(example, ensure_ascii=False) + "\n")
                f.flush()
                idx += 1
                generated_today += 1
                print(f"[{idx}/{N_EXAMPLES}] Généré : {theme}")
                time.sleep(3)
            except Exception as e:
                msg = str(e)
                if "RESOURCE_EXHAUSTED" in msg or "429" in msg:
                    print(f"\nQuota journalier atteint ({generated_today} générés aujourd'hui).")
                    print(f"Relance le script demain pour continuer à partir de {idx}/{N_EXAMPLES}.")
                    return
                print(f"Erreur sur '{theme}': {e} — on réessaie dans 10s")
                time.sleep(10)

    total = count_existing_lines()
    if total >= N_EXAMPLES:
        print(f"\nTerminé ! {total} exemples au total dans {OUTPUT_FILE}")
    else:
        print(f"\n{generated_today} générés aujourd'hui. Total : {total}/{N_EXAMPLES}. Relance demain pour continuer.")


if __name__ == "__main__":
    main()
