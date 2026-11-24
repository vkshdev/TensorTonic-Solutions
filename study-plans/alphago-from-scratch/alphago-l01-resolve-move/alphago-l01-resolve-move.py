import numpy as np

def resolve_go_action(board: list, player: int, action: int, consecutive_passes: int, move_count: int) -> tuple:
    """
    Returns: a tuple: next board, player, captures, consecutive passes, move count, terminal.
    """
    board = np.array(board, dtype=int)
    n = len(board)
    next_board = board.copy()

    def get_group_and_liberties(r, c):
        color = next_board[r, c]
        group = set()
        liberties = set()
        stack = [(r, c)]
        while stack:
            x, y = stack.pop()
            if (x, y) in group:
                continue
            group.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if next_board[nx, ny] == color:
                        stack.append((nx, ny))
                    elif next_board[nx, ny] == 0:
                        liberties.add((nx, ny))
        return group, liberties
    captures = 0

    if action == n * n:
        consecutive_passes += 1
    else:
        row, col = divmod(action, n)
        next_board[row, col] = player
        consecutive_passes = 0
        seen = set()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < n:
                if next_board[nr, nc] == -player and (nr, nc) not in seen:
                    group, liberties = get_group_and_liberties(nr, nc)
                    seen.update(group)
                    if len(liberties) == 0:
                        captures += len(group)
                        for x, y in group:
                            next_board[x, y] = 0
    move_count += 1
    next_player = -player
    terminal = (
        consecutive_passes >= 2
        or move_count >= 2 * n * n
    )
    return (
        next_board,
        next_player,
        captures,
        consecutive_passes,
        move_count,
        terminal,
    )
