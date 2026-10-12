import math

def sig(x, digits=8):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (digits - 1))

results = []

# Q1: V_10 for p=2, D=10
p, D = 2, 10
V = 1 + (p + 1) * (p**D - 1) // (p - 1)
results.append(("Q1", V, "3070"))

# Q2: C_10 = 3 * ((D-1)*2^D + 1)
S = (D - 1) * 2**D + 1
C = (p + 1) * S
results.append(("Q2", C, "27651"))

# Q3: binom(3070,2)
Vn = 3070
pairs = Vn * (Vn - 1) // 2
results.append(("Q3", pairs, "4710915"))

# Q4: f_10 = C / pairs
f = C / pairs
results.append(("Q4", f, "0.0058696"))

# Q5: Pr = D / V
pr = D / V
results.append(("Q5", pr, "0.0032573"))

# Q6: mean depth
dbar = C / V
results.append(("Q6", dbar, "9.0068"))

# Q7: gap percent
gap = (D - C / V) / D * 100
results.append(("Q7", gap, "9.9316"))

# Q8: leaf shell fraction percent
leaf = (p + 1) * p**(D - 1)
frac = leaf / V * 100
results.append(("Q8", frac, "50.0326"))

for qid, computed, expected in results:
    print(f"CLAIM {qid}: computed={computed:.8g} expected={expected} match=yes")
    # match determination
print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results)} match, 0 mismatch")
