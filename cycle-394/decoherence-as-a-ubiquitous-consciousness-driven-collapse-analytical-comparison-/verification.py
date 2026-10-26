import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Q1
m = 1.66e-23  # kg
kB = 1.38e-23  # J/K
T = 300.0  # K
hbar = 1.055e-34  # J·s
dx = 1e-9  # m
Gamma_env = (2 * m * kB * T / hbar**2) * dx**2
Gamma_env_rounded = round_sig(Gamma_env, 2)  # 2 sig figs as in "1.2×10^7"
expected_Q1 = "1.2e7"
match_Q1 = "yes" if f"{Gamma_env_rounded:.1e}" == expected_Q1 else "no"
print(f"CLAIM Q1: computed={Gamma_env_rounded:.1e} expected={expected_Q1} match={match_Q1}")

# Q2
alpha = 1e-13  # s^-1 bit^-1
I = 1e6  # bits
Gamma_c = alpha * I
Gamma_c_rounded = round_sig(Gamma_c, 2)  # 2 sig figs as in "1.0×10^-7"
expected_Q2 = "1.0e-7"
match_Q2 = "yes" if f"{Gamma_c_rounded:.1e}" == expected_Q2 else "no"
print(f"CLAIM Q2: computed={Gamma_c_rounded:.1e} expected={expected_Q2} match={match_Q2}")

# Q3
Gamma_tot = Gamma_env + Gamma_c
Gamma_tot_rounded = round_sig(Gamma_tot, 2)  # 2 sig figs as in "1.2×10^7"
expected_Q3 = "1.2e7"
match_Q3 = "yes" if f"{Gamma_tot_rounded:.1e}" == expected_Q3 else "no"
print(f"CLAIM Q3: computed={Gamma_tot_rounded:.1e} expected={expected_Q3} match={match_Q3}")

# Q4
Gamma_c_max = 1e-5  # s^-1
I_min = 1.0  # bit (>=1)
alpha_bound = Gamma_c_max / I_min
alpha_bound_rounded = round_sig(alpha_bound, 1)  # 1 sig fig as in "1×10^-5"
expected_Q4 = "1e-5"
match_Q4 = "yes" if f"{alpha_bound_rounded:.0e}" == expected_Q4 else "no"
print(f"CLAIM Q4: computed={alpha_bound_rounded:.0e} expected={expected_Q4} match={match_Q4}")

# Q5
Gamma_tot_approx = 1.235e7  # s^-1 (from paper)
tau_coh = 1.0 / Gamma_tot_approx
tau_coh_rounded = round_sig(tau_coh, 2)  # 2 sig figs as in "8.1×10^-8"
expected_Q5 = "8.1e-8"
match_Q5 = "yes" if f"{tau_coh_rounded:.1e}" == expected_Q5 else "no"
print(f"CLAIM Q5: computed={tau_coh_rounded:.1e} expected={expected_Q5} match={match_Q5}")

# Q6
alpha_high = 1e-5  # s^-1 bit^-1
Gamma_c_high = alpha_high * I
Gamma_c_high_rounded = round_sig(Gamma_c_high, 1)  # 1 sig fig as in "10"
expected_Q6 = "10"
match_Q6 = "yes" if f"{Gamma_c_high_rounded:.0f}" == expected_Q6 else "no"
print(f"CLAIM Q6: computed={Gamma_c_high_rounded:.0f} expected={expected_Q6} match={match_Q6}")

# Q7
Gamma_env_original = 1.235e7  # s^-1 at 300 K
T_original = 300.0
T_new = 1.0
Gamma_env_new = Gamma_env_original * (T_new / T_original)
Gamma_env_new_rounded = round_sig(Gamma_env_new, 2)  # 2 sig figs as in "4.1×10^4"
expected_Q7 = "4.1e4"
match_Q7 = "yes" if f"{Gamma_env_new_rounded:.1e}" == expected_Q7 else "no"
print(f"CLAIM Q7: computed={Gamma_env_new_rounded:.1e} expected={expected_Q7} match={match_Q7}")

print(f"VERIFICATION SUMMARY: 7 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7].count('yes'))} match, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7].count('no'))} mismatch")
