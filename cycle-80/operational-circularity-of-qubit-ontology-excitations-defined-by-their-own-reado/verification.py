import math

def check(cid, computed, expected, tol=1e-6):
    if expected is None:
        match = None
    else:
        match = math.isclose(computed, expected, rel_tol=tol)
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match

results = []

# Q1: p_e = 1 - F, F = 0.99991
F = 0.99991
p_e = 1 - F
results.append(check("Q1", p_e, 9e-5))

# Q2: N_err = p_e * N_trials, N_trials = 1e6
N_trials = 1e6
N_err = p_e * N_trials
results.append(check("Q2", N_err, 90))

# Q3: sqrt(N_err)
sqrt_err = math.sqrt(N_err)
results.append(check("Q3", sqrt_err, 9.49))

# Q4: sigma_p = sqrt(p*(1-p)/N), p=0.5, N=1e4
p = 0.5
N = 1e4
sigma_p = math.sqrt(p * (1 - p) / N)
results.append(check("Q4", sigma_p, 5.00e-3))

# Q5: sigma_p / p_e
ratio = sigma_p / p_e
results.append(check("Q5", ratio, 55.6))

# Q6: N_cross = p*(1-p)/p_e^2
N_cross = p * (1 - p) / p_e**2
results.append(check("Q6", N_cross, 3.09e7))

# Q7: n = ceil(ln(eps/d0)/ln(L)), L=0.6, d0=1, eps=1e-3
L = 0.6
d0 = 1.0
eps = 1e-3
n_raw = math.log(eps / d0) / math.log(L)
n = math.ceil(n_raw)
results.append(check("Q7", n, 14))

# Q8: L**14 and L**13
L14 = L**14
L13 = L**13
results.append(check("Q8a", L14, 7.836e-4))
results.append(check("Q8b", L13, 1.306e-3))

matched = sum(1 for m in results if m is True)
mismatched = sum(1 for m in results if m is False)
total = len(results)
print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {mismatched} mismatch")
