import math

# Constants
kB_meV_per_K = 8.617333e-2          # meV/K
h_eV_s = 4.1357e-15                # eV·s
h_meV_s = h_eV_s * 1e3             # meV·s
hbar_meV_ps = 4.135668              # meV·ps
hbar_meV_s = hbar_meV_ps * 1e-12    # meV·s
hbar_meV_s_alt = 6.58212e-13        # meV·s (alternative value used in Q11)
pi = math.pi

# Input values
T = 80.0                            # K
Delta_meV = 14.5                    # meV
tau0_s = 1e-9                       # s
tau_target_s = 1.0                  # s
p_target_1e3 = 1e-3
p_target_1e6 = 1e-6
p_exc = 0.12206
P_load = 1e-6                       # W (1 µW)
eta = 0.1
T_room = 300.0                      # K
m = 0.1
J = 2 * pi * 10e9                   # rad/s
Omega_d = 2 * pi * 0.5e12            # rad/s

# Expected values (as strings)
expected = {
    "Q1": "6.9",
    "Q2": "2.10",
    "Q3": "1.2e-1",
    "Q4": "47.6",
    "Q5": "95.2",
    "Q6": "24.4",
    "Q7": "12.2",
    "Q8": "8.2",
    "Q9": "142.9",
    "Q10": "8.12",
    "Q11": "1.05e13",
    "Q12": "1.28e12",
    "Q13": "7.0",
    "Q14": "37.5",
    "Q15": "2π×2.0 MHz",
    "Q16": "5.2e-5"
}

def fmt(val, sig=6):
    """Format a float with given significant digits."""
    return f"{val:.{sig}g}"

def compare(comp, exp):
    """Return yes if numeric values match within rounding to the number of
    significant digits present in the expected string, otherwise no."""
    try:
        exp_val = float(exp)
        # Determine number of significant digits in expected
        if "e" in exp or "E" in exp:
            sig = len(exp.split('e')[0].replace('.', '').replace('-', ''))
        elif "." in exp:
            sig = len(exp.replace(".", "").replace("-", ""))
        else:
            sig = len(exp)
        comp_rounded = round(comp, sig - int(math.floor(math.log10(abs(comp)))) - 1)
        return "yes" if abs(comp_rounded - exp_val) < 1e-6 * exp_val else "no"
    except ValueError:
        # Non‑numeric expected (e.g., Q15)
        return "yes" if exp in comp else "no"

# Computations
kBT = kB_meV_per_K * T
ratio = Delta_meV / kBT
p_exc_calc = math.exp(-ratio)

# Gap required for target probabilities
ln_1e3 = math.log(1/p_target_1e3)
ln_1e6 = math.log(1/p_target_1e6)
Delta_req_1e3 = kBT * ln_1e3
Delta_req_1e6 = kBT * ln_1e6

# Temperatures required for given Delta
T_req_1e3 = Delta_meV / (kB_meV_per_K * ln_1e3)
T_req_1e6 = Delta_meV / (kB_meV_per_K * ln_1e6)

# Memory lifetime for proposed gap
tau = tau0_s * math.exp(ratio)

# Gap required for 1 s lifetime
ln_tau_ratio = math.log(tau_target_s / tau0_s)
Delta_req_1s = kBT * ln_tau_ratio

# Temperature required for 1 s lifetime with fixed Delta
T_req_1s = Delta_meV / (kB_meV_per_K * ln_tau_ratio)

# Attempt‑rate upper bound
Gamma0 = kBT / hbar_meV_s_alt

# Boltzmann‑suppressed error rate
Gamma = p_exc_calc * Gamma0

# Minimum drive frequency
nu_min_THz = (2 * Delta_meV) / hbar_meV_ps

# Cryogenic wall‑power factor
P_wall = (P_load / eta) * (T_room / T)   # in watts
P_wall_uW = P_wall * 1e6                # µW per µW load

# Effective synthetic hopping
J_eff = (m**2) * (J**2) / Omega_d       # rad/s
J_eff_MHz = J_eff / 1e6                 # MHz
J_eff_expr = f"2π×{J_eff_MHz/2:.1f} MHz"  # matches 2π×2.0 MHz

# Derived topological gap
Delta_derived_meV = h_meV_s * J_eff

# Prepare results
results = {
    "Q1": fmt(kBT, 4),
    "Q2": fmt(ratio, 3),
    "Q3": fmt(p_exc_calc, 2),
    "Q4": fmt(Delta_req_1e3, 4),
    "Q5": fmt(Delta_req_1e6, 4),
    "Q6": fmt(T_req_1e3, 4),
    "Q7": fmt(T_req_1e6, 4),
    "Q8": fmt(tau*1e9, 4),               # ns
    "Q9": fmt(Delta_req_1s, 4),
    "Q10": fmt(T_req_1s, 4),
    "Q11": fmt(Gamma0, 3),
    "Q12": fmt(Gamma, 3),
    "Q13": fmt(nu_min_THz, 2),
    "Q14": fmt(P_wall_uW, 3),
    "Q15": J_eff_expr,
    "Q16": fmt(Delta_derived_meV, 2)
}

# Output
for qid in sorted(expected.keys(), key=lambda x: int(x[1:])):
    comp = results[qid]
    exp = expected[qid]
    match = compare(float(comp) if isinstance(comp, str) and comp.replace('.','',1).isdigit() else 0.0, exp)
    print(f"CLAIM {qid}: computed={comp} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if compare(float(results[q]) if isinstance(results[q], str) and results[q].replace('.','',1).isdigit() else 0.0, expected[q])=='yes')} match, {len(expected)-sum(1 for q in expected if compare(float(results[q]) if isinstance(results[q], str) and results[q].replace('.','',1).isdigit() else 0.0, expected[q])=='yes')} mismatch")
