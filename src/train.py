import os
import mlflow

def train_model(model):

    # Log the model using MLflow
    mlflow.log_model(model, "model")

    # Log additional artifacts
    mlflow.log_artifact("path/to/artifact")

if __name__ == '__main__':
    models_folder = "models"

    # Create the models folder if it doesn't exist
    if not os.path.exists(models_folder):
        os.makedirs(models_folder)

    # Start an MLflow run
    with mlflow.start_run():
        # Set metadata and tags for the run
        mlflow.set_tag("team", "data-science")
        mlflow.set_tag("experiment", "experiment-1")

        # Train the model and log artifacts
        train_model()

        # Save the model to the models folder
        model_path = os.path.join(models_folder, "my_model")
        mlflow.pyfunc.save_model(path=model_path, loader_module="mlflow.pyfunc")