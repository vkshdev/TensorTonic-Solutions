import numpy as np

def batch_generator(X: list, y: list, batch_size: int, seed: int = 42, drop_last: bool = False):
    """
    Returns a generator of (X_batch, y_batch) tuples.
    """
    # Write code here
    
    X = np.asarray(X)
    y = np.asarray(y)
    rng = np.random.default_rng(seed)
    n = len(X)
    idx = np.arange(n)
    rng.shuffle(idx)
    for start in range(0, n, batch_size):
        end = start + batch_size
        batch_idx = idx[start:end]
        if drop_last and len(batch_idx) < batch_size:
            break
        yield X[batch_idx], y[batch_idx]