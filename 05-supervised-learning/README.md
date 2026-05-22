# Supervised Learning

Algorithms that learn from labeled data to make predictions. Covers both regression (continuous targets) and classification (categorical targets).

## Prerequisites

- Data manipulation with Pandas
- Basic understanding of probability

## Learning Objectives

- Implement and interpret linear and logistic regression
- Build decision trees and understand their interpretability trade-offs
- Apply SVM for high-dimensional classification
- Use KNN for non-parametric learning
- Understand Naive Bayes for text classification
- Evaluate models using appropriate metrics
- Diagnose bias-variance trade-off with learning curves

## Notebooks

| Notebook | Description | Key Techniques |
|----------|-------------|----------------|
| [01-linear-regression](01-linear-regression.ipynb) | Linear, Ridge, Lasso, ElasticNet | OLS, regularization, polynomial features, learning curves |
| [02-logistic-regression](02-logistic-regression.ipynb) | Binary and multi-class classification | Sigmoid, log-loss, OvR vs Softmax, regularization |
| [03-decision-trees](03-decision-trees.ipynb) | Interpretable tree-based models | Gini/Entropy, pruning, feature importance, decision boundaries |
| [04-naive-bayes](04-naive-bayes.ipynb) | Probabilistic classification | Gaussian, Multinomial, Bernoulli, Complement NB |
| [05-support-vector-machines](05-support-vector-machines.ipynb) | Maximum margin classification | Linear/RBF/Poly kernels, C/gamma, margin visualization |
| [06-k-nearest-neighbors](06-k-nearest-neighbors.ipynb) | Similarity-based learning | Distance metrics, K selection, scaling importance, KD-trees |
| [07-model-selection-and-evaluation](07-model-selection-and-evaluation.ipynb) | Model comparison and tuning | CV strategies, grid/random search, learning curves, metrics |
