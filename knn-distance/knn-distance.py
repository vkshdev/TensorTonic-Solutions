import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """
    # Write code here

    X_train = np.array(X_train, dtype=float)
    X_test = np.array(X_test, dtype=float)

    if X_train.ndim == 1:
        X_train = X_train.reshape(-1, 1)
    if X_test.ndim == 1:
        X_test = X_test.reshape(-1, 1)

    n_train = X_train.shape[0]
    n_test = X_test.shape[0]
    diff = X_test[:, None, :] - X_train[None, :, :]
    dists = np.sqrt(np.sum(diff**2, axis=2))

    sorted_idx = np.argsort(dists, axis=1)
    if k > n_train:
        pad = -1 * np.ones((n_test, k - n_train), dtype=int)
        neighbors = np.hstack([sorted_idx[:, :n_train], pad])
    else:
        neighbors = sorted_idx[:, :k]

    return neighbors
    pass