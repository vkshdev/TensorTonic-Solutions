def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here

    if len(ordering) == 0:
        raise ValueError("ordering list must not empty")
    mapping = {}
    for i in range(len(ordering)):
        category = ordering[i]
        mapping[category] = i
    result = []
    for v in values:
        result.append(mapping[v])
    return result