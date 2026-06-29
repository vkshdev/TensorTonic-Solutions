import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    # Write code here
    
    if not docs:
        return np.array([], dtype=float)

    N = len(docs)
    doc_lens = np.array([len(d) for d in docs], dtype=float)
    avgdl = doc_lens.mean() if N > 0 else 0.0
    df = Counter()
    for d in docs:
        unique_terms = set(d)
        for t in unique_terms:
            df[t] += 1
    query_terms = list(dict.fromkeys(query_tokens))

    idf = {}
    for t in query_terms:
        if t in df:
            idf[t] = math.log((N - df[t] + 0.5) / (df[t] + 0.5) + 1)
        else:
            idf[t] = 0.0

    scores = np.zeros(N, dtype=float)
    for i, d in enumerate(docs):
        tf = Counter(d)
        for t in query_terms:
            if tf[t] == 0 or idf[t] == 0:
                continue
            numerator = tf[t] * (k1 + 1)
            denominator = tf[t] + k1 * (1 - b + b * doc_lens[i] / avgdl)
            scores[i] += idf[t] * numerator / denominator
    return scores
    pass