import numpy as np

def go_group_liberties(board: list, row: int, col: int) -> tuple:
    """
    Returns: a tuple of two sorted coordinate lists: group and liberties.
    """

    board = np.array(board)
    color = board[row, col]
    n = board.shape[0]

    group = set()
    liberties = set()
    stack = [(row, col)]

    while stack:
        r, c = stack.pop()
        if (r, c) in group:
            continue
        group.add((r, c))

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if board[nr, nc] == color and (nr, nc) not in group:
                    stack.append((nr, nc))
                elif board[nr, nc] == 0:
                    liberties.add((nr, nc))

    group_list = sorted([list(x) for x in group])
    liberty_list = sorted([list(x) for x in liberties])
    return (group_list, liberty_list)
    pass
