import torch

def conditional_perplexity(
    logits: torch.Tensor, target_ids: torch.Tensor, response_mask: torch.Tensor,
) -> dict:
    """
    Returns a dict: negative_log_likelihood (float), perplexity (float), selected_token_count (int).
    """

    log_probs = torch.log_softmax(logits, dim=-1)
    target_log_probs = log_probs.gather(-1, target_ids.unsqueeze(-1)).squeeze(-1)
    selected = target_log_probs[response_mask]

    M = selected.numel()
    if M == 0:
        nll = 0.0
        ppl = 1.0
    else:
        nll = float((-selected.to(torch.float64).mean()).item())
        ppl = float(torch.exp(torch.tensor(nll, dtype=torch.float64)).item())

    return {
        "negative_log_likelihood": nll,
        "perplexity": ppl,
        "selected_token_count": int(M),
    }
    pass
