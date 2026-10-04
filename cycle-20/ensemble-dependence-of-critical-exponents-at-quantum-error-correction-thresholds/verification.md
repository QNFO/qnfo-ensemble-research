# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Grand-canonical fidelity F_GC = P(k=0)+P(k=1) = 0.735762 for n=100, p=0.01, t=1",
    "inputs": "n=100, p=0.01, t=1",
    "formula": "F_GC = (1-p)^n + n*p*(1-p)^(n-1)"
  },
  {
    "id": "Q2",
    "statement": "Canonical fidelity F_C = 1.000000 since k = pn = 1 = t",
    "inputs": "n=100, p=0.01, t=1",
    "formula": "F_C = 1 if pn <= t"
  },
  {
    "id": "Q3",
    "statement": "Ensemble gap ΔF = 0.264238",
    "inputs": "F_C=1.000000, F_GC=0.735762",
    "formula": "ΔF = F_C - F_GC"
  },
  {
    "id": "Q4",
    "statement": "Mean error number μ = 1",
    "inputs": "n=100, p=0.01",
    "formula": "μ = n*p"
  },
  {
    "id": "Q5",
    "statement": "Variance σ² = 0.99, σ = 0.994987",
    "inputs": "n=100, p=0.01",
    "formula": "σ² = n*p*(1-p)"
  },
  {
    "id": "Q6",
    "statement": "Relative fluctuation σ/μ = 0.994987, scaling as n^(-1/2)",
    "inputs": "σ=0.994987, μ=1",
    "formula": "σ/μ = sqrt(1-p)/(n*p)^(1/2)"
  },
  {
    "id": "Q7",
    "statement": "Tail mass P(k≥2) = 0.264238",
    "inputs": "F_GC=0.735762",
    "formula": "P(k≥2) = 1 - F_GC"
  },
  {
    "id": "Q8",
    "statement": "Binary entropy h₂(0.01) = 0.0807931 bits/qubit",
    "inputs": "p=0.01",
    "formula": "h₂(p) = -p*log₂(p) - (1-p)*log₂(1-p)"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) and isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1
n, p, t = 100, 0.01, 1
F_GC = (1-p)**n + n*p*(1-p)**(n-1)
results.append(check("Q1", round(F_GC, 6), 0.735762))

# Q2
F_C = 1.0 if n*p <= t else 0.0
results.append(check("Q2", F_C, 1.0))

# Q3
dF = F_C - F_GC
results.append(check("Q3", round(dF, 6), 0.264238))

# Q4
mu = n*p
results.append(check("Q4", mu, 1.0))

# Q5
var = n*p*(1-p)
sigma = math.sqrt(var)
results.append(check("Q5", round(sigma, 6), 0.994987))

# Q6
rel = sigma/mu
results.append(check("Q6", round(rel, 6), 0.994987))

# Q7
tail = 1 - F_GC
results.append(check("Q7", round(tail, 6), 0.264238))

# Q8
h2 = -p*math.log2(p) - (1-p)*math.log2(1-p)
results.append(check("Q8", round(h2, 7), 0.0807931))

print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(results)} match, {len(results)-sum(results)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.735762 expected=0.735762 match=yes
CLAIM Q2: computed=1.0 expected=1.0 match=yes
CLAIM Q3: computed=0.264238 expected=0.264238 match=yes
CLAIM Q4: computed=1.0 expected=1.0 match=yes
CLAIM Q5: computed=0.994987 expected=0.994987 match=yes
CLAIM Q6: computed=0.994987 expected=0.994987 match=yes
CLAIM Q7: computed=0.264238 expected=0.264238 match=yes
CLAIM Q8: computed=0.0807931 expected=0.0807931 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
