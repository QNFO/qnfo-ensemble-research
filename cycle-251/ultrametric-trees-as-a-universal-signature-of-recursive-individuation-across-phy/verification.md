# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The number of ternary increasing trees of order three is $T_{3}=15$.",
    "inputs": "k=2, n=3",
    "formula": "T_n = \\prod_{l=1}^{n} (k\\,(l-1) + 1); compute T_3 with k=2, n=3"
  },
  {
    "id": "Q2",
    "statement": "The majority‑estimator critical error probability for shape parameter $\\alpha=2$ is $q_{\\text{crit}} \\approx 0.4166667$.",
    "inputs": "alpha=2",
    "formula": "f(\\alpha) = (2\\alpha + 1) / (4(\\alpha + 1)); evaluate at \\alpha=2"
  },
  {
    "id": "Q3",
    "statement": "For binary branching ($b=2$) and depth $d=2$, the leaf count is $N_{2}=4$.",
    "inputs": "b=2, d=2",
    "formula": "N_d = b^{d}; compute N_2"
  },
  {
    "id": "Q4",
    "statement": "For binary branching ($b=2$) and depth $d=2$, the number of internal nodes is $M_{2}=3$.",
    "inputs": "b=2, d=2",
    "formula": "M_d = (b^{d} - 1) / (b - 1); compute M_2"
  },
  {
    "id": "Q5",
    "statement": "For ternary branching ($b=3$) and depth $d=1$, the leaf count is $N_{1}=3$.",
    "inputs": "b=3, d=1",
    "formula": "N_d = b^{d}; compute N_1"
  },
  {
    "id": "Q6",
    "statement": "For ternary branching ($b=3$) and depth $d=1$, the number of internal nodes is $M_{1}=1$.",
    "inputs": "b=3, d=1",
    "formula": "M_d = (b^{d} - 1) / (b - 1); compute M_1"
  },
  {
    "id": "Q7",
    "statement": "The number of unordered triples of 100 points is $\\binom{100}{3}=161{,}700$.",
    "inputs": "n=100",
    "formula": "C(n,3) = n (n-1) (n-2) / 6; compute for n=100"
  },
  {
    "id": "Q8",
    "statement": "A binary nesting depth of two yields $2^{2}=4$ items, matching the assumed subitizing ceiling $m=4$; depth three yields $2^{3}=8$ items, exceeding it.",
    "inputs": "b=2, m=4",
    "formula": "Find smallest d such that b^{d} \\ge m; solution d=2 gives N=4, d=3 gives N=8"
  },
  {
    "id": "Q9",
    "statement": "Assuming a per‑triangle check time of $1\\,\\mu\\text{s}$, verifying ultrametricity for $n=100$ points requires $161{,}700\\times1\\,\\mu\\text{s}=0.162\\,\\text{s}$.",
    "inputs": "checks=161700, per_check=1e-6 s",
    "formula": "time = checks * per_check; compute 161700 * 1e-6"
  }
]

## Script
```python
import math

def round_sig(x, sig):
    """Round x to sig significant digits."""
    if x == 0:
        return 0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Q1: Tree count T_3 for k=2, n=3
k = 2
n = 3
T = 1
for l in range(1, n+1):
    T *= (k*(l-1) + 1)
computed_Q1 = T
expected_Q1 = 15
match_Q1 = "yes" if computed_Q1 == expected_Q1 else "no"
print(f"CLAIM Q1: computed={computed_Q1} expected={expected_Q1} match={match_Q1}")

# Q2: Majority‑estimator threshold for alpha=2
alpha = 2
f = (2*alpha + 1) / (4*(alpha + 1))
computed_Q2 = f
expected_Q2 = 0.4166667
# round to 7 decimal places as in the paper
computed_Q2_rounded = round(computed_Q2, 7)
match_Q2 = "yes" if computed_Q2_rounded == expected_Q2 else "no"
print(f"CLAIM Q2: computed={computed_Q2_rounded} expected={expected_Q2} match={match_Q2}")

# Q3: Leaf count N_d = b^d for b=2, d=2
b = 2
d = 2
N = b**d
computed_Q3 = N
expected_Q3 = 4
match_Q3 = "yes" if computed_Q3 == expected_Q3 else "no"
print(f"CLAIM Q3: computed={computed_Q3} expected={expected_Q3} match={match_Q3}")

# Q4: Internal nodes M_d = (b^d - 1)/(b - 1) for b=2, d=2
M = (b**d - 1) // (b - 1)
computed_Q4 = M
expected_Q4 = 3
match_Q4 = "yes" if computed_Q4 == expected_Q4 else "no"
print(f"CLAIM Q4: computed={computed_Q4} expected={expected_Q4} match={match_Q4}")

# Q5: Leaf count for ternary branching b=3, d=1
b = 3
d = 1
N = b**d
computed_Q5 = N
expected_Q5 = 3
match_Q5 = "yes" if computed_Q5 == expected_Q5 else "no"
print(f"CLAIM Q5: computed={computed_Q5} expected={expected_Q5} match={match_Q5}")

# Q6: Internal nodes for b=3, d=1
M = (b**d - 1) // (b - 1)
computed_Q6 = M
expected_Q6 = 1
match_Q6 = "yes" if computed_Q6 == expected_Q6 else "no"
print(f"CLAIM Q6: computed={computed_Q6} expected={expected_Q6} match={match_Q6}")

# Q7: Number of unordered triples for n=100
n = 100
C = n*(n-1)*(n-2)//6
computed_Q7 = C
expected_Q7 = 161700
match_Q7 = "yes" if computed_Q7 == expected_Q7 else "no"
print(f"CLAIM Q7: computed={computed_Q7} expected={expected_Q7} match={match_Q7}")

# Q8: Binary nesting depth results
b = 2
m = 4
# smallest d with b^d >= m
d_min = 0
while b**d_min < m:
    d_min += 1
N_min = b**d_min
# depth three
d_three = 3
N_three = b**d_three
computed_Q8 = f"{N_min},{N_three}"
expected_Q8 = "4,8"
match_Q8 = "yes" if computed_Q8 == expected_Q8 else "no"
print(f"CLAIM Q8: computed={computed_Q8} expected={expected_Q8} match={match_Q8}")

# Q9: Verification time with per‑triangle check time 1 µs
checks = 161700
per_check = 1e-6  # seconds
time_sec = checks * per_check
# round to 3 decimal places as in the paper
computed_Q9 = round(time_sec, 3)
expected_Q9 = 0.162
match_Q9 = "yes" if computed_Q9 == expected_Q9 else "no"
print(f"CLAIM Q9: computed={computed_Q9} expected={expected_Q9} match={match_Q9}")

print(f"VERIFICATION SUMMARY: 9 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9].count('yes'))} match, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9].count('no'))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=15 expected=15 match=yes
CLAIM Q2: computed=0.4166667 expected=0.4166667 match=yes
CLAIM Q3: computed=4 expected=4 match=yes
CLAIM Q4: computed=3 expected=3 match=yes
CLAIM Q5: computed=3 expected=3 match=yes
CLAIM Q6: computed=1 expected=1 match=yes
CLAIM Q7: computed=161700 expected=161700 match=yes
CLAIM Q8: computed=4,8 expected=4,8 match=yes
CLAIM Q9: computed=0.162 expected=0.162 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 96, in <module>
TypeError: 'int' object is not iterable

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 15 | 15 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.4166667 | 0.4166667 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q3 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 161700 | 161700 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q8 | 4,8 | 4,8 | yes | match | script verdict (values not both numeric) |
| Q9 | 0.162 | 0.162 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 9.
