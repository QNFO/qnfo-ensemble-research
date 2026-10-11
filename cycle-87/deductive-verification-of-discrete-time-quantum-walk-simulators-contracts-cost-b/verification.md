# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "State-vector dimension at t=1000 is d_t = 4002",
    "inputs": "d_c=2, t=1000",
    "formula": "d_t = 2*(2*t+1)"
  },
  {
    "id": "Q2",
    "statement": "State-vector dimension at t=10^6 is d_t = 4,000,002",
    "inputs": "d_c=2, t=1000000",
    "formula": "d_t = 2*(2*t+1)"
  },
  {
    "id": "Q3",
    "statement": "Dense unitarity-check cost at t=1000 is 64,096,048,008 multiply-adds",
    "inputs": "d_t=4002",
    "formula": "d_t^3"
  },
  {
    "id": "Q4",
    "statement": "Projected dense-check time is 64.096 s at rate r=10^9 multiply-adds/s",
    "inputs": "d_t^3=64096048008, r=1e9",
    "formula": "T_dense = d_t^3 / r"
  },
  {
    "id": "Q5",
    "statement": "Sparse unitarity-check cost is 64,064,016 multiply-adds",
    "inputs": "d_t=4002, k=2",
    "formula": "k^2 * d_t^2 = 4*d_t^2"
  },
  {
    "id": "Q6",
    "statement": "Sparse-over-dense speedup factor is 1000.5",
    "inputs": "d_t=4002",
    "formula": "d_t / 4"
  },
  {
    "id": "Q7",
    "statement": "Row-norm check costs 32,016 multiply-adds",
    "inputs": "d_t=4002",
    "formula": "8*d_t"
  },
  {
    "id": "Q8",
    "statement": "Unitarity constraint count is 16,020,006",
    "inputs": "d_t=4002",
    "formula": "d_t*(d_t+1)"
  }
]

## Script
```python
import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

# Q1: d_t = 2*(2*t+1), t=1000
t1 = 1000
q1 = 2 * (2 * t1 + 1)
print(f"CLAIM Q1: computed={q1} expected=4002 match={'yes' if isclose(q1, 4002) else 'no'}")

# Q2: d_t = 2*(2*t+1), t=10^6
t2 = 10**6
q2 = 2 * (2 * t2 + 1)
print(f"CLAIM Q2: computed={q2} expected=4000002 match={'yes' if isclose(q2, 4000002) else 'no'}")

# Q3: dense unitarity cost = d_t^3, d_t=4002
d = 4002
q3 = d**3
print(f"CLAIM Q3: computed={q3} expected=64096048008 match={'yes' if isclose(q3, 64096048008) else 'no'}")

# Q4: T_dense = d_t^3 / r, r=1e9
r = 1e9
q4 = q3 / r
print(f"CLAIM Q4: computed={q4} expected=64.096048008 match={'yes' if isclose(q4, 64.096048008) else 'no'}")

# Q5: sparse cost = k^2 * d_t^2, k=2
k = 2
q5 = k**2 * d**2
print(f"CLAIM Q5: computed={q5} expected=64064016 match={'yes' if isclose(q5, 64064016) else 'no'}")

# Q6: speedup = d_t / 4
q6 = d / 4
print(f"CLAIM Q6: computed={q6} expected=1000.5 match={'yes' if isclose(q6, 1000.5) else 'no'}")

# Q7: row-norm check = 8*d_t
q7 = 8 * d
print(f"CLAIM Q7: computed={q7} expected=32016 match={'yes' if isclose(q7, 32016) else 'no'}")

# Q8: constraint count = d_t*(d_t+1)
q8 = d * (d + 1)
print(f"CLAIM Q8: computed={q8} expected=16020006 match={'yes' if isclose(q8, 16020006) else 'no'}")

matches = sum([
    isclose(q1, 4002), isclose(q2, 4000002), isclose(q3, 64096048008),
    isclose(q4, 64.096048008), isclose(q5, 64064016), isclose(q6, 1000.5),
    isclose(q7, 32016), isclose(q8, 16020006)
])
print(f"VERIFICATION SUMMARY: 8 claims, {matches} match, {8 - matches} mismatch")

```

## Execution output
```
CLAIM Q1: computed=4002 expected=4002 match=yes
CLAIM Q2: computed=4000002 expected=4000002 match=yes
CLAIM Q3: computed=64096048008 expected=64096048008 match=yes
CLAIM Q4: computed=64.096048008 expected=64.096048008 match=yes
CLAIM Q5: computed=64064016 expected=64064016 match=yes
CLAIM Q6: computed=1000.5 expected=1000.5 match=yes
CLAIM Q7: computed=32016 expected=32016 match=yes
CLAIM Q8: computed=16020006 expected=16020006 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
