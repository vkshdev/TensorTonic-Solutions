import numpy as np
def _dot(a, b):
    """Dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))

def lbfgs_direction(grad, s_list, y_list):
    """
    Compute the L-BFGS search direction using the two-loop recursion.
    """
    # Write code here

    grad = np.asarray(grad, dtype=float)
    s_list = [np.asarray(s, dtype=float) for s in s_list]
    y_list = [np.asarray(y, dtype=float) for y in y_list]

    m = len(s_list)
    if m == 0:
        return (-grad).tolist()

    rho = [1.0 / np.dot(y_list[i], s_list[i]) for i in range(m)]

    q = grad.copy()
    alpha = []
    for i in reversed(range(m)):
        a_i = rho[i] * np.dot(s_list[i], q)
        alpha.append(a_i)
        q = q - a_i * y_list[i]
    alpha = alpha[::-1]

    y_last, s_last = y_list[-1], s_list[-1]
    gamma = np.dot(s_last, y_last) / np.dot(y_last, y_last)
    r = gamma * q

    for i in range(m):
        beta = rho[i] * np.dot(y_list[i], r)
        r = r + s_list[i] * (alpha[i] - beta)
    return (-r).tolist()
