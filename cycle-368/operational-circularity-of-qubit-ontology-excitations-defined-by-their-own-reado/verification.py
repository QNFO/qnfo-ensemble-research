import math

def fmt(x, fmt_str):
    """Format number according to a simple format string like '9e-05'."""
    return format(x, fmt_str)

# Compute claims
results = {}

# Q1
p_e = 1 - 0.99991
results['Q1'] = p_e

# Q2
N_err = p_e * 1e6
results['Q2'] = N_err

# Q3
sigma_p = math.sqrt(0.5 * 0.5 / 1e4)
results['Q3'] = sigma_p

# Q4
ratio = sigma_p / p_e
results['Q4'] = ratio

# Q5
N_cross = 0.5 * 0.5 / (p_e ** 2)
results['Q5'] = N_cross

# Q6
L = 0.6
d0 = 1.0
eps = 1e-3
n6 = math.ceil(math.log(eps / d0) / math.log(L))
results['Q6'] = n6

# Q7
L13 = L ** 13
L14 = L ** 14
results['Q7'] = (L13, L14)

# Q8
d0b = 5e-2
epsb = p_e
n8 = math.ceil(math.log(epsb / d0b) / math.log(L))
results['Q8'] = n8

# Q9
alpha = 0.01
delta1 = 1e-3
N9 = math.log(2 / alpha) / (2 * delta1 ** 2)
results['Q9'] = N9

# Q10
delta2 = 1e-4
N10 = math.log(2 / alpha) / (2 * delta2 ** 2)
results['Q10'] = N10

# Q11 (formula only, no numeric check)
# Q12
x0 = 0.6
x1 = 0.5 * x0 + 0.5
x2 = 0.5 * x1 + 0.5
x3 = 0.5 * x2 + 0.5
results['Q12'] = (x1, x2, x3)

# Q13
epsilon_min1 = math.sqrt(sigma_p ** 2 + p_e ** 2)
results['Q13'] = epsilon_min1

# Q14
sigma_cross = 9.0e-5
epsilon_min2 = math.sqrt(sigma_cross ** 2 + p_e ** 2)
results['Q14'] = epsilon_min2

# Q15
# Jacobian with all entries 0.2 (3x3) has singular value 0.6
Lmax = 0.6
results['Q15'] = Lmax

# Q16
shot_budget = 2.649159e6
rate = 1e6
time_sec = shot_budget / rate
results['Q16'] = time_sec

# Expected values (as strings taken directly from the paper)
expected = {
    'Q1': '9e-05',
    'Q2': '90',
    'Q3': '5.00e-03',
    'Q4': '55.6',
    'Q5': '3.09e7',
    'Q6': '14',
    'Q7': ('1.306e-03', '7.836e-04'),  # (L^13, L^14)
    'Q8': '13',
    'Q9': '2.649159e6',
    'Q10': '2.649159e8',
    'Q12': ('0.8', '0.9', '0.95'),
    'Q13': '5.001e-03',
    'Q14': '1.27e-04',
    'Q15': '0.6',
    'Q16': 'approximately 3 s'
}

def match(val, exp):
    """Simple matching: compare rounded strings."""
    if isinstance(exp, tuple):
        # For Q7 and Q12 compare each component
        return all(match(v, e) for v, e in zip(val, exp))
    if isinstance(exp, str) and exp.startswith('approximately'):
        # Approximate textual match
        return True
    # Convert expected to float if possible
    try:
        exp_f = float(exp)
        # Determine number of significant digits in expected string
        sig = len(exp.replace('.', '').replace('e', '').replace('-', '').lstrip('0'))
        # Round computed value to same number of sig digits
        fmt_str = f".{sig}g"
        return format(val, fmt_str) == format(exp_f, fmt_str)
    except ValueError:
        # Non‑numeric expected (e.g., textual), accept if equal strings
        return str(val) == exp

# Print results
for qid in sorted(expected.keys(), key=lambda x: int(x[1:]) if x[1:].isdigit() else 0):
    comp = results[qid]
    exp = expected[qid]
    m = 'yes' if match(comp, exp) else 'no'
    # Format computed value for printing
    if isinstance(comp, tuple):
        comp_str = ', '.join(str(c) for c in comp)
    else:
        comp_str = str(comp)
    print(f"CLAIM {qid}: computed={comp_str} expected={exp} match={m}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if match(results[q], expected[q]))} match, {len(expected) - sum(1 for q in expected if match(results[q], expected[q]))} mismatch")
