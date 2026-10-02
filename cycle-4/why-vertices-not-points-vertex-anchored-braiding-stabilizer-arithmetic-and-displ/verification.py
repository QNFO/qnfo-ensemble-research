import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: sphere size |S_n| = (p+1)*p^(n-1), test p=3, n=2
p, n = 3, 2
S = (p + 1) * p ** (n - 1)
results.append(check("Q1", S, 12))

# Q2: ball size V(N) = 1 + (p+1)(p^N - 1)/(p-1), test p=3, N=3
p, N = 3, 3
V = 1 + (p + 1) * (p ** N - 1) // (p - 1)
results.append(check("Q2", V, 53))

# Q3: edges in ball E(N) = V(N) - 1, test V(N)=53
VN = 53
E = VN - 1
results.append(check("Q3", E, 52))

# Q4: p=3, N=2: V(2)=17, E(2)=16
p, N = 3, 2
V2 = 1 + (p + 1) * (p ** N - 1) // (p - 1)
E2 = V2 - 1
results.append(check("Q4", (V2, E2), (17, 16)))

# Q5: p=3, N=3: V(3)=53, E(3)=52
p, N = 3, 3
V3 = 1 + (p + 1) * (p ** N - 1) // (p - 1)
E3 = V3 - 1
results.append(check("Q5", (V3, E3), (53, 52)))

# Q6: p=3, N=4: V(4)=161
p, N = 3, 4
V4 = 1 + (p + 1) * (p ** N - 1) // (p - 1)
results.append(check("Q6", V4, 161))

# Q7: asymptotic V(N) ~ ((p+1)/(p-1))*p^N; check ratio V(N)/p^N -> (p+1)/(p-1)
p = 3
N = 20
Vn = 1 + (p + 1) * (p ** N - 1) / (p - 1)
ratio = Vn / p ** N
target = (p + 1) / (p - 1)
results.append(check("Q7", round(ratio, 6), round(target, 6)))

# Q8: |SL_2(F_p)| = p(p^2-1), computed as (p+1)*p*(p-1), test p=3
p = 3
order = (p + 1) * p * (p - 1)
results.append(check("Q8", order, p * (p ** 2 - 1)))

m = sum(results)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {m} match, {len(results) - m} mismatch")
