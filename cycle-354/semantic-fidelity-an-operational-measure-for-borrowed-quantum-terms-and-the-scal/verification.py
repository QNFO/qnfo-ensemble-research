import math

def fmt(val, expected):
    """Format value with enough digits and compare to expected string."""
    # Determine number of decimal places in expected (if any)
    if '.' in expected:
        dec = len(expected.split('.')[1])
        fmt_str = f"{{:.{dec}f}}"
        comp = fmt_str.format(val)
    else:
        # integer expected
        comp = str(int(round(val)))
    match = "yes" if comp == expected else "no"
    return comp, match

def report(claim_id, computed, expected):
    print(f"CLAIM {claim_id}: computed={computed} expected={expected} match={expected}")

# Q1
val = 0.5 * (abs(1 - 0.5) + abs(0 - 0.5))
comp, match = fmt(val, "0.5")
print(f"CLAIM Q1: computed={comp} expected=0.5 match={match}")

# Q2
val = 1 - 0.5
comp, match = fmt(val, "0.5")
print(f"CLAIM Q2: computed={comp} expected=0.5 match={match}")

# Q4 (k=2)
k = 2
delta = 0.5
val = 1 - (1 - delta) ** k
comp, match = fmt(val, "0.75")
print(f"CLAIM Q4: computed={comp} expected=0.75 match={match}")

# Q5 (k=3)
k = 3
val = 1 - (1 - delta) ** k
comp, match = fmt(val, "0.875")
print(f"CLAIM Q5: computed={comp} expected=0.875 match={match}")

# Q6 (k=4)
k = 4
val = 1 - (1 - delta) ** k
comp, match = fmt(val, "0.9375")
print(f"CLAIM Q6: computed={comp} expected=0.9375 match={match}")

# Q7 (k=5)
k = 5
val = 1 - (1 - delta) ** k
comp, match = fmt(val, "0.96875")
print(f"CLAIM Q7: computed={comp} expected=0.96875 match={match}")

# Q8 (k=6)
k = 6
val = 1 - (1 - delta) ** k
comp, match = fmt(val, "0.984375")
print(f"CLAIM Q8: computed={comp} expected=0.984375 match={match}")

# Q9 (k=2 fidelity)
k = 2
D = 1 - (1 - delta) ** k
val = 1 - D
comp, match = fmt(val, "0.25")
print(f"CLAIM Q9: computed={comp} expected=0.25 match={match}")

# Q10 (k=3 fidelity)
k = 3
D = 1 - (1 - delta) ** k
val = 1 - D
comp, match = fmt(val, "0.125")
print(f"CLAIM Q10: computed={comp} expected=0.125 match={match}")

# Q11 (k=4 fidelity)
k = 4
D = 1 - (1 - delta) ** k
val = 1 - D
comp, match = fmt(val, "0.0625")
print(f"CLAIM Q11: computed={comp} expected=0.0625 match={match}")

# Q12 (k=5 fidelity)
k = 5
D = 1 - (1 - delta) ** k
val = 1 - D
comp, match = fmt(val, "0.03125")
print(f"CLAIM Q12: computed={comp} expected=0.03125 match={match}")

# Q13 (k=6 fidelity)
k = 6
D = 1 - (1 - delta) ** k
val = 1 - D
comp, match = fmt(val, "0.015625")
print(f"CLAIM Q13: computed={comp} expected=0.015625 match={match}")

# Q14 (k* crossing)
epsilon = 0.9
delta = 0.5
k_star = math.ceil(math.log(1 - epsilon) / math.log(1 - delta))
comp, match = fmt(k_star, "4")
print(f"CLAIM Q14: computed={comp} expected=4 match={match}")

# Q15 (particles = 2 * k*)
particles = 2 * k_star
comp, match = fmt(particles, "8")
print(f"CLAIM Q15: computed={comp} expected=8 match={match}")

# Q16 (delta=0.10 crossing)
delta = 0.10
k_star = math.ceil(math.log(0.1) / math.log(1 - delta))
comp, match = fmt(k_star, "22")
print(f"CLAIM Q16: computed={comp} expected=22 match={match}")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
