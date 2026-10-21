import math

def fmt(value, expected):
    if '.' in expected:
        dp = len(expected.split('.')[1])
        rounded = round(value, dp)
        # Ensure trailing zeros are kept
        return f"{rounded:.{dp}f}"
    else:
        return str(int(round(value)))

claims = {
    "Q1": {"calc": (1+1)/(2+1), "expected": "0.6667"},
    "Q2": {"calc": 0.6*2 - (1-0.6)*1, "expected": "0.8"},
    "Q3": {"calc": 1, "expected": "1.0"},
    "Q4": {"calc": 0.8 - 1.0, "expected": "-0.2"},
    "Q5": {"calc": math.log(9)/0.2, "expected": "10.99"},
    "Q6": {"calc": (1 + (1-0.6)*1)/0.6, "expected": "2.3333"},
    "Q7": {"calc": -(1+1)/(2+1)**2, "expected": "-0.2222"},
    "Q8": {"calc": (2-1)/(2+1)**2, "expected": "0.1111"},
    "Q9": {"calc": 1/(2+1), "expected": "0.3333"},
    "Q10": {"calc": 1/0.6, "expected": "1.6667"},
    "Q11": {"calc": (1-0.6)/0.6, "expected": "0.6667"},
    "Q12": {"calc": (0.6*10 - (1-0.6)*1, (1+1)/(10+1), 0.6*10 - (1-0.6)*1 - 1),
            "expected": "5.6, 0.1818, 4.6"},
    "Q13": {"calc": (0.6*5 - (1-0.6)*1, (1+1)/(5+1), 0.6*5 - (1-0.6)*1 - 1),
            "expected": "2.6, 0.3333, 1.6"},
    "Q14": {"calc": ((2+1)/(2+1), 0.6*2 - (1-0.6)*1 - 2),
            "expected": "1.0, -1.2"},
    "Q15": {"calc": (0.6*2 - (1-0.6)*5,
                    0.6*2 - (1-0.6)*5 - 1,
                    math.log(9)/1.8),
            "expected": "-0.8, -1.8, 1.22"},
    "Q16": {"calc": 2*(1+1)/(2+1)**3, "expected": "0.1481"},
}

for cid, data in claims.items():
    calc = data["calc"]
    exp = data["expected"]
    if isinstance(calc, tuple):
        comps = [fmt(v, e.strip()) for v, e in zip(calc, exp.split(','))]
        computed_str = ", ".join(comps)
    else:
        computed_str = fmt(calc, exp)
    match = "yes" if computed_str == exp else "no"
    print(f"CLAIM {cid}: computed={computed_str} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, "
      f"{sum(1 for d in claims.values() if (lambda c,e: (c if not isinstance(c,tuple) else ', '.join([fmt(v, e_i.strip()) for v,e_i in zip(c,e.split(','))])) ) (d['calc'], d['expected']) == d['expected'])} match, "
      f"{len(claims) - sum(1 for d in claims.values() if (lambda c,e: (c if not isinstance(c,tuple) else ', '.join([fmt(v, e_i.strip()) for v,e_i in zip(c,e.split(','))])) ) (d['calc'], d['expected']) == d['expected'])} mismatch")
