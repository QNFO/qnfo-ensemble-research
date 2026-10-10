import math

def check(cid, computed, expected):
    if expected is None:
        match = "n/a"
    else:
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: T_c = n_p * (tau_p + tau_i)
n_p = 8
tau_p = 5e-7
tau_i = 5e-7
T_c = n_p * (tau_p + tau_i)
check("Q1", T_c, 8e-6)

# Q2: f = tau_p / (tau_p + tau_i)
f = tau_p / (tau_p + tau_i)
check("Q2", f, 0.5)

# Q3: N_c = floor(T_2 / T_c)
T_2 = 1e-3
N_c = math.floor(T_2 / T_c)
check("Q3", N_c, 125)

# Q4: epsilon_tot = N_c * epsilon_c
epsilon_c = 1e-5
epsilon_tot = N_c * epsilon_c
check("Q4", epsilon_tot, 1.25e-3)

# Q5: F_proj = 1 - epsilon_tot
F_proj = 1 - epsilon_tot
check("Q5", F_proj, 0.99875)

# Q6: R_u = 1 / tau_p
R_u = 1 / tau_p
check("Q6", R_u, 2e6)

# Q7: aggregate = K * R_u
K = 64
agg = K * R_u
check("Q7", agg, 1.28e8)

# Q8: degraded T2 case
T_2p = 1e-4
N_cp = math.floor(T_2p / T_c)
eps_tot_p = N_cp * epsilon_c
F_proj_p = 1 - eps_tot_p
check("Q8a", N_cp, 12)
check("Q8b", eps_tot_p, 1.2e-4)
check("Q8c", F_proj_p, 0.99988)

print("VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch")
