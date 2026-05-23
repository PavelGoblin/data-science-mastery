<div align="center">

# 🧠 Data Science Mastery

**A comprehensive, hands-on data science repository** — from Python fundamentals to production-ready ML deployment.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)](https://jupyter.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-150458?)](https://xgboost.readthedocs.io)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](opencolab_setup.ipynb)
[![License](https://img.shields.io/badge/License-MIT-green)]()

**90+ notebooks · 30 Python topics · 16 ML algorithms · 50+ projects · 4 unique modules**

</div>

---

## 📋 Table of Contents

- [🗺️ Roadmap](#-roadmap)
- [📦 Repository Structure](#-repository-structure)
- [🐍 Python Fundamentals](#-python-fundamentals)
- [📊 Data Handling](#-data-handling)
- [📈 Supervised Learning](#-supervised-learning)
- [🔍 Unsupervised Learning](#-unsupervised-learning)
- [⚡ Advanced ML Techniques](#-advanced-ml-techniques)
- [🔮 Model Interpretability](#-model-interpretability)
- [🚀 Production ML](#-production-ml)
- [📁 Projects & Case Studies](#-projects--case-studies)
- [🤖 Google Colab](#-google-colab)
- [🚦 Getting Started](#-getting-started)

---

## 🗺️ Roadmap

```
🐍 Python    →  📊 Data        →  📈 Supervised    →  🔍 Unsupervised
Fundamentals     Handling          Learning             Learning
                                   
    ↓                ↓                  ↓                    ↓
   
⚡ Advanced     →  🔮 Model       →  🚀 Production   →  📁 50+ Projects
   ML              Interpretability    ML                   & Case Studies
```

---

## 📦 Repository Structure

```
📦 data-science-mastery
├── 📁 01_python_fundamentals/      # NumPy · Pandas · Visualization · Deep Learning · Python Reference
├── 📁 02_data_handling/            # Preprocessing · Comprehensive Pandas Guide
├── 📁 03_supervised_learning/      # Linear Models · Trees · SVM · KNN · Naive Bayes · XGBoost
├── 📁 04_unsupervised_learning/    # Clustering · Anomaly Detection · Association Rules · PCA
├── 📁 05_advanced_ml/              # Pipelines · Feature Selection · Ensembles · Imbalanced Data
├── 📁 06_model_interpretability/   # SHAP · Permutation Importance · Partial Dependence
├── 📁 07_production_ml/            # Model Deployment · FastAPI · Docker · Monitoring
├── 📁 08_projects/                 # 50+ Real-World Case Studies & Projects
├── 📁 Data/                        # Synthetic Datasets (auto-generated)
├── 📁 scripts/                     # Data Preparation Utilities
├── 📄 opencolab_setup.ipynb        # One-click Colab environment setup
└── 📄 requirements.txt             # Python dependencies
```

---

## 🐍 Python Fundamentals

| # | Notebook | What You'll Learn |
|---|----------|-------------------|
| 01 | [Python Complete Reference](01_python_fundamentals/python_complete_reference.ipynb) | 30 topics · 138 code examples · Types, Strings, OOP, Decorators, Generators, Regex, JSON, Threading |
| 02 | [NumPy Crash Course](01_python_fundamentals/numpy_crash_course.ipynb) | Arrays, broadcasting, vectorization, linear algebra operations |
| 03 | [Pandas Essentials](01_python_fundamentals/pandas_essentials.ipynb) | DataFrames, I/O, filtering, aggregation, groupby basics |
| 04 | [Data Visualization](01_python_fundamentals/data_visualization.ipynb) | Matplotlib, Seaborn, Plotly — line, bar, scatter, heatmaps |
| 05 | [Intro to Deep Learning](01_python_fundamentals/intro_to_deep_learning.ipynb) | Neural networks with TensorFlow/Keras — regression & classification |
| | **🛠️ NumPy Projects** | |
| 06 | [Image Processing with NumPy](01_python_fundamentals/numpy_image_processing.ipynb) | Grayscale, edge detection (Sobel), cropping, flips, brightness with array ops |
| 07 | [Monte Carlo Simulations](01_python_fundamentals/numpy_monte_carlo.ipynb) | π estimation, stock price (GBM), birthday problem, antithetic variates |
| 08 | [Linear Algebra Applications](01_python_fundamentals/numpy_linear_algebra.ipynb) | PCA from scratch, SVD image compression, PageRank, solving linear systems |
| | **🛠️ Pandas Projects** | |
| 09 | [Automated EDA Pipeline](01_python_fundamentals/pandas_automated_eda.ipynb) | Data profiling, missing analysis, correlation, outlier detection, EDA report |
| 10 | [Time Series Analysis](01_python_fundamentals/pandas_time_series_analysis.ipynb) | Resampling, rolling windows, seasonal decomposition, lag features |
| 11 | [Data Wrangling Pipeline](01_python_fundamentals/pandas_data_wrangling.ipynb) | Cleaning, standardization, dedup, merging, feature engineering |
| | **🛠️ Visualization Projects** | |
| 12 | [Interactive Dashboards (Plotly)](01_python_fundamentals/viz_interactive_dashboards.ipynb) | Scatter matrix, treemap, parallel coordinates, subplot dashboard |
| 13 | [Statistical Storytelling (Seaborn)](01_python_fundamentals/viz_statistical_storytelling.ipynb) | FacetGrid, PairGrid, regression plots, categorical comparisons |
| 14 | [Custom Matplotlib Visualizations](01_python_fundamentals/viz_custom_matplotlib.ipynb) | Dual-axis, GridSpec, custom colormaps, 3D plots, annotations |
| | **🛠️ Deep Learning Projects** | |
| 15 | [CNN for Fashion MNIST](01_python_fundamentals/dl_fashion_mnist_cnn.ipynb) | Conv2D, MaxPooling, confusion matrix, prediction visualization |
| 16 | [Transfer Learning](01_python_fundamentals/dl_transfer_learning.ipynb) | MobileNetV2 pretrained model, fine-tuning on CIFAR-10 |

---

## 📊 Data Handling

| # | Notebook | What You'll Learn |
|---|----------|-------------------|
| 01 | [Pandas Comprehensive Guide](02_data_handling/pandas_comprehensive_guide.ipynb) | Loading, indexing, merge/join, pivot, groupby, time series, text, missing data, styling (11 topics in 1 notebook) |
| 02 | [Data Preprocessing](02_data_handling/data_preprocessing_techniques.ipynb) | Scaling, encoding, outlier handling, feature engineering |
| | **🛠️ Data Handling Projects** | |
| 03 | [Data Cleaning Pipeline](02_data_handling/data_cleaning_pipeline.ipynb) | Duplicates, invalid values, outlier capping, email validation, imputation |
| 04 | [Feature Engineering Project](02_data_handling/feature_engineering_project.ipynb) | Encoding, log transform, interaction features, scaler comparison, selection |

---

## 📈 Supervised Learning

| # | Notebook | What You'll Learn |
|---|----------|-------------------|
| 01 | [Linear Models](03_supervised_learning/linear_models.ipynb) | Linear & Logistic regression, Ridge, Lasso, ElasticNet |
| 02 | [Decision Trees](03_supervised_learning/decision_trees.ipynb) | Classification & regression trees, pruning strategies |
| 03 | [Naive Bayes](03_supervised_learning/naive_bayes_classifier.ipynb) | Gaussian, Multinomial, Bernoulli classifiers |
| 04 | [Nearest Neighbors](03_supervised_learning/nearest_neighbors.ipynb) | KNN for classification & regression, distance metrics |
| 05 | [Support Vector Machines](03_supervised_learning/support_vector_machines.ipynb) | SVM, kernel trick, margin optimization, hyperparameter tuning |
| 06 | [Gradient Boosting](03_supervised_learning/gradient_boosting_xgboost.ipynb) | **XGBoost · LightGBM · CatBoost** — head-to-head benchmarks |
| | **🛠️ Supervised Learning Projects** | |
| 07 | [Credit Risk Classification](03_supervised_learning/credit_risk_classification.ipynb) | Logistic Regression vs RF vs XGBoost — ROC curves, feature importance |
| 08 | [Medical Diagnosis with Ensembles](03_supervised_learning/medical_diagnosis_ensemble.ipynb) | Bagging, Boosting, Voting, Stacking — cross-validated comparison |

---

## 🔍 Unsupervised Learning

| # | Notebook | What You'll Learn |
|---|----------|-------------------|
| 01 | [Clustering Algorithms](04_unsupervised_learning/clustering_algorithms.ipynb) | K-Means, DBSCAN, Hierarchical, silhouette score, elbow method |
| 02 | [Outlier & Anomaly Detection](04_unsupervised_learning/outlier_and_anomaly_detection.ipynb) | Isolation Forest, LOF, statistical methods |
| 03 | [Association Rules](04_unsupervised_learning/association_rules_mining.ipynb) | Apriori, FP-Growth, market basket analysis |
| 04 | [Dimensionality Reduction](04_unsupervised_learning/dimensionality_reduction.ipynb) | **PCA · t-SNE · UMAP** — visualization, noise reduction, feature extraction |
| | **🛠️ Unsupervised Learning Projects** | |
| 05 | [Customer Segmentation](04_unsupervised_learning/customer_segmentation_project.ipynb) | K-Means, elbow method, silhouette score, segment profiling |
| 06 | [Anomaly Detection (Network)](04_unsupervised_learning/anomaly_detection_network.ipynb) | Isolation Forest, LOF, Z-score — detection rate comparison |

---

## ⚡ Advanced ML Techniques

| # | Notebook | What You'll Learn |
|---|----------|-------------------|
| 01 | [Pipelines & Transformers](05_advanced_ml/pipelines_and_transformers.ipynb) | ColumnTransformer, FeatureUnion, custom sklearn transformers |
| 02 | [Feature Selection](05_advanced_ml/feature_selection_methods.ipynb) | Filter, wrapper, embedded methods, RFE, mutual information |
| 03 | [Feature Engineering](05_advanced_ml/feature_engineering_techniques.ipynb) | Polynomial features, frequency/target encoding, binning, date features |
| 04 | [Model Selection & Evaluation](05_advanced_ml/model_selection_and_evaluation.ipynb) | Cross-validation, grid search, metrics, learning curves |
| 05 | [Ensemble Learning](05_advanced_ml/ensemble_learning.ipynb) | Random Forest, Gradient Boosting, Stacking, Voting classifiers |
| 06 | [Handling Imbalance](05_advanced_ml/handling_class_imbalance.ipynb) | SMOTE, undersampling, cost-sensitive learning, class weights |
| | **🛠️ Advanced ML Projects** | |
| 07 | [ML Pipeline with Tuning](05_advanced_ml/ml_pipeline_tuning.ipynb) | ColumnTransformer, model comparison, RandomizedSearchCV, learning curves |
| 08 | [Model Selection & CV](05_advanced_ml/model_selection_cv.ipynb) | KFold, StratifiedKFold, RepeatedKFold, validation curves |

---

## 🔮 Model Interpretability

> *Unique — not found in most tutorials*

| # | Notebook | What You'll Learn |
|---|----------|-------------------|
| 01 | [Interpretability with SHAP](06_model_interpretability/model_interpretability_shap.ipynb) | Feature importance, permutation importance, partial dependence plots, SHAP values |

---

## 🚀 Production ML

> *Unique — not found in most tutorials*

| # | Notebook | What You'll Learn |
|---|----------|-------------------|
| 01 | [Model Deployment Guide](07_production_ml/model_deployment_guide.ipynb) | Model serialization, FastAPI REST API, Docker containerization, monitoring checklist |

---

## 📁 Projects & Case Studies

**50+ projects** in `08_projects/` covering real-world scenarios:

<div align="center">

| Domain | Projects |
|--------|----------|
| 🏦 **Finance** | Fraud detection, credit risk, insurance claim prediction |
| 🏥 **Healthcare** | Cancer prediction, healthcare data analysis, readmission risk |
| 🛒 **Retail & E-commerce** | Customer churn, market basket analysis, recommendation engine |
| 🏠 **Real Estate** | House price prediction, similar houses search |
| 📰 **NLP & Text** | Sentiment analysis, review classification, spam detection |
| 🖼️ **Computer Vision** | Face detection, clothing classifier, digit recognition, color quantization |
| 👥 **HR & People** | Employee attrition, income prediction, visa status |
| 🚢 **Classic Datasets** | Titanic survival, IMDB ratings, wine quality |
| 🛠️ **Techniques** | Grid search, pipeline design, feature selection, model comparison |

</div>

---

## 🤖 Google Colab

Run everything in your browser — no local setup required.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](opencolab_setup.ipynb)

**3-step workflow:**

```python
# 1. Open opencolab_setup.ipynb → click "Open in Colab"
# 2. Run all cells (installs packages, mounts Drive, generates data)
# 3. Open any notebook → run the first "Colab Setup" cell → done!
```

Every notebook that reads data has a built-in Colab preamble — just run the first cell.

---

## 🚦 Getting Started

### Local setup

```bash
# Clone the repo
git clone https://github.com/PavelGoblin/data-science-mastery.git
cd data-science-mastery

# Install dependencies
pip install -r requirements.txt

# Generate synthetic datasets
python scripts/prepare_datasets.py

# Launch Jupyter
jupyter notebook
```

### Docker (coming soon)

```bash
# docker build -t data-science-mastery .
# docker run -p 8888:8888 data-science-mastery
```

---

## 📊 By the Numbers

```
📓 90+ Jupyter notebooks   🐍 30 Python topics   🤖 16 ML algorithms
📁 50+ case studies        🎯 4 unique modules   ☁️ Colab-ready
📊 19 hands-on projects    🛠️ 8 topic areas      🎓 Project-based learning
```

---

## 📄 License

This project is for educational purposes. Built with ❤️ for the data science community.

---

<div align="center">

**⭐ Star this repo if you find it useful!** · [Report Issue](https://github.com/PavelGoblin/data-science-mastery/issues)

</div>
