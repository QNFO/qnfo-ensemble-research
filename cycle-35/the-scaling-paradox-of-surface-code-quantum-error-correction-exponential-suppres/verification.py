import math

def close(a, b):
    if b is None:
        return False
    if isinstance(a, float) or isinstance(b, float):
        return math.isclose(a, b, rel_tol=1e-6)
    return a == b

def compute_d(p_L, p, p_th, A):
    return 2 * math.log10(p_L / A) / math.log10(p / p_th) - 1

def compute_n(d):
    return 2 * d**2 - 1

claims = []

# Q1
d = compute_d(1e-12, 1e-3, 1e-2, 0.1)
claims.append(("Q1", d, 21.0))

# Q2
d = compute_d(1e-12, 1e-4, 1e-2, 0.1)
claims.append(("Q2", d, 10.0))

# Q3
d = compute_d(1e-6, 1e-3, 1e-2, 0.1)
claims.append(("Q3", d, 9.0))

# Q4
d = compute_d(1e-15, 1e-3, 1e-2, 0.1)
claims.append(("Q4", d, 27.0))

# Q5
n = compute_n(21)
claims.append(("Q5", n, 881))

# Q6
n = compute_n(10)
claims.append(("Q6", n, 199))

# Q7
n = compute_n(9)
claims.append(("Q7", n, 161))

# Q8
n = compute_n(27)
claims.append(("Q8", n, 1457))

match = 0
mismatch = 0
for cid, comp, exp in claims:
    ok = close(float(comp), float(exp))
    if ok:
        match += 1
    else:
        mismatch += 1
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match} match, {mismatch} mismatch")
