# Data Science Mastery

A hands-on data science learning repository with topic-based organization, practical Jupyter notebooks, and real-world projects.

## Directory Structure

```
01_python_fundamentals/      # NumPy, Pandas, Data Visualization
02_data_handling/            # Preprocessing, comprehensive Pandas guide
03_supervised_learning/      # Linear models, Trees, SVM, KNN, Naive Bayes
04_unsupervised_learning/    # Clustering, Anomaly detection, Association rules
05_advanced_ml/              # Pipelines, Feature selection, Ensembles, Imbalanced data
06_model_interpretability/   # SHAP, Permutation importance, PDP (unique)
07_production_ml/            # Model deployment, API serving, Docker (unique)
08_projects/                 # 50+ real-world case studies and projects
```

## Python Fundamentals

| Notebook | Description |
|----------|-------------|
| [NumPy Crash Course](01_python_fundamentals/numpy_crash_course.ipynb) | Arrays, broadcasting, vectorization, linear algebra |
| [Pandas Essentials](01_python_fundamentals/pandas_essentials.ipynb) | DataFrames, I/O, filtering, aggregation basics |
| [Data Visualization](01_python_fundamentals/data_visualization.ipynb) | Matplotlib, Seaborn, Plotly fundamentals |

## Data Handling

| Notebook | Description |
|----------|-------------|
| [Pandas Comprehensive Guide](02_data_handling/pandas_comprehensive_guide.ipynb) | Deep-dive into merge, reshape, groupby, time series, text, missing data |
| [Data Preprocessing](02_data_handling/data_preprocessing_techniques.ipynb) | Scaling, encoding, outlier handling, feature engineering |

## Supervised Learning

| Notebook | Description |
|----------|-------------|
| [Linear Models](03_supervised_learning/linear_models.ipynb) | Linear/Logistic regression, regularization |
| [Decision Trees](03_supervised_learning/decision_trees.ipynb) | Classification & regression trees, pruning |
| [Naive Bayes](03_supervised_learning/naive_bayes_classifier.ipynb) | Gaussian, Multinomial, Bernoulli classifiers |
| [Nearest Neighbors](03_supervised_learning/nearest_neighbors.ipynb) | KNN for classification & regression |
| [Support Vector Machines](03_supervised_learning/support_vector_machines.ipynb) | SVM, kernels, margin optimization |

## Unsupervised Learning

| Notebook | Description |
|----------|-------------|
| [Clustering Algorithms](04_unsupervised_learning/clustering_algorithms.ipynb) | K-Means, DBSCAN, Hierarchical, evaluation |
| [Outlier & Anomaly Detection](04_unsupervised_learning/outlier_and_anomaly_detection.ipynb) | Isolation Forest, LOF, statistical methods |
| [Association Rules](04_unsupervised_learning/association_rules_mining.ipynb) | Apriori, FP-Growth, market basket analysis |

## Advanced ML Techniques

| Notebook | Description |
|----------|-------------|
| [Pipelines & Transformers](05_advanced_ml/pipelines_and_transformers.ipynb) | ColumnTransformer, FeatureUnion, custom transformers |
| [Feature Selection Methods](05_advanced_ml/feature_selection_methods.ipynb) | Filter, wrapper, embedded, RFE, mutual information |
| [Model Selection & Evaluation](05_advanced_ml/model_selection_and_evaluation.ipynb) | Cross-validation, hyperparameter tuning, metrics |
| [Ensemble Learning](05_advanced_ml/ensemble_learning.ipynb) | Random Forest, Gradient Boosting, Stacking, Voting |
| [Handling Class Imbalance](05_advanced_ml/handling_class_imbalance.ipynb) | SMOTE, undersampling, cost-sensitive learning |

## Model Interpretability *(unique content)*

| Notebook | Description |
|----------|-------------|
| [Interpretability with SHAP](06_model_interpretability/model_interpretability_shap.ipynb) | Feature importance, partial dependence, SHAP values |

## Production ML *(unique content)*

| Notebook | Description |
|----------|-------------|
| [Model Deployment Guide](07_production_ml/model_deployment_guide.ipynb) | Serialization, FastAPI, Docker, monitoring |

## Projects & Case Studies

All 50+ projects in `08_projects/` covering:
- Classification, regression, clustering, NLP, computer vision
- Fraud detection, churn prediction, sentiment analysis, image recognition
- Hyperparameter tuning, pipeline design, feature engineering

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
