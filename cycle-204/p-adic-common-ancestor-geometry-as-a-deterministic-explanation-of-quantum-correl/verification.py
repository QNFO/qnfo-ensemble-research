import math
from fractions import Fraction

def round_sig(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Q1: 3‑adic norm |12/5|_3
p = 3
num = 12
den = 5
r = 0
temp = num
while temp % p == 0:
    r += 1
    temp //= p
norm = Fraction(p, p**(r+1))  # p^{-r} = 1/p
computed_Q1 = norm
expected_Q1 = Fraction(1, 3)
match_Q1 = computed_Q1 == expected_Q1

# Q2: age of universe in seconds
years = 14e9
seconds_per_year = 365.25 * 24 * 3600  # 31,557,600
seconds = years * seconds_per_year
computed_Q2 = seconds
expected_Q2 = 4.41e17
# paper gives 3 significant figures
computed_Q2_3sf = round_sig(computed_Q2, 3)
match_Q2 = computed_Q2_3sf == expected_Q2

# Q3: probability P = 1/p for p=3
p = 3
computed_Q3 = Fraction(1, p)
expected_Q3 = Fraction(1, 3)
match_Q3 = computed_Q3 == expected_Q3

# Q4: maximal CHSH value S_max = 2*sqrt(2)
computed_Q4 = 2 * math.sqrt(2)
expected_Q4 = 2.828
# paper shows 4 significant digits (2.828)
computed_Q4_4sf = round_sig(computed_Q4, 4)
match_Q4 = computed_Q4_4sf == expected_Q4

# Q5: CHSH with scaling factor κ = sqrt(2)
kappa = math.sqrt(2)
angle = math.pi / (2 * kappa)
cos_val = math.cos(angle)  # ≈0.444
S = abs(cos_val - cos_val) + abs(cos_val + cos_val)  # = 2*cos_val
computed_Q5 = S
expected_Q5 = 0.888
# 3 significant figures
computed_Q5_3sf = round_sig(computed_Q5, 3)
match_Q5 = computed_Q5_3sf == expected_Q5

# Q6: scaling factor κ = sqrt(2)
computed_Q6 = math.sqrt(2)
expected_Q6 = 1.41421356
# compare to 8 decimal places
computed_Q6_8dp = round(computed_Q6, 8)
match_Q6 = computed_Q6_8dp == expected_Q6

# Q7: statistical uncertainty 1/sqrt(N) for N=1e6
N = 1_000_000
computed_Q7 = 1 / math.sqrt(N)
expected_Q7 = 0.001
# compare directly
match_Q7 = abs(computed_Q7 - expected_Q7) < 1e-12

# Q8: seconds in one year
computed_Q8 = int(seconds_per_year)
expected_Q8 = 31557600
match_Q8 = computed_Q8 == expected_Q8

# Print results
print(f"CLAIM Q1: computed={computed_Q1} expected={expected_Q1} match={'yes' if match_Q1 else 'no'}")
print(f"CLAIM Q2: computed={computed_Q2:.6e} expected={expected_Q2:.6e} match={'yes' if match_Q2 else 'no'}")
print(f"CLAIM Q3: computed={computed_Q3} expected={expected_Q3} match={'yes' if match_Q3 else 'no'}")
print(f"CLAIM Q4: computed={computed_Q4:.6f} expected={expected_Q4:.3f} match={'yes' if match_Q4 else 'no'}")
print(f"CLAIM Q5: computed={computed_Q5:.3f} expected={expected_Q5:.3f} match={'yes' if match_Q5 else 'no'}")
print(f"CLAIM Q6: computed={computed_Q6_8dp:.8f} expected={expected_Q6:.8f} match={'yes' if match_Q6 else 'no'}")
print(f"CLAIM Q7: computed={computed_Q7:.3f} expected={expected_Q7:.3f} match={'yes' if match_Q7 else 'no'}")
print(f"CLAIM Q8: computed={computed_Q8} expected={expected_Q8} match={'yes' if match_Q8 else 'no'}")
print(f"VERIFICATION SUMMARY: 8 claims, {sum([match_Q1, match_Q2, match_Q3, match_Q4, match_Q5, match_Q6, match_Q7, match_Q8])} match, {8 - sum([match_Q1, match_Q2, match_Q3, match_Q4, match_Q5, match_Q6, match_Q7, match_Q8])} mismatch")
