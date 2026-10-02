import math
from fractions import Fraction

results = []

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    results.append(match == "yes")
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: fixed point of f(p)=3p^2-2p^3
# 3p^2-2p^3 = p -> p(2p^2-3p+1)=0 -> p=(3±1)/4
roots = [Fraction(3+s, 4) for s in (-1, 1)]
p_star = [r for r in roots if 0 < r < Fraction(1, 2)][0]
check("Q1", float(p_star), 0.25)

# Q2: depolarizing threshold
# (2/3)*p_dep < 1/4 => p_dep < 3/8
p_dep = Fraction(1, 4) * Fraction(3, 2)
check("Q2", float(p_dep), 0.375)

# Q3: p_2q = 1 - 0.9956
p_2q = 1 - 0.9956
check("Q3", p_2q, 4.4e-3)

# Q4: p_1q = 1 - 0.9990
p_1q = 1 - 0.9990
check("Q4", p_1q, 1.0e-3)

# Q5: p_ro = 1 - 0.987
p_ro = 1 - 0.987
check("Q5", p_ro, 1.3e-2)

# Q6: p_bf = e^{-2*nbar} at nbar=6
nbar = 6
p_bf = math.exp(-2 * nbar)
check("Q6", p_bf, 6.144e-6)

# Q7: p_eff = p_2q * p_bf
p_eff = p_2q * p_bf
check("Q7", p_eff, 2.703e-8)

# Q8: margin = threshold / p_eff
threshold = 1e-4
margin = threshold / p_eff
check("Q8", margin, 3.70e3)

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
