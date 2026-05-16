import numpy as np 

def calibrate_isotonic(cal_labels, cal_probs, new_probs):
    cal_labels = np.asarray(cal_labels, dtype=float)
    cal_probs = np.asarray(cal_probs, dtype=float)
    new_probs = np.asarray(new_probs, dtype=float)

    order = np.argsort(cal_probs)
    x = cal_probs[order]
    y = cal_labels[order]

    stack = []
    for i in range(len(y)):
        s = y[i]
        w = 1.0
        idxs = [i]
        stack.append([s, w, idxs])
        while len(stack) >= 2 and (stack[-2][0] / stack[-2][1]) > (stack[-1][0] / stack[-1][1]):
            s2, w2, idx2 = stack.pop()
            s1, w1, idx1 = stack.pop()
            stack.append([s1 + s2, w1 + w2, idx1 + idx2])

    calibrated_vals = np.empty_like(y)
    for s, w, idxs in stack:
        mean = s / w
        for j in idxs:
            calibrated_vals[j] = mean

    xp = x
    fp = calibrated_vals
    if len(xp) == 0:
        return [0.0 for _ in new_probs]
    calibrated = np.interp(new_probs, xp, fp, left=fp[0], right=fp[-1])
    return [float(v) for v in calibrated]
    
    pass