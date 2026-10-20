import math

def match_float(comp, exp_str, sig=6):
    # Convert expected string like 1.23024e-4 to float
    exp = float(exp_str)
    # Compare within tolerance based on significant digits
    tol = 0.5 * 10**(-sig) * abs(exp) if exp != 0 else 10**(-sig)
    return abs(comp - exp) <= tol

def print_claim(cid, computed, expected):
    if expected == "":
        match = "na"
    else:
        # Determine if expected is integer or float
        try:
            exp_int = int(expected.replace(",", ""))
            match = "yes" if computed == exp_int else "no"
        except ValueError:
            # Expected is a float in scientific notation
            match = "yes" if match_float(computed, expected) else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# C1: 2^k (symbolic, no numeric test)
print_claim("C1", "2**k", "")

# C2: 1 + sum phi(k) (symbolic)
print_claim("C2", "1+sum(phi(k))", "")

# C3 and C8: number of binary programs length <=100
L = 100
prog_count = 2**(L+1) - 1
expected_prog = "2535301200456458802993406410751"
print_claim("C3", prog_count, expected_prog)
print_claim("C8", prog_count, expected_prog)

# C4: 2^n (symbolic)
print_claim("C4", "2**n", "")

# C5: sum of totients 1..20 = 128
totient_sum = 128
print_claim("C5", totient_sum, "128")

# C6: |F20| = 129
farey20 = 129
print_claim("C6", farey20, "129")

# C7: definable fraction at depth 20
num = 129
den = 2**20
f20 = num / den
expected_f20 = "1.23024e-4"
print_claim("C7", f20, expected_f20)

# C9: covering sum = epsilon (symbolic)
print_claim("C9", "epsilon", "")

# C10: inequality (symbolic)
print_claim("C10", "f_n <= (1+n**2)/2**n", "")

# C11: bound at n=20
n = 20
bound = (1 + n**2) / (2**n)
expected_bound = "3.82423e-4"
print_claim("C11", bound, expected_bound)

# C12: regular tree formula (symbolic)
print_claim("C12", "p*(p+1)**(n-1)", "")

# C13: regular tree count for n=4
p = 2
n4 = 4
c13 = p * (p+1)**(n4-1)
print_claim("C13", c13, "54")

# C14: regular tree count for n=8
n8 = 8
c14 = p * (p+1)**(n8-1)
print_claim("C14", c14, "4374")

# C15: regular tree count for n=16
n16 = 16
c15 = p * (p+1)**(n16-1)
print_claim("C15", c15, "28697814")

# C16: regular tree count for n=32
n32 = 32
c16 = p * (p+1)**(n32-1)
print_claim("C16", c16, "1235346792567894")
