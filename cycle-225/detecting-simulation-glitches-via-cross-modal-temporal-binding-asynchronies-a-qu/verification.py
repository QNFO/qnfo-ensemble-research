import math

def round_sig(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Q1
p0 = 0.5077
delta_margin = 0.025
z = 1.96
N = p0 * (1 - p0) / ((delta_margin / z) ** 2)
N_ceil = math.ceil(N)
expected_Q1 = 1536
match_Q1 = "yes" if N_ceil == expected_Q1 else "no"
print(f"CLAIM Q1: computed={N_ceil} expected={expected_Q1} match={match_Q1}")

# Q2
f2 = 60.0  # Hz
Delta2 = 1000.0 / f2  # ms
sigma_q2 = math.sqrt(Delta2 ** 2 / 12.0)
sigma_q2_rounded = round_sig(sigma_q2, 4)  # 4 significant digits
expected_Q2 = 4.811
match_Q2 = "yes" if abs(sigma_q2_rounded - expected_Q2) < 1e-3 else "no"
print(f"CLAIM Q2: computed={sigma_q2_rounded} expected={expected_Q2} match={match_Q2}")

# Q3
f3 = 120.0  # Hz
Delta3 = 1000.0 / f3  # ms
sigma_q3 = math.sqrt(Delta3 ** 2 / 12.0)
sigma_q3_rounded = round_sig(sigma_q3, 4)
expected_Q3 = 2.406
match_Q3 = "yes" if abs(sigma_q3_rounded - expected_Q3) < 1e-3 else "no"
print(f"CLAIM Q3: computed={sigma_q3_rounded} expected={expected_Q3} match={match_Q3}")

# Q4
sigma_bio = 50.0  # ms
sigma_tot_60 = math.sqrt(sigma_bio ** 2 + sigma_q2 ** 2)
sigma_tot_60_rounded = round_sig(sigma_tot_60, 5)  # 5 sig figs
expected_Q4 = 50.231
match_Q4 = "yes" if abs(sigma_tot_60_rounded - expected_Q4) < 1e-3 else "no"
print(f"CLAIM Q4: computed={sigma_tot_60_rounded} expected={expected_Q4} match={match_Q4}")

# Q5
sigma_tot_120 = math.sqrt(sigma_bio ** 2 + sigma_q3 ** 2)
sigma_tot_120_rounded = round_sig(sigma_tot_120, 5)
expected_Q5 = 50.058
match_Q5 = "yes" if abs(sigma_tot_120_rounded - expected_Q5) < 1e-3 else "no"
print(f"CLAIM Q5: computed={sigma_tot_120_rounded} expected={expected_Q5} match={match_Q5}")

# Q6
D = 0.057
critical_constant = 1.36
n_ks = (critical_constant / D) ** 2
n_ks_rounded = round(n_ks)  # nearest integer
expected_Q6 = "566-570"
match_Q6 = "yes" if 566 <= n_ks_rounded <= 570 else "no"
print(f"CLAIM Q6: computed={n_ks_rounded} expected={expected_Q6} match={match_Q6}")

# Q7
sigma_tot = sigma_tot_60  # use 60 Hz case as in paper
delta = 10.0  # ms
z_alpha = 1.96
z_power = 0.842
n_mean = ((z_alpha + z_power) ** 2 * 2 * sigma_tot ** 2) / (delta ** 2)
n_mean_ceil = math.ceil(n_mean)
expected_Q7 = 397
match_Q7 = "yes" if n_mean_ceil == expected_Q7 else "no"
print(f"CLAIM Q7: computed={n_mean_ceil} expected={expected_Q7} match={match_Q7}")

# Q8
effect = math.log(1.21)  # ln(1.21)
n_var = 1 + 2 * ((z_alpha + z_power) / effect) ** 2
n_var_rounded = round(n_var)
expected_Q8 = 433
match_Q8 = "yes" if n_var_rounded == expected_Q8 else "no"
print(f"CLAIM Q8: computed={n_var_rounded} expected={expected_Q8} match={match_Q8}")

# Q9
EEG_system = 30000
monitor = 2000
participants = 8
comp_per = 20
C_total = EEG_system + monitor + participants * comp_per
expected_Q9 = 32160
match_Q9 = "yes" if C_total == expected_Q9 else "no"
print(f"CLAIM Q9: computed={C_total} expected={expected_Q9} match={match_Q9}")

# Q10
sigma_tot = sigma_tot_60  # ms
n_trials = 200
z_val = 1.96
half_width = z_val * sigma_tot / math.sqrt(n_trials)
half_width_rounded = round_sig(half_width, 2)  # two significant digits as in 6.9
expected_Q10 = 6.9
match_Q10 = "yes" if abs(half_width_rounded - expected_Q10) < 0.05 else "no"
print(f"CLAIM Q10: computed={half_width_rounded} expected={expected_Q10} match={match_Q10}")

print(f"VERIFICATION SUMMARY: 10 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10].count('yes'))} match, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10].count('no'))} mismatch")
