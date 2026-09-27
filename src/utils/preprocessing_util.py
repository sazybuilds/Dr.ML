import numpy as np
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)

import matplotlib.pyplot as plt
import seaborn as sns

#convert unethical zero values to nulls
def replace_zeros_with_nan_df(X):
    """
    Replace 0 -> NaN for selected columns in a pandas DataFrame.
    Returns a NEW DataFrame (safe for sklearn pipelines).
    """
    X = X.copy()
    cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    for col in cols:
        if col in X.columns:
            X[col] = X[col].replace(0, np.nan)
    return X


def evaluate_classifier(model_name, X_train, y_train, X_test, y_test, model_pipeline) -> None:
    model_train_pred = model_pipeline.predict(X_train)
    model_test_pred = model_pipeline.predict(X_test)
    print(f"---------------{model_name}---------------")
    print("-------TRAINING EVALUATION-------")
    print("Model Accuracy: ", accuracy_score(y_train, model_train_pred))
    print("Model Precision: ", precision_score(y_train, model_train_pred))
    print("Model Recall: ", recall_score(y_train, model_train_pred))
    print("Classification Report: \n", classification_report(y_train, model_train_pred))

    print("-"*80)


    print("-------TESTING EVALUATION------------")
    print("Model Accuracy: ", accuracy_score(y_test, model_test_pred))
    print("Model Precision: ", precision_score(y_test, model_test_pred))
    print("Model Recall: ", recall_score(y_test, model_test_pred))
    print("Classification Report: \n", classification_report(y_test, model_test_pred))

