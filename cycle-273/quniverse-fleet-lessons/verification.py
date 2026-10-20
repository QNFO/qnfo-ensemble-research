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
