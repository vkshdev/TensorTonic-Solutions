import numpy as np

def naive_bayes_bernoulli(X_train, y_train, X_test, alpha=1.0):
    """
    Compute log-likelihood P(y|x) for Bernoulli Naive Bayes.
    """
    # Write code here
    
    X_train = np.asarray(X_train, dtype=int)
    y_train = np.asarray(y_train, dtype=int)
    X_test = np.asarray(X_test, dtype=int)

    n_train, d = X_train.shape
    classes, class_counts = np.unique(y_train, return_counts=True)
    n_classes = len(classes)

    priors = class_counts / n_train
    log_priors = np.log(priors)
    theta = np.zeros((n_classes, d))
    for idx, c in enumerate(classes):
        X_c = X_train[y_train == c]
        count_ones = X_c.sum(axis=0)
        theta[idx] = (count_ones + alpha) / (X_c.shape[0] + 2 * alpha)

    log_posteriors = []
    for x in X_test:
        logs = []
        for idx in range(n_classes):
            ll = (x * np.log(theta[idx]) + (1 - x) * np.log(1 - theta[idx])).sum()
            logs.append(log_priors[idx] + ll)
        log_posteriors.append(logs)

    return np.array(log_posteriors)
    pass