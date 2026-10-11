# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Number of pairwise translation maps for N=29 frameworks is 406",
    "inputs": "N=29",
    "formula": "C(N,2) = N*(N-1)/2"
  },
  {
    "id": "Q2",
    "statement": "Number of composition constraints for N=29 frameworks is 3654",
    "inputs": "N=29",
    "formula": "C(N,3) = N*(N-1)*(N-2)/6"
  },
  {
    "id": "Q3",
    "statement": "Constraint-to-map ratio is exactly 9.0",
    "inputs": "N=29",
    "formula": "C(N,3)/C(N,2) = (N-2)/3"
  },
  {
    "id": "Q4",
    "statement": "Under factor-2 reading N=58: 1653 maps and 30856 constraints, ratio 18.667",
    "inputs": "N=58",
    "formula": "C(58,2)=1653; C(58,3)=30856; ratio=(58-2)/3"
  },
  {
    "id": "Q5",
    "statement": "Unordered pairwise translations among 7 domains is 21 (directed 42)",
    "inputs": "n=7",
    "formula": "C(7,2)=21; directed=7*6=42"
  },
  {
    "id": "Q6",
    "statement": "At least 8 schisms lie outside the seven-domain pairwise relations",
    "inputs": "N_schism=29, P=21",
    "formula": "N_schism - P = 29 - 21 = 8"
  },
  {
    "id": "Q7",
    "statement": "Closure error bound for three-edge cycle with errors 1e-3, 2e-3, 5e-4 is 3.4965e-3",
    "inputs": "eps12=0.001, eps23=0.002, eps31=0.0005",
    "formula": "Delta = 1 - (1-eps12)*(1-eps23)*(1-eps31)"
  },
  {
    "id": "Q8",
    "statement": "Additive first-order bound for the same cycle is 3.5e-3",
    "inputs": "eps12=0.001, eps23=0.002, eps31=0.0005",
    "formula": "eps12 + eps23 + eps31"
  }
]

## Script
```python
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

```

## Execution output
```
CLAIM Q1: computed=406 expected=406 match=yes
CLAIM Q2: computed=3654 expected=3654 match=yes
CLAIM Q3: computed=9.0 expected=9.0 match=yes
CLAIM Q4a: computed=1653 expected=1653 match=yes
CLAIM Q4b: computed=30856 expected=30856 match=yes
CLAIM Q4c: computed=18.666666666666668 expected=18.666666666666668 match=yes
CLAIM Q5a: computed=21 expected=21 match=yes
CLAIM Q5b: computed=42 expected=42 match=yes
CLAIM Q6: computed=8 expected=8 match=yes
CLAIM Q7: computed=0.003496500999999985 expected=0.0034965 match=yes
CLAIM Q8: computed=0.0035 expected=0.0035 match=yes
VERIFICATION SUMMARY: 11 claims, 11 match, 0 mismatch

[exit 0]
```
