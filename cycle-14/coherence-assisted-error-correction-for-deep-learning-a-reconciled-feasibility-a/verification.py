import math

results = []

def check(cid, computed, expected, tol=1e-6):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=tol) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    results.append(match == "yes")

# Q1: SEC-DED energy
E_SEC = 1e8 * (8/64) * 2 * 0.1e-12
check("Q1", E_SEC, 2.5e-6)

# Q2: BCH energy
E_BCH = 1e8 * (16/64) * 4 * 0.1e-12
check("Q2", E_BCH, 1e-5)

# Q3: upgrade cost and power
dE = (E_BCH - E_SEC) * 1e9  # J/day
P = dE / 86400
check("Q3", P, 0.0868, tol=1e-2)

# Q4: TMR energy per block
E_TMR = 3 * 256 * 1e-12
check("Q4", E_TMR, 768e-12)

# Q5: TMR residual BER
p_TMR = 3 * (1e-5)**2
check("Q5", p_TMR, 3e-10)

# Q6: max coherent depth
D_max = 100e-6 / 20e-9
check("Q6", D_max, 5000)

# Q7: syndrome circuit time and margin
t_syn = 14 * 20e-9
margin = 100e-6 / t_syn
check("Q7", margin, 357, tol=1e-2)

# Q8: per-call latency
t_call = 10e-6 + 100 * (50 * 20e-9)
check("Q8", t_call, 110e-6)

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n-m} mismatch")
