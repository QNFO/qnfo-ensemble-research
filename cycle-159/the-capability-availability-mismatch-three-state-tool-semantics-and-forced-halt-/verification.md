# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "State-space ratio for k=10: three-state space is 57.7 times larger than binary model",
    "inputs": "k=10",
    "formula": "3^10 / 2^10"
  },
  {
    "id": "Q2",
    "statement": "Number of configurations containing at least one disabled tool for k=10",
    "inputs": "3^10=59049, 2^10=1024",
    "formula": "59049 - 1024"
  },
  {
    "id": "Q3",
    "statement": "Well-defined fraction for k=5 under uniform representation",
    "inputs": "k=5",
    "formula": "(2/3)^5 = 32/243"
  },
  {
    "id": "Q4",
    "statement": "Unspecified fraction for k=5",
    "inputs": "32/243",
    "formula": "1 - 32/243"
  },
  {
    "id": "Q5",
    "statement": "Mismatch probability q per gated invocation",
    "inputs": "p_C=0.90, p_P=0.70",
    "formula": "p_C * (1 - p_P)"
  },
  {
    "id": "Q6",
    "statement": "Probability at least one mismatch in a k=5 task",
    "inputs": "q=0.27, k=5",
    "formula": "1 - (1 - 0.27)^5"
  },
  {
    "id": "Q7",
    "statement": "Probability at least one mismatch in a k=10 task",
    "inputs": "q=0.27, k=10",
    "formula": "1 - (1 - 0.27)^10"
  },
  {
    "id": "Q8",
    "statement": "Signaling break-even threshold per task",
    "inputs": "q=0.27, c_t",
    "formula": "s* = q * c_t = 0.27 * c_t"
  },
  {
    "id": "Q9",
    "statement": "Well-defined fraction if a fourth state appears, k=5",
    "inputs": "k=5, 4 states",
    "formula": "(2/4)^5 = 1/32"
  }
]

## Script
```python
import math
from fractions import Fraction

def sig(x, n=8):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: 3^10 / 2^10
c1 = 3**10 / 2**10
results.append(("Q1", c1, "57.7"))

# Q2: 59049 - 1024
c2 = 3**10 - 2**10
results.append(("Q2", c2, "58025"))

# Q3: (2/3)^5 = 32/243
c3 = Fraction(2, 3)**5
c3f = float(c3)
results.append(("Q3", c3f, "0.132"))

# Q4: 1 - 32/243
c4 = 1 - Fraction(32, 243)
c4f = float(c4)
results.append(("Q4", c4f, "0.868"))

# Q5: 0.90 * (1 - 0.70)
c5 = 0.90 * (1 - 0.70)
results.append(("Q5", c5, "0.27"))

# Q6: 1 - (1 - 0.27)^5
c6 = 1 - (1 - 0.27)**5
results.append(("Q6", c6, "0.793"))

# Q7: 1 - (1 - 0.27)^10
c7 = 1 - (1 - 0.27)**10
results.append(("Q7", c7, "0.957"))

# Q8: s* = 0.27 * c_t (symbolic; report coefficient)
c8 = 0.27
results.append(("Q8", c8, "0.27"))

# Q9: (2/4)^5 = 1/32
c9 = Fraction(2, 4)**5
c9f = float(c9)
results.append(("Q9", c9f, "0.03125"))

mismatch = 0
for cid, comp, exp in results:
    # match: computed rounded to paper's stated sig digits equals expected
    if cid in ("Q1",):
        match = "yes" if abs(comp - 57.7) < 0.05 else "no"
    elif cid in ("Q3",):
        match = "yes" if abs(comp - 0.132) < 0.0005 else "no"
    elif cid in ("Q4",):
        match = "yes" if abs(comp - 0.868) < 0.0005 else "no"
    elif cid in ("Q5",):
        match = "yes" if abs(comp - 0.27) < 1e-9 else "no"
    elif cid in ("Q6",):
        match = "yes" if abs(comp - 0.793) < 0.0005 else "no"
    elif cid in ("Q7",):
        match = "yes" if abs(comp - 0.957) < 0.0005 else "no"
    elif cid in ("Q8",):
        match = "yes" if abs(comp - 0.27) < 1e-9 else "no"
    elif cid in ("Q9",):
        match = "yes" if abs(comp - 0.03125) < 1e-9 else "no"
    else:
        match = "yes" if abs(comp - float(exp)) < 1e-9 else "no"
    if match == "no":
        mismatch += 1
    print(f"CLAIM {cid}: computed={sig(comp)} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results)-mismatch} match, {mismatch} mismatch")

```

## Execution output
```
CLAIM Q1: computed=57.665039 expected=57.7 match=yes
CLAIM Q2: computed=58025 expected=58025 match=yes
CLAIM Q3: computed=0.13168724 expected=0.132 match=yes
CLAIM Q4: computed=0.86831276 expected=0.868 match=yes
CLAIM Q5: computed=0.27 expected=0.27 match=yes
CLAIM Q6: computed=0.79269284 expected=0.793 match=yes
CLAIM Q7: computed=0.95702374 expected=0.957 match=yes
CLAIM Q8: computed=0.27 expected=0.27 match=yes
CLAIM Q9: computed=0.03125 expected=0.03125 match=yes
VERIFICATION SUMMARY: 9 claims, 9 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 57.665039 | 57.7 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 58025 | 58025 | yes | match | 5 significant digits (as printed, at least 3) |
| Q3 | 0.13168724 | 0.132 | yes | match | 3 significant digits (as printed, at least 3) |
| Q4 | 0.86831276 | 0.868 | yes | match | 3 significant digits (as printed, at least 3) |
| Q5 | 0.27 | 0.27 | yes | match | 3 significant digits (as printed, at least 3) |
| Q6 | 0.79269284 | 0.793 | yes | match | 3 significant digits (as printed, at least 3) |
| Q7 | 0.95702374 | 0.957 | yes | match | 3 significant digits (as printed, at least 3) |
| Q8 | 0.27 | 0.27 | yes | match | 3 significant digits (as printed, at least 3) |
| Q9 | 0.03125 | 0.03125 | yes | match | 4 significant digits (as printed, at least 3) |

Mismatches: 0 of 9.
