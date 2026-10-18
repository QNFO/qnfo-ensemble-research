import math

def round_to_str(value, fmt):
    """Round value to the number of decimal places in fmt string."""
    if '.' in fmt:
        dec = len(fmt.split('.')[1])
        return f"{round(value, dec):.{dec}f}"
    else:
        # integer format
        return str(int(round(value)))

claims = [
    # Q1
    ("Q1", 1.0,
     "1.0"),
    # Q2
    ("Q2", 1.0,
     "1.0"),
    # Q3
    ("Q3", math.sqrt(2 * (1 + 0.5**2)),
     "1.581"),
    # Q4
    ("Q4", math.sqrt(2 * (1 + 0**2)),
     "1.414"),
    # Q5a
    ("Q5a", math.sqrt(0.5**2 + 1**2),
     "1.11803"),
    # Q5b
    ("Q5b", 2 / math.sqrt(0.5**2 + 1**2),
     "1.78885"),
    # Q6
    ("Q6", math.sqrt(2) * 1,
     "1.41421"),
    # Q7
    ("Q7", 2 * 2 / (math.sqrt(2) * 1),
     "2.82843"),
    # Q8
    ("Q8", (2 * 2 / (math.sqrt(2) * 1)) / (2 / math.sqrt(0.5**2 + 1**2)),
     "1.58114"),
    # Q9
    ("Q9", 1 - 0.5 * math.erfc(1.78885 / math.sqrt(2)),
     "0.963"),
    # Q10
    ("Q10", 1 - 0.5 * math.erfc(2.82843 / math.sqrt(2)),
     "0.998"),
    # Q11
    ("Q11", 1 / math.sqrt(0.9 + 0.1),
     "1.0"),
    # Q12
    ("Q12", 1 / math.sqrt(2 * 0.1),
     "2.236"),
    # Q13
    ("Q13", 1 - 0.5 * math.erfc(1.0 / math.sqrt(2)),
     "0.841"),
    # Q14
    ("Q14", 1 - 0.5 * math.erfc(2.236 / math.sqrt(2)),
     "0.987"),
    # Q15
    ("Q15", (0.1 * (0.015)**2) / (0.1 * (0.006)**2),
     "6.25")
]

for cid, comp, exp in claims:
    comp_str = round_to_str(comp, exp)
    match = "yes" if comp_str == exp else "no"
    print(f"CLAIM {cid}: computed={comp_str} expected={exp} match={match}")
