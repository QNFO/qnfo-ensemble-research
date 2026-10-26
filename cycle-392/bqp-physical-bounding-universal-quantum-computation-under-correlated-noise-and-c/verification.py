import math

def round_sig(x, sig=6):
    """Round x to given significant digits."""
    if x == 0:
        return 0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Constants
L = 10.0                     # meters
c = 3e8                      # m/s
D = 1e3                      # circuit depth
p = 1e-3                     # independent gate error
alpha_base = 1e-5            # baseline correlated coefficient
alpha_opt = 1e-6             # optimistic correlated coefficient
p_th = 1e-3                  # surface-code threshold
p_th_relaxed = 1e-2          # relaxed logical error budget
T_coh = 100e-6               # coherence time (seconds)
k = 1e3                      # physical gates per logical gate
tau_gate = 20e-9             # gate duration (seconds)
r_gate = 1e8                 # gate rate (1/s)
N_shor = 1e4                 # qubits for Shor-scale processor
p0 = 1e-4                    # independent error per gate (alternative)
p_corr = 1e-3                # correlated error floor (alternative)
modules = 10                 # number of modules
cost_per_module = 5.0        # million dollars per module

# Claim computations
# Q1: propagation latency per hop
tau_prop = L / c                         # seconds
tau_prop_ns = tau_prop * 1e9             # ns
computed_Q1 = round(tau_prop_ns)         # ns, rounded to nearest integer

# Q2: total latency for depth-1000 circuit
T_lat = D * tau_prop                     # seconds
T_lat_us = T_lat * 1e6                   # µs
computed_Q2 = round(T_lat_us)            # µs, rounded to nearest integer

# Q3: baseline correlated error threshold N
# Solve p*N + alpha_base*N*(N-1) = p_th
# Quadratic: alpha_base*N^2 + (p - alpha_base)*N - p_th = 0
a = alpha_base
b = p - alpha_base
c_eq = -p_th
disc = b**2 - 4*a*c_eq
N_pos = (-b + math.sqrt(disc)) / (2*a)
computed_Q3 = round(N_pos)               # should be 1

# Q4: optimistic correlated error threshold N
a = alpha_opt
b = p - alpha_opt
c_eq = -p_th
disc = b**2 - 4*a*c_eq
N_pos = (-b + math.sqrt(disc)) / (2*a)
computed_Q4 = round(N_pos)               # should be 1

# Q5: relaxed logical‑error budget maximal qubits (approximation)
computed_Q5 = p_th_relaxed / p           # 10.0

# Q6: time per logical gate
tau_log = k * tau_gate                   # seconds
tau_log_us = tau_log * 1e6               # µs
computed_Q6 = tau_log_us                  # 20.0 µs

# Q7: maximum logical gates within coherence window
C_max = T_coh / tau_log
computed_Q7 = C_max                       # 5.0

# Q8: independent error term for Shor-scale processor
indep_error = N_shor * p0
computed_Q8 = indep_error                 # 1.0

# Q9: latency‑induced error term (repeating)
tau_lat = L / c                           # seconds (33.33... ns)
latency_term = tau_lat * r_gate           # dimensionless, 3.333...
computed_Q9 = round_sig(latency_term, 5)  # 3.3333...

# Q10: total logical error for Shor-scale
epsilon_log = indep_error + p_corr + latency_term
computed_Q10 = round_sig(epsilon_log, 5)  # 4.33433...

# Q11: modular latency term (repeating)
tau_lat_mod = 1.0 / c                     # L=1 m, so 1/c seconds
latency_term_mod = tau_lat_mod * r_gate   # 1/3 ≈ 0.33333...
computed_Q11 = round_sig(latency_term_mod, 5)  # 0.33333...

# Q12: total logical error for modular case
epsilon_log_mod = indep_error + p_corr + latency_term_mod
computed_Q12 = round_sig(epsilon_log_mod, 5)   # 1.33433...

# Q13: projected total cost for ten‑module architecture
total_cost = modules * cost_per_module   # million dollars
computed_Q13 = total_cost                # 50.0

# Expected values (as strings from the paper)
expected = {
    "Q1": "33 ns",
    "Q2": "33 µs",
    "Q3": "1 qubit",
    "Q4": "1 qubit",
    "Q5": "10",
    "Q6": "20 µs",
    "Q7": "5",
    "Q8": "1.0",
    "Q9": "3.33",
    "Q10": "4.33433",
    "Q11": "0.333",
    "Q12": "1.33433",
    "Q13": "50 M$"
}

# Helper to format computed values with appropriate units
def fmt(val, claim):
    if claim in ["Q1"]:
        return f"{int(val)} ns"
    if claim in ["Q2", "Q6"]:
        return f"{int(val)} µs"
    if claim in ["Q3", "Q4"]:
        return f"{int(val)} qubit"
    if claim in ["Q7"]:
        return f"{int(val)}"
    if claim in ["Q8", "Q9", "Q10", "Q11", "Q12"]:
        # keep up to 5 decimal places, strip trailing zeros
        s = f"{val:.5f}".rstrip('0').rstrip('.')
        return s
    if claim == "Q13":
        return f"{int(val)} M$"
    return str(val)

# Comparison and output
for q in ["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10","Q11","Q12","Q13"]:
    comp_val = locals()[f"computed_{q}"]
    comp_str = fmt(comp_val, q)
    exp_str = expected[q]
    # Determine match: compare numeric parts after stripping units and rounding to expected precision
    # For simplicity, compare formatted strings directly
    match = "yes" if comp_str == exp_str else "no"
    print(f"CLAIM {q}: computed={comp_str} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if fmt(locals()[f'computed_{q}'], q)==expected[q])} match, {sum(1 for q in expected if fmt(locals()[f'computed_{q}'], q)!=expected[q])} mismatch")
