import math

def fmt(x, fmt_str):
    return fmt_str.format(x)

def compare(computed, expected_str):
    # Remove any approx symbols and whitespace
    exp = expected_str.replace('≈', '').replace('~', '').strip()
    # Determine if expected is in scientific notation
    if 'e' in exp or 'E' in exp:
        # Compare as float with tolerance relative
        return abs(computed - float(exp)) / float(exp) < 1e-6
    # Determine decimal places
    if '.' in exp:
        dec = len(exp.split('.')[1])
        return round(computed, dec) == round(float(exp), dec)
    else:
        return int(round(computed)) == int(round(float(exp)))

claims = [
    ("Q1", 2 - 1.984, "0.016"),
    ("Q2", (2+1) - 2*math.sqrt(2), "0.17157288"),
    ("Q3", (2+1)*2**(10-1), "1536"),
    ("Q4", 1 + (2+1)*(2**10 - 1)//(2-1), "3070"),
    ("Q5", 1 + (2+1)*(2**12 - 1)//(2-1), "12286"),
    ("Q6", (2+1)*2**(7-1), "192"),
    ("Q7", 1 + (2+1)*(2**7 - 1)//(2-1), "382"),
    ("Q8", 2/7, "0.2857"),
    ("Q9", 2/9, "0.222"),
    ("Q10", math.ceil(math.log2(101)), "7"),
    ("Q11", math.ceil(math.log2(100)), "7"),
    ("Q12", math.ceil(math.log2(257)), "9"),
    ("Q13", 1 + (2+1)*(2**9 - 1)//(2-1), "1534"),
    ("Q14", 5e2 * (1024**6), "5.8e20"),
    ("Q15", (0.40+0.30+0.20)*6, "5.4"),
]

for cid, comp, exp in claims:
    match = "yes" if compare(comp, exp) else "no"
    # Use scientific notation for large numbers
    if abs(comp) >= 1e6:
        comp_str = "{:.8e}".format(comp)
    else:
        comp_str = "{:.8f}".format(comp).rstrip('0').rstrip('.')
    print(f"CLAIM {cid}: computed={comp_str} expected={exp} match={match}")

print("VERIFICATION SUMMARY: {} claims, {} match, {} mismatch".format(
    len(claims),
    sum(1 for _,c,e in claims if compare(c,e)),
    sum(1 for _,c,e in claims if not compare(c,e))
))
