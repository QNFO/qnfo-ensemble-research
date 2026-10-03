# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Two-round 15-to-1 ladder output error is 1,500,625 p^9; at p = 10^-3 it equals 1.500625e-21",
    "inputs": "per-round coefficient 35; p = 1e-3",
    "formula": "p2 = 35*(35*p^3)^3 = 35^4 * p^9 = 1,500,625 * p^9; at p=1e-3: 1,500,625 * 1e-27 = 1.500625e-21"
  },
  {
    "id": "Q2",
    "statement": "At p = 10^-2 the two-round output error is 1.500625e-12",
    "inputs": "coefficient 35; p = 1e-2",
    "formula": "p2 = 1,500,625 * p^9 = 1,500,625 * 1e-18 = 1.500625e-12"
  },
  {
    "id": "Q3",
    "statement": "Leading-order model validity check: 35 p^2 = 3.5e-3 at p = 10^-2 (valid)",
    "inputs": "coefficient 35; p = 1e-2",
    "formula": "35 * p^2 = 35 * 1e-4 = 3.5e-3"
  },
  {
    "id": "Q4",
    "statement": "Conventional nested two-round factory peak occupancy is 240 qubits",
    "inputs": "block size 15; 15 parallel level-1 blocks",
    "formula": "15 + 15*15 = 15 + 225 = 240"
  },
  {
    "id": "Q5",
    "statement": "Recycled constant-support factory peak occupancy is 30 qubits",
    "inputs": "S = 15; B = 15",
    "formula": "S + B = 15 + 15 = 30"
  },
  {
    "id": "Q6",
    "statement": "Peak occupancy reduction factor is 8.0x",
    "inputs": "baseline 240; recycled 30",
    "formula": "240 / 30 = 8.0"
  },
  {
    "id": "Q7",
    "statement": "Recycling budget: at most 10 reuses keep degradation within 10% of nominal",
    "inputs": "p0 = 1e-3; f = 0.10; delta = 1e-5",
    "formula": "k_max = f * p0 / delta = 0.10 * 1e-3 / 1e-5 = 1e-4 / 1e-5 = 10"
  },
  {
    "id": "Q8",
    "statement": "Sensitivity: k_max = 1 reuse if delta = 1e-4; k_max = 100 reuses if delta = 1e-6",
    "inputs": "f = 0.10; p0 = 1e-3; delta = 1e-4 or 1e-6",
    "formula": "k_max = f * p0 / delta = 1e-4 / delta"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: p2 = 35^4 * p^9 at p=1e-3
coef = 35
p = 1e-3
p2 = coef * (coef * p**3)**3
results.append(check("Q1", p2, 1.500625e-21))

# Q2: at p=1e-2
p = 1e-2
p2 = coef * (coef * p**3)**3
results.append(check("Q2", p2, 1.500625e-12))

# Q3: validity check 35*p^2 at p=1e-2
val = 35 * (1e-2)**2
results.append(check("Q3", val, 3.5e-3))

# Q4: baseline peak occupancy
baseline = 15 + 15 * 15
results.append(check("Q4", baseline, 240))

# Q5: recycled peak occupancy
recycled = 15 + 15
results.append(check("Q5", recycled, 30))

# Q6: reduction factor
factor = baseline / recycled
results.append(check("Q6", factor, 8.0))

# Q7: k_max = f*p0/delta
f, p0, delta = 0.10, 1e-3, 1e-5
kmax = f * p0 / delta
results.append(check("Q7", kmax, 10))

# Q8: sensitivity
k1 = f * p0 / 1e-4
k2 = f * p0 / 1e-6
ok8 = check("Q8a", k1, 1) and check("Q8b", k2, 100)
results.append(ok8)

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.5006250000000003e-21 expected=1.500625e-21 match=yes
CLAIM Q2: computed=1.5006250000000004e-12 expected=1.500625e-12 match=yes
CLAIM Q3: computed=0.0035 expected=0.0035 match=yes
CLAIM Q4: computed=240 expected=240 match=yes
CLAIM Q5: computed=30 expected=30 match=yes
CLAIM Q6: computed=8.0 expected=8.0 match=yes
CLAIM Q7: computed=10.0 expected=10 match=yes
CLAIM Q8a: computed=1.0 expected=1 match=yes
CLAIM Q8b: computed=100.00000000000001 expected=100 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
