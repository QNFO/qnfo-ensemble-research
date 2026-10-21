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
