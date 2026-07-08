def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here

    if window_size < 1:
        raise ValueError("window size be >= 1")
    if len(values) < window_size:
        raise ValueError("values should have at least window size element")
    result = []
    for i in range(len(values) - window_size + 1):
        window = sorted(values[i:i+window_size])
        k = window_size
        if k % 2 == 1:
            median = float(window[k // 2])
        else:
            median = (window[k // 2 - 1] + window[k // 2]) / 2.0
        result.append(median)
    return result