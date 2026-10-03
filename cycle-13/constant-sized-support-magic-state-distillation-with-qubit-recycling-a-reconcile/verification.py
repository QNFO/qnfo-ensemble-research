import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: p2 = 35^4 * p^9 at p=1e-3
coef = 35
p = 1e-3
p2 = coef * (coef * p**3)**3
results.append(check("Q1", p2, 1.500625e-21))

# Q2: at p=1e-2
p = 1e-2
p2 = coef * (coef * p**3)**3
results.append(check("Q2", p2, 1.500625e-12))

# Q3: validity check 35*p^2 at p=1e-2
val = 35 * (1e-2)**2
results.append(check("Q3", val, 3.5e-3))

# Q4: baseline peak occupancy
baseline = 15 + 15 * 15
results.append(check("Q4", baseline, 240))

# Q5: recycled peak occupancy
recycled = 15 + 15
results.append(check("Q5", recycled, 30))

# Q6: reduction factor
factor = baseline / recycled
results.append(check("Q6", factor, 8.0))

# Q7: k_max = f*p0/delta
f, p0, delta = 0.10, 1e-3, 1e-5
kmax = f * p0 / delta
results.append(check("Q7", kmax, 10))

# Q8: sensitivity
k1 = f * p0 / 1e-4
k2 = f * p0 / 1e-6
ok8 = check("Q8a", k1, 1) and check("Q8b", k2, 100)
results.append(ok8)

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
