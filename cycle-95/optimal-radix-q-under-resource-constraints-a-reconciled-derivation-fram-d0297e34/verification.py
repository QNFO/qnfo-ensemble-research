import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: continuous optimum of q/ln q at q = e
q_opt = math.e
f_e = q_opt / math.log(q_opt)
# check derivative zero at e: (ln q - 1)/(ln q)^2
deriv = (math.log(q_opt) - 1) / (math.log(q_opt) ** 2)
match = isclose(deriv, 0.0) and isclose(q_opt, math.e)
results.append(("Q1", q_opt, math.e, match))

# Q2: n(2) = ceil(13.815511 / 0.693147)
lnN = 13.815511
n2 = math.ceil(lnN / 0.693147)
results.append(("Q2", n2, 20, n2 == 20))

# Q3: n(3)
n3 = math.ceil(lnN / 1.098612)
results.append(("Q3", n3, 13, n3 == 13))

# Q4: n(4)
n4 = math.ceil(lnN / 1.386294)
results.append(("Q4", n4, 10, n4 == 10))

# Q5: n(5)
n5 = math.ceil(lnN / 1.609438)
results.append(("Q5", n5, 9, n5 == 9))

# Q6: traversal costs
T2, T3, T4, T5 = 2 * n2, 3 * n3, 4 * n4, 5 * n5
match6 = (T2 == 40) and (T3 == 39) and (T4 == 40) and (T5 == 45)
results.append(("Q6", (T2, T3, T4, T5), (40, 39, 40, 45), match6))

# Q7: S(2)/N = 2*(1 - 2^-20)/(2-1)
s2 = 2 * (1 - 2 ** (-20)) / (2 - 1)
match7 = isclose(s2, 2.0000)
results.append(("Q7", round(s2, 4), 2.0000, match7))

# Q8: S(3)/N = 3*(1 - 3^-13)/(3-1)
s3 = 3 * (1 - 3 ** (-13)) / (3 - 1)
match8 = isclose(s3, 1.5000)
results.append(("Q8", round(s3, 4), 1.5000, match8))

mismatches = 0
for cid, computed, expected, match in results:
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")
    if not match:
        mismatches += 1

print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results) - mismatches} match, {mismatches} mismatch")
