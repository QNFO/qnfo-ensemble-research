import math
from decimal import Decimal, getcontext

# set precision sufficient for the huge exponentiation in Q12
getcontext().prec = 12  # enough for mantissa, exponent will be huge

def claim_line(cid, computed, expected, match):
    return f"CLAIM {cid}: computed={computed} expected={expected} match={match}"

def approx_equal(a, b, rel_tol=1e-12, abs_tol=0.0):
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)

# Q1
c1 = 2 ** 3
e1 = "8"
m1 = "yes" if c1 == 8 else "no"
print(claim_line("Q1", c1, e1, m1))

# Q2
c2 = (8 - 1) / 8
e2 = "0.875"
m2 = "yes" if abs(c2 - 0.875) < 1e-12 else "no"
print(claim_line("Q2", c2, e2, m2))

# Q3
c3 = 2 ** 10
e3 = "1024"
m3 = "yes" if c3 == 1024 else "no"
print(claim_line("Q3", c3, e3, m3))

# Q4
c4 = 2 ** (8 * 8)
e4 = "18446744073709551616"
m4 = "yes" if c4 == 18446744073709551616 else "no"
print(claim_line("Q4", c4, e4, m4))

# Q5
c5 = 2 ** (8 * (8 - 1))
e5 = "72057594037927936"
m5 = "yes" if c5 == 72057594037927936 else "no"
print(claim_line("Q5", c5, e5, m5))

# Q6
c6 = 2 ** 3
e6 = "8"
m6 = "yes" if c6 == 8 else "no"
print(claim_line("Q6", c6, e6, m6))

# Q7
c7 = 8 - 1
e7 = "7"
m7 = "yes" if c7 == 7 else "no"
print(claim_line("Q7", c7, e7, m7))

# Q8
c8 = 7 - 1
e8 = "6"
m8 = "yes" if c8 == 6 else "no"
print(claim_line("Q8", c8, e8, m8))

# Q9
c9 = 6 - 2
e9 = "4"
m9 = "yes" if c9 == 4 else "no"
print(claim_line("Q9", c9, e9, m9))

# Q10
c10 = 7 / 4
e10 = "1.75"
m10 = "yes" if abs(c10 - 1.75) < 1e-12 else "no"
print(claim_line("Q10", c10, e10, m10))

# Q11
c11 = 8 * 3
e11 = "24"
m11 = "yes" if c11 == 24 else "no"
print(claim_line("Q11", c11, e11, m11))

# Q12
# Compute 10^(65536 * log10(2)) ≈ 10^19728.3, expected as 10^{19728}
exponent = Decimal(65536) * Decimal('0.30103')
c12 = (Decimal(10) ** exponent)
e12 = "10^{19728}"
# Since c12 is a huge number, we compare only the exponent part
# Extract exponent from Decimal's scientific notation
c12_str = format(c12, 'E')
# Example format: '1.000000E+19728'
c12_exp = int(c12_str.split('E')[1])
m12 = "yes" if c12_exp == 19728 else "no"
print(claim_line("Q12", c12_str, e12, m12))

# Q13
c13 = 2 ** (10 ** 2)  # 2^(10^2) = 2^100
e13 = "1267650600228229401496703205376"
m13 = "yes" if c13 == 1267650600228229401496703205376 else "no"
print(claim_line("Q13", c13, e13, m13))

# Q14
c14 = 2 ** 10
e14 = "1024"
m14 = "yes" if c14 == 1024 else "no"
print(claim_line("Q14", c14, e14, m14))

# Q15
c15 = 2 ** 2
e15 = "4"
m15 = "yes" if c15 == 4 else "no"
print(claim_line("Q15", c15, e15, m15))

# Q16
c16 = 2 ** 3
e16 = "8"
m16 = "yes" if c16 == 8 else "no"
print(claim_line("Q16", c16, e16, m16))

print(f"VERIFICATION SUMMARY: 16 claims, {sum([m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16].count('yes'))} match, {sum([m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16].count('no'))} mismatch")
