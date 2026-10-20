import math

def fmt(val, sig=6):
    # format with given significant digits, removing trailing zeros
    return f"{val:.{sig}g}"

claims = [
    ("Q1", "5.0e8", fmt(1.0e9/2)),
    ("Q2", "0.881911", fmt(math.exp(-4*math.pi*0.01), 6)),
    ("Q3", "2.2e-13", fmt((1e-12) / (1.381e-23*300/(9.109e-31*1e9)), 6)),
    ("Q4", "1.0e-9", fmt(1/1e9, 6)),
    ("Q5", "5.49306e-10", fmt(0.549306/1e9, 6)),
    ("Q6", "2.55413e-10", fmt(0.255413/1e9, 6)),
    ("Q7", "2.0e-9", fmt(2/1e9, 6)),
    ("Q8", "1.16e10", fmt(1.055e-34*1e14/9.109e-31, 6)),
    ("Q9", "5.8e9", fmt(1.055e-34*1e14/(2*9.109e-31), 6)),
    ("Q10", "0.993866", fmt((0.9990+0.9956+0.9870)/3, 6)),
    ("Q11", "0.98727", fmt((0.9990+2*0.9956+105*0.9870)/(1+2+105), 6)),
    ("Q12", "5.49e-7", fmt(0.549306/1e6, 6)),
    ("Q13", "0.939101", fmt(math.exp(-2*math.pi*0.01), 6)),
    ("Q14", "0.533488", fmt(math.exp(-2*math.pi*10*0.01), 6)),
    ("Q15", "4.5e3", fmt(1e-9/2.2e-13, 2)),
]

for cid, expected, computed in claims:
    match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,e,c in claims if c==e)} match, {sum(1 for _,e,c in claims if c!=e)} mismatch")
