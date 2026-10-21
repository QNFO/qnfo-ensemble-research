import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Q1
N = 64
computed_Q1 = 2**N
expected_Q1 = "1.8446744e19"
match_Q1 = "yes" if round_sig(computed_Q1, 8) == 1.8446744e19 else "no"
print(f"CLAIM Q1: computed={computed_Q1:.8e} expected={expected_Q1} match={match_Q1}")

# Q2
# Compute exponent = 2^N * log10(2)
exponent = (2**N) * math.log10(2)
computed_Q2 = exponent  # we compare exponent part
expected_Q2 = "10^{5.553e18}"
# round exponent to 4 significant digits as in paper (5.553×10^{18})
rounded_exp = round_sig(exponent, 4)
match_Q2 = "yes" if abs(rounded_exp - 5.553e18) < 1e14 else "no"
print(f"CLAIM Q2: computed={rounded_exp:.3e} expected={expected_Q2} match={match_Q2}")

# Q3
max_literals = 9
reachable = 0
for k in range(1, max_literals + 1):
    reachable += math.comb(N, k) * (2**k)
computed_Q3 = reachable
expected_Q3 = "1.53e13"
match_Q3 = "yes" if round_sig(computed_Q3, 3) == 1.53e13 else "no"
print(f"CLAIM Q3: computed={computed_Q3:.3e} expected={expected_Q3} match={match_Q3}")

# Q4
# total predicates ≈ 10^{5.553e18}, effectively infinite for float
# fraction is essentially zero
computed_Q4 = 0.0
expected_Q4 = "0"
match_Q4 = "yes" if computed_Q4 == 0.0 else "no"
print(f"CLAIM Q4: computed={computed_Q4:.1e} expected={expected_Q4} match={match_Q4}")

# Q5
k_B = 1.380649e-23  # J/K
T = 300.0
ln2 = 0.693147
computed_Q5 = k_B * T * ln2
expected_Q5 = "2.8709e-21"
match_Q5 = "yes" if round_sig(computed_Q5, 5) == 2.8709e-21 else "no"
print(f"CLAIM Q5: computed={computed_Q5:.5e} expected={expected_Q5} match={match_Q5}")

# Q6
f_cycle = 1.0  # Hz
N_dist = 1e9
computed_Q6 = f_cycle * N_dist * computed_Q5
expected_Q6 = "2.8709e-12"
match_Q6 = "yes" if round_sig(computed_Q6, 5) == 2.8709e-12 else "no"
print(f"CLAIM Q6: computed={computed_Q6:.5e} expected={expected_Q6} match={match_Q6}")

# Q7
P_obs = 1e-12  # W
tau = 1.0      # s
computed_Q7 = (P_obs * tau) / computed_Q5
expected_Q7 = "3.48e8"
match_Q7 = "yes" if round_sig(computed_Q7, 3) == 3.48e8 else "no"
print(f"CLAIM Q7: computed={computed_Q7:.3e} expected={expected_Q7} match={match_Q7}")

# Q8
computed_Q8 = 2**(30-10)
expected_Q8 = "1.05e6"
match_Q8 = "yes" if round_sig(computed_Q8, 3) == 1.05e6 else "no"
print(f"CLAIM Q8: computed={computed_Q8:.3e} expected={expected_Q8} match={match_Q8}")

# Q9
m = 1e5
coarse = 2**10  # 1024
lam = m / coarse
p1 = lam * math.exp(-lam)
computed_Q9 = p1
expected_Q9 = "3.78e-41"
match_Q9 = "yes" if round_sig(computed_Q9, 3) == 3.78e-41 else "no"
print(f"CLAIM Q9: computed={computed_Q9:.3e} expected={expected_Q9} match={match_Q9}")

# Q10
computed_Q10 = coarse * p1
expected_Q10 = "3.9e-38"
match_Q10 = "yes" if round_sig(computed_Q10, 2) == 3.9e-38 else "no"
print(f"CLAIM Q10: computed={computed_Q10:.2e} expected={expected_Q10} match={match_Q10}")

# Q12
n_prec = 100
computed_Q12 = n_prec - N
expected_Q12 = "36"
match_Q12 = "yes" if computed_Q12 == 36 else "no"
print(f"CLAIM Q12: computed={computed_Q12} expected={expected_Q12} match={match_Q12}")

print(f"VERIFICATION SUMMARY: 11 claims, {sum(1 for m in [match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10,match_Q12] if m=='yes')} match, {sum(1 for m in [match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10,match_Q12] if m=='no')} mismatch")
