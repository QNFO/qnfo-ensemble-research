# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "For E = x1^3 x2^2 + x1 x2 x3 - 7 x3^4 + 2, the syntactic degree bound B(E) = 5 and the true degree is 5 (tight).",
    "inputs": "exponent vectors (3,2,0),(1,1,1),(0,0,4),(0,0,0); B(x1^3 x2^2)=3+2, B(x1 x2 x3)=1+1+1, B(x3^4)=4, B(2)=0",
    "formula": "B(E) = max(max(3+2, 1+1+1), 4, 0) = max(5,3,4,0) = 5"
  },
  {
    "id": "Q2",
    "statement": "For E' = x1^3 x2^2 - x1^3 x2^2 + x1, B(E') = 5 while the true degree is 1; overestimate is 4.",
    "inputs": "B(x1^3 x2^2)=5, B(x1)=1",
    "formula": "B(E') = max(max(5,5),1) = 5; overestimate = 5 - 1 = 4"
  },
  {
    "id": "Q3",
    "statement": "For p = x^3 y^2 + xy and q = x^2 + y^4 z, D(p) = 5, D(q) = 5, D(pq) = 10, and direct expansion confirms deg(pq) = 10 (tight).",
    "inputs": "|(3,2,0)|=5, |(1,1,0)|=2, |(2,0,0)|=2, |(0,4,1)|=5",
    "formula": "D(p) = max(5,2) = 5; D(q) = max(2,5) = 5; D(pq) = D(p) + D(q) = 5 + 5 = 10; max product weight = max(7,10,4,7) = 10"
  },
  {
    "id": "Q4",
    "statement": "Sum bound D(p + q) <= 5 for the same p and q.",
    "inputs": "D(p)=5, D(q)=5",
    "formula": "D(p+q) <= max(D(p), D(q)) = max(5,5) = 5"
  },
  {
    "id": "Q5",
    "statement": "Single composition bound: substituting q (D=5) into p (D=5) gives bound 25, tight for the worst monomial x^3 y^2.",
    "inputs": "d_p=5, d_q=5",
    "formula": "D = d_p * d_q = 5 * 5 = 25; worst monomial check: 3*5 + 2*5 = 15 + 10 = 25"
  },
  {
    "id": "Q6",
    "statement": "Three iterated compositions give D3 = 625.",
    "inputs": "d_p=5, d_q=5, k=3",
    "formula": "D3 = d_p * d_q^k = 5 * 5^3 = 5^4 = 625"
  },
  {
    "id": "Q7",
    "statement": "Syntax-tree size of the Section 4.3 example is s(E) = 17 nodes, so the traversal performs at most 17 rule applications.",
    "inputs": "leaf nodes 3+3+2+0=8, monomial-product nodes 4, sum nodes 3, negation 1, outer structure node 1",
    "formula": "s(E) = 8 + 4 + 3 + 1 + 1 = 17"
  },
  {
    "id": "Q8",
    "statement": "Number of monomials in n variables of total degree at most d is M(n,d) = C(n+d, d); M(2,2)=6, M(3,2)=10, M(3,5)=56, M(10,5)=3003.",
    "inputs": "n=2,d=2; n=3,d=2; n=3,d=5; n=10,d=5",
    "formula": "M(n,d) = C(n+d, d)"
  }
]

## Script
```python
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

```

## Execution output
```
CLAIM Q1: computed=5 expected=5 match=yes
CLAIM Q2: computed=5 expected=5 match=yes
CLAIM Q2-over: computed=4 expected=4 match=yes
CLAIM Q3-Dp: computed=5 expected=5 match=yes
CLAIM Q3-Dq: computed=5 expected=5 match=yes
CLAIM Q3-Dpq: computed=10 expected=10 match=yes
CLAIM Q3-maxw: computed=10 expected=10 match=yes
CLAIM Q4: computed=5 expected=5 match=yes
CLAIM Q5: computed=25 expected=25 match=yes
CLAIM Q5-worst: computed=25 expected=25 match=yes
CLAIM Q6: computed=625 expected=625 match=yes
CLAIM Q7: computed=17 expected=17 match=yes
CLAIM Q8-M22: computed=6 expected=6 match=yes
CLAIM Q8-M32: computed=10 expected=10 match=yes
CLAIM Q8-M35: computed=56 expected=56 match=yes
CLAIM Q8-M105: computed=3003 expected=3003 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```
