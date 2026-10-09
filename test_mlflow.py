import dagshub
import mlflow

dagshub.init(repo_owner='amen1920-hub', repo_name='copilote-ia', mlflow=True)

with mlflow.start_run():
    mlflow.log_param("test_param", "setup_phase0")
    mlflow.log_metric("test_metric", 1.0)
    print("Run MLflow envoyé avec succès vers DagsHub !")
