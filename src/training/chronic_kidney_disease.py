#IMPORTANT: The Base Model Performance, was very good so I accepted it,

import sys

from ucimlrepo import fetch
import logging
import yaml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    classification_report,
)
from joblib import dump
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

#directory based imports
from src.utils.preprocessing_util import evaluate_classifier
from src.training.config.settings import Settings

from ucimlrepo import fetch_ucirepo 


def train_chronic_kidney_model():
    try:
        settings = Settings()

        MODEL_PATH = Path(settings.chronic_kidney_disease_model_path)
        LOG_PATH = Path(settings.log_path)
        HYPERPARAMETERS_YAML_PATH = Path(settings.hyper_params_yaml_path)

        TARGET_COL = settings.chronic_kidney_disease_target_col
        TEST_SIZE = settings.test_size
        RANDOM_STATE = settings.random_state

        MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

        #logging structure
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s | %(levelname)s | %(message)s",
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(LOG_PATH)
            ]
        )
  
        #fetch dataset 
        chronic_kidney_disease = fetch_ucirepo(id=336) 
        logging.info("Chronic Kidney dataset fetched")
        
        # data (as pandas dataframes) 
        X = chronic_kidney_disease.data.features 
        y = chronic_kidney_disease.data.targets 

        df = X.copy()
        df["target"] = y
        df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

        logging.info("Dataframe for Chronic Dataset created")
        
        X = df.drop(columns=[TARGET_COL])
        y = df[TARGET_COL]

        logging.info("Features and target separation done")



        le = LabelEncoder()

        y = pd.Series(le.fit_transform(y), index=y.index, name=TARGET_COL)
        logging.info("Target Column encoded")

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            stratify=y,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE
        )
        logging.info("Train/Test Split completed")

        numerical_features = X_train.select_dtypes(include=[np.number]).columns.tolist()
        cat_features = X_train.select_dtypes(exclude=[np.number]).columns.tolist()

        logging.info("Categorical and Numerical Features gotten")

        numerical_transformer = Pipeline(
            steps = [
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
            ]
        )

        cat_transformer = Pipeline(
            steps = [
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("oneHotEncode", OneHotEncoder(handle_unknown="ignore", drop="first"))
            ]
        )

        preprocess = ColumnTransformer(
            transformers=[
                ("num", numerical_transformer, numerical_features),
                ("cat", cat_transformer, cat_features)
            ]
        )

        logging.info("Preprocessing steps created")

        with open(HYPERPARAMETERS_YAML_PATH, mode="r") as file:
            hyperparams = yaml.safe_load(file)

        logging.info("Hyperparameters have been accessed")

        model_params = hyperparams["chronic_kidney_disease"]["params"]

        model = LogisticRegression(
            random_state=RANDOM_STATE,
            **model_params
        )

        pipeline = Pipeline(
            steps = [
                ("preprocess", preprocess),
                ("model", model)
            ]
        )

        pipeline.fit(X_train, y_train)
        logging.info("Model Training Completed")
        logging.info("Model Evaluation....\n")

        logging.info(
            evaluate_classifier("Logistic Regression", X_train, y_train, X_test, y_test, pipeline)
        )

        dump(pipeline, MODEL_PATH)
        logging.info(f"Model saved at: {MODEL_PATH}")
        logging.info("Chronic Disease Script Completed")
    except Exception as e:
        print("Training Script Failed: ", str(e))
        logging.info("Training Script Failed: ", str(e))
        raise

if __name__ == "__main__":
    train_chronic_kidney_model()












