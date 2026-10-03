import math
from fractions import Fraction

results = []

def report(cid, computed, expected, is_float=True):
    if expected is None:
        match = "no"
    elif is_float:
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    results.append(match == "yes")

# Q1: topological regime |mu| < 2 t zeta(alpha), alpha > 1
alpha1 = 3.0
t1 = 1.0
mu1 = 0.1
zeta3 = 1.2020569
bound = 2 * t1 * zeta3
computed_q1 = abs(mu1) < bound
report("Q1", computed_q1, True, is_float=False)

# Q2: braid unitary U = cos(pi/4) 1 + sin(pi/4) gamma_i gamma_j = (1/sqrt2)(1 + gamma_i gamma_j)
theta = math.pi / 4
c, s = math.cos(theta), math.sin(theta)
computed_q2 = math.isclose(c, 1 / math.sqrt(2), rel_tol=1e-6) and math.isclose(s, 1 / math.sqrt(2), rel_tol=1e-6)
report("Q2", computed_q2, True, is_float=False)

# Q3: U^4 = exp(i*pi*sigma_3) = diag(e^{i pi}, e^{-i pi}) = -1
U4_00 = complex(math.cos(math.pi), math.sin(math.pi))   # e^{i pi}
U4_11 = complex(math.cos(-math.pi), math.sin(-math.pi)) # e^{-i pi}
computed_q3 = math.isclose(U4_00, -1, rel_tol=1e-6) and math.isclose(U4_11, -1, rel_tol=1e-6)
report("Q3", computed_q3, True, is_float=False)

# Q4: phi_Ising = pi/8 with pi = 3.14159
pi_input = 3.14159
phi = pi_input / 8
report("Q4", phi, 0.3927)

# Q5: lambda = (mu/t0)/(2*zeta(alpha)) at alpha=3, mu/t0=0.1
lam = 0.1 / (2 * zeta3)
report("Q5", lam, 0.0416)

# Q6: xi = 1/|ln(lambda)|
xi = 1 / abs(math.log(lam))
report("Q6", xi, 0.3145)

# Q7: epsilon = lambda^s * s^{-alpha}, s=10, alpha=3
s_sep = 10
eps = (lam ** s_sep) * (s_sep ** (-alpha1))
report("Q7", eps, 1.46e-17)

# Q8: cumulative drift <= 2*pi*epsilon*N_pairs, N_pairs = 1e6
N_pairs = 1e6
drift = 2 * math.pi * eps * N_pairs
report("Q8", drift, 9.2e-11)

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
