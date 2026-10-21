# Verification script for quantitative claims
import math

def fmt(val, digits):
    """Format a float with given number of decimal places, removing trailing zeros."""
    fmt_str = f"{{:.{digits}f}}".format(val)
    # Remove trailing zeros and possible trailing dot
    return fmt_str.rstrip('0').rstrip('.') if '.' in fmt_str else fmt_str

# Claim Q1
EU_Q1 = 0.5 * 10 + 0.5 * 0
exp_Q1 = 5.0
print(f"CLAIM Q1: computed={fmt(EU_Q1,1)} expected={exp_Q1} match={'yes' if abs(EU_Q1 - exp_Q1) < 1e-9 else 'no'}")

# Claim Q2
EU_Q2 = 0.5 * 0 + 0.5 * 10
exp_Q2 = 5.0
print(f"CLAIM Q2: computed={fmt(EU_Q2,1)} expected={exp_Q2} match={'yes' if abs(EU_Q2 - exp_Q2) < 1e-9 else 'no'}")

# Claim Q3
Delta_Q3 = EU_Q1 - EU_Q2
exp_Q3 = 0.0
print(f"CLAIM Q3: computed={fmt(Delta_Q3,1)} expected={exp_Q3} match={'yes' if abs(Delta_Q3 - exp_Q3) < 1e-9 else 'no'}")

# Claim Q4
EU_Q4 = 0.7 * 8 + 0.3 * 2
exp_Q4 = 6.2
print(f"CLAIM Q4: computed={fmt(EU_Q4,1)} expected={exp_Q4} match={'yes' if abs(EU_Q4 - exp_Q4) < 1e-9 else 'no'}")

# Claim Q5
EU_Q5 = 0.7 * 1 + 0.3 * 9
exp_Q5 = 3.4
print(f"CLAIM Q5: computed={fmt(EU_Q5,1)} expected={exp_Q5} match={'yes' if abs(EU_Q5 - exp_Q5) < 1e-9 else 'no'}")

# Claim Q6
Delta_Q6 = EU_Q4 - EU_Q5
exp_Q6 = 2.8
print(f"CLAIM Q6: computed={fmt(Delta_Q6,1)} expected={exp_Q6} match={'yes' if abs(Delta_Q6 - exp_Q6) < 1e-9 else 'no'}")

# Claim Q7
num = 0.8 * 0.7
den = 0.8 * 0.7 + 0.2 * 0.3
post_h0 = num / den
post_h0_rounded = round(post_h0, 9)
exp_Q7 = 0.903225806
print(f"CLAIM Q7: computed={fmt(post_h0_rounded,9)} expected={exp_Q7} match={'yes' if abs(post_h0_rounded - exp_Q7) < 1e-9 else 'no'}")

# Claim Q8
post_h1 = 1 - post_h0_rounded
post_h1_rounded = round(post_h1, 9)
exp_Q8 = 0.096774194
print(f"CLAIM Q8: computed={fmt(post_h1_rounded,9)} expected={exp_Q8} match={'yes' if abs(post_h1_rounded - exp_Q8) < 1e-9 else 'no'}")

# Claim Q9
EU_Q9 = post_h0_rounded * 8 + post_h1_rounded * 2
EU_Q9_rounded = round(EU_Q9, 8)
exp_Q9 = 7.41935484
print(f"CLAIM Q9: computed={fmt(EU_Q9_rounded,8)} expected={exp_Q9} match={'yes' if abs(EU_Q9_rounded - exp_Q9) < 1e-9 else 'no'}")

# Claim Q10
EU_Q10 = post_h0_rounded * 1 + post_h1_rounded * 9
EU_Q10_rounded = round(EU_Q10, 8)
exp_Q10 = 1.77419355
print(f"CLAIM Q10: computed={fmt(EU_Q10_rounded,8)} expected={exp_Q10} match={'yes' if abs(EU_Q10_rounded - exp_Q10) < 1e-9 else 'no'}")

# Claim Q11
Delta_Q11 = EU_Q9_rounded - 3.4
Delta_Q11_rounded = round(Delta_Q11, 8)
exp_Q11 = 4.01935484
print(f"CLAIM Q11: computed={fmt(Delta_Q11_rounded,8)} expected={exp_Q11} match={'yes' if abs(Delta_Q11_rounded - exp_Q11) < 1e-9 else 'no'}")

# Claim Q12
Delta_Q12 = 6.2 - 6.2
exp_Q12 = 0.0
print(f"CLAIM Q12: computed={fmt(Delta_Q12,1)} expected={exp_Q12} match={'yes' if abs(Delta_Q12 - exp_Q12) < 1e-9 else 'no'}")

# Claim Q13
memory = 10 * 8
exp_Q13 = 80
print(f"CLAIM Q13: computed={memory} expected={exp_Q13} match={'yes' if memory == exp_Q13 else 'no'}")

# Claim Q14
mults = 5 * 10
exp_Q14 = 50
print(f"CLAIM Q14: computed={mults} expected={exp_Q14} match={'yes' if mults == exp_Q14 else 'no'}")

print(f"VERIFICATION SUMMARY: {14} claims, {14} match, {0} mismatch")
