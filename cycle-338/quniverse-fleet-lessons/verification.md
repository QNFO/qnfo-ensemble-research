# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The mitigation factor α equals the ratio of self‑heal actions to total actions, α = H / (H + X) ≈ 0.5991.",
    "inputs": "H = 1,889; X = 1,264",
    "formula": "α = H / (H + X)"
  },
  {
    "id": "Q2",
    "statement": "The expected number of unresolved worker‑script failures per month is E[F] = N_w · p_f · (1 − α) ≈ 1.732.",
    "inputs": "N_w = 36; p_f = 0.12; α = 0.5991",
    "formula": "E[F] = N_w * p_f * (1 - α)"
  },
  {
    "id": "Q3",
    "statement": "The standard deviation of the monthly failure count is σ_F = sqrt(N_w · p_eff · (1 − p_eff)) ≈ 1.284.",
    "inputs": "N_w = 36; p_f = 0.12; α = 0.5991; p_eff = p_f · (1 − α) = 0.0481063",
    "formula": "σ_F = sqrt(N_w * p_eff * (1 - p_eff))"
  },
  {
    "id": "Q4",
    "statement": "The corpus productivity is 9.65 papers per active project, computed as P_total / N_proj.",
    "inputs": "P_total = 917; N_proj = 95",
    "formula": "P_total / N_proj"
  },
  {
    "id": "Q5",
    "statement": "The high‑severity gap proportion is 11.9 %, computed as G_high / G_total.",
    "inputs": "G_high = 5; G_total = 42",
    "formula": "G_high / G_total"
  },
  {
    "id": "Q6a",
    "statement": "The vector‑index storage in bytes is S_vi = rows · bytes_per_row = 17,744,384 B.",
    "inputs": "rows = 34,657; bytes_per_row = 512 B",
    "formula": "S_vi = rows * bytes_per_row"
  },
  {
    "id": "Q6b",
    "statement": "Converted to MiB, the vector‑index storage is S_vi ≈ 16.922 MiB.",
    "inputs": "S_vi = 17,744,384 B; 1 MiB = 1,048,576 B",
    "formula": "S_vi_MiB = S_vi / 1,048,576"
  },
  {
    "id": "Q6c",
    "statement": "Total storage is approximately 320.9 MB, computed as S_db + S_vi_MiB.",
    "inputs": "S_db = 304 MB; S_vi_MiB ≈ 16.922 MiB (treated as MB)",
    "formula": "S_tot = S_db + S_vi_MiB"
  },
  {
    "id": "Q7",
    "statement": "The baseline composite autonomy score is C_base = 4.26.",
    "inputs": "w_c = 0.4; S_c = 4.5; w_sh = 0.3; S_sh = 4.0; w_oc = 0.3; S_oc = 4.2",
    "formula": "C_base = w_c*S_c + w_sh*S_sh + w_oc*S_oc"
  },
  {
    "id": "Q8",
    "statement": "The improved composite autonomy score after a 50 % failure‑probability reduction is C_new = 4.66.",
    "inputs": "w_c = 0.4; S_c' = 4.9; w_sh = 0.3; S_sh' = 4.4; w_oc = 0.3; S_oc' = 4.6",
    "formula": "C_new = w_c*S_c' + w_sh*S_sh' + w_oc*S_oc'"
  },
  {
    "id": "Q9",
    "statement": "Baseline projected monthly gateway spend is S_proj = $158.66, computed as S_cap + E[F]·c_f.",
    "inputs": "S_cap = 150 $; E[F] = 1.731828; c_f = 5 $/failure",
    "formula": "S_proj = S_cap + E[F] * c_f"
  },
  {
    "id": "Q10",
    "statement": "Improved projected spend after halving p_f is S_proj' = $154.33, computed as S_cap + E[F]'·c_f.",
    "inputs": "S_cap = 150 $; E[F]' = 0.865922; c_f = 5 $/failure",
    "formula": "S_proj' = S_cap + E[F]' * c_f"
  },
  {
    "id": "Q11",
    "statement": "The billing‑unit misread inflates spend to S_misread = $11,000, computed as f_unit · S_corr.",
    "inputs": "f_unit = 100; S_corr = 110 $",
    "formula": "S_misread = f_unit * S_corr"
  },
  {
    "id": "Q12",
    "statement": "The misread spend exceeds the $150 cap by a factor of 73.3, computed as S_misread / C_cap.",
    "inputs": "S_misread = 11,000 $; C_cap = 150 $",
    "formula": "S_misread / C_cap"
  },
  {
    "id": "Q13",
    "statement": "The cap‑excess factor is 72.3‑fold, computed as (S_misread − C_cap) / C_cap.",
    "inputs": "S_misread = 11,000 $; C_cap = 150 $",
    "formula": "(S_misread - C_cap) / C_cap"
  },
  {
    "id": "Q14",
    "statement": "The misread spend exceeds the $90 gate by a factor of 122.2, computed as S_misread / G_gate.",
    "inputs": "S_misread = 11,000 $; G_gate = 90 $",
    "formula": "S_misread / G_gate"
  }
]

