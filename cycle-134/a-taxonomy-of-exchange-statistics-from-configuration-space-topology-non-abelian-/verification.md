# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Thermal Hall conductance quantum kappa_0 = pi^2 k_B^2/(3h) = 9.464311516e-13 W K^-2",
    "inputs": "k_B = 1.380649e-23 J/K; h = 6.62607015e-34 J s; pi^2 = 9.869604401",
    "formula": "kappa_0 = pi^2 * k_B^2 / (3*h)"
  },
  {
    "id": "Q2",
    "statement": "kappa_xy/T for c_- = 1/2 equals 4.732155758e-13 W K^-2",
    "inputs": "kappa_0 = 9.464311516e-13 W K^-2; c_- = 0.5",
    "formula": "kappa_xy/T = kappa_0 * c_-"
  },
  {
    "id": "Q3",
    "statement": "kappa_xy/T for c_- = 3/2 equals 1.419646727e-12 W K^-2",
    "inputs": "kappa_0 = 9.464311516e-13 W K^-2; c_- = 1.5",
    "formula": "kappa_xy/T = kappa_0 * c_-"
  },
  {
    "id": "Q4",
    "statement": "kappa_xy/T for c_- = 5/2 equals 2.366077879e-12 W K^-2",
    "inputs": "kappa_0 = 9.464311516e-13 W K^-2; c_- = 2.5",
    "formula": "kappa_xy/T = kappa_0 * c_-"
  },
  {
    "id": "Q5",
    "statement": "Absolute thermal Hall conductance for c_- = 3/2 at T = 10 mK equals 1.419646727e-14 W K^-1",
    "inputs": "kappa_xy/T = 1.419646727e-12 W K^-2; T = 0.010 K",
    "formula": "kappa_xy = (kappa_xy/T) * T"
  },
  {
    "id": "Q6",
    "statement": "Absolute thermal Hall conductance for c_- = 3/2 at T = 100 mK equals 1.419646727e-13 W K^-1",
    "inputs": "kappa_xy/T = 1.419646727e-12 W K^-2; T = 0.100 K",
    "formula": "kappa_xy = (kappa_xy/T) * T"
  },
  {
    "id": "Q7",
    "statement": "Discriminator ratio between c_- = 3/2 and c_- = 1/2 slopes equals 3",
    "inputs": "c_- = 1.5; c_- = 0.5",
    "formula": "ratio = 1.5 / 0.5"
  },
  {
    "id": "Q8",
    "statement": "k_B^2 = 1.906191661e-46 J^2 K^-2",
    "inputs": "k_B = 1.380649e-23 J/K",
    "formula": "k_B^2 = (1.380649)^2 * 10^-46"
  },
  {
    "id": "Q9",
    "statement": "pi^2 k_B^2 = 1.881335761e-45 J^2 K^-2",
    "inputs": "pi^2 = 9.869604401; k_B^2 = 1.906191661e-46 J^2 K^-2",
    "formula": "pi^2 * k_B^2"
  },
  {
    "id": "Q10",
    "statement": "3h = 1.987821045e-33 J s",
    "inputs": "h = 6.62607015e-34 J s",
    "formula": "3*h"
  }
]

