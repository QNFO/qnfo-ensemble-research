# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Model fidelity for the accurate‑entropy agent is Φ₍acc₎ = 0.060.",
    "inputs": "β = 0.075, M = 0.8",
    "formula": "Φ₍acc₎ = β \\times M"
  },
  {
    "id": "Q2",
    "statement": "Expected fitness for the accurate‑entropy agent is F₍acc₎ = 0.015.",
    "inputs": "Φ₍acc₎ = 0.060, S = 0.25",
    "formula": "F₍acc₎ = Φ₍acc₎ \\times S"
  },
  {
    "id": "Q3",
    "statement": "Model fidelity for the entropy‑masking agent is Φ₍mask₎ = 0.3375.",
    "inputs": "α = 0.925, γ = 0.7, H_t = 1, β = 0.075, M = 0.8",
    "formula": "Φ₍mask₎ = α \\times (1-γ) \\times H_t + β \\times M"
  },
  {
    "id": "Q4",
    "statement": "Expected fitness for the entropy‑masking agent is F₍mask₎ = 0.084375.",
    "inputs": "Φ₍mask₎ = 0.3375, S = 0.25",
    "formula": "F₍mask₎ = Φ₍mask₎ \\times S"
  },
  {
    "id": "Q5",
    "statement": "Relative fitness increase of the entropy‑masking agent over the accurate‑entropy baseline is 462.5 %.",
    "inputs": "F₍mask₎ = 0.084375, F₍acc₎ = 0.015",
    "formula": "(F₍mask₎ - F₍acc₎) / F₍acc₎ \\times 100"
  },
  {
    "id": "Q6",
    "statement": "Absolute fitness gain of the entropy‑masking agent is ΔF = 0.069375.",
    "inputs": "F₍mask₎ = 0.084375, F₍acc₎ = 0.015",
    "formula": "ΔF = F₍mask₎ - F₍acc₎"
  },
  {
    "id": "Q7",
    "statement": "Optimal hazard‑compression factor is α* = 0.5 for p = 0.2, c = 1, λ = 0.1.",
    "inputs": "p = 0.2, c = 1, λ = 0.1",
    "formula": "α* = \\max\\bigl(0,\\,1-\\lambda c / p\\bigr) = 1 - 0.1\\times1/0.2"
  },
  {
    "id": "Q8",
    "statement": "Perceived hazard under the optimal compression is \\hat p = 0.1 (50 % under‑estimation).",
    "inputs": "α* = 0.5, p = 0.2",
    "formula": "\\hat p = α* \\times p"
  },
  {
    "id": "Q9",
    "statement": "Effort chosen by the distorted agent is E* = 0.9.",
    "inputs": "α* = 0.5, p = 0.2, c = 1",
    "formula": "E* = (1 - α* p) / c"
  },
  {
    "id": "Q10",
    "statement": "Effort chosen by a veridical agent is E_ver = 0.8.",
    "inputs": "p = 0.2, c = 1",
    "formula": "E_{ver} = (1 - p) / c"
  },
  {
    "id": "Q11",
    "statement": "Effort inflation relative to the veridical agent is 12.5 %.",
    "inputs": "E* = 0.9, E_ver = 0.8",
    "formula": "(E* - E_{ver}) / E_{ver} \\times 100"
  },
  {
    "id": "Q12",
    "statement": "Fitness of the distorted agent is F_dist = 0.305.",
    "inputs": "E* = 0.9, p = 0.2, c = 1, λ = 0.1, α* = 0.5",
    "formula": "F_{dist} = E*(1-p) - \\frac{c\\,E^{2}}{2} - λ\\,α*\\,p"
  },
  {
    "id": "Q13",
    "statement": "Fitness of the veridical agent is F_ver = 0.30.",
    "inputs": "E_ver = 0.8, p = 0.2, c = 1, λ = 0.1, α = 1",
    "formula": "F_{ver} = E_{ver}(1-p) - \\frac{c\\,E_{ver}^{2}}{2} - λ\\,p"
  },
  {
    "id": "Q14",
    "statement": "Relative fitness gain of the distorted agent over the veridical agent is 1.67 %.",
    "inputs": "ΔF = 0.005, F_{ver} = 0.30",
    "formula": "ΔF / F_{ver} \\times 100"
  },
  {
    "id": "Q15",
    "statement": "For hazard probability p = 0.05 the optimal compression collapses to α* = 0.",
    "inputs": "p = 0.05, c = 1, λ = 0.1",
    "formula": "α* = \\max\\bigl(0,\\,1-\\lambda c / p\\bigr) = \\max(0, 1-0.1/0.05) = 0"
  },
  {
    "id": "Q16",
    "statement": "For p = 0.05 the optimal agent exerts effort E* = 1.00 and attains fitness F = 0.475.",
    "inputs": "p = 0.05, α* = 0, c = 1, λ = 0.1",
    "formula": "E* = (1-α* p)/c;\\; F = E*(1-p) - \\frac{c\\,E^{2}}{2} - λ\\,α* p"
  }
]

