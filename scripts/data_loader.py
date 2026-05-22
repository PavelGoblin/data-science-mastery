import pandas as pd
import numpy as np
from sklearn.datasets import (
    load_iris, load_wine, load_breast_cancer, load_digits,
    fetch_california_housing, fetch_openml
)
import os


def load_iris_dataset():
    data = load_iris(as_frame=True)
    df = data.frame
    df.columns = [col.replace(" (cm)", "").replace(" ", "_") for col in df.columns]
    df["species"] = data.target_names[df["target"]]
    print(f"Iris dataset loaded: {df.shape[0]} samples, {df.shape[1] - 2} features")
    return df


def load_wine_dataset():
    data = load_wine(as_frame=True)
    df = data.frame
    df["target"] = data.target_names[df["target"]]
    print(f"Wine dataset loaded: {df.shape[0]} samples, {df.shape[1] - 1} features")
    return df


def load_cancer_dataset():
    data = load_breast_cancer(as_frame=True)
    df = data.frame
    df["target"] = data.target_names[df["target"]]
    print(f"Breast Cancer dataset loaded: {df.shape[0]} samples, {df.shape[1] - 1} features")
    return df


def load_housing_dataset():
    data = fetch_california_housing(as_frame=True)
    df = data.frame
    df["MedHouseVal"] = df["MedHouseVal"] * 100000
    print(f"California Housing loaded: {df.shape[0]} samples, {df.shape[1]} features")
    return df


def load_titanic():
    df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    print(f"Titanic dataset loaded: {df.shape[0]} samples, {df.shape[1]} features")
    return df


def load_digits_dataset():
    data = load_digits(as_frame=True)
    df = data.frame
    df["target"] = data.target
    print(f"Digits dataset loaded: {df.shape[0]} samples, {df.shape[1] - 1} features")
    return df


def generate_synthetic_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42):
    from sklearn.datasets import make_regression
    X, y = make_regression(
        n_samples=n_samples, n_features=n_features,
        noise=noise, random_state=random_state
    )
    feature_names = [f"feature_{i}" for i in range(n_features)]
    df = pd.DataFrame(X, columns=feature_names)
    df["target"] = y
    return df


def generate_synthetic_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42):
    from sklearn.datasets import make_classification
    X, y = make_classification(
        n_samples=n_samples, n_features=n_features,
        n_classes=n_classes, n_informative=max(4, n_features // 2),
        random_state=random_state
    )
    feature_names = [f"feature_{i}" for i in range(n_features)]
    df = pd.DataFrame(X, columns=feature_names)
    df["target"] = y
    return df


def generate_synthetic_clustering(n_samples=300, n_features=2, n_clusters=3, random_state=42):
    from sklearn.datasets import make_blobs
    X, y = make_blobs(
        n_samples=n_samples, n_features=n_features,
        centers=n_clusters, random_state=random_state
    )
    feature_names = [f"feature_{i}" for i in range(n_features)]
    df = pd.DataFrame(X, columns=feature_names)
    df["cluster"] = y
    return df


DATASET_REGISTRY = {
    "iris": load_iris_dataset,
    "wine": load_wine_dataset,
    "cancer": load_cancer_dataset,
    "housing": load_housing_dataset,
    "titanic": load_titanic,
    "digits": load_digits_dataset,
    "synthetic_regression": generate_synthetic_regression,
    "synthetic_classification": generate_synthetic_classification,
    "synthetic_clustering": generate_synthetic_clustering,
}


def get_dataset(name, **kwargs):
    if name not in DATASET_REGISTRY:
        available = ", ".join(DATASET_REGISTRY.keys())
        raise ValueError(f"Dataset '{name}' not found. Available: {available}")
    return DATASET_REGISTRY[name](**kwargs)


def describe_dataset(df):
    print("=" * 60)
    print(f"Dataset shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print("=" * 60)
    print("\nColumn types:")
    print(df.dtypes.value_counts().to_string())
    print(f"\nMissing values: {df.isnull().sum().sum()}")
    if df.isnull().sum().sum() > 0:
        print("\nPer-column missing:")
        print(df.isnull().sum()[df.isnull().sum() > 0].to_string())
    print("\nSummary statistics:")
    print(df.describe(include="all").T.to_string())
    return df
