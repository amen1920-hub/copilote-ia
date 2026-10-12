"""
Dataset v2 pour l'Agent 1 : 60 projets differents, avec des descriptions de styles varies
(courte / detaillee / avec contraintes), 2 descriptions par projet = 120 exemples.

Ameliorations par rapport a la v1 :
  - chaque description est differente (plus de copies identiques)
  - categories limitees a une liste fermee (evalue la conformite des categories)
  - l'effort total doit etre coherent avec l'ampleur decrite
  - chaque exemple est valide avant d'etre ecrit
  - le script reprend ou il s'est arrete (relance-le si besoin)

Usage (PowerShell) :
    $env:GEMINI_API_KEY="ta_cle"
    python generate_dataset_v2.py
"""

import json
import os
import re
import time

MODEL_NAME = "gemini-3.1-flash-lite"   # si 404 : prends le nom que le message d'erreur recommande
OUTPUT_FILE = "data/raw/scoping_dataset_v2.jsonl"
MAX_RETRIES = 4

CATEGORIES = ["Backend", "Frontend", "Base de données", "DevOps", "Design", "Tests", "Sécurité", "Documentation"]

THEMES = [
    "application mobile de livraison de repas", "plateforme e-commerce de vêtements",
    "outil interne de gestion des congés", "site web vitrine pour un artisan",
    "application de suivi de fitness", "chatbot de support client",
    "système de réservation pour un restaurant", "plateforme e-learning",
    "application de covoiturage", "gestion de budget personnel",
    "réseau social pour photographes", "gestion de stock pour un entrepôt",
    "marketplace de services freelance", "application de méditation",
    "CRM pour une petite entreprise", "application de recherche d'appartement",
    "plateforme de cours particuliers en ligne", "suivi de notes de frais",
    "site de petites annonces locales", "application météo avec alertes",
    "portail de prise de rendez-vous médicaux", "suivi de santé pour patients chroniques",
    "gestion d'une bibliothèque universitaire", "plateforme de dons pour associations",
    "gestion de flotte de véhicules", "système de billetterie pour événements",
    "tableau de bord analytique pour une PME", "gestion de chantier BTP",
    "vote électronique pour associations", "application de suivi de colis",
    "site de comparaison de prix", "gestion du planning du personnel",
    "plateforme de formation en entreprise", "application de partage de recettes",
    "gestion de parking intelligent", "application d'apprentissage des langues",
    "outil de gestion de projets agiles", "plateforme de crowdfunding",
    "gestion d'une exploitation agricole", "portail citoyen pour démarches administratives",
    "gestion hôtelière", "application de suivi d'habitudes",
    "plateforme de streaming de podcasts", "gestion de cabinet d'avocats",
    "supervision IoT pour bâtiment", "application de téléconsultation",
    "plateforme de recrutement et suivi de candidatures", "gestion de copropriété",
    "gestion de pharmacie", "application de transport public en temps réel",
    "plateforme de revente d'objets d'occasion", "facturation pour auto-entrepreneurs",
    "jeu éducatif pour enfants", "suivi de production en usine",
    "gestion de clubs sportifs", "réservation de salles de coworking",
    "application de don de sang", "gestion du transport scolaire",
    "application de visites guidées de musée", "plateforme de petites missions entre voisins",
]

STYLES = {
    "courte": "une seule phrase de 15 à 25 mots, sans détail technique",
    "detaillee": "3 à 4 phrases décrivant des fonctionnalités précises et le public visé",
    "contraintes": "2 à 3 phrases incluant une contrainte (équipe de 2 à 3 développeurs, délai serré, budget limité ou technologie imposée)",
}
STYLE_KEYS = list(STYLES)

PROMPT = """Tu es un chef de projet logiciel expérimenté.

1. Invente la demande d'un client pour un projet de type : {theme}.
   Style de la demande : {style}. Écris-la à la première personne ("Je veux...", "Nous voulons...").
2. Découpe ce projet en 6 à 10 tâches concrètes.

Réponds UNIQUEMENT avec un JSON valide (sans ``` ni texte autour) au format exact :
{{"description": "...", "tasks": [{{"name": "...", "description": "...", "estimate_days": 5, "category": "Backend"}}]}}

Règles :
- "category" doit être EXACTEMENT l'une de ces valeurs : {categories}
- "estimate_days" est un entier de 1 à 15
- l'effort total doit refléter l'ampleur de la demande : un projet court et simple a un total plus faible qu'un projet détaillé avec beaucoup de fonctionnalités
- des tâches concrètes (ex : "API de gestion des commandes"), pas des phases génériques ("Analyse", "Maintenance")
"""


