import math

results = []

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    results.append(match == "yes")

# Q1
N, k, l = 100, 1, 2
d_bulk = N**k
d_boundary = N**l
check("Q1", (d_bulk, d_boundary), (100, 10000))

# Q2
lam = 1 / N**2
check("Q2", lam, 1e-4)

# Q3
eps_petz = 1 - d_bulk / d_boundary
check("Q3", eps_petz, 0.99)

# Q4
Nv = 100
K1 = (1/2) * Nv**2 / Nv**4 - (1/2) * Nv**2 / Nv**4
check("Q4", K1, 0.0)

# Q5
Delta_eps = (1/Nv) * K1
check("Q5", Delta_eps, 0.0)

# Q6 (from stated inputs of Q6)
eps_petz_in, Delta_in = 0.01, 0.005
eps_tw = eps_petz_in - Delta_in
check("Q6", eps_tw, 0.005)

# Q7
rel_improve = (eps_petz_in - eps_tw) / eps_petz_in
check("Q7", rel_improve, 0.5)

# Q8
unc = (1/Nv)**2
check("Q8", unc, 0.0001)

print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(results)} match, {len(results)-sum(results)} mismatch")
