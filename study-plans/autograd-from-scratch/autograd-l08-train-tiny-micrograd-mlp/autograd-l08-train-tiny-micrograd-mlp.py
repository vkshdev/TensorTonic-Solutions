import torch

def train_tiny_micrograd_mlp(inputs: torch.Tensor, targets: torch.Tensor, weights: list[torch.Tensor], biases: list[torch.Tensor], learning_rate: float, steps: int) -> tuple:
    """
    Returns final predictions, final loss, trained weights, trained biases, and pre-update loss history.
    """
    
    weights = [w.clone() for w in weights]
    biases = [b.clone() for b in biases]
    loss_history = []
    def forward(x):
        activations = [x]
        preacts = []
        h = x
        for W, b in zip(weights, biases):
            z = h @ W.t() + b
            h = torch.tanh(z)
            preacts.append(z)
            activations.append(h)
        return activations, preacts
        
    for _ in range(steps):
        activations, preacts = forward(inputs)
        preds = activations[-1].squeeze(-1)
        loss = ((preds - targets) ** 2).sum()
        loss_history.append(loss.clone())
        if inputs.shape[0] == 0:
            continue
        dpred = 2 * (preds - targets)
        delta = dpred.unsqueeze(-1)
        grad_w = [None] * len(weights)
        grad_b = [None] * len(biases)
        
        for layer in reversed(range(len(weights))):
            h = activations[layer + 1]
            dz = delta * (1 - h * h)
            grad_w[layer] = dz.t() @ activations[layer]
            grad_b[layer] = dz.sum(dim=0)
            if layer > 0:
                delta = dz @ weights[layer]
                
        for layer in range(len(weights)):
            weights[layer] = weights[layer] - learning_rate * grad_w[layer]
            biases[layer] = biases[layer] - learning_rate * grad_b[layer]
    activations, _ = forward(inputs)
    preds = activations[-1].squeeze(-1)
    loss = ((preds - targets) ** 2).sum()
    return preds, loss, weights, biases, loss_history