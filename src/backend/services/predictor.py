import logging
from pathlib import Path

import pandas as pd
# pyrefly: ignore [missing-import]
from joblib import load

from src.backend.config.settings import Settings
from src.utils.preprocessing_util import replace_zeros_with_nan_df


settings = Settings()

DIABETES_MODEL_PATH = Path(settings.diabetes_model_path)
HEART_DISEASE_MODEL_PATH = Path(settings.heart_disease_model_path)
LOG_PATH = Path(settings.log_path)

LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_PATH)

    ]
)

logging.info("Loading Trained models...")
diabetes_model = load(DIABETES_MODEL_PATH)
heart_disease_model = load(HEART_DISEASE_MODEL_PATH)
logging.info("Models Loaded Successfully")


#common prediction function
def predict_disease(disease: str, input_data: dict) -> None:
    if disease == "diabetes":
        model = diabetes_model
    elif disease == "heart_disease":
        model = heart_disease_model
    else:
        raise ValueError("Invalid Disease Type. Use 'diabetes' or 'heart_disease'")

    X_df = pd.DataFrame([input_data])

    prediction = int(model.predict(X_df)[0])

    probability = float(model.predict_proba(X_df)[0][1])

    logging.info(
        f"[{disease}] prediction={prediction}, probability={probability}"
    )

    return {
        "disease": disease,
        "prediction": prediction,
        "probability": probability,
    }


"""example usage"""
# diabetes_test_data = {
#     "Pregnancies": 2,
#     "Glucose": 138,
#     "BloodPressure": 62,
#     "SkinThickness": 35,
#     "Insulin": 0,
#     "BMI": 33.6,
#     "DiabetesPedigreeFunction": 0.127,
#     "Age": 47
# }

# heart_disease_test_data = {
#     "age": 52,
#     "sex": 1,
#     "cp": 0,
#     "trestbps": 125,
#     "chol": 212,
#     "fbs": 0,
#     "restecg": 1,
#     "thalach": 168,
#     "exang": 0,
#     "oldpeak": 1.0,
#     "slope": 2,
#     "ca": 2,
#     "thal": 3
# }

# print(predict_disease("diabetes", diabetes_test_data))
# print(predict_disease("heart_disease", heart_disease_test_data))




