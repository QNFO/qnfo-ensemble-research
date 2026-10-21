# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The number of renderings is 40.",
    "inputs": "n_t = 10, n_d = 4",
    "formula": "N_rend = n_t * n_d"
  },
  {
    "id": "Q2",
    "statement": "The number of unordered lexicon pairs per object is 6.",
    "inputs": "n_d = 4",
    "formula": "binom(n_d,2) = n_d * (n_d - 1) / 2"
  },
  {
    "id": "Q3",
    "statement": "The total number of pairwise analogy hypotheses is 60.",
    "inputs": "n_t = 10, n_d = 4",
    "formula": "N_hyp = n_t * binom(n_d,2)"
  },
  {
    "id": "Q4",
    "statement": "The total number of evaluation points is 180.",
    "inputs": "N_hyp = 60",
    "formula": "E_total = N_hyp * 3"
  },
  {
    "id": "Q5",
    "statement": "The expert‑rating time for all hypotheses (single rater) is 5.0 h.",
    "inputs": "N_hyp = 60, rating per hypothesis = 5 minutes",
    "formula": "T_rate = N_hyp * 5 minutes, then convert minutes to hours"
  },
  {
    "id": "Q6",
    "statement": "With three independent raters the total rating time is 15.0 h.",
    "inputs": "T_rate = 5.0 h",
    "formula": "T_rate^(3) = 3 * T_rate"
  },
  {
    "id": "Q7",
    "statement": "The baseline hypothesis pool contains 20 hypotheses.",
    "inputs": "n_t = 10, k0 = 2",
    "formula": "N0 = n_t * k0"
  },
  {
    "id": "Q8",
    "statement": "The baseline rating time is 1.67 h.",
    "inputs": "N0 = 20, rating per hypothesis = 5 minutes",
    "formula": "T_base = N0 * 5 minutes, then convert to hours"
  },
  {
    "id": "Q9",
    "statement": "The synthesis‑phase beam cost is 5.0 h.",
    "inputs": "n_t = 10, B = 3, cost per candidate = 10 minutes",
    "formula": "T_syn = n_t * B * 10 minutes, then convert to hours"
  },
  {
    "id": "Q10",
    "statement": "The total expert‑validation budget (unfiltered) is 20.0 h.",
    "inputs": "T_rate^(3) = 15.0 h, T_syn = 5.0 h",
    "formula": "T_total = T_rate^(3) + T_syn"
  },
  {
    "id": "Q11",
    "statement": "After applying a pre‑filter with pass rate 0.4, 24 hypotheses are rated.",
    "inputs": "q = 0.4, N_hyp = 60",
    "formula": "N_rated = q * N_hyp"
  },
  {
    "id": "Q12",
    "statement": "The filtered rating time is 6.0 h.",
    "inputs": "N_rated = 24, rating per hypothesis = 5 minutes, 3 raters",
    "formula": "T_rated = N_rated * 5 minutes * 3, then convert to hours"
  },
  {
    "id": "Q13",
    "statement": "The filtered total expert time is 11.0 h.",
    "inputs": "T_rated = 6.0 h, T_syn = 5.0 h",
    "formula": "T_total_filtered = T_rated + T_syn"
  },
  {
    "id": "Q14",
    "statement": "A structural‑overlap score for the illustrative pair is 4/7 ≈ 0.571.",
    "inputs": "|R+| = 4, |R‑| = 1, |R0| = 2",
    "formula": "s = |R+| / (|R+| + |R‑| + |R0|)"
  },
  {
    "id": "Q15",
    "statement": "The unmitigated probability that at least one spurious link survives is ≈ 0.265.",
    "inputs": "p0 = 0.05, m = 6",
    "formula": "P_any = 1 - (1 - p0)^m"
  },
  {
    "id": "Q16",
    "statement": "After validation with sensitivity 0.8, the residual spurious‑link probability is ≈ 0.059.",
    "inputs": "p0 = 0.05, s = 0.8, m = 6",
    "formula": "P_any_tested = 1 - (1 - p0*(1-s))^m"
  }
]

