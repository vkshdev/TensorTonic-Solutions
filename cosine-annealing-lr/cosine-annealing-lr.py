import math 

def cosine_annealing_schedule(base_lr, min_lr, total_steps, current_step):
    """
    Compute the learning rate using cosine annealing.
    """
    # Write code here

    if total_steps <= 0:
        raise ValueError("total_steps must be > 0")
    if not (0 <= current_step <= total_steps):
        raise ValueError("current_step must be between 0 and total_steps")
    if base_lr <= min_lr:
        raise ValueError("base_lr must be greater than min_lr")

    lr = min_lr + 0.5 * (base_lr - min_lr) * (1 + math.cos(math.pi * current_step / total_steps))
    return float(lr)