def canonical_preference_pairs(records: list) -> dict:
    """
    Returns a dict with pairs: a list of prompt_id, winner_id, loser_id dictionaries.
    """
    pairs = []
    for record in records:
        prompt_id = record["prompt_id"]
        candidates = sorted(record["candidates"], key=lambda x: x["rank"])
        n = len(candidates)
        for i in range(n):
            for j in range(i + 1, n):
                pairs.append({
                    "prompt_id": prompt_id,
                    "winner_id": candidates[i]["id"],
                    "loser_id": candidates[j]["id"]
                })
    return {"pairs": pairs}
