# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Pure dephasing rate gamma_phi = 10^4 s^-1 from T2 = 100 microseconds",
    "inputs": "T2 = 100e-6 s",
    "formula": "gamma_phi = 1/T2"
  },
  {
    "id": "Q2",
    "statement": "Energy relaxation rate gamma_1 = 10^2 s^-1 from T1 = 10 ms",
    "inputs": "T1 = 10e-3 s",
    "formula": "gamma_1 = 1/T1"
  },
  {
    "id": "Q3",
    "statement": "Hierarchy ratio R = 100",
    "inputs": "gamma_phi = 1e4 s^-1, gamma_1 = 1e2 s^-1",
    "formula": "R = gamma_phi/gamma_1"
  },
  {
    "id": "Q4",
    "statement": "Suppressed dephasing rate gamma_phi' = 10^2 s^-1 at S = 100",
    "inputs": "gamma_phi = 1e4 s^-1, S = 100",
    "formula": "gamma_phi' = gamma_phi/S"
  },
  {
    "id": "Q5",
    "statement": "Per-DTU relaxation probability p1 = 1e-4 per cycle",
    "inputs": "gamma_1 = 1e2 s^-1, tau = 1e-6 s",
    "formula": "p1 = gamma_1 * tau"
  },
  {
    "id": "Q6",
    "statement": "Per-DTU residual dephasing probability p_Z = 1e-4 per cycle at S = R",
    "inputs": "gamma_phi' = 1e2 s^-1, tau = 1e-6 s",
    "formula": "p_Z = gamma_phi' * tau"
  },
  {
    "id": "Q7",
    "statement": "Repetition-code logical failure probability from relaxation pairs p_L^X = 2.9998e-8 per cycle",
    "inputs": "p1 = 1e-4",
    "formula": "p_L^X = C(3,2)*p1^2*(1-p1) + C(3,3)*p1^3 = 3*p1^2*(1-p1) + p1^3"
  },
  {
    "id": "Q8",
    "statement": "Residual single-Z contribution p_L^Z ≈ 2.9997e-4 per cycle at S = R",
    "inputs": "p_Z = 1e-4",
    "formula": "p_L^Z = 1 - (1-p_Z)^3 ≈ 3*p_Z"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1
T2 = 100e-6
gamma_phi = 1 / T2
results.append(check("Q1", gamma_phi, 1e4))

# Q2
T1 = 10e-3
gamma_1 = 1 / T1
results.append(check("Q2", gamma_1, 1e2))

# Q3
R = gamma_phi / gamma_1
results.append(check("Q3", R, 100))

# Q4
S = 100
gamma_phi_p = gamma_phi / S
results.append(check("Q4", gamma_phi_p, 1e2))

# Q5
tau = 1e-6
p1 = gamma_1 * tau
results.append(check("Q5", p1, 1e-4))

# Q6
p_Z = gamma_phi_p * tau
results.append(check("Q6", p_Z, 1e-4))

# Q7
pLX = 3 * p1**2 * (1 - p1) + p1**3
results.append(check("Q7", pLX, 2.9998e-8))

# Q8
pLZ = 1 - (1 - p_Z)**3
results.append(check("Q8", pLZ, 2.9997e-4))

print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(results)} match, {len(results)-sum(results)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=10000.0 expected=10000.0 match=yes
CLAIM Q2: computed=100.0 expected=100.0 match=yes
CLAIM Q3: computed=100.0 expected=100 match=yes
CLAIM Q4: computed=100.0 expected=100.0 match=yes
CLAIM Q5: computed=9.999999999999999e-05 expected=0.0001 match=yes
CLAIM Q6: computed=9.999999999999999e-05 expected=0.0001 match=yes
CLAIM Q7: computed=2.9998e-08 expected=2.9998e-08 match=yes
CLAIM Q8: computed=0.00029997000100001614 expected=0.00029997 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
