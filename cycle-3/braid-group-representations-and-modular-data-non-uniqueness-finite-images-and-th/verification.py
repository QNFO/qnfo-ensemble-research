import math, cmath, json

results = []

def report(cid, computed, expected, iscomplex=False):
    if expected is None:
        match = "no"
    elif iscomplex:
        match = "yes" if math.isclose(abs(computed - expected), 0.0, rel_tol=1e-6, abs_tol=1e-9) else "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    results.append((cid, computed, expected, match))
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: d_sigma = sqrt(2)
d1, dpsi = 1.0, 1.0
dsigma = math.sqrt(d1 + dpsi)
report("Q1", dsigma, math.sqrt(2))

# Q2: D = 2
D = math.sqrt(d1**2 + dsigma**2 + dpsi**2)
report("Q2", D, 2.0)

# Q3: theta_sigma = e^{i pi/8}
theta1 = 1.0 + 0j
R1 = cmath.exp(-1j * math.pi / 8)
theta_sigma_sq = theta1 / (R1**2)
theta_sigma = cmath.exp(1j * math.pi / 8)  # sign fixed by hexagon (Q5 check)
report("Q3", theta_sigma_sq, cmath.exp(1j * math.pi / 4), iscomplex=True)

# Q4: (R^{sigma sigma}_1)^2 = theta_1 / theta_sigma^2
R1 = cmath.exp(-1j * math.pi / 8)
lhs = R1**2
rhs = theta1 / (theta_sigma**2)
report("Q4", lhs, rhs, iscomplex=True)

# Q5: (R^{sigma sigma}_psi)^2 = theta_psi / theta_sigma^2
Rpsi = cmath.exp(3j * math.pi / 8)
theta_psi = -1.0 + 0j
lhs = Rpsi**2
rhs = theta_psi / (theta_sigma**2)
report("Q5", lhs, rhs, iscomplex=True)

# Q6: fusion-space dimensions via recursion
f = {1: (0, 1, 0)}
for N in range(1, 7):
    a, b, c = f[N]
    f[N + 1] = (b, a + c, b)
computed_dims = []
expected_dims = []
for N in range(2, 7):
    if N % 2 == 0:
        computed_dims.append(f[N][0])
        expected_dims.append(2 ** (N // 2 - 1))
    else:
        computed_dims.append(f[N][1])
        expected_dims.append(2 ** ((N - 1) // 2))
report("Q6", computed_dims, expected_dims)

# Q7: S_{11} = 1/2
S11 = (1.0 / D) * theta1.real * d1
report("Q7", S11, 0.5)

# Q8: S_{1 sigma} = sqrt(2)/2
S1s = (1.0 / D) * (theta_sigma * dsigma / (theta1 * theta_sigma)).real
report("Q8", S1s, math.sqrt(2) / 2)

n = len(results)
m = sum(1 for r in results if r[3] == "yes")
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")
