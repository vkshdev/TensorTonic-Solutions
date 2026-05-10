import numpy as np

def confusion_matrix_norm(y_true, y_pred, num_classes=None, normalize='none'):
    """
    Compute confusion matrix with optional normalization.
    """
    # Write code here

    y_true = np.asarray(y_true, dtype=int)
    y_pred = np.asarray(y_pred, dtype=int)
    if y_true.shape != y_pred.shape or y_true.ndim != 1:
        return None

    if num_classes is None:
        num_classes = max(y_true.max(), y_pred.max()) + 1

    if np.any(y_true < 0) or np.any(y_true >= num_classes):
        return None
    if np.any(y_pred < 0) or np.any(y_pred >= num_classes):
        return None

    cm = np.bincount(y_true * num_classes + y_pred,
                     minlength=num_classes * num_classes).reshape(num_classes, num_classes)

    if normalize == 'none':
        return cm

    cm = cm.astype(float)
    if normalize == 'true':
        row_sums = cm.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1
        cm = cm / row_sums
    elif normalize == 'pred':
        col_sums = cm.sum(axis=0, keepdims=True)
        col_sums[col_sums == 0] = 1
        cm = cm / col_sums
    elif normalize == 'all':
        total = cm.sum()
        if total == 0:
            total = 1
        cm = cm / total
    else:
        return None

    return cm
    
    pass