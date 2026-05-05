import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here

    fpr = np.asarray(fpr, dtype=float)
    tpr = np.asarray(tpr, dtype=float)
    if fpr.shape != tpr.shape or fpr.ndim != 1 or fpr.size < 2:
        return None
        
    return float(np.trapezoid(tpr, fpr))
    
    pass