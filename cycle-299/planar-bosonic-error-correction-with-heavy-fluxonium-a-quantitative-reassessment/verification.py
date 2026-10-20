import math

# Inputs
T1_bf = 451e-6          # seconds
sigma_T1_bf = 70e-6     # seconds (unused for central values)
F = 1.59
T_cyc = 10e-6           # seconds
T1_tm = 30e-6           # seconds
eta = 0.1

# Computations
Gamma_bf = 1.0 / T1_bf
removed = 1.0 - 1.0 / F
residual = 1.0 / F
p_flx = 1.0 - math.exp(-Gamma_bf * T_cyc)
Gamma_tm = 1.0 / T1_tm
p_tm = 1.0 - math.exp(-Gamma_tm * T_cyc)
ratio_per_cycle = p_tm / p_flx
ratio_rates = T1_bf / T1_tm
Gamma_anc = eta * Gamma_bf
T_L1 = 1.0 / Gamma_anc
adv_lower = 5.0 * F
adv_upper = 40.0 * F

# Helper for rounding to match expected significant digits
def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Expected values (central) for comparison
expected = {
    "Q1": 2.22e3,
    "Q2": 0.371,
    "Q3": 0.629,
    "Q4": 0.0219,
    "Q5": 0.2835,
    "Q6": 12.9,
    "Q7": 15.0,
    "Q8": 221.7,
    "Q9": 4.51e-3,
    "Q10": 8.0,
    "Q11": 64.0,
}

# Rounding to match expected precision
computed = {
    "Q1": round_sig(Gamma_bf, 3),          # 3 sig figs
    "Q2": round(Gamma_bf, 0),  # placeholder not used
    "Q2": round(removed, 3),               # 3 decimal places
    "Q3": round(residual, 3),              # 3 decimal places
    "Q4": round(p_flx, 4),                 # 4 decimal places
    "Q5": round(p_tm, 4),                  # 4 decimal places
    "Q6": round(ratio_per_cycle, 1),       # 1 decimal place
    "Q7": round(ratio_rates, 1),           # 1 decimal place
    "Q8": round(Gamma_anc, 1),             # 1 decimal place
    "Q9": round(T_L1, 5),                  # 5 significant digits (0.004508)
    "Q10": round(adv_lower, 1),            # 1 decimal place
    "Q11": round(adv_upper, 0),            # integer
}

# Function to format numbers consistently
def fmt(x):
    if isinstance(x, float):
        # Use scientific notation if magnitude is large or small
        if abs(x) >= 1e4 or (0 < abs(x) < 1e-3):
            return f"{x:.3e}"
        else:
            return f"{x}"
    return str(x)

# Print results
for qid in sorted(expected.keys()):
    comp = computed[qid]
    exp = expected[qid]
    match = "yes" if round(comp, 10) == round(exp, 10) else "no"
    print(f"CLAIM {qid}: computed={fmt(comp)} expected={fmt(exp)} match={match}")
