import math

def show(x):
    return f"{x:.10g}"

results = []

# Q6-Q9 interpolation fractions as stated in the paper
def phi_interp(z, lo, hi, phi_lo, phi_hi):
    frac = (z - lo) / (hi - lo)
    return phi_lo + frac * (phi_hi - phi_lo)

# Q1
pL = 1 - 0.8413
results.append(("Q1", pL, "0.1587"))

# Q2
pQ = 2 * (1 - 0.8413)
results.append(("Q2", pQ, "0.3174"))

# Q3
dP = pQ - pL
results.append(("Q3", dP, "0.1587"))

# Q4
ratio = pQ / pL
results.append(("Q4", ratio, "2.000"))

# Q5
sigma_n = 1.4142136 / 1.7724539
results.append(("Q5", sigma_n, "0.7978846"))

# Q6
z0 = 1 / sigma_n
phi0 = phi_interp(z0, 1.25, 1.26, 0.8944, 0.8962)
results.append(("Q6", phi0, "0.8950"))

# Q7
z1 = 0.8660254 / sigma_n
phi1 = phi_interp(z1, 1.08, 1.09, 0.8599, 0.8621)
results.append(("Q7", phi1, "0.8611"))

# Q8
z2 = 0.7071068 / sigma_n
phi2 = phi_interp(z2, 0.88, 0.89, 0.8106, 0.8133)
results.append(("Q8", phi2, "0.8123"))

# Q9
z3 = 0.5 / sigma_n
phi3 = phi_interp(z3, 0.62, 0.63, 0.7324, 0.7357)
results.append(("Q9", phi3, "0.7346"))

# Q10
dev0 = phi0 - 1.0000
results.append(("Q10", dev0, "-0.1050"))

# Q11
dev1 = phi1 - (1 + 0.8660254) / 2
dev2 = phi2 - (1 + 0.7071068) / 2
dev3 = phi3 - (1 + 0.5) / 2
rms = math.sqrt((dev0**2 + dev1**2 + dev2**2 + dev3**2 + 0.0**2) / 5)
results.append(("Q11", rms, "0.0602"))

# Q12
chsh = 2 * 1.4142136
results.append(("Q12", chsh, "2.8284"))

# Q13
gap = chsh - 2
results.append(("Q13", gap, "0.8284"))

# Q14
pQ4 = 2 * (1 - 0.9772)
results.append(("Q14", pQ4, "0.0456"))

# Q15
pL4 = 1 - 0.9772
results.append(("Q15", pL4, "0.0228"))

# Q16
pbar = (pQ + pL) / 2
n_req = (3 * math.sqrt(2 * pbar * (1 - pbar)) / dP) ** 2
results.append(("Q16", n_req, "129.6"))

match_count = 0
for cid, computed, expected in results:
    exp_val = float(expected)
    # round computed to the significant digits of the expected string
    sig = len(expected.replace("-", "").replace(".", "").lstrip("0"))
    rounded = float(f"%.{sig}g" % computed)
    match = "yes" if abs(rounded - exp_val) < 10 ** (-(sig)) * max(1, abs(exp_val)) * 1.0 else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={show(computed)} expected={expected} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
