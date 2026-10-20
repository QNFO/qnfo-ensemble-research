# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The Euclidean distances are d₁₃ = |x₁−x₃| = 2, d₂₄ = |x₂−x₄| = 3, d₁₂ = |x₁−x₂| = 1, d₃₄ = |x₃−x₄| = 2.",
    "inputs": "x₁=0, x₂=1, x₃=2, x₄=4",
    "formula": "d_{ij}=|x_i - x_j|"
  },
  {
    "id": "Q2",
    "statement": "The cross‑ratio for the four points is CR = (d₁₃·d₂₄)/(d₁₂·d₃₄) = 3.0.",
    "inputs": "d₁₃=2, d₂₄=3, d₁₂=1, d₃₄=2",
    "formula": "CR = (d_{13} * d_{24}) / (d_{12} * d_{34})"
  },
  {
    "id": "Q3",
    "statement": "After applying the homothetic scaling φ(s)=3s, the scaled distances are \\tilde d₁₃=6, \\tilde d₂₄=9, \\tilde d₁₂=3, \\tilde d₃₄=6.",
    "inputs": "d₁₃=2, d₂₄=3, d₁₂=1, d₃₄=2, c=3",
    "formula": "\\tilde d_{ij}=c * d_{ij}"
  },
  {
    "id": "Q4",
    "statement": "The scaled cross‑ratio is \\tilde{CR}= (6·9)/(3·6)=3.0, identical to the original value.",
    "inputs": "\\tilde d₁₃=6, \\tilde d₂₄=9, \\tilde d₁₂=3, \\tilde d₃₄=6",
    "formula": "\\tilde{CR} = (\\tilde d_{13} * \\tilde d_{24}) / (\\tilde d_{12} * \\tilde d_{34})"
  },
  {
    "id": "Q5",
    "statement": "The classical electron radius is r_e = 2.81794×10⁻¹⁵ m and the Compton wavelength is λ_c = 2.42631×10⁻¹² m.",
    "inputs": "",
    "formula": ""
  },
  {
    "id": "Q6",
    "statement": "The cross‑ratio built from these lengths is CR_α = r_e / λ_c = 1.1614×10⁻³.",
    "inputs": "r_e=2.81794e-15, λ_c=2.42631e-12",
    "formula": "CR_α = r_e / λ_c"
  },
  {
    "id": "Q7",
    "statement": "Assuming the linear proportionality α = 2π·CR_α, the projected fine‑structure constant is α_proj = 7.2973×10⁻³.",
    "inputs": "CR_α=1.1614e-3, π≈3.1415926535",
    "formula": "α_proj = 2 * π * CR_α"
  },
  {
    "id": "Q8",
    "statement": "The CODATA value is α = 1/137.035999084 = 7.29735×10⁻³.",
    "inputs": "α^{-1}=137.035999084",
    "formula": "α = 1 / α^{-1}"
  },
  {
    "id": "Q9",
    "statement": "The L3 cache capacity is C_L3 = 20 MiB = 20×1024×1024 = 20 971 520 B.",
    "inputs": "20 MiB, 1 MiB = 1024×1024 B",
    "formula": "C_L3 = 20 * 1024 * 1024"
  },
  {
    "id": "Q10",
    "statement": "The cache‑line size is L_line = 64 B.",
    "inputs": "",
    "formula": ""
  },
  {
    "id": "Q11",
    "statement": "The cache‑line to L3‑cache ratio is R_cache = C_L3 / L_line = 327 680.",
    "inputs": "C_L3=20 971 520, L_line=64",
    "formula": "R_cache = C_L3 / L_line"
  },
  {
    "id": "Q12",
    "statement": "With baseline Mach number Ma_t=1.2 and extended value Ma_t=2.0, the ratio is κ_M = 2.0 / 1.2 = 1.666….",
    "inputs": "Ma_extended=2.0, Ma_baseline=1.2",
    "formula": "κ_M = Ma_extended / Ma_baseline"
  },
  {
    "id": "Q13",
    "statement": "Assuming relative uncertainties of 10⁻⁶ for both r_e and λ_c, the combined relative uncertainty is √( (10⁻⁶)² + (10⁻⁶)² ) = 1.4142×10⁻⁶.",
    "inputs": "δr_e/r_e = 1e-6, δλ_c/λ_c = 1e-6",
    "formula": "δ_rel = sqrt( (δr_e/r_e)^2 + (δλ_c/λ_c)^2 )"
  },
  {
    "id": "Q14",
    "statement": "The absolute uncertainty on CR_α is δCR = CR_α × 1.4142×10⁻⁶ ≈ 1.64×10⁻⁹.",
    "inputs": "CR_α=1.1614e-3, δ_rel=1.4142e-6",
    "formula": "δCR = CR_α * δ_rel"
  }
]

