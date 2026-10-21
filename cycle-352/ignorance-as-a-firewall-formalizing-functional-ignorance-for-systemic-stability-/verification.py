import math

def fmt(x):
    # format with at least 8 significant digits, removing trailing zeros
    s = f"{x:.10g}"
    return s

claims = [
    ("Q1", 1 * 10, "10"),
    ("Q2", 0.3 * 10, "3"),
    ("Q3", 1 - 1/3, "0.6667"),
    ("Q4", 1 - 1/10, "0.9"),
    ("Q5", 1 - 0.1, "0.9"),
    ("Q6", 1 - 0.2 * 1, "0.8"),
    ("Q7", math.floor(1 / 0.15), "6"),
    ("Q8", math.floor(1 / (0.15 * (1 - 2/3))), "20"),
    ("Q9", 20 / 6, "3.33"),
    ("Q10", 0.5 / 0.5, "1"),
    ("Q11", 1 - 1/3, "0.6667"),
    ("Q12", 10000 * 3600 * 0.00002, "7.20"),
    ("Q13", 0.66 / 0.8, "0.825"),
]

for cid, comp, exp in claims:
    # round computed to match expected precision for comparison
    # determine number of decimal places in expected
    if "." in exp:
        dec = len(exp.split(".")[1])
        comp_rounded = round(comp, dec)
    else:
        comp_rounded = int(round(comp))
    match = "yes" if str(comp_rounded) == exp else "no"
    print(f"CLAIM {cid}: computed={fmt(comp)} expected={exp} match={match}")
print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if (str(round(c, len(e.split('.')[1])) if '.' in e else int(round(c))) == e))} match, {len(claims) - sum(1 for _,c,e in claims if (str(round(c, len(e.split('.')[1])) if '.' in e else int(round(c))) == e))} mismatch")
