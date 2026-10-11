import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: average segment length for L=10
L = 10
S = sum(k * (10 - k + 1) for k in range(1, L + 1))
n_seg = L * (L + 1) // 2
avg = S / n_seg
results.append(("Q1", avg, 4.0))

# Q2: saturation time under projection P0
t_sat = math.ceil(L / 4.0)
results.append(("Q2", t_sat, 3))

# Q3: first-moment rate for uniform density on [-1,1]
# integral of omega^2 * (1/2) domega from -1 to 1
rate = 0.5 * (1/3 - (-1/3))
results.append(("Q3", rate, 1/3))

# Q4: mean advance integral = 0
mean_int = 0.5 * (0.5**2/2 - (-0.5)**2/2)
results.append(("Q4", mean_int, 0.0))

# Q5: variance at t=0.3, u=+1
U = 0.3
var = U**2 * (1/3)
sigma = math.sqrt(var)
results.append(("Q5", var, 0.03))
results.append(("Q5-sigma", sigma, math.sqrt(0.03)))  # paper states sigma ~ 0.1732

# Q6: minimum steering time to M1 target 0.1
M1_target = 0.1
U_req = M1_target / (1/3)
T_min = U_req / 1.0
check = (1/3) * 0.3
results.append(("Q6", T_min, 0.3))
results.append(("Q6-check", check, 0.1))

# Q7: skewed density c2 and steering time
# rho_s(omega) = (2/3)(omega+1) on [0,1]
c2 = (2/3) * (1/4 + 1/3)
T_min_s = 0.1 / c2
results.append(("Q7-c2", c2, 7/18))
results.append(("Q7-Tmin", T_min_s, 1.8/7))

# Q8: baseline tokens per cycle, alpha=0.7, gamma=4
alpha = 0.7
gamma = 4
EN = (1 - alpha**(gamma + 1)) / (1 - alpha)
results.append(("Q8", EN, 2.7731))

for cid, computed, expected in results:
    if isinstance(expected, (int, float)) and isinstance(computed, (int, float)):
        match = isclose(float(computed), float(expected))
    else:
        match = computed == expected
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

n = len(results)
m = sum(1 for _, c, e in results if (math.isclose(float(c), float(e), rel_tol=1e-6) if isinstance(c, (int, float)) and isinstance(e, (int, float)) else c == e))
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")
