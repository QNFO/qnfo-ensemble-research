import math

def fmt(val, sig=8):
    # format with given significant digits, removing trailing zeros
    s = f"{val:.{sig}g}"
    return s

claims = [
    # Q1
    ("Q1", 0.075 * 0.8, "0.060"),
    # Q2
    ("Q2", 0.06 * 0.25, "0.015"),
    # Q3
    ("Q3", 0.925 * (1-0.7) * 1 + 0.075 * 0.8, "0.3375"),
    # Q4
    ("Q4", 0.3375 * 0.25, "0.084375"),
    # Q5
    ("Q5", ((0.084375 - 0.015) / 0.015) * 100, "462.5"),
    # Q6
    ("Q6", 0.084375 - 0.015, "0.069375"),
    # Q7
    ("Q7", max(0, 1 - 0.1 * 1 / 0.2), "0.5"),
    # Q8
    ("Q8", 0.5 * 0.2, "0.1"),
    # Q9
    ("Q9", (1 - 0.5 * 0.2) / 1, "0.9"),
    # Q10
    ("Q10", (1 - 0.2) / 1, "0.8"),
    # Q11
    ("Q11", ((0.9 - 0.8) / 0.8) * 100, "12.5"),
    # Q12
    ("Q12", 0.9 * (1-0.2) - 1 * 0.9**2 / 2 - 0.1 * 0.5 * 0.2, "0.305"),
    # Q13
    ("Q13", 0.8 * (1-0.2) - 1 * 0.8**2 / 2 - 0.1 * 0.2, "0.30"),
    # Q14
    ("Q14", (0.005 / 0.30) * 100, "1.67"),
    # Q15
    ("Q15", max(0, 1 - 0.1 * 1 / 0.05), "0"),
    # Q16
    ("Q16", (1 - 0 * 0.05) / 1, "1.00"),  # effort E*
]

# compute fitness for Q16 separately
def fitness_q16():
    p = 0.05
    c = 1
    lam = 0.1
    alpha = 0
    E = (1 - alpha * p) / c
    F = E * (1 - p) - c * E**2 / 2 - lam * alpha * p
    return E, F

E16, F16 = fitness_q16()
claims[15] = ("Q16", F16, "0.475")  # expected from paper

for cid, computed, expected in claims:
    # determine match
    # compare numeric values within tolerance appropriate to expected digits
    try:
        exp_val = float(expected)
        # tolerance: half of last displayed unit
        # determine number of decimal places in expected
        if "." in expected:
            dec = len(expected.split(".")[1])
            tol = 0.5 * 10**(-dec)
        else:
            # integer expected
            tol = 0.5
        match = "yes" if abs(computed - exp_val) <= tol else "no"
    except:
        match = "no"
    print(f"CLAIM {cid}: computed={fmt(computed)} expected={expected} match={match}")
print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if (abs(c-float(e))<= (0.5*10**(-len(e.split('.')[1]) if '.' in e else 0))) )} match, {len(claims)-sum(1 for _,c,e in claims if (abs(c-float(e))<= (0.5*10**(-len(e.split('.')[1]) if '.' in e else 0))) )} mismatch")
