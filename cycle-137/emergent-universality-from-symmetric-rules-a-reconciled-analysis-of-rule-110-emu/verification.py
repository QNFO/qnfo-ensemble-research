import math

def fmt(x):
    return f"{x:.10g}"

claims = []

# Q1
a, b, eps = 1.0, 1.0, 1e-2
rho = math.sqrt(a * eps / b)
claims.append(("Q1", rho, "0.1"))

# Q2
eps = 1e-4
rho = math.sqrt(a * eps / b)
claims.append(("Q2", rho, "0.01"))

# Q3
eps = 0.25
rho = math.sqrt(a * eps / b)
claims.append(("Q3", rho, "0.5"))

# Q4
a, b, eps = 1.0, 1.0, 1e-2
tau = 1.0 / math.sqrt(a * b * eps)
claims.append(("Q4", tau, "10"))

# Q5
eps = 1e-4
tau = 1.0 / math.sqrt(a * b * eps)
claims.append(("Q5", tau, "100"))

# Q6
v, T = 1.0, 1000.0
rho0 = 1.0 / (2 * v * T)
claims.append(("Q6", rho0, "0.0005"))

# Q7
a, b, Nc = 1.0, 1.0, 100.0
eps_max = b / (a * Nc ** 2)
claims.append(("Q7", eps_max, "0.0001"))

# Q8
lam = 3.0
eps_max_corr = b / (a * Nc ** 2 * lam)
claims.append(("Q8", eps_max_corr, "0.00003333333333"))

match_count = 0
for cid, computed, expected in claims:
    match = "yes" if abs(computed - float(expected)) < 1e-12 else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={fmt(computed)} expected={expected} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")
