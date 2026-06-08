def linear_lr(step, total_steps, initial_lr, final_lr=0.0, warmup_steps=0) -> float:
    """
    Linear warmup (0→initial_lr) then linear decay (initial_lr→final_lr).
    Steps are 0-based; clamp at final_lr after total_steps.
    """
    # Write code here

    if total_steps <= 0:
        return float(final_lr)

    if step < warmup_steps and warmup_steps > 0:
        return (step / warmup_steps) * initial_lr

    elif step <= total_steps:
        decay_steps = max(1, total_steps - warmup_steps) 
        progress = (step - warmup_steps) / decay_steps
        return final_lr + (initial_lr - final_lr) * (1 - progress)

    else:
        return float(final_lr)
    pass