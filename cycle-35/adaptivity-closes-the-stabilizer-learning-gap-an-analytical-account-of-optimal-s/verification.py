import math

def check(id, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {id}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: log2 N_n = n^2/2 + O(n); at n=100, log2 N_100 = 5000
n = 100
log2N = n**2 / 2
results.append(check("Q1", log2N, 5000))

# Q2: m_floor(100) >= log2 N_100 / b_copy = 5000/100 = 50
b_copy = n
m_floor = log2N / b_copy
results.append(check("Q2", m_floor, 50))

# Q3: m_na_tight(100) = c * 100^2; with c=1 -> 10^4
c = 1.0
m_na = c * n**2
results.append(check("Q3", m_na, 1e4))

# Q4: ratio >= (10^4 c)/(C*100) = 100c/C; with c=1, C=1 -> 100
C = 1.0
ratio = (c * n**2) / (C * n)
results.append(check("Q4", ratio, 100))

# Q5: m_test = n - k + 1/eps = 100 - 10 + 100 = 190
k = 10
eps = 0.01
m_test = n - k + 1/eps
results.append(check("Q5", m_test, 190))

# Q6: k=0 -> 200; k=100 -> 100
m_test_k0 = n - 0 + 1/eps
m_test_k100 = n - 100 + 1/eps
results.append(check("Q6a", m_test_k0, 200))
results.append(check("Q6b", m_test_k100, 100))

# Q7: eps* = 1/n = 0.01
eps_star = 1/n
results.append(check("Q7", eps_star, 0.01))

# Q8: n * 2^r: r=5 -> 3200; r=10 -> 102400
r5 = n * 2**5
r10 = n * 2**10
results.append(check("Q8a", r5, 3200))
results.append(check("Q8b", r10, 102400))

N = len(results)
M = sum(results)
K = N - M
print(f"VERIFICATION SUMMARY: {N} claims, {M} match, {K} mismatch")
