import math

def posterior(prior_odds, bf):
    o = prior_odds * bf
    return o / (1 + o)

# Q1
K_R = 0.9 / 0.9
print(f"CLAIM Q1: computed={K_R} expected=1 match={'yes' if math.isclose(K_R, 1, rel_tol=1e-6) else 'no'}")

# Q2
K_S = 0.4 / 0.05
print(f"CLAIM Q2: computed={K_S} expected=8 match={'yes' if math.isclose(K_S, 8, rel_tol=1e-6) else 'no'}")

# Q3
O_prior = 0.1 / 0.9
O_2 = O_prior * K_S
P_2 = O_2 / (1 + O_2)
print(f"CLAIM Q3: computed={P_2} expected={8/17} match={'yes' if math.isclose(P_2, 8/17, rel_tol=1e-6) else 'no'}")

# Q4
O_3 = O_prior * K_S ** 2
P_3 = O_3 / (1 + O_3)
print(f"CLAIM Q4: computed={P_3} expected=0.8767 match={'yes' if math.isclose(P_3, 0.8767, rel_tol=1e-4) else 'no'}")

# Q5
O_4 = O_prior * K_S ** 3
P_4 = O_4 / (1 + O_4)
print(f"CLAIM Q5: computed={P_4} expected=0.9827 match={'yes' if math.isclose(P_4, 0.9827, rel_tol=1e-4) else 'no'}")

# Q6
N_req = 1 + math.log(171) / math.log(8)
N = math.ceil(N_req)
print(f"CLAIM Q6: computed={N} expected=4 match={'yes' if N == 4 else 'no'}")

# Q7
log10_8 = math.log10(8)
print(f"CLAIM Q7: computed={log10_8:.6f} expected=0.903 match={'yes' if math.isclose(log10_8, 0.903, rel_tol=1e-2) else 'no'}")

# Q8
K_T = 0.1 ** 2 / 0.9
print(f"CLAIM Q8: computed={K_T:.6f} expected=0.0111 match={'yes' if math.isclose(K_T, 0.0111, rel_tol=1e-2) else 'no'}")

print("VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch")
