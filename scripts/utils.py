import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import learning_curve, validation_curve
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report,
    mean_squared_error, mean_absolute_error, r2_score
)


def evaluate_classification(model, X_test, y_test, model_name="Model"):
    y_pred = model.predict(X_test)
    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, average="weighted"),
        "Recall": recall_score(y_test, y_pred, average="weighted"),
        "F1-Score": f1_score(y_test, y_pred, average="weighted"),
    }
    if len(np.unique(y_test)) == 2:
        y_proba = model.predict_proba(X_test)[:, 1]
        metrics["ROC-AUC"] = roc_auc_score(y_test, y_proba)
    print(f"=== {model_name} Performance ===")
    for k, v in metrics.items():
        print(f"{k:12s}: {v:.4f}")
    print(f"\n{classification_report(y_test, y_pred)}")
    return metrics


def evaluate_regression(model, X_test, y_test, model_name="Model"):
    y_pred = model.predict(X_test)
    metrics = {
        "R2 Score": r2_score(y_test, y_pred),
        "MAE": mean_absolute_error(y_test, y_pred),
        "MSE": mean_squared_error(y_test, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
        "MAPE": np.mean(np.abs((y_test - y_pred) / y_test)) * 100,
    }
    print(f"=== {model_name} Performance ===")
    for k, v in metrics.items():
        print(f"{k:12s}: {v:.4f}")
    return metrics


def plot_confusion_matrix(y_test, y_pred, labels=None):
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()


def plot_learning_curve(estimator, X, y, cv=5, scoring="accuracy", title="Learning Curve"):
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, scoring=scoring,
        train_sizes=np.linspace(0.1, 1.0, 10), n_jobs=-1
    )
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    plt.figure(figsize=(10, 6))
    plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1, color="blue")
    plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.1, color="orange")
    plt.plot(train_sizes, train_mean, "o-", color="blue", label="Training score")
    plt.plot(train_sizes, test_mean, "o-", color="orange", label="Cross-validation score")
    plt.xlabel("Training examples")
    plt.ylabel(scoring.title())
    plt.title(title)
    plt.legend(loc="best")
    plt.grid(True, alpha=0.3)
    plt.show()
    return {"train_sizes": train_sizes, "train_scores": train_mean, "test_scores": test_mean}


def plot_validation_curve(estimator, X, y, param_name, param_range, cv=5, scoring="accuracy"):
    train_scores, test_scores = validation_curve(
        estimator, X, y, param_name=param_name, param_range=param_range,
        cv=cv, scoring=scoring, n_jobs=-1
    )
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    plt.figure(figsize=(10, 6))
    plt.fill_between(param_range, train_mean - train_std, train_mean + train_std, alpha=0.1, color="blue")
    plt.fill_between(param_range, test_mean - test_std, test_mean + test_std, alpha=0.1, color="orange")
    plt.plot(param_range, train_mean, "o-", color="blue", label="Training score")
    plt.plot(param_range, test_mean, "o-", color="orange", label="Cross-validation score")
    plt.xlabel(param_name)
    plt.ylabel(scoring.title())
    plt.title(f"Validation Curve ({param_name})")
    plt.legend(loc="best")
    plt.grid(True, alpha=0.3)
    plt.show()


def detect_outliers_iqr(dataframe, column):
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = dataframe[(dataframe[column] < lower_bound) | (dataframe[column] > upper_bound)]
    return outliers, lower_bound, upper_bound


def summarize_missing_values(df):
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    summary = pd.DataFrame({"Missing Count": missing, "Percentage (%)": missing_pct})
    summary = summary[summary["Missing Count"] > 0].sort_values("Missing Count", ascending=False)
    return summary


def train_test_split_stratified(df, target_col, test_size=0.2, random_state=42):
    from sklearn.model_selection import train_test_split as tts
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return tts(X, y, test_size=test_size, random_state=random_state, stratify=y if y.dtype == "object" or len(np.unique(y)) < 20 else None)
