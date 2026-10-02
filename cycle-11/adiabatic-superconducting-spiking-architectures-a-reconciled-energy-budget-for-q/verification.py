import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: E_conv = C * V^2
C = 100e-15
V = 0.5e-3
E_conv = C * V**2
results.append(check("Q1", E_conv, 25e-21))

# Q2: RC = R * C
R = 10e3
RC = R * C
results.append(check("Q2", RC, 1e-9))

# Q3: T/RC
T = 10e-9
ratio = T / RC
results.append(check("Q3", ratio, 10.0))

# Q4: f = 1/(2*T) with T = 100*RC
T_cons = 100 * RC
f = 1 / (2 * T_cons)
results.append(check("Q4", f, 5e6))

# Q5: E_ad = (RC/T) * C * V^2
E_ad = (RC / T) * C * V**2
results.append(check("Q5", E_ad, 2.5e-21))

# Q6: P_static = I_leak * V
I_leak = 1e-9
P_static = I_leak * V
results.append(check("Q6", P_static, 5e-13))

# Q7: E_static = P_static * T
E_static = P_static * T
results.append(check("Q7", E_static, 5e-21))

# Q8: E_event = E_ad + E_static
E_event = E_ad + E_static
results.append(check("Q8", E_event, 7.5e-21))

n = len(results)
m = sum(results)
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")
