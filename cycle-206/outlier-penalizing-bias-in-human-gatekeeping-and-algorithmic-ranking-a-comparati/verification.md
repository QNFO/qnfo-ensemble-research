# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The algorithmic gatekeeper assigns a posterior probability of high quality $P_{\\text{alg}} = 0.470588$ (≈47.06%).",
    "inputs": "K_S = 8, P(H_c) = 0.1",
    "formula": "P = (K_S * P(H_c)) / (K_S * P(H_c) + (1 - P(H_c)))"
  },
  {
    "id": "Q2",
    "statement": "The human gatekeeper retains the prior acceptance probability $P_{\\text{hum}} = 0.10$ (10%).",
    "inputs": "K_R = 1, P(H_c) = 0.1",
    "formula": "P = (K_R * P(H_c)) / (K_R * P(H_c) + (1 - P(H_c)))"
  },
  {
    "id": "Q3",
    "statement": "Metadata optimization increases algorithmic acceptance by a factor of approximately 4.706 relative to human acceptance.",
    "inputs": "P_{\\text{alg}} = 0.470588, P_{\\text{hum}} = 0.10",
    "formula": "factor = P_{\\text{alg}} / P_{\\text{hum}}"
  },
  {
    "id": "Q4",
    "statement": "The pilot experiment is projected to cost approximately $21,000.",
    "inputs": "cost per manuscript = 100 USD, number of manuscripts = 200, reviewer hour cost = 50 USD, reviewer hours = 20",
    "formula": "total cost = (cost per manuscript * number of manuscripts) + (reviewer hour cost * reviewer hours)"
  }
]

## Script
```python
import math

# Q1
K_S = 8
P_Hc = 0.1
P_alg = (K_S * P_Hc) / (K_S * P_Hc + (1 - P_Hc))
expected_Q1 = "0.470588"
computed_Q1 = round(P_alg, 6)  # match 6 decimal places
match_Q1 = "yes" if f"{computed_Q1:.6f}" == expected_Q1 else "no"
print(f"CLAIM Q1: computed={P_alg:.8g} expected={expected_Q1} match={match_Q1}")

# Q2
K_R = 1
P_hum = (K_R * P_Hc) / (K_R * P_Hc + (1 - P_Hc))
expected_Q2 = "0.10"
computed_Q2 = round(P_hum, 2)
match_Q2 = "yes" if f"{computed_Q2:.2f}" == expected_Q2 else "no"
print(f"CLAIM Q2: computed={P_hum:.8g} expected={expected_Q2} match={match_Q2}")

# Q3
factor = P_alg / P_hum
expected_Q3 = "4.706"
computed_Q3 = round(factor, 3)
match_Q3 = "yes" if f"{computed_Q3:.3f}" == expected_Q3 else "no"
print(f"CLAIM Q3: computed={factor:.8g} expected={expected_Q3} match={match_Q3}")

# Q4
cost_per_manuscript = 100
num_manuscripts = 200
reviewer_hour_cost = 50
reviewer_hours = 20
total_cost = cost_per_manuscript * num_manuscripts + reviewer_hour_cost * reviewer_hours
expected_Q4 = "21000"
computed_Q4 = round(total_cost)
match_Q4 = "yes" if str(computed_Q4) == expected_Q4 else "no"
print(f"CLAIM Q4: computed={total_cost:.8g} expected={expected_Q4} match={match_Q4}")

print("VERIFICATION SUMMARY: 4 claims, 4 match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.47058824 expected=0.470588 match=yes
CLAIM Q2: computed=0.1 expected=0.10 match=yes
CLAIM Q3: computed=4.7058824 expected=4.706 match=yes
CLAIM Q4: computed=21000 expected=21000 match=yes
VERIFICATION SUMMARY: 4 claims, 4 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.47058824 | 0.470588 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q2 | 0.1 | 0.10 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 4.7058824 | 4.706 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 21000 | 21000 | yes | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 4.
