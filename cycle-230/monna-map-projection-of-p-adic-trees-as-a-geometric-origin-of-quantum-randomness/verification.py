import math

def fmt(val, digits):
    """Format value with given number of decimal places (digits)."""
    if digits == 0:
        return str(int(round(val)))
    fmt_str = "{:." + str(digits) + "f}"
    return fmt_str.format(round(val, digits))

claims = [
    # Q1
    {
        "id": "Q1",
        "computed": 3 ** 3,
        "expected": "27",
        "match": None,
        "digits": 0
    },
    # Q2
    {
        "id": "Q2",
        "computed": 1 / (3 ** 3),
        "expected": "0.037037",
        "match": None,
        "digits": 6
    },
    # Q3
    {
        "id": "Q3",
        "computed": math.log(3 ** 3, 2),
        "expected": "4.7548875",
        "match": None,
        "digits": 7
    },
    # Q4
    {
        "id": "Q4",
        "computed": abs(3 ** 3 - 1) / (3 ** 3),
        "expected": "0.96296",
        "match": None,
        "digits": 5
    },
    # Q5
    {
        "id": "Q5",
        "computed": 1 / (3 ** 3),
        "expected": "0.03704",
        "match": None,
        "digits": 5
    },
    # Q6
    {
        "id": "Q6",
        "computed": (4.7548875 * 100e6) / 1e6,  # convert to Mbit/s
        "expected": "475.5",
        "match": None,
        "digits": 1
    },
    # Q7
    {
        "id": "Q7",
        "computed": 1_000_000 / 27,
        "expected": "37037",
        "match": None,
        "digits": 0
    },
    # Q8
    {
        "id": "Q8",
        "computed": 3 ** 3,
        "expected": "27",
        "match": None,
        "digits": 0
    },
]

for c in claims:
    comp_str = fmt(c["computed"], c["digits"])
    c["match"] = "yes" if comp_str == c["expected"] else "no"
    print(f"CLAIM {c['id']}: computed={comp_str} expected={c['expected']} match={c['match']}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, "
      f"{sum(1 for c in claims if c['match']=='yes')} match, "
      f"{sum(1 for c in claims if c['match']=='no')} mismatch")
