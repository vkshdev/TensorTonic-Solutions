def differencing(series, order=1):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here

    if order < 1:
        raise ValueError("order must be >= 1")
    if len(series) < order + 1:
        raise ValueError("series must have at least order+1 elements")

    result = series[:]
    for _ in range(order):
        result = [result[i] - result[i-1] for i in range(1, len(result))]
    return result