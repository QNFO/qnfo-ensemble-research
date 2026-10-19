import math

def fmt(val, sig):
    """Format a float with given significant digits."""
    if val == 0:
        return "0"
    # Determine number of digits before decimal
    int_digits = int(math.floor(math.log10(abs(val)))) + 1
    if int_digits >= sig:
        # No decimal part needed
        fmt_str = "{:." + str(0) + "f}"
    else:
        dec = sig - int_digits
        fmt_str = "{:." + str(dec) + "f}"
    return fmt_str.format(val)

claims = [
    # Q1
    {
        "id": "Q1",
        "computed": 100 * 1 * 0.1 / 2,
        "expected": "5.0",
    },
    # Q2
    {
        "id": "Q2",
        "computed": math.sqrt(5.0 / (0.095 * 100)),
        "expected": "0.726",
    },
    # Q3
    {
        "id": "Q3",
        "computed": 1.0 * 0.5,
        "expected": "0.5",
    },
    # Q4
    {
        "id": "Q4",
        "computed": (0.6 / (1 + 0.6)) / (0.5 / (2 * math.pi)),
        "expected": "4.71",
    },
    # Q5 (energy cost)
    {
        "id": "Q5",
        "computed": (0.05 / 2) * 1.0,
        "expected": "0.025",
    },
    # Q6
    {
        "id": "Q6",
        "computed": (0.05 / 2) / 0.5,
        "expected": "0.05",
    },
    # Q7
    {
        "id": "Q7",
        "computed": (0.1 / 0.6) * 100,
        "expected": "16.7",
    },
    # Q8
    {
        "id": "Q8",
        "computed": 0.5 * (0.1 ** 2),  # ΔV = 0.5 * u0^2 because x0=0
        "expected": "0.005",
    },
    # Q9
    {
        "id": "Q9",
        "computed": 0.1 - (0.1 ** 2) / 2,
        "expected": "0.095",
    },
    # Q10
    {
        "id": "Q10",
        "computed": 0.5 * (0.9 * 2) ** 2 - 0.5 * (2 ** 2),
        "expected": "-0.38",
    },
    # Q11
    {
        "id": "Q11",
        "computed": 0.5 * (2.3 ** 2) - 0.5 * (2 ** 2),
        "expected": "0.645",
    },
    # Q12
    {
        "id": "Q12",
        "computed": -0.095 * (1 ** 2) - 0.1 * (1) * (-1) + 0.5 * ((-1) ** 2),
        "expected": "0.505",
    },
    # Q13 (max δ)
    {
        "id": "Q13",
        "computed": 1 - (1 ** 2) / 2,
        "expected": "0.5",
    },
]

matches = 0
for c in claims:
    # Determine number of significant digits from expected string
    exp_str = c["expected"]
    # Count digits ignoring sign, decimal point
    sig = len(exp_str.replace(".", "").replace("-", ""))
    comp_str = fmt(c["computed"], sig)
    match = "yes" if comp_str == exp_str else "no"
    if match == "yes":
        matches += 1
    print(f"CLAIM {c['id']}: computed={comp_str} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {matches} match, {len(claims)-matches} mismatch")
