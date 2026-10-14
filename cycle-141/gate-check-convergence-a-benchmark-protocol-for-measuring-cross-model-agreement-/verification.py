import math

def sig(x, d=8):
    return f"{x:.{d}g}"

results = []

# Q1: pairwise chance agreement, uniform 4 categories
p_e = sum((1/4)**2 for _ in range(4))
results.append(("Q1", p_e, "0.25"))

# Q2: p_all(M) = (1/4)^(M-1) for M=3,5,7
p3 = (1/4)**2
p5 = (1/4)**4
p7 = (1/4)**6
results.append(("Q2", p3, "0.0625"))
results.append(("Q2b", p5, "0.003906"))
results.append(("Q2c", p7, "0.00024414"))

# Q3: unanimous 5 models, 60 claims: 4^(-240)
log10p = -240 * 0.60206
p_unan = 10 ** log10p
results.append(("Q3", p_unan, "3.2e-145"))

# Q4: n for w=0.10, p_o=0.80, p_e=0.25, z=1.96
def n_kappa(w, po=0.80, pe=0.25, z=1.96):
    return po*(1-po) / (w**2 * (1-pe)**2) * z**2
n10 = n_kappa(0.10)
results.append(("Q4", n10, "109.3"))

# Q5: n for w=0.15
n15 = n_kappa(0.15)
results.append(("Q5", n15, "48.6"))

# Q6: worst case n_max, po(1-po)=0.25
nmax = 0.25 / (0.10**2 * 0.75**2) * 1.96**2
results.append(("Q6", nmax, "170.7"))

# Q7: illustrative kappa
po = 40/50
pe = (23*21 + 13*14 + 12*13 + 2*2) / 50**2
kappa = (po - pe) / (1 - pe)
results.append(("Q7a", po, "0.80"))
results.append(("Q7b", pe, "0.33"))
results.append(("Q7c", kappa, "0.7015"))

# Q8: Spearman sample size, rho=0.35
zsum = 1.96 + 0.8416
n_sp = (zsum/0.35)**2 + 3
results.append(("Q8", n_sp, "67.1"))

# Q9: rho_min for n=50
rho_min = zsum / math.sqrt(50 - 3)
results.append(("Q9", rho_min, "0.4087"))

# Q10: SE(Delta) with n1=n2=55
var_k = 0.16 / (55 * 0.5625)
se = math.sqrt(2 * var_k)
results.append(("Q10", se, "0.1017"))

# Q11: z-scores for Delta=0.20 and 0.30
z20 = 0.20 / se
z30 = 0.30 / se
results.append(("Q11a", z20, "1.97"))
results.append(("Q11b", z30, "2.95"))

# Q12: runs = M*F*n
runs = 5 * 3 * 110
results.append(("Q12", runs, "1650"))

# Q13: expert hours
hours = 110 * 2 * 0.25
results.append(("Q13", hours, "55"))

def match(computed, expected_str):
    # round computed to significant digits of expected string
    exp = float(expected_str)
    # count significant digits in expected
    s = expected_str.replace("-", "").replace(".", "").lstrip("0")
    digits = len(s.rstrip("e023456789")) if False else None
    # simpler: count sig digits manually via string
    import re
    m = re.match(r"^-?0*(\d[\d.]*)$", expected_str)
    # count significant digits
    digits = len(re.sub(r"[^0-9]", "", expected_str.split("e")[0]).lstrip("0"))
    if "e" in expected_str:
        mant = expected_str.split("e")[0]
        digits = len(re.sub(r"[^0-9]", "", mant).lstrip("0"))
    rounded = float(f"%.{digits}g" % computed)
    return "yes" if abs(rounded - exp) <= 1e-12 * max(1, abs(exp)) or rounded == exp else "no"

for cid, comp, exp in results:
    print(f"CLAIM {cid}: computed={comp:.8g} expected={exp} match={match(comp, exp)}")

n_claims = len(results)
n_match = sum(1 for _, c, e in results if match(c, e) == "yes")
print(f"VERIFICATION SUMMARY: {n_claims} claims, {n_match} match, {n_claims - n_match} mismatch")
