# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Arithmetic mean fidelity bar{F} = 0.993866... (99.3867%)",
    "inputs": "f1 = 0.9990, f2 = 0.9956, f3 = 0.9870",
    "formula": "bar{F} = (f1 + f2 + f3) / 3"
  },
  {
    "id": "Q2",
    "statement": "Product fidelity F_prod = 0.9816745428 (98.16745428%)",
    "inputs": "f1 = 0.9990, f2 = 0.9956, f3 = 0.9870",
    "formula": "F_prod = f1 * f2 * f3"
  },
  {
    "id": "Q3",
    "statement": "Gap between mean and product fidelity = 0.0121921238 (about 1.22 percentage points)",
    "inputs": "bar{F} = (f1 + f2 + f3)/3 with f1 = 0.9990, f2 = 0.9956, f3 = 0.9870; F_prod = f1 * f2 * f3",
    "formula": "gap = bar{F} - F_prod"
  }
]

## Script
```python
import math

f1 = 0.9990
f2 = 0.9956
f3 = 0.9870

# Q1
mean = (f1 + f2 + f3) / 3
expected_mean = 0.9938666666666667
match1 = math.isclose(mean, expected_mean, rel_tol=1e-6)
print(f"CLAIM Q1: computed={mean:.10f} expected={expected_mean:.10f} match={'yes' if match1 else 'no'}")

# Q2
prod = f1 * f2 * f3
expected_prod = 0.9816745428
match2 = math.isclose(prod, expected_prod, rel_tol=1e-6)
print(f"CLAIM Q2: computed={prod:.10f} expected={expected_prod:.10f} match={'yes' if match2 else 'no'}")

# Q3
gap = mean - prod
expected_gap = 0.0121921238
match3 = math.isclose(gap, expected_gap, rel_tol=1e-6)
print(f"CLAIM Q3: computed={gap:.10f} expected={expected_gap:.10f} match={'yes' if match3 else 'no'}")

total = 3
matched = sum([match1, match2, match3])
print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {total - matched} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.9938666667 expected=0.9938666667 match=yes
CLAIM Q2: computed=0.9816745428 expected=0.9816745428 match=yes
CLAIM Q3: computed=0.0121921239 expected=0.0121921238 match=yes
VERIFICATION SUMMARY: 3 claims, 3 match, 0 mismatch

[exit 0]
```
