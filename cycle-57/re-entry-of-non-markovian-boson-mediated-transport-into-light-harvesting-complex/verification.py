import math

c = 2.9979e10  # cm/s

def tau_T_ps(V, Delta):
    k = V**2 / Delta          # cm^-1
    omega = 2 * math.pi * c * k  # rad/s
    tau = 1 / omega           # s
    return k, omega, tau * 1e12  # ps

results = []

# Q1
g = 100.0
results.append(("Q1", g, 100.0, g == 100.0))

# Q2
k2 = 30**2 / 100
results.append(("Q2", k2, 9.0, math.isclose(k2, 9.0, rel_tol=1e-6)))

# Q3
omega3 = 2 * math.pi * c * 9
results.append(("Q3", omega3, 1.6952e12, math.isclose(omega3, 1.6952e12, rel_tol=1e-3)))

# Q4
tau4 = 1 / omega3
results.append(("Q4", tau4, 5.899e-13, math.isclose(tau4, 5.899e-13, rel_tol=1e-3)))

# Q5
eta5 = 1 / (1 + 1/1000)
results.append(("Q5", eta5, 0.999001, math.isclose(eta5, 0.999001, rel_tol=1e-6)))

# Q6, Q7
_, _, tau_ps = tau_T_ps(30, 100)
R6 = 0.1 / tau_ps
R7 = 1.0 / tau_ps
results.append(("Q6", R6, 0.1695, math.isclose(R6, 0.1695, rel_tol=1e-3)))
results.append(("Q7", R7, 1.6953, math.isclose(R7, 1.6953, rel_tol=1e-3)))

# Q8
_, _, tau8 = tau_T_ps(20, 100)
R8f = 0.1 / tau8
R8s = 1.0 / tau8
ok8 = (math.isclose(tau8, 1.3272, rel_tol=1e-3)
       and math.isclose(R8f, 0.0753, rel_tol=1e-2)
       and math.isclose(R8s, 0.7535, rel_tol=1e-2))
results.append(("Q8", (tau8, R8f, R8s), (1.3272, 0.0753, 0.7535), ok8))

for cid, comp, exp, match in results:
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if match else 'no'}")

n = len(results)
m = sum(1 for r in results if r[3])
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
