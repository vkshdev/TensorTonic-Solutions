def user_based_cf_prediction(similarities: list, ratings: list) -> float:
    """
    Returns the positive-similarity weighted rating prediction.
    """
    # Write code here
    
    num = 0.0
    den = 0.0
    for i in range(len(similarities)):
        s = similarities[i]
        r = ratings[i]
        if s > 0:
            num += s * r
            den += s
    if den == 0:
        return 0.0
    return round(num / den,6)