import math

eps0 = 1e-2
p = 2
L = 10
N = 1024
gamma = 1e-2

# Q1
P_U = eps0 * p ** (-L)
print(f"CLAIM Q1: computed={P_U:.12g} expected=9.765625e-06 match={'yes' if math.isclose(P_U, 9.765625e-6, rel_tol=1e-6) else 'no'}")

# Q2
P_A = eps0 * (1 - p ** (-(L + 1))) / (1 - p ** (-1))
print(f"CLAIM Q2: computed={P_A:.12g} expected=1.9990234375e-02 match={'yes' if math.isclose(P_A, 1.9990234375e-2, rel_tol=1e-6) else 'no'}")

# Q3
ratio = P_A / P_U
print(f"CLAIM Q3: computed={ratio:.12g} expected=2047 match={'yes' if math.isclose(ratio, 2047, rel_tol=1e-6) else 'no'}")

# Q4
eta_U = 1 - P_U
dU = 1 / (N * eta_U)
print(f"CLAIM Q4: computed={dU:.12g} expected=9.7657e-04 match={'yes' if math.isclose(dU, 9.7657e-4, rel_tol=1e-4) else 'no'}")

# Q5
eta_A = (1 - 2 * eps0) ** N
print(f"CLAIM Q5: computed={eta_A:.12g} expected=1.0364e-09 match={'yes' if math.isclose(eta_A, 1.0364e-9, rel_tol=1e-3) else 'no'}")

# Q6
dA = 1 / (N * eta_A)
print(f"CLAIM Q6: computed={dA:.12g} expected=9.4232e+05 match={'yes' if math.isclose(dA, 9.4232e5, rel_tol=1e-3) else 'no'}")

# Q7
r7 = eta_U / eta_A
print(f"CLAIM Q7: computed={r7:.12g} expected=9.6493e+08 match={'yes' if math.isclose(r7, 9.6493e8, rel_tol=1e-3) else 'no'}")

# Q8
dprod = math.e * gamma / math.sqrt(N)
print(f"CLAIM Q8: computed={dprod:.12g} expected=8.4946e-04 match={'yes' if math.isclose(dprod, 8.4946e-4, rel_tol=1e-3) else 'no'}")

results = [
    math.isclose(P_U, 9.765625e-6, rel_tol=1e-6),
    math.isclose(P_A, 1.9990234375e-2, rel_tol=1e-6),
    math.isclose(ratio, 2047, rel_tol=1e-6),
    math.isclose(dU, 9.7657e-4, rel_tol=1e-4),
    math.isclose(eta_A, 1.0364e-9, rel_tol=1e-3),
    math.isclose(dA, 9.4232e5, rel_tol=1e-3),
    math.isclose(r7, 9.6493e8, rel_tol=1e-3),
    math.isclose(dprod, 8.4946e-4, rel_tol=1e-3),
]
m = sum(results)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {m} match, {len(results) - m} mismatch")
