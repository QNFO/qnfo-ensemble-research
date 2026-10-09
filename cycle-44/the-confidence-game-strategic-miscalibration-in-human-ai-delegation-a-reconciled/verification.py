import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: delta* = Delta(eps)*v1 / (lambda*G2bar) = 0.05/(0.3*0.25)
Delta_eps = 0.05
v1 = 1.0
lam = 0.3
G2bar = 0.25
q1 = (Delta_eps * v1) / (lam * G2bar)
results.append(("Q1", q1, 0.6666666666666666))

# Q2: gain = Delta(eps)*v1 = 0.05; cost = lambda*delta*G2bar = 0.3*0.5*0.25 = 0.0375
delta = 0.5
gain = Delta_eps * v1
cost = lam * delta * G2bar
results.append(("Q2", gain, 0.05))
results.append(("Q2b", cost, 0.0375))

# Q3: p* = (V_self - V_fail)/(V_succ - V_fail) = 40/100
V_self, V_fail, V_succ = 40.0, 0.0, 100.0
q3 = (V_self - V_fail) / (V_succ - V_fail)
results.append(("Q3", q3, 0.40))

# Q4: G1 = Delta_1 * (60 - 40) = 0.2*20
Delta_1 = 0.2
deleg_EV = 0.6 * 100
self_val = 40.0
q4 = Delta_1 * (deleg_EV - self_val)
results.append(("Q4", q4, 4.0))

# Q5: delta*q <= G1/20 = 0.20, so delta <= 0.20/q = 0.40 with q=0.5
G1 = 4.0
surplus2 = 20.0
q_detect = 0.5
ratio = G1 / surplus2
q5 = ratio / q_detect
results.append(("Q5", q5, 0.40))

# Q6: Pi_honest = lambda*(p*|0.6-1| + (1-p)*|0.6-0|) = 5*(0.6*0.4+0.4*0.6)
p = 0.6
lam5 = 5.0
pi_honest = lam5 * (p * abs(0.6 - 1) + (1 - p) * abs(0.6 - 0))
results.append(("Q6", pi_honest, 2.4))

# Q7: Pi_inflated = lambda*(p*0 + (1-p)*1) = 5*0.4
pi_inflated = lam5 * (p * 0 + (1 - p) * 1)
results.append(("Q7", pi_inflated, 2.0))

# Q8: U_honest = 10 - 2.4 = 7.6; U_inflated = 10 - 2.0 = 8.0
R = 10.0
u_honest = R - pi_honest
u_inflated = R - pi_inflated
results.append(("Q8a", u_honest, 7.6))
results.append(("Q8b", u_inflated, 8.0))

n_match = 0
n_total = 0
for cid, computed, expected in results:
    n_total += 1
    match = close(computed, expected) if expected is not None else None
    if match:
        n_match += 1
    exp_str = f"{expected}" if expected is not None else "none"
    print(f"CLAIM {cid}: computed={computed} expected={exp_str} match={'yes' if match else 'no'}")

n_mismatch = n_total - n_match
print(f"VERIFICATION SUMMARY: {n_total} claims, {n_match} match, {n_mismatch} mismatch")
