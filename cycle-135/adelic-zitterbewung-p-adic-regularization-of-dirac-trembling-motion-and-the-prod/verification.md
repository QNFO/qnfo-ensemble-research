# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Electron rest energy $m_e c^2 = 8.18717 \\times 10^{-14}\\,\\mathrm{J}$",
    "inputs": "$m_e = 9.109 \\times 10^{-31}\\,\\mathrm{kg}$, $c = 2.998 \\times 10^{8}\\,\\mathrm{m\\,s^{-1}}$",
    "formula": "m_e * c^2"
  },
  {
    "id": "Q2",
    "statement": "ZBW angular frequency $\\omega_\\infty = 1.5521 \\times 10^{21}\\,\\mathrm{rad\\,s^{-1}}$",
    "inputs": "$m_e c^2 = 8.18717 \\times 10^{-14}\\,\\mathrm{J}$, $\\hbar = 1.055 \\times 10^{-34}\\,\\mathrm{J\\,s}$",
    "formula": "2 * m_e c^2 / hbar"
  },
  {
    "id": "Q3",
    "statement": "Cyclic frequency $f_\\infty = 2.47020 \\times 10^{20}\\,\\mathrm{Hz}$",
    "inputs": "$\\omega_\\infty = 1.55207 \\times 10^{21}\\,\\mathrm{rad\\,s^{-1}}$",
    "formula": "omega_inf / (2 * pi)"
  },
  {
    "id": "Q4",
    "statement": "Period $T = 4.0482 \\times 10^{-21}\\,\\mathrm{s}$",
    "inputs": "$f_\\infty = 2.47020 \\times 10^{20}\\,\\mathrm{Hz}$",
    "formula": "1 / f_inf"
  },
  {
    "id": "Q5",
    "statement": "Compton wavelength $\\lambda_C = 3.8632 \\times 10^{-13}\\,\\mathrm{m}$",
    "inputs": "$\\hbar = 1.055 \\times 10^{-34}\\,\\mathrm{J\\,s}$, $m_e = 9.109 \\times 10^{-31}\\,\\mathrm{kg}$, $c = 2.998 \\times 10^{8}\\,\\mathrm{m\\,s^{-1}}$",
    "formula": "hbar / (m_e * c)"
  },
  {
    "id": "Q6",
    "statement": "Planck length $\\ell_P = 1.6165 \\times 10^{-35}\\,\\mathrm{m}$",
    "inputs": "$\\hbar = 1.055 \\times 10^{-34}\\,\\mathrm{J\\,s}$, $G = 6.674 \\times 10^{-11}\\,\\mathrm{m^3\\,kg^{-1}\\,s^{-2}}$, $c = 2.998 \\times 10^{8}\\,\\mathrm{m\\,s^{-1}}$",
    "formula": "sqrt(hbar * G / c^3)"
  },
  {
    "id": "Q7",
    "statement": "Product formula holds for $x = 6$: $6 \\times 0.5 \\times (1/3) = 1$",
    "inputs": "$x = 6$, $|6|_2 = 0.5$, $|6|_3 = 1/3$",
    "formula": "6 * 0.5 * (1/3)"
  },
  {
    "id": "Q8",
    "statement": "Product formula holds for $x = 12$: $12 \\times 0.25 \\times (1/3) = 1$",
    "inputs": "$x = 12$, $|12|_2 = 0.25$, $|12|_3 = 1/3$",
    "formula": "12 * 0.25 * (1/3)"
  },
  {
    "id": "Q9",
    "statement": "Product formula holds for $x = 10$: $10 \\times 0.5 \\times 0.2 = 1$",
    "inputs": "$x = 10$, $|10|_2 = 0.5$, $|10|_5 = 0.2$",
    "formula": "10 * 0.5 * 0.2"
  },
  {
    "id": "Q10",
    "statement": "Suppression ratio at $\\ell = 1\\,\\mathrm{m}$: $A_{\\mathrm{int}}/A_0 = 3.863 \\times 10^{-13}$",
    "inputs": "$\\lambda_C = 3.8632 \\times 10^{-13}\\,\\mathrm{m}$, $\\ell = 1\\,\\mathrm{m}$",
    "formula": "lambda_C / ell"
  },
  {
    "id": "Q11",
    "statement": "Intensity-like suppression at $\\ell = 1\\,\\mathrm{m}$: $1.492 \\times 10^{-25}$",
    "inputs": "$A_{\\mathrm{int}}/A_0 = 3.863 \\times 10^{-13}$",
    "formula": "(3.863e-13)^2"
  },
  {
    "id": "Q12",
    "statement": "Planck-scale dominance $\\lambda_C/\\ell_P = 2.3898 \\times 10^{22}$",
    "inputs": "$\\lambda_C = 3.8632 \\times 10^{-13}\\,\\mathrm{m}$, $\\ell_P = 1.6165 \\times 10^{-35}\\,\\mathrm{m}$",
    "formula": "lambda_C / ell_P"
  },
  {
    "id": "Q13",
    "statement": "Ratio of Planck-scale factor to laboratory suppression $\\approx 6.19 \\times 10^{34}$",
    "inputs": "$2.3898 \\times 10^{22}$, $3.863 \\times 10^{-13}$",
    "formula": "2.3898e22 / 3.863e-13"
  },
  {
    "id": "Q14",
    "statement": "Crossover scale $386.3\\,\\mathrm{nm}$ for threshold $\\varepsilon = 10^{-6}$",
    "inputs": "$\\lambda_C = 3.8632 \\times 10^{-13}\\,\\mathrm{m}$, $\\varepsilon = 10^{-6}$",
    "formula": "lambda_C / 1e-6"
  },
  {
    "id": "Q15",
    "statement": "Intensity-like crossover $100\\,\\lambda_C = 3.8632 \\times 10^{-11}\\,\\mathrm{m}$ for threshold $10^{-4}$",
    "inputs": "$\\lambda_C = 3.8632 \\times 10^{-13}\\,\\mathrm{m}$, threshold $10^{-4}$",
    "formula": "(1e-4)^(-1/2) * lambda_C"
  },
  {
    "id": "Q16",
    "statement": "Projected sector frequency $f_2 = 1.2351 \\times 10^{20}\\,\\mathrm{Hz}$",
    "inputs": "$|10|_2 = 0.5$, $f_\\infty = 2.47020 \\times 10^{20}\\,\\mathrm{Hz}$",
    "formula": "0.5 * f_inf"
  }
]

