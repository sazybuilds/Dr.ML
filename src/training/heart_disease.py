# pyrefly: ignore [missing-import]
import logging
import yaml
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GroupShuffleSplit

# pyrefly: ignore [missing-import]
from pathlib import Path

# pyrefly: ignore [missing-import]
from joblib import dump

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    recall_score,
    f1_score
)

from src.utils.preprocessing_util import evaluate_classifier
from src.training.config.settings import Settings


#TODO: Modularize Code, apply DRY and orthogonality principles

def train_model():
    try:
        settings = Settings()
        DATASET_PATH = Path(settings.heart_disease_dataset_path)
        MODEL_PATH = Path(settings.heart_disease_model_path)
        LOG_PATH = Path(settings.log_path)
        HYPER_PARAMS_YAML_PATH = Path(settings.hyper_params_yaml_path)

        TARGET_COL = settings.heart_disease_target_col
        TEST_SIZE = settings.test_size
        RANDOM_STATE = settings.random_state

        MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s | %(levelname)s | %(message)s",
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(LOG_PATH)
            ]
        )

        df = pd.read_csv(DATASET_PATH)
        logging.info(f"Dataset loaded with shape: {df.shape}")

        X = df.drop(columns=TARGET_COL)
        y=df[TARGET_COL]


        row_signature = pd.util.hash_pandas_object(X, index=False)


        gss = GroupShuffleSplit(
            n_splits=1,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE
        )

        train_idx, test_idx = next(gss.split(X, y, groups=row_signature))

        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        logging.info(f"Train shape: {X_train.shape}, Test Shape: {X_test.shape}")

        with open(HYPER_PARAMS_YAML_PATH, mode="r") as file:
            hyperparams = yaml.safe_load(file)

        logging.info("Heart Disease Hyperparameters have been accessed")

        model_params = hyperparams["heart_disease"]["params"]



        #TODO: Add parameters as environment variables instead of hardcoding
        model = RandomForestClassifier(
            random_state=RANDOM_STATE,
            **model_params
        )

        pipeline = Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                ("model", model)
            ]
        )

        pipeline.fit(X_train, y_train)
        logging.info("Model training completed")
        logging.info("Model Evaluation..")

        logging.info(
            evaluate_classifier(pipeline, X_train, y_train, X_test, y_test, "RandomForest")
        )

        dump(pipeline, MODEL_PATH)
        logging.info(f"Model saved to {MODEL_PATH}")

        logging.info("Training Script Completed")

    except  Exception as e:
        print(f"Training Failed: {e}")
        logging.exception(f"Training Scipt Failed: {e}")
        raise


if __name__ == '__main__':
    train_model()