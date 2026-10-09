# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Parent total quantum dimension squared for Ising x anti-Ising is D_C^2 = 16",
    "inputs": "d_(1,1)=1, d_(1,sigma-bar)=(sqrt(2))^2=2, d_(1,psi-bar)=1, d_(sigma,1)=2, d_(sigma,sigma-bar)=2^2=4, d_(sigma,psi-bar)=2, d_(psi,1)=1, d_(psi,sigma-bar)=2, d_(psi,psi-bar)=1",
    "formula": "D_C^2 = 1+2+1+2+4+2+1+2+1"
  },
  {
    "id": "Q2",
    "statement": "D_C^2 via product of factors equals 16",
    "inputs": "D_Ising^2 = 1^2+(sqrt(2))^2+1^2 = 4, D_antiIsing^2 = 4",
    "formula": "D_C^2 = 4*4"
  },
  {
    "id": "Q3",
    "statement": "Child total quantum dimension squared D_D^2 = 4",
    "inputs": "four child simples each with d=1",
    "formula": "D_D^2 = 1^2+1^2+1^2+1^2"
  },
  {
    "id": "Q4",
    "statement": "Dimension ratio kappa = 4",
    "inputs": "D_C^2=16, D_D^2=4",
    "formula": "kappa = D_C^2/D_D^2"
  },
  {
    "id": "Q5",
    "statement": "Child-side non-Abelian fraction f_NA = 0",
    "inputs": "N_NA^D=0, N_tot^D=4",
    "formula": "f_NA = 0/4"
  },
  {
    "id": "Q6",
    "statement": "Parent-side non-Abelian weight fraction f_NA^(parent) = 1/2",
    "inputs": "(sqrt(2))^2=2, (sqrt(2))^2=2, 2^2=4, D_C^2=16",
    "formula": "f_NA^(parent) = (2+2+4)/16"
  },
  {
    "id": "Q7",
    "statement": "Chirality index mu = 0 for Case III",
    "inputs": "c_C = 1/2 + (-1/2) = 0, c_D = 0",
    "formula": "mu = 2*(c_C - c_D)"
  },
  {
    "id": "Q8",
    "statement": "Anchor point nu=0: mu = 0",
    "inputs": "c_toric = 0",
    "formula": "mu = 2*0"
  }
]

## Script
```python
import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: D_C^2 = 1+2+1+2+4+2+1+2+1 = 16
terms = [1, 2, 1, 2, 4, 2, 1, 2, 1]
q1 = sum(terms)
results.append(("Q1", q1, 16))

# Q2: D_C^2 = D_Ising^2 * D_antiIsing^2 = 4*4 = 16
d_ising_sq = 1**2 + (math.sqrt(2))**2 + 1**2
d_anti_sq = 1**2 + (math.sqrt(2))**2 + 1**2
q2 = d_ising_sq * d_anti_sq
results.append(("Q2", q2, 16))

# Q3: D_D^2 = 1^2+1^2+1^2+1^2 = 4
q3 = sum(1**2 for _ in range(4))
results.append(("Q3", q3, 4))

# Q4: kappa = D_C^2 / D_D^2 = 16/4 = 4
q4 = 16 / 4
results.append(("Q4", q4, 4))

# Q5: f_NA = 0/4 = 0
q5 = 0 / 4
results.append(("Q5", q5, 0))

# Q6: f_NA^(parent) = (2+2+4)/16 = 8/16 = 0.5
num = (math.sqrt(2))**2 + (math.sqrt(2))**2 + 2**2
q6 = num / 16
results.append(("Q6", q6, 0.5))

# Q7: mu = 2*(c_C - c_D), c_C = 1/2 + (-1/2) = 0, c_D = 0 -> mu = 0
c_C = 1/2 + (-1/2)
c_D = 0
q7 = 2 * (c_C - c_D)
results.append(("Q7", q7, 0))

# Q8: nu=0 anchor: mu = 2*0 = 0
c_toric = 0
q8 = 2 * c_toric
results.append(("Q8", q8, 0))

match_count = 0
for cid, computed, expected in results:
    m = close(computed, expected)
    if m:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if m else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=16 expected=16 match=yes
CLAIM Q2: computed=16.0 expected=16 match=yes
CLAIM Q3: computed=4 expected=4 match=yes
CLAIM Q4: computed=4.0 expected=4 match=yes
CLAIM Q5: computed=0.0 expected=0 match=yes
CLAIM Q6: computed=0.5 expected=0.5 match=yes
CLAIM Q7: computed=0.0 expected=0 match=yes
CLAIM Q8: computed=0 expected=0 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
