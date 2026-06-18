import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here

    preds = np.array(predictions, dtype=int)
    T, N = preds.shape

    final = []
    for i in range(N):
        counts = np.bincount(preds[:, i])
        max_count = counts.max()
        chosen = np.where(counts == max_count)[0].min()
        final.append(chosen)
    return final