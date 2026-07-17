def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here

    if len(categories) != len(targets):
        raise ValueError("categories and targets must have the same length")
    if len(categories) == 0:
        raise ValueError("input lists must not empty")

    sums = {}
    counts = {}
    for cat, val in zip(categories, targets):
        if cat not in sums:
            sums[cat] = 0.0
            counts[cat] = 0
        sums[cat] = sums[cat] + val
        counts[cat] = counts[cat] + 1

    means = {}
    for cat in sums:
        means[cat] = sums[cat] / counts[cat]
    result = []
    for cat in categories:
        result.append(float(means[cat]))
    return result