# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The Jackiw–Rebbi domain‑wall energy splitting for a separation L/ξ=10 is ΔE = e^{-10} = 4.539992976×10^{-5} ≈ 4.54×10^{-5}.",
    "inputs": "L/ξ = 10",
    "formula": "ΔE = exp(-L/ξ)"
  },
  {
    "id": "Q2",
    "statement": "The dimensionless product of the pion decay constant and box size is F L ≈ 36.6.",
    "inputs": "F = 93 MeV, conversion 1 MeV^{-1}=0.197 fm, L = 2 fm",
    "formula": "F (fm^{-1}) = F (MeV) × 0.197;  F L = F (fm^{-1}) × L"
  },
  {
    "id": "Q3",
    "statement": "The thermal energy scale from the graphene vacancy model is T ≈ 0.0303 eV.",
    "inputs": "t = 3.03 eV, β = 100 / t",
    "formula": "β = 100 / t;  T = 1 / β"
  },
  {
    "id": "Q4",
    "statement": "The leading finite‑size correction scales as (F L)^{-2} ≈ 7.5×10^{-4}.",
    "inputs": "F L ≈ 36.6",
    "formula": "(F L)^{-2} = 1 / (F L)^2"
  }
]

## Script
```python
import math

# Q1: Jackiw–Rebbi splitting ΔE = exp(-L/ξ) with L/ξ = 10
L_over_xi = 10
delta_E = math.exp(-L_over_xi)
expected_Q1 = "4.539992976e-05"
match_Q1 = "yes" if f"{delta_E:.12e}"[:13] == expected_Q1 else "no"
print(f"CLAIM Q1: computed={delta_E:.12e} expected={expected_Q1} match={match_Q1}")

# Q2: Dimensionless product F L
F_MeV = 93.0
conversion = 0.197  # fm per MeV^{-1}
F_fm_inv = F_MeV * conversion
L_fm = 2.0
FL = F_fm_inv * L_fm
expected_Q2 = "36.6"
# round to one decimal place as in claim
FL_rounded = round(FL, 1)
match_Q2 = "yes" if f"{FL_rounded:.1f}" == expected_Q2 else "no"
print(f"CLAIM Q2: computed={FL_rounded:.1f} expected={expected_Q2} match={match_Q2}")

# Q3: Thermal scale T = 1/β with β = 100 / t, t = 3.03 eV
t = 3.03
beta = 100.0 / t
T = 1.0 / beta
expected_Q3 = "0.0303"
# round to 4 decimal places as in claim
T_rounded = round(T, 4)
match_Q3 = "yes" if f"{T_rounded:.4f}" == expected_Q3 else "no"
print(f"CLAIM Q3: computed={T_rounded:.4f} expected={expected_Q3} match={match_Q3}")

# Q4: Leading finite-size correction (F L)^{-2} with F L ≈ 36.6
FL_approx = 36.6
correction = 1.0 / (FL_approx ** 2)
expected_Q4 = "7.5e-04"
# format in scientific notation with two significant digits
correction_formatted = f"{correction:.2e}"
match_Q4 = "yes" if correction_formatted == expected_Q4 else "no"
print(f"CLAIM Q4: computed={correction_formatted} expected={expected_Q4} match={match_Q4}")

print(f"VERIFICATION SUMMARY: 4 claims, {sum([match_Q1, match_Q2, match_Q3, match_Q4].count('yes'))} match, {sum([match_Q1, match_Q2, match_Q3, match_Q4].count('no'))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=4.539992976248e-05 expected=4.539992976e-05 match=no
CLAIM Q2: computed=36.6 expected=36.6 match=yes
CLAIM Q3: computed=0.0303 expected=0.0303 match=yes
CLAIM Q4: computed=7.47e-04 expected=7.5e-04 match=no

[stderr]
Traceback (most recent call last):
  File "<string>", line 41, in <module>
TypeError: 'int' object is not iterable

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 4.539992976248e-05 | 4.539992976e-05 | no | match | 10 significant digits (as the paper states, at least 2) |
| Q2 | 36.6 | 36.6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 0.0303 | 0.0303 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 7.47e-04 | 7.5e-04 | no | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 4.
