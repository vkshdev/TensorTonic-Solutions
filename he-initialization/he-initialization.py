def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here

    W = np.asarray(W, dtype=float)
    if fan_in < 1:
        raise ValueError("fan_in must be >= 1")
    limit = np.sqrt(6.0 / fan_in)
    scaled = W * (2 * limit) - limit
    return scaled.tolist()