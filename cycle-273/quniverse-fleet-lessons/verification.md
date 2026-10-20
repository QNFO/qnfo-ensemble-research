# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Expected unresolved failures per month $E[F]=2.16$.",
    "inputs": "N_w=36, p_f=0.12, \\alpha=0.5",
    "formula": "E[F] = N_w * p_f * (1-\\alpha)"
  },
  {
    "id": "Q2",
    "statement": "Effective unresolved‑failure probability $p_{\\text{eff}} = 0.06$.",
    "inputs": "p_f=0.12, \\alpha=0.5",
    "formula": "p_{\\text{eff}} = p_f * (1-\\alpha)"
  },
  {
    "id": "Q3",
    "statement": "Count‑derived mitigation factor $\\alpha_{\\text{counts}} \\approx 0.599$.",
    "inputs": "self‑heal actions=1889, handoff actions=1264",
    "formula": "\\alpha_{\\text{counts}} = 1889 / (1889 + 1264)"
  },
  {
    "id": "Q4",
    "statement": "Effective probability using count‑derived factor $p_{\\text{eff}}^{\\text{counts}} \\approx 0.0481066$.",
    "inputs": "p_f=0.12, \\alpha_{\\text{counts}}=0.599",
    "formula": "p_{\\text{eff}}^{\\text{counts}} = p_f * (1-\\alpha_{\\text{counts}})"
  },
  {
    "id": "Q5",
    "statement": "Variance of monthly failure count $\\operatorname{Var}[F]=2.0304$.",
    "inputs": "N_w=36, p_{\\text{eff}}=0.06",
    "formula": "Var[F] = N_w * p_{\\text{eff}} * (1 - p_{\\text{eff}})"
  },
  {
    "id": "Q6",
    "statement": "Standard deviation of monthly failure count $\\sigma_F \\approx 1.425$.",
    "inputs": "Var[F]=2.0304",
    "formula": "sigma_F = sqrt(Var[F])"
  },
  {
    "id": "Q7",
    "statement": "Papers per active project $9.65$ papers/project.",
    "inputs": "P_{\\text{total}}=917, N_{\\text{proj}}=95",
    "formula": "P_{\\text{total}} / N_{\\text{proj}}"
  },
  {
    "id": "Q8",
    "statement": "High‑severity gap proportion $11.9\\%$.",
    "inputs": "G_{\\text{high}}=5, G_{\\text{total}}=42",
    "formula": "(G_{\\text{high}} / G_{\\text{total}}) * 100"
  },
  {
    "id": "Q9",
    "statement": "Baseline composite autonomy score $C_{\\text{base}} = 4.26$.",
    "inputs": "w_c=0.4, w_{sh}=0.3, w_{oc}=0.3, S_c=4.5, S_{sh}=4.0, S_{oc}=4.2",
    "formula": "C = w_c*S_c + w_{sh}*S_{sh} + w_{oc}*S_{oc}"
  },
  {
    "id": "Q10",
    "statement": "Improved composite autonomy score $C_{\\text{new}} = 4.66$.",
    "inputs": "w_c=0.4, w_{sh}=0.3, w_{oc}=0.3, S_c'=4.9, S_{sh}'=4.4, S_{oc}'=4.6",
    "formula": "C = w_c*S_c' + w_{sh}*S_{sh}' + w_{oc}*S_{oc}'"
  },
  {
    "id": "Q11",
    "statement": "Baseline projected monthly gateway spend $S_{\\text{proj}} = \\$160.8$.",
    "inputs": "S_{\\text{base}}=150, E[F]=2.16, c_f=5",
    "formula": "S_{\\text{proj}} = S_{\\text{base}} + E[F] * c_f"
  },
  {
    "id": "Q12",
    "statement": "Improved projected monthly gateway spend $S_{\\text{proj}}' = \\$155.4$.",
    "inputs": "S_{\\text{base}}=150, E[F]'=1.08, c_f=5",
    "formula": "S_{\\text{proj}}' = S_{\\text{base}} + E[F]' * c_f"
  },
  {
    "id": "Q13",
    "statement": "Billing‑unit misread spend $S_{\\text{misread}} = \\$11{,}000$.",
    "inputs": "f_{\\text{unit}}=100, S_{\\text{corr}}=110",
    "formula": "S_{\\text{misread}} = f_{\\text{unit}} * S_{\\text{corr}}"
  },
  {
    "id": "Q14",
    "statement": "Cap‑violation ratio $73.3$‑fold (relative to $\\$150$ cap).",
    "inputs": "S_{\\text{misread}}=11000, C_{\\text{cap}}=150",
    "formula": "S_{\\text{misread}} / C_{\\text{cap}}"
  },
  {
    "id": "Q15",
    "statement": "Gate‑violation ratio $122.2$‑fold (relative to $\\$90$ gate).",
    "inputs": "S_{\\text{misread}}=11000, G_{\\text{gate}}=90",
    "formula": "S_{\\text{misread}} / G_{\\text{gate}}"
  },
  {
    "id": "Q16",
    "statement": "Gate exceedance for corrected spend $22.2\\%$.",
    "inputs": "S_{\\text{corr}}=110, G_{\\text{gate}}=90",
    "formula": "((S_{\\text{corr}} - G_{\\text{gate}}) / G_{\\text{gate}}) * 100"
  }
]

