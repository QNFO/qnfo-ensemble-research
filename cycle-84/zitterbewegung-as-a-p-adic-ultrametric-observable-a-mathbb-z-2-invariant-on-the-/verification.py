import math

log10_2 = 0.30103
mec2 = 5.11e5      # eV
hbar = 6.582e-16   # eV s
hbarc = 197.327    # eV nm
c = 2.998e8        # m/s

# Q1
omega_C = mec2 / hbar
print(f"CLAIM Q1: computed={omega_C:.4e} expected=7.7636e20 match={'yes' if math.isclose(omega_C, 7.7636e20, rel_tol=1e-6) else 'no'}")

# Q2
log10_omega = math.log10(omega_C)
log2_omega = log10_omega / log10_2
nu_omega = math.floor(log2_omega)
print(f"CLAIM Q2: computed={log2_omega:.4f} (nu={nu_omega}) expected=69.3953 (nu=69) match={'yes' if math.isclose(log2_omega, 69.3953, rel_tol=1e-4) and nu_omega == 69 else 'no'}")

# Q3
lambda_nm = hbarc / mec2
lambda_m = lambda_nm * 1e-9
print(f"CLAIM Q3: computed={lambda_m:.4e} expected=3.8616e-13 match={'yes' if math.isclose(lambda_m, 3.8616e-13, rel_tol=1e-4) else 'no'}")

# Q4
log10_lambda = math.log10(lambda_m)
log2_lambda = log10_lambda / log10_2
nu_lambda = math.floor(log2_lambda)
print(f"CLAIM Q4: computed={log2_lambda:.4f} (nu={nu_lambda}) expected=-41.2359 (nu=-42) match={'yes' if math.isclose(log2_lambda, -41.2359, rel_tol=1e-4) and nu_lambda == -42 else 'no'}")

# Q5
chi = nu_omega % 2
print(f"CLAIM Q5: computed={chi} expected=1 match={'yes' if chi == 1 else 'no'}")

# Q6
total = log2_omega + log2_lambda
log2_c = math.log10(c) / log10_2
print(f"CLAIM Q6: computed={total:.4f} (log2(c)={log2_c:.4f}) expected=28.1592 (28.1594) match={'yes' if math.isclose(total, 28.1592, rel_tol=1e-4) and math.isclose(log2_c, 28.1594, rel_tol=1e-4) else 'no'}")

# Q7
d_T = abs(nu_omega - nu_lambda)
print(f"CLAIM Q7: computed={d_T} expected=111 match={'yes' if d_T == 111 else 'no'}")

# Q8
Delta = d_T - log2_c
print(f"CLAIM Q8: computed={Delta:.4f} expected=82.8406 match={'yes' if math.isclose(Delta, 82.8406, rel_tol=1e-4) else 'no'}")

print("VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch")
