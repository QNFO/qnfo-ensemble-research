# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Number of distinct functional profiles is 3 125.",
    "inputs": "K=5 functions, L=5 ordinal levels per function",
    "formula": "P = L^K"
  },
  {
    "id": "Q2",
    "statement": "Binary present/absent coding yields 32 profiles and the resolution increase over binary is 97.65625‑fold.",
    "inputs": "K=5 functions, binary levels=2, L=5 ordinal levels",
    "formula": "P_binary = 2^K; increase = L^K / 2^K"
  },
  {
    "id": "Q3",
    "statement": "Evaluation instances equal 90 (9 environments × 10 seeds).",
    "inputs": "M_classes=9 environment classes, M_seeds=10 random seeds",
    "formula": "instances = M_classes * M_seeds"
  },
  {
    "id": "Q4",
    "statement": "Indoor environment proportion is 77.78 % (7/9).",
    "inputs": "M_indoor=7 indoor classes, total=9 classes",
    "formula": "P_indoor = M_indoor / total"
  },
  {
    "id": "Q5",
    "statement": "Outdoor environment proportion is 22.22 % (2/9).",
    "inputs": "M_outdoor=2 outdoor classes, total=9 classes",
    "formula": "P_outdoor = M_outdoor / total"
  },
  {
    "id": "Q6",
    "statement": "Total attribute entries are 18 000 (1 800 warriors × 10 attributes).",
    "inputs": "N_warriors=1800, N_attributes=10",
    "formula": "entries = N_warriors * N_attributes"
  },
  {
    "id": "Q7",
    "statement": "Expected number of disagreements between random traditions is 4.0.",
    "inputs": "K=5 functions, L=5 ordinal levels",
    "formula": "E[D] = K * (1 - 1/L)"
  },
  {
    "id": "Q8",
    "statement": "Variance of disagreements is 0.8 and standard deviation is approximately 0.894427.",
    "inputs": "K=5 functions, L=5 ordinal levels",
    "formula": "Var(D) = K * (1/L) * (1 - 1/L); sigma = sqrt(Var(D))"
  },
  {
    "id": "Q9",
    "statement": "Per‑function chance agreement is 0.2.",
    "inputs": "L=5 ordinal levels",
    "formula": "p_e = sum_{j=1}^{L} (1/L)^2 = L * (1/L)^2"
  },
  {
    "id": "Q10",
    "statement": "Cohen's κ equals 0.625 when raw agreement is 0.7.",
    "inputs": "p_o=0.7 observed raw agreement, p_e=0.2 chance agreement",
    "formula": "kappa = (p_o - p_e) / (1 - p_e)"
  },
  {
    "id": "Q11",
    "statement": "Total pairwise rater comparisons in the pilot are 60.",
    "inputs": "N=4 traditions, R=3 raters, K=5 functions",
    "formula": "comparisons = N * K * binom(R,2)"
  },
  {
    "id": "Q12",
    "statement": "Number of mechanism‑ablation configurations is 32.",
    "inputs": "M=5 candidate mechanisms",
    "formula": "configs = 2^M"
  },
  {
    "id": "Q13",
    "statement": "Total simulation runs equal 320 (32 configurations × 10 seeds).",
    "inputs": "configs=32 configurations, seeds=10 random seeds",
    "formula": "runs = configs * seeds"
  },
  {
    "id": "Q14",
    "statement": "Community intensity C is 0.25 for uniform familiarity q=0.5 among 100 members.",
    "inputs": "M=100 members, q=0.5 uniform familiarity",
    "formula": "C = (1 / binom(M,2)) * binom(M,2) * q^2 = q^2"
  },
  {
    "id": "Q15",
    "statement": "Community intensity C is approximately 0.248384 for 50 members with q=0.9 and 50 with q=0.1.",
    "inputs": "M=100 members, 50 with q=0.9, 50 with q=0.1",
    "formula": "C = (1 / binom(100,2)) * [1225*0.81 + 2500*0.09 + 1225*0.01]"
  },
  {
    "id": "Q16",
    "statement": "Projected cost for adding one tradition is $1 950.",
    "inputs": "hours=5 annotation hours, rate=150 dollars per hour, computer=1200 dollars",
    "formula": "cost = hours * rate + computer"
  }
]

