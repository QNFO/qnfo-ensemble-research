import math

def fmt(val, fmt_type):
    """Format val according to the expected representation."""
    if fmt_type == "int":
        return f"{int(round(val))}"
    if fmt_type == "int_no_round":
        return f"{int(val)}"
    if fmt_type == "float_4dp":
        return f"{val:.4f}"
    if fmt_type == "float_5dp":
        return f"{val:.5f}"
    if fmt_type == "float_1dp":
        return f"{val:.1f}"
    if fmt_type == "float_2dp":
        return f"{val:.2f}"
    if fmt_type == "sci_2sd":
        return f"{val:.2e}"
    if fmt_type == "sci_3sd":
        return f"{val:.3e}"
    if fmt_type == "sci_1sd":
        return f"{val:.1e}"
    raise ValueError

# Inputs
g_step = 3          # MS gates per Trotter step
s = 2               # steps per simulated second
f_MS = 0.995        # per-gate fidelity
N = 6               # number of gates
J = 0.18            # Hz
dt = 0.5            # s
pairs = 3
gates_per_pair = 3
t_low = 50e-6       # s
t_high = 100e-6     # s
t_gate = (t_low + t_high) / 2   # s
N_gate = 6
E_gate = 1e-6       # J (1 µJ)
E_sol_low = 8.5     # J
E_sol_high = 16.3   # J
Delta_protect = 1e12
tau_bio = 25e-3     # s
tau_willow = 291e-6 # s

# Computations
g_total = g_step * s
F = f_MS ** N
trot_err_step = (J * dt) ** 3
cumulative_error = 2 * trot_err_step
g_trimer = pairs * gates_per_pair
t_wall = N_gate * t_gate
E_sim = N_gate * E_gate
R_low = E_sol_low / E_sim
R_high = E_sol_high / E_sim
scale_factor = Delta_protect * (tau_bio / tau_willow)
p_error = 1 - f_MS ** N
error_rate = p_error / t_wall  # per second

# Expected representations
expected = {
    "Q2": ("6", fmt(g_total, "int")),
    "Q3": ("0.9703", fmt(F, "float_4dp")),
    "Q4": ("7.3e-4", fmt(trot_err_step, "sci_1sd")),
    "Q5": ("0.00146", fmt(cumulative_error, "float_5dp")),
    "Q6": ("9", fmt(g_trimer, "int")),
    "Q7": ("450", fmt(t_wall * 1e6, "int")),  # µs
    "Q8": ("6", fmt(E_sim * 1e6, "int")),    # µJ
    "Q9": ("1.42e6", fmt(R_low, "sci_3sd")),
    "Q10": ("2.72e6", fmt(R_high, "sci_3sd")),
    "Q11": ("8.6e13", fmt(scale_factor, "sci_2sd")),
    "Q12": ("0.0297", fmt(p_error, "float_4dp")),
    "Q13": ("66.0", fmt(error_rate, "float_1dp")),
    "Q14": ("75", fmt(t_gate * 1e6, "int")),  # µs
}

# Reporting
for qid, (exp_str, comp_str) in expected.items():
    match = "yes" if exp_str == comp_str else "no"
    print(f"CLAIM {qid}: computed={comp_str} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for _,(_,c) in expected.items() if c==expected[_][0])} match, {len(expected)-sum(1 for _,(_,c) in expected.items() if c==expected[_][0])} mismatch")
