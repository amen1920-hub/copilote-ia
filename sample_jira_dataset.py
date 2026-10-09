"""
Prend un échantillon raisonnable des gros fichiers CSV Apache Jira Issues,
au lieu de tout charger (évite les problèmes de taille/stockage).

Usage :
    pip install pandas
    python sample_jira_dataset.py
"""

import pandas as pd
import os
import glob

INPUT_DIR = "data/raw/apache_jira_issues"
OUTPUT_FILE = "data/raw/jira_issues_sample.csv"
N_ROWS_PER_FILE = 2000  # ajuste selon besoin (quelques milliers suffisent)

def main():
    csv_files = glob.glob(os.path.join(INPUT_DIR, "*.csv"))
    if not csv_files:
        raise SystemExit(f"Aucun CSV trouvé dans {INPUT_DIR}")

    print(f"{len(csv_files)} fichiers trouvés : {csv_files}")

    samples = []
    for file in csv_files:
        print(f"Lecture d'un échantillon de {file}...")
        # On lit seulement les N premières lignes, pas tout le fichier
        try:
            df = pd.read_csv(file, nrows=N_ROWS_PER_FILE, low_memory=False)
            df["source_file"] = os.path.basename(file)
            samples.append(df)
            print(f"  -> {len(df)} lignes récupérées")
        except Exception as e:
            print(f"  -> Erreur sur {file}: {e}")

    if not samples:
        raise SystemExit("Aucun échantillon n'a pu être lu.")

    combined = pd.concat(samples, ignore_index=True)
    combined.to_csv(OUTPUT_FILE, index=False)
    print(f"\nTerminé ! {len(combined)} lignes au total -> {OUTPUT_FILE}")
    print(f"Taille du fichier échantillon : {os.path.getsize(OUTPUT_FILE) / 1e6:.1f} Mo")

if __name__ == "__main__":
    main()