## Script
```python
import math

def round_to(value, decimals):
    """Round value to a given number of decimal places."""
    factor = 10 ** decimals
    return round(value * factor) / factor

def format_number(value, decimals):
    """Format number with fixed decimal places (or as int if decimals==0)."""
    if decimals == 0:
        return str(int(value))
    else:
        fmt = "{:." + str(decimals) + "f}"
        return fmt.format(value)

# Q1
P = 5 ** 5
expected_Q1 = 3125
match_Q1 = P == expected_Q1
print(f"CLAIM Q1: computed={P} expected={expected_Q1} match={'yes' if match_Q1 else 'no'}")

# Q2 - binary profiles
P_binary = 2 ** 5
expected_Q2_binary = 32
match_Q2_binary = P_binary == expected_Q2_binary

# Q2 - resolution increase
increase = P / P_binary
expected_Q2_inc = 97.65625
inc_rounded = round_to(increase, 5)
match_Q2_inc = inc_rounded == expected_Q2_inc

print(f"CLAIM Q2 (binary): computed={P_binary} expected={expected_Q2_binary} match={'yes' if match_Q2_binary else 'no'}")
print(f"CLAIM Q2 (increase): computed={format_number(increase,5)} expected={expected_Q2_inc} match={'yes' if match_Q2_inc else 'no'}")

# Q3
instances = 9 * 10
expected_Q3 = 90
match_Q3 = instances == expected_Q3
print(f"CLAIM Q3: computed={instances} expected={expected_Q3} match={'yes' if match_Q3 else 'no'}")

# Q4
indoor = 7 / 9 * 100
expected_Q4 = 77.78
indoor_rounded = round_to(indoor, 2)
match_Q4 = indoor_rounded == expected_Q4
print(f"CLAIM Q4: computed={format_number(indoor,2)} expected={expected_Q4} match={'yes' if match_Q4 else 'no'}")

# Q5
outdoor = 2 / 9 * 100
expected_Q5 = 22.22
outdoor_rounded = round_to(outdoor, 2)
match_Q5 = outdoor_rounded == expected_Q5
print(f"CLAIM Q5: computed={format_number(outdoor,2)} expected={expected_Q5} match={'yes' if match_Q5 else 'no'}")

# Q6
entries = 1800 * 10
expected_Q6 = 18000
match_Q6 = entries == expected_Q6
print(f"CLAIM Q6: computed={entries} expected={expected_Q6} match={'yes' if match_Q6 else 'no'}")

# Q7
E_D = 5 * (1 - 1/5)
expected_Q7 = 4.0
E_D_rounded = round_to(E_D, 1)
match_Q7 = E_D_rounded == expected_Q7
print(f"CLAIM Q7: computed={format_number(E_D,1)} expected={expected_Q7} match={'yes' if match_Q7 else 'no'}")

# Q8
var_D = 5 * (1/5) * (1 - 1/5)
sigma = math.sqrt(var_D)
expected_var = 0.8
expected_sigma = 0.894427
var_rounded = round_to(var_D, 1)
sigma_rounded = round_to(sigma, 6)
match_var = var_rounded == expected_var
match_sigma = sigma_rounded == expected_sigma
print(f"CLAIM Q8 (variance): computed={format_number(var_D,1)} expected={expected_var} match={'yes' if match_var else 'no'}")
print(f"CLAIM Q8 (stddev): computed={format_number(sigma,6)} expected={expected_sigma} match={'yes' if match_sigma else 'no'}")

# Q9
p_e = 5 * (1/5)**2
expected_Q9 = 0.2
p_e_rounded = round_to(p_e, 1)
match_Q9 = p_e_rounded == expected_Q9
print(f"CLAIM Q9: computed={format_number(p_e,1)} expected={expected_Q9} match={'yes' if match_Q9 else 'no'}")

# Q10
p_o = 0.7
kappa = (p_o - p_e) / (1 - p_e)
expected_Q10 = 0.625
kappa_rounded = round_to(kappa, 3)
match_Q10 = kappa_rounded == expected_Q10
print(f"CLAIM Q10: computed={format_number(kappa,3)} expected={expected_Q10} match={'yes' if match_Q10 else 'no'}")

# Q11
comparisons = 4 * 5 * (math.comb(3,2))
expected_Q11 = 60
match_Q11 = comparisons == expected_Q11
print(f"CLAIM Q11: computed={comparisons} expected={expected_Q11} match={'yes' if match_Q11 else 'no'}")

# Q12
configs = 2 ** 5
expected_Q12 = 32
match_Q12 = configs == expected_Q12
print(f"CLAIM Q12: computed={configs} expected={expected_Q12} match={'yes' if match_Q12 else 'no'}")

# Q13
runs = configs * 10
expected_Q13 = 320
match_Q13 = runs == expected_Q13
print(f"CLAIM Q13: computed={runs} expected={expected_Q13} match={'yes' if match_Q13 else 'no'}")

# Q14
C_uniform = 0.5 ** 2
expected_Q14 = 0.25
C_uniform_rounded = round_to(C_uniform, 2)
match_Q14 = C_uniform_rounded == expected_Q14
print(f"CLAIM Q14: computed={format_number(C_uniform,2)} expected={expected_Q14} match={'yes' if match_Q14 else 'no'}")

# Q15
M = 100
# compute components
term1 = 1225 * 0.81
term2 = 2500 * 0.09
term3 = 1225 * 0.01
C_hetero = (term1 + term2 + term3) / 4950
expected_Q15 = 0.248384
C_hetero_rounded = round_to(C_hetero, 6)
match_Q15 = C_hetero_rounded == expected_Q15
print(f"CLAIM Q15: computed={format_number(C_hetero,6)} expected={expected_Q15} match={'yes' if match_Q15 else 'no'}")

# Q16
cost = 5 * 150 + 1200
expected_Q16 = 1950
match_Q16 = cost == expected_Q16
print(f"CLAIM Q16: computed={cost} expected={expected_Q16} match={'yes' if match_Q16 else 'no'}")

# Summary
total = 16
matches = sum([
    match_Q1,
    match_Q2_binary,
    match_Q2_inc,
    match_Q3,
    match_Q4,
    match_Q5,
    match_Q6,
    match_Q7,
    match_var,
    match_sigma,
    match_Q9,
    match_Q10,
    match_Q11,
    match_Q12,
    match_Q13,
    match_Q14,
    match_Q15,
    match_Q16
])
print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {total - matches} mismatch")

```