## Script
```python
import math

# Expected values as given in the paper (exact string representation)
expected = {
    "Q1": "2.16",
    "Q2": "0.06",
    "Q3": "0.599",
    "Q4": "0.0481066",
    "Q5": "2.0304",
    "Q6": "1.425",
    "Q7": "9.65",
    "Q8": "11.9",
    "Q9": "4.26",
    "Q10": "4.66",
    "Q11": "160.8",
    "Q12": "155.4",
    "Q13": "11000",
    "Q14": "73.3",
    "Q15": "122.2",
    "Q16": "22.2"
}

# Helper to format a number with the same number of decimal places as the expected string
def format_match(val, exp_str):
    if "." in exp_str:
        dec_places = len(exp_str.split(".")[1])
        fmt = f"{{:.{dec_places}f}}"
        return fmt.format(val)
    else:
        return str(int(round(val)))

# Compute each claim
results = {}

# Q1: E[F] = N_w * p_f * (1-α)
N_w = 36
p_f = 0.12
alpha = 0.5
E_F = N_w * p_f * (1 - alpha)
results["Q1"] = E_F

# Q2: p_eff = p_f * (1-α)
p_eff = p_f * (1 - alpha)
results["Q2"] = p_eff

# Q3: α_counts = 1889 / (1889 + 1264)
alpha_counts = 1889 / (1889 + 1264)
results["Q3"] = alpha_counts

# Q4: p_eff_counts = p_f * (1-α_counts)
p_eff_counts = p_f * (1 - alpha_counts)
results["Q4"] = p_eff_counts

# Q5: Var[F] = N_w * p_eff * (1 - p_eff)
var_F = N_w * p_eff * (1 - p_eff)
results["Q5"] = var_F

# Q6: sigma_F = sqrt(Var[F])
sigma_F = math.sqrt(var_F)
results["Q6"] = sigma_F

# Q7: papers per project = P_total / N_proj
P_total = 917
N_proj = 95
papers_per_proj = P_total / N_proj
results["Q7"] = papers_per_proj

# Q8: high‑severity gap proportion = (G_high / G_total) * 100
G_high = 5
G_total = 42
gap_pct = (G_high / G_total) * 100
results["Q8"] = gap_pct

# Q9: baseline composite autonomy score
w_c, w_sh, w_oc = 0.4, 0.3, 0.3
S_c, S_sh, S_oc = 4.5, 4.0, 4.2
C_base = w_c * S_c + w_sh * S_sh + w_oc * S_oc
results["Q9"] = C_base

# Q10: improved composite autonomy score
S_c_p, S_sh_p, S_oc_p = 4.9, 4.4, 4.6
C_new = w_c * S_c_p + w_sh * S_sh_p + w_oc * S_oc_p
results["Q10"] = C_new

# Q11: baseline projected spend = S_base + E[F] * c_f
S_base = 150
c_f = 5
S_proj = S_base + E_F * c_f
results["Q11"] = S_proj

# Q12: improved projected spend = S_base + E[F]' * c_f
E_F_prime = 1.08  # halved failure probability scenario
S_proj_prime = S_base + E_F_prime * c_f
results["Q12"] = S_proj_prime

# Q13: billing‑unit misread spend = f_unit * S_corr
f_unit = 100
S_corr = 110
S_misread = f_unit * S_corr
results["Q13"] = S_misread

# Q14: cap‑violation ratio = S_misread / C_cap
C_cap = 150
ratio_cap = S_misread / C_cap
results["Q14"] = ratio_cap

# Q15: gate‑violation ratio = S_misread / G_gate
G_gate = 90
ratio_gate = S_misread / G_gate
results["Q15"] = ratio_gate

# Q16: gate exceedance % = ((S_corr - G_gate) / G_gate) * 100
exceed_pct = ((S_corr - G_gate) / G_gate) * 100
results["Q16"] = exceed_pct

# Print verification lines
for qid in sorted(expected.keys(), key=lambda x: int(x[1:])):  # Q1, Q2, ...
    comp = results[qid]
    exp_str = expected[qid]
    comp_str = format_match(comp, exp_str)
    match = "yes" if comp_str == exp_str else "no"
    print(f"CLAIM {qid}: computed={comp_str} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for qid in expected if format_match(results[qid], expected[qid]) == expected[qid])} match, {sum(1 for qid in expected if format_match(results[qid], expected[qid]) != expected[qid])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=2.16 expected=2.16 match=yes
CLAIM Q2: computed=0.06 expected=0.06 match=yes
CLAIM Q3: computed=0.599 expected=0.599 match=yes
CLAIM Q4: computed=0.0481066 expected=0.0481066 match=yes
CLAIM Q5: computed=2.0304 expected=2.0304 match=yes
CLAIM Q6: computed=1.425 expected=1.425 match=yes
CLAIM Q7: computed=9.65 expected=9.65 match=yes
CLAIM Q8: computed=11.9 expected=11.9 match=yes
CLAIM Q9: computed=4.26 expected=4.26 match=yes
CLAIM Q10: computed=4.66 expected=4.66 match=yes
CLAIM Q11: computed=160.8 expected=160.8 match=yes
CLAIM Q12: computed=155.4 expected=155.4 match=yes
CLAIM Q13: computed=11000 expected=11000 match=yes
CLAIM Q14: computed=73.3 expected=73.3 match=yes
CLAIM Q15: computed=122.2 expected=122.2 match=yes
CLAIM Q16: computed=22.2 expected=22.2 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2.16 | 2.16 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 0.06 | 0.06 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.599 | 0.599 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.0481066 | 0.0481066 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q5 | 2.0304 | 2.0304 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 1.425 | 1.425 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 9.65 | 9.65 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 11.9 | 11.9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 4.26 | 4.26 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 4.66 | 4.66 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 160.8 | 160.8 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 155.4 | 155.4 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 11000 | 11000 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q14 | 73.3 | 73.3 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 122.2 | 122.2 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q16 | 22.2 | 22.2 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
