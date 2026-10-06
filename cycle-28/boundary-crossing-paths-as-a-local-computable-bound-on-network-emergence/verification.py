import math

def match(a, b):
    if isinstance(a, float) or isinstance(b, float):
        return math.isclose(float(a), float(b), rel_tol=1e-6)
    return a == b

results = []

# Q1: length-1 walk count on C4 = 2*|E|
E = 4
q1 = 2 * E
results.append(("Q1", q1, 8))

# Q2: length-2 walk count = sum d_v^2, n=4, d=2
n, d = 4, 2
q2 = sum(d**2 for _ in range(n))
results.append(("Q2", q2, 16))

# Q3: per-length walk count via spectral formula: lambda0^k * (u0^T 1)^2
# C4 eigenvalues {2,0,-2,0}; u0 = (1/2)*1 so (u0^T 1)^2 = (4*(1/2))^2 = 4
lam0 = 2.0
u0 = [0.5] * 4
coef = sum(u0) ** 2
k = 3
q3 = lam0**k * coef
results.append(("Q3", q3, 4 * 2**k))

# Q4: W_k = 4*2^k for k=1,2,3
q4 = [4 * 2**kk for kk in (1, 2, 3)]
results.append(("Q4", q4, [8, 16, 32]))

# Q5: K2 has 2 walks of every length k>=1 (compute via adjacency powers)
# K2 adjacency [[0,1],[1,0]]; A^k 1 = 1 for all k>=1, so 1^T A^k 1 = 2
A = [[0, 1], [1, 0]]
def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(v))]
def walk_count(M, k):
    v = [1] * len(M)
    for _ in range(k):
        v = matvec(M, v)
    return sum(v)
q5 = [walk_count(A, kk) for kk in (1, 2, 3, 4)]
results.append(("Q5", q5, [2, 2, 2, 2]))

# Q6: combined per-length part observation = 2 + 2 = 4
q6 = 2 + 2
results.append(("Q6", q6, 4))

# Q7: D^(1) = 8 - 2 - 2
q7 = 8 - 2 - 2
results.append(("Q7", q7, 4))

# Q8: D^(2) = 16 - 2 - 2
q8 = 16 - 2 - 2
results.append(("Q8", q8, 12))

mism = 0
for cid, comp, exp in results:
    if isinstance(comp, list):
        ok = all(match(c, e) for c, e in zip(comp, exp))
        comp_s, exp_s = str(comp), str(exp)
    else:
        ok = match(comp, exp)
        comp_s, exp_s = str(comp), str(exp)
    if not ok:
        mism += 1
    print(f"CLAIM {cid}: computed={comp_s} expected={exp_s} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results)-mism} match, {mism} mismatch")
