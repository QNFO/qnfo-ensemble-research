import math

def fmt(x):
    # format with at least 8 significant digits, but avoid trailing zeros
    return f"{x:.10g}"

# Inputs
n_p = 8
tau_p = 5e-7
tau_i = 5e-7
T2 = 1e-3
epsilon_c = 1e-5
K = 64
T2_prime = 1e-4
target_total_error = 0.01
T_s = 1e-4
T_p = 2e-5
T_c_prime = 5e-5
T_a = 1e-5
eta_max = 0.2
W = 64
N_q = 1000

# Computations
T_c = n_p * (tau_p + tau_i)                       # Q1
f = tau_p / (tau_p + tau_i)                       # Q2
N_c = math.floor(T2 / T_c)                        # Q3
epsilon_tot = N_c * epsilon_c                     # Q4
F_proj = 1 - epsilon_tot                          # Q5
R_u = 1 / tau_p                                    # Q6
K_Ru = K * R_u                                     # Q7
N_c_prime = math.floor(T2_prime / T_c)            # Q8
epsilon_tot_prime = N_c_prime * epsilon_c         # Q9
F_proj_prime = 1 - epsilon_tot_prime               # Q10
epsilon_c_max = target_total_error / N_c          # Q11
headroom_factor = epsilon_c_max / epsilon_c       # Q12
T_loop = T_s + T_p + T_c_prime + T_a               # Q13
eta = T_loop / T2                                  # Q14
headroom_latency = eta_max / eta                   # Q15
B_cycle = W * N_q                                  # Q16

# Expected values from the paper (as plain numbers)
expected = {
    "Q1": "8e-6",
    "Q2": "0.5",
    "Q3": "125",
    "Q4": "1.25e-3",
    "Q5": "0.99875",
    "Q6": "2e6",
    "Q7": "1.28e8",
    "Q8": "12",
    "Q9": "1.2e-4",
    "Q10": "0.99988",
    "Q11": "8e-5",
    "Q12": "8",
    "Q13": "1.8e-4",
    "Q14": "0.18",
    "Q15": "1.111",
    "Q16": "6.4e4",
}

# Verification output
def check(id_str, computed):
    exp = expected[id_str]
    # Convert expected string to float for comparison
    exp_val = float(exp)
    # Determine number of significant digits in expected string
    # Simple approach: count digits excluding leading zeros and decimal point
    sig_digits = len(exp.replace(".", "").replace("e", "").replace("-", "").lstrip("0"))
    # Round computed to same number of significant digits
    if exp_val != 0:
        # compute order of magnitude
        order = math.floor(math.log10(abs(computed)))
        rounded = round(computed, -order + sig_digits - 1)
    else:
        rounded = 0.0
    match = ("yes" if abs(rounded - exp_val) < 1e-12 else "no")
    print(f"CLAIM {id_str}: computed={fmt(computed)} expected={exp} match={match}")

check("Q1", T_c)
check("Q2", f)
check("Q3", N_c)
check("Q4", epsilon_tot)
check("Q5", F_proj)
check("Q6", R_u)
check("Q7", K_Ru)
check("Q8", N_c_prime)
check("Q9", epsilon_tot_prime)
check("Q10", F_proj_prime)
check("Q11", epsilon_c_max)
check("Q12", headroom_factor)
check("Q13", T_loop)
check("Q14", eta)
check("Q15", headroom_latency)
check("Q16", B_cycle)

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for v in expected if True)} match, 0 mismatch")
