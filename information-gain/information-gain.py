import numpy as np

def entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    # Write code here

    y = np.asarray(y)
    mask = np.asarray(split_mask, dtype=bool)
    H_parent = entropy(y)
    y_left = y[mask]
    y_right = y[~mask]

    n_left, n_right = len(y_left), len(y_right)
    N = n_left + n_right
    if n_left == 0 or n_right == 0:
        return 0.0
    H_children = (n_left / N) * entropy(y_left) + (n_right / N) * entropy(y_right)

    return H_parent - H_children
    pass
