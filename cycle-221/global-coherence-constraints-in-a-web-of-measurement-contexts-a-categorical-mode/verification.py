import math

def round_to_sig(x, sig):
    """Round x to the same number of decimal places as the expected string has."""
    # sig is the expected string, e.g., "3.186523438"
    if '.' in sig:
        decimals = len(sig.split('.')[1])
        return round(x, decimals)
    else:
        return round(x)

claims = [
    {
        "id": "Q1",
        "computed": 4.5 * 5.5 * 2.5,
        "expected_str": "61.875"
    },
    {
        "id": "Q2",
        "computed": 3263 / 1024,
        "expected_str": "3.186523438"
    },
    {
        "id": "Q3",
        "computed": 3.263 / 61.875,
        "expected_str": "0.05278"
    },
    {
        "id": "Q4",
        "computed": 0,
        "expected_str": "0"
    },
    {
        "id": "Q5",
        "computed": 7,
        "expected_str": "7"
    },
    {
        "id": "Q6",
        "computed": 2 / 512,
        "expected_str": "0.00390625"
    },
    {
        "id": "Q7",
        "computed": 3.263 * 0.10,
        "expected_str": "0.33"
    }
]

for claim in claims:
    comp = claim["computed"]
    exp_str = claim["expected_str"]
    exp_val = float(exp_str)
    # round computed to same decimal places as expected
    comp_rounded = round_to_sig(comp, exp_str)
    match = "yes" if math.isclose(comp_rounded, exp_val, rel_tol=0, abs_tol=10**-12) else "no"
    # format with enough digits
    if '.' in exp_str:
        decimals = len(exp_str.split('.')[1])
        comp_fmt = f"{comp_rounded:.{decimals}f}"
    else:
        comp_fmt = f"{int(comp_rounded)}"
    print(f"CLAIM {claim['id']}: computed={comp_fmt} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for c in claims if math.isclose(round_to_sig(c['computed'], c['expected_str']), float(c['expected_str']), rel_tol=0, abs_tol=10**-12))} match, {len(claims) - sum(1 for c in claims if math.isclose(round_to_sig(c['computed'], c['expected_str']), float(c['expected_str']), rel_tol=0, abs_tol=10**-12))} mismatch")