## Script
```python
import math

def round_to_match(value, expected_str):
    """Round value to the same number of decimal places as expected_str."""
    # Remove any commas and dollar signs for counting
    clean = expected_str.replace(',', '').replace('$', '')
    if '.' in clean:
        dec_places = len(clean.split('.')[1])
    else:
        dec_places = 0
    return round(value, dec_places)

def compare(value, expected_str):
    """Return 'yes' if rounded value matches expected string, else 'no'."""
    rounded = round_to_match(value, expected_str)
    # Format rounded number similarly to expected (preserve commas if any)
    if ',' in expected_str:
        # Insert commas for thousands
        formatted = f"{rounded:,.0f}"
    else:
        # Preserve decimal places
        if '.' in expected_str:
            dec = len(expected_str.split('.')[1])
            fmt = f"{{:.{dec}f}}"
            formatted = fmt.format(rounded)
        else:
            formatted = str(int(rounded))
    # Remove any trailing zeros after decimal if expected doesn't have them
    return formatted == expected_str.replace('$', ''), formatted

# Inputs
H = 1889
X = 1264
N_w = 36
p_f = 0.12
P_total = 917
N_proj = 95
G_high = 5
G_total = 42
rows = 34657
bytes_per_row = 512
S_db_MB = 304
w_c, S_c = 0.4, 4.5
w_sh, S_sh = 0.3, 4.0
w_oc, S_oc = 0.3, 4.2
w_c2, S_c_p = 0.4, 4.9
w_sh2, S_sh_p = 0.3, 4.4
w_oc2, S_oc_p = 0.3, 4.6
S_cap = 150.0
c_f = 5.0
f_unit = 100
S_corr = 110.0
C_cap = 150.0
G_gate = 90.0

# Claims calculations
alpha = H / (H + X)                         # Q1
E_F = N_w * p_f * (1 - alpha)               # Q2
p_eff = p_f * (1 - alpha)                   # intermediate for Q3
sigma_F = math.sqrt(N_w * p_eff * (1 - p_eff))  # Q3
corpus_prod = P_total / N_proj               # Q4
high_gap_prop = G_high / G_total * 100       # Q5 (percentage)
S_vi_bytes = rows * bytes_per_row            # Q6a
S_vi_MiB = S_vi_bytes / 1_048_576            # Q6b
S_tot_MB = S_db_MB + S_vi_MiB                # Q6c (treated as MB)
C_base = w_c * S_c + w_sh * S_sh + w_oc * S_oc   # Q7
C_new = w_c2 * S_c_p + w_sh2 * S_sh_p + w_oc2 * S_oc_p  # Q8
S_proj = S_cap + E_F * c_f                    # Q9
E_F_prime = N_w * (p_f/2) * (1 - alpha)      # halved p_f
S_proj_prime = S_cap + E_F_prime * c_f       # Q10
S_misread = f_unit * S_corr                  # Q11
ratio_cap = S_misread / C_cap                # Q12
excess_cap = (S_misread - C_cap) / C_cap     # Q13
ratio_gate = S_misread / G_gate              # Q14

# Expected strings
expected = {
    "Q1": "0.5991",
    "Q2": "1.732",
    "Q3": "1.284",
    "Q4": "9.65",
    "Q5": "11.9",
    "Q6a": "17744384",
    "Q6b": "16.922",
    "Q6c": "320.9",
    "Q7": "4.26",
    "Q8": "4.66",
    "Q9": "158.66",
    "Q10": "154.33",
    "Q11": "11000",
    "Q12": "73.3",
    "Q13": "72.3",
    "Q14": "122.2"
}

# Mapping of computed values
computed = {
    "Q1": alpha,
    "Q2": E_F,
    "Q3": sigma_F,
    "Q4": corpus_prod,
    "Q5": high_gap_prop,
    "Q6a": S_vi_bytes,
    "Q6b": S_vi_MiB,
    "Q6c": S_tot_MB,
    "Q7": C_base,
    "Q8": C_new,
    "Q9": S_proj,
    "Q10": S_proj_prime,
    "Q11": S_misread,
    "Q12": ratio_cap,
    "Q13": excess_cap,
    "Q14": ratio_gate
}

# Perform verification
matches = 0
total = len(expected)

for cid in sorted(expected.keys()):
    val = computed[cid]
    exp_str = expected[cid]
    ok, formatted = compare(val, exp_str)
    match = "yes" if ok else "no"
    if ok:
        matches += 1
    # Ensure dollar signs are not printed in expected; they are omitted in expected strings
    print(f"CLAIM {cid}: computed={formatted} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {total - matches} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.5991 expected=0.5991 match=yes
CLAIM Q10: computed=154.33 expected=154.33 match=yes
CLAIM Q11: computed=11000 expected=11000 match=yes
CLAIM Q12: computed=73.3 expected=73.3 match=yes
CLAIM Q13: computed=72.3 expected=72.3 match=yes
CLAIM Q14: computed=122.2 expected=122.2 match=yes
CLAIM Q2: computed=1.732 expected=1.732 match=yes
CLAIM Q3: computed=1.284 expected=1.284 match=yes
CLAIM Q4: computed=9.65 expected=9.65 match=yes
CLAIM Q5: computed=11.9 expected=11.9 match=yes
CLAIM Q6a: computed=17744384 expected=17744384 match=yes
CLAIM Q6b: computed=16.922 expected=16.922 match=yes
CLAIM Q6c: computed=320.9 expected=320.9 match=yes
CLAIM Q7: computed=4.26 expected=4.26 match=yes
CLAIM Q8: computed=4.66 expected=4.66 match=yes
CLAIM Q9: computed=158.66 expected=158.66 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.5991 | 0.5991 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 154.33 | 154.33 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q11 | 11000 | 11000 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q12 | 73.3 | 73.3 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 72.3 | 72.3 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 122.2 | 122.2 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 1.732 | 1.732 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 1.284 | 1.284 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 9.65 | 9.65 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 11.9 | 11.9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6a | 17744384 | 17744384 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q6b | 16.922 | 16.922 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6c | 320.9 | 320.9 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 4.26 | 4.26 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 4.66 | 4.66 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 158.66 | 158.66 | yes | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
