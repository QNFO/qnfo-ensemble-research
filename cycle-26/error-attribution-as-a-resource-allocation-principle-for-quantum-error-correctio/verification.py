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

# Q1: n_c = 4 * 57
per_round = 9 + 4*8 + 8 + 8
n_c = 4 * per_round
results.append(check("Q1", n_c, 228))

# Q2: m = f * n_c
m_low = 0.05 * n_c
m_high = 0.07 * n_c
results.append(check("Q2", round(m_low), 11))
results.append(check("Q2", round(m_high), 16))

# Q3: r = 2(1-f)/(1-2f) at f=0.05
r3 = 2*(1-0.05)/(1-2*0.05)
results.append(check("Q3", r3, 2.111))

# Q4: r at f=0.07
r4 = 2*(1-0.07)/(1-2*0.07)
results.append(check("Q4", r4, 2.163))

# Q5: f = (r-2)/(2r-1) at r=3
f5 = (3-2)/(2*3-1)
results.append(check("Q5", f5, 0.20))

# Q6: rho = r/(f*r+1-f) at f=0.06, r=1.88/0.88
r6 = 1.88/0.88
rho6 = r6/(0.06*r6 + 1 - 0.06)
results.append(check("Q6", rho6, 2.000))

# Q7: P_L = n_c * p * s * (1 + f(r-1))
p = 1e-3
s = 1.0
f = 0.06
r = 2.136
P_L = n_c * p * s * (1 + f*(r-1))
results.append(check("Q7", P_L, 0.2435))

# Q8: G_tgt = m*r / (2*n_c*(1 + f(r-1)))
m = 14
G_tgt = m*r / (2*n_c*(1 + f*(r-1)))
results.append(check("Q8", G_tgt, 0.0614))

N = len(results)
M = sum(results)
K = N - M
print(f"VERIFICATION SUMMARY: {N} claims, {M} match, {K} mismatch")
