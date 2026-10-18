import math
from fractions import Fraction

def round_to_places(x, places):
    return round(x, places)

def format_scientific(x, mantissa_places):
    # Return string like 5.31e-3
    exp = int(math.floor(math.log10(abs(x)))) if x != 0 else 0
    mant = x / (10**exp)
    mant_rounded = round(mant, mantissa_places)
    # Adjust if rounding caused mantissa to be 10
    if abs(mant_rounded) >= 10:
        mant_rounded /= 10
        exp += 1
    return f"{mant_rounded:.{mantissa_places}f}e{exp:+d}"

# Compute claims
results = {}

# Q1
anthro = 28
total = 31
P = anthro / total
results["Q1"] = round_to_places(P, 5)  # 5 decimal places

# Q4 (radix factor)
lambda_r = math.log10(8)
results["Q4"] = round_to_places(lambda_r, 9)  # 9 decimal places

# Q5 (body-scale factor)
lambda_s_L = 0.01 / 1.70
results["Q5"] = round_to_places(lambda_s_L, 10)  # 10 decimal places

# Q6 (chemical factor)
lambda_c_M = 2330 / 1000
results["Q6"] = round_to_places(lambda_c_M, 2)  # 2 decimal places

# Q2 (length scaling)
lambda_L = lambda_r * lambda_s_L
# Expected in scientific form with 2 mantissa digits
results["Q2"] = format_scientific(lambda_L, 2)

# Q3 (mass scaling)
lambda_M = lambda_r * lambda_c_M
results["Q3"] = round_to_places(lambda_M, 2)  # 2 decimal places

# Q7 (observer types)
observer_types = 4 * 3 * 3
results["Q7"] = observer_types

# Q8 (digit-slot cost base 10)
N = 137.036
digits_base10 = math.ceil(math.log10(N))
E10 = 10 * digits_base10
results["Q8"] = E10

# Q9 (continuous optimum)
e = 2.71828
lnN = math.log(N)
E_star = e * lnN
results["Q9"] = round_to_places(E_star, 2)  # 2 decimal places

# Q10 (overhead)
overhead = E10 / E_star
results["Q10"] = round_to_places(overhead, 2)  # 2 decimal places

# Q11 (optimal integer radix)
log3_N = math.log(N, 3)
digits_base3 = math.ceil(log3_N)
E3 = 3 * digits_base3
results["Q11"] = E3

# Q12 (cross-ratio original)
A, B, C, D = 0, 1, 2, 3
CR = ((A - C) * (B - D)) / ((A - D) * (B - C))
results["Q12"] = Fraction(CR).limit_denominator()

# Q13 (cross-ratio after transformation)
Ap, Bp, Cp, Dp = 1, 3, 5, 7
CRp = ((Ap - Cp) * (Bp - Dp)) / ((Ap - Dp) * (Bp - Cp))
results["Q13"] = Fraction(CRp).limit_denominator()

# Expected values as strings
expected = {
    "Q1": "0.90323",
    "Q2": "5.31e-3",
    "Q3": "2.10",
    "Q4": "0.903089987",
    "Q5": "0.0058823529",
    "Q6": "2.33",
    "Q7": "36",
    "Q8": "30",
    "Q9": "13.37",
    "Q10": "2.24",
    "Q11": "15",
    "Q12": "4/3",
    "Q13": "4/3",
}

# Comparison and output
for cid in sorted(expected.keys()):
    comp = results[cid]
    exp = expected[cid]
    if isinstance(comp, Fraction):
        comp_str = f"{comp.numerator}/{comp.denominator}"
        match = comp_str == exp
    else:
        comp_str = str(comp)
        # For numeric strings, compare after normalizing formatting
        if 'e' in exp:
            # scientific notation comparison
            match = comp_str == exp
        else:
            # compare as float with appropriate rounding
            match = comp_str == exp
    print(f"CLAIM {cid}: computed={comp_str} expected={exp} match={'yes' if match else 'no'}")
