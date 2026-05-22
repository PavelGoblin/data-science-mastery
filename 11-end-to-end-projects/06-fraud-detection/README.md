# Fraud Detection: Imbalanced Classification Case Study

Detecting fraudulent transactions in a highly imbalanced dataset where fraud represents only ~2% of all transactions.

## Key Techniques

- **Imbalanced Data Handling**: Class weighting, SMOTE oversampling, balanced subsampling
- **Anomaly Detection**: Isolation Forest for unsupervised outlier detection
- **Threshold Tuning**: Optimizing decision thresholds on precision-recall curve
- **Cost-Benefit Analysis**: Minimizing total business cost (false negatives > false positives)
- **Evaluation Metrics**: Precision, recall, F1, PR-AUC (not accuracy)

## Methods Compared

1. Baseline (predict all non-fraud)
2. Logistic Regression (class-weighted)
3. Random Forest (balanced subsampling)
4. Isolation Forest (unsupervised)
5. SMOTE + Classifier
6. Threshold-optimized model for business goals

## Key Insight

Accuracy is misleading with 2% fraud rate — a model predicting "no fraud" for every case is 98% accurate but useless. Proper evaluation requires precision-recall analysis and cost-aware threshold selection.
