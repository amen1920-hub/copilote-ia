"""
Tache 1.1 - Prepare les donnees d'entrainement de l'Agent 1 (Cadrage).

Lit data/raw/scoping_dataset.jsonl et produit trois fichiers au format "messages"
(system / user / assistant) utilisable par le fine-tuning LoRA :
    data/processed/train.jsonl
    data/processed/val.jsonl
    data/processed/test.jsonl

La separation se fait PAR THEME : un theme est soit dans train, soit dans val,
soit dans test, jamais dans deux a la fois (sinon le test mesure de la memorisation).

Usage :
    python prepare_data.py
"""

import argparse
import json
import os
import random
from collections import defaultdict

SYSTEM_PROMPT = (
    "Tu es un chef de projet logiciel experimente. A partir de la description d'un projet, "
    "tu produis un decoupage en taches au format JSON strict : "
    '{"tasks": [{"name": str, "description": str, "estimate_days": int, "category": str}]}. '
    "Reponds uniquement avec le JSON."
)

REQUIRED_TASK_KEYS = {"name", "description", "estimate_days", "category"}


def load_examples(path):
    examples, rejected = [], 0
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                ex = json.loads(line)
                tasks = ex["tasks"]
                assert isinstance(tasks, list) and tasks
                assert all(REQUIRED_TASK_KEYS <= set(t) for t in tasks)
                assert all(isinstance(t["estimate_days"], (int, float)) for t in tasks)
                examples.append(ex)
            except Exception:
                rejected += 1
    return examples, rejected


def to_chat(ex):
    answer = json.dumps({"tasks": ex["tasks"]}, ensure_ascii=False)
    return {
        "theme": ex["theme"],
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": ex["description"]},
            {"role": "assistant", "content": answer},
        ],
    }


def split_by_theme(examples, seed, val_ratio, test_ratio):
    by_theme = defaultdict(list)
    for ex in examples:
        by_theme[ex["theme"]].append(ex)
    themes = sorted(by_theme)
    random.Random(seed).shuffle(themes)

    n = len(themes)
    n_val = max(1, round(n * val_ratio))
    n_test = max(1, round(n * test_ratio))
    split_themes = {
        "val": themes[:n_val],
        "test": themes[n_val:n_val + n_test],
        "train": themes[n_val + n_test:],
    }
    return {name: [e for t in ts for e in by_theme[t]] for name, ts in split_themes.items()}, split_themes


def write_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/raw/scoping_dataset.jsonl")
    p.add_argument("--output-dir", default="data/processed")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--val-ratio", type=float, default=0.15)
    p.add_argument("--test-ratio", type=float, default=0.15)
    args = p.parse_args()

    examples, rejected = load_examples(args.input)
    print(f"{len(examples)} exemples valides lus ({rejected} rejetes)")

    splits, split_themes = split_by_theme(examples, args.seed, args.val_ratio, args.test_ratio)

    os.makedirs(args.output_dir, exist_ok=True)
    for name, rows in splits.items():
        write_jsonl(os.path.join(args.output_dir, f"{name}.jsonl"), [to_chat(e) for e in rows])
        print(f"{name:5s}: {len(rows):3d} exemples, {len(split_themes[name]):2d} themes")

    # Garde-fou : aucun theme ne doit etre dans deux ensembles
    all_sets = [set(t) for t in split_themes.values()]
    assert not (all_sets[0] & all_sets[1] or all_sets[0] & all_sets[2] or all_sets[1] & all_sets[2])
    print("Controle OK : aucun theme partage entre train, val et test.")


if __name__ == "__main__":
    main()
