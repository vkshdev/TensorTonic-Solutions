def double_exponential_smoothing(series, alpha, beta):
    """
    Apply Holt's linear trend method and return the level values.
    """
    # Write code here

    if not (0 < alpha <= 1 and 0 < beta <= 1):
        raise ValueError("alpha and beta must in (0,1]")
    if len(series) < 2:
        raise ValueError("series must have least 2 elements")
        
    level = series[0]
    trend = series[1] - series[0]
    result = [float(level)]

    for t in range(1, len(series)):
        value = series[t]
        new_level = alpha * value + (1 - alpha) * (level + trend)
        new_trend = beta * (new_level - level) + (1 - beta) * trend
        level, trend = new_level, new_trend
        result.append(float(level))
    return result