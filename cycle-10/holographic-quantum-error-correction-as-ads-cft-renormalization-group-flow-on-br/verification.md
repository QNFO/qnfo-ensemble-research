# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Bit-flip threshold of the ternary majority-vote tree recursion is p* = 1/4",
    "inputs": "p*=0.25",
    "formula": "f(p) = 3p^2 - 2p^3; fixed point f(p)=p gives 2p^2-3p+1=0, p=(3±1)/4"
  },
  {
    "id": "Q2",
    "statement": "Depolarizing threshold is 3/8 = 3.75e-1",
    "inputs": "p*=0.25",
    "formula": "(2/3)*p_dep < 1/4 => p_dep < 3/8"
  },
  {
    "id": "Q3",
    "statement": "Two-qubit gate error p_2q = 4.4e-3",
    "inputs": "fidelity=0.9956",
    "formula": "p_2q = 1 - 0.9956"
  },
  {
    "id": "Q4",
    "statement": "Single-qubit gate error p_1q = 1.0e-3",
    "inputs": "fidelity=0.9990",
    "formula": "p_1q = 1 - 0.9990"
  },
  {
    "id": "Q5",
    "statement": "Readout error p_ro = 1.3e-2",
    "inputs": "fidelity=0.987",
    "formula": "p_ro = 1 - 0.987"
  },
  {
    "id": "Q6",
    "statement": "Cat-code bit-flip probability per loss event p_bf = 6.144e-6 at nbar=6",
    "inputs": "nbar=6",
    "formula": "p_bf = e^{-2*nbar} = e^{-12} = (e^{-6})^2 = (2.4788e-3)^2"
  },
  {
    "id": "Q7",
    "statement": "Effective per-mode bit-flip rate p_eff = 2.703e-8",
    "inputs": "p_2q=4.4e-3, p_bf=6.144e-6",
    "formula": "p_eff = p_2q * p_bf = 4.4e-3 * 6.144e-6"
  },
  {
    "id": "Q8",
    "statement": "Margin of p_eff over 1e-4 threshold is 3.70e3",
    "inputs": "threshold=1e-4, p_eff=2.703e-8",
    "formula": "margin = 1e-4 / 2.703e-8"
  }
]

## Script
```python
import math
from fractions import Fraction

results = []

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    results.append(match == "yes")
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: fixed point of f(p)=3p^2-2p^3
# 3p^2-2p^3 = p -> p(2p^2-3p+1)=0 -> p=(3±1)/4
roots = [Fraction(3+s, 4) for s in (-1, 1)]
p_star = [r for r in roots if 0 < r < Fraction(1, 2)][0]
check("Q1", float(p_star), 0.25)

# Q2: depolarizing threshold
# (2/3)*p_dep < 1/4 => p_dep < 3/8
p_dep = Fraction(1, 4) * Fraction(3, 2)
check("Q2", float(p_dep), 0.375)

# Q3: p_2q = 1 - 0.9956
p_2q = 1 - 0.9956
check("Q3", p_2q, 4.4e-3)

# Q4: p_1q = 1 - 0.9990
p_1q = 1 - 0.9990
check("Q4", p_1q, 1.0e-3)

# Q5: p_ro = 1 - 0.987
p_ro = 1 - 0.987
check("Q5", p_ro, 1.3e-2)

# Q6: p_bf = e^{-2*nbar} at nbar=6
nbar = 6
p_bf = math.exp(-2 * nbar)
check("Q6", p_bf, 6.144e-6)

# Q7: p_eff = p_2q * p_bf
p_eff = p_2q * p_bf
check("Q7", p_eff, 2.703e-8)

# Q8: margin = threshold / p_eff
threshold = 1e-4
margin = threshold / p_eff
check("Q8", margin, 3.70e3)

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```

[stderr]
Traceback (most recent call last):
  File "<string>", line 19, in <module>
IndexError: list index out of range

[exit 1]
```
