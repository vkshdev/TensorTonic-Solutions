import torch

def mlp_forward(inputs: torch.Tensor, weights: list[torch.Tensor], biases: list[torch.Tensor]) -> tuple:
    """
    Returns the final output tensor and a list of layer-output tensors.
    """

    h = inputs
    layer_outputs = []
    for W, b in zip(weights, biases):
        h = torch.mv(W, h) + b
        h = torch.tanh(h)
        layer_outputs.append(h)
    return h, layer_outputs
