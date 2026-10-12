import math

def sig(x, n=8):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: N_def(3) = 2^((4^4-4)/3) = 2^84
Nd3 = 2 ** ((4 ** (3 + 1) - 4) // 3)
computed = Nd3
expected = "1.93e25"
comp_sig = sig(computed, 3)
match = "yes" if abs(comp_sig - 1.93e25) / 1.93e25 < 0.005 else "no"
results.append(("Q1", computed, expected, match))

# Q2: N_def(2) = 2^20
Nd2 = 2 ** ((4 ** 3 - 4) // 3)
computed = Nd2
expected = "1048576"
match = "yes" if computed == 1048576 else "no"
results.append(("Q2", computed, expected, match))

# Q3: N_def(4) = 2^340
Nd4 = 2.0 ** ((4 ** 5 - 4) // 3)
computed = Nd4
expected = "2.24e102"
comp_sig = sig(computed, 3)
match = "yes" if abs(comp_sig - 2.24e102) / 2.24e102 < 0.005 else "no"
results.append(("Q3", computed, expected, match))

# Q4: n_3 = 4^3
computed = 4 ** 3
expected = "64"
match = "yes" if computed == 64 else "no"
results.append(("Q4", computed, expected, match))

# Q5: d_3 = 2^3
computed = 2 ** 3
expected = "8"
match = "yes" if computed == 8 else "no"
results.append(("Q5", computed, expected, match))

# Q6: r_3 = 4^-3
computed = 4.0 ** (-3)
expected = "0.015625"
match = "yes" if computed == 0.015625 else "no"
results.append(("Q6", computed, expected, match))

# Q7: p_tot at L=2, alpha=6, p0=1e-3, eta=10
alpha, p0, eta, L = 6.0, 1e-3, 10.0, 2
pX = alpha ** (2 ** L - 1) * p0 ** (2 ** L)
pZ = alpha ** (2 ** L - 1) * (eta * p0) ** (2 ** L)
computed = pX + pZ
expected = "2.160216e-6"
match = "yes" if abs(computed - 2.160216e-6) < 1e-15 else "no"
results.append(("Q7", computed, expected, match))

# Q8: Z share at L=2
computed = pZ / (pX + pZ)
expected = "0.9999 (share > 99.99%)"
match = "yes" if computed > 0.9999 else "no"
results.append(("Q8", computed, expected, match))

# Q9: skew ratios eta^(2^L) at L=1,2,3
for L in (1, 2, 3):
    computed = eta ** (2 ** L)
    expected = {1: "100", 2: "10000", 3: "100000000"}[L]
    match = "yes" if computed == float(expected) else "no"
    results.append((f"Q9(L={L})", computed, expected, match))

# Q10: G(3) = 16*(4^3-1)/3
computed = 16 * (4 ** 3 - 1) // 3
expected = "336"
match = "yes" if computed == 336 else "no"
results.append(("Q10", computed, expected, match))

# Q11: reduction factor 2^84/336
computed = Nd3 / 336.0
expected = "5.7568e22"
comp_sig = sig(computed, 5)
match = "yes" if abs(comp_sig - 5.7568e22) / 5.7568e22 < 0.00005 else "no"
results.append(("Q11", computed, expected, match))

# Q12: sweep time at L=2, R=1e6
R = 1e6
computed = Nd2 / R
expected = "1.05"
comp_sig = sig(computed, 3)
match = "yes" if abs(comp_sig - 1.05) < 0.005 else "no"
results.append(("Q12", computed, expected, match))

# Q13: sweep time at L=3 in seconds and years
computed_s = Nd3 / R
year = 3.156e7
computed_y = computed_s / year
expected = "6.13e11"
comp_sig = sig(computed_y, 3)
match = "yes" if abs(comp_sig - 6.13e11) / 6.13e11 < 0.005 else "no"
results.append(("Q13", computed_y, expected, match))

# Q14: N_def(3)/N_def(2) = 2^64
computed = Nd3 / Nd2
expected = "1.8e19"
comp_sig = sig(computed, 2)
match = "yes" if abs(comp_sig - 1.8e19) / 1.8e19 < 0.05 else "no"
results.append(("Q14", computed, expected, match))

# Q15: p_tot at L=3
L = 3
pZ3 = alpha ** (2 ** L - 1) * (eta * p0) ** (2 ** L)
pX3 = alpha ** (2 ** L - 1) * p0 ** (2 ** L)
computed = pX3 + pZ3
expected = "2.79936e-11"
match = "yes" if abs(computed - 2.79936e-11) < 1e-20 else "no"
results.append(("Q15", computed, expected, match))

n_match = 0
for cid, computed, expected, match in results:
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected} match={match}")
    if match == "yes":
        n_match += 1
print(f"VERIFICATION SUMMARY: {len(results)} claims, {n_match} match, {len(results) - n_match} mismatch")