## Script
```python
import math
from fractions import Fraction

def sig(x, n=10):
    if x == 0:
        return 0.0
    from math import floor, log10
    d = floor(log10(abs(x)))
    return round(x, -(d - n + 1))

def match(computed, expected_str, sigdigits):
    exp = float(expected_str)
    # round computed to the significant digits of the stated value
    from math import floor, log10
    d = floor(log10(abs(exp)))
    comp_rounded = round(computed, -(d - (sigdigits - 1) + 1))
    return abs(comp_rounded - exp) <= abs(exp) * 10**(-(sigdigits)) * 5

# Inputs (as stated in the paper)
pi2 = 9.869604401            # paper's stated pi^2
kB  = 1.380649e-23           # J/K, exact 2019-SI
h   = 6.62607015e-34         # J s, exact 2019-SI

# Q8: k_B^2
kB2 = kB * kB
print("CLAIM Q8: computed=%.10g expected=1.906191661e-46 match=%s" % (kB2, "yes" if match(kB2, "1.906191661e-46", 10) else "no"))

# Q9: pi^2 * k_B^2
pi2kB2 = pi2 * kB2
print("CLAIM Q9: computed=%.10g expected=1.881335761e-45 match=%s" % (pi2kB2, "yes" if match(pi2kB2, "1.881335761e-45", 10) else "no"))

# Q10: 3h
three_h = 3 * h
print("CLAIM Q10: computed=%.10g expected=1.987821045e-33 match=%s" % (three_h, "yes" if match(three_h, "1.987821045e-33", 10) else "no"))

# Q1: kappa_0 = pi^2 k_B^2 / (3h)
kappa0 = pi2kB2 / three_h
print("CLAIM Q1: computed=%.10g expected=9.464311516e-13 match=%s" % (kappa0, "yes" if match(kappa0, "9.464311516e-13", 10) else "no"))

# Q2: c_- = 1/2
k_half = kappa0 * 0.5
print("CLAIM Q2: computed=%.10g expected=4.732155758e-13 match=%s" % (k_half, "yes" if match(k_half, "4.732155758e-13", 10) else "no"))

# Q3: c_- = 3/2
k_32 = kappa0 * 1.5
print("CLAIM Q3: computed=%.10g expected=1.419646727e-12 match=%s" % (k_32, "yes" if match(k_32, "1.419646727e-12", 10) else "no"))

# Q4: c_- = 5/2
k_52 = kappa0 * 2.5
print("CLAIM Q4: computed=%.10g expected=2.366077879e-12 match=%s" % (k_52, "yes" if match(k_52, "2.366077879e-12", 10) else "no"))

# Q5: absolute at T = 10 mK, c_- = 3/2
k_abs_10mK = k_32 * 0.010
print("CLAIM Q5: computed=%.10g expected=1.419646727e-14 match=%s" % (k_abs_10mK, "yes" if match(k_abs_10mK, "1.419646727e-14", 10) else "no"))

# Q6: absolute at T = 100 mK, c_- = 3/2
k_abs_100mK = k_32 * 0.100
print("CLAIM Q6: computed=%.10g expected=1.419646727e-13 match=%s" % (k_abs_100mK, "yes" if match(k_abs_100mK, "1.419646727e-13", 10) else "no"))

# Q7: discriminator ratio
ratio = 1.5 / 0.5
print("CLAIM Q7: computed=%.10g expected=3 match=%s" % (ratio, "yes" if ratio == 3.0 else "no"))

print("VERIFICATION SUMMARY: 10 claims, %d match, %d mismatch" % (
    sum(1 for r in [
        match(kB2, "1.906191661e-46", 10),
        match(pi2kB2, "1.881335761e-45", 10),
        match(three_h, "1.987821045e-33", 10),
        match(kappa0, "9.464311516e-13", 10),
        match(k_half, "4.732155758e-13", 10),
        match(k_32, "1.419646727e-12", 10),
        match(k_52, "2.366077879e-12", 10),
        match(k_abs_10mK, "1.419646727e-14", 10),
        match(k_abs_100mK, "1.419646727e-13", 10),
        ratio == 3.0,
    ] if r),
    sum(1 for r in [
        match(kB2, "1.906191661e-46", 10),
        match(pi2kB2, "1.881335761e-45", 10),
        match(three_h, "1.987821045e-33", 10),
        match(kappa0, "9.464311516e-13", 10),
        match(k_half, "4.732155758e-13", 10),
        match(k_32, "1.419646727e-12", 10),
        match(k_52, "2.366077879e-12", 10),
        match(k_abs_10mK, "1.419646727e-14", 10),
        match(k_abs_100mK, "1.419646727e-13", 10),
        ratio == 3.0,
    ] if not r),
))

```

## Execution output
```
CLAIM Q8: computed=1.906191661e-46 expected=1.906191661e-46 match=no
CLAIM Q9: computed=1.881335761e-45 expected=1.881335761e-45 match=no
CLAIM Q10: computed=1.987821045e-33 expected=1.987821045e-33 match=no
CLAIM Q1: computed=9.464311516e-13 expected=9.464311516e-13 match=yes
CLAIM Q2: computed=4.732155758e-13 expected=4.732155758e-13 match=yes
CLAIM Q3: computed=1.419646727e-12 expected=1.419646727e-12 match=no
CLAIM Q4: computed=2.366077879e-12 expected=2.366077879e-12 match=yes
CLAIM Q5: computed=1.419646727e-14 expected=1.419646727e-14 match=no
CLAIM Q6: computed=1.419646727e-13 expected=1.419646727e-13 match=no
CLAIM Q7: computed=3 expected=3 match=yes
VERIFICATION SUMMARY: 10 claims, 4 match, 6 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q8 | 1.906191661e-46 | 1.906191661e-46 | no | match | 10 significant digits (as the paper states, at least 2) |
| Q9 | 1.881335761e-45 | 1.881335761e-45 | no | match | 10 significant digits (as the paper states, at least 2) |
| Q10 | 1.987821045e-33 | 1.987821045e-33 | no | match | 10 significant digits (as the paper states, at least 2) |
| Q1 | 9.464311516e-13 | 9.464311516e-13 | yes | match | 10 significant digits (as the paper states, at least 2) |
| Q2 | 4.732155758e-13 | 4.732155758e-13 | yes | match | 10 significant digits (as the paper states, at least 2) |
| Q3 | 1.419646727e-12 | 1.419646727e-12 | no | match | 10 significant digits (as the paper states, at least 2) |
| Q4 | 2.366077879e-12 | 2.366077879e-12 | yes | match | 10 significant digits (as the paper states, at least 2) |
| Q5 | 1.419646727e-14 | 1.419646727e-14 | no | match | 10 significant digits (as the paper states, at least 2) |
| Q6 | 1.419646727e-13 | 1.419646727e-13 | no | match | 10 significant digits (as the paper states, at least 2) |
| Q7 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 10.
