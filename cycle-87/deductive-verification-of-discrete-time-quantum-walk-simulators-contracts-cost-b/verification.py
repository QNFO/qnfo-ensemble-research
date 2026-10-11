import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

# Q1: d_t = 2*(2*t+1), t=1000
t1 = 1000
q1 = 2 * (2 * t1 + 1)
print(f"CLAIM Q1: computed={q1} expected=4002 match={'yes' if isclose(q1, 4002) else 'no'}")

# Q2: d_t = 2*(2*t+1), t=10^6
t2 = 10**6
q2 = 2 * (2 * t2 + 1)
print(f"CLAIM Q2: computed={q2} expected=4000002 match={'yes' if isclose(q2, 4000002) else 'no'}")

# Q3: dense unitarity cost = d_t^3, d_t=4002
d = 4002
q3 = d**3
print(f"CLAIM Q3: computed={q3} expected=64096048008 match={'yes' if isclose(q3, 64096048008) else 'no'}")

# Q4: T_dense = d_t^3 / r, r=1e9
r = 1e9
q4 = q3 / r
print(f"CLAIM Q4: computed={q4} expected=64.096048008 match={'yes' if isclose(q4, 64.096048008) else 'no'}")

# Q5: sparse cost = k^2 * d_t^2, k=2
k = 2
q5 = k**2 * d**2
print(f"CLAIM Q5: computed={q5} expected=64064016 match={'yes' if isclose(q5, 64064016) else 'no'}")

# Q6: speedup = d_t / 4
q6 = d / 4
print(f"CLAIM Q6: computed={q6} expected=1000.5 match={'yes' if isclose(q6, 1000.5) else 'no'}")

# Q7: row-norm check = 8*d_t
q7 = 8 * d
print(f"CLAIM Q7: computed={q7} expected=32016 match={'yes' if isclose(q7, 32016) else 'no'}")

# Q8: constraint count = d_t*(d_t+1)
q8 = d * (d + 1)
print(f"CLAIM Q8: computed={q8} expected=16020006 match={'yes' if isclose(q8, 16020006) else 'no'}")

matches = sum([
    isclose(q1, 4002), isclose(q2, 4000002), isclose(q3, 64096048008),
    isclose(q4, 64.096048008), isclose(q5, 64064016), isclose(q6, 1000.5),
    isclose(q7, 32016), isclose(q8, 16020006)
])
print(f"VERIFICATION SUMMARY: 8 claims, {matches} match, {8 - matches} mismatch")
