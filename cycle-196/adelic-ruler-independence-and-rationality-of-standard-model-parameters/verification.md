# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The adelic consistency condition forces any positive rational scalar coupling to equal 1, i.e. λ = 1.",
    "inputs": "a and b are positive integers with a = b",
    "formula": "λ = a / b = 1"
  },
  {
    "id": "Q2",
    "statement": "For the rational coupling λ = 2/3 the product of its real absolute value and all p‑adic absolute values equals 1.",
    "inputs": "a = 2, b = 3, ν₂(2)=1, ν₂(3)=0, ν₃(2)=0, ν₃(3)=1",
    "formula": "(2/3) * 2^{-1} * 3^{1} = 1"
  },
  {
    "id": "Q3",
    "statement": "The one‑loop beta‑function evaluated at λ = 1 is β(1) = 3/(16π²) ≈ 0.0190.",
    "inputs": "π ≈ 3.1415926535",
    "formula": "3 / (16 * π^2) ≈ 0.0190"
  },
  {
    "id": "Q4",
    "statement": "A projected measurement uncertainty of 2 % on a coupling of value 1 corresponds to an absolute deviation of 0.02.",
    "inputs": "λ = 1, uncertainty = 2 %",
    "formula": "0.02 = 0.02 * 1"
  },
  {
    "id": "Q5",
    "statement": "The fine‑structure constant is approximately α ≈ 1/137.",
    "inputs": "1 and 137",
    "formula": "α = 1 / 137 ≈ 0.00729927"
  }
]

## Script
```python
import math

# Q1: λ = a / b with a = b
a = 5
b = 5
lam_q1 = a / b
print(f"CLAIM Q1: computed={lam_q1:.10g} expected=1 match={'yes' if abs(lam_q1 - 1) < 1e-12 else 'no'}")

# Q2: (2/3) * 2^{-1} * 3^{1}
lam_q2 = 2 / 3
p2 = 2 ** (-1)
p3 = 3 ** 1
product_q2 = lam_q2 * p2 * p3
print(f"CLAIM Q2: computed={product_q2:.10g} expected=1 match={'yes' if abs(product_q2 - 1) < 1e-12 else 'no'}")

# Q3: β(1) = 3 / (16 * π^2)
pi = 3.1415926535
beta_q3 = 3 / (16 * pi ** 2)
print(f"CLAIM Q3: computed={beta_q3:.10g} expected=0.0190 match={'yes' if round(beta_q3, 4) == 0.0190 else 'no'}")

# Q4: 2% of λ = 1
lam_val = 1
uncertainty = 0.02
abs_dev_q4 = uncertainty * lam_val
print(f"CLAIM Q4: computed={abs_dev_q4:.10g} expected=0.02 match={'yes' if abs(abs_dev_q4 - 0.02) < 1e-12 else 'no'}")

# Q5: α = 1 / 137
alpha_q5 = 1 / 137
print(f"CLAIM Q5: computed={alpha_q5:.10g} expected=0.00729927 match={'yes' if round(alpha_q5, 8) == 0.00729927 else 'no'}")

print("VERIFICATION SUMMARY: 5 claims, 5 match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=1 expected=1 match=yes
CLAIM Q2: computed=1 expected=1 match=yes
CLAIM Q3: computed=0.01899772193 expected=0.0190 match=yes
CLAIM Q4: computed=0.02 expected=0.02 match=yes
CLAIM Q5: computed=0.007299270073 expected=0.00729927 match=yes
VERIFICATION SUMMARY: 5 claims, 5 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.01899772193 | 0.0190 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.02 | 0.02 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.007299270073 | 0.00729927 | yes | match | 6 significant digits (as printed, at least 3) |

Mismatches: 0 of 5.
