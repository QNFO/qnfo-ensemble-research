# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Raw circuit enumeration for m=6 modes, k=3 beam splitters is 3,375 ordered-slot instances",
    "inputs": "m=6, k=3, C(6,2)=15",
    "formula": "N_circ = C(m,2)^k = 15^3 = 3375"
  },
  {
    "id": "Q2",
    "statement": "Reordering-inclusive circuit count is 20,250",
    "inputs": "N_circ=3375, 3!=6",
    "formula": "N_circ_reorder = 3375 * 6 = 20250"
  },
  {
    "id": "Q3",
    "statement": "Graph instances for m=6, k=3 number 455",
    "inputs": "C(6,2)=15, k=3",
    "formula": "N_graph = C(C(m,2), k) = C(15,3) = (15*14*13)/6 = 455"
  },
  {
    "id": "Q4",
    "statement": "Search-space reduction factor is ≈7.4176 (≈44.5055 reordering-inclusive)",
    "inputs": "N_circ=3375, N_circ_reorder=20250, N_graph=455",
    "formula": "R = 3375/455 = 7.4176; R' = 20250/455 = 44.5055"
  },
  {
    "id": "Q5",
    "statement": "At m=10, k=5, circuit count is 184,528,125 and graph count is 1,221,759, reduction ≈151.03",
    "inputs": "m=10, k=5, C(10,2)=45",
    "formula": "N_circ = 45^5 = 184528125; N_graph = C(45,5) = (45*44*43*42*41)/120 = 1221759; R = 184528125/1221759 ≈ 151.03"
  },
  {
    "id": "Q6",
    "statement": "Three-qubit GHZ heralding probability via type-II fusion is p²/2 (lossless)",
    "inputs": "p=0.1 (also 0.25, 0.5)",
    "formula": "P_3GHZ = p^2 * (1/2); at p=0.1: 0.01/2 = 5e-3; at p=0.25: 3.125e-2; at p=0.5: 0.125"
  },
  {
    "id": "Q7",
    "statement": "Three-qubit GHZ heralding probability with loss at p=0.1, η=0.9 is 4.05×10⁻³",
    "inputs": "p=0.1, η=0.9",
    "formula": "P = p^2 * (1/2) * η^2 = 0.01 * 0.5 * 0.81 = 4.05e-3"
  },
  {
    "id": "Q8",
    "statement": "Four-qubit caterpillar heralding probability P = p⁴η⁴/8 at p=0.1, η=1 is 1.25×10⁻⁵",
    "inputs": "p=0.1, η=1",
    "formula": "P_4cat = p^4 * (1/8) * η^4 = 0.0001/8 = 1.25e-5"
  }
]

## Script
```python
import math
from fractions import Fraction
from math import comb, isclose

results = []

def report(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        try:
            match = "yes" if isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
        except Exception:
            match = "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    results.append(match == "yes")

# Q1
m, k = 6, 3
pairs = comb(m, 2)
N_circ = pairs ** k
report("Q1", N_circ, 3375)

# Q2
N_circ_reorder = N_circ * math.factorial(k)
report("Q2", N_circ_reorder, 20250)

# Q3
N_graph = comb(pairs, k)
report("Q3", N_graph, 455)

# Q4
R = N_circ / N_graph
R2 = N_circ_reorder / N_graph
report("Q4", round(R, 4), 7.4176)
report("Q4", round(R2, 4), 44.5055)

# Q5
m2, k2 = 10, 5
pairs2 = comb(m2, 2)
N_circ2 = pairs2 ** k2
N_graph2 = comb(pairs2, k2)
R5 = N_circ2 / N_graph2
report("Q5", N_circ2, 184528125)
report("Q5", N_graph2, 1221759)
report("Q5", round(R5, 2), 151.03)

# Q6
for p, exp in [(0.1, 5e-3), (0.25, 3.125e-2), (0.5, 0.125)]:
    P = p**2 * Fraction(1, 2)
    report("Q6", float(P), exp)

# Q7
p, eta = 0.1, 0.9
P7 = p**2 * 0.5 * eta**2
report("Q7", P7, 4.05e-3)

# Q8
p, eta = 0.1, 1.0
P8 = p**4 * Fraction(1, 8) * eta**4
report("Q8", float(P8), 1.25e-5)

n = len(results)
m_ = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m_} match, {n - m_} mismatch")

```

## Execution output
```
CLAIM Q1: computed=3375 expected=3375 match=yes
CLAIM Q2: computed=20250 expected=20250 match=yes
CLAIM Q3: computed=455 expected=455 match=yes
CLAIM Q4: computed=7.4176 expected=7.4176 match=yes
CLAIM Q4: computed=44.5055 expected=44.5055 match=yes
CLAIM Q5: computed=184528125 expected=184528125 match=yes
CLAIM Q5: computed=1221759 expected=1221759 match=yes
CLAIM Q5: computed=151.03 expected=151.03 match=yes
CLAIM Q6: computed=0.005000000000000001 expected=0.005 match=yes
CLAIM Q6: computed=0.03125 expected=0.03125 match=yes
CLAIM Q6: computed=0.125 expected=0.125 match=yes
CLAIM Q7: computed=0.004050000000000001 expected=0.00405 match=yes
CLAIM Q8: computed=1.2500000000000002e-05 expected=1.25e-05 match=yes
VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch

[exit 0]
```
