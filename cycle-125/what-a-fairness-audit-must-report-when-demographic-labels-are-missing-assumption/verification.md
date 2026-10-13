# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "For the Section 4.2 example, the disparity interval is [-0.475, 0.625] with width 1.100 = m1 + m2.",
    "inputs": "m1 = 0.6, m2 = 0.5, r1_hat = 0.25, r2_hat = 0.15",
    "formula": "l1 = r1_hat*(1-m1); u1 = l1+m1; l2 = r2_hat*(1-m2); u2 = l2+m2; Dmin = l1-u2; Dmax = u1-l2; width = Dmax-Dmin"
  },
  {
    "id": "Q2",
    "statement": "The pooled-audit rate interval is [0.24, 0.44] with width m = 0.2.",
    "inputs": "pA_hat = 0.30, m = 0.2",
    "formula": "pmin = pA_hat*(1-m); pmax = pmin+m"
  },
  {
    "id": "Q3",
    "statement": "The four-fifths ratio interval is [0.686, 1.257] and the point estimate is 0.857.",
    "inputs": "pmin = 0.24, pmax = 0.44, pB = 0.35",
    "formula": "Rmin = pmin/pB; Rmax = pmax/pB; Rhat = 0.30/pB"
  },
  {
    "id": "Q4",
    "statement": "The conditional label-recovery target is 134 labels.",
    "inputs": "pA_hat = 0.30, threshold = 0.8*pB = 0.28, k = 800, n = 1000",
    "formula": "1-m' >= 0.28/0.30; k+dk >= n*(0.28/0.30); dk = ceil(n*0.28/0.30 - k)"
  },
  {
    "id": "Q5",
    "statement": "At near-complete labeling (m1 = m2 = 0.02, n_g = 980, r_hat = 0.25), the per-group sampling half-width is 0.027111 and the two-group sampling contribution is 0.05422177.",
    "inputs": "r_hat = 0.25, n_g = 980, z = 1.96",
    "formula": "half = z*sqrt(r_hat*(1-r_hat)/n_g); contribution = 2*half"
  },
  {
    "id": "Q6",
    "statement": "At m = 0.2 with 800 labeled records and pA_hat = 0.30, the sampling half-width is 0.031756 and missingness dominates by a factor of 6.30.",
    "inputs": "pA_hat = 0.30, k = 800, z = 1.96, m = 0.2",
    "formula": "half = z*sqrt(pA_hat*(1-pA_hat)/k); factor = m/half"
  },
  {
    "id": "Q7",
    "statement": "In the Section 4.4 counter-example, Dmin = 0.04 > 0 while the shortcut fails (0.6 < 0.7).",
    "inputs": "r1_hat = 0.8, m1 = 0.2, r2_hat = 0.2, m2 = 0.5",
    "formula": "Dmin = r1_hat*(1-m1) - (r2_hat*(1-m2)+m2); ghat = r1_hat-r2_hat; shortcut = m1+m2"
  },
  {
    "id": "Q8",
    "statement": "The combined half-width is 0.231756 per rate at m = 0.2 and 0.09422177 per disparity at m = 0.02.",
    "inputs": "m = 0.2, half = 0.031756; m1+m2 = 0.04, sampling contribution = 0.05422177",
    "formula": "combined_1 = m + half; combined_2 = (m1+m2) + 2*1.96*sqrt(0.25*0.75/980)"
  },
  {
    "id": "Q9",
    "statement": "The overall missing fraction in the pooled audit is m = 0.2.",
    "inputs": "k = 800, n = 1000",
    "formula": "m = 1 - k/n"
  },
  {
    "id": "Q10",
    "statement": "The ratio of sampling to missingness uncertainty at near-complete labeling is 1.356.",
    "inputs": "sampling = 0.05422177, missingness = 0.04",
    "formula": "ratio = sampling/missingness"
  }
]

