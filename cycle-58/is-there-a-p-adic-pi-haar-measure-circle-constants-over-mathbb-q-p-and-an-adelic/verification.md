# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "kappa_p = 1 - 1/p^2, e.g. kappa_2 = 0.75",
    "inputs": "p=2",
    "formula": "1 - 1/p^2"
  },
  {
    "id": "Q2",
    "statement": "kappa_3 = 8/9 ≈ 0.888889",
    "inputs": "p=3",
    "formula": "1 - 1/p^2"
  },
  {
    "id": "Q3",
    "statement": "kappa_5 = 24/25 = 0.96",
    "inputs": "p=5",
    "formula": "1 - 1/p^2"
  },
  {
    "id": "Q4",
    "statement": "kappa_7 = 48/49 ≈ 0.979592",
    "inputs": "p=7",
    "formula": "1 - 1/p^2"
  },
  {
    "id": "Q5",
    "statement": "kappa_11 = 120/121 ≈ 0.991736",
    "inputs": "p=11",
    "formula": "1 - 1/p^2"
  },
  {
    "id": "Q6",
    "statement": "kappa'_p = (1 - 1/p^2)/2, e.g. kappa'_2 = 0.375",
    "inputs": "p=2",
    "formula": "(1 - 1/p^2)/2"
  },
  {
    "id": "Q7",
    "statement": "kappa'_3 ≈ 0.444444",
    "inputs": "p=3",
    "formula": "(1 - 1/p^2)/2"
  },
  {
    "id": "Q8",
    "statement": "kappa'_5 = 0.48",
    "inputs": "p=5",
    "formula": "(1 - 1/p^2)/2"
  }
]

## Script
```python
import math

claims = [
    ("Q1", 2, 1 - 1/pow(2,2), 0.75),
    ("Q2", 3, 1 - 1/pow(3,2), 8/9),
    ("Q3", 5, 1 - 1/pow(5,2), 24/25),
    ("Q4", 7, 1 - 1/pow(7,2), 48/49),
    ("Q5", 11, 1 - 1/pow(11,2), 120/121),
    ("Q6", 2, (1 - 1/pow(2,2))/2, 0.375),
    ("Q7", 3, (1 - 1/pow(3,2))/2, 4/9),
    ("Q8", 5, (1 - 1/pow(5,2))/2, 0.48),
]

match_count = 0
for cid, p, computed, expected in claims:
    match = math.isclose(computed, expected, rel_tol=1e-6)
    if match:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed:.6f} expected={expected:.6f} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.750000 expected=0.750000 match=yes
CLAIM Q2: computed=0.888889 expected=0.888889 match=yes
CLAIM Q3: computed=0.960000 expected=0.960000 match=yes
CLAIM Q4: computed=0.979592 expected=0.979592 match=yes
CLAIM Q5: computed=0.991736 expected=0.991736 match=yes
CLAIM Q6: computed=0.375000 expected=0.375000 match=yes
CLAIM Q7: computed=0.444444 expected=0.444444 match=yes
CLAIM Q8: computed=0.480000 expected=0.480000 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
