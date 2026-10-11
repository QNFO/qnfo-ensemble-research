# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Per-shot error probability p_e = 1 - F = 9e-5",
    "inputs": "F = 0.99991 (readout fidelity from [4])",
    "formula": "p_e = 1 - F"
  },
  {
    "id": "Q2",
    "statement": "Expected wrong outcomes over 10^6 trials: N_err = 90",
    "inputs": "p_e = 9e-5, N_trials = 1e6",
    "formula": "N_err = p_e * N_trials"
  },
  {
    "id": "Q3",
    "statement": "Binomial fluctuation sqrt(N_err) ≈ 9.49",
    "inputs": "N_err = 90",
    "formula": "sqrt(N_err)"
  },
  {
    "id": "Q4",
    "statement": "Tomographic statistical floor sigma_p ≈ 5.00e-3 at N = 10^4 shots, p = 1/2",
    "inputs": "p = 0.5, N = 1e4",
    "formula": "sigma_p = sqrt(p*(1-p)/N)"
  },
  {
    "id": "Q5",
    "statement": "Statistics dominate readout error by factor ≈ 55.6",
    "inputs": "sigma_p = 5.00e-3, p_e = 9e-5",
    "formula": "sigma_p / p_e"
  },
  {
    "id": "Q6",
    "statement": "Crossover shot count N ≈ 3.09e7",
    "inputs": "p = 0.5, p_e = 9e-5",
    "formula": "N = p*(1-p)/p_e^2"
  },
  {
    "id": "Q7",
    "statement": "Convergence rounds n = 14 for L = 0.6, d0 = 1, eps = 1e-3",
    "inputs": "L = 0.6, d0 = 1, eps = 1e-3",
    "formula": "n = ceil(ln(eps/d0)/ln(L))"
  },
  {
    "id": "Q8",
    "statement": "Check 0.6^14 ≈ 7.836e-4 < 1e-3 and 0.6^13 ≈ 1.306e-3 > 1e-3",
    "inputs": "L = 0.6",
    "formula": "L**14 and L**13"
  }
]

## Script
```python
import math

def check(cid, computed, expected, tol=1e-6):
    if expected is None:
        match = None
    else:
        match = math.isclose(computed, expected, rel_tol=tol)
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match

results = []

# Q1: p_e = 1 - F, F = 0.99991
F = 0.99991
p_e = 1 - F
results.append(check("Q1", p_e, 9e-5))

# Q2: N_err = p_e * N_trials, N_trials = 1e6
N_trials = 1e6
N_err = p_e * N_trials
results.append(check("Q2", N_err, 90))

# Q3: sqrt(N_err)
sqrt_err = math.sqrt(N_err)
results.append(check("Q3", sqrt_err, 9.49))

# Q4: sigma_p = sqrt(p*(1-p)/N), p=0.5, N=1e4
p = 0.5
N = 1e4
sigma_p = math.sqrt(p * (1 - p) / N)
results.append(check("Q4", sigma_p, 5.00e-3))

# Q5: sigma_p / p_e
ratio = sigma_p / p_e
results.append(check("Q5", ratio, 55.6))

# Q6: N_cross = p*(1-p)/p_e^2
N_cross = p * (1 - p) / p_e**2
results.append(check("Q6", N_cross, 3.09e7))

# Q7: n = ceil(ln(eps/d0)/ln(L)), L=0.6, d0=1, eps=1e-3
L = 0.6
d0 = 1.0
eps = 1e-3
n_raw = math.log(eps / d0) / math.log(L)
n = math.ceil(n_raw)
results.append(check("Q7", n, 14))

# Q8: L**14 and L**13
L14 = L**14
L13 = L**13
results.append(check("Q8a", L14, 7.836e-4))
results.append(check("Q8b", L13, 1.306e-3))

matched = sum(1 for m in results if m is True)
mismatched = sum(1 for m in results if m is False)
total = len(results)
print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {mismatched} mismatch")

```

## Execution output
```
CLAIM Q1: computed=9.00000000000345e-05 expected=9e-05 match=True
CLAIM Q2: computed=90.0000000000345 expected=90 match=True
CLAIM Q3: computed=9.486832980506957 expected=9.49 match=False
CLAIM Q4: computed=0.005 expected=0.005 match=True
CLAIM Q5: computed=55.55555555553426 expected=55.6 match=False
CLAIM Q6: computed=30864197.530840535 expected=30900000.0 match=False
CLAIM Q7: computed=14 expected=14 match=True
CLAIM Q8a: computed=0.0007836416409599996 expected=0.0007836 match=False
CLAIM Q8b: computed=0.0013060694015999993 expected=0.001306 match=False
VERIFICATION SUMMARY: 9 claims, 4 match, 5 mismatch

[exit 0]
```
