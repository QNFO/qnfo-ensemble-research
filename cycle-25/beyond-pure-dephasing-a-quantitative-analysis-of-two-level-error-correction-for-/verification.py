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
T2 = 100e-6
gamma_phi = 1 / T2
results.append(check("Q1", gamma_phi, 1e4))

# Q2
T1 = 10e-3
gamma_1 = 1 / T1
results.append(check("Q2", gamma_1, 1e2))

# Q3
R = gamma_phi / gamma_1
results.append(check("Q3", R, 100))

# Q4
S = 100
gamma_phi_p = gamma_phi / S
results.append(check("Q4", gamma_phi_p, 1e2))

# Q5
tau = 1e-6
p1 = gamma_1 * tau
results.append(check("Q5", p1, 1e-4))

# Q6
p_Z = gamma_phi_p * tau
results.append(check("Q6", p_Z, 1e-4))

# Q7
pLX = 3 * p1**2 * (1 - p1) + p1**3
results.append(check("Q7", pLX, 2.9998e-8))

# Q8
pLZ = 1 - (1 - p_Z)**3
results.append(check("Q8", pLZ, 2.9997e-4))

print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(results)} match, {len(results)-sum(results)} mismatch")
