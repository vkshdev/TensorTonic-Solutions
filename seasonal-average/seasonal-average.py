def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    # Write code here

    if period < 1:
        raise ValueError("period must be >= 1")
    if len(series) < period:
        raise ValueError("series must at least period elements")

    result = []
    for p in range(period):
        values_at_position = [series[i] 
                              for i in range(p, len(series), period)]
        mean_val = sum(values_at_position) / len(values_at_position)
        result.append(float(mean_val))
    return result