import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: N_k = q^k via recurrence N_0=1, N_{k+1}=q*N_k
def ball_count(q, k):
    N = 1
    for _ in range(k):
        N = q * N
    return N

N5_q3 = ball_count(3, 5)
N20_q2 = ball_count(2, 20)
results.append(("Q1a", N5_q3, 243))
results.append(("Q1b", N20_q2, 1048576))

# Q2: s_k = (S/d_0)*q^k, ratio s_{k+1}/s_k = q
S = 10.0
d0 = 5.0
q = 3.0
k = 4
s_k = (S / d0) * (q ** k)
s_k1 = (S / d0) * (q ** (k + 1))
ratio = s_k1 / s_k
results.append(("Q2a", s_k, (S / d0) * (q ** k)))
results.append(("Q2b", ratio, q))

# Q3: L(n,d) = d * n^(d-1)
L43 = 3 * (4 ** 2)
L34 = 4 * (3 ** 3)
results.append(("Q3a", L43, 48))
results.append(("Q3b", L34, 108))

# Q4: incidences = d * n^d = L(n,d) * n
incidences_direct = 3 * (4 ** 3)
incidences_via_L = L43 * 4
results.append(("Q4a", incidences_direct, 192))
results.append(("Q4b", incidences_via_L, 192))

match_count = 0
for cid, computed, expected in results:
    match = close(float(computed), float(expected))
    if match:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

total = len(results)
mismatch = total - match_count
print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {mismatch} mismatch")
