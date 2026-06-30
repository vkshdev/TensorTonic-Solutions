import numpy as np

def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here
    
    values = np.asarray(values, dtype=float)
    if not (0 < alpha <= 1):
        raise ValueError("alpha must be betwen 0 and 1")
    ema = [values[0]]
    for t in range(1, len(values)):
        ema_t = alpha * values[t] + (1 - alpha) * ema[-1]
        ema.append(ema_t)
    return ema