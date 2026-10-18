# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The maximal admissible additive noise is ε_max = 0.5.",
    "inputs": "g_min = 1",
    "formula": "ε_max = g_min / 2"
  },
  {
    "id": "Q2",
    "statement": "The critical lateral‑transfer amplitude computed from tree depths is α_crit = 0.7.",
    "inputs": "β = 1, D = 5, D' = 3, σ = 0.1",
    "formula": "α_crit = β * (D - D') / 2 - 3 * σ"
  },
  {
    "id": "Q3",
    "statement": "Using the generic gap g = 2, the critical lateral‑transfer amplitude is α_crit = 0.7.",
    "inputs": "g = 2, σ = 0.1",
    "formula": "α_crit = g / 2 - 3 * σ"
  },
  {
    "id": "Q4",
    "statement": "The spin‑glass field scaling gives h = 0.015625 ≈ 1.56×10⁻².",
    "inputs": "N = 4096",
    "formula": "h = 1 / sqrt(N)"
  },
  {
    "id": "Q5",
    "statement": "The empirical violation proportion is p_viol = 0.294.",
    "inputs": "violations = 147, total triples = 500",
    "formula": "p_viol = violations / total triples"
  },
  {
    "id": "Q6",
    "statement": "The lateral‑transfer rate threshold is λ_crit ≈ 2.94×10⁻¹.",
    "inputs": "p_viol = 0.294",
    "formula": "λ_crit ≈ p_viol"
  },
  {
    "id": "Q7",
    "statement": "The violation probability for α = 0.5 and gap g = 2 is P_violation = 0.",
    "inputs": "α = 0.5, g = 2",
    "formula": "P_violation = max(0, (α - g/2) / α)"
  },
  {
    "id": "Q8",
    "statement": "Seeing‑induced lens‑yield loss fraction is ℓ = 0.17 for a 0.1'' degradation.",
    "inputs": "Δθ = 0.1'' (seeing degradation)",
    "formula": "ℓ = 0.17 (given by empirical study)"
  },
  {
    "id": "Q9",
    "statement": "The lens count after degradation is L_0.9 = 0.83 L_0.8.",
    "inputs": "ℓ = 0.17",
    "formula": "L_0.9 = (1 - ℓ) * L_0.8"
  }
]

## Script
```python
import math

def fmt(val, fmt_type):
    if fmt_type == '1dp':
        return f"{val:.1f}"
    if fmt_type == '6dp':
        return f"{val:.6f}"
    if fmt_type == '3dp':
        return f"{val:.3f}"
    if fmt_type == '2dp':
        return f"{val:.2f}"
    if fmt_type == 'int':
        return f"{int(round(val))}"
    if fmt_type == 'sci3':
        return f"{val:.3e}"
    return str(val)

# Claim Q1
g_min = 1
epsilon_max = g_min / 2
exp_Q1 = "0.5"
comp_Q1 = fmt(epsilon_max, '1dp')
match_Q1 = "yes" if comp_Q1 == exp_Q1 else "no"
print(f"CLAIM Q1: computed={comp_Q1} expected={exp_Q1} match={match_Q1}")

# Claim Q2
beta, D, Dp, sigma = 1, 5, 3, 0.1
alpha_crit_Q2 = beta * (D - Dp) / 2 - 3 * sigma
exp_Q2 = "0.7"
comp_Q2 = fmt(alpha_crit_Q2, '1dp')
match_Q2 = "yes" if comp_Q2 == exp_Q2 else "no"
print(f"CLAIM Q2: computed={comp_Q2} expected={exp_Q2} match={match_Q2}")

# Claim Q3
g, sigma = 2, 0.1
alpha_crit_Q3 = g / 2 - 3 * sigma
exp_Q3 = "0.7"
comp_Q3 = fmt(alpha_crit_Q3, '1dp')
match_Q3 = "yes" if comp_Q3 == exp_Q3 else "no"
print(f"CLAIM Q3: computed={comp_Q3} expected={exp_Q3} match={match_Q3}")

# Claim Q4
N = 4096
h = 1 / math.sqrt(N)
exp_Q4 = "0.015625"
comp_Q4 = fmt(h, '6dp')
match_Q4 = "yes" if comp_Q4 == exp_Q4 else "no"
print(f"CLAIM Q4: computed={comp_Q4} expected={exp_Q4} match={match_Q4}")

# Claim Q5
violations, total = 147, 500
p_viol = violations / total
exp_Q5 = "0.294"
comp_Q5 = fmt(p_viol, '3dp')
match_Q5 = "yes" if comp_Q5 == exp_Q5 else "no"
print(f"CLAIM Q5: computed={comp_Q5} expected={exp_Q5} match={match_Q5}")

# Claim Q6
lambda_crit = p_viol
exp_Q6 = "2.94e-1"
comp_Q6 = fmt(lambda_crit, 'sci3')
match_Q6 = "yes" if comp_Q6 == exp_Q6 else "no"
print(f"CLAIM Q6: computed={comp_Q6} expected={exp_Q6} match={match_Q6}")

# Claim Q7
alpha, g = 0.5, 2
P_violation = max(0, (alpha - g/2) / alpha)
exp_Q7 = "0"
comp_Q7 = fmt(P_violation, 'int')
match_Q7 = "yes" if comp_Q7 == exp_Q7 else "no"
print(f"CLAIM Q7: computed={comp_Q7} expected={exp_Q7} match={match_Q7}")

# Claim Q8
ell = 0.17  # given directly
exp_Q8 = "0.17"
comp_Q8 = fmt(ell, '2dp')
match_Q8 = "yes" if comp_Q8 == exp_Q8 else "no"
print(f"CLAIM Q8: computed={comp_Q8} expected={exp_Q8} match={match_Q8}")

# Claim Q9
L_factor = 1 - ell
exp_Q9 = "0.83"
comp_Q9 = fmt(L_factor, '2dp')
match_Q9 = "yes" if comp_Q9 == exp_Q9 else "no"
print(f"CLAIM Q9: computed={comp_Q9} expected={exp_Q9} match={match_Q9}")

print(f"VERIFICATION SUMMARY: 9 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9].count('yes'))} match, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9].count('no'))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.5 expected=0.5 match=yes
CLAIM Q2: computed=0.7 expected=0.7 match=yes
CLAIM Q3: computed=0.7 expected=0.7 match=yes
CLAIM Q4: computed=0.015625 expected=0.015625 match=yes
CLAIM Q5: computed=0.294 expected=0.294 match=yes
CLAIM Q6: computed=2.940e-01 expected=2.94e-1 match=no
CLAIM Q7: computed=0 expected=0 match=yes
CLAIM Q8: computed=0.17 expected=0.17 match=yes
CLAIM Q9: computed=0.83 expected=0.83 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 87, in <module>
TypeError: 'int' object is not iterable

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.5 | 0.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.7 | 0.7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.7 | 0.7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.015625 | 0.015625 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | 0.294 | 0.294 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 2.940e-01 | 2.94e-1 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 0 | 0 | yes | match | stated value is zero |
| Q8 | 0.17 | 0.17 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 0.83 | 0.83 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 9.
