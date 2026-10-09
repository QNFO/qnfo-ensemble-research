# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Absorbing fraction of a three-move observer's epistemic space under rho_1 is 37/64 = 0.578125",
    "inputs": "k=3 (model definition); assessment set size |{T,F,N,B}|=4; contradiction-free values per coordinate = 3 ({T,F,N})",
    "formula": "f(3) = (4^3 - 3^3)/4^3 = (64 - 27)/64 = 37/64 = 0.578125"
  },
  {
    "id": "Q2",
    "statement": "Total epistemic profiles for k=3 perceived candidate moves is 64",
    "inputs": "k=3; |{T,F,N,B}|=4",
    "formula": "4^3 = 64"
  },
  {
    "id": "Q3",
    "statement": "Number of absorbing contradictory profiles is 37",
    "inputs": "4^3 = 64 total profiles; 3^3 = 27 contradiction-free profiles",
    "formula": "64 - 27 = 37"
  },
  {
    "id": "Q3b",
    "statement": "Contradiction-free profiles number 27",
    "inputs": "k=3; 3 values per coordinate ({T,F,N})",
    "formula": "3^3 = 27"
  },
  {
    "id": "Q4",
    "statement": "Projected absorbing fraction for k=10 is 989527/1048576 ≈ 0.9436865",
    "inputs": "k=10; 3^10 = 59049; 4^10 = 1048576",
    "formula": "f(10) = 1 - (3/4)^10 = 1 - 59049/1048576 = 989527/1048576 ≈ 0.9436865"
  },
  {
    "id": "Q5",
    "statement": "Average number of assessment profiles collapsing onto each perceived move set is 8",
    "inputs": "4^3 = 64 profiles; 2^3 = 8 perceived move sets",
    "formula": "64/8 = 8"
  },
  {
    "id": "Q6",
    "statement": "Number of distinct perceived move sets is at most 8",
    "inputs": "k=3",
    "formula": "2^3 = 8"
  },
  {
    "id": "Q7",
    "statement": "Each polarity-blind operator has exactly 8 preimage profiles per move set",
    "inputs": "k=3; 2 verdict values per option",
    "formula": "2^3 = 8"
  }
]

## Script
```python
import math
from fractions import Fraction

def check(cid, computed, expected):
    if expected is None:
        match = "n/a"
    else:
        if isinstance(computed, float) or isinstance(expected, float):
            match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
        else:
            match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: absorbing fraction f(3) = (4^3 - 3^3)/4^3
total3 = 4**3          # 64
free3 = 3**3           # 27
absorbing3 = total3 - free3
f3 = Fraction(absorbing3, total3)
results.append(check("Q1", f3, Fraction(37, 64)))
print(f"  (decimal: {float(f3)})")

# Q2: total epistemic profiles 4^3
results.append(check("Q2", 4**3, 64))

# Q3: absorbing contradictory profiles 64 - 27
results.append(check("Q3", 64 - 27, 37))

# Q3b: contradiction-free profiles 3^3
results.append(check("Q3b", 3**3, 27))

# Q4: f(10) = 1 - (3/4)^10 = 989527/1048576
num10 = 4**10 - 3**10
den10 = 4**10
f10 = Fraction(num10, den10)
results.append(check("Q4", f10, Fraction(989527, 1048576)))
print(f"  (decimal: {float(f10):.7f})")

# Q5: average profiles per perceived move set 64/8
results.append(check("Q5", Fraction(64, 8), Fraction(8, 1)))

# Q6: number of distinct perceived move sets at most 2^3
results.append(check("Q6", 2**3, 8))

# Q7: preimage profiles per move set 2^3
results.append(check("Q7", 2**3, 8))

n = len(results)
m = sum(1 for r in results if r)
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")

```

## Execution output
```
CLAIM Q1: computed=37/64 expected=37/64 match=yes
  (decimal: 0.578125)
CLAIM Q2: computed=64 expected=64 match=yes
CLAIM Q3: computed=37 expected=37 match=yes
CLAIM Q3b: computed=27 expected=27 match=yes
CLAIM Q4: computed=989527/1048576 expected=989527/1048576 match=yes
  (decimal: 0.9436865)
CLAIM Q5: computed=8 expected=8 match=yes
CLAIM Q6: computed=8 expected=8 match=yes
CLAIM Q7: computed=8 expected=8 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
