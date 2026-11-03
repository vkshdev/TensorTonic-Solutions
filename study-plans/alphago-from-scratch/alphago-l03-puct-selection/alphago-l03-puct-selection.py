import numpy as np
def select_puct_action(visits, total_values, priors, legal_mask, cpuct):
    scores = np.full(len(visits), -np.inf, dtype=np.float64)

    total_visits = np.sum(visits)
    for i in range(len(visits)):
        if not legal_mask[i]:
            continue
        if visits[i] == 0:
            q = 0.0
        else:
            q = total_values[i] / visits[i]
        explore = cpuct * priors[i] * np.sqrt(total_visits) / (1 + visits[i])
        scores[i] = q + explore
    action = int(np.argmax(scores))
    return action, scores