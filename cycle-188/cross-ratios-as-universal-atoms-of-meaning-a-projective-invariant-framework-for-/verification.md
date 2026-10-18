# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Fine‑structure constant expressed as a cross‑ratio: α = 0.007297357 (≈ 1/137.036).",
    "inputs": "r_e = 2.81794×10^{-15} m, \\bar{\\lambda}_C = 3.86159×10^{-13} m",
    "formula": "α = r_e / \\bar{\\lambda}_C"
  },
  {
    "id": "Q2",
    "statement": "Simple four‑point cross‑ratio for points A=1, B=2, C=3, D=4 equals 4/3.",
    "inputs": "A = 1, B = 2, C = 3, D = 4",
    "formula": "CR = ((A - C) * (B - D)) / ((A - D) * (B - C))"
  },
  {
    "id": "Q3",
    "statement": "Sum of reported low‑FPR improvements for PL‑MIA: 22.94 % + 27.29 % + 27.65 % = 77.88 %.",
    "inputs": "improvement_1 = 22.94, improvement_2 = 27.29, improvement_3 = 27.65",
    "formula": "sum = improvement_1 + improvement_2 + improvement_3"
  },
  {
    "id": "Q4",
    "statement": "Average low‑FPR improvement of PL‑MIA: 77.88 % / 3 = 25.96 %.",
    "inputs": "sum = 77.88, divisor = 3",
    "formula": "average = sum / divisor"
  },
  {
    "id": "Q5",
    "statement": "Projected true‑positive rate for CIFAR‑10 after PL‑MIA improvement: 50 % × (1 + 0.2294) = 61.47 %.",
    "inputs": "baseline_TPR = 50, relative_improvement = 0.2294",
    "formula": "TPR_proj = baseline_TPR * (1 + relative_improvement)"
  },
  {
    "id": "Q6",
    "statement": "Absolute gain in true‑positive rate: 61.47 % − 50 % = 11.47 %.",
    "inputs": "TPR_proj = 61.47, baseline_TPR = 50",
    "formula": "gain = TPR_proj - baseline_TPR"
  }
]

## Script
```python
# Verification script for quantitative claims in the paper

from fractions import Fraction

def round_sig(x, sig):
    """Round x to sig significant digits."""
    if x == 0:
        return 0.0
    return float(format(x, f".{sig}g"))

# Claim Q1
r_e = 2.81794e-15
lam_c = 3.86159e-13
alpha = r_e / lam_c
alpha_rounded = round_sig(alpha, 7)          # 7 significant digits (0.007297357)
expected_q1 = "0.007297357"
match_q1 = "yes" if abs(alpha_rounded - float(expected_q1)) < 1e-12 else "no"
print(f"CLAIM Q1: computed={alpha:.15g} expected={expected_q1} match={match_q1}")

# Claim Q2
A, B, C, D = 1, 2, 3, 4
cr = ((A - C) * (B - D)) / ((A - D) * (B - C))
expected_q2 = "4/3"
match_q2 = "yes" if Fraction(cr).limit_denominator() == Fraction(4, 3) else "no"
print(f"CLAIM Q2: computed={cr:.15g} expected={expected_q2} match={match_q2}")

# Claim Q3
imp1, imp2, imp3 = 22.94, 27.29, 27.65
sum_imp = imp1 + imp2 + imp3
sum_imp_rounded = round_sig(sum_imp, 4)      # 4 significant digits (77.88)
expected_q3 = "77.88"
match_q3 = "yes" if abs(sum_imp_rounded - float(expected_q3)) < 1e-9 else "no"
print(f"CLAIM Q3: computed={sum_imp:.15g} expected={expected_q3} match={match_q3}")

# Claim Q4
average_imp = sum_imp / 3
average_imp_rounded = round_sig(average_imp, 4)  # 4 significant digits (25.96)
expected_q4 = "25.96"
match_q4 = "yes" if abs(average_imp_rounded - float(expected_q4)) < 1e-9 else "no"
print(f"CLAIM Q4: computed={average_imp:.15g} expected={expected_q4} match={match_q4}")

# Claim Q5
baseline_TPR = 50.0
rel_imp = 0.2294
TPR_proj = baseline_TPR * (1 + rel_imp)
TPR_proj_rounded = round_sig(TPR_proj, 4)    # 4 significant digits (61.47)
expected_q5 = "61.47"
match_q5 = "yes" if abs(TPR_proj_rounded - float(expected_q5)) < 1e-9 else "no"
print(f"CLAIM Q5: computed={TPR_proj:.15g} expected={expected_q5} match={match_q5}")

# Claim Q6
gain = TPR_proj - baseline_TPR
gain_rounded = round_sig(gain, 4)            # 4 significant digits (11.47)
expected_q6 = "11.47"
match_q6 = "yes" if abs(gain_rounded - float(expected_q6)) < 1e-9 else "no"
print(f"CLAIM Q6: computed={gain:.15g} expected={expected_q6} match={match_q6}")

# Summary
matches = [match_q1, match_q2, match_q3, match_q4, match_q5, match_q6]
num_claims = len(matches)
num_match = matches.count("yes")
num_mismatch = num_claims - num_match
print(f"VERIFICATION SUMMARY: {num_claims} claims, {num_match} match, {num_mismatch} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.00729735678826597 expected=0.007297357 match=yes
CLAIM Q2: computed=1.33333333333333 expected=4/3 match=yes
CLAIM Q3: computed=77.88 expected=77.88 match=yes
CLAIM Q4: computed=25.96 expected=25.96 match=yes
CLAIM Q5: computed=61.47 expected=61.47 match=yes
CLAIM Q6: computed=11.47 expected=11.47 match=yes
VERIFICATION SUMMARY: 6 claims, 6 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.00729735678826597 | 0.007297357 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q2 | 1.33333333333333 | 4/3 | yes | match | script verdict (values not both numeric) |
| Q3 | 77.88 | 77.88 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 25.96 | 25.96 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 61.47 | 61.47 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 11.47 | 11.47 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 6.
