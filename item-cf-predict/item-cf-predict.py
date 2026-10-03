def item_cf_predict(user_ratings: list, item_similarities: list, target: int) -> float:
    """
    Returns the similarity-weighted rating prediction.
    """
    # Write code here

    weighted_sum = 0.0
    sim_sum = 0.0
    n = len(user_ratings)
    
    for i in range(n):
        if i == target:
            continue
        if user_ratings[i] > 0 and item_similarities[i] > 0:
            weighted_sum += item_similarities[i] * user_ratings[i]
            sim_sum += item_similarities[i]

    if sim_sum == 0:
        return 0.0
    return weighted_sum / sim_sum