# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Expected failures per month = 2.16",
    "inputs": "N_w = 36, p_f = 0.12, alpha = 0.5",
    "formula": "E[F] = N_w * p_f * (1 - alpha)"
  },
  {
    "id": "Q2",
    "statement": "Papers per active project = 9.65",
    "inputs": "P_total = 917, N_proj = 95",
    "formula": "Papers per project = P_total / N_proj"
  },
  {
    "id": "Q3",
    "statement": "High‑severity gap proportion = 11.9 %",
    "inputs": "G_high = 5, G_total = 42",
    "formula": "High‑severity proportion = (G_high / G_total) * 100"
  },
  {
    "id": "Q4",
    "statement": "Baseline composite autonomy score = 4.26",
    "inputs": "S_c = 4.5, S_sh = 4.0, S_oc = 4.2, w_c = 0.4, w_sh = 0.3, w_oc = 0.3",
    "formula": "C_base = w_c*S_c + w_sh*S_sh + w_oc*S_oc"
  },
  {
    "id": "Q5",
    "statement": "Improved composite autonomy score = 4.66",
    "inputs": "S_c' = 4.9, S_sh' = 4.4, S_oc' = 4.6, w_c = 0.4, w_sh = 0.3, w_oc = 0.3",
    "formula": "C_new = w_c*S_c' + w_sh*S_sh' + w_oc*S_oc'"
  },
  {
    "id": "Q6",
    "statement": "Projected monthly gateway spend (baseline) = $160.8",
    "inputs": "S_base = 150, E[F] = 2.16, c_f = 5",
    "formula": "S_proj = S_base + E[F] * c_f"
  },
  {
    "id": "Q7",
    "statement": "Projected monthly gateway spend (improved) = $155.4",
    "inputs": "S_base = 150, E[F]_new = 1.08, c_f = 5",
    "formula": "S_proj_improved = S_base + E[F]_new * c_f"
  },
  {
    "id": "Q8",
    "statement": "Billing‑unit misread spend = $11 000",
    "inputs": "f_unit = 100, S_corr = 110",
    "formula": "S_misread = f_unit * S_corr"
  },
  {
    "id": "Q9",
    "statement": "Cap‑violation ratio (misread) = 73.3",
    "inputs": "S_misread = 11000, C = 150",
    "formula": "ratio = S_misread / C"
  },
  {
    "id": "Q10",
    "statement": "Corrected ratio = 0.733",
    "inputs": "S_corr = 110, C = 150",
    "formula": "ratio_corr = S_corr / C"
  }
]

