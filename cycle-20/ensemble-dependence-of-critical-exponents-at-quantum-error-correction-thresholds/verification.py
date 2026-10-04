import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) and isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1
n, p, t = 100, 0.01, 1
F_GC = (1-p)**n + n*p*(1-p)**(n-1)
results.append(check("Q1", round(F_GC, 6), 0.735762))

# Q2
F_C = 1.0 if n*p <= t else 0.0
results.append(check("Q2", F_C, 1.0))

# Q3
dF = F_C - F_GC
results.append(check("Q3", round(dF, 6), 0.264238))

# Q4
mu = n*p
results.append(check("Q4", mu, 1.0))

# Q5
var = n*p*(1-p)
sigma = math.sqrt(var)
results.append(check("Q5", round(sigma, 6), 0.994987))

# Q6
rel = sigma/mu
results.append(check("Q6", round(rel, 6), 0.994987))

# Q7
tail = 1 - F_GC
results.append(check("Q7", round(tail, 6), 0.264238))

# Q8
h2 = -p*math.log2(p) - (1-p)*math.log2(1-p)
results.append(check("Q8", round(h2, 7), 0.0807931))

print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(results)} match, {len(results)-sum(results)} mismatch")
