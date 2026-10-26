import math

# Constants
c = 2.998e8          # m s^-1
G = 6.674e-11        # m^3 kg^-1 s^-2
pi_approx = 3.1416
L = 1.0              # m
P = 1.000e3          # W
n = 3.0
V = 5.0e3            # V
d = 20.0e-6          # m
mass = 100.0         # kg
dv = 1.0             # m s^-1
specific_energy = 3.6e5   # J kg^-1

# Expected values from the paper (as strings)
expected = {
    "Q1": "4.82e42",
    "Q2": "8.078e33",
    "Q3": "1.677e-9",
    "Q4": "4.82e42",
    "Q5": "51.7",
    "Q6": "6.67e-6",
    "Q7": "6.67e-6",
    "Q8": "3.34e-6",
    "Q9": "2.998e8",
    "Q10": "3.00e10",
    "Q11": "8.33e4",
    "Q12": "4.17e4",
    "Q13": "2.5e8",
    "Q14": "1e-8",
    "Q15": "3.3e-7",
    "Q16": "51.7"
}

def fmt(x):
    """Format a number with at least 8 significant digits, using scientific notation."""
    return f"{x:.8g}"

# Computations
u = c**4 / (8 * pi_approx * G * L**2)                     # Q1, Q4
c4 = c**4                                                  # Q2
eight_pi_G = 8 * pi_approx * G                             # Q3
log_ratio = math.log10(u / 1e-9)                           # Q5, Q16
F_max = (P / c) * (n - 1)                                 # Q6, Q7
F_gamma = P / c                                            # Q8
E_per_I = c                                                # Q9
I = mass * dv                                              # Q10 intermediate
E = I * c                                                  # Q10
M_E = E / specific_energy                                   # Q11
M_E_half = M_E / 2                                          # Q12
E_field = V / d                                            # Q13
detect_limit = 1e-8                                         # Q14 (given)
threshold = F_gamma / 10                                   # Q15

# Prepare results
results = {
    "Q1": fmt(u),
    "Q2": fmt(c4),
    "Q3": fmt(eight_pi_G),
    "Q4": fmt(u),
    "Q5": fmt(log_ratio),
    "Q6": fmt(F_max),
    "Q7": fmt(F_max),
    "Q8": fmt(F_gamma),
    "Q9": fmt(E_per_I),
    "Q10": fmt(E),
    "Q11": fmt(M_E),
    "Q12": fmt(M_E_half),
    "Q13": fmt(E_field),
    "Q14": fmt(detect_limit),
    "Q15": fmt(threshold),
    "Q16": fmt(log_ratio)
}

# Verification output
match_count = 0
total = len(expected)

for qid in sorted(expected.keys()):
    comp = results[qid]
    exp = expected[qid]
    match = "yes" if comp == exp else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {qid}: computed={comp} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {total - match_count} mismatch")
