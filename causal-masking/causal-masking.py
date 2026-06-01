import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    # Write code here

    scores = np.array(scores, dtype=float)
    if scores.shape[-1] != scores.shape[-2]:
        raise ValueError("Last two dimensions must be equal (T,T)")
        
    T = scores.shape[-1]
    mask = np.triu(np.ones((T, T)), k=1).astype(bool)
    masked_scores = scores.copy()
    masked_scores[..., mask] = mask_value
    return masked_scores
    
    pass