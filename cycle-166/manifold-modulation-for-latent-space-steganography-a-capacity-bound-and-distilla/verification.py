import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

ln2 = 0.693147
ln100 = 4.60517

results = []

# Q1
c = 0.05 / ln2
results.append(("Q1", c, "0.072134", 6))
# Q2
c = 0.10 / ln2
results.append(("Q2", c, "0.144270", 6))
# Q3
c = 0.20 / ln2
results.append(("Q3", c, "0.288539", 6))
# Q4
c1 = 0.05 / ln2
imax = 10**4 * c1
results.append(("Q4", imax, "721.34", 5))
# Q5
bytes_ = imax / 8
results.append(("Q5", bytes_, "90.17", 4))
# Q6
c20 = 0.20 / ln2
imax20 = 10**4 * c20
results.append(("Q6", imax20, "2885.39", 6))
# Q7
n = ln100 / 0.05
results.append(("Q7", n, "92.10", 4))
# Q8
n = ln100 / 0.10
results.append(("Q8", n, "46.05", 4))
# Q9
n = ln100 / 0.20
results.append(("Q9", n, "23.03", 4))
# Q10
M = 10**4 * ln2 / 0.05
results.append(("Q10", M, "138629.4", 7))
# Q11
M = 10**4 * ln2 / 0.10
results.append(("Q11", M, "69314.7", 6))
# Q12
M = 10**4 * ln2 / 0.20
results.append(("Q12", M, "34657.4", 6))
# Q13
docs = 10**4 * ln2 / 0.05 / 10**4
results.append(("Q13", docs, "13.86", 4))
# Q14
ratio = 1 / (0.4 * ln2)
results.append(("Q14", ratio, "3.6068", 5))
# Q15
da = 0.4 * 0.05
results.append(("Q15", da, "0.02", 2))
# Q16
da = 0.4 * 0.20
results.append(("Q16", da, "0.08", 2))

match_count = 0
for qid, computed, expected, nsig in results:
    comp = sig(computed, nsig)
    match = "yes" if abs(comp - float(expected)) < 10**(-nsig) * max(1, abs(float(expected))) else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {qid}: computed={comp:.8f} expected={expected} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
