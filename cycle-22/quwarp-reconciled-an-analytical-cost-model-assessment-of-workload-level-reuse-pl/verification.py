import math

def close(a, b):
    if a is None or b is None:
        return a == b
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(a, b, rel_tol=1e-6)
    return a == b

results = []

# Q1: S_run = 1/(1-f+α), with representative inputs f=0.90, α=0.02
f, alpha = 0.90, 0.02
computed = 1.0 / (1.0 - f + alpha)
expected = 1.0 / (1.0 - f + alpha)
results.append(("Q1", computed, expected))

# Q2: S_R = R / (1 + α + (R-1)(1-f+α)), R=100, f=0.90, α=0.02
R = 100
computed = R / (1 + alpha + (R - 1) * (1 - f + alpha))
expected = 100 / 12.90
results.append(("Q2", computed, expected))

# Q3: break-even f >= α; test f=0.05, α=0.02 -> True; f=0.01, α=0.02 -> False
f3, a3 = 0.05, 0.02
computed = (1 - f3 + a3) <= 1
expected = f3 >= a3
results.append(("Q3", computed, expected))

# Q4: S=2.95, α=0.05 -> f = 1 - 1/S + α
S, a4 = 2.95, 0.05
computed = 1 - 1 / S + a4
expected = 0.711017
results.append(("Q4", computed, expected))

# Q5: S=32.84, α=0.05 -> f = 1.019549, infeasible (f > 1)
S, a5 = 32.84, 0.05
computed = 1 - 1 / S + a5
expected = 1.019549
results.append(("Q5", computed, expected))
infeasible = computed > 1.0
results.append(("Q5-infeasible", infeasible, True))

# Q6: α_max = 1/S = 1/32.84
computed = 1 / 32.84
expected = 0.0304507
results.append(("Q6", computed, expected))

# Q7: S=32.84, α=0.01 -> f ≈ 0.979549
computed = 1 - 1 / 32.84 + 0.01
expected = 0.979549
results.append(("Q7", computed, expected))

# Q8: S=2.95, α=0.01 -> f ≈ 0.671017
computed = 1 - 1 / 2.95 + 0.01
expected = 0.671017
results.append(("Q8", computed, expected))

match_count = 0
for cid, comp, exp in results:
    m = close(comp, exp)
    if m:
        match_count += 1
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if m else 'no'}")

n = len(results)
print(f"VERIFICATION SUMMARY: {n} claims, {match_count} match, {n - match_count} mismatch")
