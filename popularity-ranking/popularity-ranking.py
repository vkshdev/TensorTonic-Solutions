def popularity_ranking(items: list, min_votes: int, global_mean: float) -> list:
    """
    Returns the weighted rating for every item.
    """
    # Write code here

    results = []
    for avg, votes in items:
        wr = (votes / (votes + min_votes)) * avg + (min_votes / (votes + min_votes)) * global_mean
        results.append(wr)
    return results