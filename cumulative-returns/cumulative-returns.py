def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here

    if not returns:
        raise ValueError("returns must be non-empty")
    wealth = 1.0
    result = []
    for r in returns:
        if r <= -1:
            raise ValueError("each return must be greater than -1")
        wealth = wealth * (1 + r)
        result.append(wealth - 1)
    return result