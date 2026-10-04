import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1
omega_c = 2 * math.pi * 5e9
results.append(check("Q1", omega_c, 3.141592654e10))

# Q2
g = 0.01 * omega_c
results.append(check("Q2", g, 3.141592654e8))

# Q3
n_bar = 1e4
Omega = 2 * g * math.sqrt(n_bar)
results.append(check("Q3", Omega, 6.283185307e10))

# Q4
nu = Omega / (2 * math.pi)
results.append(check("Q4", nu, 1.0e10))

# Q5
rel_unc = math.sqrt(0.10**2 + (0.5 * 0.10)**2)
results.append(check("Q5", rel_unc, 0.1118033988749895))

# Q6
delta_nu = rel_unc * 10.0
results.append(check("Q6", delta_nu, 1.118033988749895))

# Q7
amp_corr = 1 / (2 * math.sqrt(n_bar))
results.append(check("Q7", amp_corr, 0.005))

# Q8
fluct = 1 / math.sqrt(n_bar)
results.append(check("Q8", fluct, 0.01))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
