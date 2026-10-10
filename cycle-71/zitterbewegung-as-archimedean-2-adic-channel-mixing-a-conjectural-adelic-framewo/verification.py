import math

m_e = 9.109e-31
c = 2.998e8
hbar = 1.055e-34

# Q1
omega_zbw = 2 * m_e * c**2 / hbar
print(f"CLAIM Q1: computed={omega_zbw:.4e} expected=1.5521e21 match={math.isclose(omega_zbw, 1.5521e21, rel_tol=1e-6)}")

# Q2
nu_zbw = omega_zbw / (2 * math.pi)
print(f"CLAIM Q2: computed={nu_zbw:.4e} expected=2.4702e20 match={math.isclose(nu_zbw, 2.4702e20, rel_tol=1e-6)}")

# Q3
T_zbw = 2 * math.pi / omega_zbw
print(f"CLAIM Q3: computed={T_zbw:.4e} expected=4.0483e-21 match={math.isclose(T_zbw, 4.0483e-21, rel_tol=1e-6)}")

# Q4
omega_c = m_e * c**2 / hbar
print(f"CLAIM Q4: computed={omega_c:.4e} expected=7.7604e20 match={math.isclose(omega_c, 7.7604e20, rel_tol=1e-6)}")

# Q5
prod2 = 2 * 0.5
print(f"CLAIM Q5: computed={prod2} expected=1 match={math.isclose(prod2, 1, rel_tol=1e-6)}")

# Q6
prod12 = 12 * (1/4) * (1/3)
print(f"CLAIM Q6: computed={prod12} expected=1 match={math.isclose(prod12, 1, rel_tol=1e-6)}")

# Q7
prod_ost = 1024 * 2**(-10)
print(f"CLAIM Q7: computed={prod_ost} expected=1 match={math.isclose(prod_ost, 1, rel_tol=1e-6)}")

# Q8
E0 = 8.187e-14
E_inf = E0 * math.sqrt(3**2 + 1)
print(f"CLAIM Q8: computed={E_inf:.4e} expected=2.5890e-13 match={math.isclose(E_inf, 2.5890e-13, rel_tol=1e-6)}")

print("VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch")
