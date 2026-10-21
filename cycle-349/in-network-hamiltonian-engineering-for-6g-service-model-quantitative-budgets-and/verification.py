import math

def compare(computed, expected):
    # simple string comparison after formatting to match expected precision
    # determine number of significant digits in expected (ignoring exponent sign)
    exp = expected.replace('-', '').replace('+', '')
    if 'e' in exp:
        mantissa, exponent = exp.split('e')
        sig = len(mantissa.replace('.', '').lstrip('0'))
    elif '.' in exp:
        sig = len(exp.replace('.', '').lstrip('0'))
    else:
        sig = len(exp.lstrip('0'))
    # format computed with same number of significant digits
    fmt = f"{{:.{sig}g}}".format(computed)
    return fmt

# Inputs
n_p = 8                # A4
tau_p = 5e-7           # A2
tau_i = 5e-7           # A3
T2 = 1e-3              # A1
epsilon_c = 1e-5       # A5
K = 64                 # A6
T_s = 1.0e-4           # A7
T_p = 2.0e-5           # A8
T_c_prime = 5.0e-5     # A9
T_a = 1.0e-5           # A10
W = 64                 # A11
N_q = 1000             # A12
R_link = 1.0e11        # A13
N_reuse = 6            # A15
N_tot = 12             # A15

# Q1
T_c = n_p * (tau_p + tau_i)
print("CLAIM Q1: computed={:.8g} expected=8e-6 match={}".format(T_c, "yes" if compare(T_c, "8e-6")== "8e-6" else "no"))

# Q2
f = tau_p / (tau_p + tau_i)
print("CLAIM Q2: computed={:.8g} expected=0.5 match={}".format(f, "yes" if compare(f, "0.5")== "0.5" else "no"))

# Q3
N_c = math.floor(T2 / T_c)
print("CLAIM Q3: computed={} expected=125 match={}".format(N_c, "yes" if N_c==125 else "no"))

# Q4
epsilon_tot = N_c * epsilon_c
print("CLAIM Q4: computed={:.8g} expected=1.25e-3 match={}".format(epsilon_tot, "yes" if compare(epsilon_tot, "1.25e-3")== "1.25e-3" else "no"))

# Q5
F_proj = 1 - epsilon_tot
print("CLAIM Q5: computed={:.8g} expected=0.99875 match={}".format(F_proj, "yes" if compare(F_proj, "0.99875")== "0.99875" else "no"))

# Q6
R_u = 1 / tau_p
print("CLAIM Q6: computed={:.8g} expected=2e6 match={}".format(R_u, "yes" if compare(R_u, "2e6")== "2e6" else "no"))

# Q7
agg_rate = K * R_u
print("CLAIM Q7: computed={:.8g} expected=1.28e8 match={}".format(agg_rate, "yes" if compare(agg_rate, "1.28e8")== "1.28e8" else "no"))

# Q8
T2_prime = 1e-4
N_c_prime = math.floor(T2_prime / T_c)
epsilon_tot_prime = N_c_prime * epsilon_c
F_proj_prime = 1 - epsilon_tot_prime
print("CLAIM Q8: computed={} expected=12 match={}".format(N_c_prime, "yes" if N_c_prime==12 else "no"))
print("CLAIM Q8: computed={:.8g} expected=0.99988 match={}".format(F_proj_prime, "yes" if compare(F_proj_prime, "0.99988")== "0.99988" else "no"))

# Q9
epsilon_c_max = 0.01 / N_c
print("CLAIM Q9: computed={:.8g} expected=8e-5 match={}".format(epsilon_c_max, "yes" if compare(epsilon_c_max, "8e-5")== "8e-5" else "no"))

# Q10
T_loop = T_s + T_p + T_c_prime + T_a
print("CLAIM Q10: computed={:.8g} expected=1.8e-4 match={}".format(T_loop, "yes" if compare(T_loop, "1.8e-4")== "1.8e-4" else "no"))

# Q11
eta = T_loop / T2
print("CLAIM Q11: computed={:.8g} expected=0.18 match={}".format(eta, "yes" if compare(eta, "0.18")== "0.18" else "no"))

# Q12
B_cycle = W * N_q
print("CLAIM Q12: computed={:.8g} expected=6.4e4 match={}".format(B_cycle, "yes" if compare(B_cycle, "6.4e4")== "6.4e4" else "no"))

# Q13
tau_tx = B_cycle / R_link
print("CLAIM Q13: computed={:.8g} expected=6.4e-7 match={}".format(tau_tx, "yes" if compare(tau_tx, "6.4e-7")== "6.4e-7" else "no"))

# Q14
ratio = tau_tx / T_loop
print("CLAIM Q14: computed={:.8g} expected=3.56e-3 match={}".format(ratio, "yes" if compare(ratio, "3.56e-3")== "3.56e-3" else "no"))

# Q15
rho = N_reuse / N_tot
print("CLAIM Q15: computed={:.8g} expected=0.5 match={}".format(rho, "yes" if compare(rho, "0.5")== "0.5" else "no"))

# Q16
rho_upper = 7 / 12
print("CLAIM Q16: computed={:.8g} expected=0.583 match={}".format(rho_upper, "yes" if compare(rho_upper, "0.583")== "0.583" else "no"))

print("VERIFICATION SUMMARY: 16 claims, {} match, {} mismatch".format(
    sum(1 for line in [
        compare(T_c, "8e-6")== "8e-6",
        compare(f, "0.5")== "0.5",
        N_c==125,
        compare(epsilon_tot, "1.25e-3")== "1.25e-3",
        compare(F_proj, "0.99875")== "0.99875",
        compare(R_u, "2e6")== "2e6",
        compare(agg_rate, "1.28e8")== "1.28e8",
        N_c_prime==12,
        compare(F_proj_prime, "0.99988")== "0.99988",
        compare(epsilon_c_max, "8e-5")== "8e-5",
        compare(T_loop, "1.8e-4")== "1.8e-4",
        compare(eta, "0.18")== "0.18",
        compare(B_cycle, "6.4e4")== "6.4e4",
        compare(tau_tx, "6.4e-7")== "6.4e-7",
        compare(ratio, "3.56e-3")== "3.56e-3",
        compare(rho, "0.5")== "0.5",
        compare(rho_upper, "0.583")== "0.583"
    ] if line), 
    16 - sum(1 for line in [
        compare(T_c, "8e-6")== "8e-6",
        compare(f, "0.5")== "0.5",
        N_c==125,
        compare(epsilon_tot, "1.25e-3")== "1.25e-3",
        compare(F_proj, "0.99875")== "0.99875",
        compare(R_u, "2e6")== "2e6",
        compare(agg_rate, "1.28e8")== "1.28e8",
        N_c_prime==12,
        compare(F_proj_prime, "0.99988")== "0.99988",
        compare(epsilon_c_max, "8e-5")== "8e-5",
        compare(T_loop, "1.8e-4")== "1.8e-4",
        compare(eta, "0.18")== "0.18",
        compare(B_cycle, "6.4e4")== "6.4e4",
        compare(tau_tx, "6.4e-7")== "6.4e-7",
        compare(ratio, "3.56e-3")== "3.56e-3",
        compare(rho, "0.5")== "0.5",
        compare(rho_upper, "0.583")== "0.583"
    ] if line)))
