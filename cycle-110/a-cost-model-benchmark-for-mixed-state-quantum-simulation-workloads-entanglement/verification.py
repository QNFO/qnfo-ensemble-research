import math

def log2(x):
    return math.log(x) / math.log(2)

def h2(mu):
    if mu in (0.0, 1.0):
        return 0.0
    return -mu * log2(mu) - (1 - mu) * log2(1 - mu)

claims = []

# Q1
computed = h2(0.5)
claims.append(("Q1", computed, 1.000000))

# Q2
computed = -0.75 * log2(0.75) - 0.25 * log2(0.25)
claims.append(("Q2", computed, 0.811278))

# Q3
computed = -0.9 * log2(0.9) - 0.1 * log2(0.1)
claims.append(("Q3", computed, 0.468996))

# Q4
computed = log2((1 - 0.5) / 0.5)
claims.append(("Q4", computed, 0.0))

# Q5
n = 10
computed = (4 ** n) / (2 ** n)
claims.append(("Q5", computed, 1024))

# Q6
computed = (2 ** n) * 16
claims.append(("Q6", computed, 16384))

# Q7
computed = (4 ** n) * 16
claims.append(("Q7", computed, 16777216))

# Q8
K = 21
computed = K * (4 ** n) * 16
claims.append(("Q8", computed, 352321536))

match_count = 0
for cid, computed, expected in claims:
    if expected is None:
        match = "no"
    else:
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

mismatch = len(claims) - match_count
print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {mismatch} mismatch")
