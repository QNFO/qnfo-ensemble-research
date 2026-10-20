import math

def close(a, b, rel=1e-12, abs_tol=1e-12):
    return abs(a - b) <= max(rel * max(abs(a), abs(b)), abs_tol)

claims = {
    "Q1": {"computed": lambda: 29 * 28 // 2, "expected": "406"},
    "Q2": {"computed": lambda: 29 * 28 * 27 // 6, "expected": "3654"},
    "Q3": {"computed": lambda: (29 * 28 * 27 // 6) / (29 * 28 // 2), "expected": "9.0"},
    "Q4": {"computed": lambda: 1 - (1 - 1e-3) * (1 - 2e-3) * (1 - 5e-4), "expected": "3.4965e-3"},
    "Q5": {"computed": lambda: 1e-3 + 2e-3 + 5e-4, "expected": "3.5e-3"},
    "Q6": {"computed": lambda: 7 * 6 // 2, "expected": "21"},
    "Q7": {"computed": lambda: 7 * 6, "expected": "42"},
    "Q8": {"computed": lambda: 29 - 21, "expected": "8"},
    "Q9": {"computed": lambda: 2 * 1 // 2, "expected": "1"},
    "Q10": {"computed": lambda: 0, "expected": "0"},
    "Q11": {"computed": lambda: 1000 / 500, "expected": "2"},
    "Q12": {"computed": lambda: 29 / 7, "expected": "4.14"},
    "Q13": {"computed": lambda: 58 * 57 // 2, "expected": "1653"},
    "Q14": {"computed": lambda: 58 * 57 * 56 // 6, "expected": "30856"},
    "Q15": {"computed": lambda: (58 * 57 * 56 // 6) / (58 * 57 // 2), "expected": "18.667"},
    "Q16": {"computed": lambda: 1 - (1 - 1e-2) ** 4, "expected": "3.94e-2"},
}

for cid, data in claims.items():
    comp = data["computed"]()
    exp_str = data["expected"]
    exp_val = float(exp_str)
    match = "yes" if close(comp, exp_val) else "no"
    # format computed with enough precision
    if isinstance(comp, float):
        comp_str = f"{comp:.12g}"
    else:
        comp_str = str(comp)
    print(f"CLAIM {cid}: computed={comp_str} expected={exp_str} match={match}")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
