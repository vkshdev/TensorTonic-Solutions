import torch
def assistant_only_sft_mask(
    input_ids: torch.Tensor, role_ids: torch.Tensor,
    attention_mask: torch.Tensor, assistant_role: int = 1,
) -> dict:
    """
    Returns a dict: labels (input token dtype), loss_mask (Boolean tensor).
    """
    labels = torch.full_like(input_ids, -100)
    loss_mask = torch.zeros_like(input_ids, dtype=torch.bool)
    src_mask = attention_mask[:, :-1]
    tgt_mask = attention_mask[:, 1:]
    tgt_roles = role_ids[:, 1:]
    tgt_tokens = input_ids[:, 1:]

    cond = src_mask & tgt_mask & (tgt_roles == assistant_role)
    labels[:, :-1] = torch.where(cond, tgt_tokens, labels[:, :-1])
    loss_mask[:, :-1] = cond
    return {"labels": labels, "loss_mask": loss_mask}
