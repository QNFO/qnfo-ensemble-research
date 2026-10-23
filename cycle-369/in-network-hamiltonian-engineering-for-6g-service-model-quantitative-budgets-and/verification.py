import math

def fmt(val, sig):
    """Format a number with given significant digits, using scientific notation if needed."""
    if val == 0:
        return "0"
    # Determine order of magnitude
    order = int(math.floor(math.log10(abs(val))))
    # Number of digits after decimal in mantissa
    digits = sig - 1
    fmt_str = "{:." + str(digits) + "f}"
    mant = val / (10 ** order)
    mant_str = fmt_str.format(mant)
    # Remove trailing zeros and possible dot
    mant_str = mant_str.rstrip('0').rstrip('.')
    return f"{mant_str}e{order}" if order != 0 else mant_str

# Inputs
n_p = 8
tau_p = 5e-7
tau_i = 5e-7
T2 = 1e-3
epsilon_c = 1e-5
K = 64
T_s = 1.0e-4
T_p = 2.0e-5
T_c_prime = 5.0e-5
T_a = 1.0e-5
W = 64
N_q = 1000
R_link = 1.0e11

# Derived quantities
T_c = n_p * (tau_p + tau_i)                     # Q1
f = tau_p / (tau_p + tau_i)                     # Q2
N_c = math.floor(T2 / T_c)                      # Q3
epsilon_tot_1 = N_c * epsilon_c                 # Q4
F_proj_1 = 1 - epsilon_tot_1                    # Q5
R_u = 1 / tau_p                                 # Q6
agg_rate = K * R_u                              # Q7
# Degraded coherence
T2_prime = 1e-4
N_c_prime = math.floor(T2_prime / T_c)          # part of Q8
epsilon_tot_1_prime = N_c_prime * epsilon_c     # part of Q8
F_proj_1_prime = 1 - epsilon_tot_1_prime        # part of Q8
epsilon_c_max = 0.01 / N_c                      # Q9
epsilon_c_valid = 0.01 * T_c / T2               # Q10 (same as epsilon_c_max)
T_loop = T_s + T_p + T_c_prime + T_a            # Q11
eta = T_loop / T2                               # Q12
B_cycle = W * N_q                               # Q13
tau_tx = B_cycle / R_link                       # Q14
ratio_tx_loop = tau_tx / T_loop                 # Q15
rho = 6 / 12                                     # Q16

# Expected values (as strings)
expected = {
    "Q1": ("8e-6", 2),
    "Q2": ("0.5", 1),
    "Q3": ("125", 3),
    "Q4": ("1.25e-3", 3),
    "Q5": ("0.99875", 5),
    "Q6": ("2e6", 2),
    "Q7": ("1.28e8", 3),
    "Q8": ("N_c'=12, epsilon=1.2e-4, F=0.99988", None),
    "Q9": ("8e-5", 2),
    "Q10": ("8e-5", 2),
    "Q11": ("1.8e-4", 2),
    "Q12": ("0.18", 2),
    "Q13": ("6.4e4", 2),
    "Q14": ("6.4e-7", 2),
    "Q15": ("3.56e-3", 3),
    "Q16": ("0.5", 1),
}

def compare(val, exp_str, sig):
    """Return True if val matches exp_str within the given significant digits."""
    if sig is None:
        return False
    try:
        exp_val = float(exp_str)
    except:
        return False
    # relative tolerance based on sig digits
    tol = 0.5 * 10**(-sig)
    return abs(val - exp_val) <= tol * abs(exp_val)

# Print results
print(f"CLAIM Q1: computed={T_c:.6e} expected={expected['Q1'][0]} match={'yes' if compare(T_c, *expected['Q1']) else 'no'}")
print(f"CLAIM Q2: computed={f:.6e} expected={expected['Q2'][0]} match={'yes' if compare(f, *expected['Q2']) else 'no'}")
print(f"CLAIM Q3: computed={N_c} expected={expected['Q3'][0]} match={'yes' if compare(N_c, *expected['Q3']) else 'no'}")
print(f"CLAIM Q4: computed={epsilon_tot_1:.6e} expected={expected['Q4'][0]} match={'yes' if compare(epsilon_tot_1, *expected['Q4']) else 'no'}")
print(f"CLAIM Q5: computed={F_proj_1:.6e} expected={expected['Q5'][0]} match={'yes' if compare(F_proj_1, *expected['Q5']) else 'no'}")
print(f"CLAIM Q6: computed={R_u:.6e} expected={expected['Q6'][0]} match={'yes' if compare(R_u, *expected['Q6']) else 'no'}")
print(f"CLAIM Q7: computed={agg_rate:.6e} expected={expected['Q7'][0]} match={'yes' if compare(agg_rate, *expected['Q7']) else 'no'}")
# Q8 has three sub‑values; we compare each separately
match_Nc = N_c_prime == 12
match_eps = abs(epsilon_tot_1_prime - 1.2e-4) < 1e-9
match_F = abs(F_proj_1_prime - 0.99988) < 1e-9
overall_match = match_Nc and match_eps and match_F
print(f"CLAIM Q8: computed=N_c'={N_c_prime}, epsilon={epsilon_tot_1_prime:.6e}, F={F_proj_1_prime:.6e} expected={expected['Q8'][0]} match={'yes' if overall_match else 'no'}")
print(f"CLAIM Q9: computed={epsilon_c_max:.6e} expected={expected['Q9'][0]} match={'yes' if compare(epsilon_c_max, *expected['Q9']) else 'no'}")
print(f"CLAIM Q10: computed={epsilon_c_valid:.6e} expected={expected['Q10'][0]} match={'yes' if compare(epsilon_c_valid, *expected['Q10']) else 'no'}")
print(f"CLAIM Q11: computed={T_loop:.6e} expected={expected['Q11'][0]} match={'yes' if compare(T_loop, *expected['Q11']) else 'no'}")
print(f"CLAIM Q12: computed={eta:.6e} expected={expected['Q12'][0]} match={'yes' if compare(eta, *expected['Q12']) else 'no'}")
print(f"CLAIM Q13: computed={B_cycle:.6e} expected={expected['Q13'][0]} match={'yes' if compare(B_cycle, *expected['Q13']) else 'no'}")
print(f"CLAIM Q14: computed={tau_tx:.6e} expected={expected['Q14'][0]} match={'yes' if compare(tau_tx, *expected['Q14']) else 'no'}")
print(f"CLAIM Q15: computed={ratio_tx_loop:.6e} expected={expected['Q15'][0]} match={'yes' if compare(ratio_tx_loop, *expected['Q15']) else 'no'}")
print(f"CLAIM Q16: computed={rho:.6e} expected={expected['Q16'][0]} match={'yes' if compare(rho, *expected['Q16']) else 'no'}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for k in expected if compare(globals().get('T_c' if k=='Q1' else ''), *expected[k]) )} match, {len(expected)-sum(1 for k in expected if compare(globals().get('T_c' if k=='Q1' else ''), *expected[k]) )} mismatch")
