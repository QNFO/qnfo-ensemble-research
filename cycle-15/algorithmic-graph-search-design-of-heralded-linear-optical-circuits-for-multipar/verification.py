import math
from fractions import Fraction
from math import comb, isclose

results = []

def report(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        try:
            match = "yes" if isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
        except Exception:
            match = "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    results.append(match == "yes")

# Q1
m, k = 6, 3
pairs = comb(m, 2)
N_circ = pairs ** k
report("Q1", N_circ, 3375)

# Q2
N_circ_reorder = N_circ * math.factorial(k)
report("Q2", N_circ_reorder, 20250)

# Q3
N_graph = comb(pairs, k)
report("Q3", N_graph, 455)

# Q4
R = N_circ / N_graph
R2 = N_circ_reorder / N_graph
report("Q4", round(R, 4), 7.4176)
report("Q4", round(R2, 4), 44.5055)

# Q5
m2, k2 = 10, 5
pairs2 = comb(m2, 2)
N_circ2 = pairs2 ** k2
N_graph2 = comb(pairs2, k2)
R5 = N_circ2 / N_graph2
report("Q5", N_circ2, 184528125)
report("Q5", N_graph2, 1221759)
report("Q5", round(R5, 2), 151.03)

# Q6
for p, exp in [(0.1, 5e-3), (0.25, 3.125e-2), (0.5, 0.125)]:
    P = p**2 * Fraction(1, 2)
    report("Q6", float(P), exp)

# Q7
p, eta = 0.1, 0.9
P7 = p**2 * 0.5 * eta**2
report("Q7", P7, 4.05e-3)

# Q8
p, eta = 0.1, 1.0
P8 = p**4 * Fraction(1, 8) * eta**4
report("Q8", float(P8), 1.25e-5)

n = len(results)
m_ = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m_} match, {n - m_} mismatch")
