import math

def phi(n):
    result = n
    m = n
    d = 2
    while d * d <= m:
        if m % d == 0:
            while m % d == 0:
                m //= d
            result -= result // d
        d += 1
    if m > 1:
        result -= result // m
    return result

claims = []

# Q1: sum of totients k=1..20
s = sum(phi(k) for k in range(1, 21))
claims.append(("Q1", s, 128))

# Q2: Farey order 20 cardinality
f20 = 1 + s
claims.append(("Q2", f20, 129))

# Q3: definable fraction at depth 20
f_20 = 129 / 1048576
claims.append(("Q3", f_20, 1.23024e-4))

# Q4: programs of length at most 100
prog = sum(2**k for k in range(0, 101))
claims.append(("Q4", prog, 2**101 - 1))

# Q5: total covering length = eps * sum 2^-j (use eps=1 for the series value)
eps = 1.0
total = sum(2 * eps * 2**(-j - 1) for j in range(1, 10000))
claims.append(("Q5", total, eps))

# Q6: upper bound (1 + n^2)/2^n at n=20
ub = (1 + 20**2) / 2**20
claims.append(("Q6", ub, 401 / 1048576))

# Q7: regular-tree rays p=2, n=4
r7 = 2 * 3**(4 - 1)
claims.append(("Q7", r7, 54))

# Q8: regular-tree rays p=2, n=8
r8 = 2 * 3**(8 - 1)
claims.append(("Q8", r8, 4374))

match_count = 0
for cid, computed, expected in claims:
    if isinstance(computed, float) or isinstance(expected, float):
        ok = math.isclose(float(computed), float(expected), rel_tol=1e-6)
    else:
        ok = computed == expected
    if ok:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")
