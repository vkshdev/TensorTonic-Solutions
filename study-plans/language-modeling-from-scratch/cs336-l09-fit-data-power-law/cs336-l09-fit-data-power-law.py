import torch

def fit_data_power_law(data_sizes: torch.Tensor, losses: torch.Tensor, target_sizes: torch.Tensor, floor_candidates: torch.Tensor) -> dict:
    """
    Returns a dict: floor, coefficient, exponent, predictions (float64 tensor), rmse.
    """
    x = torch.log(data_sizes.to(torch.float64))
    best = None
    best_rmse = float("inf")
    for floor in floor_candidates:
        floor = float(floor)
        if torch.any(losses <= floor):
            continue
        y = torch.log(losses - floor)
        A = torch.stack([torch.ones_like(x), x], dim=1)
        sol = torch.linalg.lstsq(A, y.unsqueeze(1)).solution.squeeze()
        a = sol[0]
        b = sol[1]
        coeff = torch.exp(a).item()
        exponent = -b.item()

        if not (
            coeff > 0
            and exponent > 0
            and torch.isfinite(torch.tensor(coeff))
            and torch.isfinite(torch.tensor(exponent))
        ):
            continue
        preds = floor + coeff * data_sizes.pow(-exponent)
        rmse = torch.sqrt(torch.mean((preds - losses) ** 2)).item()
        if rmse < best_rmse:
            best_rmse = rmse
            best = (floor, coeff, exponent)
    floor, coeff, exponent = best
    predictions = floor + coeff * target_sizes.to(torch.float64).pow(-exponent)

    return {
        "floor": float(floor),
        "coefficient": float(coeff),
        "exponent": float(exponent),
        "predictions": predictions,
        "rmse": float(best_rmse),
    }