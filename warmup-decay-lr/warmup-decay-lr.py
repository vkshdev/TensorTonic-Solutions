def warmup_decay_schedule(base_lr, warmup_steps, total_steps, current_step):
    """
    Compute the learning rate at a given step using warmup + linear decay.
    """
    # Write code here

    if current_step < warmup_steps and warmup_steps > 0:
        return base_lr * (current_step / warmup_steps)
    
    # decay phase
    elif current_step >= warmup_steps and current_step <= total_steps:
        decay_steps = total_steps - warmup_steps
        if decay_steps == 0:
            return float(base_lr)
        return base_lr * (total_steps - current_step) / decay_steps
    else:
        return 0