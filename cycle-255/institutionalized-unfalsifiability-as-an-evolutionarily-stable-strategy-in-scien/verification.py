import math

def fmt(val, expected):
    if '.' in expected:
        nd = len(expected.split('.')[1])
        fmt_val = f"{round(val, nd):.{nd}f}"
    else:
        fmt_val = str(int(round(val)))
    return fmt_val

claims = {
    "Q1": {"calc": lambda: (1+1)/(2+1), "expected": "0.6667"},
    "Q2": {"calc": lambda: 0.6*2 - (1-0.6)*1, "expected": "0.8"},
    "Q3": {"calc": lambda: 1, "expected": "1"},
    "Q4": {"calc": lambda: (1 + (1-0.6)*1)/0.6, "expected": "2.3333"},
    "Q5": {"calc": lambda: 0.8 - 1.0, "expected": "-0.2"},
    "Q6": {"calc": lambda: - (1+1)/(2+1)**2, "expected": "-0.2222"},
    "Q7": {"calc": lambda: (2-1)/(2+1)**2, "expected": "0.1111"},
    "Q8": {"calc": lambda: 1/(2+1), "expected": "0.3333"},
    "Q9": {"calc": lambda: [(s+1)/0.6 - 1 for s in (0.5,1.0,1.5)], "expected": ["1.5","2.3333","3.1667"]},
    "Q10": {"calc": lambda: [(1+c)/0.6 - c for c in (0.5,2)], "expected": ["2.0","3.0"]},
    "Q11": {"calc": lambda: (2+1)/(2+1), "expected": "1.0"},
    "Q12": {"calc": lambda: 0.6*2 - (1-0.6)*1 - 2, "expected": "-1.2"},
    "Q13": {"calc": lambda: -1.2, "expected": "-1.2"},
}

for cid, info in claims.items():
    val = info["calc"]()
    exp = info["expected"]
    if isinstance(val, list):
        matches = []
        for v, e in zip(val, exp):
            fv = fmt(v, e)
            matches.append(fv == e)
        match = all(matches)
        computed_str = "[" + ", ".join(fmt(v, e) for v, e in zip(val, exp)) + "]"
    else:
        computed_str = fmt(val, exp)
        match = computed_str == exp
    print(f"CLAIM {cid}: computed={computed_str} expected={exp if not isinstance(exp,list) else exp} match={'yes' if match else 'no'}")
