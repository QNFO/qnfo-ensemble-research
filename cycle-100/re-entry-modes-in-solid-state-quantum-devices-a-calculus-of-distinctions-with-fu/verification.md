# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Thermal energy at 1 K is 8.62e-5 eV",
    "inputs": "k_B = 8.617333e-5 eV/K, T = 1 K",
    "formula": "E_T = k_B * T"
  },
  {
    "id": "Q2",
    "statement": "Thermal energy at 0.1 K is 8.62e-6 eV",
    "inputs": "k_B = 8.617333e-5 eV/K, T = 0.1 K",
    "formula": "E_T = k_B * T"
  },
  {
    "id": "Q3",
    "statement": "Thermal energy at 20 K is 1.72e-3 eV",
    "inputs": "k_B = 8.617333e-5 eV/K, T = 20 K",
    "formula": "E_T = k_B * T"
  },
  {
    "id": "Q4",
    "statement": "Ratio of thermal energies at 1 K and 0.1 K is 10.0",
    "inputs": "T1 = 1 K, T2 = 0.1 K",
    "formula": "E_T(T1)/E_T(T2) = T1/T2"
  },
  {
    "id": "Q5",
    "statement": "Schottky peak position x* = 2.3993",
    "inputs": "peak condition 2/x = tanh(x/2)",
    "formula": "solve tanh(x/2) - 2/x = 0 for x > 0"
  },
  {
    "id": "Q6",
    "statement": "Schottky peak height C_max/R = 0.439",
    "inputs": "x* = 2.3993",
    "formula": "C/R = x^2 / (4*cosh(x/2)^2) evaluated at x = x*"
  },
  {
    "id": "Q7",
    "statement": "C_max = 3.65 J/mol/K",
    "inputs": "C_max/R = 0.43920, R = 8.314 J/mol/K",
    "formula": "C_max = (C_max/R) * R"
  },
  {
    "id": "Q8",
    "statement": "Peak temperature T* = 0.4168 * Delta/k_B",
    "inputs": "x* = 2.3993",
    "formula": "T* = Delta/(x* k_B), coefficient = 1/x*"
  }
]

## Script
```python
import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

# Q1: E_T(1 K)
k_B = 8.617333e-5  # eV/K
E1 = k_B * 1.0
print(f"CLAIM Q1: computed={E1:.6e} expected=8.617333e-05 match={'yes' if isclose(E1, 8.617333e-5) else 'no'}")

# Q2: E_T(0.1 K)
E2 = k_B * 0.1
print(f"CLAIM Q2: computed={E2:.6e} expected=8.617333e-06 match={'yes' if isclose(E2, 8.617333e-6) else 'no'}")

# Q3: E_T(20 K)
E3 = k_B * 20.0
print(f"CLAIM Q3: computed={E3:.6e} expected=1.7234666e-03 match={'yes' if isclose(E3, 1.7234666e-3) else 'no'}")

# Q4: ratio E_T(1K)/E_T(0.1K)
ratio = E1 / E2
print(f"CLAIM Q4: computed={ratio:.6f} expected=10.0 match={'yes' if isclose(ratio, 10.0) else 'no'}")

# Q5: solve tanh(x/2) - 2/x = 0 by bisection
def g(x):
    return math.tanh(x / 2.0) - 2.0 / x

lo, hi = 2.0, 3.0
for _ in range(200):
    mid = (lo + hi) / 2.0
    if g(lo) * g(mid) <= 0:
        hi = mid
    else:
        lo = mid
x_star = (lo + hi) / 2.0
print(f"CLAIM Q5: computed={x_star:.6f} expected=2.3993 match={'yes' if isclose(x_star, 2.3993, ) or abs(x_star-2.3993)<5e-4 else 'no'}")

# Q6: C_max/R at x*
C_over_R = x_star**2 / (4.0 * math.cosh(x_star / 2.0)**2)
print(f"CLAIM Q6: computed={C_over_R:.6f} expected=0.439 match={'yes' if isclose(C_over_R, 0.439) or abs(C_over_R-0.439)<5e-4 else 'no'}")

# Q7: C_max = (C_max/R)*R
R = 8.314  # J/mol/K
C_max = C_over_R * R
print(f"CLAIM Q7: computed={C_max:.6f} expected=3.65 match={'yes' if abs(C_max-3.65)<5e-3 else 'no'}")

# Q8: coefficient 1/x*
coeff = 1.0 / x_star
print(f"CLAIM Q8: computed={coeff:.6f} expected=0.4168 match={'yes' if abs(coeff-0.4168)<5e-4 else 'no'}")

n = 8
m = sum([
    isclose(E1, 8.617333e-5),
    isclose(E2, 8.617333e-6),
    isclose(E3, 1.7234666e-3),
    isclose(ratio, 10.0),
    abs(x_star - 2.3993) < 5e-4,
    abs(C_over_R - 0.439) < 5e-4,
    abs(C_max - 3.65) < 5e-3,
    abs(coeff - 0.4168) < 5e-4,
])
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=8.617333e-05 expected=8.617333e-05 match=yes
CLAIM Q2: computed=8.617333e-06 expected=8.617333e-06 match=yes
CLAIM Q3: computed=1.723467e-03 expected=1.7234666e-03 match=yes
CLAIM Q4: computed=10.000000 expected=10.0 match=yes
CLAIM Q5: computed=2.399357 expected=2.3993 match=yes
CLAIM Q6: computed=0.439229 expected=0.439 match=yes
CLAIM Q7: computed=3.651749 expected=3.65 match=yes
CLAIM Q8: computed=0.416778 expected=0.4168 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
