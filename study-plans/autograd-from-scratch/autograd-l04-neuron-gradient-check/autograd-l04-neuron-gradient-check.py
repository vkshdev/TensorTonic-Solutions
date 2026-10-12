import torch

def neuron_gradient_check(inputs: torch.Tensor, weights: torch.Tensor, bias: torch.Tensor, h: float) -> tuple:
    """
    Returns five tensors: analytic/numerical weight gradients, analytic/numerical bias gradients, maximum error.
    """

    x = torch.tensor(inputs, dtype=torch.float64)
    w = torch.tensor(weights, dtype=torch.float64)
    b = torch.tensor(bias, dtype=torch.float64)
    y = torch.tanh(torch.dot(w, x) + b)
    
    grad_w_analytic = (1 - y**2) * x
    grad_b_analytic = (1 - y**2)
    grad_w_num = torch.zeros_like(w)
    for i in range(len(w)):
        w_perturb = w.clone()
        w_perturb[i] += h
        y_perturb = torch.tanh(torch.dot(w_perturb, x) + b)
        grad_w_num[i] = (y_perturb - y) / h
    y_bias_perturb = torch.tanh(torch.dot(w, x) + (b + h))
    grad_b_num = (y_bias_perturb - y) / h
    diffs = []
    if len(w) > 0:
        diffs.append(torch.abs(grad_w_analytic - grad_w_num).max())
    diffs.append(torch.abs(grad_b_analytic - grad_b_num))
    max_disagreement = torch.max(torch.stack(diffs))
    return (grad_w_analytic, grad_w_num, grad_b_analytic, grad_b_num, max_disagreement)
    pass