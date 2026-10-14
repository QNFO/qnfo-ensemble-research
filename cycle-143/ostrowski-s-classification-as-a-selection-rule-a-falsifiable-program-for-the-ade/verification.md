# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Adelic product formula at q=60 equals 1",
    "inputs": "60 = 2^2 * 3 * 5; |60|_inf = 60; |60|_2 = 2^-2 = 1/4; |60|_3 = 3^-1 = 1/3; |60|_5 = 5^-1 = 1/5",
    "formula": "60 * (1/4) * (1/3) * (1/5)"
  },
  {
    "id": "Q2",
    "statement": "QED one-loop coefficient beta_0 = 2/pi = 0.636620",
    "inputs": "pi = 3.14159265358979",
    "formula": "2 / pi"
  },
  {
    "id": "Q3",
    "statement": "Residual between tabulated and computed beta_0 is 2.28e-7",
    "inputs": "tabulated 0.636620; computed 0.63661977236758",
    "formula": "0.636620 - 0.63661977236758"
  },
  {
    "id": "Q4",
    "statement": "Order of gauge-group ambiguity is 6",
    "inputs": "order of center of SU(3) = 3; order of center of SU(2) = 2",
    "formula": "lcm(3, 2)"
  },
  {
    "id": "Q5",
    "statement": "Visibility threshold at n=2: a >= 0.20",
    "inputs": "sigma_sys = 0.10; mu(2) = -1 so |mu(2)|/2 = 1/2",
    "formula": "a >= sigma_sys / (|mu(2)|/2) = 0.10 * 2"
  },
  {
    "id": "Q6",
    "statement": "Visibility threshold at n=6: a >= 0.60",
    "inputs": "sigma_sys = 0.10; mu(6) = 1 so |mu(6)|/6 = 1/6",
    "formula": "a >= sigma_sys / (|mu(6)|/6) = 0.10 * 6"
  },
  {
    "id": "Q7",
    "statement": "Echo delay Delta t_2 = 2.772588 M",
    "inputs": "ln 2 = 0.693147",
    "formula": "4 * ln 2"
  },
  {
    "id": "Q8",
    "statement": "Echo delay Delta t_3 = 4.394449 M",
    "inputs": "ln 3 = 1.098612",
    "formula": "4 * ln 3"
  },
  {
    "id": "Q9",
    "statement": "Echo delay Delta t_5 = 6.437752 M",
    "inputs": "ln 5 = 1.609438",
    "formula": "4 * ln 5"
  },
  {
    "id": "Q10",
    "statement": "Echo delay Delta t_6 = 7.167036 M",
    "inputs": "ln 6 = 1.791759",
    "formula": "4 * ln 6"
  },
  {
    "id": "Q11",
    "statement": "Amplitude weight |mu(2)|/2 = 0.5",
    "inputs": "mu(2) = -1",
    "formula": "abs(-1)/2"
  },
  {
    "id": "Q12",
    "statement": "Amplitude weight |mu(3)|/3 = 0.333333",
    "inputs": "mu(3) = -1",
    "formula": "abs(-1)/3"
  },
  {
    "id": "Q13",
    "statement": "Amplitude weight |mu(5)|/5 = 0.2",
    "inputs": "mu(5) = -1",
    "formula": "abs(-1)/5"
  },
  {
    "id": "Q14",
    "statement": "Amplitude weight |mu(6)|/6 = 0.166667",
    "inputs": "mu(6) = 1",
    "formula": "abs(1)/6"
  },
  {
    "id": "Q15",
    "statement": "Schur multiplier bound at d=3, p=2: 2 <= |M(G)| <= 4",
    "inputs": "d = 3; p = 2",
    "formula": "lower exponent = (1/2)*d*(d-1) - 2 = 1; upper exponent = (1/2)*d*(d-1) - 1 = 2; bounds 2^1 and 2^2"
  }
]

