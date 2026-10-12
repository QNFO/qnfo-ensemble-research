import math
from fractions import Fraction
from math import gcd, log2, factorial

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: conjugation rescales shear coefficient c' = (lambda1/lambda2)*c
lam1, lam2, c = 2, 3, 1
c_prime = (lam1 / lam2) * c
expected_q1 = 2 / 3
results.append(("Q1", c_prime, expected_q1))

# Q2: ratio N_sed/N_oct
N_oct, N_sed = 7, 35
ratio = N_sed / N_oct
expected_q2 = 5
results.append(("Q2", ratio, expected_q2))

# Q3: g = log2(N_sed/N_oct)
g = log2(N_sed / N_oct)
expected_q3 = 2.321928
results.append(("Q3", g, expected_q3))

# Q4: Cayley-Dickson dimensions D_k = 2^k for k=3,4; growth factor
D3 = 2 ** 3
D4 = 2 ** 4
growth = D4 / D3
expected_q4 = 2
results.append(("Q4", growth, expected_q4))

# Q5: ring densities and density growth factor
delta_O = N_oct / D3
delta_S = N_sed / D4
density_factor = delta_S / delta_O
expected_q5 = 2.5
results.append(("Q5", density_factor, expected_q5))

# Q6: binomial identities 7 = C(7,1), 35 = C(7,3)
def binom(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
b1 = binom(7, 1)
b3 = binom(7, 3)
expected_q6 = 35  # check both; report combined as b3 with b1 checked too
ok_q6 = (b1 == 7) and (b3 == 35)
results.append(("Q6", 1 if ok_q6 else 0, 1))

# Q7: simplicial 2-cone faces F = C(2,0)+C(2,1)+C(2,2); extreme rays = 2
rho = 2
F = binom(rho, 0) + binom(rho, 1) + binom(rho, 2)
extreme = rho
expected_q7 = 4
results.append(("Q7", F, expected_q7))

# Q8: Euler totient phi(k) for k=2..6
def phi(k):
    return sum(1 for j in range(1, k + 1) if gcd(j, k) == 1)
phi_vals = {k: phi(k) for k in (2, 3, 4, 5, 6)}
expected_q8 = {2: 1, 3: 2, 4: 2, 5: 4, 6: 2}
ok_q8 = all(phi_vals[k] == expected_q8[k] for k in phi_vals)
results.append(("Q8", 1 if ok_q8 else 0, 1))

match_count = 0
for cid, computed, expected in results:
    if isinstance(expected, float):
        m = isclose(float(computed), expected)
    else:
        m = (computed == expected)
    if m:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if m else 'no'}")

total = len(results)
mismatch = total - match_count
print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {mismatch} mismatch")
