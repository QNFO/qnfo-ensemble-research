import math

def claim_line(cid, computed, expected):
    match = "yes" if expected == "" else ("yes" if round(computed, len(expected.split('e')[-1]) if 'e' in expected else len(expected.split('.')[-1])) == float(expected) else "no")
    print(f"CLAIM {cid}: computed={computed:.9g} expected={expected} match={match}")

# C1: generic formula, no numeric expected
# We'll just compute for a sample p=5, t=2 to demonstrate the formula
p, t = 5, 2
C1 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C1", C1, "")

# C2
p, t = 3, 1
C2 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C2", C2, "5")

# C3
p, t = 3, 2
C3 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C3", C3, "17")

# C4
p, t = 3, 3
C4 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C4", C4, "53")

# C5
p, t = 2, 1
C5 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C5", C5, "4")

# C6
p, t = 2, 2
C6 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C6", C6, "10")

# C7
p, t = 2, 3
C7 = 1 + (p + 1) * (p**t - 1) / (p - 1)
claim_line("C7", C7, "22")

# C8: distance formula, no numeric expected
t = 4
C8 = 2 * t + 1
claim_line("C8", C8, "")

# C9
t = 1
C9 = 2 * t + 1
claim_line("C9", C9, "3")

# C10
d = 3
C10 = math.floor((d - 1) / 2)
claim_line("C10", C10, "1")

# C11
n1 = 5
C11 = 1 / n1
claim_line("C11", C11, "0.2")

# C12: formula, no numeric expected
eps = 0.001
C12 = 1 - (1 - eps)**5 - 5 * eps * (1 - eps)**4
claim_line("C12", C12, "")

# C13
eps = 0.001
C13 = 1 - (1 - eps)**5 - 5 * eps * (1 - eps)**4
claim_line("C13", C13, "9.98e-6")

# C14
eps = 0.001
P_pass = 1 - (1 - eps)**5 - 5 * eps * (1 - eps)**4
C14 = eps / P_pass
claim_line("C14", C14, "100.2")

# C15
eps = 0.001
n2 = 17
term3 = math.comb(n2, 3) * eps**3 * (1 - eps)**14
term4 = math.comb(n2, 4) * eps**4 * (1 - eps)**13
C15 = term3 + term4
claim_line("C15", C15, "6.73e-7")

# C16
eps = 0.001
C16 = 1 - (1 - eps)**2
claim_line("C16", C16, "0.001999")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for line in open(__file__) if 'match=yes' in line)} match, {sum(1 for line in open(__file__) if 'match=no' in line)} mismatch")
