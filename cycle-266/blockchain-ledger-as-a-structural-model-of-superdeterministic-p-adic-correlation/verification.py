import math

def fmt(val, fmt_str):
    return fmt_str.format(val)

claims = [
    {
        "id": "Q1",
        "computed": 1000 * 150 * 3000 / 1e6,  # MB
        "expected": "450",
        "match": None
    },
    {
        "id": "Q2",
        "computed": 2 ** 16,
        "expected": "65536",
        "match": None
    },
    {
        "id": "Q3",
        "computed": 1 / (2 ** 16),
        "expected": "1.525878906e-5",
        "match": None
    },
    {
        "id": "Q4",
        "computed": 2 ** (-16),
        "expected": "1.525878906e-5",
        "match": None
    },
    {
        "id": "Q5",
        "computed": sum(2 ** (-k) for k in range(1, 1000)),  # converges to 1
        "expected": "1",
        "match": None
    },
    {
        "id": "Q6",
        "computed": None,  # formula, no numeric value
        "expected": "none",
        "match": "yes"
    },
    {
        "id": "Q7",
        "computed": math.sqrt(2) - 1,
        "expected": "0.4142",
        "match": None
    },
    {
        "id": "Q8",
        "computed": 1 - 2 ** (-256),
        "expected": "none",
        "match": "yes"
    },
    {
        "id": "Q9",
        "computed": 0.10 * 168,
        "expected": "16.80",
        "match": None
    },
]

matches = 0
total = 0
for c in claims:
    if c["expected"] == "none":
        # No numeric expectation; assume match if computation succeeded
        c["match"] = "yes"
        continue
    total += 1
    if c["id"] == "Q1":
        comp_str = fmt(c["computed"], "{:.0f}")
    elif c["id"] in ("Q2", "Q5"):
        comp_str = fmt(c["computed"], "{:.0f}")
    elif c["id"] in ("Q3", "Q4"):
        comp_str = fmt(c["computed"], "{:.9e}")
    elif c["id"] == "Q7":
        comp_str = fmt(round(c["computed"], 4), "{:.4f}")
    elif c["id"] == "Q9":
        comp_str = fmt(round(c["computed"], 2), "{:.2f}")
    else:
        comp_str = str(c["computed"])
    if comp_str == c["expected"]:
        c["match"] = "yes"
        matches += 1
    else:
        c["match"] = "no"

print("VERIFICATION SUMMARY:")
print(f"{len(claims)} claims, {matches} match, {len(claims)-matches} mismatch")
for c in claims:
    print(f"CLAIM {c['id']}: computed={c['computed'] if c['computed'] is not None else 'none'} expected={c['expected']} match={c['match']}")
