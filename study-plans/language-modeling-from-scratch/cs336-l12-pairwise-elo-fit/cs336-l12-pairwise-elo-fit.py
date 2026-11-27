import torch
import math

def pairwise_elo_fit(
    num_models: int, model_a: torch.Tensor, model_b: torch.Tensor,
    outcomes: torch.Tensor, steps: int, learning_rate: int | float,
) -> dict:
    """
    Returns a dict: ratings, rankings, fitted_probabilities, component_ids (tensors), connected (bool).
    """
    device = outcomes.device
    ratings = torch.zeros(num_models, dtype=torch.float64, device=device)
    m = len(outcomes)

    if m:
        coeff = math.log(10.0) / (400.0 * m)
        for _ in range(steps):
            probs = 1.0 / (
                1.0 + torch.pow(
                    10.0,
                    (ratings[model_b] - ratings[model_a]) / 400.0
                )
            )
            residual = coeff * (outcomes - probs)
            grad = torch.zeros_like(ratings)
            grad.index_add_(0, model_a, residual)
            grad.index_add_(0, model_b, -residual)
            ratings.add_(learning_rate * grad)
            ratings.sub_(ratings.mean())
        fitted_probabilities = 1.0 / (
            1.0 + torch.pow(
                10.0,
                (ratings[model_b] - ratings[model_a]) / 400.0
            )
        )
    else:
        fitted_probabilities = torch.empty(
            0, dtype=torch.float64, device=device
        )
    parent = list(range(num_models))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in zip(model_a.tolist(), model_b.tolist()):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[rb] = ra
    comp_map = {}
    comp_ids = []
    comp = 0

    for i in range(num_models):
        root = find(i)
        if root not in comp_map:
            comp_map[root] = comp
            comp += 1
        comp_ids.append(comp_map[root])
    component_ids = torch.tensor(
        comp_ids,
        dtype=torch.int64,
        device=device
    )
    rankings = torch.tensor(
        sorted(
            range(num_models),
            key=lambda i: (-float(ratings[i]), i)
        ),
        dtype=torch.int64,
        device=device
    )
    return {
        "ratings": ratings,
        "rankings": rankings,
        "fitted_probabilities": fitted_probabilities,
        "component_ids": component_ids,
        "connected": comp == 1,
    }