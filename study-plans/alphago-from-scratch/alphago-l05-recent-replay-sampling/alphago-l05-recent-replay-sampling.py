import copy
def sample_recent_replay_batch(
    games: list | tuple,
    window_size: int,
    position_indices: list | tuple,
) -> tuple[list, int]:
    """
    Returns independent sampled records and the eligible position count.
    """

    recent_games = games[-window_size:]
    pool = []
    for g in recent_games:
        for record in g:
            pool.append(record)
    eligible_count = len(pool)
    batch = [copy.deepcopy(pool[idx]) for idx in position_indices]
    return (batch, eligible_count)