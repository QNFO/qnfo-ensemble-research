import math
from fractions import Fraction

def isclose(a, b, rel_tol=1e-6):
    return math.isclose(a, b, rel_tol=rel_tol)

results = []

# Q1: H_tail(g) = 12 * 0.85^g
H0 = 12.0
eps = 0.15
rho = 1 - eps
H5 = H0 * rho**5
H10 = H0 * rho**10
q1_ok = isclose(H5, 5.32446375) and isclose(H10, 2.36249285)
results.append(("Q1", H5, 5.32446375, q1_ok))
results.append(("Q1b", H10, 2.36249285, isclose(H10, 2.36249285)))

# Q2: g = ceil(ln(12)/ln(1/0.85))
g_star = math.ceil(math.log(12.0) / math.log(1.0 / 0.85))
q2_ok = (g_star == 16)
results.append(("Q2", g_star, 16, q2_ok))

# Q3: kappa* = eps * H0 / (beta*V0 * p_bridge), beta*V0 = 1
p_bridge = 1 - 0.972
kappa_star = eps * H0 / (1.0 * p_bridge)
q3_ok = isclose(kappa_star, 64.29, rel_tol=1e-4)
results.append(("Q3", kappa_star, 64.29, q3_ok))

# Q4: slope = 12/0.028; kappa*(0.05), kappa*(0.30)
slope = H0 / p_bridge
k05 = 0.05 * H0 / p_bridge
k30 = 0.30 * H0 / p_bridge
q4_ok = isclose(slope, 428.57, rel_tol=1e-4) and isclose(k05, 21.43, rel_tol=1e-4) and isclose(k30, 128.57, rel_tol=1e-4)
results.append(("Q4", slope, 428.57, q4_ok))
results.append(("Q4b", k05, 21.43, isclose(k05, 21.43, rel_tol=1e-4)))
results.append(("Q4c", k30, 128.57, isclose(k30, 128.57, rel_tol=1e-4)))

# Q5: re-anchoring m=5, r=1
m = 5
r = 1.0
H_bar = (H0 * r / m) * (1 - rho**m) / eps
H_end = H0 * rho**m
uplift = H_bar / H_end - 1
q5_ok = isclose(H_bar, 8.90, rel_tol=1e-3) and isclose(uplift, 0.671, rel_tol=1e-3)
results.append(("Q5", H_bar, 8.90, isclose(H_bar, 8.90, rel_tol=1e-3)))
results.append(("Q5b", uplift, 0.671, isclose(uplift, 0.671, rel_tol=1e-3)))

# Q6: 0.85^16
surv16 = rho**16
q6_ok = isclose(surv16, 0.0743, rel_tol=1e-3)
results.append(("Q6", surv16, 0.0743, q6_ok))

# Q7: secondary model
rho2 = 0.95
beta_c = 1.5
N0 = 10000
pi0 = 1e-6
gamma = 1
E0 = math.comb(N0, 2) * pi0
growth = (beta_c**2 * rho2**gamma)**10
E10 = E0 * growth
q7_ok = isclose(E0, 49.995, rel_tol=1e-6) and isclose(E10, 99524, rel_tol=1e-2)
results.append(("Q7", E0, 49.995, isclose(E0, 49.995, rel_tol=1e-6)))
results.append(("Q7b", E10, 99524, isclose(E10, 99524, rel_tol=1e-2)))

# Q8: p_bridge = 1 - 0.972
q8_ok = isclose(p_bridge, 0.028, rel_tol=1e-6)
results.append(("Q8", p_bridge, 0.028, q8_ok))

for cid, computed, expected, ok in results:
    print(f"CLAIM {cid}: computed={computed:.6g} expected={expected:.6g} match={'yes' if ok else 'no'}")

n = len(results)
m_ok = sum(1 for r_ in results if r_[3])
k = n - m_ok
print(f"VERIFICATION SUMMARY: {n} claims, {m_ok} match, {k} mismatch")