## Script
```python
# Compute and verify quantitative claims from the paper

def fmt(x):
    """Format with at least 8 significant digits."""
    # Use general format with high precision
    return f"{x:.8g}"

# Claim Q1
N_w = 36
p_f = 0.12
alpha = 0.5
E_F = N_w * p_f * (1 - alpha)          # 36 * 0.12 * 0.5 = 2.16
exp_Q1 = 2.16
comp_Q1 = round(E_F, 2)
match_Q1 = comp_Q1 == exp_Q1
print(f"CLAIM Q1: computed={fmt(comp_Q1)} expected={exp_Q1} match={'yes' if match_Q1 else 'no'}")

# Claim Q2
P_total = 917
N_proj = 95
papers_per_proj = P_total / N_proj      # 9.65263158...
exp_Q2 = 9.65
comp_Q2 = round(papers_per_proj, 2)
match_Q2 = comp_Q2 == exp_Q2
print(f"CLAIM Q2: computed={fmt(comp_Q2)} expected={exp_Q2} match={'yes' if match_Q2 else 'no'}")

# Claim Q3
G_high = 5
G_total = 42
high_sev_pct = (G_high / G_total) * 100  # 11.9047619...
exp_Q3 = 11.9
comp_Q3 = round(high_sev_pct, 1)
match_Q3 = comp_Q3 == exp_Q3
print(f"CLAIM Q3: computed={fmt(comp_Q3)} expected={exp_Q3} match={'yes' if match_Q3 else 'no'}")

# Claim Q4
S_c = 4.5
S_sh = 4.0
S_oc = 4.2
w_c = 0.4
w_sh = 0.3
w_oc = 0.3
C_base = w_c*S_c + w_sh*S_sh + w_oc*S_oc   # 4.26
exp_Q4 = 4.26
comp_Q4 = round(C_base, 2)
match_Q4 = comp_Q4 == exp_Q4
print(f"CLAIM Q4: computed={fmt(comp_Q4)} expected={exp_Q4} match={'yes' if match_Q4 else 'no'}")

# Claim Q5
S_c_n = 4.9
S_sh_n = 4.4
S_oc_n = 4.6
C_new = w_c*S_c_n + w_sh*S_sh_n + w_oc*S_oc_n   # 4.66
exp_Q5 = 4.66
comp_Q5 = round(C_new, 2)
match_Q5 = comp_Q5 == exp_Q5
print(f"CLAIM Q5: computed={fmt(comp_Q5)} expected={exp_Q5} match={'yes' if match_Q5 else 'no'}")

# Claim Q6
S_base = 150
c_f = 5
S_proj = S_base + E_F * c_f                # 150 + 2.16*5 = 160.8
exp_Q6 = 160.8
comp_Q6 = round(S_proj, 1)
match_Q6 = comp_Q6 == exp_Q6
print(f"CLAIM Q6: computed={fmt(comp_Q6)} expected={exp_Q6} match={'yes' if match_Q6 else 'no'}")

# Claim Q7
E_F_new = 1.08
S_proj_imp = S_base + E_F_new * c_f        # 150 + 1.08*5 = 155.4
exp_Q7 = 155.4
comp_Q7 = round(S_proj_imp, 1)
match_Q7 = comp_Q7 == exp_Q7
print(f"CLAIM Q7: computed={fmt(comp_Q7)} expected={exp_Q7} match={'yes' if match_Q7 else 'no'}")

# Claim Q8
f_unit = 100
S_corr = 110
S_misread = f_unit * S_corr                # 100 * 110 = 11000
exp_Q8 = 11000
comp_Q8 = S_misread
match_Q8 = comp_Q8 == exp_Q8
print(f"CLAIM Q8: computed={fmt(comp_Q8)} expected={exp_Q8} match={'yes' if match_Q8 else 'no'}")

# Claim Q9
C_cap = 150
ratio = S_misread / C_cap                  # 11000 / 150 = 73.333...
exp_Q9 = 73.3
comp_Q9 = round(ratio, 1)
match_Q9 = comp_Q9 == exp_Q9
print(f"CLAIM Q9: computed={fmt(comp_Q9)} expected={exp_Q9} match={'yes' if match_Q9 else 'no'}")

# Claim Q10
ratio_corr = S_corr / C_cap                # 110 / 150 = 0.73333...
exp_Q10 = 0.733
comp_Q10 = round(ratio_corr, 3)
match_Q10 = comp_Q10 == exp_Q10
print(f"CLAIM Q10: computed={fmt(comp_Q10)} expected={exp_Q10} match={'yes' if match_Q10 else 'no'}")

# Summary
total = 10
matches = sum([match_Q1, match_Q2, match_Q3, match_Q4, match_Q5,
               match_Q6, match_Q7, match_Q8, match_Q9, match_Q10])
print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {total - matches} mismatch")

```

## Execution output
```
CLAIM Q1: computed=2.16 expected=2.16 match=yes
CLAIM Q2: computed=9.65 expected=9.65 match=yes
CLAIM Q3: computed=11.9 expected=11.9 match=yes
CLAIM Q4: computed=4.26 expected=4.26 match=yes
CLAIM Q5: computed=4.66 expected=4.66 match=yes
CLAIM Q6: computed=160.8 expected=160.8 match=yes
CLAIM Q7: computed=155.4 expected=155.4 match=yes
CLAIM Q8: computed=11000 expected=11000 match=yes
CLAIM Q9: computed=73.3 expected=73.3 match=yes
CLAIM Q10: computed=0.733 expected=0.733 match=yes
VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2.16 | 2.16 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 9.65 | 9.65 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 11.9 | 11.9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 4.26 | 4.26 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 4.66 | 4.66 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 160.8 | 160.8 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 155.4 | 155.4 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 11000 | 11000 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 73.3 | 73.3 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 0.733 | 0.733 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 10.
