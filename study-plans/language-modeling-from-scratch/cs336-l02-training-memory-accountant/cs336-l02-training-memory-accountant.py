import math
def memory_accountant(
    param_shapes: list[list[int]], param_bytes_per_element: int,
    grad_bytes_per_element: int, activation_shapes: list[list[int]],
    activation_bytes_per_element: int, optimizer: str,
    optimizer_bytes_per_element: int,
) -> dict:
    """
    Returns integer byte counts for parameters, gradients, activations, optimizer_state, and total.
    """

    def count_elements(shape):
        if not shape:
            return 1
        return math.prod(shape)
    param_elems = sum(count_elements(s) for s in param_shapes)
    parameters = param_elems * param_bytes_per_element
    gradients = param_elems * grad_bytes_per_element
    act_elems = sum(count_elements(s) for s in activation_shapes)
    activations = act_elems * activation_bytes_per_element
    if optimizer == "sgd":
        opt_states = 0
    elif optimizer == "adagrad":
        opt_states = 1
    elif optimizer == "adam":
        opt_states = 2
    else:
        raise ValueError("Unknown optimizer")
    optimizer_state = param_elems * opt_states * optimizer_bytes_per_element
    total = parameters + gradients + activations + optimizer_state
    return {
        "parameters": parameters,
        "gradients": gradients,
        "activations": activations,
        "optimizer_state": optimizer_state,
        "total": total
    }
