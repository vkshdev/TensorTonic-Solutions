import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here

    lam = float(lam)
    k = int(k)

    if lam <= 0 or k < 0:
        raise ValueError("lam must be > 0 and k >= 0")
    if k == 0:
        log_fact_k = 0.0
    else:
        log_fact_k = np.sum(np.log(np.arange(1, k+1)))

    log_pmf = -lam + k * np.log(lam) - log_fact_k
    pmf = np.exp(log_pmf)

    log_fact = np.cumsum(np.log(np.arange(1, k+1))) if k > 0 else np.array([])
    log_fact = np.insert(log_fact, 0, 0.0) 
    log_pmfs = -lam + np.arange(0, k+1) * np.log(lam) - log_fact
    pmfs = np.exp(log_pmfs)
    cdf = pmfs.sum()

    return float(pmf), float(cdf)
    pass