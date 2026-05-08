import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here

    y_true = list(y_true)
    y_pred = [min(max(p, eps), 1 - eps) for p in y_pred]
    losses = [-(y * math.log(p) + (1 - y) * math.log(1 - p)) for y, p in zip(y_true, y_pred)]
    return losses
    
    pass