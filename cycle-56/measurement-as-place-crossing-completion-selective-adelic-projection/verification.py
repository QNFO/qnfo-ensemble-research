import math

def check(cid, computed, expected, tol=1e-6):
    if expected is None:
        match = None
    else:
        match = math.isclose(computed, expected, rel_tol=tol)
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: rate ratio
lam_ratio = 2.0
q1 = lam_ratio**2
check("Q1", q1, 4.0)

# Q2: Gamma_infty3
lam_inf = 1e-12
lam_3 = lam_inf / 2.0
N_b = 1e23
sigma2 = 1.0
q2 = 0.5 * (lam_inf**2 + lam_3**2) * N_b * sigma2
check("Q2", q2, 6.25e-2)

# Q3: T_x
q3 = 1.0 / q2
check("Q3", q3, 16.0)

# Q4: residual coherence at t = 5*T_x
t4 = 5 * q3
q4 = math.exp(-t4 / q3)
check("Q4", q4, math.exp(-5.0))

# Q5: Born-rule deviation at t = 80
a2, b2 = 0.6, 0.4
t5 = 80.0
q5 = math.sqrt(a2 * b2) * math.exp(-q2 * t5)
check("Q5", q5, 3.3009e-3)

# Q6: consistency bound
eps = 1.3e-2
worst = 0.5
q6 = math.log(worst / eps) / q2
check("Q6", q6, 58.41)

# Q7: physical-time projection
tau = 1e-13
q7 = q3 * tau
check("Q7", q7, 1.6e-12)

# Q8: full suppression time projection
q8 = q6 * tau
check("Q8", q8, 5.84e-12)

# summary
results = [q1, q2, q3, q4, q5, q6, q7, q8]
expected = [4.0, 6.25e-2, 16.0, math.exp(-5.0), 3.3009e-3, 58.41, 1.6e-12, 5.84e-12]
mism = sum(1 for c, e in zip(results, expected) if not math.isclose(c, e, rel_tol=1e-6))
print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results)-mism} match, {mism} mismatch")
