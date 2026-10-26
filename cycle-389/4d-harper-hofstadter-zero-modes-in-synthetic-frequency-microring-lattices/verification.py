import math

def sig_round(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0.0
    else:
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Inputs
c = 3e8                     # m/s
lam = 1.55e-6               # m
Q = 1e10
hnu_over_kB = 167.9         # K
T = 80.0                    # K
p_sc = 1e-3
J_hz = 3.606e10             # Hz
N = 100

# Derived quantities
omega_c = 2 * math.pi * c / lam
kappa = omega_c / Q
kappa_over_2pi = kappa / (2 * math.pi)
tau = 1 / kappa
J_rad = 2 * math.pi * J_hz
ratio = J_rad / kappa
n = 1 / (math.exp(hnu_over_kB / T) - 1)
p_eff = p_sc * n
F = (1 - p_eff) ** N
C2 = 1 ** 2  # p = 1

# Expected values (as strings from the paper)
expected = {
    "Q1": "1.216e15",
    "Q2": "1.216e5",
    "Q3": "1.94e4",   # 19.4 kHz -> 1.94e4 Hz
    "Q4": "8.22e-6",
    "Q5": "2.267e11",
    "Q6": "1.86e6",
    "Q7": "0.1396",
    "Q8": "1.396e-4",
    "Q9": "0.9861",
    "Q10": "1"
}

# Helper to format computed value with appropriate sig figs
def format_match(comp, exp_str):
    # Determine number of significant digits in expected string
    # Remove exponent part if present
    if 'e' in exp_str:
        mantissa, _ = exp_str.split('e')
    else:
        mantissa = exp_str
    # Count digits ignoring leading zeros and decimal point
    mantissa = mantissa.lstrip('0').replace('.', '')
    sig = len(mantissa)
    comp_rounded = sig_round(comp, sig)
    # Use scientific notation with lower-case e
    comp_str = f"{comp_rounded:.{sig-1}e}"
    match = "yes" if comp_str == exp_str else "no"
    return comp_str, match

# Compute and print results
claims = {
    "Q1": omega_c,
    "Q2": kappa,
    "Q3": kappa_over_2pi,
    "Q4": tau,
    "Q5": J_rad,
    "Q6": ratio,
    "Q7": n,
    "Q8": p_eff,
    "Q9": F,
    "Q10": C2
}

for cid, value in claims.items():
    exp = expected[cid]
    comp_str, match = format_match(value, exp)
    print(f"CLAIM {cid}: computed={comp_str} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for cid in claims if format_match(claims[cid], expected[cid])[1]=='yes')} match, {sum(1 for cid in claims if format_match(claims[cid], expected[cid])[1]=='no')} mismatch")
