# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Explanation‑assisted image retrieval yields an 8.14 percentage‑point increase in win‑rate.",
    "inputs": "Baseline win‑rate = 61.15 %; Explanation win‑rate = 69.29 %",
    "formula": "Δ = 69.29 % - 61.15 % = 8.14 %"
  },
  {
    "id": "Q2",
    "statement": "Standard error of the mean performance in the feature‑engineering study is approximately 0.00588.",
    "inputs": "Standard deviation = 0.022; Sample size n = 14",
    "formula": "SE = SD / sqrt(n) = 0.022 / sqrt(14) ≈ 0.00588"
  },
  {
    "id": "Q3",
    "statement": "Margin of error for a 95 % confidence interval is approximately 0.0115.",
    "inputs": "Standard error SE ≈ 0.00588; z‑value for 95 % ≈ 1.96",
    "formula": "ME = z * SE = 1.96 * 0.00588 ≈ 0.0115"
  },
  {
    "id": "Q4",
    "statement": "Lower bound of the 95 % confidence interval for mean performance is 0.8095.",
    "inputs": "Mean performance = 0.821; Margin of error ME ≈ 0.0115",
    "formula": "Lower = mean - ME = 0.821 - 0.0115 = 0.8095"
  },
  {
    "id": "Q5",
    "statement": "Upper bound of the 95 % confidence interval for mean performance is 0.8325.",
    "inputs": "Mean performance = 0.821; Margin of error ME ≈ 0.0115",
    "formula": "Upper = mean + ME = 0.821 + 0.0115 = 0.8325"
  },
  {
    "id": "Q6",
    "statement": "Average win‑rate improvement across the available studies is 8.14 %.",
    "inputs": "Sum of ΔPerformance = 8.14 %; Number of studies with Δ = 1",
    "formula": "Average Δ = Sum / Count = 8.14 % / 1 = 8.14 %"
  },
  {
    "id": "Q7",
    "statement": "Personnel cost for the pilot experiment is approximately 21 000 USD.",
    "inputs": "Project manager salary = 120 000 USD/yr, FTE = 0.2; Analyst salary = 90 000 USD/yr, FTE = 0.2; Duration factor = 0.5 (six months)",
    "formula": "Cost = (120000*0.2 + 90000*0.2) * 0.5 = 21000 USD"
  },
  {
    "id": "Q8",
    "statement": "Total projected cost for the pilot experiment is approximately 30 000 USD.",
    "inputs": "Personnel cost = 21 000 USD; Software licences = 5 000 USD; Participant incentives = 4 000 USD",
    "formula": "Total = 21000 + 5000 + 4000 = 30000 USD"
  }
]

## Script
```python
import math

def fmt(x, sig=8):
    # format with at least sig significant digits, removing trailing zeros
    s = f"{x:.{sig}g}"
    return s

# Q1
baseline = 61.15
explanation = 69.29
delta = explanation - baseline
expected_q1 = "8.14"
match_q1 = fmt(delta, 4) == expected_q1
print(f"CLAIM Q1: computed={fmt(delta,8)} expected={expected_q1} match={'yes' if match_q1 else 'no'}")

# Q2
sd = 0.022
n = 14
se = sd / math.sqrt(n)
expected_q2 = "0.00588"
# round to 5 decimal places for comparison
match_q2 = f"{se:.5f}" == expected_q2
print(f"CLAIM Q2: computed={fmt(se,8)} expected={expected_q2} match={'yes' if match_q2 else 'no'}")

# Q3
z = 1.96
me = z * se
expected_q3 = "0.0115"
match_q3 = f"{me:.4f}" == expected_q3
print(f"CLAIM Q3: computed={fmt(me,8)} expected={expected_q3} match={'yes' if match_q3 else 'no'}")

# Q4
mean_perf = 0.821
lower = mean_perf - me
expected_q4 = "0.8095"
match_q4 = f"{lower:.4f}" == expected_q4
print(f"CLAIM Q4: computed={fmt(lower,8)} expected={expected_q4} match={'yes' if match_q4 else 'no'}")

# Q5
upper = mean_perf + me
expected_q5 = "0.8325"
match_q5 = f"{upper:.4f}" == expected_q5
print(f"CLAIM Q5: computed={fmt(upper,8)} expected={expected_q5} match={'yes' if match_q5 else 'no'}")

# Q6
sum_delta = delta  # only one study
count = 1
avg_delta = sum_delta / count
expected_q6 = "8.14"
match_q6 = fmt(avg_delta,4) == expected_q6
print(f"CLAIM Q6: computed={fmt(avg_delta,8)} expected={expected_q6} match={'yes' if match_q6 else 'no'}")

# Q7
pm_salary = 120000
pm_fte = 0.2
analyst_salary = 90000
analyst_fte = 0.2
duration_factor = 0.5
cost = (pm_salary * pm_fte + analyst_salary * analyst_fte) * duration_factor
expected_q7 = "21000"
match_q7 = f"{cost:.0f}" == expected_q7
print(f"CLAIM Q7: computed={fmt(cost,8)} expected={expected_q7} match={'yes' if match_q7 else 'no'}")

# Q8
software = 5000
incentives = 4000
total = cost + software + incentives
expected_q8 = "30000"
match_q8 = f"{total:.0f}" == expected_q8
print(f"CLAIM Q8: computed={fmt(total,8)} expected={expected_q8} match={'yes' if match_q8 else 'no'}")

print(f"VERIFICATION SUMMARY: 8 claims, {sum([match_q1, match_q2, match_q3, match_q4, match_q5, match_q6, match_q7, match_q8])} match, {8 - sum([match_q1, match_q2, match_q3, match_q4, match_q5, match_q6, match_q7, match_q8])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=8.14 expected=8.14 match=yes
CLAIM Q2: computed=0.0058797473 expected=0.00588 match=yes
CLAIM Q3: computed=0.011524305 expected=0.0115 match=yes
CLAIM Q4: computed=0.8094757 expected=0.8095 match=yes
CLAIM Q5: computed=0.8325243 expected=0.8325 match=yes
CLAIM Q6: computed=8.14 expected=8.14 match=yes
CLAIM Q7: computed=21000 expected=21000 match=yes
CLAIM Q8: computed=30000 expected=30000 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 8.14 | 8.14 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 0.0058797473 | 0.00588 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 0.011524305 | 0.0115 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.8094757 | 0.8095 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 0.8325243 | 0.8325 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 8.14 | 8.14 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 21000 | 21000 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 30000 | 30000 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 8.