## Script
```python
import math

def fmt(val, digits=8):
    # format with at least given significant digits, remove trailing zeros
    s = f"{val:.{digits}g}"
    return s

# Q1: distances
x1, x2, x3, x4 = 0, 1, 2, 4
d13 = abs(x1 - x3)
d24 = abs(x2 - x4)
d12 = abs(x1 - x2)
d34 = abs(x3 - x4)
computed_q1 = f"{d13},{d24},{d12},{d34}"
expected_q1 = "2,3,1,2"
match_q1 = "yes" if computed_q1 == expected_q1 else "no"
print(f"CLAIM Q1: computed={computed_q1} expected={expected_q1} match={match_q1}")

# Q2: cross‑ratio
CR = (d13 * d24) / (d12 * d34)
computed_q2 = fmt(CR, 8)
expected_q2 = "3.0"
match_q2 = "yes" if computed_q2 == expected_q2 else "no"
print(f"CLAIM Q2: computed={computed_q2} expected={expected_q2} match={match_q2}")

# Q3: scaled distances (c=3)
c = 3
d13_s = c * d13
d24_s = c * d24
d12_s = c * d12
d34_s = c * d34
computed_q3 = f"{d13_s},{d24_s},{d12_s},{d34_s}"
expected_q3 = "6,9,3,6"
match_q3 = "yes" if computed_q3 == expected_q3 else "no"
print(f"CLAIM Q3: computed={computed_q3} expected={expected_q3} match={match_q3}")

# Q4: scaled cross‑ratio
CR_s = (d13_s * d24_s) / (d12_s * d34_s)
computed_q4 = fmt(CR_s, 8)
expected_q4 = "3.0"
match_q4 = "yes" if computed_q4 == expected_q4 else "no"
print(f"CLAIM Q4: computed={computed_q4} expected={expected_q4} match={match_q4}")

# Q5: constants
r_e = 2.81794e-15
lam_c = 2.42631e-12
computed_q5 = f"{r_e:.5e},{lam_c:.5e}"
expected_q5 = "2.81794e-15,2.42631e-12"
match_q5 = "yes" if computed_q5 == expected_q5 else "no"
print(f"CLAIM Q5: computed={computed_q5} expected={expected_q5} match={match_q5}")

# Q6: cross‑ratio α
CR_alpha = r_e / lam_c
computed_q6 = fmt(CR_alpha, 8)
expected_q6 = "1.1614e-3"
match_q6 = "yes" if computed_q6 == expected_q6 else "no"
print(f"CLAIM Q6: computed={computed_q6} expected={expected_q6} match={match_q6}")

# Q7: projected fine‑structure constant
alpha_proj = 2 * math.pi * CR_alpha
computed_q7 = fmt(alpha_proj, 8)
expected_q7 = "7.2973e-3"
match_q7 = "yes" if computed_q7 == expected_q7 else "no"
print(f"CLAIM Q7: computed={computed_q7} expected={expected_q7} match={match_q7}")

# Q8: CODATA value
alpha_inv = 137.035999084
alpha_cod = 1 / alpha_inv
computed_q8 = fmt(alpha_cod, 8)
expected_q8 = "7.29735e-3"
match_q8 = "yes" if computed_q8 == expected_q8 else "no"
print(f"CLAIM Q8: computed={computed_q8} expected={expected_q8} match={match_q8}")

# Q9: L3 cache capacity
C_L3 = 20 * 1024 * 1024
computed_q9 = fmt(C_L3, 8)
expected_q9 = "20971520"
match_q9 = "yes" if computed_q9 == expected_q9 else "no"
print(f"CLAIM Q9: computed={computed_q9} expected={expected_q9} match={match_q9}")

# Q10: cache‑line size
L_line = 64
computed_q10 = fmt(L_line, 8)
expected_q10 = "64"
match_q10 = "yes" if computed_q10 == expected_q10 else "no"
print(f"CLAIM Q10: computed={computed_q10} expected={expected_q10} match={match_q10}")

# Q11: cache‑line to L3‑cache ratio
R_cache = C_L3 / L_line
computed_q11 = fmt(R_cache, 8)
expected_q11 = "327680"
match_q11 = "yes" if computed_q11 == expected_q11 else "no"
print(f"CLAIM Q11: computed={computed_q11} expected={expected_q11} match={match_q11}")

# Q12: Mach number scaling
Ma_baseline = 1.2
Ma_extended = 2.0
kappa_M = Ma_extended / Ma_baseline
computed_q12 = fmt(kappa_M, 8)
expected_q12 = "1.666"
match_q12 = "yes" if computed_q12.startswith("1.666") else "no"
print(f"CLAIM Q12: computed={computed_q12} expected={expected_q12} match={match_q12}")

# Q13: combined relative uncertainty
delta_rel = math.sqrt((1e-6)**2 + (1e-6)**2)
computed_q13 = fmt(delta_rel, 8)
expected_q13 = "1.4142e-6"
match_q13 = "yes" if computed_q13 == expected_q13 else "no"
print(f"CLAIM Q13: computed={computed_q13} expected={expected_q13} match={match_q13}")

# Q14: absolute uncertainty on CR_alpha
delta_CR = CR_alpha * delta_rel
computed_q14 = fmt(delta_CR, 8)
expected_q14 = "1.64e-9"
match_q14 = "yes" if computed_q14 == expected_q14 else "no"
print(f"CLAIM Q14: computed={computed_q14} expected={expected_q14} match={match_q14}")

print(f"VERIFICATION SUMMARY: 14 claims, {sum([match_q1,match_q2,match_q3,match_q4,match_q5,match_q6,match_q7,match_q8,match_q9,match_q10,match_q11,match_q12,match_q13,match_q14].count('yes'))} match, {sum([match_q1,match_q2,match_q3,match_q4,match_q5,match_q6,match_q7,match_q8,match_q9,match_q10,match_q11,match_q12,match_q13,match_q14].count('no'))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=2,3,1,2 expected=2,3,1,2 match=yes
CLAIM Q2: computed=3 expected=3.0 match=no
CLAIM Q3: computed=6,9,3,6 expected=6,9,3,6 match=yes
CLAIM Q4: computed=3 expected=3.0 match=no
CLAIM Q5: computed=2.81794e-15,2.42631e-12 expected=2.81794e-15,2.42631e-12 match=yes
CLAIM Q6: computed=0.0011614097 expected=1.1614e-3 match=no
CLAIM Q7: computed=0.0072973524 expected=7.2973e-3 match=no
CLAIM Q8: computed=0.0072973526 expected=7.29735e-3 match=no
CLAIM Q9: computed=20971520 expected=20971520 match=yes
CLAIM Q10: computed=64 expected=64 match=yes
CLAIM Q11: computed=327680 expected=327680 match=yes
CLAIM Q12: computed=1.6666667 expected=1.666 match=yes
CLAIM Q13: computed=1.4142136e-06 expected=1.4142e-6 match=no
CLAIM Q14: computed=1.6424814e-09 expected=1.64e-9 match=no

[stderr]
Traceback (most recent call last):
  File "<string>", line 118, in <module>
TypeError: 'int' object is not iterable

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2,3,1,2 | 2,3,1,2 | yes | match | script verdict (values not both numeric) |
| Q2 | 3 | 3.0 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 6,9,3,6 | 6,9,3,6 | yes | match | script verdict (values not both numeric) |
| Q4 | 3 | 3.0 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 2.81794e-15,2.42631e-12 | 2.81794e-15,2.42631e-12 | yes | match | script verdict (values not both numeric) |
| Q6 | 0.0011614097 | 1.1614e-3 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 0.0072973524 | 7.2973e-3 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 0.0072973526 | 7.29735e-3 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q9 | 20971520 | 20971520 | yes | match | 8 significant digits (as printed, at least 3) |
| Q10 | 64 | 64 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 327680 | 327680 | yes | match | 6 significant digits (as printed, at least 3) |
| Q12 | 1.6666667 | 1.666 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 1.4142136e-06 | 1.4142e-6 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q14 | 1.6424814e-09 | 1.64e-9 | no | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 14.
