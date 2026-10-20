import math

def fmt(val, digits):
    """Format number with given significant digits (as in expected string)."""
    # For scientific notation like 4.103e-4, keep as is.
    s = f"{val:.{digits}g}"
    # Ensure scientific notation uses 'e' lower case
    return s.replace('E', 'e')

claims = [
    ("Q1", lambda: 2/50 - 2/70, "0.0114286", 7),
    ("Q2", lambda R: math.pi * R**2, "4.103e-4", 4),  # 4 sig figs
    ("Q3", lambda V: V * 50**2, "1.0258", 5),
    ("Q4", lambda C: C * 60**-2, None, None),  # law, no numeric expected
    ("Q5", lambda: 1 * 1.0258 * 50**-2, "4.103e-4", 4),
    ("Q6", lambda: 1 * 1.0258 * 60**-2, "2.849e-4", 4),
    ("Q7", lambda P60, P50: P60 / P50, "0.694", 3),
    ("Q8", lambda eps: math.ceil(1/eps), "1000", 4),
    ("Q9", lambda eps: math.ceil(math.log(1/eps)), "7", 1),
    ("Q10", lambda eps: math.ceil(1/eps), "1000000", 7),
    ("Q11", lambda eps: math.ceil(math.log(1/eps)), "14", 2),
    ("Q12", lambda p: sum(x**2 for x in p), "0.2750", 5),
    ("Q13", lambda p: sum(x**3 for x in p), "0.08875", 5),
    ("Q14", lambda p1, P2: p1**2 / P2, "0.581818", 6),
    ("Q15", lambda p1, p2: (p1/p2)**2, "2.56", 3),
    ("Q16", lambda d0, q, eps: math.log(eps/d0) / math.log(q), "458.21", 5),
]

# Pre‑compute shared intermediate values
R = 2/50 - 2/70
V = math.pi * R**2
C = V * 50**2
P50 = 1 * C * 50**-2
P60 = 1 * C * 60**-2
p_vals = [0.40, 0.25, 0.20, 0.10, 0.05]
P2 = sum(x**2 for x in p_vals)
P3 = sum(x**3 for x in p_vals)

for cid, func, expected, sig in claims:
    # compute based on cid
    if cid == "Q1":
        comp = func()
    elif cid == "Q2":
        comp = func(R)
    elif cid == "Q3":
        comp = func(V)
    elif cid == "Q4":
        comp = func(C)  # just to have a number, not used
    elif cid == "Q5":
        comp = func()
    elif cid == "Q6":
        comp = func()
    elif cid == "Q7":
        comp = func(P60, P50)
    elif cid == "Q8":
        comp = func(1e-3)
    elif cid == "Q9":
        comp = func(1e-3)
    elif cid == "Q10":
        comp = func(1e-6)
    elif cid == "Q11":
        comp = func(1e-6)
    elif cid == "Q12":
        comp = func(p_vals)
    elif cid == "Q13":
        comp = func(p_vals)
    elif cid == "Q14":
        comp = func(0.40, P2)
    elif cid == "Q15":
        comp = func(0.40, 0.25)
    elif cid == "Q16":
        comp = func(1, 0.99, 1e-2)
    else:
        comp = None

    if expected is None:
        exp_str = "none"
        match = "yes"
    else:
        # format computed value to same number of significant digits as expected
        # Determine number of digits after decimal or in mantissa from expected string
        # Simple approach: use sig provided
        comp_str = fmt(comp, sig)
        exp_str = expected
        match = "yes" if comp_str == exp_str else "no"

    print(f"CLAIM {cid}: computed={comp_str if expected is not None else comp} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for c in claims if (c[2] is None) or (fmt(eval('comp'), c[3]) == c[2]))} match, {sum(1 for c in claims if not (c[2] is None) and (fmt(eval('comp'), c[3]) != c[2]))} mismatch")
