import math

def sig(x, n):
    # round to n significant digits
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: H(K) = log2(65535) + log2(26!)
log2_26fact = math.lgamma(27) / math.log(2)  # log2(26!)
log2_65535 = math.log2(65535)
H = log2_65535 + log2_26fact
results.append(("Q1", H, "104.38", 2))

# Q2: |K| = 2^104.38
K = 2 ** 104.38
results.append(("Q2", K, "2.64e31", 3))

# Q3: n0 = 104.38 / 0.70
n0 = 104.38 / 0.70
results.append(("Q3", n0, "149.1", 4))

# Q4: n0_radix = 16.00 / 0.70
n0r = 16.00 / 0.70
results.append(("Q4", n0r, "22.9", 3))

# Q5: W1 = 65535 * 1000
W1 = 65535 * 1000
results.append(("Q5", W1, "6.5535e7", 5))

# Q6: t = 6.5535e7 / 1e8
t6 = 6.5535e7 / 1e8
results.append(("Q6", t6, "0.66", 2))

# Q7: t = 6.5535e7 / 1e9
t7 = 6.5535e7 / 1e9
results.append(("Q7", t7, "0.066", 2))

# Q8: 0.995^1000
p8 = 0.995 ** 1000
results.append(("Q8", p8, "0.006654", 4))

# Q9: T_bf = (2.64e31 / 1e9) / 3.156e7
T9 = (2.64e31 / 1e9) / 3.156e7
results.append(("Q9", T9, "8.36e14", 3))

# Q10: ratio = 8.36e14 / (0.66 / 3.156e7)
r10 = 8.36e14 / (0.66 / 3.156e7)
results.append(("Q10", r10, "4.0e22", 2))

# Q11: gap = 0.12 / 1e-3
g11 = 0.12 / 1e-3
results.append(("Q11", g11, "120", 3))

# Q12: 104.38 / 0.5
n12 = 104.38 / 0.5
results.append(("Q12", n12, "208.8", 4))

# Q13: 104.38 / 1.0
n13 = 104.38 / 1.0
results.append(("Q13", n13, "104.4", 4))

# Q14: gap = 0.05 / 1e-3
g14 = 0.05 / 1e-3
results.append(("Q14", g14, "50", 2))

# Q15: 1000 / 149.1
f15 = 1000 / 149.1
results.append(("Q15", f15, "6.7", 2))

# Q16: log2(26!) via log10(4.0329e26) * 3.32193
v16 = math.log10(4.0329e26) * 3.32193
results.append(("Q16", v16, "88.38", 2))

match_count = 0
for cid, computed, expected_str, sigd in results:
    # parse expected string to plain number
    exp_val = float(expected_str)
    comp_rounded = sig(computed, sigd)
    match = "yes" if abs(comp_rounded - exp_val) <= abs(exp_val) * 10 ** (-sigd + 1) / 2 or abs(comp_rounded - exp_val) < 10 ** (math.floor(math.log10(abs(exp_val))) - sigd + 1) else "no"
    # simpler: compare formatted strings
    match = "yes" if ("%.{0}g".format(sigd) % computed) == ("%.{0}g".format(sigd) % exp_val) else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")
