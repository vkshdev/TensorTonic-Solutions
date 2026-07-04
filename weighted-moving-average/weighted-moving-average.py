def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    n = len(values)
    k = len(weights)
    if k < 1 or n < k:
        raise ValueError("weights length must be >=1 and <= len(values)")
        
    w_sum = sum(weights)
    result = []
    for i in range(n - k + 1):
        window = values[i:i+k]
        weighted_sum = sum(w * x for w, x in zip(weights, window))
        result.append(weighted_sum / w_sum)
    return result