# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Effective Hubble‑like parameter for a binary tree (p=2) with λ=1 is H = ln 2 ≈ 0.693.",
    "inputs": "p = 2, λ = 1",
    "formula": "H = ln(p) / λ"
  },
  {
    "id": "Q2",
    "statement": "Node count at depth n=5 for p=2 is N5 = 32.",
    "inputs": "p = 2, n = 5",
    "formula": "N = p^n"
  },
  {
    "id": "Q3",
    "statement": "Total information up to depth n=10 for p=2 is I10 = 1024 bits.",
    "inputs": "p = 2, n = 10",
    "formula": "I = p^n"
  },
  {
    "id": "Q4",
    "statement": "Area estimate at depth n=10 with c=1 is A10 ≈ 101.6.",
    "inputs": "c = 1, p = 2, n = 10",
    "formula": "A = c * p^{2n/3}"
  },
  {
    "id": "Q5",
    "statement": "Holographic entropy bound at depth n=10 with c=1 is S10^max ≈ 25.4 bits.",
    "inputs": "c = 1, p = 2, n = 10",
    "formula": "S = (c/4) * p^{2n/3}"
  },
  {
    "id": "Q6",
    "statement": "Ratio of information to holographic bound at depth 10 is I10 / S10^max ≈ 40.3.",
    "inputs": "I10 = 1024, S10^max = 25.4",
    "formula": "ratio = I10 / S10^max"
  },
  {
    "id": "Q7",
    "statement": "Log‑periodic modulation period in ln k is ln p, which for p=2 equals ln 2 ≈ 0.693.",
    "inputs": "p = 2",
    "formula": "period = ln(p)"
  },
  {
    "id": "Q8",
    "statement": "Embedding constant c required for equality I10 = S10^max is approximately c ≈ 40.",
    "inputs": "I10 = 1024, p = 2, n = 10",
    "formula": "c = 4 * I10 / p^{2n/3}"
  }
]

## Script
```python
import math

def fmt(value, template):
    """Format value to have the same number of decimal places as the template string."""
    if '.' in template:
        dec = len(template.split('.')[-1])
        fmt_str = f"{{:.{dec}f}}"
        return fmt_str.format(value)
    else:
        # integer template
        return str(int(round(value)))

# Q1: H = ln(p) / λ
p = 2
lam = 1
H = math.log(p) / lam
expected_Q1 = "0.693"
computed_Q1 = fmt(H, expected_Q1)
match_Q1 = "yes" if computed_Q1 == expected_Q1 else "no"
print(f"CLAIM Q1: computed={computed_Q1} expected={expected_Q1} match={match_Q1}")

# Q2: N = p^n
n = 5
N5 = p ** n
expected_Q2 = "32"
computed_Q2 = fmt(N5, expected_Q2)
match_Q2 = "yes" if computed_Q2 == expected_Q2 else "no"
print(f"CLAIM Q2: computed={computed_Q2} expected={expected_Q2} match={match_Q2}")

# Q3: I = p^n
n = 10
I10 = p ** n
expected_Q3 = "1024"
computed_Q3 = fmt(I10, expected_Q3)
match_Q3 = "yes" if computed_Q3 == expected_Q3 else "no"
print(f"CLAIM Q3: computed={computed_Q3} expected={expected_Q3} match={match_Q3}")

# Q4: A = c * p^{2n/3}
c = 1
n = 10
A10 = c * (p ** (2 * n / 3))
expected_Q4 = "101.6"
computed_Q4 = fmt(A10, expected_Q4)
match_Q4 = "yes" if computed_Q4 == expected_Q4 else "no"
print(f"CLAIM Q4: computed={computed_Q4} expected={expected_Q4} match={match_Q4}")

# Q5: S = (c/4) * p^{2n/3}
S10_max = (c / 4) * (p ** (2 * n / 3))
expected_Q5 = "25.4"
computed_Q5 = fmt(S10_max, expected_Q5)
match_Q5 = "yes" if computed_Q5 == expected_Q5 else "no"
print(f"CLAIM Q5: computed={computed_Q5} expected={expected_Q5} match={match_Q5}")

# Q6: ratio = I10 / S10_max
ratio = I10 / S10_max
expected_Q6 = "40.3"
computed_Q6 = fmt(ratio, expected_Q6)
match_Q6 = "yes" if computed_Q6 == expected_Q6 else "no"
print(f"CLAIM Q6: computed={computed_Q6} expected={expected_Q6} match={match_Q6}")

# Q7: period = ln(p)
period = math.log(p)
expected_Q7 = "0.693"
computed_Q7 = fmt(period, expected_Q7)
match_Q7 = "yes" if computed_Q7 == expected_Q7 else "no"
print(f"CLAIM Q7: computed={computed_Q7} expected={expected_Q7} match={match_Q7}")

# Q8: c = 4 * I10 / p^{2n/3}
c_needed = 4 * I10 / (p ** (2 * n / 3))
expected_Q8 = "40"
computed_Q8 = fmt(c_needed, expected_Q8)
match_Q8 = "yes" if computed_Q8 == expected_Q8 else "no"
print(f"CLAIM Q8: computed={computed_Q8} expected={expected_Q8} match={match_Q8}")

print(f"VERIFICATION SUMMARY: 8 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8].count('yes'))} match, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8].count('no'))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.693 expected=0.693 match=yes
CLAIM Q2: computed=32 expected=32 match=yes
CLAIM Q3: computed=1024 expected=1024 match=yes
CLAIM Q4: computed=101.6 expected=101.6 match=yes
CLAIM Q5: computed=25.4 expected=25.4 match=yes
CLAIM Q6: computed=40.3 expected=40.3 match=yes
CLAIM Q7: computed=0.693 expected=0.693 match=yes
CLAIM Q8: computed=40 expected=40 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 75, in <module>
TypeError: 'int' object is not iterable

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.693 | 0.693 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 32 | 32 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 1024 | 1024 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 101.6 | 101.6 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 25.4 | 25.4 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 40.3 | 40.3 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 0.693 | 0.693 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 40 | 40 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 8.
