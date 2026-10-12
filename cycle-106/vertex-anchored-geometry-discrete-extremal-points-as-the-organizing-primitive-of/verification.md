# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Ball counts in a q-homogeneous ultrametric tree satisfy N_k = q^k (e.g. N_5 = 243 for q=3, N_20 = 1048576 for q=2)",
    "inputs": "branching factor q (q=3 for first example, q=2 for second); recurrence N_0 = 1, N_{k+1} = q*N_k",
    "formula": "N_k = q^k"
  },
  {
    "id": "Q2",
    "statement": "Apparent size at shell k is s_k = (S/d_0) q^k, so adjacent shells differ by ratio q",
    "inputs": "object size S, reference distance d_0, branching factor q, shell index k; admissible distances d_k = d_0 * q^{-k}",
    "formula": "s_k = S / d_k = (S/d_0) * q^k; ratio s_{k+1}/s_k = q"
  },
  {
    "id": "Q3",
    "statement": "Number of lines of a d-dimensional order-n polystochastic array is L(n,d) = d*n^{d-1}, with L(4,3) = 48 and L(3,4) = 108",
    "inputs": "order n (4 then 3), dimension d (3 then 4)",
    "formula": "L(n,d) = d * n^(d-1)"
  },
  {
    "id": "Q4",
    "statement": "Total (entry, line) incidences equal d*n^d; for (n,d)=(4,3) this is 192 = 48*4",
    "inputs": "n=4, d=3, L(4,3)=48",
    "formula": "incidences = d * n^d = L(n,d) * n"
  }
]

## Script
```python
import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: N_k = q^k via recurrence N_0=1, N_{k+1}=q*N_k
def ball_count(q, k):
    N = 1
    for _ in range(k):
        N = q * N
    return N

N5_q3 = ball_count(3, 5)
N20_q2 = ball_count(2, 20)
results.append(("Q1a", N5_q3, 243))
results.append(("Q1b", N20_q2, 1048576))

# Q2: s_k = (S/d_0)*q^k, ratio s_{k+1}/s_k = q
S = 10.0
d0 = 5.0
q = 3.0
k = 4
s_k = (S / d0) * (q ** k)
s_k1 = (S / d0) * (q ** (k + 1))
ratio = s_k1 / s_k
results.append(("Q2a", s_k, (S / d0) * (q ** k)))
results.append(("Q2b", ratio, q))

# Q3: L(n,d) = d * n^(d-1)
L43 = 3 * (4 ** 2)
L34 = 4 * (3 ** 3)
results.append(("Q3a", L43, 48))
results.append(("Q3b", L34, 108))

# Q4: incidences = d * n^d = L(n,d) * n
incidences_direct = 3 * (4 ** 3)
incidences_via_L = L43 * 4
results.append(("Q4a", incidences_direct, 192))
results.append(("Q4b", incidences_via_L, 192))

match_count = 0
for cid, computed, expected in results:
    match = close(float(computed), float(expected))
    if match:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

total = len(results)
mismatch = total - match_count
print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {mismatch} mismatch")

```

## Execution output
```
CLAIM Q1a: computed=243 expected=243 match=yes
CLAIM Q1b: computed=1048576 expected=1048576 match=yes
CLAIM Q2a: computed=162.0 expected=162.0 match=yes
CLAIM Q2b: computed=3.0 expected=3.0 match=yes
CLAIM Q3a: computed=48 expected=48 match=yes
CLAIM Q3b: computed=108 expected=108 match=yes
CLAIM Q4a: computed=192 expected=192 match=yes
CLAIM Q4b: computed=192 expected=192 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
