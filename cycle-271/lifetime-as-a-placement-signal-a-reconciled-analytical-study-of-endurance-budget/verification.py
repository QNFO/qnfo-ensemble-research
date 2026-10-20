import math

def fmt_sig(value, sig_digits):
    """Return a string with the given number of significant digits."""
    if value == 0:
        return "0"
    # Determine order of magnitude
    order = int(math.floor(math.log10(abs(value))))
    # Scale to get the desired sig digits
    scale = 10 ** (sig_digits - 1 - order)
    rounded = round(value * scale) / scale
    # Use plain decimal representation
    fmt_str = f"{{:.{max(sig_digits - order - 1, 0)}f}}".format(rounded)
    # Strip trailing zeros and possible trailing dot
    return fmt_str.rstrip('0').rstrip('.') if '.' in fmt_str else fmt_str

def fmt_scientific(value, mantissa_digits):
    """Return a string like 8.20e3 with the given mantissa digits."""
    if value == 0:
        return "0e0"
    exponent = int(math.floor(math.log10(abs(value))))
    mantissa = value / (10 ** exponent)
    mantissa_str = f"{mantissa:.{mantissa_digits}f}"
    # Strip trailing zeros
    mantissa_str = mantissa_str.rstrip('0').rstrip('.')
    return f"{mantissa_str}e{exponent}"

# Claim computations
claims = [
    # Q1
    ("Q1", 24 * 365, "8760"),
    # Q2
    ("Q2", 5 * 8760, "43800"),
    # Q3
    ("Q3", 12.2 / 5, "2.44"),
    # Q4
    ("Q4", 3.3 / 5, "0.66"),
    # Q5
    ("Q5", 3.3 / 3.13, "1.05"),
    # Q6
    ("Q6", 12.2 / 1.19, "10.25"),
    # Q7
    ("Q7", math.sqrt(1.19 * 3.13), "1.93"),
    # Q8
    ("Q8", 1 - 1 / 1.19, "15.97"),
    # Q9
    ("Q9", 1 - 1 / 3.13, "68.05"),
    # Q10
    ("Q10", 1e5 / 12.2, "8.20e3"),
    # Q11
    ("Q11", 8196.72 / 8760, "0.936"),
    # Q12
    ("Q12", 1e5 / 3.3, "3.03e4"),
    # Q13
    ("Q13", 30303.03 / 8760, "3.46"),
]

for cid, computed, expected in claims:
    # Determine formatting for comparison
    # For percentages we keep the raw fraction and compare after scaling
    if cid in ("Q8", "Q9"):
        # Convert to percent for display
        computed_display = fmt_sig(computed * 100, 4)  # e.g., 15.97
    elif cid in ("Q10", "Q12"):
        # Scientific notation with two mantissa digits
        computed_display = fmt_scientific(computed, 2)
    else:
        # Use appropriate significant digits based on expected string length
        # Count digits before decimal to decide sig digits
        if "." in expected:
            int_part, frac_part = expected.split(".")
            sig = len(int_part) + len(frac_part)
        else:
            sig = len(expected)
        computed_display = fmt_sig(computed, sig)

    match = "yes" if computed_display == expected else "no"
    print(f"CLAIM {cid}: computed={computed_display} expected={expected} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if (fmt_sig(c, len(e)) if not (c in (8196.72/8760,30303.03/8760)) else fmt_sig(c*100,4)) == e) } match, {len(claims) - sum(1 for _,c,e in claims if (fmt_sig(c, len(e)) if not (c in (8196.72/8760,30303.03/8760)) else fmt_sig(c*100,4)) == e)} mismatch")
