def gae(rewards: list, values: list, gamma: float, lam: float) -> list:
    """
    Returns the generalized advantage estimate at every timestep.
    """
    # Write code here

    T = len(rewards)
    advantages = [0.0] * T
    next_adv = 0.0
    for t in reversed(range(T)):
        delta = rewards[t] + gamma * values[t+1] - values[t]
        advantages[t] = delta + gamma * lam * next_adv
        next_adv = advantages[t]
    return advantages