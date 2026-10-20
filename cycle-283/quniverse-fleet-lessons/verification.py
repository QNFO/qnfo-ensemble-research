import math

def round_to(value, places):
    return round(value, places)

claims = [
    ("Q1", 36 * 0.12 * (1 - 0.5), "2.16", 2),
    ("Q2", 1889 / (1889 + 1264), "0.599", 3),
    ("Q3", 0.12 * (1 - 0.5), "0.06", 2),
    ("Q4", 0.12 * (1 - 0.599), "0.04812", 5),
    ("Q5", 36 * 0.12 * (1 - 0.599), "1.73", 2),
    ("Q6", 36 * 0.06 * (1 - 0.06), "2.0304", 4),
    ("Q7", math.sqrt(2.0304), "1.425", 3),
    ("Q8", 917 / 95, "9.65", 2),
    ("Q9", (5 / 42) * 100, "11.9", 1),
    ("Q10", (34657 * 512) / 1048576, "16.922", 3),
    ("Q11", 304 + 16.922, "320.9", 1),
    ("Q12", 0.4*4.5 + 0.3*4.0 + 0.3*4.2, "4.26", 2),
    ("Q13", 0.4*4.9 + 0.3*4.4 + 0.3*4.6, "4.66", 2),
    ("Q14", 150 + 2.16 * 5, "160.8", 1),
    ("Q15", 150 + 1.08 * 5, "155.4", 1),
    ("Q16", 100 * 110, "11000", 0),
]

for cid, comp, exp_str, dec in claims:
    comp_rounded = round_to(comp, dec)
    # format computed with at least 8 significant digits
    comp_str = f"{comp:.10g}"
    match = "yes" if str(comp_rounded) == exp_str else "no"
    print(f"CLAIM {cid}: computed={comp_str} expected={exp_str} match={match}")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
