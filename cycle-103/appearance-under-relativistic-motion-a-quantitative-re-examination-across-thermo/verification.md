# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Lorentz factor at beta_1 = 0.8 is gamma_1 = 5/3 ≈ 1.666667",
    "inputs": "beta_1 = 0.8",
    "formula": "gamma_1 = 1/sqrt(1 - beta_1^2)"
  },
  {
    "id": "Q2",
    "statement": "Approach Doppler factor D+ = 3 at beta_1 = 0.8",
    "inputs": "beta_1 = 0.8, gamma_1 = 5/3",
    "formula": "D+ = 1/(gamma_1*(1 - beta_1))"
  },
  {
    "id": "Q3",
    "statement": "Recede Doppler factor D- = 1/3 at beta_1 = 0.8",
    "inputs": "beta_1 = 0.8, gamma_1 = 5/3",
    "formula": "D- = 1/(gamma_1*(1 + beta_1))"
  },
  {
    "id": "Q4",
    "statement": "Transverse Doppler factor D_perp = 0.6 at beta_1 = 0.8",
    "inputs": "beta_1 = 0.8, gamma_1 = 5/3",
    "formula": "D_perp = 1/gamma_1"
  },
  {
    "id": "Q5",
    "statement": "Cooler-branch temperature transformation T_cool = 0.6*T_0 at beta_1 = 0.8",
    "inputs": "beta_1 = 0.8, gamma_1 = 5/3",
    "formula": "T_cool = T_0/gamma_1"
  },
  {
    "id": "Q6",
    "statement": "Hotter-branch temperature transformation T_hot = 1.666667*T_0 at beta_1 = 0.8",
    "inputs": "beta_1 = 0.8, gamma_1 = 5/3",
    "formula": "T_hot = gamma_1*T_0"
  },
  {
    "id": "Q7",
    "statement": "Ratio of the two temperature candidates gamma_1^2 = 25/9 ≈ 2.777778",
    "inputs": "gamma_1 = 5/3",
    "formula": "gamma_1^2"
  },
  {
    "id": "Q8",
    "statement": "Cross-check at beta = 0.6: gamma = 1.25 and T' = 0.8*T_0; for T_0 = 300 K, T' = 240 K",
    "inputs": "beta = 0.6, T_0 = 300 K",
    "formula": "gamma = 1/sqrt(1 - beta^2); T' = T_0/gamma"
  }
]

## Script
```python
import math
from fractions import Fraction

def check(cid, computed, expected):
    if expected is None:
        match = "n/a"
    else:
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match

results = []

# Q1: gamma_1 = 1/sqrt(1 - 0.8^2)
beta1 = 0.8
g1 = 1.0 / math.sqrt(1.0 - beta1**2)
results.append(check("Q1", g1, 5.0/3.0))

# Q2: D+ = 1/(gamma_1*(1 - beta_1))
Dp = 1.0 / (g1 * (1.0 - beta1))
results.append(check("Q2", Dp, 3.0))

# Q3: D- = 1/(gamma_1*(1 + beta_1))
Dm = 1.0 / (g1 * (1.0 + beta1))
results.append(check("Q3", Dm, 1.0/3.0))

# Q4: D_perp = 1/gamma_1
Dperp = 1.0 / g1
results.append(check("Q4", Dperp, 0.6))

# Q5: T_cool = T_0/gamma_1 (in units of T_0)
Tcool = 1.0 / g1
results.append(check("Q5", Tcool, 0.6))

# Q6: T_hot = gamma_1*T_0 (in units of T_0)
Thot = g1
results.append(check("Q6", Thot, 1.666667))

# Q7: gamma_1^2 = 25/9
g1sq = g1**2
results.append(check("Q7", g1sq, 25.0/9.0))

# Q8: beta = 0.6: gamma = 1/sqrt(1-0.36); T' = 300/gamma
b = 0.6
g = 1.0 / math.sqrt(1.0 - b**2)
T0 = 300.0
Tp = T0 / g
results.append(check("Q8a", g, 1.25))
results.append(check("Q8b", Tp, 240.0))

n = len(results)
m = sum(1 for r in results if r == "yes")
k = sum(1 for r in results if r == "no")
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.666666666666667 expected=1.6666666666666667 match=yes
CLAIM Q2: computed=3.0 expected=3.0 match=yes
CLAIM Q3: computed=0.33333333333333326 expected=0.3333333333333333 match=yes
CLAIM Q4: computed=0.5999999999999999 expected=0.6 match=yes
CLAIM Q5: computed=0.5999999999999999 expected=0.6 match=yes
CLAIM Q6: computed=1.666666666666667 expected=1.666667 match=yes
CLAIM Q7: computed=2.7777777777777786 expected=2.7777777777777777 match=yes
CLAIM Q8a: computed=1.25 expected=1.25 match=yes
CLAIM Q8b: computed=240.0 expected=240.0 match=yes
VERIFICATION SUMMARY: 9 claims, 9 match, 0 mismatch

[exit 0]
```
