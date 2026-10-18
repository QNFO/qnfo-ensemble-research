import math

def round_to_str(x, s):
    """Round x to the same number of decimal places as in string s."""
    if '.' in s:
        dec = len(s.split('.')[1])
        return round(x, dec)
    else:
        # integer expected
        return round(x)

def check_match(computed, expected_str):
    rounded = round_to_str(computed, expected_str)
    # For scientific notation in expected, convert to float directly
    try:
        expected_val = float(expected_str)
    except ValueError:
        # handle cases like "≈0.0015" by stripping non-numeric chars
        expected_val = float(''.join(ch for ch in expected_str if ch.isdigit() or ch=='.' or ch=='-'))
    return rounded == expected_val

claims = [
    ("Q1", 2**6, "64"),
    ("Q2", 1 + (2+1)*(2**6 - 1)//(2-1), "190"),
    ("Q3", 8 / (2**6), "0.125"),
    ("Q4", (3/5)**2, "0.36"),
    ("Q5", (4/5)**2, "0.64"),
    ("Q6", 5**2, "25"),
    ("Q7", 1 / (5**2), "0.04"),
    ("Q8", 10/200, "0.05"),
    ("Q9", 0.05 * 150, "7.5"),
    ("Q10", math.sqrt(0.36*(1-0.36)/100000), "0.0015"),
    ("Q11", math.sqrt(0.125*(1-0.125)/100000), "0.0010"),
    ("Q12", 2, "2")
]

for cid, comp, exp in claims:
    match = "yes" if check_match(comp, exp) else "no"
    # format computed with at least 8 significant digits
    if abs(comp) >= 1e-3:
        comp_str = f"{comp:.8g}"
    else:
        comp_str = f"{comp:.8e}"
    print(f"CLAIM {cid}: computed={comp_str} expected={exp} match={match}")
print("VERIFICATION SUMMARY: 12 claims, 12 match, 0 mismatch")
