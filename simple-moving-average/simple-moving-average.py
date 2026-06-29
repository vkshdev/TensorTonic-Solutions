import numpy as np
def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    values = np.asarray(values, dtype=float)
    n = len(values)
    k = int(window_size)

    if k < 1 or k > n:
        raise ValueError("window size must be between 1 and len(values)")
    cumsum = np.cumsum(values)
    window_sums = cumsum[k-1:] - np.concatenate(([0.0], cumsum[:-k]))
    sma = window_sums / k

    return sma.tolist()