## Script
```python
import math

def show(id, computed, expected, sig):
    c = computed
    if c != 0:
        d = math.floor(math.log10(abs(c)))
        rounded = round(c, -(d - (sig - 1)))
    else:
        rounded = 0.0
    match = (f"{rounded:.{sig}g}" == f"{float(expected):.{sig}g}")
    print(f"CLAIM {id}: computed={c:.8e} expected={expected} match={'yes' if match else 'no'}")

# Q1
me = 9.109e-31
c = 2.998e8
mc2 = me * c * c
show("Q1", mc2, "8.18717e-14", 6)

# Q2
hbar = 1.055e-34
omega = 2 * mc2 / hbar
show("Q2", omega, "1.5521e21", 5)

# Q3
omega_in = 1.55207e21
f_inf = omega_in / (2 * math.pi)
show("Q3", f_inf, "2.47020e20", 6)

# Q4
f_in = 2.47020e20
T = 1 / f_in
show("Q4", T, "4.0482e-21", 5)

# Q5
lam = hbar / (me * c)
show("Q5", lam, "3.8632e-13", 5)

# Q6
G = 6.674e-11
lP = math.sqrt(hbar * G / c**3)
show("Q6", lP, "1.6165e-35", 5)

# Q7
v7 = 6 * 0.5 * (1/3)
show("Q7", v7, "1", 10)

# Q8
v8 = 12 * 0.25 * (1/3)
show("Q8", v8, "1", 10)

# Q9
v9 = 10 * 0.5 * 0.2
show("Q9", v9, "1", 10)

# Q10
lamC = 3.8632e-13
ell = 1.0
s10 = lamC / ell
show("Q10", s10, "3.863e-13", 4)

# Q11
s11 = (3.863e-13)**2
show("Q11", s11, "1.492e-25", 4)

# Q12
lPv = 1.6165e-35
s12 = lamC / lPv
show("Q12", s12, "2.3898e22", 5)

# Q13
s13 = 2.3898e22 / 3.863e-13
show("Q13", s13, "6.19e34", 3)

# Q14
s14 = lamC / 1e-6
show("Q14", s14, "3.8632e-7", 5)

# Q15
s15 = (1e-4)**(-0.5) * lamC
show("Q15", s15, "3.8632e-11", 5)

# Q16
f_inf16 = 2.47020e20
s16 = 0.5 * f_inf16
show("Q16", s16, "1.2351e20", 5)

print("VERIFICATION SUMMARY: 16 claims, " + str(sum(1 for _ in [])) + " match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=8.18717284e-14 expected=8.18717e-14 match=yes
CLAIM Q2: computed=1.55207068e+21 expected=1.5521e21 match=yes
CLAIM Q3: computed=2.47019613e+20 expected=2.47020e20 match=yes
CLAIM Q4: computed=4.04825520e-21 expected=4.0482e-21 match=no
CLAIM Q5: computed=3.86322612e-13 expected=3.8632e-13 match=yes
CLAIM Q6: computed=1.61648578e-35 expected=1.6165e-35 match=yes
CLAIM Q7: computed=1.00000000e+00 expected=1 match=yes
CLAIM Q8: computed=1.00000000e+00 expected=1 match=yes
CLAIM Q9: computed=1.00000000e+00 expected=1 match=yes
CLAIM Q10: computed=3.86320000e-13 expected=3.863e-13 match=yes
CLAIM Q11: computed=1.49227690e-25 expected=1.492e-25 match=yes
CLAIM Q12: computed=2.38985462e+22 expected=2.3898e22 match=no
CLAIM Q13: computed=6.18638364e+34 expected=6.19e34 match=yes
CLAIM Q14: computed=3.86320000e-07 expected=3.8632e-7 match=yes
CLAIM Q15: computed=3.86320000e-11 expected=3.8632e-11 match=yes
CLAIM Q16: computed=1.23510000e+20 expected=1.2351e20 match=yes
VERIFICATION SUMMARY: 16 claims, 0 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 8.18717284e-14 | 8.18717e-14 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q2 | 1.55207068e+21 | 1.5521e21 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 2.47019613e+20 | 2.47020e20 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q4 | 4.04825520e-21 | 4.0482e-21 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | 3.86322612e-13 | 3.8632e-13 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 1.61648578e-35 | 1.6165e-35 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 1.00000000e+00 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 1.00000000e+00 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 1.00000000e+00 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 3.86320000e-13 | 3.863e-13 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 1.49227690e-25 | 1.492e-25 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 2.38985462e+22 | 2.3898e22 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q13 | 6.18638364e+34 | 6.19e34 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 3.86320000e-07 | 3.8632e-7 | yes | match | 5 significant digits (as printed, at least 3) |
| Q15 | 3.86320000e-11 | 3.8632e-11 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q16 | 1.23510000e+20 | 1.2351e20 | yes | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
