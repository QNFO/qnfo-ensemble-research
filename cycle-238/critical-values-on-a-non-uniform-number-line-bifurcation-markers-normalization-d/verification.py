import math

# Define placeholder values for symbolic parameters
m = g = l = L = A = B = L_ang = 1.0  # arbitrary non-zero values

# Expected values as strings (exact as stated in the paper)
expected = {
    "Q1": "2",
    "Q2": "1",
    "Q3": "4",               # interpreted as numeric after setting m=g=l=1
    "Q4": "1",
    "Q5": "1.333",
    "Q6": "4",
    "Q7": "-1",
    "Q8": "1",
    "Q9": "7.29927e-3",
    "Q10": "137",
    "Q11": "2.14",
    "Q12": "1024",
    "Q13": "1.2676506e30",
    "Q14": "0.693147",
    "Q15": "137"
}

def format_match(computed, exp_str):
    """Return 'yes' if computed matches expected within the precision implied by exp_str."""
    # Determine number of significant digits in expected string (ignoring exponent notation)
    if 'e' in exp_str or 'E' in exp_str:
        # scientific notation: compare as float with same number of digits before 'e'
        exp_val = float(exp_str)
        return "yes" if abs(computed - exp_val) / exp_val < 1e-6 else "no"
    elif '.' in exp_str:
        # decimal representation: round computed to same number of decimal places
        places = len(exp_str.split('.')[1])
        return "yes" if round(computed, places) == float(exp_str) else "no"
    else:
        # integer representation
        return "yes" if int(round(computed)) == int(exp_str) else "no"

# Compute each claim
results = {}

# Q1
epsilon_sep = (2 * m * g * L) / (m * g * L)
results["Q1"] = epsilon_sep

# Q2
tilde_eps = (2 * m * g * L) / (2 * m * g * L)
results["Q2"] = tilde_eps

# Q3
delta_E = 4 * m * g * l
results["Q3"] = delta_E

# Q4
epsilon_c = delta_E / (4 * m * g * l)
results["Q4"] = epsilon_c

# Q5
V_hang_abs = 3 * m * g * l
val_Q5 = delta_E / V_hang_abs
results["Q5"] = val_Q5

# Q6
val_Q6 = delta_E / (m * g * l)
results["Q6"] = val_Q6

# Q7
beta_c = (2 * m * (-L_ang**2 / (2 * m))) / (L_ang**2)
results["Q7"] = beta_c

# Q8
tilde_beta = -beta_c
results["Q8"] = tilde_beta

# Q9
alpha = 1.0 / 137.0
results["Q9"] = alpha

# Q10
inv_alpha = 1.0 / alpha
results["Q10"] = inv_alpha

# Q11
log10_inv = math.log10(inv_alpha)
results["Q11"] = log10_inv

# Q12
two_pow_10 = 2**10
results["Q12"] = two_pow_10

# Q13
two_pow_100 = 2**100
results["Q13"] = two_pow_100

# Q14
mu_log = abs(math.log(2.0 / 1.0))
results["Q14"] = mu_log

# Q15
factor_alpha = 1.0 / alpha
results["Q15"] = factor_alpha

# Print verification lines
for qid in sorted(expected.keys(), key=lambda x: int(x[1:])):  # Q1, Q2, ...
    comp = results[qid]
    exp = expected[qid]
    # Format computed value with sufficient precision
    if isinstance(comp, float):
        comp_str = f"{comp:.8g}"
    else:
        comp_str = str(comp)
    match = format_match(comp, exp)
    print(f"CLAIM {qid}: computed={comp_str} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if format_match(results[q], expected[q])=='yes')} match, {sum(1 for q in expected if format_match(results[q], expected[q])=='no')} mismatch")
