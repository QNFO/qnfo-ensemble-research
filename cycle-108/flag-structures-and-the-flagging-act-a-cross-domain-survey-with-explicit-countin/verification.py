import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: |Fl_3(F_2)| = 21
q1 = 1
for k in range(1, 4):
    q1 *= (2**k - 1) // (2 - 1)
results.append(("Q1", q1, 21))

# Q2: |Fl_4(F_2)| = 315
q2 = 1
for k in range(1, 5):
    q2 *= (2**k - 1) // (2 - 1)
results.append(("Q2", q2, 315))

# Q3: |Fl_5(F_2)| = 9765
q3 = 1
for k in range(1, 6):
    q3 *= (2**k - 1) // (2 - 1)
results.append(("Q3", q3, 9765))

# Q4: |Fl_6(F_2)| = 615195
q4 = 1
for k in range(1, 7):
    q4 *= (2**k - 1) // (2 - 1)
results.append(("Q4", q4, 615195))

# Q5: growth factors 315/21 = 15 = 2^4-1 and 615195/9765 = 63 = 2^6-1
g1 = 315 / 21
g2 = 615195 / 9765
ok5 = isclose(g1, 2**4 - 1) and isclose(g2, 2**6 - 1)
results.append(("Q5", (g1, g2), (15, 63)))

# Q6: 2^(n(n-1)/2) for n=4 -> 64 <= 315
lb = 2 ** (4 * 3 // 2)
ok6 = lb <= 315
results.append(("Q6", lb, 64))

# Q7: dim_C Fl_4 = C(4,2) = 6
d = 4 * 3 // 2
results.append(("Q7", d, 6))

# Q8: 315/24 = 13.125
r = 315 / 24
results.append(("Q8", r, 13.125))

match_count = 0
for cid, computed, expected in results:
    if isinstance(computed, tuple):
        match = all(isclose(c, e) for c, e in zip(computed, expected))
    elif isinstance(expected, float):
        match = isclose(computed, expected)
    else:
        match = (computed == expected)
    if cid == "Q6":
        match = ok6
    if cid == "Q5":
        match = ok5
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")
    if match:
        match_count += 1

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
