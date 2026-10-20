import math

# Constants
k_B = 8.617333e-5          # eV/K
R = 8.314                  # J·mol⁻¹·K⁻¹

# Expected values (as strings)
expected = {
    "Q1": "8.62e-5",
    "Q2": "8.62e-6",
    "Q3": "1.72e-3",
    "Q4": "10.0",
    "Q5": "2.3993",
    "Q6": "0.439",
    "Q7": "3.65",
    "Q8": "0.4168",
    "Q9": "8.32",
    "Q10": "0.9",
    "Q11": "0.05",
    "Q12": "11.1",
    "Q13": "1873.15",
    "Q14": "0.16142",
    "Q15": "1.33e-3"
}

def sig_round(value, sig):
    """Round value to given number of significant figures."""
    if value == 0:
        return 0.0
    else:
        return round(value, sig - int(math.floor(math.log10(abs(value)))) - 1)

def compare(comp, exp_str):
    """Compare computed value to expected string."""
    # Convert expected string to float (handle scientific notation)
    exp_val = float(exp_str.replace('e', 'E'))
    # Determine number of significant digits in expected string
    # Remove leading zeros, decimal point, and exponent part
    mantissa = exp_str.split('e')[0] if 'e' in exp_str else exp_str
    mantissa = mantissa.replace('.', '').lstrip('0')
    sig = len(mantissa)
    # Round computed to same sig figs
    comp_rounded = sig_round(comp, sig)
    match = math.isclose(comp_rounded, exp_val, rel_tol=1e-12, abs_tol=0)
    return comp_rounded, match

# Compute claims
results = {}

# Q1
E1 = k_B * 1.0
results["Q1"] = E1

# Q2
E2 = k_B * 0.1
results["Q2"] = E2

# Q3
E3 = k_B * 20.0
results["Q3"] = E3

# Q4
results["Q4"] = E1 / E2

# Q5 – solve 2/x = tanh(x/2) by fixed‑point iteration
x = 2.0
for _ in range(20):
    x = 2.0 / math.tanh(x/2.0)
results["Q5"] = x

# Q6
x_star = results["Q5"]
Cmax_R = (x_star**2) / (4 * math.cosh(x_star/2.0)**2)
results["Q6"] = Cmax_R

# Q7
results["Q7"] = Cmax_R * R

# Q8
results["Q8"] = 1.0 / x_star

# Q9
Delta = 1.72e-3  # eV
T_star = Delta / (x_star * k_B)
results["Q9"] = T_star

# Q10
y_min, y_max = -0.4, 0.5
results["Q10"] = y_max - y_min

# Q11
results["Q11"] = (y_max + y_min) / 2.0

# Q12
excess = 0.1
results["Q12"] = (excess / results["Q10"]) * 100.0

# Q13
results["Q13"] = 1600.0 + 273.15

# Q14
results["Q14"] = k_B * results["Q13"]

# Q15
results["Q15"] = 1e-5 * 133.322

# Print verification lines
for qid in sorted(expected.keys(), key=lambda x: int(x[1:])):
    comp = results[qid]
    comp_rounded, is_match = compare(comp, expected[qid])
    # Use scientific notation for very small/large numbers to match expected format
    if "e" in expected[qid]:
        comp_str = f"{comp_rounded:.2e}"
    else:
        # Preserve the number of decimal places in expected string
        dec_places = expected[qid].split('.')[-1]
        if 'e' in dec_places:
            # fallback
            comp_str = f"{comp_rounded}"
        else:
            comp_str = f"{comp_rounded:.{len(dec_places)}f}"
    print(f"CLAIM {qid}: computed={comp_str} expected={expected[qid]} match={'yes' if is_match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for v in expected if compare(results[v], expected[v])[1])} match, {len(expected) - sum(1 for v in expected if compare(results[v], expected[v])[1])} mismatch")
