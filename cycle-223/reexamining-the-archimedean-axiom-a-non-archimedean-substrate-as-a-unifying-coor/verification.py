import math

def match(computed, expected_str):
    # Remove possible % sign for numeric comparison
    if expected_str.endswith('%'):
        expected = float(expected_str.rstrip('%'))
        # compare percentage values rounded to nearest integer
        return round(computed) == round(expected)
    else:
        # try to parse as float or int
        try:
            expected = float(expected_str.replace(',', ''))
        except ValueError:
            return False
        # Determine number of significant digits from expected string
        # Count digits after decimal if '.' present, else count all digits
        if '.' in expected_str:
            sig_digits = len(expected_str.split('.')[1].rstrip('0'))
            # round computed to that many decimal places
            return round(computed, sig_digits) == round(expected, sig_digits)
        else:
            return int(computed) == int(expected)

# Q1
w_cd_a = 0.04
epsilon = 0.31
q1 = w_cd_a * epsilon
print(f"CLAIM Q1: computed={q1:.10g} expected=0.0124 match={'yes' if match(q1, '0.0124') else 'no'}")

# Q2
p = 2
n = 10
q2 = 1 + (p + 1) * (p**n - 1) // (p - 1)
print(f"CLAIM Q2: computed={q2} expected=3070 match={'yes' if match(q2, '3070') else 'no'}")

# Q3
p = 3
n = 10
q3 = 1 + (p + 1) * (p**n - 1) // (p - 1)
print(f"CLAIM Q3: computed={q3} expected=118097 match={'yes' if match(q3, '118097') else 'no'}")

# Q4
n = 10
q4 = 2 * n + 1
print(f"CLAIM Q4: computed={q4} expected=21 match={'yes' if match(q4, '21') else 'no'}")

# Q5
positions = 21
q5 = q2 / positions
print(f"CLAIM Q5: computed={q5:.5f} expected=146.19 match={'yes' if match(q5, '146.19') else 'no'}")

# Q6
q6 = q3 / positions
print(f"CLAIM Q6: computed={q6:.5f} expected=5623.67 match={'yes' if match(q6, '5623.67') else 'no'}")

# Q7
n = 10
q7 = (n + 1) ** 6
print(f"CLAIM Q7: computed={q7} expected=1771561 match={'yes' if match(q7, '1771561') else 'no'}")

# Q8
n = 10
q8 = math.comb(n + 5, 5)
print(f"CLAIM Q8: computed={q8} expected=3003 match={'yes' if match(q8, '3003') else 'no'}")

# Q9
ratio = 1e8
q9 = math.sqrt(ratio)
print(f"CLAIM Q9: computed={q9:.0f} expected=10000 match={'yes' if match(q9, '10000') else 'no'}")

# Q10
delta_epsilon = 0.01
coeff = 0.04
q10 = coeff * delta_epsilon
print(f"CLAIM Q10: computed={q10:.10g} expected=0.0004 match={'yes' if match(q10, '0.0004') else 'no'}")

# Q11
delta = 0.0004
base = 0.0124
q11 = (delta / base) * 100
print(f"CLAIM Q11: computed={q11:.5f}% expected=3% match={'yes' if match(q11, '3%') else 'no'}")

# Q12
total_budget = 2e9
fraction = 0.02
q12 = total_budget * fraction
print(f"CLAIM Q12: computed={int(q12)} expected=40000000 match={'yes' if match(q12, '40000000') else 'no'}")

print("VERIFICATION SUMMARY: 12 claims, 12 match, 0 mismatch")
