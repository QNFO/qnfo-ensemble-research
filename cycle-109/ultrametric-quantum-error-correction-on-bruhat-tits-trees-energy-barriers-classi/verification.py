import math

def maj_fail(p, n=8, kmin=5):
    total = 0.0
    for k in range(kmin, n + 1):
        total += math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    return total

results = []

# Q1: single-level majority vote at p=0.4
q1 = maj_fail(0.4)
expected_q1 = 0.1736704
results.append(("Q1", q1, expected_q1))

# Q2: two concatenated levels
p1 = maj_fail(0.4)
q2 = maj_fail(p1)
expected_q2 = 0.0055485
results.append(("Q2", q2, expected_q2))

# Q3: three concatenated levels
p2 = maj_fail(p1)
q3 = maj_fail(p2)
expected_q3 = 2.905e-10
results.append(("Q3", q3, expected_q3))

# Q4: 95% one-sided confidence bound for N=10^4
N4 = 10 ** 4
q4 = 1 - 0.05 ** (1.0 / N4)
expected_q4 = 2.9957e-4
results.append(("Q4", q4, expected_q4))

# Q5: 95% one-sided confidence bound for N=10^5
N5 = 10 ** 5
q5 = 1 - 0.05 ** (1.0 / N5)
expected_q5 = 2.9957e-5
results.append(("Q5", q5, expected_q5))

# Q6: thermal activation bound at d=3
q6 = math.exp(-2 ** 3)
expected_q6 = 3.3553e-4
results.append(("Q6", q6, expected_q6))

# Q7: thermal activation bound at d=5
q7 = math.exp(-2 ** 5)
expected_q7 = 1.2664e-14
results.append(("Q7", q7, expected_q7))

# Q8: thermal activation bound at d=10, expressed as power of ten
q8 = 1024 / math.log(10)
expected_q8 = 444.7
results.append(("Q8", q8, expected_q8))

mismatch = 0
for cid, computed, expected in results:
    if isinstance(expected, float) and abs(expected) < 1:
        match = math.isclose(computed, expected, rel_tol=1e-2)
    else:
        match = math.isclose(computed, expected, rel_tol=1e-2)
    if not match:
        mismatch += 1
    print(f"CLAIM {cid}: computed={computed:.10g} expected={expected} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results) - mismatch} match, {mismatch} mismatch")
