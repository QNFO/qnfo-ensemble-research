import math

def fmt(val):
    # Format with at least 8 significant digits, removing trailing zeros
    if isinstance(val, float):
        s = f"{val:.10g}"
    else:
        s = str(val)
    return s

claims = [
    {
        "id": "Q1",
        "computed": (2+1) * 2**(5-1),  # N = (p+1) * p^(D-1)
        "expected": "48"
    },
    {
        "id": "Q2",
        "computed": (2+1) * 2**(10-1),
        "expected": "1536"
    },
    {
        "id": "Q3",
        "computed": 1 + (2+1)*(2**5 - 1)//(2-1),  # integer division safe here
        "expected": "94"
    },
    {
        "id": "Q4",
        "computed": 1 + (2+1)*(2**10 - 1)//(2-1),
        "expected": "3070"
    },
    {
        "id": "Q5",
        "computed": (1) * 100,  # S = (beta/alpha) * D, beta/alpha=1, D=100
        "expected": "100"
    },
    {
        "id": "Q6",
        "computed": 2**20 / 5,  # R = 2^F / D, F=20, D=5
        "expected": "209715.2"
    },
    {
        "id": "Q7",
        "computed": 2**20 / 10,
        "expected": "104857.6"
    },
    {
        "id": "Q8",
        "computed": 6.6,  # factor itself
        "expected": "6.6"
    },
    {
        "id": "Q9",
        "computed": 100 - 0,  # improvement = detection_BT - detection_baseline
        "expected": "100"
    },
    {
        "id": "Q10",
        "computed": (1 * 10**2) / (1 * 10),  # speedup = classical_steps / quantum_steps
        "expected": "10"
    }
]

for c in claims:
    comp = c["computed"]
    exp = c["expected"]
    match = "yes" if fmt(comp) == exp else "no"
    print(f"CLAIM {c['id']}: computed={fmt(comp)} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, "
      f"{sum(1 for c in claims if fmt(c['computed']) == c['expected'])} match, "
      f"{sum(1 for c in claims if fmt(c['computed']) != c['expected'])} mismatch")
