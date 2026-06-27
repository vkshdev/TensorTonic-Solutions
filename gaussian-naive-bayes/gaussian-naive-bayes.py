import numpy as np
def gaussian_naive_bayes(X_train, y_train, X_test, eps=1e-9):
    """
    Predict class labels for test samples using Gaussian Naive Bayes.
    """
    # Write code here

    X_train = np.asarray(X_train, dtype=float)
    y_train = np.asarray(y_train, dtype=int)
    X_test = np.asarray(X_test, dtype=float)

    classes, class_counts = np.unique(y_train, return_counts=True)
    n_classes = len(classes)
    n_train, d = X_train.shape

    priors = class_counts / n_train
    log_priors = np.log(priors)

    means = np.zeros((n_classes, d))
    variances = np.zeros((n_classes, d))
    for idx, c in enumerate(classes):
        X_c = X_train[y_train == c]
        means[idx] = X_c.mean(axis=0)
        variances[idx] = X_c.var(axis=0) + eps 

    predictions = []
    for x in X_test:
        log_posteriors = []
        for idx in range(n_classes):
            mean = means[idx]
            var = variances[idx]
            ll = -0.5 * np.log(2 * np.pi * var) - ((x - mean) ** 2) / (2 * var)
            log_post = log_priors[idx] + ll.sum()
            log_posteriors.append(log_post)
        predictions.append(classes[np.argmax(log_posteriors)])

    return predictions