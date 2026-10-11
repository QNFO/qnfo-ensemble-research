import math
from fractions import Fraction

def check(cid, computed, expected):
    if expected is None:
        match = "n/a"
    else:
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match

results = []

# Q1: gamma_1 = 1/sqrt(1 - 0.8^2)
beta1 = 0.8
g1 = 1.0 / math.sqrt(1.0 - beta1**2)
results.append(check("Q1", g1, 5.0/3.0))

# Q2: D+ = 1/(gamma_1*(1 - beta_1))
Dp = 1.0 / (g1 * (1.0 - beta1))
results.append(check("Q2", Dp, 3.0))

# Q3: D- = 1/(gamma_1*(1 + beta_1))
Dm = 1.0 / (g1 * (1.0 + beta1))
results.append(check("Q3", Dm, 1.0/3.0))

# Q4: D_perp = 1/gamma_1
Dperp = 1.0 / g1
results.append(check("Q4", Dperp, 0.6))

# Q5: T_cool = T_0/gamma_1 (in units of T_0)
Tcool = 1.0 / g1
results.append(check("Q5", Tcool, 0.6))

# Q6: T_hot = gamma_1*T_0 (in units of T_0)
Thot = g1
results.append(check("Q6", Thot, 1.666667))

# Q7: gamma_1^2 = 25/9
g1sq = g1**2
results.append(check("Q7", g1sq, 25.0/9.0))

# Q8: beta = 0.6: gamma = 1/sqrt(1-0.36); T' = 300/gamma
b = 0.6
g = 1.0 / math.sqrt(1.0 - b**2)
T0 = 300.0
Tp = T0 / g
results.append(check("Q8a", g, 1.25))
results.append(check("Q8b", Tp, 240.0))

n = len(results)
m = sum(1 for r in results if r == "yes")
k = sum(1 for r in results if r == "no")
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")
