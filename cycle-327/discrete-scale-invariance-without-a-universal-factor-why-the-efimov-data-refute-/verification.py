import math

# Inputs
lam = 22.694
pi = math.pi
ln2 = math.log(2)

# Computations
ln_lam = math.log(lam)                     # Q1
s0 = 2 * pi / ln_lam                        # Q2
log2_lam = ln_lam / ln2                     # Q3
per_step = lam / 2                          # Q4
lam_sq = lam ** 2                           # Q5
lam_4 = lam_sq ** 2                         # Q6
ratio = lam_4 / (2 ** 4)                    # Q7
s0_dyadic = 2 * pi / ln2                    # Q8
diff = ln_lam - ln2                         # Q9

# Helper for rounding to the required decimal places
def fmt(val, ndigits, commas=False):
    if ndigits == 0:
        # integer rounding
        v = int(round(val))
        return f"{v:,}" if commas else str(v)
    else:
        v = round(val, ndigits)
        s = f"{v:.{ndigits}f}"
        return f"{s:,}" if commas else s

# Expected values (as strings from the paper)
expected = {
    "Q1": "3.1222",
    "Q2": "2.0124",
    "Q3": "4.505",
    "Q4": "11.347",
    "Q5": "515.02",
    "Q6": "265,244",
    "Q7": "16,578",
    "Q8": "9.0647",
    "Q9": "2.4291",
}

# Prepare computed strings with appropriate formatting
computed = {
    "Q1": fmt(ln_lam, 4),
    "Q2": fmt(s0, 4),
    "Q3": fmt(log2_lam, 3),
    "Q4": fmt(per_step, 3),
    "Q5": fmt(lam_sq, 2),
    "Q6": fmt(lam_4, 0, commas=True),
    "Q7": fmt(ratio, 0, commas=True),
    "Q8": fmt(s0_dyadic, 4),
    "Q9": fmt(diff, 4),
}

# Print results
for qid in ["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9"]:
    comp = computed[qid]
    exp = expected[qid]
    match = "yes" if comp == exp else "no"
    print(f"CLAIM {qid}: computed={comp} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, "
      f"{sum(1 for q in expected if computed[q]==expected[q])} match, "
      f"{sum(1 for q in expected if computed[q]!=expected[q])} mismatch")
