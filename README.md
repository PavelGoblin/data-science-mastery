# Data Science Mastery

A comprehensive, structured learning repository covering the complete data science pipeline — from Python fundamentals to production-ready ML deployments. Designed for self-paced learners who want both theoretical understanding and hands-on practice.

## What Makes This Different

Unlike typical tutorial repos that just dump notebooks, this project is organized as a **structured curriculum** with:

- **Progressive difficulty** — each module builds on the previous one
- **Dual format** — detailed markdown explanations accompany every notebook
- **Real-world case studies** — projects use actual datasets with business context
- **Mature MLOps patterns** — pipelines, column transformers, grid search, cross-validation from day one
- **Visual-first teaching** — every algorithm comes with custom visualizations and decision diagrams

---

## Repository Structure

```
data-science-mastery/
├── 01-python-foundations/          # Python for data science (arrays, comprehensions, vectorization)
├── 02-mathematics-for-ml/          # Linear algebra, calculus, probability, statistics fundamentals
├── 03-data-manipulation/           # NumPy, Pandas, data cleaning, feature engineering
├── 04-data-visualization/          # Matplotlib, Seaborn, Plotly — storytelling with data
├── 05-supervised-learning/         # Regression & classification algorithms in depth
├── 06-unsupervised-learning/       # Clustering, dimensionality reduction, anomaly detection
├── 07-advanced-techniques/         # Ensembles, pipelines, feature selection, hyperparameter tuning
├── 08-deep-learning/               # Neural networks, CNNs, RNNs, transfer learning
├── 09-natural-language-processing/ # Text preprocessing, embeddings, sentiment, transformers
├── 10-time-series-forecasting/     # ARIMA, Prophet, LSTM for temporal data
├── 11-end-to-end-projects/         # Full ML projects from EDA to deployment
├── scripts/                        # Reusable utility functions
├── datasets/                       # Dataset descriptions and download links
├── requirements.txt                # Python dependencies
├── setup.py                        # Package installer
└── README.md                       # You are here
```

---

## Learning Roadmap

### Phase 1: Foundations

| Module | Topics | Key Skills |
|--------|--------|------------|
| Python Foundations | Data types, comprehensions, generators, OOP, decorators | Writing efficient Python code |
| Mathematics for ML | Linear algebra, calculus, probability, statistics | Understanding how algorithms work under the hood |
| Data Manipulation | NumPy arrays, Pandas DataFrames, data cleaning, EDA | Loading, inspecting, transforming real-world data |
| Data Visualization | Matplotlib API, Seaborn stats plots, Plotly interactives | Communicating insights visually |

### Phase 2: Core Machine Learning

| Module | Topics | Key Skills |
|--------|--------|------------|
| Supervised Learning | Linear/Logistic regression, Decision Trees, SVM, KNN, Naive Bayes | Building predictive models |
| Unsupervised Learning | K-Means, DBSCAN, Hierarchical clustering, PCA, t-SNE | Finding patterns in unlabeled data |
| Advanced Techniques | Random Forests, Gradient Boosting, Pipelines, Feature Selection, Hyperparameter Tuning | Production-grade ML workflows |

### Phase 3: Specialized Domains

| Module | Topics | Key Skills |
|--------|--------|------------|
| Deep Learning | ANN, CNN, RNN/LSTM, Transfer Learning, Dropout, BatchNorm | Building neural networks with TensorFlow/Keras |
| NLP | Tokenization, TF-IDF, Word2Vec, Sentiment Analysis, Transformers | Processing and understanding text data |
| Time Series | Stationarity, ARIMA, Prophet, LSTM forecasting | Predicting future values from temporal data |

### Phase 4: End-to-End Projects

| Project | Domain | Techniques |
|---------|--------|------------|
| House Price Prediction | Regression | Feature engineering, Ridge/Lasso, ensemble stacking |
| Customer Churn Prediction | Classification | Imbalanced data handling, ROC analysis, business KPIs |
| Image Classification | Computer Vision | CNN, data augmentation, transfer learning (EfficientNet) |
| Sentiment Analysis | NLP | Text preprocessing, TF-IDF + embeddings, LSTM, BERT |

---

## Getting Started

### Prerequisites

- Python 3.9+
- Git
- 4GB+ RAM (8GB recommended for deep learning sections)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/data-science-mastery.git
cd data-science-mastery

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
.\venv\Scripts\Activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

### Navigate the Curriculum

Start with `01-python-foundations/` if you are new to Python, or jump directly to your area of interest. Each module folder contains:

- A `README.md` with learning objectives and theory
- One or more `.ipynb` notebooks with executable code
- Practice exercises at the end of each notebook

---

## Key Features

### 1. Visual Algorithm Guides

Every algorithm notebook includes a visual decision guide to help you understand when to use which technique:

```
┌─────────────────────────────────────────┐
│         DATA SCIENCE CHEAT SHEET        │
├─────────────────────────────────────────┤
│  Labeled Data?                          │
│  ├── Yes → Supervised Learning          │
│  │   ├── Continuous target? → Regression│
│  │   └── Categorical target? → Classify │
│  └── No  → Unsupervised Learning        │
│       ├── Need groups? → Clustering     │
│       ├── Reduce dims? → PCA/t-SNE      │
│       └── Find outliers? → Anomaly Det  │
└─────────────────────────────────────────┘
```

### 2. Progressive Complexity

Each topic follows a consistent template:
1. **Intuition** — What does this algorithm do? Real-world analogy.
2. **Math** — The core equation(s) with plain-English explanation.
3. **Implementation** — From scratch (educational) + using scikit-learn (practical).
4. **Evaluation** — Appropriate metrics with interpretation guidelines.
5. **Practice** — 3-5 exercises with varying difficulty.

### 3. MLOps from the Start

Every supervised learning notebook demonstrates:
- Train/validation/test splits
- Cross-validation strategies
- Pipeline construction with ColumnTransformers
- Hyperparameter tuning via GridSearchCV / RandomizedSearchCV
- Model persistence with joblib

---

## Projects Deep Dive

### House Price Prediction
- **Dataset**: Ames Housing (alternative to Boston — more features, no ethical concerns)
- **Focus**: Feature engineering, handling missing values, log-transform of skewed targets, regularization
- **Deployment**: Flask API with pickled pipeline

### Customer Churn Prediction
- **Dataset**: Telco customer churn
- **Focus**: Imbalanced classification (SMOTE, class weights), uplift modeling, cost-benefit analysis
- **Metric**: Precision-Recall curve over accuracy

### Image Classification
- **Dataset**: CIFAR-10 / custom dataset
- **Focus**: CNN architecture design, data augmentation, transfer learning with fine-tuning
- **Framework**: TensorFlow/Keras

### Sentiment Analysis
- **Dataset**: IMDB reviews / Twitter sentiment
- **Focus**: Text cleaning, TF-IDF vs. word embeddings, LSTM vs. Transformer comparison
- **Framework**: TensorFlow + Hugging Face Transformers

---

## Contributing

Contributions are welcome! If you find errors, want to add content, or improve explanations:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

Please ensure notebooks are run from top to bottom before committing.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- Inspired by the need for structured, practical data science education
- Built with scikit-learn, TensorFlow, Pandas, and the Python data ecosystem
- Datasets sourced from Kaggle, UCI repository, and open data portals
