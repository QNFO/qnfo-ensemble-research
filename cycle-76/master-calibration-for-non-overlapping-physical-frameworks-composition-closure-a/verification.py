import math
from math import comb

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: C(29,2)
c1 = comb(29, 2)
results.append(("Q1", c1, 406))

# Q2: C(29,3)
c2 = comb(29, 3)
results.append(("Q2", c2, 3654))

# Q3: ratio (N-2)/3
r3 = (29 - 2) / 3
results.append(("Q3", r3, 9.0))

# Q4: N=58
c4a = comb(58, 2)
c4b = comb(58, 3)
r4 = (58 - 2) / 3
results.append(("Q4a", c4a, 1653))
results.append(("Q4b", c4b, 30856))
results.append(("Q4c", r4, 18.666666666666668))

# Q5: C(7,2) and directed 7*6
c5 = comb(7, 2)
d5 = 7 * 6
results.append(("Q5a", c5, 21))
results.append(("Q5b", d5, 42))

# Q6: 29 - 21
q6 = 29 - 21
results.append(("Q6", q6, 8))

# Q7: closure error for three-edge cycle
eps12, eps23, eps31 = 0.001, 0.002, 0.0005
delta = 1 - (1 - eps12) * (1 - eps23) * (1 - eps31)
results.append(("Q7", delta, 0.0034965))

# Q8: additive first-order bound
add = eps12 + eps23 + eps31
results.append(("Q8", add, 0.0035))

match = 0
mismatch = 0
for cid, computed, expected in results:
    if isinstance(expected, float):
        ok = close(computed, expected)
    else:
        ok = computed == expected
    if ok:
        match += 1
    else:
        mismatch += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match} match, {mismatch} mismatch")
