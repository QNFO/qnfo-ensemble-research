# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The basic reproduction number with full transparency (β=1) and average degree per layer k=10 is R₀ = 10.",
    "inputs": "β = 1, k = 10",
    "formula": "R0 = β * k"
  },
  {
    "id": "Q2",
    "statement": "With partial attention decay β=0.3 and average degree per layer k=10 the basic reproduction number is R₀ = 3.",
    "inputs": "β = 0.3, k = 10",
    "formula": "R0 = β * k"
  },
  {
    "id": "Q3",
    "statement": "For R₀ = 3 the suppression threshold required for subcritical cascades is q* = 2/3 ≈ 0.6667.",
    "inputs": "R0 = 3",
    "formula": "q* = 1 - 1/R0"
  },
  {
    "id": "Q4",
    "statement": "For R₀ = 10 the suppression threshold required for subcritical cascades is q* = 0.9.",
    "inputs": "R0 = 10",
    "formula": "q* = 1 - 1/R0"
  },
  {
    "id": "Q5",
    "statement": "The expected payoff for the suppressor strategy with cost c = 0.1 is π_S = 0.9.",
    "inputs": "c = 0.1",
    "formula": "π_S = 1 - c"
  },
  {
    "id": "Q6",
    "statement": "The expected payoff for the transparent strategy with shock probability p = 0.2 and damage L = 1 is π_T = 0.8.",
    "inputs": "p = 0.2, L = 1",
    "formula": "π_T = 1 - p * L"
  },
  {
    "id": "Q7",
    "statement": "Without suppression (q = 0) the maximal number of simultaneous revelations a group can absorb is n_max = 6.",
    "inputs": "C = 1, δ = 0.15",
    "formula": "n_max = floor(C / δ)"
  },
  {
    "id": "Q8",
    "statement": "With suppression at the critical rate q* = 2/3 the maximal number of simultaneous revelations a group can absorb is n_max = 20.",
    "inputs": "C = 1, δ = 0.15, q = 2/3",
    "formula": "n_max = floor(C / (δ * (1 - q)))"
  },
  {
    "id": "Q9",
    "statement": "The capacity increase factor from no suppression to critical suppression is 20 / 6 ≈ 3.33.",
    "inputs": "n_max_no = 6, n_max_crit = 20",
    "formula": "ratio = n_max_crit / n_max_no"
  },
  {
    "id": "Q10",
    "statement": "The elasticity of link deletion is e_del = 1.",
    "inputs": "r_del = 0.5, f_del = 0.5",
    "formula": "e_del = r_del / f_del"
  },
  {
    "id": "Q11",
    "statement": "To achieve subcriticality for R₀ = 3 by link deletion alone one must remove a fraction f_req = 2/3 ≈ 0.6667 of links.",
    "inputs": "R0 = 3",
    "formula": "f_req = 1 - 1/R0"
  },
  {
    "id": "Q12",
    "statement": "A detection pipeline processing 10,000 messages per second at a cost of $0.00002 per inference incurs an hourly operational cost of $7.20.",
    "inputs": "messages_per_sec = 10000, seconds_per_hour = 3600, cost_per_inference = 0.00002",
    "formula": "cost = messages_per_sec * seconds_per_hour * cost_per_inference"
  },
  {
    "id": "Q13",
    "statement": "With a true‑positive rate of 0.8, achieving an effective suppression factor q_eff > 0.66 requires the raw filter to be set to q > 0.825.",
    "inputs": "target_q_eff = 0.66, true_positive_rate = 0.8",
    "formula": "q = target_q_eff / true_positive_rate"
  }
]

## Script
```python
import math

def fmt(x):
    # format with at least 8 significant digits, removing trailing zeros
    s = f"{x:.10g}"
    return s

claims = [
    ("Q1", 1 * 10, "10"),
    ("Q2", 0.3 * 10, "3"),
    ("Q3", 1 - 1/3, "0.6667"),
    ("Q4", 1 - 1/10, "0.9"),
    ("Q5", 1 - 0.1, "0.9"),
    ("Q6", 1 - 0.2 * 1, "0.8"),
    ("Q7", math.floor(1 / 0.15), "6"),
    ("Q8", math.floor(1 / (0.15 * (1 - 2/3))), "20"),
    ("Q9", 20 / 6, "3.33"),
    ("Q10", 0.5 / 0.5, "1"),
    ("Q11", 1 - 1/3, "0.6667"),
    ("Q12", 10000 * 3600 * 0.00002, "7.20"),
    ("Q13", 0.66 / 0.8, "0.825"),
]

for cid, comp, exp in claims:
    # round computed to match expected precision for comparison
    # determine number of decimal places in expected
    if "." in exp:
        dec = len(exp.split(".")[1])
        comp_rounded = round(comp, dec)
    else:
        comp_rounded = int(round(comp))
    match = "yes" if str(comp_rounded) == exp else "no"
    print(f"CLAIM {cid}: computed={fmt(comp)} expected={exp} match={match}")
print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if (str(round(c, len(e.split('.')[1])) if '.' in e else int(round(c))) == e))} match, {len(claims) - sum(1 for _,c,e in claims if (str(round(c, len(e.split('.')[1])) if '.' in e else int(round(c))) == e))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=10 expected=10 match=yes
CLAIM Q2: computed=3 expected=3 match=yes
CLAIM Q3: computed=0.6666666667 expected=0.6667 match=yes
CLAIM Q4: computed=0.9 expected=0.9 match=yes
CLAIM Q5: computed=0.9 expected=0.9 match=yes
CLAIM Q6: computed=0.8 expected=0.8 match=yes
CLAIM Q7: computed=6 expected=6 match=yes
CLAIM Q8: computed=20 expected=20 match=yes
CLAIM Q9: computed=3.333333333 expected=3.33 match=yes
CLAIM Q10: computed=1 expected=1 match=yes
CLAIM Q11: computed=0.6666666667 expected=0.6667 match=yes
CLAIM Q12: computed=720 expected=7.20 match=no
CLAIM Q13: computed=0.825 expected=0.825 match=yes
VERIFICATION SUMMARY: 13 claims, 12 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 10 | 10 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.6666666667 | 0.6667 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 0.9 | 0.9 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.9 | 0.9 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 0.8 | 0.8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 6 | 6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 20 | 20 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 3.333333333 | 3.33 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 0.6666666667 | 0.6667 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 720 | 7.20 | no | MISMATCH | 3 significant digits (as the paper states, at least 2) |
| Q13 | 0.825 | 0.825 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 1 of 13.


## Auto-corrections

The worker corrected these independently-verified values in place of the paper's stated values (deterministic, no model edit):

| claim | stated | corrected |
|---|---|---|
| Q12 | 7.20 | 720 |
