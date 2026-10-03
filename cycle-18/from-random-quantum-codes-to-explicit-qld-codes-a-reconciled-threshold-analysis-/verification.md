# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Binary entropy at radius 0.1 is H2(0.1) = 0.468996 bits",
    "inputs": "rho = 0.1",
    "formula": "H2(rho) = -rho*log2(rho) - (1-rho)*log2(1-rho)"
  },
  {
    "id": "Q2",
    "statement": "Classical (and per-sector quantum) list-decoding threshold at radius 0.1 is R* = 0.5310",
    "inputs": "H2(0.1) = 0.468996",
    "formula": "R* = 1 - H2(0.1)"
  },
  {
    "id": "Q3",
    "statement": "Total CSS code rate for per-sector rates R_X = R_Z = 0.3 is R = 0.4",
    "inputs": "R_X = 0.3, R_Z = 0.3",
    "formula": "R = 1 - R_X - R_Z"
  },
  {
    "id": "Q4",
    "statement": "Per-sector slack below threshold is 0.2310 in each sector",
    "inputs": "R* = 0.5310, R_X = 0.3",
    "formula": "slack = R* - R_X"
  },
  {
    "id": "Q5",
    "statement": "At n = 100,000 with R_X = R_Z = 0.3, the code has k = 40,000 logical qubits",
    "inputs": "n = 100000, R_X = 0.3, R_Z = 0.3",
    "formula": "k = n - R_X*n - R_Z*n"
  },
  {
    "id": "Q6",
    "statement": "Gap to capacity at R = 0.4, rho = 0.1 is epsilon = 0.1310",
    "inputs": "R = 0.4, H2(0.1) = 0.468996",
    "formula": "epsilon = 1 - R - H2(0.1)"
  },
  {
    "id": "Q7",
    "statement": "List size at R = 0.4, rho = 0.1 is L ≈ 16",
    "inputs": "epsilon = 0.1310",
    "formula": "L = ceil(2/epsilon)"
  },
  {
    "id": "Q8",
    "statement": "Fixed-list-size threshold for L = 2 at p = 0.1 is R*_2 = 0.031004",
    "inputs": "H2(0.1) = 0.468996, L = 2",
    "formula": "R*_L = 1 - H2(p) - 1/L"
  }
]

## Script
```python
import math

def H2(p):
    return -p*math.log2(p) - (1-p)*math.log2(1-p)

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

# Q1
h = H2(0.1)
results.append(check("Q1", round(h, 6), 0.468996))

# Q2
rstar = 1 - h
results.append(check("Q2", round(rstar, 4), 0.5310))

# Q3
R = 1 - 0.3 - 0.3
results.append(check("Q3", round(R, 6), 0.4))

# Q4
slack = rstar - 0.3
results.append(check("Q4", round(slack, 4), 0.2310))

# Q5
k = 100000 - 0.3*100000 - 0.3*100000
results.append(check("Q5", int(round(k)), 40000))

# Q6
eps = 1 - 0.4 - h
results.append(check("Q6", round(eps, 4), 0.1310))

# Q7
L = math.ceil(2/eps)
results.append(check("Q7", L, 16))

# Q8
r2 = 1 - h - 1/2
results.append(check("Q8", round(r2, 6), 0.031004))

print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(results)} match, {len(results)-sum(results)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.468996 expected=0.468996 match=yes
CLAIM Q2: computed=0.531 expected=0.531 match=yes
CLAIM Q3: computed=0.4 expected=0.4 match=yes
CLAIM Q4: computed=0.231 expected=0.231 match=yes
CLAIM Q5: computed=40000 expected=40000 match=yes
CLAIM Q6: computed=0.131 expected=0.131 match=yes
CLAIM Q7: computed=16 expected=16 match=yes
CLAIM Q8: computed=0.031004 expected=0.031004 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
