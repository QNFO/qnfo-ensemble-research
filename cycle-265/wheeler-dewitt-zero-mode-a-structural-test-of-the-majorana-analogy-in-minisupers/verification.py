import math

# Q1: Jackiw–Rebbi splitting ΔE = exp(-L/ξ) with L/ξ = 10
L_over_xi = 10
delta_E = math.exp(-L_over_xi)
expected_Q1 = "4.539992976e-05"
match_Q1 = "yes" if f"{delta_E:.12e}"[:13] == expected_Q1 else "no"
print(f"CLAIM Q1: computed={delta_E:.12e} expected={expected_Q1} match={match_Q1}")

# Q2: Dimensionless product F L
F_MeV = 93.0
conversion = 0.197  # fm per MeV^{-1}
F_fm_inv = F_MeV * conversion
L_fm = 2.0
FL = F_fm_inv * L_fm
expected_Q2 = "36.6"
# round to one decimal place as in claim
FL_rounded = round(FL, 1)
match_Q2 = "yes" if f"{FL_rounded:.1f}" == expected_Q2 else "no"
print(f"CLAIM Q2: computed={FL_rounded:.1f} expected={expected_Q2} match={match_Q2}")

# Q3: Thermal scale T = 1/β with β = 100 / t, t = 3.03 eV
t = 3.03
beta = 100.0 / t
T = 1.0 / beta
expected_Q3 = "0.0303"
# round to 4 decimal places as in claim
T_rounded = round(T, 4)
match_Q3 = "yes" if f"{T_rounded:.4f}" == expected_Q3 else "no"
print(f"CLAIM Q3: computed={T_rounded:.4f} expected={expected_Q3} match={match_Q3}")

# Q4: Leading finite-size correction (F L)^{-2} with F L ≈ 36.6
FL_approx = 36.6
correction = 1.0 / (FL_approx ** 2)
expected_Q4 = "7.5e-04"
# format in scientific notation with two significant digits
correction_formatted = f"{correction:.2e}"
match_Q4 = "yes" if correction_formatted == expected_Q4 else "no"
print(f"CLAIM Q4: computed={correction_formatted} expected={expected_Q4} match={match_Q4}")

print(f"VERIFICATION SUMMARY: 4 claims, {sum([match_Q1, match_Q2, match_Q3, match_Q4].count('yes'))} match, {sum([match_Q1, match_Q2, match_Q3, match_Q4].count('no'))} mismatch")
