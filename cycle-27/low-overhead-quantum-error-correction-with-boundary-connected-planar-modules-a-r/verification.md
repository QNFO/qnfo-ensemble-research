# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Rotated surface code data qubits at d=22: n_rot(22)=925",
    "inputs": "d=22",
    "formula": "n_rot(d) = 2d^2 - 2d + 1 = 2*484 - 44 + 1 = 925"
  },
  {
    "id": "Q2",
    "statement": "Twelve distance-22 surface-code patches require 11100 data qubits",
    "inputs": "n_rot(22)=925, k=12",
    "formula": "n_SC,12 = 12 * 925 = 11100"
  },
  {
    "id": "Q3",
    "statement": "Surface code total including syndrome qubits at d=22 is ~22200",
    "inputs": "n_SC,12=11100, syndrome ratio 1:1",
    "formula": "total ≈ 2 * 11100 = 22200"
  },
  {
    "id": "Q4",
    "statement": "Rotated surface code data qubits at d=18: 613 per logical, 7356 for 12 logical",
    "inputs": "d=18, k=12",
    "formula": "n_rot(18) = 2*324 - 36 + 1 = 613; 12*613 = 7356"
  },
  {
    "id": "Q5",
    "statement": "Modular memory for 12 logical qubits requires 192 physical qubits",
    "inputs": "rate k/n=1/16, k=12",
    "formula": "n_mod = 16k = 12*16 = 192"
  },
  {
    "id": "Q6",
    "statement": "Overhead reduction vs surface code at d=22 is 57.8x",
    "inputs": "n_SC,12=11100, n_mod=192",
    "formula": "11100/192 = 57.8125"
  },
  {
    "id": "Q7",
    "statement": "Reduction stays >=30x provided modular implementation uses <=370 qubits",
    "inputs": "n_SC,12=11100, factor=30",
    "formula": "n_mod <= 11100/30 = 370"
  },
  {
    "id": "Q8",
    "statement": "Overhead reduction vs surface code at d=18 baseline is 38.3x",
    "inputs": "n_SC,12(d=18)=7356, n_mod=192",
    "formula": "7356/192 = 38.3125"
  }
]

## Script
```python
import math

def check(id, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        try:
            match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
        except (TypeError, ValueError):
            match = "yes" if computed == expected else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {id}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: n_rot(22) = 2*22^2 - 2*22 + 1
d = 22
n_rot_22 = 2 * d**2 - 2 * d + 1
results.append(check("Q1", n_rot_22, 925))

# Q2: 12 patches at d=22
n_SC_12_22 = 12 * n_rot_22
results.append(check("Q2", n_SC_12_22, 11100))

# Q3: total with syndrome qubits ~ 2 * 11100
total_22 = 2 * n_SC_12_22
results.append(check("Q3", total_22, 22200))

# Q4: n_rot(18) and 12 patches at d=18
d18 = 18
n_rot_18 = 2 * d18**2 - 2 * d18 + 1
n_SC_12_18 = 12 * n_rot_18
results.append(check("Q4", n_SC_12_18, 7356))

# Q5: modular memory n_mod = 16k, k=12
k = 12
n_mod = 16 * k
results.append(check("Q5", n_mod, 192))

# Q6: overhead reduction vs d=22 baseline
ratio_22 = n_SC_12_22 / n_mod
results.append(check("Q6", ratio_22, 57.8125))

# Q7: n_mod bound for >=30x
bound = n_SC_12_22 / 30
results.append(check("Q7", bound, 370))

# Q8: overhead reduction vs d=18 baseline
ratio_18 = n_SC_12_18 / n_mod
results.append(check("Q8", ratio_18, 38.3125))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=925 expected=925 match=yes
CLAIM Q2: computed=11100 expected=11100 match=yes
CLAIM Q3: computed=22200 expected=22200 match=yes
CLAIM Q4: computed=7356 expected=7356 match=yes
CLAIM Q5: computed=192 expected=192 match=yes
CLAIM Q6: computed=57.8125 expected=57.8125 match=yes
CLAIM Q7: computed=370.0 expected=370 match=yes
CLAIM Q8: computed=38.3125 expected=38.3125 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