## Script
```python
import math

def fmt(val, sig=8):
    # format with given significant digits, removing trailing zeros
    s = f"{val:.{sig}g}"
    return s

claims = [
    # Q1
    ("Q1", 0.075 * 0.8, "0.060"),
    # Q2
    ("Q2", 0.06 * 0.25, "0.015"),
    # Q3
    ("Q3", 0.925 * (1-0.7) * 1 + 0.075 * 0.8, "0.3375"),
    # Q4
    ("Q4", 0.3375 * 0.25, "0.084375"),
    # Q5
    ("Q5", ((0.084375 - 0.015) / 0.015) * 100, "462.5"),
    # Q6
    ("Q6", 0.084375 - 0.015, "0.069375"),
    # Q7
    ("Q7", max(0, 1 - 0.1 * 1 / 0.2), "0.5"),
    # Q8
    ("Q8", 0.5 * 0.2, "0.1"),
    # Q9
    ("Q9", (1 - 0.5 * 0.2) / 1, "0.9"),
    # Q10
    ("Q10", (1 - 0.2) / 1, "0.8"),
    # Q11
    ("Q11", ((0.9 - 0.8) / 0.8) * 100, "12.5"),
    # Q12
    ("Q12", 0.9 * (1-0.2) - 1 * 0.9**2 / 2 - 0.1 * 0.5 * 0.2, "0.305"),
    # Q13
    ("Q13", 0.8 * (1-0.2) - 1 * 0.8**2 / 2 - 0.1 * 0.2, "0.30"),
    # Q14
    ("Q14", (0.005 / 0.30) * 100, "1.67"),
    # Q15
    ("Q15", max(0, 1 - 0.1 * 1 / 0.05), "0"),
    # Q16
    ("Q16", (1 - 0 * 0.05) / 1, "1.00"),  # effort E*
]

# compute fitness for Q16 separately
def fitness_q16():
    p = 0.05
    c = 1
    lam = 0.1
    alpha = 0
    E = (1 - alpha * p) / c
    F = E * (1 - p) - c * E**2 / 2 - lam * alpha * p
    return E, F

E16, F16 = fitness_q16()
claims[15] = ("Q16", F16, "0.475")  # expected from paper

for cid, computed, expected in claims:
    # determine match
    # compare numeric values within tolerance appropriate to expected digits
    try:
        exp_val = float(expected)
        # tolerance: half of last displayed unit
        # determine number of decimal places in expected
        if "." in expected:
            dec = len(expected.split(".")[1])
            tol = 0.5 * 10**(-dec)
        else:
            # integer expected
            tol = 0.5
        match = "yes" if abs(computed - exp_val) <= tol else "no"
    except:
        match = "no"
    print(f"CLAIM {cid}: computed={fmt(computed)} expected={expected} match={match}")
print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if (abs(c-float(e))<= (0.5*10**(-len(e.split('.')[1]) if '.' in e else 0))) )} match, {len(claims)-sum(1 for _,c,e in claims if (abs(c-float(e))<= (0.5*10**(-len(e.split('.')[1]) if '.' in e else 0))) )} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.06 expected=0.060 match=yes
CLAIM Q2: computed=0.015 expected=0.015 match=yes
CLAIM Q3: computed=0.3375 expected=0.3375 match=yes
CLAIM Q4: computed=0.084375 expected=0.084375 match=yes
CLAIM Q5: computed=462.5 expected=462.5 match=yes
CLAIM Q6: computed=0.069375 expected=0.069375 match=yes
CLAIM Q7: computed=0.5 expected=0.5 match=yes
CLAIM Q8: computed=0.1 expected=0.1 match=yes
CLAIM Q9: computed=0.9 expected=0.9 match=yes
CLAIM Q10: computed=0.8 expected=0.8 match=yes
CLAIM Q11: computed=12.5 expected=12.5 match=yes
CLAIM Q12: computed=0.305 expected=0.305 match=yes
CLAIM Q13: computed=0.3 expected=0.30 match=yes
CLAIM Q14: computed=1.6666667 expected=1.67 match=yes
CLAIM Q15: computed=0 expected=0 match=yes
CLAIM Q16: computed=0.45 expected=0.475 match=no
VERIFICATION SUMMARY: 16 claims, 15 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.06 | 0.060 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.015 | 0.015 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.3375 | 0.3375 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 0.084375 | 0.084375 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | 462.5 | 462.5 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 0.069375 | 0.069375 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 0.5 | 0.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 0.1 | 0.1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 0.9 | 0.9 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 0.8 | 0.8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 12.5 | 12.5 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 0.305 | 0.305 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 0.3 | 0.30 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 1.6666667 | 1.67 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 0 | 0 | yes | match | stated value is zero |
| Q16 | 0.45 | 0.475 | no | MISMATCH | 3 significant digits (as the paper states, at least 2) |

Mismatches: 1 of 16.


## Auto-corrections

The worker corrected these independently-verified values in place of the paper's stated values (deterministic, no model edit):

| claim | stated | corrected |
|---|---|---|
| Q16 | 0.475 | 0.45 |