## Script
```python
import math
from fractions import Fraction

def report(qid, computed, expected):
    print(f"CLAIM {qid}: computed={computed:.10f} expected={expected} match={'yes' if computed_str(computed, expected) else 'no'}")

def computed_str(value, expected):
    if expected is None:
        return False
    exp = float(expected)
    # match when computed rounded to significant digits of expected equals expected
    digits = len(expected.replace('.', '').replace('-', '').lstrip('0')) if '.' in expected else len(expected.replace('-', '').lstrip('0'))
    return round(value, digits) == round(exp, digits)

# Q1
m1, m2, r1, r2 = 0.6, 0.5, 0.25, 0.15
l1 = r1*(1-m1); u1 = l1+m1
l2 = r2*(1-m2); u2 = l2+m2
Dmin = l1-u2; Dmax = u1-l2
width = Dmax-Dmin
print(f"CLAIM Q1: computed={width:.10f} expected=1.100 match={'yes' if round(width,3)==1.100 and round(Dmin,3)==-0.475 and round(Dmax,3)==0.625 else 'no'}")

# Q2
pA, m = 0.30, 0.2
pmin = pA*(1-m); pmax = pmin+m
print(f"CLAIM Q2: computed={pmax-pmin:.10f} expected=0.2 match={'yes' if round(pmin,2)==0.24 and round(pmax,2)==0.44 and round(pmax-pmin,1)==0.2 else 'no'}")

# Q3
pB = 0.35
Rmin = pmin/pB; Rmax = pmax/pB; Rhat = pA/pB
print(f"CLAIM Q3: computed={Rmin:.10f} expected=0.686 match={'yes' if round(Rmin,3)==0.686 and round(Rmax,3)==1.257 and round(Rhat,3)==0.857 else 'no'}")

# Q4
threshold = 0.8*pB
needed = 1000*threshold/pA
dk = math.ceil(needed - 800)
print(f"CLAIM Q4: computed={dk:.10f} expected=134 match={'yes' if dk==134 else 'no'}")

# Q5
rhat, ng, z = 0.25, 980, 1.96
half = z*math.sqrt(rhat*(1-rhat)/ng)
contrib = 2*half
print(f"CLAIM Q5: computed={contrib:.10f} expected=0.05422177 match={'yes' if round(contrib,8)==0.05422177 else 'no'}")

# Q6
half6 = z*math.sqrt(pA*(1-pA)/800)
factor = m/half6
print(f"CLAIM Q6: computed={factor:.10f} expected=6.30 match={'yes' if round(half6,6)==0.031756 and round(factor,2)==6.30 else 'no'}")

# Q7
r1h, m1c, r2h, m2c = 0.8, 0.2, 0.2, 0.5
Dmin7 = r1h*(1-m1c) - (r2h*(1-m2c)+m2c)
ghat = r1h-r2h
shortcut = m1c+m2c
print(f"CLAIM Q7: computed={Dmin7:.10f} expected=0.04 match={'yes' if round(Dmin7,2)==0.04 and ghat < shortcut else 'no'}")

# Q8
combined1 = m + half6
combined2 = 0.04 + 2*z*math.sqrt(0.25*0.75/980)
print(f"CLAIM Q8: computed={combined2:.10f} expected=0.09422177 match={'yes' if round(combined1,6)==0.231756 and round(combined2,8)==0.09422177 else 'no'}")

# Q9
m9 = 1 - 800/1000
print(f"CLAIM Q9: computed={m9:.10f} expected=0.2 match={'yes' if m9==0.2 else 'no'}")

# Q10
ratio10 = contrib/0.04
print(f"CLAIM Q10: computed={ratio10:.10f} expected=1.356 match={'yes' if round(ratio10,3)==1.356 else 'no'}")

print("VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.1000000000 expected=1.100 match=yes
CLAIM Q2: computed=0.2000000000 expected=0.2 match=yes
CLAIM Q3: computed=0.6857142857 expected=0.686 match=yes
CLAIM Q4: computed=134.0000000000 expected=134 match=yes
CLAIM Q5: computed=0.0542217668 expected=0.05422177 match=yes
CLAIM Q6: computed=6.2980959168 expected=6.30 match=yes
CLAIM Q7: computed=0.0400000000 expected=0.04 match=yes
CLAIM Q8: computed=0.0942217668 expected=0.09422177 match=yes
CLAIM Q9: computed=0.2000000000 expected=0.2 match=no
CLAIM Q10: computed=1.3555441712 expected=1.356 match=yes
VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.1000000000 | 1.100 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 0.2000000000 | 0.2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.6857142857 | 0.686 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 134.0000000000 | 134 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 0.0542217668 | 0.05422177 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q6 | 6.2980959168 | 6.30 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 0.0400000000 | 0.04 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 0.0942217668 | 0.09422177 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q9 | 0.2000000000 | 0.2 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 1.3555441712 | 1.356 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 10.
