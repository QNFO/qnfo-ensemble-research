import math

def round_sig(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Constants
c = 2.9979e10  # cm/s

# Expected values as strings
expected = {
    "Q1": "100",
    "Q2": "9",
    "Q3": "1.6952e12",
    "Q4": "0.5899",
    "Q5": "0.001",
    "Q6": "0.999001",
    "Q7": "0.1695",
    "Q8": "1.6953",
    "Q9": "4.0",
    "Q10": "7.5345e11",
    "Q11": "1.3272",
    "Q12": "0.0753",
    "Q13": "0.7535",
    "Q14": "16.67",
    "Q15": "3.1394e12",
    "Q16": "0.3185",
}

# Computations
results = {}

# Q1
Gamma_star = 100.0
results["Q1"] = Gamma_star

# Q2
V = 30.0
Delta = 100.0
k_star = V**2 / Delta
results["Q2"] = k_star

# Q3
omega_star = 2 * math.pi * c * k_star
results["Q3"] = omega_star

# Q4
tau_T = 1.0 / omega_star * 1e12  # convert s to ps
results["Q4"] = tau_T

# Q5
tau_e_ps = 1e3  # 1 ns = 1000 ps
gamma_rec = 1.0 / tau_e_ps
results["Q5"] = gamma_rec

# Q6
kappa = 1.0
eta = kappa / (kappa + gamma_rec)
results["Q6"] = eta

# Q7
tau_B_fast = 0.1
R_fast = tau_B_fast / tau_T
results["Q7"] = R_fast

# Q8
tau_B_slow = 1.0
R_slow = tau_B_slow / tau_T
results["Q8"] = R_slow

# Q9
V20 = 20.0
k_star_20 = V20**2 / Delta
results["Q9"] = k_star_20

# Q10
omega_star_20 = 2 * math.pi * c * k_star_20
results["Q10"] = omega_star_20

# Q11
tau_T_20 = 1.0 / omega_star_20 * 1e12
results["Q11"] = tau_T_20

# Q12
R_fast_20 = tau_B_fast / tau_T_20
results["Q12"] = R_fast_20

# Q13
R_slow_20 = tau_B_slow / tau_T_20
results["Q13"] = R_slow_20

# Q14
V50 = 50.0
Delta150 = 150.0
k_star_50 = V50**2 / Delta150
results["Q14"] = k_star_50

# Q15
omega_star_50 = 2 * math.pi * c * k_star_50
results["Q15"] = omega_star_50

# Q16
tau_T_50 = 1.0 / omega_star_50 * 1e12
results["Q16"] = tau_T_50

# Helper to decide match
def matches(comp, exp_str):
    # Determine number of significant digits in expected string
    if "e" in exp_str:
        base, exp = exp_str.split("e")
        sig = len(base.replace(".", "").replace("-", ""))
    elif "." in exp_str:
        sig = len(exp_str.replace(".", "").replace("-", ""))
    else:
        sig = len(exp_str.replace("-", ""))
    comp_rounded = round_sig(comp, sig)
    try:
        exp_val = float(exp_str)
    except ValueError:
        # handle cases like "1.6952e12"
        exp_val = float(exp_str.replace("e", "E"))
    return abs(comp_rounded - exp_val) < 1e-12 * max(1.0, abs(exp_val))

# Print results
for qid in sorted(expected.keys(), key=lambda x: int(x[1:])):
    comp = results[qid]
    exp_str = expected[qid]
    match = "yes" if matches(comp, exp_str) else "no"
    # Use scientific notation for large numbers, otherwise plain
    if abs(comp) >= 1e4 or abs(comp) < 1e-3:
        comp_str = f"{comp:.8e}"
    else:
        comp_str = f"{comp:.8g}"
    print(f"CLAIM {qid}: computed={comp_str} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if matches(results[q], expected[q]))} match, {len(expected) - sum(1 for q in expected if matches(results[q], expected[q]))} mismatch")
