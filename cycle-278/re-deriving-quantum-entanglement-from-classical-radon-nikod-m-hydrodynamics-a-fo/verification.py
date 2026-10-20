import math

def round_sig(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

def format_scientific(x, sig):
    """Format x in scientific notation with sig significant digits."""
    return f"{round_sig(x, sig):.{sig}g}"

# Claims computations
results = {}

# Q1: Mermin violation factor
M_LHV = 2
M_Q = 4
factor_Q1 = M_Q / M_LHV
results["Q1"] = {"computed": factor_Q1, "expected": "2"}

# Q2: CHSH violation factor sqrt(2)
factor_Q2 = math.sqrt(2)
results["Q2"] = {"computed": factor_Q2, "expected": "1.414214"}

# Q3: GHZ triple‑product expectations
# +1 for XXX, -1 for the other three
expectations_Q3 = [+1, -1, -1, -1]
results["Q3"] = {"computed": expectations_Q3, "expected": "+1, -1, -1, -1"}

# Q4: Quantum product of the four GHZ correlations
product_Q4 = (+1) * (-1) * (-1) * (-1)
results["Q4"] = {"computed": product_Q4, "expected": "-1"}

# Q5: Classical pointwise product constraint
product_Q5 = (+1)  # from algebraic squaring of ±1 outcomes
results["Q5"] = {"computed": product_Q5, "expected": "+1"}

# Q6: Minimum propagation time for L = 1.0e-3 m
L_small = 1.0e-3
v_max = 3.0e8
t_min_small = L_small / v_max
results["Q6"] = {"computed": t_min_small, "expected": "3.333333e-12"}

# Q7: Required simulation timestep (one‑tenth of t_min)
delta_t = t_min_small / 10
results["Q7"] = {"computed": delta_t, "expected": "3.333333e-13"}

# Q8: Number of timesteps for one crossing of the small barrier
N_steps_small = t_min_small / delta_t
results["Q8"] = {"computed": N_steps_small, "expected": "10"}

# Q9: Minimum propagation time for L = 1.0 m
L_large = 1.0
t_min_large = L_large / v_max
results["Q9"] = {"computed": t_min_large, "expected": "3.333333e-9"}

# Q10: Number of timesteps for one crossing of the macroscopic barrier
N_steps_large = t_min_large / delta_t
results["Q10"] = {"computed": N_steps_large, "expected": "1.0e4"}

# Q11: Classical and quantum Mermin values
classical_M = 2
quantum_M = abs((+1) - (-1) - (-1) - (-1))
results["Q11"] = {"computed": (classical_M, quantum_M), "expected": "2,4"}

# Q12: Classical CHSH bound and quantum Tsirelson maximum
classical_CHSH = 2
quantum_CHSH = 2 * math.sqrt(2)
results["Q12"] = {"computed": quantum_CHSH, "expected": "2.828427"}

# Q13: Maximum signal speed assumed
v_assumed = 3.0e8
results["Q13"] = {"computed": v_assumed, "expected": "3.0e8"}

# Verification and printing
for cid, data in results.items():
    comp = data["computed"]
    exp = data["expected"]
    # Determine match
    if isinstance(comp, tuple):
        # For tuple claims, compare each element as string
        comp_str = ",".join(str(int(x)) for x in comp)
        match = "yes" if comp_str == exp.replace(" ", "") else "no"
        comp_out = comp_str
    elif isinstance(comp, list):
        comp_str = ", ".join(str(int(x)) for x in comp)
        match = "yes" if comp_str == exp.replace(" ", "") else "no"
        comp_out = comp_str
    else:
        # Determine number of significant digits from expected string
        # Strip possible scientific notation and signs
        exp_clean = exp.replace("-", "").replace("+", "")
        if "e" in exp_clean:
            mantissa, _ = exp_clean.split("e")
            sig = len(mantissa.replace(".", "").lstrip("0"))
        elif "." in exp_clean:
            sig = len(exp_clean.replace(".", "").lstrip("0"))
        else:
            sig = len(exp_clean.lstrip("0"))
        # Round computed value to that many sig figs
        comp_rounded = round_sig(comp, sig)
        # Format for comparison
        if "e" in exp:
            comp_str = format_scientific(comp_rounded, sig)
        else:
            comp_str = f"{comp_rounded:.{sig}g}"
        match = "yes" if comp_str == exp else "no"
        comp_out = comp_str
    print(f"CLAIM {cid}: computed={comp_out} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(1 for d in results.values() if ('yes' in (d.get('match') if isinstance(d, dict) else '')))} match, {sum(1 for d in results.values() if ('no' in (d.get('match') if isinstance(d, dict) else '')))} mismatch")
