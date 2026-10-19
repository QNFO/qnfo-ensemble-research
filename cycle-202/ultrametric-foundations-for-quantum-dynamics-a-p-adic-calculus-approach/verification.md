# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The standard deviation is σ = 0.349 (to three decimal places).",
    "inputs": "σ² = 0.122",
    "formula": "σ = sqrt(σ²)"
  },
  {
    "id": "Q2",
    "statement": "The coefficient of variation is CV ≈ 0.503.",
    "inputs": "σ = 0.349, μ = 0.693",
    "formula": "CV = σ / μ"
  },
  {
    "id": "Q3",
    "statement": "The variance‑to‑mean ratio is R ≈ 0.176.",
    "inputs": "σ² = 0.122, μ = 0.693",
    "formula": "R = σ² / μ"
  },
  {
    "id": "Q4",
    "statement": "The Euclidean root‑mean‑square displacement after N = 1000 steps is √1000 ≈ 31.62.",
    "inputs": "N = 1000",
    "formula": "sqrt(N)"
  },
  {
    "id": "Q5",
    "statement": "The Euclidean RMS displacement is a factor ≈ 45.6 larger than the p‑adic mean displacement μ = 0.693.",
    "inputs": "sqrt(N) ≈ 31.62, μ = 0.693",
    "formula": "factor = sqrt(N) / μ"
  },
  {
    "id": "Q6",
    "statement": "The lower bound of the ±10 % acceptance window for R is 0.158 (rounded).",
    "inputs": "R = 0.176, lower‑factor = 0.9",
    "formula": "lower = 0.9 * R"
  },
  {
    "id": "Q7",
    "statement": "The upper bound of the ±10 % acceptance window for R is 0.194 (rounded).",
    "inputs": "R = 0.176, upper‑factor = 1.1",
    "formula": "upper = 1.1 * R"
  },
  {
    "id": "Q8",
    "statement": "The falsification window is R ∈ [0.158, 0.194].",
    "inputs": "lower = 0.158, upper = 0.194",
    "formula": "lower ≤ R ≤ upper"
  },
  {
    "id": "Q9",
    "statement": "The consistency check CV²·μ ≈ 0.176 holds (CV²·μ = 0.1758).",
    "inputs": "CV ≈ 0.5036, μ = 0.693",
    "formula": "CV^2 * μ"
  }
]

## Script
```python
import math

def round_to_str(value, fmt):
    """Round value to the number of decimal places in fmt string and return as string."""
    if '.' in fmt:
        decimals = len(fmt.split('.')[1])
        return f"{round(value, decimals):.{decimals}f}"
    else:
        return str(int(round(value)))

# Inputs
sigma2 = 0.122
mu = 0.693
N = 1000

# Expected values as strings from the paper
expected = {
    "Q1": "0.349",
    "Q2": "0.503",
    "Q3": "0.176",
    "Q4": "31.62",
    "Q5": "45.6",
    "Q6": "0.158",
    "Q7": "0.194",
    "Q8": "True",   # Boolean window inclusion
    "Q9": "0.176"
}

# Computations
sigma = math.sqrt(sigma2)                     # Q1
cv = sigma / mu                               # Q2
R = sigma2 / mu                               # Q3
sqrtN = math.sqrt(N)                         # Q4
factor = sqrtN / mu                           # Q5
lower = 0.9 * R                               # Q6
upper = 1.1 * R                               # Q7
window_ok = lower <= R <= upper               # Q8
cv2_mu = (cv ** 2) * mu                       # Q9

# Prepare computed strings
computed = {
    "Q1": round_to_str(sigma, expected["Q1"]),
    "Q2": round_to_str(cv, expected["Q2"]),
    "Q3": round_to_str(R, expected["Q3"]),
    "Q4": round_to_str(sqrtN, expected["Q4"]),
    "Q5": round_to_str(factor, expected["Q5"]),
    "Q6": round_to_str(lower, expected["Q6"]),
    "Q7": round_to_str(upper, expected["Q7"]),
    "Q8": str(window_ok),
    "Q9": round_to_str(cv2_mu, expected["Q9"])
}

# Print results
for qid in ["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9"]:
    comp = computed[qid]
    exp = expected[qid]
    match = "yes" if comp == exp else "no"
    print(f"CLAIM {qid}: computed={comp} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if computed[q]==expected[q])} match, {sum(1 for q in expected if computed[q]!=expected[q])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.349 expected=0.349 match=yes
CLAIM Q2: computed=0.504 expected=0.503 match=no
CLAIM Q3: computed=0.176 expected=0.176 match=yes
CLAIM Q4: computed=31.62 expected=31.62 match=yes
CLAIM Q5: computed=45.6 expected=45.6 match=yes
CLAIM Q6: computed=0.158 expected=0.158 match=yes
CLAIM Q7: computed=0.194 expected=0.194 match=yes
CLAIM Q8: computed=True expected=True match=yes
CLAIM Q9: computed=0.176 expected=0.176 match=yes
VERIFICATION SUMMARY: 9 claims, 8 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.349 | 0.349 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 0.504 | 0.503 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 0.176 | 0.176 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 31.62 | 31.62 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 45.6 | 45.6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 0.158 | 0.158 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 0.194 | 0.194 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | True | True | yes | match | script verdict (values not both numeric) |
| Q9 | 0.176 | 0.176 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 9.
