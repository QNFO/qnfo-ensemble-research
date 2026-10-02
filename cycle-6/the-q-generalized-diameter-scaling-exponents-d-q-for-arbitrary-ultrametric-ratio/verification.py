import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: ln(1/alpha) = ln(137.035999)
alpha_inv = 137.035999
v = math.log(alpha_inv)
results.append(check("Q1", round(v, 7), 4.9202436))

# Q2: r_e / lambda_C
r_e = 2.817940e-15
lam_C = 3.861593e-13
v = r_e / lam_C
results.append(check("Q2", round(v, 8), 0.00729735))

# Q3: D2^alpha
ln_a = 4.9202436
ln2 = 0.6931472
v = ln_a / ln2
results.append(check("Q3", round(v, 5), 7.09841))

# Q4: D3^alpha
ln3 = 1.0986123
v = ln_a / ln3
results.append(check("Q4", round(v, 5), 4.47860))

# Q5: D10^alpha
ln10 = 2.3025851
v = ln_a / ln10
results.append(check("Q5", round(v, 5), 2.13683))

# Q6: D_phi^alpha
lnphi = 0.4812118
v = ln_a / lnphi
results.append(check("Q6", round(v, 5), 10.22469))

# Q7: D_{alpha^-1}^alpha = 1 exactly
v = ln_a / math.log(alpha_inv)
results.append(check("Q7", round(v, 10), 1.0))

# Q8: base covariance D_q^alpha * ln q = 4.92024 for q in {2, 10, phi}
D2 = ln_a / ln2
D10 = ln_a / ln10
Dphi = ln_a / lnphi
p2 = D2 * ln2
p10 = D10 * ln10
pphi = Dphi * lnphi
ok = (math.isclose(p2, 4.92024, rel_tol=1e-6)
      and math.isclose(p10, 4.92024, rel_tol=1e-6)
      and math.isclose(pphi, 4.92024, rel_tol=1e-6))
print(f"CLAIM Q8: computed=({round(p2,5)}, {round(p10,5)}, {round(pphi,5)}) expected=4.92024 match={'yes' if ok else 'no'}")
results.append(ok)

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
