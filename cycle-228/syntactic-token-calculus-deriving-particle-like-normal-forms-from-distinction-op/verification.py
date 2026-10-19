# Compute and verify quantitative claims from the paper

def sig_round(value, sig_digits):
    """Round value to the given number of significant digits."""
    from math import log10, floor
    if value == 0:
        return 0.0
    digits = sig_digits - int(floor(log10(abs(value)))) - 1
    return round(value, digits)

claims = [
    {
        "id": "Q1",
        "computed": 87.1 + 83.8 + 68.7 + 73.0 + 75.0 + 88.9 + 86.6 + 86.6 + 58.7,
        "expected_str": "708.4",
        "sig": 4  # 4 significant digits in 708.4
    },
    {
        "id": "Q2",
        "computed": (87.1 + 83.8 + 68.7 + 73.0 + 75.0 + 88.9 + 86.6 + 86.6 + 58.7) / 9,
        "expected_str": "78.711",
        "sig": 6  # 6 significant digits in 78.711
    },
    {
        "id": "Q3",
        "computed": 2**(5 + 1) - 1,
        "expected_str": "63",
        "sig": 2  # 2 significant digits in 63
    },
    {
        "id": "Q4",
        "computed": 1e-3 * 1 * 63,
        "expected_str": "0.063",
        "sig": 3  # 3 significant digits in 0.063
    },
    {
        "id": "Q5",
        "computed": 0.063 / 1e-12,
        "expected_str": "6.3e10",
        "sig": 2  # 2 significant digits in 6.3e10
    },
]

for c in claims:
    expected = float(c["expected_str"].replace("e", "E"))
    rounded = sig_round(c["computed"], c["sig"])
    match = "yes" if abs(rounded - expected) < 1e-12 else "no"
    # format computed with at least 8 significant digits
    comp_str = f"{c['computed']:.12g}"
    exp_str = c["expected_str"]
    print(f"CLAIM {c['id']}: computed={comp_str} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, "
      f"{sum(1 for c in claims if sig_round(c['computed'], c['sig']) == float(c['expected_str'].replace('e','E')))} match, "
      f"{sum(1 for c in claims if sig_round(c['computed'], c['sig']) != float(c['expected_str'].replace('e','E')))} mismatch")
