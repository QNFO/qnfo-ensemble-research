import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

claims = []

# Q1: rho(50) = 2^50 / (50*49/2) = 9.19e11 (paper states 9.19e11, 3 sig figs)
H50 = 2**50
R50 = 50 * 49 // 2
rho50 = H50 / R50
claims.append(("Q1", rho50, "9.19e11", 3))

# Q2/Q3 handled below; keep ids in order
# Q2: R(50) = 1225 (exact)
claims.append(("Q2", float(R50), "1225", None))

# Q3: H(50) = 2^50 = 1.1259e15 (paper: 1.1259e15, 5 sig figs)
claims.append(("Q3", float(H50), "1.1259e15", 5))

# Q4: memory = 16 * 2^50 bytes = 18.014 PB (paper: 18.014 PB, 5 sig figs)
bytes_H = 16 * 2**50
PB = bytes_H / 1e15
claims.append(("Q4", PB, "18.014", 5))

# Q5: pairwise memory = 16 * 1225 = 19600 bytes (paper: 1.96e4, 3 sig figs)
bytes_R = 16 * R50
claims.append(("Q5", float(bytes_R), "19600", 3))

# Q6: FWHM-to-sigma constant = 2*sqrt(2*ln2) = 2.354820 (6 sig figs)
c = 2 * math.sqrt(2 * math.log(2))
claims.append(("Q6", c, "2.354820", 6))

# Q7: upper band = 0.01 / c = 4.2466e-3 (5 sig figs)
up = 0.01 / c
claims.append(("Q7", up, "4.2466e-3", 5))

# Q8: lower band = 0.005 / c = 2.1233e-3 (5 sig figs)
lo = 0.005 / c
claims.append(("Q8", lo, "2.1233e-3", 5))

# Q9: worst-case stack = 5 * 1e-2 = 5e-2 (exact)
wc = 5 * 1e-2
claims.append(("Q9", wc, "5e-2", None))

# Q10: RSS stack = 1e-2 * sqrt(5) = 2.2361e-2 (5 sig figs)
rss = 1e-2 * math.sqrt(5)
claims.append(("Q10", rss, "2.2361e-2", 5))

# Q11: ratio = sqrt(5) = 2.2361 (5 sig figs)
ratio = math.sqrt(5)
claims.append(("Q11", ratio, "2.2361", 5))

# Q12: N = 60*60 = 3600 (exact)
N = 60 * 60
claims.append(("Q12", float(N), "3600", None))

# Q13: drift = 1e-3 * sqrt(3600) = 6.0e-2 m (2 sig figs)
drift = 1e-3 * math.sqrt(N)
claims.append(("Q13", drift, "0.06", 2))

# Q14: linear drift = 1e-3 * 3600 = 3.6 m (2 sig figs)
lin = 1e-3 * N
claims.append(("Q14", lin, "3.6", 2))

# Q15: ratio = 3.6 / 0.06 = 60 (exact)
dr = 3.6 / 0.06
claims.append(("Q15", dr, "60", None))

# Q16: frame period = 1/90 s = 11.111 ms (5 sig figs)
Tf_ms = (1 / 90) * 1000
claims.append(("Q16", Tf_ms, "11.111", 5))

mismatch = 0
for cid, computed, expected_str, nsig in claims:
    if nsig is None:
        match = (abs(computed - float(expected_str)) < 1e-12)
    else:
        match = (sig(computed, nsig) == float(expected_str))
    if not match:
        mismatch += 1
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected_str} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {len(claims) - mismatch} match, {mismatch} mismatch")
