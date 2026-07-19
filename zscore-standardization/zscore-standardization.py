import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here

    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        mean_val = np.mean(X)
        std_val = np.std(X)
        denom = std_val + eps
        return (X - mean_val) / denom
    elif X.ndim == 2:
        mean_val = np.mean(X, axis=axis, keepdims=True)
        std_val = np.std(X, axis=axis, keepdims=True)
        denom = std_val + eps
        return (X - mean_val) / denom
    else:
        raise ValueError("input must be 1D or 2D array")
    pass