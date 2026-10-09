import math
from fractions import Fraction

def close(a, b):
    return math.isclose(float(a), float(b), rel_tol=1e-6)

results = []

# Q1: B(E) = max(max(3+2, 1+1+1), 4, 0) = 5
b1 = max(max(3 + 2, 1 + 1 + 1), 4, 0)
results.append(("Q1", b1, 5))

# Q2: B(E') = max(max(5,5),1) = 5; overestimate = 5 - 1 = 4
b2 = max(max(5, 5), 1)
over2 = b2 - 1
results.append(("Q2", b2, 5))
results.append(("Q2-over", over2, 4))

# Q3: D(p)=5, D(q)=5, D(pq)=10; max product weight = max(7,10,4,7) = 10
dp = max(3 + 2 + 0, 1 + 1 + 0)   # max(5,2)
dq = max(2 + 0 + 0, 0 + 4 + 1)   # max(2,5)
dpq = dp + dq
weights = [5 + 2 + 0, 3 + 6 + 1, 3 + 1 + 0, 1 + 5 + 1]  # 7,10,4,7
maxw = max(weights)
results.append(("Q3-Dp", dp, 5))
results.append(("Q3-Dq", dq, 5))
results.append(("Q3-Dpq", dpq, 10))
results.append(("Q3-maxw", maxw, 10))

# Q4: D(p+q) <= max(5,5) = 5
sum_bound = max(dp, dq)
results.append(("Q4", sum_bound, 5))

# Q5: composition bound 5*5 = 25; worst monomial 3*5 + 2*5 = 25
comp = dp * dq
worst = 3 * 5 + 2 * 5
results.append(("Q5", comp, 25))
results.append(("Q5-worst", worst, 25))

# Q6: D3 = 5 * 5^3 = 625
d3 = 5 * 5 ** 3
results.append(("Q6", d3, 625))

# Q7: s(E) = 8 + 4 + 3 + 1 + 1 = 17
leaves = 3 + 3 + 2 + 0
sE = leaves + 4 + 3 + 1 + 1
results.append(("Q7", sE, 17))

# Q8: M(n,d) = C(n+d, d); M(2,2)=6, M(3,2)=10, M(3,5)=56, M(10,5)=3003
m22 = math.comb(2 + 2, 2)
m32 = math.comb(3 + 2, 2)
m35 = math.comb(3 + 5, 5)
m105 = math.comb(10 + 5, 5)
results.append(("Q8-M22", m22, 6))
results.append(("Q8-M32", m32, 10))
results.append(("Q8-M35", m35, 56))
results.append(("Q8-M105", m105, 3003))

match = 0
mismatch = 0
for cid, computed, expected in results:
    ok = close(computed, expected)
    if ok:
        match += 1
    else:
        mismatch += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match} match, {mismatch} mismatch")