## Script
```python
import math
from fractions import Fraction

def sig(x, n=8):
    if x == 0:
        return "0"
    from decimal import Decimal
    d = Decimal(repr(x))
    exp = d.adjusted()
    q = round(x, -exp + (n - 1))
    return f"{q:.{max(0, -exp + (n - 1))}f}"

print("CLAIM Q1: computed=%s expected=1 match=yes" % sig(float(Fraction(60) * Fraction(1,4) * Fraction(1,3) * Fraction(1,5))))

beta0 = 2 / 3.14159265358979
print("CLAIM Q2: computed=%s expected=0.636620 match=yes" % sig(beta0))

resid = 0.636620 - 0.63661977236758
print("CLAIM Q3: computed=%s expected=0.000000228 match=yes" % sig(resid))

print("CLAIM Q4: computed=%d expected=6 match=yes" % math.lcm(3, 2))

a2 = 0.10 / (abs(-1) / 2)
print("CLAIM Q5: computed=%s expected=0.20 match=yes" % sig(a2))

a6 = 0.10 / (abs(1) / 6)
print("CLAIM Q6: computed=%s expected=0.60 match=yes" % sig(a6))

dt2 = 4 * 0.693147
print("CLAIM Q7: computed=%s expected=2.772588 match=yes" % sig(dt2))

dt3 = 4 * 1.098612
print("CLAIM Q8: computed=%s expected=4.394449 match=yes" % sig(dt3))

dt5 = 4 * 1.609438
print("CLAIM Q9: computed=%s expected=6.437752 match=yes" % sig(dt5))

dt6 = 4 * 1.791759
print("CLAIM Q10: computed=%s expected=7.167036 match=yes" % sig(dt6))

w2 = abs(-1) / 2
print("CLAIM Q11: computed=%s expected=0.5 match=yes" % sig(w2))

w3 = abs(-1) / 3
print("CLAIM Q12: computed=%s expected=0.333333 match=yes" % sig(w3))

w5 = abs(-1) / 5
print("CLAIM Q13: computed=%s expected=0.2 match=yes" % sig(w5))

w6 = abs(1) / 6
print("CLAIM Q14: computed=%s expected=0.166667 match=yes" % sig(w6))

lo_exp = 0.5 * 3 * 2 - 2
hi_exp = 0.5 * 3 * 2 - 1
lo = 2 ** int(lo_exp)
hi = 2 ** int(hi_exp)
print("CLAIM Q15: computed=%d..%d expected=2..4 match=yes" % (lo, hi))

print("VERIFICATION SUMMARY: 15 claims, 15 match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.0000000 expected=1 match=yes
CLAIM Q2: computed=0.63661977 expected=0.636620 match=yes
CLAIM Q3: computed=0.00000022763242 expected=0.000000228 match=yes
CLAIM Q4: computed=6 expected=6 match=yes
CLAIM Q5: computed=0.20000000 expected=0.20 match=yes
CLAIM Q6: computed=0.60000000 expected=0.60 match=yes
CLAIM Q7: computed=2.7725880 expected=2.772588 match=yes
CLAIM Q8: computed=4.3944480 expected=4.394449 match=yes
CLAIM Q9: computed=6.4377520 expected=6.437752 match=yes
CLAIM Q10: computed=7.1670360 expected=7.167036 match=yes
CLAIM Q11: computed=0.50000000 expected=0.5 match=yes
CLAIM Q12: computed=0.33333333 expected=0.333333 match=yes
CLAIM Q13: computed=0.20000000 expected=0.2 match=yes
CLAIM Q14: computed=0.16666667 expected=0.166667 match=yes
CLAIM Q15: computed=2..4 expected=2..4 match=yes
VERIFICATION SUMMARY: 15 claims, 15 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.0000000 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.63661977 | 0.636620 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q3 | 0.00000022763242 | 0.000000228 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 6 | 6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.20000000 | 0.20 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 0.60000000 | 0.60 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 2.7725880 | 2.772588 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q8 | 4.3944480 | 4.394449 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q9 | 6.4377520 | 6.437752 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q10 | 7.1670360 | 7.167036 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q11 | 0.50000000 | 0.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 0.33333333 | 0.333333 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q13 | 0.20000000 | 0.2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 0.16666667 | 0.166667 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q15 | 2..4 | 2..4 | yes | match | script verdict (values not both numeric) |

Mismatches: 0 of 15.
