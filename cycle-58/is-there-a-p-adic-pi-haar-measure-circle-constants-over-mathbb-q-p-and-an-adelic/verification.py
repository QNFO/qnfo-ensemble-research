import math

claims = [
    ("Q1", 2, 1 - 1/pow(2,2), 0.75),
    ("Q2", 3, 1 - 1/pow(3,2), 8/9),
    ("Q3", 5, 1 - 1/pow(5,2), 24/25),
    ("Q4", 7, 1 - 1/pow(7,2), 48/49),
    ("Q5", 11, 1 - 1/pow(11,2), 120/121),
    ("Q6", 2, (1 - 1/pow(2,2))/2, 0.375),
    ("Q7", 3, (1 - 1/pow(3,2))/2, 4/9),
    ("Q8", 5, (1 - 1/pow(5,2))/2, 0.48),
]

match_count = 0
for cid, p, computed, expected in claims:
    match = math.isclose(computed, expected, rel_tol=1e-6)
    if match:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed:.6f} expected={expected:.6f} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")
