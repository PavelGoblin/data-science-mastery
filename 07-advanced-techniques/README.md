# Advanced Techniques

Production-ready ML workflows: combining multiple models, building pipelines, engineering features, and tuning hyperparameters systematically.

## Prerequisites

- Supervised learning basics
- Unsupervised learning basics

## Learning Objectives

- Build ensemble models (bagging, boosting, stacking) for superior performance
- Construct ML pipelines to prevent data leakage
- Use ColumnTransformers for heterogeneous data
- Select features systematically (filter, wrapper, embedded methods)
- Handle imbalanced datasets appropriately
- Tune hyperparameters with cross-validation

## Notebooks

| Notebook | Description | Techniques |
|----------|-------------|------------|
| [01-ensemble-methods](01-ensemble-methods.ipynb) | Combining models for better predictions | Voting, Bagging, RF, AdaBoost, Gradient Boosting, Stacking |
| [02-feature-selection](02-feature-selection.ipynb) | Selecting the most relevant features | Filter (chi2, MI), Wrapper (RFE, SFS), Embedded (Lasso, tree importance) |
| [03-feature-engineering](03-feature-engineering.ipynb) | Creating better features | Binning, encoding, date features, interactions, cyclical encoding |
| [04-imbalanced-classes](04-imbalanced-classes.ipynb) | Handling class imbalance | SMOTE, class weights, threshold tuning, cost-sensitive learning |
| [05-pipelines-and-column-transformers](05-pipelines-and-column-transformers.ipynb) | Production ML workflows | Pipeline, ColumnTransformer, FeatureUnion, GridSearchCV, custom transformers |
| [06-data-preprocessing](06-data-preprocessing.ipynb) | Cleaning data for ML | Missing value imputation, scaling, encoding, transformations, outlier handling |