def jobs():
    """2 styles differents par theme, en tournant sur les 3 styles."""
    out = []
    for i, theme in enumerate(THEMES):
        for k in (i % 3, (i + 1) % 3):
            out.append((theme, STYLE_KEYS[k]))
    return out


def strip_fences(text):
    return re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())


def validate(data):
    """Retourne l'exemple nettoye, ou leve ValueError avec la raison du rejet."""
    desc = data.get("description")
    tasks = data.get("tasks")
    if not isinstance(desc, str) or len(desc.strip()) < 15:
        raise ValueError("description absente ou trop courte")
    if not isinstance(tasks, list) or not (6 <= len(tasks) <= 10):
        raise ValueError(f"nombre de taches invalide : {len(tasks) if isinstance(tasks, list) else 'n/a'}")
    clean = []
    for t in tasks:
        if not isinstance(t, dict) or not {"name", "description", "estimate_days", "category"} <= set(t):
            raise ValueError("tache incomplete")
        d = t["estimate_days"]
        if isinstance(d, float) and d.is_integer():
            d = int(d)
        if not isinstance(d, int) or isinstance(d, bool) or not (1 <= d <= 15):
            raise ValueError(f"estimate_days invalide : {t['estimate_days']!r}")
        if t["category"] not in CATEGORIES:
            raise ValueError(f"categorie hors liste : {t['category']!r}")
        clean.append({"name": str(t["name"]).strip(), "description": str(t["description"]).strip(),
                      "estimate_days": d, "category": t["category"]})
    return {"description": desc.strip(), "tasks": clean}


def generate_one(client, theme, style_key):
    prompt = PROMPT.format(theme=theme, style=STYLES[style_key], categories=", ".join(CATEGORIES))
    resp = client.models.generate_content(model=MODEL_NAME, contents=prompt)
    return validate(json.loads(strip_fences(resp.text)))


def load_done(path):
    done, descs = set(), set()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    ex = json.loads(line)
                    done.add((ex["theme"], ex["style"]))
                    descs.add(ex["description"].strip().casefold())
                except Exception:
                    pass
    return done, descs


def run(client, sleep=2.0, out_path=OUTPUT_FILE):
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    todo_all = jobs()
    done, descs = load_done(out_path)
    todo = [j for j in todo_all if j not in done]
    print(f"{len(done)}/{len(todo_all)} deja generes. Reste : {len(todo)}")

    failed = []
    with open(out_path, "a", encoding="utf-8") as f:
        for n, (theme, style_key) in enumerate(todo, 1):
            for attempt in range(1, MAX_RETRIES + 1):
                try:
                    ex = generate_one(client, theme, style_key)
                    if ex["description"].casefold() in descs:
                        raise ValueError("description en double")
                    descs.add(ex["description"].casefold())
                    f.write(json.dumps({"description": ex["description"], "theme": theme,
                                        "style": style_key, "tasks": ex["tasks"]}, ensure_ascii=False) + "\n")
                    f.flush()
                    print(f"[{len(done) + n}/{len(todo_all)}] {theme[:40]:40s} ({style_key})")
                    time.sleep(sleep)
                    break
                except Exception as e:
                    msg = str(e)
                    if "RESOURCE_EXHAUSTED" in msg or "429" in msg:
                        print("\nQuota atteint. Relance le script plus tard : il reprendra ici.")
                        return
                    wait = 5 * attempt
                    print(f"  essai {attempt}/{MAX_RETRIES} echoue ({msg[:90]}) -> pause {wait}s")
                    time.sleep(wait)
            else:
                failed.append((theme, style_key))
                print(f"  ABANDON pour l'instant : {theme} ({style_key})")

    done_now, _ = load_done(out_path)
    print(f"\nTermine : {len(done_now)}/{len(todo_all)} exemples dans {out_path}")
    if failed:
        print(f"{len(failed)} exemple(s) a regenerer : relance simplement le script.")


def main():
    from google import genai
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit('ERREUR : GEMINI_API_KEY manquante. PowerShell : $env:GEMINI_API_KEY="ta_cle"')
    run(genai.Client(api_key=api_key))


if __name__ == "__main__":
    main()
