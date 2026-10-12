# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "E_F at p=0.5 equals 1.000000 ebits",
    "inputs": "p=0.5, lambda_max=0.5",
    "formula": "E_F = -lambda_max*log2(lambda_max) - (1-lambda_max)*log2(1-lambda_max)"
  },
  {
    "id": "Q2",
    "statement": "E_F at p=0.25 equals 0.811278 ebits",
    "inputs": "p=0.25, lambda_max=0.75",
    "formula": "E_F = -0.75*log2(0.75) - 0.25*log2(0.25)"
  },
  {
    "id": "Q3",
    "statement": "E_F at p=0.9 equals 0.468996 ebits",
    "inputs": "p=0.9, lambda_max=0.9",
    "formula": "E_F = -0.9*log2(0.9) - 0.1*log2(0.1)"
  },
  {
    "id": "Q4",
    "statement": "dE_F/dp at p=0.5 equals 0",
    "inputs": "p=0.5",
    "formula": "dE_F/dp = log2((1-p)/p)"
  },
  {
    "id": "Q5",
    "statement": "Representation overhead R_10 = 1024",
    "inputs": "n=10",
    "formula": "R_n = 4^n / 2^n = 2^n"
  },
  {
    "id": "Q6",
    "statement": "Pure-state storage at n=10 is 16384 bytes (16 KiB)",
    "inputs": "n=10, 16 bytes per complex amplitude",
    "formula": "bytes = 2^n * 16"
  },
  {
    "id": "Q7",
    "statement": "Density-matrix storage at n=10 is 16777216 bytes (16 MiB)",
    "inputs": "n=10, 16 bytes per complex amplitude",
    "formula": "bytes = 4^n * 16"
  },
  {
    "id": "Q8",
    "statement": "Sweep footprint M_sweep = 352321536 bytes (~352 MB)",
    "inputs": "K=21, n=10, 16 bytes per entry",
    "formula": "M_sweep = K * 4^n * 16"
  }
]

## Script
```python
import math

def log2(x):
    return math.log(x) / math.log(2)

def h2(mu):
    if mu in (0.0, 1.0):
        return 0.0
    return -mu * log2(mu) - (1 - mu) * log2(1 - mu)

claims = []

# Q1
computed = h2(0.5)
claims.append(("Q1", computed, 1.000000))

# Q2
computed = -0.75 * log2(0.75) - 0.25 * log2(0.25)
claims.append(("Q2", computed, 0.811278))

# Q3
computed = -0.9 * log2(0.9) - 0.1 * log2(0.1)
claims.append(("Q3", computed, 0.468996))

# Q4
computed = log2((1 - 0.5) / 0.5)
claims.append(("Q4", computed, 0.0))

# Q5
n = 10
computed = (4 ** n) / (2 ** n)
claims.append(("Q5", computed, 1024))

# Q6
computed = (2 ** n) * 16
claims.append(("Q6", computed, 16384))

# Q7
computed = (4 ** n) * 16
claims.append(("Q7", computed, 16777216))

# Q8
K = 21
computed = K * (4 ** n) * 16
claims.append(("Q8", computed, 352321536))

match_count = 0
for cid, computed, expected in claims:
    if expected is None:
        match = "no"
    else:
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

mismatch = len(claims) - match_count
print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {mismatch} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.0 expected=1.0 match=yes
CLAIM Q2: computed=0.8112781244591328 expected=0.811278 match=yes
CLAIM Q3: computed=0.4689955935892812 expected=0.468996 match=yes
CLAIM Q4: computed=0.0 expected=0.0 match=yes
CLAIM Q5: computed=1024.0 expected=1024 match=yes
CLAIM Q6: computed=16384 expected=16384 match=yes
CLAIM Q7: computed=16777216 expected=16777216 match=yes
CLAIM Q8: computed=352321536 expected=352321536 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
