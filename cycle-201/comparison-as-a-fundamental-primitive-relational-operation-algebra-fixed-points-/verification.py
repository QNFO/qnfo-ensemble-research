import math

def sig_from_expected(exp):
    # Split off exponent if present
    base = exp.split('e')[0]
    # Remove sign
    base = base.lstrip('+-')
    # Count digits, ignoring decimal point
    digits = [c for c in base if c.isdigit()]
    # Find first non‑zero digit
    first_nz = next((i for i, c in enumerate(digits) if c != '0'), len(digits))
    sig = len(digits) - first_nz
    # If all digits are zero, treat as one significant digit
    return max(sig, 1)

def fmt(val, exp):
    sig = sig_from_expected(exp)
    # Use general format with the required significant digits
    return format(val, f".{sig}g")

# Inputs
K = 0.2
eta = 0.290
beta = 5
sigma = 1.5
gamma = 2.30
N10 = 10
N20 = 20
kB = 1.380649e-23
T = 300.0
ln2 = 0.69314718056
L = 10

# Claims
claims = [
    ("Q1", K * eta, "0.058"),
    ("Q2", beta * sigma, "7.5"),
    ("Q3", (K * eta) / (beta * sigma), "7.73e-3"),
    ("Q4", gamma - 1, "1.30"),
    ("Q5", (2**N10) * (2**N10 - 1) / 2, "523776"),
    ("Q6", (2**N20) * (2**N20 - 1) / 2, "5.50e11"),
    ("Q7", (2**N10 - 1) / 2, "511.5"),
    ("Q8", kB * T, "4.141947e-21"),
    ("Q9", kB * T * ln2, "2.870979e-21"),
    ("Q10", N10 * kB * T * ln2, "2.87e-20"),
    ("Q11", ((2**N20) * (2**N20 - 1) / 2) * kB * T * ln2, "1.58e-9"),
    ("Q12", 2**(L+1) - 2, "2046"),
    ("Q13", 2**L - 1, "1023")
]

for cid, comp, exp in claims:
    comp_fmt = fmt(comp, exp)
    match = "yes" if comp_fmt == exp else "no"
    print(f"CLAIM {cid}: computed={comp_fmt} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, "
      f"{sum(1 for _,c,e in claims if fmt(c,e)==e)} match, "
      f"{sum(1 for _,c,e in claims if fmt(c,e)!=e)} mismatch")
