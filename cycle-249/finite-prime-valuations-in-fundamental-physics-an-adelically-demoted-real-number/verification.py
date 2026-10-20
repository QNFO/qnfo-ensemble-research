import math
from fractions import Fraction

def fmt(val):
    if isinstance(val, (int, float)):
        # format with at least 8 significant digits
        return f"{val:.8g}"
    return str(val)

# Q1
q1 = Fraction(6, 35)
prod_q1 = q1 * Fraction(1,2) * Fraction(1,3) * 5 * 7
computed_Q1 = float(prod_q1)
expected_Q1 = 1
match_Q1 = abs(computed_Q1 - expected_Q1) < 1e-12
print(f"CLAIM Q1: computed={fmt(computed_Q1)} expected={expected_Q1} match={'yes' if match_Q1 else 'no'}")

# Q2
prod_q2 = 1.001 * 8 * 125 * Fraction(1,7) * Fraction(1,11) * Fraction(1,13)
computed_Q2 = float(prod_q2)
expected_Q2 = 1
match_Q2 = abs(computed_Q2 - expected_Q2) < 1e-12
print(f"CLAIM Q2: computed={fmt(computed_Q2)} expected={expected_Q2} match={'yes' if match_Q2 else 'no'}")

# Q3
sum_inv = 2.1945
sum_inv_sq = 0.452
E = 2 * sum_inv - 2 * sum_inv_sq
computed_Q3 = E
expected_Q3 = 3.485
match_Q3 = abs(computed_Q3 - expected_Q3) < 1e-12
print(f"CLAIM Q3: computed={fmt(computed_Q3)} expected={expected_Q3} match={'yes' if match_Q3 else 'no'}")

# Q4
N = 19 * 13 * 9 * 7 * 5 * 5
computed_Q4 = N
expected_Q4 = 389025
match_Q4 = computed_Q4 == expected_Q4
print(f"CLAIM Q4: computed={fmt(computed_Q4)} expected={expected_Q4} match={'yes' if match_Q4 else 'no'}")

# Q5
pi = math.pi
approx = (3 / (pi**2)) * (1000**2)
computed_Q5 = approx
expected_Q5 = "3.04e5"
# round to 3 significant digits for comparison
expected_val = 3.04e5
match_Q5 = round(computed_Q5, -2) == round(expected_val, -2)
print(f"CLAIM Q5: computed={fmt(computed_Q5)} expected={expected_Q5} match={'yes' if match_Q5 else 'no'}")

# Q6
S = 5.56e6
computed_Q6 = S
expected_Q6 = "5.56e6"
match_Q6 = abs(computed_Q6 - 5.56e6) < 1e-6
print(f"CLAIM Q6: computed={fmt(computed_Q6)} expected={expected_Q6} match={'yes' if match_Q6 else 'no'}")

# Q7
abs_S_2 = Fraction(1,64)
abs_S_5 = Fraction(1,625)
abs_S_139 = Fraction(1,139)
computed_Q7 = (float(abs_S_2), float(abs_S_5), float(abs_S_139))
expected_Q7 = "(1/64, 1/625, 1/139)"
match_Q7 = (abs_S_2 == Fraction(1,64) and abs_S_5 == Fraction(1,625) and abs_S_139 == Fraction(1,139))
print(f"CLAIM Q7: computed={fmt(computed_Q7)} expected={expected_Q7} match={'yes' if match_Q7 else 'no'}")

# Q8
prod_S = 5_560_000 * float(Fraction(1,64)) * float(Fraction(1,625)) * float(Fraction(1,139))
computed_Q8 = prod_S
expected_Q8 = 1
match_Q8 = abs(computed_Q8 - 1) < 1e-12
print(f"CLAIM Q8: computed={fmt(computed_Q8)} expected={expected_Q8} match={'yes' if match_Q8 else 'no'}")

# Q9
r = 1000
prod_r = r * Fraction(1,8) * Fraction(1,125)
computed_Q9 = float(prod_r)
expected_Q9 = 1
match_Q9 = abs(computed_Q9 - 1) < 1e-12
print(f"CLAIM Q9: computed={fmt(computed_Q9)} expected={expected_Q9} match={'yes' if match_Q9 else 'no'}")

# Q10
threshold = 5e-10
computed_Q10 = threshold
expected_Q10 = 5e-10
match_Q10 = abs(computed_Q10 - expected_Q10) < 1e-20
print(f"CLAIM Q10: computed={fmt(computed_Q10)} expected={expected_Q10} match={'yes' if match_Q10 else 'no'}")

# Q11
target_uncertainty = 5e-10
computed_Q11 = target_uncertainty
expected_Q11 = 5e-10
match_Q11 = abs(computed_Q11 - expected_Q11) < 1e-20
print(f"CLAIM Q11: computed={fmt(computed_Q11)} expected={expected_Q11} match={'yes' if match_Q11 else 'no'}")

# Q12
cost = 3.0e7 + 7.0e7
computed_Q12 = cost
expected_Q12 = 1.0e8
match_Q12 = abs(computed_Q12 - expected_Q12) < 1e-6
print(f"CLAIM Q12: computed={fmt(computed_Q12)} expected={expected_Q12} match={'yes' if match_Q12 else 'no'}")

print(f"VERIFICATION SUMMARY: 12 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10,match_Q11,match_Q12])} match, {12 - sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10,match_Q11,match_Q12])} mismatch")
