import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    digits = sig - int(math.floor(math.log10(abs(x)))) - 1
    return round(x, digits)

# Q1
N_schism = 29
maps = N_schism * (N_schism - 1) // 2
expected_Q1 = "406"
computed_Q1 = maps
match_Q1 = "yes" if round_sig(computed_Q1, len(expected_Q1)) == int(expected_Q1) else "no"
print(f"CLAIM Q1: computed={computed_Q1} expected={expected_Q1} match={match_Q1}")

# Q2
constraints = N_schism * (N_schism - 1) * (N_schism - 2) // 6
expected_Q2 = "3654"
computed_Q2 = constraints
match_Q2 = "yes" if round_sig(computed_Q2, len(expected_Q2)) == int(expected_Q2) else "no"
print(f"CLAIM Q2: computed={computed_Q2} expected={expected_Q2} match={match_Q2}")

# Q3
ratio = constraints / maps
expected_Q3 = "9.0"
computed_Q3 = ratio
match_Q3 = "yes" if round_sig(computed_Q3, len(expected_Q3.replace(".", ""))) == float(expected_Q3) else "no"
print(f"CLAIM Q3: computed={computed_Q3} expected={expected_Q3} match={match_Q3}")

# Q4 (ratio for N=58)
N = 58
pairs_N = N * (N - 1) // 2
triples_N = N * (N - 1) * (N - 2) // 6
ratio_N = triples_N / pairs_N
expected_Q4 = "18.667"
computed_Q4 = ratio_N
match_Q4 = "yes" if round_sig(computed_Q4, len(expected_Q4.replace(".", ""))) == float(expected_Q4) else "no"
print(f"CLAIM Q4: computed={computed_Q4} expected={expected_Q4} match={match_Q4}")

# Q5
n = 7
pairs_n = n * (n - 1) // 2
expected_Q5 = "21"
computed_Q5 = pairs_n
match_Q5 = "yes" if round_sig(computed_Q5, len(expected_Q5)) == int(expected_Q5) else "no"
print(f"CLAIM Q5: computed={computed_Q5} expected={expected_Q5} match={match_Q5}")

# Q6
unassigned = N_schism - pairs_n
expected_Q6 = "8"
computed_Q6 = unassigned
match_Q6 = "yes" if round_sig(computed_Q6, len(expected_Q6)) == int(expected_Q6) else "no"
print(f"CLAIM Q6: computed={computed_Q6} expected={expected_Q6} match={match_Q6}")

# Q7 (pair count for m=2)
m = 2
pairs_m = m * (m - 1) // 2
expected_Q7 = "1"
computed_Q7 = pairs_m
match_Q7 = "yes" if round_sig(computed_Q7, len(expected_Q7)) == int(expected_Q7) else "no"
print(f"CLAIM Q7: computed={computed_Q7} expected={expected_Q7} match={match_Q7}")

# Q8 (closure error)
e12 = 1e-3
e23 = 2e-3
e31 = 5e-4
closure = 1 - (1 - e12) * (1 - e23) * (1 - e31)
expected_Q8 = "3.4965e-3"
computed_Q8 = closure
match_Q8 = "yes" if round_sig(computed_Q8, 5) == float(expected_Q8) else "no"
print(f"CLAIM Q8: computed={computed_Q8} expected={expected_Q8} match={match_Q8}")

# Q9 (max chain length)
tau = 1e-3
eps_min = 1e-2
k_max = math.log(1 - tau) / math.log(1 - eps_min)
expected_Q9 = "0.0995"
computed_Q9 = k_max
match_Q9 = "yes" if round_sig(computed_Q9, 4) == float(expected_Q9) else "no"
print(f"CLAIM Q9: computed={computed_Q9} expected={expected_Q9} match={match_Q9}")

# Q10 (master success probability)
p = 0.9
constraints = 3654
P_master = p ** constraints
expected_Q10 = "6.34e-168"
computed_Q10 = P_master
match_Q10 = "yes" if round_sig(computed_Q10, 3) == float(expected_Q10) else "no"
print(f"CLAIM Q10: computed={computed_Q10} expected={expected_Q10} match={match_Q10}")

# Q11 (max n for threshold)
threshold = 0.01
# solve for max n such that 0.9**C(n,3) >= 0.01
max_n = 0
for candidate in range(1, 20):
    if p ** (candidate * (candidate - 1) * (candidate - 2) // 6) >= threshold:
        max_n = candidate
expected_Q11 = "7"
computed_Q11 = max_n
match_Q11 = "yes" if str(computed_Q11) == expected_Q11 else "no"
print(f"CLAIM Q11: computed={computed_Q11} expected={expected_Q11} match={match_Q11}")

# Q12 (abstract energy-window factor)
E_max_abs = 1.0  # TeV
E_min_abs = 0.5  # TeV
factor_abs = E_max_abs / E_min_abs
expected_Q12 = "2"
computed_Q12 = factor_abs
match_Q12 = "yes" if round_sig(computed_Q12, 1) == int(expected_Q12) else "no"
print(f"CLAIM Q12: computed={computed_Q12} expected={expected_Q12} match={match_Q12}")

# Q13 (preface energy-window factor)
E_max_pref = 1.5
E_min_pref = 0.5
factor_pref = E_max_pref / E_min_pref
expected_Q13 = "3"
computed_Q13 = factor_pref
match_Q13 = "yes" if round_sig(computed_Q13, 1) == int(expected_Q13) else "no"
print(f"CLAIM Q13: computed={computed_Q13} expected={expected_Q13} match={match_Q13}")

# Q14 (mean schisms per domain)
mean_schisms = N_schism / n
expected_Q14 = "4.14"
computed_Q14 = mean_schisms
match_Q14 = "yes" if round_sig(computed_Q14, 3) == float(expected_Q14) else "no"
print(f"CLAIM Q14: computed={computed_Q14} expected={expected_Q14} match={match_Q14}")

# Q15 (mediated translation error)
eps = 1e-2
delta_mediated = 1 - (1 - eps) ** 2
expected_Q15 = "0.0199"
computed_Q15 = delta_mediated
match_Q15 = "yes" if round_sig(computed_Q15, 3) == float(expected_Q15) else "no"
print(f"CLAIM Q15: computed={computed_Q15} expected={expected_Q15} match={match_Q15}")

# Q16 (scaled closure bound)
f = 0.5
closure_scaled = 1 - (1 - f * e12) * (1 - f * e23) * (1 - f * e31)
expected_Q16 = "1.7491e-3"
computed_Q16 = closure_scaled
match_Q16 = "yes" if round_sig(computed_Q16, 5) == float(expected_Q16) else "no"
print(f"CLAIM Q16: computed={computed_Q16} expected={expected_Q16} match={match_Q16}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for m in [match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10,match_Q11,match_Q12,match_Q13,match_Q14,match_Q15,match_Q16] if m=='yes')} match, {sum(1 for m in [match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10,match_Q11,match_Q12,match_Q13,match_Q14,match_Q15,match_Q16] if m=='no')} mismatch")
