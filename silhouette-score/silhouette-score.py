import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    # Write code here

    X = np.asarray(X, dtype=float)
    labels = np.asarray(labels, dtype=int)
    n_samples = X.shape[0]
    if labels.shape[0] != n_samples or n_samples < 2:
        return None
        
    diff = X[:, None, :] - X[None, :, :]
    dist_matrix = np.sqrt(np.sum(diff**2, axis=2))
    scores = []
    for i in range(n_samples):
        same_cluster = labels == labels[i]
        other_clusters = labels != labels[i]
        if np.sum(same_cluster) > 1:
            a_i = np.sum(dist_matrix[i, same_cluster]) / (np.sum(same_cluster) - 1)
        else:
            a_i = 0.0
        b_i = np.inf
        for lbl in np.unique(labels[other_clusters]):
            mask = labels == lbl
            mean_dist = np.mean(dist_matrix[i, mask])
            if mean_dist < b_i:
                b_i = mean_dist
        s_i = (b_i - a_i) / max(a_i, b_i) if max(a_i, b_i) > 0 else 0.0
        scores.append(s_i)
        
    return float(np.mean(scores))
    
    pass