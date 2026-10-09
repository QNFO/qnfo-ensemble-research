import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: Expected single-arm purity (b + b^2)/(b^3 + 1) at b = 1e6
b = 1e6
q1 = (b + b**2) / (b**3 + 1)
expected_q1 = 1.000001e-6
results.append(("Q1", q1, expected_q1))

# Q2: Excess purity (b^2 - 1)/(b^4 + b) at b = 1e6
q2 = (b**2 - 1) / (b**4 + b)
expected_q2 = 9.99999e-13
results.append(("Q2", q2, expected_q2))

# Q3: Single-arm entropy in bits: (6*ln(10) - 1/(2*b)) / ln(2)
ln10 = 2.302585
ln2 = 0.693147
q3 = (6 * ln10 - 1 / (2 * b)) / ln2
expected_q3 = 13.8155095 / ln2  # paper states 13.8155095 nats ≈ 19.93 bits
results.append(("Q3", q3, expected_q3))

# Q4: Recovery error bound K/b at K = 1e3, b = 1e6
K4 = 1e3
q4 = K4 / b
expected_q4 = 1e-3
results.append(("Q4", q4, expected_q4))

# Q5: Recovery error bound K/b at K = 1e4, b = 1e6
K5 = 1e4
q5 = K5 / b
expected_q5 = 1e-2
results.append(("Q5", q5, expected_q5))

# Q6: Recovery error bound K/b at K = 1e5, b = 1e6
K6 = 1e5
q6 = K6 / b
expected_q6 = 0.1
results.append(("Q6", q6, expected_q6))

# Q7: Recovery error bound K/b at K = 32, b = 1024
K7 = 32
b7 = 1024
q7 = K7 / b7
expected_q7 = 3.125e-2
results.append(("Q7", q7, expected_q7))

# Q8: Markov bound success probability 1 - 1/4
q8 = 1 - 1/4
expected_q8 = 0.75
results.append(("Q8", q8, expected_q8))

match_count = 0
for cid, computed, expected in results:
    match = isclose(computed, expected)
    if match:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

total = len(results)
mismatch = total - match_count
print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {mismatch} mismatch")
