import numpy as np
import logging
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


def evaluate_classifier(model_name, X_train, y_train, X_test, y_test, model_pipeline):
    model_train_pred = model_pipeline.predict(X_train)
    model_test_pred = model_pipeline.predict(X_test)
    
    print(f"---------------{model_name}---------------")
    logging.info(f"---------------{model_name}---------------")
    
    print("-------TRAINING EVALUATION-------")
    logging.info("-------TRAINING EVALUATION-------")
    
    train_acc = accuracy_score(y_train, model_train_pred)
    print("Model Accuracy: ", train_acc)
    logging.info(f"Model Accuracy: {train_acc}")
    
    train_prec = precision_score(y_train, model_train_pred)
    print("Model Precision: ", train_prec)
    logging.info(f"Model Precision: {train_prec}")
    
    train_rec = recall_score(y_train, model_train_pred)
    print("Model Recall: ", train_rec)
    logging.info(f"Model Recall: {train_rec}")
    
    train_clf = classification_report(y_train, model_train_pred)
    print("Classification Report: \n", train_clf)
    logging.info(f"Classification Report: \n{train_clf}")

    print("-"*80)
    logging.info("-" * 80)

    print("-------TESTING EVALUATION------------")
    logging.info("-------TESTING EVALUATION------------")
    
    test_acc = accuracy_score(y_test, model_test_pred)
    print("Model Accuracy: ", test_acc)
    logging.info(f"Model Accuracy: {test_acc}")
    
    test_prec = precision_score(y_test, model_test_pred)
    print("Model Precision: ", test_prec)
    logging.info(f"Model Precision: {test_prec}")
    
    test_rec = recall_score(y_test, model_test_pred)
    print("Model Recall: ", test_rec)
    logging.info(f"Model Recall: {test_rec}")
    
    test_clf = classification_report(y_test, model_test_pred)
    print("Classification Report: \n", test_clf)
    logging.info(f"Classification Report: \n{test_clf}")
