# Image Classification

This project demonstrates a complete image classification pipeline using the `load_digits` dataset from scikit-learn (8x8 images of handwritten digits, 10 classes). It serves as a proxy for real-world image classification tasks like MNIST or CIFAR.

## Key Techniques

- **Classic ML pipelines**: Logistic Regression, SVM with RBF kernel, Random Forest on flattened pixel features
- **Dimensionality reduction**: PCA projection of digit images visualized in 2D space, followed by classification on reduced features
- **Simple Neural Network**: Feedforward network built with TensorFlow/Keras (Dense layers, ReLU activations, softmax output)
- **Evaluation**: Confusion matrix analysis, misclassification inspection, accuracy/training-time comparison across all approaches
