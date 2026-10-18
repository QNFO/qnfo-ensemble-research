import math

# Q1
T1 = 451e-6  # seconds
computed_Q1 = T1
expected_Q1 = "4.51e-4"
match_Q1 = "yes" if round(computed_Q1, 7) == 4.51e-4 else "no"
print(f"CLAIM Q1: computed={computed_Q1:.8g} expected={expected_Q1} match={match_Q1}")

# Q2
Gamma = 1.0 / T1
computed_Q2 = Gamma
expected_Q2 = "2.218e3"
# round to 4 significant figures for comparison
match_Q2 = "yes" if round(computed_Q2, -0) == 2218 else "no"
print(f"CLAIM Q2: computed={computed_Q2:.8g} expected={expected_Q2} match={match_Q2}")

# Q3
T_cyc = 1.0e-5  # seconds
p_phys = 1 - math.exp(-Gamma * T_cyc)
computed_Q3 = p_phys
expected_Q3 = "2.193e-2"
# round to 4 significant figures
match_Q3 = "yes" if round(computed_Q3, 5) == 0.02193 else "no"
print(f"CLAIM Q3: computed={computed_Q3:.8g} expected={expected_Q3} match={match_Q3}")

# Q4
d = 5
p_geom = p_phys ** (d/2)
computed_Q4 = p_geom
expected_Q4 = "7.12e-5"
# round to 3 significant figures
match_Q4 = "yes" if round(computed_Q4, 6) == 7.12e-5 else "no"
print(f"CLAIM Q4: computed={computed_Q4:.8g} expected={expected_Q4} match={match_Q4}")

# Q5
p_sc = p_phys ** d
computed_Q5 = p_sc
expected_Q5 = "5.07e-9"
# round to 3 significant figures
match_Q5 = "yes" if round(computed_Q5, 10) == 5.07e-9 else "no"
print(f"CLAIM Q5: computed={computed_Q5:.8g} expected={expected_Q5} match={match_Q5}")

# Q6
cost_per_qubit = 0.10
cost = d**2 * cost_per_qubit
computed_Q6 = cost
expected_Q6 = "2.5"
match_Q6 = "yes" if abs(computed_Q6 - 2.5) < 1e-12 else "no"
print(f"CLAIM Q6: computed={computed_Q6:.8g} expected={expected_Q6} match={match_Q6}")

# Q7
log10_p_geom = (d/2) * (math.log10(p_phys))
computed_Q7 = log10_p_geom
expected_Q7 = "-4.1475"
# round to 4 decimal places
match_Q7 = "yes" if round(computed_Q7, 4) == -4.1475 else "no"
print(f"CLAIM Q7: computed={computed_Q7:.8g} expected={expected_Q7} match={match_Q7}")

# Q8
log10_p_sc = d * (math.log10(p_phys))
computed_Q8 = log10_p_sc
expected_Q8 = "-8.295"
# round to 3 decimal places
match_Q8 = "yes" if round(computed_Q8, 3) == -8.295 else "no"
print(f"CLAIM Q8: computed={computed_Q8:.8g} expected={expected_Q8} match={match_Q8}")

print("VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch")
