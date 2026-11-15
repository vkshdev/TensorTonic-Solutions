import numpy as np

def temperature_data_mixture(token_counts: list, alpha: int | float, training_budget: int) -> dict:
    """
    Returns a dict: probabilities, expected_tokens, expected_epochs (float64 arrays).
    """
    counts = np.array(token_counts, dtype=np.float64)
    probabilities = np.zeros(len(counts), dtype=np.float64)
    expected_tokens = np.zeros(len(counts), dtype=np.float64)
    expected_epochs = np.zeros(len(counts), dtype=np.float64)
    positive = counts > 0

    if np.any(positive):
        log_counts = np.log(counts[positive])
        weights = np.exp(alpha * (log_counts - np.max(log_counts)))
        probabilities[positive] = weights / np.sum(weights)
        expected_tokens = training_budget * probabilities
        expected_epochs[positive] = (
            expected_tokens[positive] / counts[positive]
        )
    return {
        "probabilities": probabilities,
        "expected_tokens": expected_tokens,
        "expected_epochs": expected_epochs,
    }
    pass
