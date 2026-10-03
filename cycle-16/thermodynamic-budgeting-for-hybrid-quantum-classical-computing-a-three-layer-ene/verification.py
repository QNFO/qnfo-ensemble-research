import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: statistical resolution 1/sqrt(N_shots)
N_shots = 10000
q1 = 1 / math.sqrt(N_shots)
results.append(check("Q1", q1, 0.01))

# Q2: t_Q = N_shots * t_shot
t_shot = 1e-4
t_Q = N_shots * t_shot
results.append(check("Q2", t_Q, 1.0))

# Q3: t_cycle = t_Q + t_opt
t_opt = 0.05
t_cycle = t_Q + t_opt
results.append(check("Q3", t_cycle, 1.05))

# Q4: E_Q = P_cryo*t_cycle + P_q_op*t_Q
P_cryo = 25000.0
P_q_op = 1000.0
E_Q = P_cryo * t_cycle + P_q_op * t_Q
results.append(check("Q4", E_Q, 27250.0))

# Q5: E_IF = N_shots*(E_ctrl+E_ro) + P_sync*t_cycle
E_ctrl = 0.001
E_ro = 0.002
P_sync = 100.0
E_IF = N_shots * (E_ctrl + E_ro) + P_sync * t_cycle
results.append(check("Q5", E_IF, 135.0))

# Q6: E_C = P_host*t_opt + P_orch*t_cycle
P_host = 400.0
P_orch = 300.0
E_C = P_host * t_opt + P_orch * t_cycle
results.append(check("Q6", E_C, 335.0))

# Q7: E_cycle = E_Q + E_IF + E_C
E_cycle = E_Q + E_IF + E_C
results.append(check("Q7", E_cycle, 27720.0))

# Q8: quantum share = E_Q / E_cycle
share = E_Q / E_cycle
results.append(check("Q8", share, 27250.0 / 27720.0))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
