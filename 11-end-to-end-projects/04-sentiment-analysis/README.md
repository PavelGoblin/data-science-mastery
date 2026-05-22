# Sentiment Analysis: NLP Classification Case Study

End-to-end project for classifying text as positive or negative sentiment using multiple NLP techniques and machine learning models.

## Key Techniques

- **Text Preprocessing**: Lowercasing, punctuation removal, stopword filtering, stemming (PorterStemmer) and lemmatization (WordNetLemmatizer)
- **Feature Extraction**: Bag of Words (CountVectorizer), TF-IDF (TfidfVectorizer), N-grams (unigrams, bigrams, trigrams)
- **Word Embeddings**: Conceptual demonstration of word2vec / GloVe for dense vector representations
- **LSTM**: Sequential deep learning model using TensorFlow/Keras with embedding layers
- **Model Comparison**: Cross-validated evaluation of Naive Bayes, Logistic Regression, SVM, and Random Forest

## Visualizations

- Word clouds for positive and negative vocabularies
- Model accuracy bar chart (cross-validation comparison)
- Confusion matrix heatmap
- Top-N most informative features (positive/negative coefficients)
- ROC curves for each classifier

## Results

Demonstrates how TF-IDF + Linear SVM or Logistic Regression typically yield the best balance of accuracy and interpretability for small-to-medium sentiment datasets.
