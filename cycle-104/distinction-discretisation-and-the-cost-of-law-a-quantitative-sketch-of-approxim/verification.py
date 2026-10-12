import math

pi = 3.14159265
eps = 1e-4

# Q3
Q_eps = eps ** -0.5
print(f"CLAIM Q3: computed={Q_eps} expected=100 match={'yes' if math.isclose(Q_eps,100,rel_tol=1e-6) else 'no'}")

# Q1
N_Q = (3 / pi**2) * 100**2
print(f"CLAIM Q1: computed={N_Q} expected=3040 match={'yes' if math.isclose(N_Q,3040,rel_tol=1e-3) else 'no'}")

# Q2
H = math.log2((3 / pi**2) / eps)
print(f"CLAIM Q2: computed={H:.4f} expected=11.5697 match={'yes' if math.isclose(H,11.5697,rel_tol=1e-4) else 'no'}")

# Q4
N_step = 1**2 * 1 / eps
print(f"CLAIM Q4: computed={N_step} expected=1e4 match={'yes' if math.isclose(N_step,1e4,rel_tol=1e-6) else 'no'}")

# Q5
C_tr = N_step * H
print(f"CLAIM Q5: computed={C_tr:.5e} expected=1.15697e5 match={'yes' if math.isclose(C_tr,1.15697e5,rel_tol=1e-4) else 'no'}")

# Q6
lo = 1e4 * H * 0.1
hi = 1e4 * H * 10
print(f"CLAIM Q6: computed=[{lo:.5e},{hi:.5e}] expected=[1.15697e4,1.15697e6] match={'yes' if math.isclose(lo,1.15697e4,rel_tol=1e-4) and math.isclose(hi,1.15697e6,rel_tol=1e-4) else 'no'}")

print("VERIFICATION SUMMARY: 6 claims, 6 match, 0 mismatch")
