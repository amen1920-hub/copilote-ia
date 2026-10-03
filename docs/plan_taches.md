# Plan de tâches — Copilote de cadrage et pilotage de projets

## Phase 0 — Setup (~15h) — avant Éval 1
- [ ] 0.1 Créer le repo GitHub
- [ ] 0.2 Initialiser DVC (remote Google Drive/local)
- [ ] 0.3 Initialiser MLflow (local ou DagsHub)
- [ ] 0.4 Collecter/générer un dataset d'historique de projets
- [ ] 0.5 Créer un compte Jira/Trello développeur + token API

## Phase 1 — Agent 1 : Cadrage (~29h) — avant Éval 2
- [ ] 1.1 Préparer les données d'entraînement (description → JSON)
- [ ] 1.2 Choisir et charger le SLM (Phi-3.5-mini / Qwen2.5-3B, 4-bit)
- [ ] 1.3 Fine-tuning LoRA/QLoRA sur Colab/Kaggle
- [ ] 1.4 Construire le RAG sur historique de projets
- [ ] 1.5 Prompt engineering pour JSON structuré
- [ ] 1.6 Évaluer l'Agent 1 (taux JSON valide, estimations vs baseline)
- [ ] 1.7 Logger les runs dans MLflow

## Phase 2 — Agent 2 : Intégration Jira/Trello (~30h) — avant Éval 2/3
- [ ] 2.1 Étudier l'API Jira/Trello
- [ ] 2.2 Écrire le connecteur API
- [ ] 2.3 Gérer l'idempotence
- [ ] 2.4 Matching compétences (embeddings)
- [ ] 2.5 Algorithme d'équilibrage de charge
- [ ] 2.6 Configurer le tool-calling
- [ ] 2.7 Tester bout en bout

## Phase 3 — Agent 3 : Risques (~30h) — avant Éval 3
- [ ] 3.1 Extraire les métriques Jira/Trello
- [ ] 3.2 Construire les features tabulaires
- [ ] 3.3 Entraîner XGBoost/LightGBM vs baseline
- [ ] 3.4 Classifieur NLP sur commentaires
- [ ] 3.5 Réutiliser le RAG (patterns historiques)
- [ ] 3.6 Produire score de risque + explication
- [ ] 3.7 Évaluer l'Agent 3

## Phase 4 — Orchestration (~23h) — avant Éval 3/4
- [ ] 4.1 Choisir l'orchestrateur (LangGraph)
- [ ] 4.2 Construire le graphe d'orchestration
- [ ] 4.3 Interface de validation humaine (Streamlit)
- [ ] 4.4 Journal d'audit
- [ ] 4.5 Tests d'intégration bout en bout

## Phase 5 — MLOps & finalisation (~28h) — avant Éval 4
- [ ] 5.1 Pipeline Airflow
- [ ] 5.2 Dashboard Grafana
- [ ] 5.3 Monitoring EvidentlyAI
- [ ] 5.4 Rapport final
- [ ] 5.5 Préparation démo live
- [ ] 5.6 Slides de présentation finale

**Total estimé : ~155h**
