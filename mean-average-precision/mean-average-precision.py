import numpy as np

def mean_average_precision(y_true_list, y_score_list, k=None):
    """
    Compute Mean Average Precision (mAP) for multiple retrieval queries.
    """
    # Write code here

    ap_scores = []
    for y_true, y_score in zip(y_true_list, y_score_list):
        y_true = np.asarray(y_true, dtype=int)
        y_score = np.asarray(y_score, dtype=float)
        if y_true.shape != y_score.shape or y_true.ndim != 1:
            ap_scores.append(0.0)
            continue
            
        order = np.argsort(-y_score, kind="mergesort")
        y_true_sorted = y_true[order]
        if k is not None:
            y_true_sorted = y_true_sorted[:k]
        R = np.sum(y_true)
        if R == 0:
            ap_scores.append(0.0)
            continue
            
        rel_cum = np.cumsum(y_true_sorted)
        ranks = np.arange(1, len(y_true_sorted) + 1)
        prec_at_k = rel_cum / ranks
        ap = np.sum(prec_at_k[y_true_sorted == 1]) / R
        ap_scores.append(float(ap))
    map_value = float(np.mean(ap_scores)) if ap_scores else 0.0
    return map_value, ap_scores
    
    pass