def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here

    if len(X) == 0:
        raise ValueError("X must be non empty")
    result = []
    
    for row in X:
        if len(row) == 0:
            raise ValueError("each sample must have least 1 feature")
        new_row = list(row)
        d = len(row)
        for i in range(d):
            for j in range(i + 1, d):
                product = row[i] * row[j]
                new_row.append(product)
        result.append(new_row)

    return result