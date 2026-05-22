# Data Science Mastery

A hands-on data science learning repository with topic-based organization, practical Jupyter notebooks, and real-world projects.

## Directory Structure

```
01_python_fundamentals/      # NumPy, Pandas, Visualization, Deep Learning
02_data_handling/            # Preprocessing, comprehensive Pandas guide
03_supervised_learning/      # Linear models, Trees, SVM, KNN, Naive Bayes, XGBoost
04_unsupervised_learning/    # Clustering, Anomaly detection, Association rules, PCA
05_advanced_ml/              # Pipelines, Feature selection/engineering, Ensembles, Imbalanced data
06_model_interpretability/   # SHAP, Permutation importance, PDP
07_production_ml/            # Model deployment, API serving, Docker
08_projects/                 # 50+ real-world case studies and projects
```

## Python Fundamentals

| Notebook | Description |
|----------|-------------|
| [NumPy Crash Course](01_python_fundamentals/numpy_crash_course.ipynb) | Arrays, broadcasting, vectorization, linear algebra |
| [Pandas Essentials](01_python_fundamentals/pandas_essentials.ipynb) | DataFrames, I/O, filtering, aggregation basics |
| [Data Visualization](01_python_fundamentals/data_visualization.ipynb) | Matplotlib, Seaborn, Plotly fundamentals |
| [Intro to Deep Learning](01_python_fundamentals/intro_to_deep_learning.ipynb) | Neural networks with TensorFlow/Keras for regression & classification |

## Data Handling

| Notebook | Description |
|----------|-------------|
| [Pandas Comprehensive Guide](02_data_handling/pandas_comprehensive_guide.ipynb) | Deep-dive into merge, reshape, groupby, time series, text, missing data, styling |
| [Data Preprocessing](02_data_handling/data_preprocessing_techniques.ipynb) | Scaling, encoding, outlier handling, feature engineering |

## Supervised Learning

| Notebook | Description |
|----------|-------------|
| [Linear Models](03_supervised_learning/linear_models.ipynb) | Linear/Logistic regression, regularization |
| [Decision Trees](03_supervised_learning/decision_trees.ipynb) | Classification & regression trees, pruning |
| [Naive Bayes](03_supervised_learning/naive_bayes_classifier.ipynb) | Gaussian, Multinomial, Bernoulli classifiers |
| [Nearest Neighbors](03_supervised_learning/nearest_neighbors.ipynb) | KNN for classification & regression |
| [Support Vector Machines](03_supervised_learning/support_vector_machines.ipynb) | SVM, kernels, margin optimization |
| [Gradient Boosting (XGBoost, LightGBM, CatBoost)](03_supervised_learning/gradient_boosting_xgboost.ipynb) | Industry-standard boosting libraries with head-to-head comparison |

## Unsupervised Learning

| Notebook | Description |
|----------|-------------|
| [Clustering Algorithms](04_unsupervised_learning/clustering_algorithms.ipynb) | K-Means, DBSCAN, Hierarchical, evaluation |
| [Outlier & Anomaly Detection](04_unsupervised_learning/outlier_and_anomaly_detection.ipynb) | Isolation Forest, LOF, statistical methods |
| [Association Rules](04_unsupervised_learning/association_rules_mining.ipynb) | Apriori, FP-Growth, market basket analysis |
| [Dimensionality Reduction](04_unsupervised_learning/dimensionality_reduction.ipynb) | PCA, t-SNE, UMAP for visualization and noise reduction |

## Advanced ML Techniques

| Notebook | Description |
|----------|-------------|
| [Pipelines & Transformers](05_advanced_ml/pipelines_and_transformers.ipynb) | ColumnTransformer, FeatureUnion, custom transformers |
| [Feature Selection Methods](05_advanced_ml/feature_selection_methods.ipynb) | Filter, wrapper, embedded, RFE, mutual information |
| [Feature Engineering Techniques](05_advanced_ml/feature_engineering_techniques.ipynb) | Polynomial features, encoding, aggregation, date features, binning |
| [Model Selection & Evaluation](05_advanced_ml/model_selection_and_evaluation.ipynb) | Cross-validation, hyperparameter tuning, metrics |
| [Ensemble Learning](05_advanced_ml/ensemble_learning.ipynb) | Random Forest, Gradient Boosting, Stacking, Voting |
| [Handling Class Imbalance](05_advanced_ml/handling_class_imbalance.ipynb) | SMOTE, undersampling, cost-sensitive learning |

## Model Interpretability

| Notebook | Description |
|----------|-------------|
| [Interpretability with SHAP](06_model_interpretability/model_interpretability_shap.ipynb) | Feature importance, partial dependence, SHAP values |

## Production ML

| Notebook | Description |
|----------|-------------|
| [Model Deployment Guide](07_production_ml/model_deployment_guide.ipynb) | Serialization, FastAPI, Docker, monitoring |

## Projects & Case Studies

All 50+ projects in `08_projects/` covering:
- Classification, regression, clustering, NLP, computer vision
- Fraud detection, churn prediction, sentiment analysis, image recognition
- Hyperparameter tuning, pipeline design, feature engineering

## Google Colab

Run everything in Colab without local setup:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](opencolab_setup.ipynb)

1. Open `opencolab_setup.ipynb` → "Open in Colab"
2. Follow the cells to install packages, mount Drive, and generate data
3. Open any notebook from the file browser

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Generate synthetic datasets
python scripts/prepare_datasets.py

# Launch Jupyter
jupyter notebook
```

## About

This repository provides practical, hands-on data science education through well-organized tutorials and real-world projects.
