import math

def Ep(k, ed, ea):
    return k * k * ed + k * ea

claims = []

# Q1
k1 = math.floor(math.sqrt(3.7 / 0.01))
claims.append(("Q1", k1, 19))

# Q2
k2 = math.floor(math.sqrt(0.9 / 0.01))
claims.append(("Q2", k2, 9))

# Q3
v3 = Ep(19, 0.01, 0.001)
claims.append(("Q3", v3, 3.629))

# Q4
v4 = Ep(20, 0.01, 0.001)
claims.append(("Q4", v4, 4.020))

# Q5
v5 = Ep(9, 0.01, 0.001)
claims.append(("Q5", v5, 0.819))

# Q6
v6 = Ep(10, 0.01, 0.001)
claims.append(("Q6", v6, 1.010))

# Q7
k7 = math.ceil(math.log(1 / 1e-2) / math.log(2))
claims.append(("Q7", k7, 7))

# Q8
v8 = Ep(7, 0.01, 0.001)
claims.append(("Q8", v8, 0.497))

match_count = 0
for cid, computed, expected in claims:
    if isinstance(expected, int):
        ok = (computed == expected)
    else:
        ok = math.isclose(computed, expected, rel_tol=1e-6)
    if ok:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")
