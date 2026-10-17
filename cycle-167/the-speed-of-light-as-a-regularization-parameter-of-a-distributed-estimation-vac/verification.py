import math

def sig(x, n):
    if x == 0:
        return 0.0
    from math import floor, log10
    d = n - 1 - floor(log10(abs(x)))
    return round(x, d)

results = []

# Q1: omega_max = 2*v/a
v = 2.998e8
a = 1.616e-35
omega_max = 2 * v / a
results.append(("Q1", omega_max, "3.710e43"))

# Q2: B = omega_max/(2*pi)
B = omega_max / (2 * math.pi)
results.append(("Q2", B, "5.905e42"))

# Q3: S(10 wc) = 1/(1+10^2)
S10 = 1 / (1 + 10**2)
results.append(("Q3", S10, "9.901e-3"))

# Q4: S(100 wc) = 1/(1+100^2)
S100 = 1 / (1 + 100**2)
results.append(("Q4", S100, "9.999e-5"))

# Q5: ratio = S10/S100
ratio = S10 / S100
results.append(("Q5", ratio, "99.02"))

# Q6: tau_0 = L/v
L = 1.0
tau0 = L / v
results.append(("Q6", tau0, "3.336e-9"))

# Q7: tau = tau0*(1+rho/rho_c)
rho = 1e-3
tau = tau0 * (1 + rho)
results.append(("Q7", tau, "3.339e-9"))

# Q8: Delta_tau = tau0 * rho
dtau = tau0 * rho
results.append(("Q8", dtau, "3.336e-12"))

# Q9: f_c = c/(2*pi*L)
c = 3.00e8
Ld = 1.0e-3
fc = c / (2 * math.pi * Ld)
results.append(("Q9", fc, "4.775e10"))

# Q10: E_c = h*f_c
h = 6.626e-34
Ec = h * fc
results.append(("Q10", Ec, "3.164e-23"))

# Q11: E_c in eV
eV = 1.602e-19
Ec_eV = Ec / eV
results.append(("Q11", Ec_eV, "1.975e-4"))

match_count = 0
for cid, computed, expected_str in results:
    expected = float(expected_str)
    # number of significant digits in the paper's stated value
    digits = len(expected_str.split("e")[0].replace(".", "").lstrip("0"))
    comp_rounded = sig(computed, digits)
    match = "yes" if abs(comp_rounded - expected) <= expected * 10**(-(digits)) / 2 or comp_rounded == expected else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={computed:.8e} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results)-match_count} mismatch")
