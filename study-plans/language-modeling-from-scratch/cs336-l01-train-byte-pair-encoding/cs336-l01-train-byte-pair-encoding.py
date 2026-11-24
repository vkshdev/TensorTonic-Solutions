def train_bpe(corpus: list[str], vocab_size: int) -> dict:
    """
    Returns a dictionary of learned vocab entries and ordered merges.
    """
    token_bytes = {i: [i] for i in range(256)}
    sequences = []
    for text in corpus:
        sequences.append(list(text.encode("utf-8")))
    merges = []
    vocab = []
    next_id = 256
    
    while next_id < vocab_size:
        counts = {}
        for seq in sequences:
            for i in range(len(seq) - 1):
                pair = (seq[i], seq[i + 1])
                counts[pair] = counts.get(pair, 0) + 1
        if not counts:
            break
        best_pair = None
        best_count = -1
        for pair, count in counts.items():
            if count > best_count:
                best_pair = pair
                best_count = count
            elif count == best_count:
                left1 = bytes(token_bytes[pair[0]])
                right1 = bytes(token_bytes[pair[1]])
                left2 = bytes(token_bytes[best_pair[0]])
                right2 = bytes(token_bytes[best_pair[1]])
                if left1 > left2 or (left1 == left2 and right1 > right2):
                    best_pair = pair
        left, right = best_pair
        token_bytes[next_id] = token_bytes[left] + token_bytes[right]
        new_sequences = []
        for seq in sequences:
            merged = []
            i = 0
            while i < len(seq):
                if (
                    i + 1 < len(seq)
                    and seq[i] == left
                    and seq[i + 1] == right
                ):
                    merged.append(next_id)
                    i += 2
                else:
                    merged.append(seq[i])
                    i += 1
            new_sequences.append(merged)
        sequences = new_sequences
        merges.append([left, right, next_id])
        vocab.append([next_id, token_bytes[next_id]])
        next_id += 1
    return {
        "vocab": vocab,
        "merges": merges
    }