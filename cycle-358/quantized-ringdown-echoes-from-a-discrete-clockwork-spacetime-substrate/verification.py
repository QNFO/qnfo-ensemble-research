import math

def fmt(x):
    # format with 8 significant digits, removing trailing zeros
    return ("{:.8g}".format(x)).replace('e+', 'e').replace('e0', 'e')

claims = [
    {
        "id": "Q1",
        "computed": 3**(-10),
        "expected": "1.693e-5"
    },
    {
        "id": "Q2",
        "computed": 250 * 3**(-10),
        "expected": "4.23e-3"
    },
    {
        "id": "Q3",
        "computed": 0.1**10,
        "expected": "1e-10"
    },
    {
        "id": "Q4",
        "computed": 250 * 2**(-15),
        "expected": "7.63e-3"
    },
    {
        "id": "Q5",
        "computed": 0.05**15,
        "expected": "3.05e-20"
    },
    {
        "id": "Q6",
        "computed": [0.1**10, 0.05**10, 0.01**10],
        "expected": ["1e-10", "9.77e-14", "1e-20"]
    },
    {
        "id": "Q7",
        "computed": 250 * 5**(-5),
        "expected": "0.08"
    },
    {
        "id": "Q8",
        "computed": 0.01,
        "expected": "0.01"
    },
    {
        "id": "Q9",
        "computed": 250 * 4**(-8),
        "expected": "3.81e-3"
    },
    {
        "id": "Q10",
        "computed": 0.2**8,
        "expected": "2.56e-6"
    },
]

for c in claims:
    cid = c["id"]
    comp = c["computed"]
    exp = c["expected"]
    if isinstance(comp, list):
        # multiple values
        matches = []
        for val, exp_val in zip(comp, exp):
            match = "yes" if fmt(val) == exp_val else "no"
            matches.append(match)
        match_str = "/".join(matches)
        comp_str = "/".join(fmt(v) for v in comp)
        print(f"CLAIM {cid}: computed={comp_str} expected={','.join(exp)} match={match_str}")
    else:
        match = "yes" if fmt(comp) == exp else "no"
        print(f"CLAIM {cid}: computed={fmt(comp)} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for c in claims if (isinstance(c['computed'], list) and all(fmt(v)==e for v,e in zip(c['computed'],c['expected']))) or (not isinstance(c['computed'], list) and fmt(c['computed'])==c['expected']))} match, {len(claims) - sum(1 for c in claims if (isinstance(c['computed'], list) and all(fmt(v)==e for v,e in zip(c['computed'],c['expected']))) or (not isinstance(c['computed'], list) and fmt(c['computed'])==c['expected']))} mismatch")
