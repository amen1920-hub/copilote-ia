"""
Audit de qualite du dataset v2 (a lancer avant le decoupage train/val/test).

Produit :
  - des statistiques affichees a l'ecran ;
  - results/audit_sample.md : 20 exemples tires au hasard, a relire a la main.

Usage :
    python audit_dataset.py
    python audit_dataset.py --input data/raw/scoping_dataset_v2.jsonl --n 20 --seed 42
"""

import argparse
import json
import os
import random
import statistics
from collections import Counter, defaultdict


def load(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def total_days(ex):
    return sum(t["estimate_days"] for t in ex["tasks"])


def flags(ex):
    """Signaux d'alerte automatiques sur un exemple."""
    out = []
    days = [t["estimate_days"] for t in ex["tasks"]]
    names = [t["name"].strip().casefold() for t in ex["tasks"]]
    if len(set(days)) == 1:
        out.append("toutes les estimations sont identiques")
    if len(set(names)) < len(names):
        out.append("noms de taches en double")
    if total_days(ex) < 15:
        out.append(f"total tres faible ({total_days(ex)} j)")
    if total_days(ex) > 90:
        out.append(f"total tres eleve ({total_days(ex)} j)")
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/raw/scoping_dataset_v2.jsonl")
    p.add_argument("--n", type=int, default=20)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--out", default="results/audit_sample.md")
    args = p.parse_args()

    data = load(args.input)
    print(f"\n=== {len(data)} exemples, {len({e['theme'] for e in data})} themes ===")

    # 1. Effort total par style : la description plus riche donne-t-elle plus de jours ?
    by_style = defaultdict(list)
    for e in data:
        by_style[e["style"]].append(total_days(e))
    print("\n[1] Total de jours par style de description")
    for s in ("courte", "detaillee", "contraintes"):
        v = by_style.get(s, [])
        if v:
            print(f"  {s:12s} n={len(v):3d}  mediane={statistics.median(v):5.0f}  min={min(v):3d}  max={max(v):3d}")
    try:
        lengths = [len(e["description"].split()) for e in data]
        totals = [total_days(e) for e in data]
        r = statistics.correlation(lengths, totals)
        print(f"  correlation (nb de mots de la description, total de jours) = {r:.2f}")
    except Exception:
        pass

    # 2. Taches et estimations
    n_tasks = [len(e["tasks"]) for e in data]
    print(f"\n[2] Taches par exemple : min={min(n_tasks)} moyenne={statistics.mean(n_tasks):.1f} max={max(n_tasks)}")
    c = Counter(t["estimate_days"] for e in data for t in e["tasks"])
    print("  repartition des estimations (jours : nombre de taches) :")
    print("  " + "  ".join(f"{d}:{c[d]}" for d in range(1, 16)))
    tot_tasks = sum(c.values())
    top = c.most_common(1)[0]
    print(f"  valeur la plus frequente : {top[0]} jours ({top[1] / tot_tasks:.0%} des taches)")

    # 3. Categories
    cats = Counter(t["category"] for e in data for t in e["tasks"])
    print("\n[3] Categories (part des taches)")
    for k, v in cats.most_common():
        print(f"  {k:18s} {v:4d}  {v / tot_tasks:.0%}")

    # 4. Alertes automatiques
    flagged = [(e, flags(e)) for e in data if flags(e)]
    print(f"\n[4] Exemples avec alerte automatique : {len(flagged)} / {len(data)}")
    for e, fl in flagged[:8]:
        print(f"  - {e['theme'][:40]} ({e['style']}) : {', '.join(fl)}")

    # 5. Extremes
    ranked = sorted(data, key=total_days)
    print("\n[5] 3 totaux les plus bas / les plus hauts")
    for e in ranked[:3] + ranked[-3:]:
        print(f"  {total_days(e):4d} j  {e['theme'][:40]} ({e['style']})")

    # Echantillon a relire a la main
    sample = random.Random(args.seed).sample(data, min(args.n, len(data)))
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(f"# Audit manuel : {len(sample)} exemples tires au hasard\n\n")
        f.write("Pour chaque exemple, note ton verdict. Question a te poser : "
                "*un chef de projet trouverait-il ce decoupage et ces durees credibles ?*\n\n")
        for i, e in enumerate(sample, 1):
            f.write(f"## {i}. {e['theme']} ({e['style']}) - total {total_days(e)} jours\n\n")
            f.write(f"**Demande :** {e['description']}\n\n")
            for t in e["tasks"]:
                f.write(f"- [{t['category']}] {t['estimate_days']} j - **{t['name']}** : {t['description']}\n")
            fl = flags(e)
            if fl:
                f.write(f"\nAlerte automatique : {', '.join(fl)}\n")
            f.write("\nVerdict : [ ] credible   [ ] discutable   [ ] absurde\n\n---\n\n")
    print(f"\nFichier a relire : {args.out}")


if __name__ == "__main__":
    main()
