import numpy as np 

def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here

    y_true = np.asarray(y_true, dtype=int)
    y_pred = np.asarray(y_pred, dtype=float)
    
    if y_true.shape != y_pred.shape or y_true.ndim != 1:
        return None
        
    n = len(y_true)
    bin_indices = np.floor(y_pred * n_bins).astype(int)
    bin_indices = np.clip(bin_indices, 0, n_bins - 1)
    ece = 0.0
    for b in range(n_bins):
        mask = bin_indices == b
        if not np.any(mask):
            continue  
        acc = np.mean(y_true[mask])
        conf = np.mean(y_pred[mask])
        ece += (np.sum(mask) / n) * abs(acc - conf)
        
    return float(ece)
    
    pass