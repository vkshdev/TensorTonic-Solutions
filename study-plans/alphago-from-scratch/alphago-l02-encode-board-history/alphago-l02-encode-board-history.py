import torch
def encode_go_history(history: list[torch.Tensor], to_play: int) -> torch.Tensor:
    """
    Returns: a float32 tensor of shape (17, board size, board size) on the history device.
    """

    device = history[0].device if history else torch.device("cpu")
    board_size = history[0].shape[0] if history else 0
    planes = []
    for t in range(8):
        if t < len(history):
            board = history[t]
            planes.append((board == to_play).float())
            planes.append((board == -to_play).float())
        else:
            planes.append(torch.zeros((board_size, board_size), device=device))
            planes.append(torch.zeros((board_size, board_size), device=device))
    if board_size > 0:
        color_plane = torch.ones((board_size, board_size), device=device) if to_play == 1 \
                      else torch.zeros((board_size, board_size), device=device)
        planes.append(color_plane)
    else:
        planes.append(torch.tensor([], dtype=torch.float32, device=device))
    return torch.stack(planes).to(torch.float32)
    pass