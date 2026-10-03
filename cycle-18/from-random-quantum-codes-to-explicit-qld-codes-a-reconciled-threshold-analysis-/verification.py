import math

def H2(p):
    return -p*math.log2(p) - (1-p)*math.log2(1-p)

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

# Q1
h = H2(0.1)
results.append(check("Q1", round(h, 6), 0.468996))

# Q2
rstar = 1 - h
results.append(check("Q2", round(rstar, 4), 0.5310))

# Q3
R = 1 - 0.3 - 0.3
results.append(check("Q3", round(R, 6), 0.4))

# Q4
slack = rstar - 0.3
results.append(check("Q4", round(slack, 4), 0.2310))

# Q5
k = 100000 - 0.3*100000 - 0.3*100000
results.append(check("Q5", int(round(k)), 40000))

# Q6
eps = 1 - 0.4 - h
results.append(check("Q6", round(eps, 4), 0.1310))

# Q7
L = math.ceil(2/eps)
results.append(check("Q7", L, 16))

# Q8
r2 = 1 - h - 1/2
results.append(check("Q8", round(r2, 6), 0.031004))

print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(results)} match, {len(results)-sum(results)} mismatch")
