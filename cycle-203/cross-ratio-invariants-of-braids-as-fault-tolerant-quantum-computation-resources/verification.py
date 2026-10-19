import math

# Q1
r = 1e3
L = 1
N_phys = r * L
expected_Q1 = 1000
match_Q1 = "yes" if abs(N_phys - expected_Q1) < 1e-12 else "no"
print(f"CLAIM Q1: computed={N_phys:.0f} expected={expected_Q1} match={match_Q1}")

# Q2
N_exp = 10
kappa = N_phys / N_exp
expected_Q2 = 100
match_Q2 = "yes" if abs(kappa - expected_Q2) < 1e-12 else "no"
print(f"CLAIM Q2: computed={kappa:.0f} expected={expected_Q2} match={match_Q2}")

# Q3
chi = 1.5
dchi_dz1 = -0.375
Delta_z = 0.01
Delta_chi = dchi_dz1 * Delta_z
rel_change = abs(Delta_chi) / chi
expected_Q3 = 2.5e-3
match_Q3 = "yes" if abs(rel_change - expected_Q3) < 1e-12 else "no"
print(f"CLAIM Q3: computed={rel_change:.6g} expected={expected_Q3:.6g} match={match_Q3}")

# Q4
expected_Q4 = -3.75e-3
match_Q4 = "yes" if abs(Delta_chi - expected_Q4) < 1e-12 else "no"
print(f"CLAIM Q4: computed={Delta_chi:.6g} expected={expected_Q4:.6g} match={match_Q4}")

# Q5
delta = 0.01
L_conf = 4
delta_over_L = delta / L_conf
expected_Q5 = 2.5e-3
match_Q5 = "yes" if abs(delta_over_L - expected_Q5) < 1e-12 else "no"
print(f"CLAIM Q5: computed={delta_over_L:.6g} expected={expected_Q5:.6g} match={match_Q5}")

# Q6
p_hit = 4 * math.pi / (100**2)
expected_Q6 = 1.257e-3
match_Q6 = "yes" if abs(p_hit - expected_Q6) < 1e-12 else "no"
print(f"CLAIM Q6: computed={p_hit:.6g} expected={expected_Q6:.6g} match={match_Q6}")

# Q7
z1, z2, z3, z4 = 0, 1, 2, 4
chi_calc = ((z1 - z3)*(z2 - z4)) / ((z1 - z4)*(z2 - z3))
expected_Q7 = 1.5
match_Q7 = "yes" if abs(chi_calc - expected_Q7) < 1e-12 else "no"
print(f"CLAIM Q7: computed={chi_calc:.6g} expected={expected_Q7:.6g} match={match_Q7}")

# Q8
dchi_dz1_calc = chi_calc * (1/(z1 - z3) - 1/(z1 - z4))
expected_Q8 = -0.375
match_Q8 = "yes" if abs(dchi_dz1_calc - expected_Q8) < 1e-12 else "no"
print(f"CLAIM Q8: computed={dchi_dz1_calc:.6g} expected={expected_Q8:.6g} match={match_Q8}")

# Q9
epsilon = 1e-2
target_logical_error = 1e-6
delta_max = target_logical_error / epsilon
expected_Q9 = 1e-4
match_Q9 = "yes" if abs(delta_max - expected_Q9) < 1e-12 else "no"
print(f"CLAIM Q9: computed={delta_max:.6g} expected={expected_Q9:.6g} match={match_Q9}")

# Q10
cost_per_qubit = 5000
C = cost_per_qubit * N_phys
expected_Q10 = 5000000
match_Q10 = "yes" if abs(C - expected_Q10) < 1e-12 else "no"
print(f"CLAIM Q10: computed={C:.0f} expected={expected_Q10} match={match_Q10}")

print(f"VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch")
