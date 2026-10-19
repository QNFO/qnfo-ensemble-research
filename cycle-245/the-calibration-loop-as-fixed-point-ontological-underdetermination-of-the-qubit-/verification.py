import math

# Inputs from the paper
f_ro = 0.99991          # readout fidelity
N_trials = 10**6        # number of trials
f_ad = 0.99999          # adaptive measurement fidelity
e0 = 0.1                # initial calibration error
contraction = 0.5       # |1 - g*s|
c_sq = 0.01             # leakage probability |c|^2
Omega_over_Delta = 0.1  # weak-drive ratio
N_tom = 10**4           # tomographic shots per element
delta_p = 0.01          # probability difference to resolve

# Q1
eps_ro = 1 - f_ro
exp1 = "9×10⁻⁵"
match1 = "yes" if abs(eps_ro - 9e-5) < 1e-12 else "no"
print(f"CLAIM Q1: computed={eps_ro:.8g} expected={exp1} match={match1}")

# Q2
mu = N_trials * eps_ro
exp2 = "90"
match2 = "yes" if mu == 90 else "no"
print(f"CLAIM Q2: computed={mu:.8g} expected={exp2} match={match2}")

# Q3
sigma_f = math.sqrt(f_ro * (1 - f_ro) / N_trials)
exp3 = "9.4864061×10⁻⁶"
# round to 8 significant digits for comparison
sigma_f_rounded = round(sigma_f, 13)  # enough to capture 8 sig figs
match3 = "yes" if abs(sigma_f_rounded - 9.4864061e-6) < 1e-13 else "no"
print(f"CLAIM Q3: computed={sigma_f:.10g} expected={exp3} match={match3}")

# Q4
eps_ad = 1 - f_ad
exp4 = "1×10⁻⁵"
match4 = "yes" if abs(eps_ad - 1e-5) < 1e-12 else "no"
print(f"CLAIM Q4: computed={eps_ad:.8g} expected={exp4} match={match4}")

# Q5
ratio = eps_ad / eps_ro
exp5 = "0.11111"
# round ratio to 5 decimal places as in the paper
ratio_rounded = round(ratio, 5)
match5 = "yes" if abs(ratio_rounded - 0.11111) < 1e-10 else "no"
print(f"CLAIM Q5: computed={ratio_rounded:.5f} expected={exp5} match={match5}")

# Q6 (formula only, no numeric expected)
exp6 = "none"
print(f"CLAIM Q6: computed=0.1*0.5**k (formula) expected={exp6} match=none")

# Q7
e11 = e0 * (contraction ** 11)
exp7 = "4.8828125×10⁻⁵"
match7 = "yes" if abs(e11 - 4.8828125e-5) < 1e-12 else "no"
print(f"CLAIM Q7: computed={e11:.10g} expected={exp7} match={match7}")

# Q8
# find smallest integer k such that e0 * contraction**k <= eps_ro
k = 0
while e0 * (contraction ** k) > eps_ro:
    k += 1
exp8 = "11"
match8 = "yes" if k == 11 else "no"
print(f"CLAIM Q8: computed={k} expected={exp8} match={match8}")

# Q9
D_TV_subspace = 0.0
exp9 = "0"
match9 = "yes" if D_TV_subspace == 0 else "no"
print(f"CLAIM Q9: computed={D_TV_subspace:.1f} expected={exp9} match={match9}")

# Q10
D_TV_leak = c_sq
exp10 = "0.01"
match10 = "yes" if abs(D_TV_leak - 0.01) < 1e-12 else "no"
print(f"CLAIM Q10: computed={D_TV_leak:.2f} expected={exp10} match={match10}")

# Q11
N_min_1sigma = 1 / (4 * delta_p ** 2)
exp11 = "2500"
match11 = "yes" if abs(N_min_1sigma - 2500) < 1e-9 else "no"
print(f"CLAIM Q11: computed={int(N_min_1sigma)} expected={exp11} match={match11}")

# Q12
N_min_3sigma = 9 / (4 * delta_p ** 2)
exp12 = "22500"
match12 = "yes" if abs(N_min_3sigma - 22500) < 1e-6 else "no"
print(f"CLAIM Q12: computed={int(N_min_3sigma)} expected={exp12} match={match12}")

# Q13
margin = c_sq / eps_ro
exp13 = "111"
# round to nearest integer as paper gives approx 111
margin_rounded = round(margin)
match13 = "yes" if margin_rounded == 111 else "no"
print(f"CLAIM Q13: computed={margin:.6f} expected={exp13} match={match13}")

# Q14
bound = (Omega_over_Delta / 2) ** 2
exp14 = "2.5×10⁻³"
match14 = "yes" if abs(bound - 2.5e-3) < 1e-12 else "no"
print(f"CLAIM Q14: computed={bound:.8g} expected={exp14} match={match14}")

# Q15
sigma_tom = math.sqrt(0.5 * 0.5 / N_tom)
exp15 = "5.0×10⁻³"
match15 = "yes" if abs(sigma_tom - 5.0e-3) < 1e-12 else "no"
print(f"CLAIM Q15: computed={sigma_tom:.8g} expected={exp15} match={match15}")

# Q16
target = bound  # 2.5e-3
N_needed = 0.25 / (target ** 2)
exp16 = "4.0×10⁴"
match16 = "yes" if abs(N_needed - 40000) < 1e-6 else "no"
print(f"CLAIM Q16: computed={int(N_needed)} expected={exp16} match={match16}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum([match1,match2,match3,match4,match5,match7,match8,match9,match10,match11,match12,match13,match14,match15,match16].count('yes'))} match, {sum([match1,match2,match3,match4,match5,match7,match8,match9,match10,match11,match12,match13,match14,match15,match16].count('no'))} mismatch")
