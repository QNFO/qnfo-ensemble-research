import math

def phi(k):
    return sum(1 for i in range(1, k + 1) if math.gcd(i, k) == 1)

results = []

# Q1: shear rescaling c' = (lambda1/lambda2)*c, lambda1=2, lambda2=3, c=1
c_prime = (2 / 3) * 1
results.append(("Q1", c_prime, "0.666667"))

# Q2: N_sed/N_oct = 35/7
ratio = 35 / 7
results.append(("Q2", ratio, "5"))

# Q3: g = log2(5) = ln(5)/ln(2)
g = math.log(5) / math.log(2)
results.append(("Q3", g, "2.321928"))

# Q4: D3 = 2^3 = 8, D4 = 2^4 = 16, D4/D3 = 2
D3 = 2 ** 3
D4 = 2 ** 4
dim_factor = D4 / D3
results.append(("Q4", dim_factor, "2"))

# Q5: delta(O) = 7/8, delta(S) = 35/16
delta_O = 7 / 8
delta_S = 35 / 16
results.append(("Q5a", delta_O, "0.875"))
results.append(("Q5b", delta_S, "2.1875"))

# Q6: density growth factor = 5 * (8/16)
dens_factor = 5 * (8 / 16)
results.append(("Q6", dens_factor, "2.5"))

# Q7: face count F = C(2,0)+C(2,1)+C(2,2)
F = math.comb(2, 0) + math.comb(2, 1) + math.comb(2, 2)
results.append(("Q7", F, "4"))

# Q8: n(n-1) for n=5,6,7
for n, exp in [(5, "20"), (6, "30"), (7, "42")]:
    results.append((f"Q8_n{n}", n * (n - 1), exp))

# Q9: n! for n=3,4,5
for n, exp in [(3, "6"), (4, "24"), (5, "120")]:
    results.append((f"Q9_{n}fact", math.factorial(n), exp))

# Q10: totient values
for k, exp in [(2, "1"), (3, "2"), (4, "2"), (5, "4"), (6, "2")]:
    results.append((f"Q10_phi{k}", phi(k), exp))

# Q11: projection P1: N_next = 35*5 = 175; density = 175/32
N_next = 35 * 5
dens_next = N_next / 32
results.append(("Q11a", N_next, "175"))
results.append(("Q11b", dens_next, "5.46875"))

match_count = 0
for cid, computed, expected in results:
    # round computed to significant digits of expected string
    sig = len(expected.replace(".", "").lstrip("0"))
    rounded = float(f"%.{sig}g" % computed)
    match = "yes" if abs(rounded - float(expected)) < 1e-12 else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={computed:.8f} expected={expected} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
