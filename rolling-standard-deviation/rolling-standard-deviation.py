import math

def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    # Write code here

    if window_size < 1:
        raise ValueError("window size must be >= 1")
    if len(values) < window_size:
        raise ValueError("value must at least window size elements")
    result = []
    for i in range(len(values) - window_size + 1):
        window = values[i:i+window_size]
        mean = sum(window) / window_size
        variance = sum((x - mean) ** 2 for x in window) / window_size 
        std = math.sqrt(variance)
        result.append(std)
    return result