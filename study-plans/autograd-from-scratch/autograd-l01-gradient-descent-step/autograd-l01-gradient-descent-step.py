import numpy as np

def gradient_descent_step(values: list, gradients: list, learning_rate: float) -> tuple[list, float]:
    """
    Returns a fresh list of updated values and the predicted objective change.
    """
    v = np.asarray(values, dtype=np.float64)
    g = np.asarray(gradients, dtype=np.float64)
    v_new = v - learning_rate * g
    delta = float(np.dot(g, v_new - v))
    return v_new.tolist(), delta
    pass
