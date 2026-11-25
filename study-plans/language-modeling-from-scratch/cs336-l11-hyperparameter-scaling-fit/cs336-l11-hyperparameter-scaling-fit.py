import torch

def hyperparameter_scaling_fit(
    model_scales: torch.Tensor, learning_rates: torch.Tensor,
    batch_sizes: torch.Tensor, measured_losses: torch.Tensor,
    target_scale: int | float,
) -> dict:
    """
    Returns a dict of optima, scaling coefficients/exponents, residual tensors and target predictions.
    """
    optima = []
    best_lrs = []
    best_batches = []

    for i in range(len(model_scales)):
        flat_idx = torch.argmin(measured_losses[i]).item()
        lr_idx, bs_idx = divmod(flat_idx, measured_losses.shape[2])
        best_lr = learning_rates[lr_idx]
        best_batch = batch_sizes[bs_idx]
        best_loss = measured_losses[i, lr_idx, bs_idx]
        best_lrs.append(best_lr)
        best_batches.append(best_batch)
        optima.append({
            "model_scale": float(model_scales[i]),
            "learning_rate": float(best_lr),
            "batch_size": float(best_batch),
            "loss": float(best_loss),
        })
        
    x = torch.log(model_scales.to(torch.float64))
    def fit(values):
        y = torch.log(torch.stack(values).to(torch.float64))
        A = torch.stack([torch.ones_like(x), x], dim=1)
        sol = torch.linalg.lstsq(A, y.unsqueeze(1)).solution.squeeze()
        intercept = sol[0]
        exponent = sol[1]
        fitted = intercept + exponent * x
        residuals = y - fitted
        coefficient = torch.exp(intercept)
        return coefficient, exponent, residuals
    lr_coeff, lr_exp, lr_residuals = fit(best_lrs)
    bs_coeff, bs_exp, bs_residuals = fit(best_batches)
    target_scale = torch.tensor(
        target_scale,
        dtype=torch.float64,
        device=model_scales.device,
    )
    
    target_lr = lr_coeff * target_scale.pow(lr_exp)
    target_bs = bs_coeff * target_scale.pow(bs_exp)
    return {
        "optima": optima,
        "learning_rate_coefficient": float(lr_coeff),
        "learning_rate_exponent": float(lr_exp),
        "batch_size_coefficient": float(bs_coeff),
        "batch_size_exponent": float(bs_exp),
        "target_learning_rate": float(target_lr),
        "target_batch_size": float(target_bs),
        "learning_rate_residuals": lr_residuals,
        "batch_size_residuals": bs_residuals,
    }