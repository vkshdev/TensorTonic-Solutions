def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here

    if degree < 0:
        raise ValueError("degree must >= 0")
    if len(values) == 0:
        raise ValueError("values must not empty")
    result = []
    for x in values:
        row = []
        for p in range(degree + 1):
            row.append(x ** p)
        result.append(row)
    return result