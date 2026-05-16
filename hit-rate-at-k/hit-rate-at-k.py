def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here

    if not recommendations or not ground_truth or k < 1:
        return 0.0
    hits = 0
    n_users = len(recommendations)
    for recs, truth in zip(recommendations, ground_truth):
        top_k = set(recs[:k])
        truth_set = set(truth)
        if top_k & truth_set:
            hits += 1
    return hits / n_users if n_users > 0 else 0.0