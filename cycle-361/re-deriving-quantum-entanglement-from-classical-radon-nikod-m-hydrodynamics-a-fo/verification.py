import math

def fmt(val, sig_digits):
    """Format val to the given number of significant digits."""
    if val == 0:
        return "0"
    # Determine order of magnitude
    order = int(math.floor(math.log10(abs(val))))
    digits = sig_digits - 1 - order
    if digits > 0:
        fmt_str = "{:." + str(digits) + "f}"
    else:
        fmt_str = "{:." + "0" + "f}"
    return fmt_str.format(round(val, digits))

claims = [
    {
        "id": "Q1",
        "computed": 4 / 2,
        "expected": "2",
        "sig": 1,
    },
    {
        "id": "Q2",
        "computed": (2 * math.sqrt(2)) / 2,
        "expected": "1.414214",
        "sig": 7,  # 1 digit before decimal + 6 after = 7 significant
    },
    {
        "id": "Q3",
        "computed": (1.0e-3) / (3.0e8) / 10,
        "expected": "3.333333e-13",
        "sig": 7,
    },
    {
        "id": "Q4",
        "computed": (1.0e-3) / (3.0e8),
        "expected": "3.333333e-12",
        "sig": 7,
    },
    {
        "id": "Q5",
        "computed": ((1.0e-3) / (3.0e8)) / ((1.0e-3) / (3.0e8) / 10),
        "expected": "10",
        "sig": 2,
    },
    {
        "id": "Q6",
        "computed": (1.0) / (3.0e8),
        "expected": "3.333333e-9",
        "sig": 7,
    },
    {
        "id": "Q7",
        "computed": ((1.0) / (3.0e8)) / 10,
        "expected": "3.333333e-10",
        "sig": 7,
    },
    {
        "id": "Q8",
        "computed": ((1.0) / (3.0e8)) / ((1.0) / (3.0e8) / 10),
        "expected": "10",
        "sig": 2,
    },
    {
        "id": "Q9",
        "computed": ((1.0) / (3.0e8)) / (3.333333e-13),
        "expected": "1.0e4",
        "sig": 2,
    },
]

for c in claims:
    comp = c["computed"]
    exp = float(c["expected"])
    # Determine match by rounding to the number of significant digits of expected
    comp_rounded = float(fmt(comp, c["sig"]))
    match = "yes" if abs(comp_rounded - exp) < 1e-12 * max(1.0, abs(exp)) else "no"
    # Print with full precision for computed value
    print(f"CLAIM {c['id']}: computed={comp:.12g} expected={c['expected']} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for c in claims if abs(float(fmt(c['computed'], c['sig'])) - float(c['expected'])) < 1e-12 * max(1.0, float(c['expected']))) } match, {len(claims) - sum(1 for c in claims if abs(float(fmt(c['computed'], c['sig'])) - float(c['expected'])) < 1e-12 * max(1.0, float(c['expected']))) } mismatch")