## Script
```python
# Compute and verify quantitative claims from the paper

def fmt(val, digits):
    """Format a number with given significant digits (as string)."""
    if isinstance(val, int):
        return str(val)
    # round to the specified number of decimal places
    return f"{round(val, digits):.{digits}f}".rstrip('0').rstrip('.') if digits > 0 else str(val)

# Claim Q1
N_rend = 10 * 4
exp_Q1 = "40"
calc_Q1 = fmt(N_rend, 0)
match_Q1 = calc_Q1 == exp_Q1

# Claim Q2
binom = 4 * (4 - 1) // 2
exp_Q2 = "6"
calc_Q2 = fmt(binom, 0)
match_Q2 = calc_Q2 == exp_Q2

# Claim Q3
N_hyp = 10 * binom
exp_Q3 = "60"
calc_Q3 = fmt(N_hyp, 0)
match_Q3 = calc_Q3 == exp_Q3

# Claim Q4
E_total = N_hyp * 3
exp_Q4 = "180"
calc_Q4 = fmt(E_total, 0)
match_Q4 = calc_Q4 == exp_Q4

# Claim Q5
T_rate_min = N_hyp * 5          # minutes
T_rate_h = T_rate_min / 60.0    # hours
exp_Q5 = "5.0"
calc_Q5 = fmt(T_rate_h, 1)
match_Q5 = calc_Q5 == exp_Q5

# Claim Q6
T_rate_3 = 3 * T_rate_h
exp_Q6 = "15.0"
calc_Q6 = fmt(T_rate_3, 1)
match_Q6 = calc_Q6 == exp_Q6

# Claim Q7
N0 = 10 * 2
exp_Q7 = "20"
calc_Q7 = fmt(N0, 0)
match_Q7 = calc_Q7 == exp_Q7

# Claim Q8
T_base_min = N0 * 5
T_base_h = T_base_min / 60.0
exp_Q8 = "1.67"
calc_Q8 = fmt(T_base_h, 2)
match_Q8 = calc_Q8 == exp_Q8

# Claim Q9
T_syn_min = 10 * 3 * 10
T_syn_h = T_syn_min / 60.0
exp_Q9 = "5.0"
calc_Q9 = fmt(T_syn_h, 1)
match_Q9 = calc_Q9 == exp_Q9

# Claim Q10
T_total = T_rate_3 + T_syn_h
exp_Q10 = "20.0"
calc_Q10 = fmt(T_total, 1)
match_Q10 = calc_Q10 == exp_Q10

# Claim Q11
N_rated = 0.4 * N_hyp
exp_Q11 = "24"
calc_Q11 = fmt(N_rated, 0)
match_Q11 = calc_Q11 == exp_Q11

# Claim Q12
T_rated_min = N_rated * 5 * 3
T_rated_h = T_rated_min / 60.0
exp_Q12 = "6.0"
calc_Q12 = fmt(T_rated_h, 1)
match_Q12 = calc_Q12 == exp_Q12

# Claim Q13
T_total_filt = T_rated_h + T_syn_h
exp_Q13 = "11.0"
calc_Q13 = fmt(T_total_filt, 1)
match_Q13 = calc_Q13 == exp_Q13

# Claim Q14
s = 4 / (4 + 1 + 2)
exp_Q14 = "0.571"
calc_Q14 = fmt(s, 3)
match_Q14 = calc_Q14 == exp_Q14

# Claim Q15
p0 = 0.05
m = 6
P_any = 1 - (1 - p0) ** m
exp_Q15 = "0.265"
calc_Q15 = fmt(P_any, 3)
match_Q15 = calc_Q15 == exp_Q15

# Claim Q16
sensitivity = 0.8
residual = p0 * (1 - sensitivity)
P_any_tested = 1 - (1 - residual) ** m
exp_Q16 = "0.059"
calc_Q16 = fmt(P_any_tested, 3)
match_Q16 = calc_Q16 == exp_Q16

# Print results
claims = [
    ("Q1", calc_Q1, exp_Q1, match_Q1),
    ("Q2", calc_Q2, exp_Q2, match_Q2),
    ("Q3", calc_Q3, exp_Q3, match_Q3),
    ("Q4", calc_Q4, exp_Q4, match_Q4),
    ("Q5", calc_Q5, exp_Q5, match_Q5),
    ("Q6", calc_Q6, exp_Q6, match_Q6),
    ("Q7", calc_Q7, exp_Q7, match_Q7),
    ("Q8", calc_Q8, exp_Q8, match_Q8),
    ("Q9", calc_Q9, exp_Q9, match_Q9),
    ("Q10", calc_Q10, exp_Q10, match_Q10),
    ("Q11", calc_Q11, exp_Q11, match_Q11),
    ("Q12", calc_Q12, exp_Q12, match_Q12),
    ("Q13", calc_Q13, exp_Q13, match_Q13),
    ("Q14", calc_Q14, exp_Q14, match_Q14),
    ("Q15", calc_Q15, exp_Q15, match_Q15),
    ("Q16", calc_Q16, exp_Q16, match_Q16),
]

for cid, comp, exp, ok in claims:
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,_,_,ok in claims if ok)} match, {sum(1 for _,_,_,ok in claims if not ok)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=40 expected=40 match=yes
CLAIM Q2: computed=6 expected=6 match=yes
CLAIM Q3: computed=60 expected=60 match=yes
CLAIM Q4: computed=180 expected=180 match=yes
CLAIM Q5: computed=5 expected=5.0 match=no
CLAIM Q6: computed=15 expected=15.0 match=no
CLAIM Q7: computed=20 expected=20 match=yes
CLAIM Q8: computed=1.67 expected=1.67 match=yes
CLAIM Q9: computed=5 expected=5.0 match=no
CLAIM Q10: computed=20 expected=20.0 match=no
CLAIM Q11: computed=24.0 expected=24 match=no
CLAIM Q12: computed=6 expected=6.0 match=no
CLAIM Q13: computed=11 expected=11.0 match=no
CLAIM Q14: computed=0.571 expected=0.571 match=yes
CLAIM Q15: computed=0.265 expected=0.265 match=yes
CLAIM Q16: computed=0.059 expected=0.059 match=yes
VERIFICATION SUMMARY: 16 claims, 9 match, 7 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 40 | 40 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 6 | 6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 60 | 60 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 180 | 180 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 5 | 5.0 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 15 | 15.0 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 20 | 20 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 1.67 | 1.67 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 5 | 5.0 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 20 | 20.0 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 24.0 | 24 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 6 | 6.0 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 11 | 11.0 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 0.571 | 0.571 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 0.265 | 0.265 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 0.059 | 0.059 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
