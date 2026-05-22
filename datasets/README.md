# Datasets

This folder stores dataset descriptions and download instructions. Actual data files are excluded from git (see `.gitignore`).

## Built-in Datasets (no download needed)

These come with scikit-learn and are used in the notebooks:

| Dataset | Type | Loader Function |
|---------|------|-----------------|
| Iris | Classification (3 classes) | `load_iris_dataset()` |
| Wine | Classification (3 classes) | `load_wine_dataset()` |
| Breast Cancer | Binary Classification | `load_cancer_dataset()` |
| Digits | Multi-class Classification | `load_digits_dataset()` |
| California Housing | Regression | `load_housing_dataset()` |

## External Datasets (download required)

These are used in case studies and projects:

| Dataset | Source | Use Case |
|---------|--------|----------|
| Titanic | Kaggle | Binary classification, missing data |
| Ames Housing | Kaggle | Regression, feature engineering |
| Telco Churn | Kaggle | Imbalanced classification |
| CIFAR-10 | Keras | Image classification |
| IMDB Reviews | Keras | Sentiment analysis |

## Synthetic Datasets

Generated programmatically using `scripts/data_loader.py`:

- `generate_synthetic_regression()` — custom n_samples, n_features, noise
- `generate_synthetic_classification()` — custom n_samples, n_features, n_classes
- `generate_synthetic_clustering()` — custom n_samples, n_clusters
