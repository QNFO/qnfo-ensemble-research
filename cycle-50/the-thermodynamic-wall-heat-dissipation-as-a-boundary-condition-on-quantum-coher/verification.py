import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: G_th = k*A/d = 4.0 W/K
k, A, d = 0.04, 10.0, 0.1
G_th = k * A / d
results.append(("Q1", G_th, 4.0))

# Q2: P = G_th * DeltaT = 120.0 W
DeltaT = 30.0
P = G_th * DeltaT
results.append(("Q2", P, 120.0))

# Q3: C = m*c = 45000 J/K
m, c = 50.0, 900.0
C = m * c
results.append(("Q3", C, 45000.0))

# Q4: DeltaE = C * DeltaT = 1.35e6 J
DeltaE = C * DeltaT
results.append(("Q4", DeltaE, 1.35e6))

# Q5: tau = DeltaE / P = 11250 s
tau = DeltaE / P
results.append(("Q5", tau, 11250.0))

# Q6: halving k -> P = 60.0 W, tau = 22500 s
k2 = 0.02
P2 = k2 * A * DeltaT / d
tau2 = DeltaE / P2
results.append(("Q6a", P2, 60.0))
results.append(("Q6b", tau2, 22500.0))

# Q7: cryogenic G_th = 1.0e-7 W/K
k_c, A_c, d_c = 1.0e-4, 1.0e-6, 1.0e-3
G_c = k_c * A_c / d_c
results.append(("Q7", G_c, 1.0e-7))

# Q8: P_wall = G_c * DeltaT_c = 1.0e-10 W
DeltaT_c = 1.0e-3
P_wall = G_c * DeltaT_c
results.append(("Q8", P_wall, 1.0e-10))

n_match = 0
for cid, computed, expected in results:
    match = isclose(computed, expected)
    if match:
        n_match += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

total = len(results)
print(f"VERIFICATION SUMMARY: {total} claims, {n_match} match, {total - n_match} mismatch")
