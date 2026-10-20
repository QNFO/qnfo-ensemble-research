# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Combined adaptive allocation and spatial modeling yields a total simulation‑budget reduction factor of 50.",
    "inputs": "factor1 = 10, factor2 = 5",
    "formula": "S = factor1 * factor2"
  },
  {
    "id": "Q2",
    "statement": "The expected empirical predictive risk estimate equals approximately 1.58 (absolute value).",
    "inputs": "sigma = 0.05",
    "formula": "Rhat = (1/2) * log(2 * pi * sigma^2) + 1/2; absolute value taken"
  },
  {
    "id": "Q3",
    "statement": "The negative log marginal likelihood equals approximately -2.058.",
    "inputs": "sigma2 = 0.0025, tau2 = 0.01, n = 100",
    "formula": "Z = 1 / sqrt(2 * pi * (sigma2 + tau2 / n)); negLogZ = -log(Z)"
  },
  {
    "id": "Q4",
    "statement": "The Epistemic‑Risk Score (ERS) for the Gaussian predictive model equals approximately -3.64.",
    "inputs": "negLogZ = -2.058, Rhat = -1.58",
    "formula": "ERS = negLogZ + Rhat"
  },
  {
    "id": "Q5",
    "statement": "Under linear interpolation, the Range Value‑at‑Risk (RVaR) between 0.95 and 0.99 equals 0.15.",
    "inputs": "VaR_0.95 = 0.10, VaR_0.99 = 0.20, alpha = 0.95, beta = 0.99",
    "formula": "RVaR = (1/(beta - alpha)) * ((beta - alpha)/2) * (VaR_0.95 + VaR_0.99) = (VaR_0.95 + VaR_0.99)/2"
  },
  {
    "id": "Q6",
    "statement": "The reduced simulation budget is 20 000 CPU‑hours.",
    "inputs": "baselineCPU = 1_000_000, reductionFactor = 50",
    "formula": "reducedCPU = baselineCPU / reductionFactor"
  },
  {
    "id": "Q7",
    "statement": "The projected compute cost after reduction is $400.",
    "inputs": "reducedCPU = 20_000, costPerHour = 0.02",
    "formula": "cost = reducedCPU * costPerHour"
  },
  {
    "id": "Q8",
    "statement": "The projected cost saving is $19 600.",
    "inputs": "originalCost = 1_000_000 * 0.02 = 20_000, reducedCost = 400",
    "formula": "saving = originalCost - reducedCost"
  }
]

## Script
```python
import math

matches = []

# Q1
factor1 = 10
factor2 = 5
S = factor1 * factor2
expected_Q1 = 50
match = S == expected_Q1
matches.append(match)
print(f"CLAIM Q1: computed={S} expected={expected_Q1} match={'yes' if match else 'no'}")

# Q2
sigma = 0.05
Rhat = 0.5 * math.log(2 * math.pi * sigma**2) + 0.5
abs_Rhat = abs(Rhat)
computed_Q2 = round(abs_Rhat, 2)
expected_Q2 = 1.58
match = abs(computed_Q2 - expected_Q2) < 1e-9
matches.append(match)
print(f"CLAIM Q2: computed={computed_Q2:.2f} expected={expected_Q2:.2f} match={'yes' if match else 'no'}")

# Q3
sigma2 = 0.0025
tau2 = 0.01
n = 100
Z = 1 / math.sqrt(2 * math.pi * (sigma2 + tau2 / n))
negLogZ = -math.log(Z)
computed_Q3 = round(negLogZ, 3)
expected_Q3 = -2.058
match = abs(computed_Q3 - expected_Q3) < 1e-9
matches.append(match)
print(f"CLAIM Q3: computed={computed_Q3:.3f} expected={expected_Q3:.3f} match={'yes' if match else 'no'}")

# Q4
ERS = negLogZ + Rhat
computed_Q4 = round(ERS, 2)
expected_Q4 = -3.64
match = abs(computed_Q4 - expected_Q4) < 1e-9
matches.append(match)
print(f"CLAIM Q4: computed={computed_Q4:.2f} expected={expected_Q4:.2f} match={'yes' if match else 'no'}")

# Q5
VaR_095 = 0.10
VaR_099 = 0.20
RVaR = (VaR_095 + VaR_099) / 2
computed_Q5 = round(RVaR, 2)
expected_Q5 = 0.15
match = abs(computed_Q5 - expected_Q5) < 1e-9
matches.append(match)
print(f"CLAIM Q5: computed={computed_Q5:.2f} expected={expected_Q5:.2f} match={'yes' if match else 'no'}")

# Q6
baselineCPU = 1_000_000
reductionFactor = 50
reducedCPU = baselineCPU // reductionFactor
computed_Q6 = reducedCPU
expected_Q6 = 20000
match = computed_Q6 == expected_Q6
matches.append(match)
print(f"CLAIM Q6: computed={computed_Q6} expected={expected_Q6} match={'yes' if match else 'no'}")

# Q7
costPerHour = 0.02
cost = reducedCPU * costPerHour
computed_Q7 = round(cost, 2)
expected_Q7 = 400
match = int(computed_Q7) == expected_Q7
matches.append(match)
print(f"CLAIM Q7: computed={int(computed_Q7)} expected={expected_Q7} match={'yes' if match else 'no'}")

# Q8
originalCost = baselineCPU * costPerHour
reducedCost = cost
saving = originalCost - reducedCost
computed_Q8 = round(saving, 0)
expected_Q8 = 19600
match = int(computed_Q8) == expected_Q8
matches.append(match)
print(f"CLAIM Q8: computed={int(computed_Q8)} expected={expected_Q8} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(matches)} claims, {sum(matches)} match, {len(matches)-sum(matches)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=50 expected=50 match=yes
CLAIM Q2: computed=1.58 expected=1.58 match=yes
CLAIM Q3: computed=-2.057 expected=-2.058 match=no
CLAIM Q4: computed=-3.63 expected=-3.64 match=no
CLAIM Q5: computed=0.15 expected=0.15 match=yes
CLAIM Q6: computed=20000 expected=20000 match=yes
CLAIM Q7: computed=400 expected=400 match=yes
CLAIM Q8: computed=19600 expected=19600 match=yes
VERIFICATION SUMMARY: 8 claims, 6 match, 2 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 50 | 50 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 1.58 | 1.58 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | -2.057 | -2.058 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | -3.63 | -3.64 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 0.15 | 0.15 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 20000 | 20000 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 400 | 400 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 19600 | 19600 | yes | match | 5 significant digits (as printed, at least 3) |

Mismatches: 0 of 8.
