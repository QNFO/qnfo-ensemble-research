# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Topological regime condition |mu| < 2 t zeta(alpha) for alpha > 1",
    "inputs": "t (hopping), mu (chemical potential), alpha > 1",
    "formula": "|mu| < 2*t*zeta(alpha)"
  },
  {
    "id": "Q2",
    "statement": "Braid unitary U_ij = exp((pi/4) gamma_i gamma_j) = (1/sqrt(2))(1 + gamma_i gamma_j)",
    "inputs": "theta = pi/4",
    "formula": "U_ij = cos(pi/4)*1 + sin(pi/4)*gamma_i*gamma_j = (1/sqrt(2))*(1 + gamma_i*gamma_j)"
  },
  {
    "id": "Q3",
    "statement": "Fourth power of exchange unitary is minus identity: U^4 = -1 (projective lift)",
    "inputs": "U = exp((pi/4)*i*sigma_3)",
    "formula": "U^4 = exp(i*pi*sigma_3) = diag(e^{i*pi}, e^{-i*pi}) = -1"
  },
  {
    "id": "Q4",
    "statement": "Ising anchor phase per exchange phi_Ising = pi/8 = 0.3927 rad",
    "inputs": "pi = 3.14159",
    "formula": "phi_Ising = pi/8 = 3.14159/8 = 0.3927 rad"
  },
  {
    "id": "Q5",
    "statement": "MZM decay parameter lambda at alpha = 3, mu/t0 = 0.1: lambda = 0.0416",
    "inputs": "mu/t0 = 0.1, alpha = 3, zeta(3) = 1.2020569",
    "formula": "lambda = (mu/t0)/(2*zeta(alpha)) = 0.1/(2*1.2020569) = 0.1/2.4041138 = 0.0416"
  },
  {
    "id": "Q6",
    "statement": "Localization length xi = 0.3145 sites at alpha = 3",
    "inputs": "lambda = 0.0416",
    "formula": "xi = 1/|ln(lambda)| = 1/3.1792 = 0.3145 sites"
  },
  {
    "id": "Q7",
    "statement": "Per-braid drift epsilon = 1.46e-17 at alpha = 3, s = 10 (assumed scaling)",
    "inputs": "lambda = 0.0416, s = 10, alpha = 3",
    "formula": "epsilon = lambda^s * s^{-alpha} = e^{10*ln(0.0416)} * 10^{-3} = 1.46e-14 * 1e-3 = 1.46e-17"
  },
  {
    "id": "Q8",
    "statement": "Cumulative drift over 1e6 braids is <= 9.2e-11 rad",
    "inputs": "epsilon = 1.46e-17, N_pairs = 1e6",
    "formula": "|Delta phi| <= 2*pi*epsilon*N_pairs = 2*pi*1.46e-17*1e6 = 9.2e-11 rad"
  }
]

## Script
```python
import math
from fractions import Fraction

results = []

def report(cid, computed, expected, is_float=True):
    if expected is None:
        match = "no"
    elif is_float:
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    results.append(match == "yes")

# Q1: topological regime |mu| < 2 t zeta(alpha), alpha > 1
alpha1 = 3.0
t1 = 1.0
mu1 = 0.1
zeta3 = 1.2020569
bound = 2 * t1 * zeta3
computed_q1 = abs(mu1) < bound
report("Q1", computed_q1, True, is_float=False)

# Q2: braid unitary U = cos(pi/4) 1 + sin(pi/4) gamma_i gamma_j = (1/sqrt2)(1 + gamma_i gamma_j)
theta = math.pi / 4
c, s = math.cos(theta), math.sin(theta)
computed_q2 = math.isclose(c, 1 / math.sqrt(2), rel_tol=1e-6) and math.isclose(s, 1 / math.sqrt(2), rel_tol=1e-6)
report("Q2", computed_q2, True, is_float=False)

# Q3: U^4 = exp(i*pi*sigma_3) = diag(e^{i pi}, e^{-i pi}) = -1
U4_00 = complex(math.cos(math.pi), math.sin(math.pi))   # e^{i pi}
U4_11 = complex(math.cos(-math.pi), math.sin(-math.pi)) # e^{-i pi}
computed_q3 = math.isclose(U4_00, -1, rel_tol=1e-6) and math.isclose(U4_11, -1, rel_tol=1e-6)
report("Q3", computed_q3, True, is_float=False)

# Q4: phi_Ising = pi/8 with pi = 3.14159
pi_input = 3.14159
phi = pi_input / 8
report("Q4", phi, 0.3927)

# Q5: lambda = (mu/t0)/(2*zeta(alpha)) at alpha=3, mu/t0=0.1
lam = 0.1 / (2 * zeta3)
report("Q5", lam, 0.0416)

# Q6: xi = 1/|ln(lambda)|
xi = 1 / abs(math.log(lam))
report("Q6", xi, 0.3145)

# Q7: epsilon = lambda^s * s^{-alpha}, s=10, alpha=3
s_sep = 10
eps = (lam ** s_sep) * (s_sep ** (-alpha1))
report("Q7", eps, 1.46e-17)

# Q8: cumulative drift <= 2*pi*epsilon*N_pairs, N_pairs = 1e6
N_pairs = 1e6
drift = 2 * math.pi * eps * N_pairs
report("Q8", drift, 9.2e-11)

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=True expected=True match=yes
CLAIM Q2: computed=True expected=True match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 34, in <module>
TypeError: must be real number, not complex

[exit 1]
```
