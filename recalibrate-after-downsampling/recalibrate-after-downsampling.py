import numpy as np

def recalibrate_after_downsampling(p: list, negative_keep_rate: float) -> np.ndarray:
    """
    Returns the corrected probabilities for a model trained after keeping only a fraction of the negatives.
    """
    p = np.asarray(p, dtype=float)
    return p / (p + (1 - p) / negative_keep_rate)
