import numpy as np
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    recall_score,
    f1_score
)


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


def evaluate_classifier(model, X_train, y_train, X_test, y_test, model_name) -> None:
    #predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)


    #accuracy
    train_acc = accuracy_score(y_train, y_train_pred)*100
    test_acc = accuracy_score(y_test, y_test_pred)*100

    train_recall = recall_score(y_train, y_train_pred)
    test_recall = recall_score(y_test, y_test_pred)

    train_f1 = f1_score(y_train, y_train_pred)
    test_f1 = f1_score(y_test, y_test_pred)

    

    #results
    print(f"{model_name} - Train Accuracy: {train_acc:.2f}%")
    print(f"{model_name} - Test Accuracy: {test_acc:.2f}%\n")

    print(f"{model_name} - Train Recall: {train_recall:.2f}")
    print(f"{model_name} - Test Recall: {test_recall:.2f}\n")

    print(f"{model_name} - Train f1_score: {train_f1:.2f}")
    print(f"{model_name} - Test f1_score: {test_f1:.2f}\n")

    print("-"*40)


    print("Train Classification Report")
    print(classification_report(y_train, y_train_pred))


    print("-"*40)


    print("Test Classification Report")
    print(classification_report(y_test, y_test_pred))
