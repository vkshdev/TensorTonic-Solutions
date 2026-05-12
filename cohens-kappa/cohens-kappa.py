import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here

    rater1 = np.asarray(rater1, dtype=int)
    rater2 = np.asarray(rater2, dtype=int)
    if rater1.shape != rater2.shape or rater1.ndim != 1:
        return None
        
    n = len(rater1)
    po = np.mean(rater1 == rater2)
    labels = np.union1d(rater1, rater2)
    pe = 0.0
    for lbl in labels:
        p1 = np.sum(rater1 == lbl) / n
        p2 = np.sum(rater2 == lbl) / n
        pe += p1 * p2
    if pe == 1.0:
        return 1.0
        
    return float((po - pe) / (1 - pe))
    
    pass