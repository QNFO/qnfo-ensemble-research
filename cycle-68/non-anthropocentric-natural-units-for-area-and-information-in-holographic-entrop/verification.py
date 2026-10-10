import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: 1/ln2 with ln2 = 0.693147
ln2 = 0.693147
v = 1 / ln2
results.append(("Q1", v, 1.442695))

# Q2: 1/ln10 with ln10 = 2.302585
ln10 = 2.302585
v = 1 / ln10
results.append(("Q2", v, 0.4342945))

# Q3: ln10/ln2
v = ln10 / ln2
results.append(("Q3", v, 3.321928))

# Q4: A=1 -> S = 0.25 nats, bits = 0.25/ln2
A = 1.0
S = A / 4
b = S / ln2
results.append(("Q4", b, 0.360674))

# Q5: A=1 -> decimal digits d = (A/4)/ln10
d = (A / 4) / ln10
results.append(("Q5", d, 0.1085736))

# Q6: A = 10^68 -> S = 2.5e67
A68 = 10.0**68
S68 = A68 / 4
results.append(("Q6", S68, 2.5e67))

# Q7: b = S/ln2 for S = 2.5e67
b68 = S68 / ln2
results.append(("Q7", b68, 3.60674e67))

# Q8: log10(D) = S/ln10 for S = 2.5e67
l10D = S68 / ln10
results.append(("Q8", l10D, 1.085736e67))

match_count = 0
for cid, computed, expected in results:
    m = close(computed, expected)
    if m:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed:.10g} expected={expected:.10g} match={'yes' if m else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
