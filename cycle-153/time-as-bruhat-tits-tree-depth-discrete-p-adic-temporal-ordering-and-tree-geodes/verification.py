import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: N_10 = (p+1)*p^(d-1), p=2, d=10
p, d = 2, 10
N10 = (p + 1) * p ** (d - 1)
results.append(("Q1", N10, "1536", 4))

# Q2: V_10 = 1 + (p+1)*(p^D - 1)/(p-1), p=2, D=10
p, D = 2, 10
V10 = 1 + (p + 1) * (p ** D - 1) // (p - 1)
results.append(("Q2", V10, "3070", 4))

# Q3: C_10 = (p+1)*(D*p^(D+1) - (D+1)*p^D + 1)/(p-1)^2, p=2, D=10
p, D = 2, 10
num = D * p ** (D + 1) - (D + 1) * p ** D + 1
C10 = (p + 1) * num // (p - 1) ** 2
results.append(("Q3", C10, "27651", 5))

# Q4: binom(3070,2) = 3070*3069/2
V = 3070
pairs = V * (V - 1) // 2
results.append(("Q4", pairs, "4710915", 7))

# Q5: f_10 = 27651/4710915
f10 = 27651 / 4710915
results.append(("Q5", f10, "0.0058696", 5))

# Q6: f_asym = 2*(p-1)*D/((p+1)*p^D), p=2, D=10
p, D = 2, 10
f_asym = 2 * (p - 1) * D / ((p + 1) * p ** D)
results.append(("Q6", f_asym, "0.0065104", 5))

# Q7: bar_d = 27651/3070
bar_d = 27651 / 3070
results.append(("Q7", bar_d, "9.0068", 5))

# Q8: fraction = 1536/3070
frac = 1536 / 3070
results.append(("Q8", frac, "0.50033", 5))

# Q9: C(5) = (2^6 - 2)/(2-1), p=2, Delta=5
p, Delta = 2, 5
C5_p2 = (p ** (Delta + 1) - p) // (p - 1)
results.append(("Q9", C5_p2, "62", 2))

# Q10: C(5) = (3^6 - 3)/2, p=3, Delta=5
p, Delta = 3, 5
C5_p3 = (p ** (Delta + 1) - p) // (p - 1)
results.append(("Q10", C5_p3, "363", 3))

# Q11: ratio = 363/62
ratio = 363 / 62
results.append(("Q11", ratio, "5.85", 3))

# Q12: gap = (10 - 9.0068)/10
gap = (10 - 27651 / 3070) / 10
results.append(("Q12", gap, "0.09932", 4))

# Q13: factor = f_asym / f_exact
factor = (2 * 1 * 10 / (3 * 2 ** 10)) / (27651 / 4710915)
results.append(("Q13", factor, "1.109", 4))

# Q14: digits = 10^20 * log10(2)
E = 10 ** 20
digits = E * math.log10(2)
results.append(("Q14", digits, "3.01e19", 3))

for cid, computed, expected, n in results:
    c = sig(computed, n)
    match = "yes" if float(expected) == c else "no"
    print(f"CLAIM {cid}: computed={c:.8g} expected={expected} match={match}")

print("VERIFICATION SUMMARY: 14 claims, " + str(sum(1 for _, _, e, n in results if float(e) == sig(dict((r[0], r[1]) for r in results)[_], n)) if False else "") , end="")
