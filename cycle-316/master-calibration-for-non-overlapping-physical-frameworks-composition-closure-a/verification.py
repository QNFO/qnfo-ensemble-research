import math

def fmt_scientific(val, sig):
    # format with given significant digits, strip unnecessary zeros and leading zeros in exponent
    s = f"{val:.{sig}e}"
    mantissa, exp = s.split('e')
    mantissa = mantissa.rstrip('0').rstrip('.')
    # remove leading zeros in exponent, e.g., -03 -> -3, +04 -> 4
    exp = exp.lstrip('+').lstrip('0')
    if exp.startswith('-') and exp[1:] == '':
        exp = '-0'
    return f"{mantissa}e{exp}"

def compare(comp, exp):
    return "yes" if comp == exp else "no"

results = []

# Q1
val = 29 * 28 // 2
exp = "406"
comp = str(val)
results.append(("Q1", comp, exp, compare(comp, exp)))

# Q2
val = 29 * 28 * 27 // 6
exp = "3654"
comp = str(val)
results.append(("Q2", comp, exp, compare(comp, exp)))

# Q3
val = 3654 / 406
exp = "9.0"
comp = f"{val:.1f}"
results.append(("Q3", comp, exp, compare(comp, exp)))

# Q4
val = 7 * 6 // 2
exp = "21"
comp = str(val)
results.append(("Q4", comp, exp, compare(comp, exp)))

# Q5
val = 29 - 21
exp = "8"
comp = str(val)
results.append(("Q5", comp, exp, compare(comp, exp)))

# Q6
val = 0  # C(2,3)=0
exp = "0"
comp = str(val)
results.append(("Q6", comp, exp, compare(comp, exp)))

# Q7
e1, e2, e3 = 1e-3, 2e-3, 5e-4
val = 1 - (1 - e1) * (1 - e2) * (1 - e3)
exp = "3.4965e-3"
comp = fmt_scientific(val, 5)
results.append(("Q7", comp, exp, compare(comp, exp)))

# Q8
tau, eps_min = 1e-3, 1e-2
val = math.log(1 - tau) / math.log(1 - eps_min)
exp = "0.0995"
comp = f"{val:.4f}"
results.append(("Q8", comp, exp, compare(comp, exp)))

# Q9
k = 4
val = 1 - (1 - eps_min) ** k
exp = "3.94e-2"
comp = fmt_scientific(val, 3)
results.append(("Q9", comp, exp, compare(comp, exp)))

# Q10
p = 0.9
m = 3654
val = p ** m
exp = "6.34e-168"
comp = fmt_scientific(val, 3)
results.append(("Q10", comp, exp, compare(comp, exp)))

# Q11
threshold = 0.01
max_n = 0
for n in range(1, 20):
    if math.comb(n, 3) <= math.log(threshold) / math.log(p):
        max_n = n
exp = "7"
comp = str(max_n)
results.append(("Q11", comp, exp, compare(comp, exp)))

# Q12
exp = "2"
comp = str(1.0 / 0.5)  # 1 TeV / 0.5 TeV
results.append(("Q12", comp, exp, compare(comp, exp)))

# Q13
exp = "3"
comp = str(1.5 / 0.5)
results.append(("Q13", comp, exp, compare(comp, exp)))

# Q14
val = 29 / 7
exp = "4.14"
comp = f"{val:.2f}"
results.append(("Q14", comp, exp, compare(comp, exp)))

# Q15
eps = 1e-2
val = 1 - (1 - eps) ** 2
exp = "0.0199"
comp = f"{val:.4f}"
results.append(("Q15", comp, exp, compare(comp, exp)))

# Q16
f = 0.5
val = 1 - (1 - f * e1) * (1 - f * e2) * (1 - f * e3)
exp = "1.7491e-3"
comp = fmt_scientific(val, 5)
results.append(("Q16", comp, exp, compare(comp, exp)))

# Output
match_count = sum(1 for _, _, _, m in results if m == "yes")
total = len(results)
mismatch_count = total - match_count

for cid, comp, exp, m in results:
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={m}")

print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {mismatch_count} mismatch")
