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
