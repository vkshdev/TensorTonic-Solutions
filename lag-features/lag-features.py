def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here

    if len(series) == 0:
        raise ValueError("series must not empty")
    if len(lags) == 0:
        raise ValueError("lags must not empty")
    max_lag = max(lags)
    if len(series) < max_lag + 1:
        raise ValueError("series must have least max(lags) + 1 elements")
    result = []
    for t in range(max_lag, len(series)):
        row = []
        for lag in lags:
            row.append(series[t - lag])
        result.append(row)

    return result