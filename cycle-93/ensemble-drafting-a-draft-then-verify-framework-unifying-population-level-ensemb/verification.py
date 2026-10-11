import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1
alpha, k = 0.8, 7
val = (1 - alpha**k) / (1 - alpha)
results.append(("Q1", val, 3.951424))

# Q2
rho, nu = 0.1, 1
val = ((1 - alpha**k) / (1 - alpha)) / (rho * k + nu)
results.append(("Q2", val, 2.324367))

# Q3: discrete optimum over k in 4..9
best_k, best_s = None, -1.0
for kk in range(4, 10):
    s = ((1 - alpha**kk) / (1 - alpha)) / (rho * kk + nu)
    if s > best_s:
        best_s, best_k = s, kk
results.append(("Q3", best_s, 2.324367))
print(f"CLAIM Q3: computed={best_s:.6f} expected=2.324367 match={'yes' if isclose(best_s, 2.324367) and best_k == 7 else 'no'} (k*={best_k})")

# Q4: single weak drafter alpha=0.5
alpha_w = 0.5
best_k, best_s = None, -1.0
for kk in range(1, 20):
    s = ((1 - alpha_w**kk) / (1 - alpha_w)) / (rho * kk + nu)
    if s > best_s:
        best_s, best_k = s, kk
results.append(("Q4", best_s, 1.346154))
print(f"CLAIM Q4: computed={best_s:.6f} expected=1.346154 match={'yes' if isclose(best_s, 1.346154) and best_k == 3 else 'no'} (k*={best_k})")

# Q5
val = 1 - (1 - 0.5)**2
results.append(("Q5", val, 0.75))

# Q6: two-drafter ensemble
alpha2, rho2 = 0.75, 0.2
best_k, best_s = None, -1.0
for kk in range(1, 20):
    s = ((1 - alpha2**kk) / (1 - alpha2)) / (rho2 * kk + nu)
    if s > best_s:
        best_s, best_k = s, kk
results.append(("Q6", best_s, 1.525391))
print(f"CLAIM Q6: computed={best_s:.6f} expected=1.525391 match={'yes' if isclose(best_s, 1.525391) and best_k == 5 else 'no'} (k*={best_k})")

# Q7
val = 1.525391 / 1.346154
results.append(("Q7", val, 1.133147))

# Q8
val = 1 - (1 - 0.6)**3
results.append(("Q8", val, 0.936))

for cid, comp, exp in results:
    match = "yes" if isclose(comp, exp) else "no"
    print(f"CLAIM {cid}: computed={comp:.6f} expected={exp} match={match}")

n = len(results)
m = sum(1 for _, c, e in results if isclose(c, e))
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
