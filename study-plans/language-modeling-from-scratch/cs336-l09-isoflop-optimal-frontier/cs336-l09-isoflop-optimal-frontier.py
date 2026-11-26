import torch

def isoflop_optimal_frontier(compute_budgets: torch.Tensor, parameter_counts: torch.Tensor, terminal_losses: torch.Tensor) -> dict:
    """
    Returns a dict: optima (list of dicts), frontier_scale, frontier_exponent.
    """
    
    optima = []
    best_params = []
    for i in range(len(compute_budgets)):
        x = torch.log(parameter_counts[i].to(torch.float64))
        y = terminal_losses[i].to(torch.float64)
        A = torch.stack([x * x, x, torch.ones_like(x)], dim=1)
        coeffs = torch.linalg.lstsq(A, y.unsqueeze(1)).solution.squeeze()
        a = coeffs[0]
        b = coeffs[1]
        c = coeffs[2]
        x_star = -b / (2 * a)
        n_star = torch.exp(x_star)
        loss_star = a * x_star * x_star + b * x_star + c
        tokens = compute_budgets[i] / (6.0 * n_star)
        best_params.append(n_star)
        optima.append({
            "compute": float(compute_budgets[i]),
            "parameters": float(n_star),
            "tokens": float(tokens),
            "loss": float(loss_star),
        })
        
    log_c = torch.log(compute_budgets.to(torch.float64))
    log_n = torch.log(torch.stack(best_params))
    A = torch.stack([torch.ones_like(log_c), log_c], dim=1)
    coeffs = torch.linalg.lstsq(A, log_n.unsqueeze(1)).solution.squeeze()
    log_k = coeffs[0]
    alpha = coeffs[1]
    k = torch.exp(log_k)
    return {
        "optima": optima,
        "frontier_scale": float(k),
        "frontier_exponent": float(alpha),
    }