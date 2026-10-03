# Copilote de cadrage, découpage et pilotage de projets

Système multi-agents qui transforme une description de projet en langage naturel
en plan de tâches, l'intègre dans Jira/Trello, et surveille les risques en continu.

## Structure du projet

```
.
├── agents/
│   ├── agent1_scoping/     # Agent 1 — Cadrage : fine-tuning LoRA + RAG, génération JSON
│   ├── agent2_ops/         # Agent 2 — Intégration Jira/Trello, tool-calling, matching
│   └── agent3_risk/        # Agent 3 — Scoring de risque (tabulaire + NLP)
├── data/
│   ├── raw/                 # Données brutes (versionnées avec DVC)
│   └── processed/           # Données prétraitées
├── notebooks/                # Exploration, entraînement, évaluation
├── api/                      # API (FastAPI) exposant les agents
├── streamlit_app/            # Interface de validation humaine
├── pipelines/airflow/        # DAGs de ré-entraînement et collecte périodique
├── monitoring/                # Configs Grafana / EvidentlyAI
├── tests/                     # Tests unitaires et d'intégration
└── docs/                      # Rapport, schémas, notes
```

## Setup rapide

```bash
python -m venv venv
source venv/bin/activate      # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt
```

## Outils utilisés
- **Versionning code** : GitHub
- **Versionning données** : DVC
- **Suivi d'expériences** : MLflow
- **Orchestration agents** : LangGraph
- **Interface** : Streamlit
- **Monitoring** : Grafana, EvidentlyAI
- **Pipeline** : Airflow

## Jalons (voir docs/plan_taches.md)
- Phase 0 — Setup
- Phase 1 — Agent 1 (Cadrage)
- Phase 2 — Agent 2 (Intégration Jira/Trello)
- Phase 3 — Agent 3 (Risques)
- Phase 4 — Orchestration
- Phase 5 — MLOps & finalisation
