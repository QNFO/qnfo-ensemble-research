import math

def round_to_sig(x, sig):
    """Round x to sig significant digits."""
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

def compare(val, expected_str):
    """Return True if val matches expected_str within its precision."""
    # Determine if expected is in scientific notation
    if 'e' in expected_str or 'E' in expected_str:
        exp_val = float(expected_str)
        # Use relative tolerance based on number of digits after 'e' sign
        # Here we assume 1 significant digit after mantissa as in the paper
        return math.isclose(val, exp_val, rel_tol=1e-12, abs_tol=0)
    if '.' in expected_str:
        # Count decimal places
        dec = len(expected_str.split('.')[1])
        return round(val, dec) == round(float(expected_str), dec)
    else:
        return round(val) == round(float(expected_str))

# Inputs
F1 = 0.9990
F2 = 0.9956
Fr = 0.987
N = 105
threshold = 0.5

# Pre-computed logs
lnF1 = math.log(F1)
lnF2 = math.log(F2)
lnFr = math.log(Fr)

# Claims
claims = [
    ("Q1", 1 - F1, "0.001"),
    ("Q2", 1 - F2, "0.0044"),
    ("Q3", 1 - Fr, "0.013"),
    ("Q4", ( (1 - F2)/(1 - F1), (1 - Fr)/(1 - F1) ), "4.4, 13"),
    ("Q5", (F1 + F2 + Fr) / 3, "0.9938667"),
    ("Q6", 1 - (F1 * F2 * Fr), "0.0183254572"),
    ("Q7", (lnF1, lnF2, lnFr), "-1.0005e-3, -4.4097e-3, -1.30816e-2"),
    ("Q8", 2**N, "4.0564819e31"),
    ("Q9", 2**(N+1) - 2, "8.113e31"),
    ("Q10", (2**(N+1) - 2) / N, "7.7266e29"),
    ("Q11", math.floor(math.log(0.5) / lnF2), "157"),
    ("Q12", math.floor(math.log(0.5 / Fr) / lnF2), "154"),
    ("Q13", math.exp(N * lnFr), "0.2532"),
    ("Q14", math.exp(105*lnF1 + 100*lnF2 + 105*lnFr), "0.1467"),
    ("Q15", (math.log(0.5) / (lnF1 + lnF2)), "128.1"),
    ("Q16", 157 / (100 * 4), "0.3925")
]

for cid, comp, exp_str in claims:
    # Handle tuple results
    if isinstance(comp, tuple):
        if cid == "Q4":
            val1 = comp[0]
            val2 = comp[1]
            match1 = compare(val1, "4.4")
            match2 = compare(val2, "13")
            match = "yes" if (match1 and match2) else "no"
            computed = f"{val1:.6g}, {val2:.6g}"
        elif cid == "Q7":
            vals = comp
            match = "yes" if (compare(vals[0], "-1.0005e-3") and
                               compare(vals[1], "-4.4097e-3") and
                               compare(vals[2], "-1.30816e-2")) else "no"
            computed = f"{vals[0]:.7e}, {vals[1]:.7e}, {vals[2]:.7e}"
        else:
            computed = ", ".join(str(v) for v in comp)
            match = "no"
    else:
        match = "yes" if compare(comp, exp_str) else "no"
        if isinstance(comp, float):
            computed = f"{comp:.10g}"
        else:
            computed = str(comp)
    print(f"CLAIM {cid}: computed={computed} expected={exp_str} match={match}")

print("VERIFICATION SUMMARY: 16 claims, {} match, {} mismatch".format(
    sum(1 for _,c,exp in claims if compare(c if not isinstance(c, tuple) else c[0], exp)),
    sum(1 for _,c,exp in claims if not compare(c if not isinstance(c, tuple) else c[0], exp))
))
