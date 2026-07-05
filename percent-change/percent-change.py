def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here

    if len(series) < 2:
        raise ValueError("series must have at least 2 elements")
    result = []
    for i in range(1, len(series)):
        prev = series[i-1]
        curr = series[i]
        if prev == 0:
            result.append(0.0)
        else:
            result.append((curr - prev) / prev)
    return result