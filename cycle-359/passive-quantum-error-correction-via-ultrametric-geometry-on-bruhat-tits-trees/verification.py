import math
from fractions import Fraction

def round_sig(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Claims data: (id, computed function, expected string, sig figs)
claims = [
    ("Q1", lambda: 1 + ((3+1)*(3**1 - 1)) // (3-1), "5", 1),
    ("Q2", lambda: 1 + ((3+1)*(3**2 - 1)) // (3-1), "17", 2),
    ("Q3", lambda: 1 + ((3+1)*(3**3 - 1)) // (3-1), "53", 2),
    ("Q4", lambda: 1 + ((2+1)*(2**1 - 1)) // (2-1), "4", 1),
    ("Q5", lambda: 1 + ((2+1)*(2**2 - 1)) // (2-1), "10", 2),
    ("Q6", lambda: 1 + ((2+1)*(2**3 - 1)) // (2-1), "22", 2),
    ("Q7", lambda: 2*1 + 1, "3", 1),
    ("Q8", lambda: sum(math.comb(5, k) * (1e-3)**k * (1-1e-3)**(5-k) for k in range(2,6)),
     "9.98e-6", 3),
    ("Q9", lambda: 1e-3 / (9.98e-6), "100.2", 4),
    ("Q10", lambda: sum(math.comb(17, k) * (1e-3)**k * (1-1e-3)**(17-k) for k in range(3,18)),
     "6.73e-7", 3),
    ("Q11", lambda: 1e-3 / (6.73e-7), "1.49e3", 3),
    ("Q12", lambda: 2**3, "8", 1),
    ("Q13", lambda: 2**4, "16", 2),
    ("Q14", lambda: 0.40**8, "6.5536e-4", 5),
    ("Q15", lambda: 0.40**16, "4.295e-7", 4),
    ("Q16", lambda: 0.40 / (6.5536e-4), "6.10e2", 3),
]

def parse_expected(s):
    """Convert expected string to float."""
    return float(s.replace('e', 'E'))

def match_value(comp, exp_str, sig):
    exp = parse_expected(exp_str)
    comp_rounded = round_sig(comp, sig)
    exp_rounded = round_sig(exp, sig)
    return comp_rounded == exp_rounded

print("VERIFICATION SUMMARY:")
match_count = 0
for cid, func, exp_str, sig in claims:
    comp = func()
    is_match = match_value(comp, exp_str, sig)
    match_word = "yes" if is_match else "no"
    if is_match:
        match_count += 1
    # format computed with enough digits
    if abs(comp) >= 1e-3:
        comp_str = f"{comp:.8g}"
    else:
        comp_str = f"{comp:.8e}"
    print(f"CLAIM {cid}: computed={comp_str} expected={exp_str} match={match_word}")

total = len(claims)
print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {total - match_count} mismatch")
