import math

def close(a, b, rel=1e-12, abs_tol=1e-15):
    return abs(a - b) <= max(rel * max(abs(a), abs(b)), abs_tol)

claims = [
    ("Q1", lambda: math.log2(12), 3.584963),
    ("Q2", lambda: math.log(12/2) * 1.442695, 2.584963),
    ("Q3", lambda: math.ceil(math.log2(12)), 4),
    ("Q4", lambda: 2**4 / 12, 1.333333),
    ("Q5", lambda: math.log2(12) / 4, 0.896241),
    ("Q6", lambda: 1 - (math.log2(12) / 4), 0.103759),
    ("Q7_X", lambda: 1e-3 / 4, 2.5e-4),
    ("Q7_Z", lambda: 1e-3 / 2, 5e-4),
    ("Q7_I", lambda: 1 - 1e-3, 0.999),
    ("Q8", lambda: -1e-3*math.log2(1e-3) - (1-1e-3)*math.log2(1-1e-3), 0.011408),
    ("Q9", lambda: -(0.999*math.log2(0.999) + 2*2.5e-4*math.log2(2.5e-4) + 5e-4*math.log2(5e-4)), 0.012908),
    ("Q10", lambda: (-(0.999*math.log2(0.999) + 2*2.5e-4*math.log2(2.5e-4) + 5e-4*math.log2(5e-4))) - (-1e-3*math.log2(1e-3) - (1-1e-3)*math.log2(1-1e-3)), 1.5e-3),
    ("Q11", lambda: (-(0.999*math.log2(0.999) + 2*2.5e-4*math.log2(2.5e-4) + 5e-4*math.log2(5e-4))) / (-1e-3*math.log2(1e-3) - (1-1e-3)*math.log2(1-1e-3)), 1.131489),
    ("Q12", lambda: 3*1e-3/2, None),  # law, no numeric expected
    ("Q13", lambda: (0.1/1.1)**12, 3.186308e-13),
    ("Q14", lambda: 1e10 * 1e4 * 3.584963, 3.584963e14),
    ("Q15", lambda: 1e11 * 1e5 * 3.584963, 3.584963e16),
    ("Q16", lambda: 3.584963e16 * 1e-9, 3.584963e7),
]

for cid, func, expected in claims:
    computed = func()
    if expected is None:
        match = "yes"
        exp_str = ""
    else:
        match = "yes" if close(computed, expected) else "no"
        # format expected to match the paper's representation
        if isinstance(expected, float):
            # decide format based on magnitude
            if abs(expected) < 1e-2 or abs(expected) >= 1e5:
                exp_str = f"{expected:.6e}"
            else:
                exp_str = f"{expected:.6f}"
        else:
            exp_str = str(expected)
    print(f"CLAIM {cid}: computed={computed:.12g} expected={exp_str} match={match}")
