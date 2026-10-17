import numpy as np

def initialize_mcts_edges(policy_logits: np.ndarray, legal_mask: np.ndarray) -> dict:
    """
    Returns: N as an int64 array; W, Q, and P as float64 arrays in a dictionary.
    """
    
    logits = policy_logits.astype(np.float64)
    mask = legal_mask.astype(bool)
    legal_idx = np.flatnonzero(mask)
    if len(legal_idx) > 0:
        legal_logits = logits[legal_idx]
        m = np.max(legal_logits)
        exp_logits = np.exp(legal_logits - m)
        probs = exp_logits / np.sum(exp_logits)
    else:
        probs = np.array([])
    N = np.zeros_like(logits, dtype=np.int64)
    W = np.zeros_like(logits, dtype=np.float64)
    Q = np.zeros_like(logits, dtype=np.float64)
    P = np.zeros_like(logits, dtype=np.float64)
    P[legal_idx] = probs

    return {"N": N, "W": W, "Q": Q, "P": P}
