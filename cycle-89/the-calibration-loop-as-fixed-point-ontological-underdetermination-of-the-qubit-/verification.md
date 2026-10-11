# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Per-shot readout error probability epsilon_ro = 1 - f_ro",
    "inputs": "f_ro = 0.99991",
    "formula": "epsilon_ro = 1 - f_ro"
  },
  {
    "id": "Q2",
    "statement": "Expected number of misidentifications over 10^6 trials",
    "inputs": "N_trials = 1000000, epsilon_ro = 9e-5",
    "formula": "mu = N_trials * epsilon_ro"
  },
  {
    "id": "Q3",
    "statement": "One-standard-error uncertainty on the readout fidelity over 10^6 trials",
    "inputs": "f_ro = 0.99991, N_trials = 1000000",
    "formula": "sigma_f = sqrt(f_ro * (1 - f_ro) / N_trials)"
  },
  {
    "id": "Q4",
    "statement": "Adaptive-technique error probability",
    "inputs": "f_ad = 0.99999",
    "formula": "epsilon_ad = 1 - f_ad"
  },
  {
    "id": "Q5",
    "statement": "Ratio of adaptive to time-resolved readout error",
    "inputs": "epsilon_ad = 1e-5, epsilon_ro = 9e-5",
    "formula": "ratio = epsilon_ad / epsilon_ro"
  },
  {
    "id": "Q6",
    "statement": "Minimum calibration iterations to reach error below readout noise floor",
    "inputs": "e0 = 0.1, contraction = 0.5, threshold = 9e-5",
    "formula": "k_min = smallest integer k with e0 * contraction**k <= threshold"
  },
  {
    "id": "Q7",
    "statement": "Calibration error after k_min iterations",
    "inputs": "e0 = 0.1, contraction = 0.5, k = 11",
    "formula": "e_k = e0 * contraction**k"
  },
  {
    "id": "Q8",
    "statement": "Total-variation distance under leakage-resolving measurement",
    "inputs": "c2 = 0.01",
    "formula": "D_TV = c2"
  }
]

## Script
```python
import math

f_ro = 0.99991
N_trials = 1_000_000
f_ad = 0.99999
e0 = 0.1
contraction = 0.5
threshold = 9e-5
c2 = 0.01

# Q1
eps_ro = 1 - f_ro
print(f"CLAIM Q1: computed={eps_ro} expected=9e-05 match={math.isclose(eps_ro, 9e-5, rel_tol=1e-6)}")

# Q2
mu = N_trials * eps_ro
print(f"CLAIM Q2: computed={mu} expected=90 match={math.isclose(mu, 90, rel_tol=1e-6)}")

# Q3
sigma_f = math.sqrt(f_ro * (1 - f_ro) / N_trials)
print(f"CLAIM Q3: computed={sigma_f} expected=9.49e-06 match={math.isclose(sigma_f, 9.49e-6, rel_tol=1e-2)}")

# Q4
eps_ad = 1 - f_ad
print(f"CLAIM Q4: computed={eps_ad} expected=1e-05 match={math.isclose(eps_ad, 1e-5, rel_tol=1e-6)}")

# Q5
ratio = eps_ad / eps_ro
print(f"CLAIM Q5: computed={ratio} expected=0.1111111111111111 match={math.isclose(ratio, 1/9, rel_tol=1e-6)}")

# Q6
k = 0
while e0 * contraction**k > threshold:
    k += 1
k_min = k
print(f"CLAIM Q6: computed={k_min} expected=11 match={k_min == 11}")

# Q7
e_k = e0 * contraction**11
print(f"CLAIM Q7: computed={e_k} expected=4.8828125e-05 match={math.isclose(e_k, 4.8828125e-5, rel_tol=1e-6)}")

# Q8
D_TV = c2
print(f"CLAIM Q8: computed={D_TV} expected=0.01 match={math.isclose(D_TV, 0.01, rel_tol=1e-6)}")

results = [
    math.isclose(eps_ro, 9e-5, rel_tol=1e-6),
    math.isclose(mu, 90, rel_tol=1e-6),
    math.isclose(sigma_f, 9.49e-6, rel_tol=1e-2),
    math.isclose(eps_ad, 1e-5, rel_tol=1e-6),
    math.isclose(ratio, 1/9, rel_tol=1e-6),
    k_min == 11,
    math.isclose(e_k, 4.8828125e-5, rel_tol=1e-6),
    math.isclose(D_TV, 0.01, rel_tol=1e-6),
]
print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(results)} match, {len(results)-sum(results)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=9.00000000000345e-05 expected=9e-05 match=True
CLAIM Q2: computed=90.0000000000345 expected=90 match=True
CLAIM Q3: computed=9.486406063416982e-06 expected=9.49e-06 match=True
CLAIM Q4: computed=9.99999999995449e-06 expected=1e-05 match=True
CLAIM Q5: computed=0.11111111111056285 expected=0.1111111111111111 match=True
CLAIM Q6: computed=11 expected=11 match=True
CLAIM Q7: computed=4.8828125e-05 expected=4.8828125e-05 match=True
CLAIM Q8: computed=0.01 expected=0.01 match=True
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
