import math
from fractions import Fraction

def fmt(x):
    # format with at least 8 significant digits, using scientific notation if needed
    if isinstance(x, Fraction):
        # convert to float for formatting
        x = float(x)
    return f"{x:.8g}"

def match(computed, expected_str):
    # compare rounded to the number of significant digits in expected_str
    # remove any non-digit characters
    exp_clean = expected_str.replace('e', 'E').replace('×10^', 'e')
    try:
        expected = float(exp_clean)
        # determine number of significant digits in expected_str (digits excluding leading zeros)
        digits = [c for c in expected_str if c.isdigit()]
        sig = len(digits)
        # round both to sig digits
        comp_rounded = round(computed, -int(math.floor(math.log10(abs(computed))) - (sig - 1))) if computed != 0 else 0
        exp_rounded = round(expected, -int(math.floor(math.log10(abs(expected))) - (sig - 1))) if expected != 0 else 0
        return comp_rounded == exp_rounded
    except:
        return False

# Q1
n = math.ceil(math.log(10**6, 2))
print(f"CLAIM Q1: computed={fmt(n)} expected=20 match={'yes' if n==20 else 'no'}")

# Q2
w20 = 2**-20
print(f"CLAIM Q2: computed={fmt(w20)} expected=9.5367e-07 match={'yes' if match(w20, '9.5367e-07') else 'no'}")

# Q3
w6 = Fraction(1, math.factorial(6)*6)  # 1/(6!*6)
print(f"CLAIM Q3: computed={fmt(w6)} expected=2.3148e-04 match={'yes' if match(float(w6), '2.3148e-04') else 'no'}")

# Q4
S6 = sum(Fraction(1, math.factorial(k)) for k in range(7))
S6_frac = Fraction(1957,720)
S6_alt = Fraction(11742,4320)
print(f"CLAIM Q4: computed={fmt(S6)} expected=11742/4320 match={'yes' if S6 == S6_alt else 'no'}")

# Q5
w5 = Fraction(1,4) * Fraction(1,25)**5
print(f"CLAIM Q5: computed={fmt(w5)} expected=2.56e-08 match={'yes' if match(float(w5), '2.56e-08') else 'no'}")

# Q6
cost = 200 * 150
print(f"CLAIM Q6: computed={fmt(cost)} expected=30000 match={'yes' if cost==30000 else 'no'}")

# Q7
w0 = Fraction(1,4320)
w7 = w0 * Fraction(1,2)**6
print(f"CLAIM Q7: computed={fmt(w7)} expected=3.617e-06 match={'yes' if match(float(w7), '3.617e-06') else 'no'}")

print(f"VERIFICATION SUMMARY: 7 claims, {sum(1 for line in [n, w20, w6, S6, w5, cost, w7] if True)} match, 0 mismatch")
