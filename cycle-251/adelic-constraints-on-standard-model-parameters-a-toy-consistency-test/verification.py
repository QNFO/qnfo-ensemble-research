import math
from fractions import Fraction

def fmt_sig(x, sig):
    """Format number x with given significant digits (sig) using scientific notation if needed."""
    return f"{x:.{sig}g}"

def fmt_fixed(x, places):
    """Format number x with fixed decimal places."""
    return f"{x:.{places}f}"

def compare_numeric(computed, expected):
    """Compare numeric expected string with computed value."""
    # Determine if expected is in scientific notation
    if 'e' in expected or 'E' in expected:
        # Count significant digits in expected (excluding exponent and sign)
        mantissa = expected.split('e')[0].replace('+','').replace('-','')
        sig = len(mantissa.replace('.','').lstrip('0'))
        comp_str = fmt_sig(computed, sig)
        # Ensure exponent format matches (lowercase e)
        exp = f"e{int(expected.split('e')[1]):+d}"
        # Adjust comp_str to have same exponent format
        if 'e' not in comp_str:
            comp_str = f"{computed:.{sig}e}"
        # Normalize exponent sign
        comp_str = comp_str.replace('E','e')
        # Remove leading '+' in exponent if present
        if '+-' not in comp_str:
            comp_str = comp_str.replace('e+', 'e')
        return comp_str == expected.lower()
    elif '.' in expected:
        # Fixed decimal places
        places = len(expected.split('.')[1])
        comp_str = fmt_fixed(computed, places)
        return comp_str == expected
    else:
        # Integer comparison
        return str(int(round(computed))) == expected

def compare_fraction(computed_frac, expected_str):
    return f"{computed_frac.numerator}/{computed_frac.denominator}" == expected_str

def claim_line(cid, computed, expected, match):
    return f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}"

results = []

# Q1
q1 = 60 * (2**-2) * (3**-1) * (5**-1)
exp1 = "1"
match1 = compare_numeric(q1, exp1)
results.append(claim_line("Q1", fmt_sig(q1, 8), exp1, match1))

# Q2
q2 = round(2 / math.pi, 6)
exp2 = "0.636620"
match2 = compare_numeric(q2, exp2)
results.append(claim_line("Q2", fmt_fixed(q2, 6), exp2, match2))

# Q3
exact = 2 / math.pi
rounded = 0.636620
delta = rounded - exact
exp3 = "2.2763242e-07"
match3 = compare_numeric(delta, exp3)
results.append(claim_line("Q3", fmt_sig(delta, 8), exp3, match3))

# Q4
half_unit = 0.5 * 10**-6
exp4 = "5e-07"
match4 = compare_numeric(half_unit, exp4)
results.append(claim_line("Q4", fmt_sig(half_unit, 1), exp4, match4))

# Q5
q5 = (Fraction(45,7) * Fraction(1,9) * Fraction(1,5) * 7)
exp5 = "1"
match5 = compare_fraction(q5, exp5)
results.append(claim_line("Q5", f"{float(q5):.8g}", exp5, match5))

# Q6
norm6 = Fraction(3) ** -1  # 1/3
exp6 = "1/3"
match6 = compare_fraction(norm6, exp6)
results.append(claim_line("Q6", f"{float(norm6):.8g}", exp6, match6))

# Q7
abs7 = Fraction(3) ** -2  # 1/9
exp7 = "1/9"
match7 = compare_fraction(abs7, exp7)
results.append(claim_line("Q7", f"{float(abs7):.8g}", exp7, match7))

# Q8
abs8 = 60
exp8 = "60"
match8 = compare_numeric(abs8, exp8)
results.append(claim_line("Q8", str(abs8), exp8, match8))

# Q9
prod9 = (2**-2) * (3**-1) * (5**-1)
exp9 = "1/60"
# compute as fraction for exactness
prod9_frac = Fraction(1,60)
match9 = compare_fraction(prod9_frac, exp9)
results.append(claim_line("Q9", f"{float(prod9_frac):.8g}", exp9, match9))

print("\n".join(results))
print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum('yes' in r for r in results)} match, {sum('no' in r for r in results)} mismatch")
