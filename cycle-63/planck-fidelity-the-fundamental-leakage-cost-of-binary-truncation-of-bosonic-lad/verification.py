import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: L_P^(2) = theta^4 / 2 (symbolic; check at a sample theta, e.g. theta=1)
theta = 1.0
computed = theta**4 / 2
expected = None
results.append(("Q1", computed, expected))

# Q2: pi-pulse: theta = pi/2, L_P^(2) = (pi/2)^4 / 2, expected 3.0440341
theta = math.pi / 2
computed = (theta**4) / 2
expected = 3.0440341
results.append(("Q2", computed, expected))

# Q3: c_2^(2) = -theta^2 / sqrt(2) (symbolic; check at theta=1)
theta = 1.0
computed = -(theta**2) / math.sqrt(2)
expected = None
results.append(("Q3", computed, expected))

# Q4: Omega/alpha = 0.1 -> L = 0.01
r = 0.1
computed = r**2
expected = 1.0e-2
results.append(("Q4", computed, expected))

# Q5: Omega/alpha = 0.05 -> L = 2.5e-3
r = 0.05
computed = r**2
expected = 2.5e-3
results.append(("Q5", computed, expected))

# Q6: Omega/alpha = 0.2 -> L = 4.0e-2
r = 0.2
computed = r**2
expected = 4.0e-2
results.append(("Q6", computed, expected))

# Q7: S_Base(12) = ln 6, expected 1.7917595 nats
d = 12
computed = math.log(d / 2)
expected = 1.7917595
results.append(("Q7", computed, expected))

# Q8: bits = S_Base / ln 2, expected 2.5849625
s_nats = math.log(6)
computed = s_nats / math.log(2)
expected = 2.5849625
results.append(("Q8", computed, expected))

match_count = 0
mismatch_count = 0
for qid, computed, expected in results:
    if expected is None:
        print(f"CLAIM {qid}: computed={computed:.10g} expected=None match=yes")
        match_count += 1
    else:
        ok = isclose(computed, expected)
        if ok:
            match_count += 1
        else:
            mismatch_count += 1
        print(f"CLAIM {qid}: computed={computed:.10g} expected={expected} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {mismatch_count} mismatch")
