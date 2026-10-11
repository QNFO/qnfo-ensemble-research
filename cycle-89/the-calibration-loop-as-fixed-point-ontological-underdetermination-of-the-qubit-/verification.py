import math

f_ro = 0.99991
N_trials = 1_000_000
f_ad = 0.99999
e0 = 0.1
contraction = 0.5
threshold = 9e-5
c2 = 0.01

# Q1
eps_ro = 1 - f_ro
print(f"CLAIM Q1: computed={eps_ro} expected=9e-05 match={math.isclose(eps_ro, 9e-5, rel_tol=1e-6)}")

# Q2
mu = N_trials * eps_ro
print(f"CLAIM Q2: computed={mu} expected=90 match={math.isclose(mu, 90, rel_tol=1e-6)}")

# Q3
sigma_f = math.sqrt(f_ro * (1 - f_ro) / N_trials)
print(f"CLAIM Q3: computed={sigma_f} expected=9.49e-06 match={math.isclose(sigma_f, 9.49e-6, rel_tol=1e-2)}")

# Q4
eps_ad = 1 - f_ad
print(f"CLAIM Q4: computed={eps_ad} expected=1e-05 match={math.isclose(eps_ad, 1e-5, rel_tol=1e-6)}")

# Q5
ratio = eps_ad / eps_ro
print(f"CLAIM Q5: computed={ratio} expected=0.1111111111111111 match={math.isclose(ratio, 1/9, rel_tol=1e-6)}")

# Q6
k = 0
while e0 * contraction**k > threshold:
    k += 1
k_min = k
print(f"CLAIM Q6: computed={k_min} expected=11 match={k_min == 11}")

# Q7
e_k = e0 * contraction**11
print(f"CLAIM Q7: computed={e_k} expected=4.8828125e-05 match={math.isclose(e_k, 4.8828125e-5, rel_tol=1e-6)}")

# Q8
D_TV = c2
print(f"CLAIM Q8: computed={D_TV} expected=0.01 match={math.isclose(D_TV, 0.01, rel_tol=1e-6)}")

results = [
    math.isclose(eps_ro, 9e-5, rel_tol=1e-6),
    math.isclose(mu, 90, rel_tol=1e-6),
    math.isclose(sigma_f, 9.49e-6, rel_tol=1e-2),
    math.isclose(eps_ad, 1e-5, rel_tol=1e-6),
    math.isclose(ratio, 1/9, rel_tol=1e-6),
    k_min == 11,
    math.isclose(e_k, 4.8828125e-5, rel_tol=1e-6),
    math.isclose(D_TV, 0.01, rel_tol=1e-6),
]
print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(results)} match, {len(results)-sum(results)} mismatch")
