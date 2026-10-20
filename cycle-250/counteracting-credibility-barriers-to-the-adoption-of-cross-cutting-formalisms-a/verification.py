import math

def fmt(x, sig):
    """Format number with given significant digits."""
    if x == 0:
        return "0"
    # Determine order of magnitude
    order = int(math.floor(math.log10(abs(x))))
    digits = sig - 1 - order
    fmt_str = "{:." + str(max(digits, 0)) + "f}"
    return fmt_str.format(round(x, digits))

claims = [
    ("Q1", 1 - 0.9936, "0.0064"),
    ("Q2", 0.05, "0.05"),
    ("Q3", 0.5*0.0064 + 0.5*0.05, "0.0282"),
    ("Q4", 0.5*0.0064, "0.0032"),
    ("Q5", 0.5*0.05, "0.025"),
    ("Q6", 0.5*0.0032 + 0.5*0.025, "0.0141"),
    ("Q7", (122_239_000_083 - 6) / 122_239_000_083, "0.9999999999509"),
    ("Q8", 6 / 122_239_000_083, "4.91e-11"),
    ("Q9", (16/60) / 24, "0.011111"),
    ("Q10", 0.45*0.0064 + 0.45*0.05 + 0.10*((16/60)/24), "0.0264911"),
    ("Q11", 0.03 / 0.0436, "0.6880733945"),
    ("Q12", (0.7*0.0064 + 0.3*0.05, 0.8*0.0064 + 0.2*0.05), "0.01968, 0.01472"),
    ("Q13", 0.5*0.0032 + 0.5*0.05, "0.0266"),
    ("Q14", 0.5*0.0064 + 0.5*0.025, "0.0157"),
    ("Q15", (6/122_239_000_083)*0.1, "4.91e-12"),
    ("Q16", (3*0.0141, 2*0.0141), "0.0423; 0.0282")
]

for cid, comp, exp in claims:
    # Handle tuple results
    if isinstance(comp, tuple):
        computed = "; ".join(fmt(v, 6) for v in comp)
    else:
        # Determine number of significant digits from expected string
        # Count digits ignoring leading zeros and decimal point
        exp_clean = exp.replace("e", "E")
        if "e" in exp.lower():
            # scientific notation, use 2 sig figs as in expected
            sig = len(exp_clean.split('e')[0].replace(".", "").replace("-", ""))
        else:
            # count digits after first non‑zero
            digits = exp_clean.lstrip("0.")
            sig = len(digits)
        computed = fmt(comp, sig)
    match = "yes" if str(computed) == exp else "no"
    print(f"CLAIM {cid}: computed={computed} expected={exp} match={match}")
print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if (str(fmt(c,6)) if not isinstance(c,tuple) else '; '.join(fmt(v,6) for v in c))==e)} match, {len(claims)-sum(1 for _,c,e in claims if (str(fmt(c,6)) if not isinstance(c,tuple) else '; '.join(fmt(v,6) for v in c))==e)} mismatch")
