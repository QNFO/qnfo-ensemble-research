import math

def fmt(val, sig):
    """Round val to given number of significant digits and format without scientific notation if possible."""
    if val == 0:
        return "0"
    # Determine order of magnitude
    order = int(math.floor(math.log10(abs(val))))
    digits = sig - 1 - order
    fmt_str = "{:." + str(max(digits,0)) + "f}"
    rounded = round(val, digits) if digits >= 0 else round(val, -digits)
    s = fmt_str.format(rounded)
    # Remove trailing zeros and dot
    s = s.rstrip('0').rstrip('.') if '.' in s else s
    return s

claims = [
    ("Q1", 4e-23, "4e-23"),
    ("Q2", 2e-3, "2e-3"),
    ("Q3", 0.08, "0.08"),
    ("Q4", 1 - math.exp(-0.08), "0.0769"),
    ("Q5", 8.0, "8"),
    ("Q6", 1 - math.exp(-8), "0.99966"),
    ("Q7", math.sqrt(8), "2.8284"),
    ("Q8", (100 * 0.02) / 19, "0.105263"),
    ("Q9", 1 - math.exp(-((100 * 0.02) / 19)), "0.0999"),
    ("Q10", 190.0, "190"),
    ("Q11", (1e6 / 1e8) ** 2, "1e-4"),
    ("Q12", (1e-4) * 1e4, "1"),
    ("Q13", 5 * 1, "5"),
    ("Q14", 1 / 5, "0.2"),
    ("Q15", (1e5 ** 2) / (8 * 1e6), "1.25e3"),
    ("Q16", 1 / ((1e5 ** 2) / (8 * 1e6)), "800e-6"),
]

for cid, comp, exp in claims:
    # Determine number of significant digits in expected value
    # Strip possible scientific notation
    if "e" in exp or "E" in exp:
        base, exp_part = exp.split('e') if 'e' in exp else exp.split('E')
        sig_digits = len(base.replace('.', '').replace('-', '').lstrip('0'))
    else:
        # Count digits ignoring decimal point and leading zeros
        sig_digits = len(exp.replace('.', '').replace('-', '').lstrip('0'))
    # Format computed value to same number of significant digits
    comp_str = fmt(comp, sig_digits)
    match = "yes" if comp_str == exp else "no"
    print(f"CLAIM {cid}: computed={comp_str} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if fmt(c, len(e.replace('.','').replace('-','').lstrip('0'))) == e)} match, {sum(1 for _,c,e in claims if fmt(c, len(e.replace('.','').replace('-','').lstrip('0'))) != e)} mismatch")
