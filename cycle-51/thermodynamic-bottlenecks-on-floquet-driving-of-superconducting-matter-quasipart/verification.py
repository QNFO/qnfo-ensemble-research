import math

kB = 1.380649e-23
h = 6.62607015e-34
e = 1.602176634e-19

# Q1
Delta0 = 1.76 * kB * 1.2
print(f"CLAIM Q1: computed={Delta0:.6e} expected=2.91593e-23 match={math.isclose(Delta0, 2.91593e-23, rel_tol=1e-6)}")

# Q2
f_pb = 2 * Delta0 / h
print(f"CLAIM Q2: computed={f_pb:.6e} expected=8.8e10 match={math.isclose(f_pb, 8.8e10, rel_tol=1e-2)}")

# Q3
eps_tol = 1e-3
tau_g = 1e-7
P_abs_max = (eps_tol / tau_g) * 2 * Delta0
print(f"CLAIM Q3: computed={P_abs_max:.6e} expected=5.8e-19 match={math.isclose(P_abs_max, 5.8e-19, rel_tol=1e-2)}")

# Q4
P_abs = 1e-12
Gamma_qp = P_abs / (2 * Delta0)
print(f"CLAIM Q4: computed={Gamma_qp:.6e} expected=1.72e10 match={math.isclose(Gamma_qp, 1.72e10, rel_tol=1e-2)}")

# Q5
tau_qp = 3e-4
V_c = 5e-5
n_ss = Gamma_qp * tau_qp / V_c
print(f"CLAIM Q5: computed={n_ss:.6e} expected=1.0e11 match={math.isclose(n_ss, 1.0e11, rel_tol=1e-2)}")

# Q6
N0 = 1.72e10
T = 0.1
n_th = 2 * N0 * math.sqrt(2 * math.pi * Delta0 * kB * T) * math.exp(-Delta0 / (kB * T))
print(f"CLAIM Q6: computed={n_th:.6e} expected=1.2e-21 match={math.isclose(n_th, 1.2e-21, rel_tol=1e-2)}")

# Q7
ratio = n_ss / n_th
print(f"CLAIM Q7: computed={ratio:.6e} expected=9e31 match={math.isclose(ratio, 9e31, rel_tol=1e-1)}")

# Q8
P_alloc = 1e-6
sigma = 1e-4
A = 1e-4
E_max = math.sqrt(2 * P_alloc / (sigma * A))
print(f"CLAIM Q8: computed={E_max:.6e} expected=14.1 match={math.isclose(E_max, 14.1, rel_tol=1e-2)}")

results = [
    math.isclose(Delta0, 2.91593e-23, rel_tol=1e-6),
    math.isclose(f_pb, 8.8e10, rel_tol=1e-2),
    math.isclose(P_abs_max, 5.8e-19, rel_tol=1e-2),
    math.isclose(Gamma_qp, 1.72e10, rel_tol=1e-2),
    math.isclose(n_ss, 1.0e11, rel_tol=1e-2),
    math.isclose(n_th, 1.2e-21, rel_tol=1e-2),
    math.isclose(ratio, 9e31, rel_tol=1e-1),
    math.isclose(E_max, 14.1, rel_tol=1e-2),
]
m = sum(results)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {m} match, {len(results)-m} mismatch")
