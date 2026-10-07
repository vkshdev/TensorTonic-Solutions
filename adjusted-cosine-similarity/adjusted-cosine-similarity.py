def adjusted_cosine_similarity(ratings_matrix: list, item_i: int, item_j: int) -> float:
    """
    Returns the adjusted cosine similarity between the requested items.
    """
    # Write code here

    num = 0.0
    den_i = 0.0
    den_j = 0.0
    for user_ratings in ratings_matrix:
        ri = user_ratings[item_i]
        rj = user_ratings[item_j]
        if ri == 0 or rj == 0:
            continue
        nonzero = [r for r in user_ratings if r != 0]
        mean_u = sum(nonzero) / len(nonzero)
        ci = ri - mean_u
        cj = rj - mean_u
        num += ci * cj
        den_i += ci * ci
        den_j += cj * cj

    if den_i == 0 or den_j == 0:
        return 0.0
    return round(num / ((den_i ** 0.5) * (den_j ** 0.5)), 6)
    pass