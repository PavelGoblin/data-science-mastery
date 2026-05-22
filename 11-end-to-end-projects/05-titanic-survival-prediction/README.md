# Titanic Survival Prediction

Binary classification case study predicting passenger survival from the Titanic disaster. Uses synthetic data simulated to mirror real Titanic passenger features.

## Key Techniques

- **EDA**: Survival rate analysis by passenger class, sex, age groups, family size, and embarkation port
- **Missing Data Imputation**: Median/strategy-based imputation for age, fare; mode imputation for embarked
- **Feature Engineering**: Title extraction from passenger names, family size computation, cabin letter extraction, age/fare binning, one-hot encoding of categorical variables
- **Multiple Classifiers Compared**: LogisticRegression, DecisionTree, RandomForest, GradientBoosting, SVM
- **Cross-Validation**: Stratified k-fold CV for robust model comparison
- **Hyperparameter Tuning**: GridSearchCV on top-performing models
- **Evaluation**: Confusion matrix, classification report, ROC curves, feature importance analysis
