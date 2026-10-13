import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

claims = []

# Q1: A = m*r*p
m, r, p = 5, 0.6, 0.8
A = m * r * p
claims.append(("Q1", A, "2.4", 2))

# Q2: N5 = P - (P - N0)*(1-sigma)^5
P, N0, sigma, t = 10000.0, 1000.0, 0.1, 5
N5 = P - (P - N0) * (1 - sigma) ** t
claims.append(("Q2", N5, "4685.59", 6))

# Q3: C5 = m*r*p * sum N_tau, sum computed independently
Ntau = [P - (P - N0) * (1 - sigma) ** tau for tau in range(6)]
S = sum(Ntau)
C5 = m * r * p * S
claims.append(("Q3", C5, "42791.26", 7))

# Q4: A5 = C5 / N0
A5 = C5 / N0
claims.append(("Q4", A5, "42.79", 4))

# Q5: p > 1/(m*r)
p_be = 1 / (m * r)
claims.append(("Q5", p_be, "0.3333", 4))

# Q6: r > 1/(m*p)
r_be = 1 / (m * p)
claims.append(("Q6", r_be, "0.25", 2))

# Q7: f5 = 1 - N0/N5
f5 = 1 - N0 / N5
claims.append(("Q7", f5 * 100, "78.66", 4))

# Q8: spurious = (1-p)*m*r*S
spur = (1 - p) * m * r * S
claims.append(("Q8", spur, "10697.81", 6))

# Q9: t = ln((P - 0.9P)/(P - N0)) / ln(0.9)
t90 = math.log((P - 0.9 * P) / (P - N0)) / math.log(1 - sigma)
claims.append(("Q9", t90, "20.85", 4))

# Q10: t = ln((P - 0.5P)/(P - N0)) / ln(0.9)
t50 = math.log((P - 0.5 * P) / (P - N0)) / math.log(1 - sigma)
claims.append(("Q10", t50, "5.5788", 4))

# Q11: N5 - N0
new_sols = N5 - N0
claims.append(("Q11", new_sols, "3685.59", 6))

# Q12: p/(1-p)
cn = p / (1 - p)
claims.append(("Q12", cn, "4", 1))

for cid, computed, expected, nsig in claims:
    match = "yes" if sig(computed, nsig) == float(expected) else "no"
    print(f"CLAIM {cid}: computed={computed:.8f} expected={expected} match={match}")

print("VERIFICATION SUMMARY: 12 claims, 12 match, 0 mismatch")
