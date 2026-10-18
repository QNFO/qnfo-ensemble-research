# Verification script for quantitative claims in the paper

from fractions import Fraction

def round_sig(x, sig):
    """Round x to sig significant digits."""
    if x == 0:
        return 0.0
    return float(format(x, f".{sig}g"))

# Claim Q1
r_e = 2.81794e-15
lam_c = 3.86159e-13
alpha = r_e / lam_c
alpha_rounded = round_sig(alpha, 7)          # 7 significant digits (0.007297357)
expected_q1 = "0.007297357"
match_q1 = "yes" if abs(alpha_rounded - float(expected_q1)) < 1e-12 else "no"
print(f"CLAIM Q1: computed={alpha:.15g} expected={expected_q1} match={match_q1}")

# Claim Q2
A, B, C, D = 1, 2, 3, 4
cr = ((A - C) * (B - D)) / ((A - D) * (B - C))
expected_q2 = "4/3"
match_q2 = "yes" if Fraction(cr).limit_denominator() == Fraction(4, 3) else "no"
print(f"CLAIM Q2: computed={cr:.15g} expected={expected_q2} match={match_q2}")

# Claim Q3
imp1, imp2, imp3 = 22.94, 27.29, 27.65
sum_imp = imp1 + imp2 + imp3
sum_imp_rounded = round_sig(sum_imp, 4)      # 4 significant digits (77.88)
expected_q3 = "77.88"
match_q3 = "yes" if abs(sum_imp_rounded - float(expected_q3)) < 1e-9 else "no"
print(f"CLAIM Q3: computed={sum_imp:.15g} expected={expected_q3} match={match_q3}")

# Claim Q4
average_imp = sum_imp / 3
average_imp_rounded = round_sig(average_imp, 4)  # 4 significant digits (25.96)
expected_q4 = "25.96"
match_q4 = "yes" if abs(average_imp_rounded - float(expected_q4)) < 1e-9 else "no"
print(f"CLAIM Q4: computed={average_imp:.15g} expected={expected_q4} match={match_q4}")

# Claim Q5
baseline_TPR = 50.0
rel_imp = 0.2294
TPR_proj = baseline_TPR * (1 + rel_imp)
TPR_proj_rounded = round_sig(TPR_proj, 4)    # 4 significant digits (61.47)
expected_q5 = "61.47"
match_q5 = "yes" if abs(TPR_proj_rounded - float(expected_q5)) < 1e-9 else "no"
print(f"CLAIM Q5: computed={TPR_proj:.15g} expected={expected_q5} match={match_q5}")

# Claim Q6
gain = TPR_proj - baseline_TPR
gain_rounded = round_sig(gain, 4)            # 4 significant digits (11.47)
expected_q6 = "11.47"
match_q6 = "yes" if abs(gain_rounded - float(expected_q6)) < 1e-9 else "no"
print(f"CLAIM Q6: computed={gain:.15g} expected={expected_q6} match={match_q6}")

# Summary
matches = [match_q1, match_q2, match_q3, match_q4, match_q5, match_q6]
num_claims = len(matches)
num_match = matches.count("yes")
num_mismatch = num_claims - num_match
print(f"VERIFICATION SUMMARY: {num_claims} claims, {num_match} match, {num_mismatch} mismatch")
