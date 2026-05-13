def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here

    if n_items <= 0:
        return 0.0
    unique_items = set()
    for recs in recommendations:
        unique_items.update(recs)
    coverage = len(unique_items) / n_items
    return float(coverage)