import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: Lambda = 2*lambda_L^2/d
lam = 1.0e-7
d = 5.0e-8
Lam = 2 * lam**2 / d
results.append(("Q1", Lam, "400e-9", 2))

# Q2: Gamma = Lambda/R
Lam_c = 2 * lam**2 / d
R = 1.0e-6
Gam = Lam_c / R
results.append(("Q2", Gam, "0.40", 2))

# Q3: H0 = Phi0/(pi R^2)
Phi0 = 2.07e-15
R1 = 1.0e-6
H0 = Phi0 / (math.pi * R1**2)
results.append(("Q3", H0, "6.589e-4", 4))

# Q4: H0(10um) = H0(1um)*1e-2
H0_10 = Phi0 / (math.pi * (10.0e-6)**2)
results.append(("Q4", H0_10, "6.589e-6", 4))

# Q5: b/R = (mu0Ha/B*)^(1/3), b = 62.996 um
mu0Ha = 0.025
Bstar = 0.100
gamma = 1
Rd = 100.0e-6
b5 = Rd * (mu0Ha / Bstar)**(1.0 / (gamma + 2))
results.append(("Q5", b5 * 1e6, "62.996", 5))

# Q6: b at 0.050 T
mu0Ha6 = 0.050
b6 = Rd * (mu0Ha6 / Bstar)**(1.0 / (gamma + 2))
results.append(("Q6", b6 * 1e6, "79.370", 5))

# Q7: B_d = B*(b/R)
bR5 = (mu0Ha / Bstar)**(1.0 / (gamma + 2))
Bd = Bstar * bR5
results.append(("Q7", Bd, "0.062996", 6))

# Q8: N = mu0Ha*pi*R^2/Phi0
N8 = mu0Ha * math.pi * Rd**2 / Phi0
results.append(("Q8", N8, "3.7942e5", 5))

# Q9: N at 0.050 T = 2*N(0.025)
N9 = 2 * (0.025 * math.pi * Rd**2 / Phi0)
results.append(("Q9", N9, "7.588e5", 4))

# Q10: N at 0.100 T = 4*N(0.025)
N10 = 4 * (0.025 * math.pi * Rd**2 / Phi0)
results.append(("Q10", N10, "1.518e6", 4))

# Q11: f0 = f1 - f2
f1 = 5.00e9
f2 = 4.99e9
f0 = f1 - f2
results.append(("Q11", f0, "10.0e6", 3))

# Q12: omega*tau = 2*pi*fq*tau
fq = 5.0e9
tau = 1.0e-4
wt = 2 * math.pi * fq * tau
results.append(("Q12", wt, "3.1416e6", 5))

# Q13: kappa_eff/kappa_c at eta=0.05
kRatio = 100.0
eta13 = 0.05
ps13 = 1.0 / (1.0 + eta13)
k13 = ps13 * kRatio + (1 - ps13)
results.append(("Q13", k13, "95.286", 5))

# Q14: at eta=0.20
eta14 = 0.20
ps14 = 1.0 / (1.0 + eta14)
k14 = ps14 * kRatio + (1 - ps14)
results.append(("Q14", k14, "83.500", 5))

# Q15: unconfined reference
k15 = 0.5 * kRatio + 0.5
results.append(("Q15", k15, "50.5", 3))

# Q16: ratio = k13/k15
ratio16 = k13 / k15
results.append(("Q16", ratio16, "1.887", 4))

mismatch = 0
for cid, comp, exp_str, nsig in results:
    exp = float(exp_str)
    comp_r = sig(comp, nsig)
    match = "yes" if abs(comp_r - exp) <= abs(exp) * 10**(-nsig + 1) * 1.01 else "no"
    if match == "no":
        mismatch += 1
    print(f"CLAIM {cid}: computed={comp:.8g} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results)-mismatch} match, {mismatch} mismatch")
