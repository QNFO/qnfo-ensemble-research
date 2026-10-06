import math

def close(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(float(a), float(b), rel_tol=1e-6)
    return a == b

results = []

def check(cid, computed, expected):
    match = "yes" if (expected is None or close(computed, expected)) else "no"
    results.append(match == "yes")
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1
L, R, e, c_t, a = 100, 60, 5, 1, 0.3
B = L - R + e
ratio = (c_t + e * a) / (B * a)
quot = math.log(ratio) / math.log(1 - a)
n_star = math.ceil(quot)
check("Q1", n_star, 5)

# Q2
dc4 = c_t + e * a - B * a * (1 - a) ** 4
check("Q2", round(dc4, 5), -0.74135)

# Q3
dc5 = c_t + e * a - B * a * (1 - a) ** 5
check("Q3", round(dc5, 6), 0.231055)

# Q4
C = R + (L - R) * (1 - a) ** 5 + c_t * 5 + e * (5 * a - (1 - a) ** 5)
check("Q4", round(C, 5), 78.38245)

# Fixed point setup
c, lam = 10, 0.5
ln7 = math.log(7)
Bf = 45

def n_of_a(av):
    r = (c_t + e * av) / (Bf * av)
    return math.ceil(math.log(r) / math.log(1 - av))

# Q5
n = 5
p = c + ln7 / ((n - 1) * lam)
av = 1 - math.exp(-lam * (p - c))
nn = n_of_a(av)
check("Q5", (round(p, 5), nn), (10.97296, 4))

# Q6
n = 4
p = c + ln7 / ((n - 1) * lam)
av = 1 - math.exp(-lam * (p - c))
nn = n_of_a(av)
check("Q6", (round(p, 5), nn), (11.29727, 3))

# Q7
n = 3
p = c + ln7 / ((n - 1) * lam)
av = 1 - math.exp(-lam * (p - c))
nn = n_of_a(av)
check("Q7", (round(p, 5), nn), (11.94591, 2))

# Q8
n = 2
p = c + ln7 / ((n - 1) * lam)
av = 1 - math.exp(-lam * (p - c))
nn = n_of_a(av)
check("Q8", (nn, round(p, 5)), (2, 13.89182))

m = sum(results)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {m} match, {len(results) - m} mismatch")