## Execution output
```
CLAIM Q1: computed=3125 expected=3125 match=yes
CLAIM Q2 (binary): computed=32 expected=32 match=yes
CLAIM Q2 (increase): computed=97.65625 expected=97.65625 match=yes
CLAIM Q3: computed=90 expected=90 match=yes
CLAIM Q4: computed=77.78 expected=77.78 match=yes
CLAIM Q5: computed=22.22 expected=22.22 match=yes
CLAIM Q6: computed=18000 expected=18000 match=yes
CLAIM Q7: computed=4.0 expected=4.0 match=yes
CLAIM Q8 (variance): computed=0.8 expected=0.8 match=yes
CLAIM Q8 (stddev): computed=0.894427 expected=0.894427 match=yes
CLAIM Q9: computed=0.2 expected=0.2 match=yes
CLAIM Q10: computed=0.625 expected=0.625 match=yes
CLAIM Q11: computed=60 expected=60 match=yes
CLAIM Q12: computed=32 expected=32 match=yes
CLAIM Q13: computed=320 expected=320 match=yes
CLAIM Q14: computed=0.25 expected=0.25 match=yes
CLAIM Q15: computed=0.248384 expected=0.248384 match=yes
CLAIM Q16: computed=1950 expected=1950 match=yes
VERIFICATION SUMMARY: 16 claims, 18 match, -2 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 3125 | 3125 | yes | match | 4 significant digits (as printed, at least 3) |
| Q3 | 90 | 90 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 77.78 | 77.78 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 22.22 | 22.22 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 18000 | 18000 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 4.0 | 4.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 0.2 | 0.2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 0.625 | 0.625 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 60 | 60 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 32 | 32 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 320 | 320 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 0.25 | 0.25 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 0.248384 | 0.248384 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q16 | 1950 | 1950 | yes | match | 4 significant digits (as printed, at least 3) |

Mismatches: 0 of 14.
