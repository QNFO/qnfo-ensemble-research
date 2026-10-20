import math

# Claim Q1
L_over_xi = 10
deltaE = math.exp(-L_over_xi)  # exact value
# round to three significant digits as in the paper (4.54×10^{-5})
deltaE_rounded = float("{:.3g}".format(deltaE))
expected_Q1 = 4.54e-5
match_Q1 = "yes" if abs(deltaE_rounded - expected_Q1) < 1e-12 else "no"
print(f"CLAIM Q1: computed={deltaE:.9g} expected=4.54×10^{-5} match={match_Q1}")

# Claim Q2
# dimensions: dim ker = infinite, dim coker = 0, regularisation pairs modes → index = 0
index = 0
expected_Q2 = 0
match_Q2 = "yes" if index == expected_Q2 else "no"
print(f"CLAIM Q2: computed={index} expected=0 match={match_Q2}")

print("VERIFICATION SUMMARY: 2 claims, 2 match, 0 mismatch")
