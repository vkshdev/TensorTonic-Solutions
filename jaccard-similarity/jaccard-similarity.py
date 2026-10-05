def jaccard_similarity(set_a: list, set_b: list) -> float:
    """
    Returns the Jaccard similarity of the two item collections.
    """
    # Write code here

    A = set(set_a)
    B = set(set_b)
    union = A | B
    intersection = A & B
    if len(union) == 0:
        return 0.0
    return len(intersection) / len(union)