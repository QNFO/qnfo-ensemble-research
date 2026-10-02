# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Ising parent total quantum dimension squared: D_C^2 = 4, so D_C = 2.",
    "inputs": "d_1=1, d_sigma=sqrt(2), d_psi=1",
    "formula": "D_C^2 = 1^2 + (sqrt(2))^2 + 1^2 = 1 + 2 + 1 = 4"
  },
  {
    "id": "Q2",
    "statement": "Ising condensate dimension dim(A) = 2 for A = 1 + psi.",
    "inputs": "d_1=1, d_psi=1",
    "formula": "dim(A) = 1 + 1 = 2"
  },
  {
    "id": "Q3",
    "statement": "Ising condensation index kappa = 4.",
    "inputs": "dim(A)=2",
    "formula": "kappa = dim(A)^2 = 2^2 = 4"
  },
  {
    "id": "Q4",
    "statement": "Ising child quantum dimension D_D = 1, consistent with D_C/dim(A).",
    "inputs": "D_C=2, dim(A)=2",
    "formula": "D_D = D_C/dim(A) = 2/2 = 1"
  },
  {
    "id": "Q5",
    "statement": "Ising parent chiral central charge c_C = 1/2 via Gauss-Milgram.",
    "inputs": "d_1^2*theta_1 = 1, d_sigma^2*theta_sigma = 2e^{i pi/8}, d_psi^2*theta_psi = -1, D_C=2",
    "formula": "sum_a d_a^2 theta_a = 1 + 2e^{i pi/8} - 1 = 2e^{i pi/8} = D_C e^{2 pi i c/8} => c_C = 1/2"
  },
  {
    "id": "Q6",
    "statement": "Ising Majorana index mu = 1.",
    "inputs": "c_C=1/2, c_D=0",
    "formula": "mu = 2(c_C - c_D) = 2*(1/2 - 0) = 1"
  },
  {
    "id": "Q7",
    "statement": "Toric code parent total quantum dimension D_C = 2.",
    "inputs": "d_1=d_e=d_m=d_epsilon=1",
    "formula": "D_C^2 = 1+1+1+1 = 4, D_C = 2"
  },
  {
    "id": "Q8",
    "statement": "Toric code condensation index kappa = 4 with dim(A) = 2.",
    "inputs": "d_1=1, d_e=1",
    "formula": "dim(A) = 1+1 = 2; kappa = 2^2 = 4"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, complex):
        match = "yes" if abs(computed - expected) < 1e-6 else "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: Ising D_C^2 = 4, D_C = 2
d1, dsig, dpsi = 1.0, math.sqrt(2), 1.0
DC2 = d1**2 + dsig**2 + dpsi**2
DC = math.sqrt(DC2)
results.append(check("Q1", DC, 2.0))

# Q2: dim(A) = 2 for A = 1 + psi
dimA = d1 + dpsi
results.append(check("Q2", dimA, 2.0))

# Q3: kappa = dim(A)^2 = 4
kappa = dimA**2
results.append(check("Q3", kappa, 4.0))

# Q4: D_D = D_C/dim(A) = 1
DD = DC / dimA
results.append(check("Q4", DD, 1.0))

# Q5: Gauss-Milgram: sum d_a^2 theta_a = 2 e^{i pi/8} = D_C e^{2 pi i c/8} => c_C = 1/2
theta1, thetasig, thetapsi = 1.0, math.exp(1j*math.pi/8), -1.0
S = d1**2*theta1 + dsig**2*thetasig + dpsi**2*thetapsi
# S = D_C e^{2 pi i c/8}; solve for c mod 8
ratio = S / DC
cC = (math.atan2(ratio.imag, ratio.real) / (2*math.pi)) * 8
cC = cC % 8
results.append(check("Q5", cC, 0.5))

# Q6: mu = 2(c_C - c_D), c_D = 0
cD = 0.0
mu = 2*(cC - cD)
results.append(check("Q6", mu, 1.0))

# Q7: Toric code D_C = 2
toric = [1.0, 1.0, 1.0, 1.0]
DC2t = sum(d**2 for d in toric)
DCt = math.sqrt(DC2t)
results.append(check("Q7", DCt, 2.0))

# Q8: Toric code dim(A) = 2, kappa = 4
dimA_t = 1.0 + 1.0
kappa_t = dimA_t**2
results.append(check("Q8", kappa_t, 4.0))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n-m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=2.0 expected=2.0 match=yes
CLAIM Q2: computed=2.0 expected=2.0 match=yes
CLAIM Q3: computed=4.0 expected=4.0 match=yes
CLAIM Q4: computed=1.0 expected=1.0 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 36, in <module>
TypeError: must be real number, not complex

[exit 1]
```
