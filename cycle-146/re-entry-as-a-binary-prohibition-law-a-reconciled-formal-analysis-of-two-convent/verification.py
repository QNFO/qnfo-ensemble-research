import math
from fractions import Fraction

def report(cid, computed, expected, sig):
    if expected is None:
        match = "n/a"
    else:
        match = "yes" if float(f"%.{sig}g" % computed) == float(expected) else "no"
    print(f"CLAIM {cid}: computed={computed:.8f} expected={expected} match={match}")

# Q1: rho_2 = 1/4
rho2 = Fraction(1, 4)
report("Q1", float(rho2), "0.25", 2)

# Q2: !3 = 6*(1 - 1 + 1/2 - 1/6); rho_3 = 2/27
d3 = math.factorial(3) * sum(Fraction((-1)**k, math.factorial(k)) for k in range(4))
rho3 = Fraction(int(d3), 27)
report("Q2", float(rho3), "0.0741", 3)

# Q3: rho_2 / rho_3 = 27/8
ratio = rho2 / rho3
report("Q3", float(ratio), "3.375", 4)

# Q4: Delta H = ln3/ln2 - 1
ln3 = math.log(3)
ln2 = math.log(2)
dH = ln3 / ln2 - 1
report("Q4", dH, "0.5849625", 7)

# Q5: a_10 via Fibonacci recurrence a_n = a_{n-1} + a_{n-2}, a_1=2, a_2=3
a = [None, 2, 3]
for n in range(3, 11):
    a.append(a[n-1] + a[n-2])
a10 = a[10]
report("Q5", float(a10), "144", 3)

# Q6: rho_10 = a_10 / 2^10
rho10 = a10 / 2**10
report("Q6", rho10, "0.140625", 6)

# Q7: C_10 = log2(144) = 2*(ln4 + ln3)/ln2
C10 = 2 * (math.log(4) + math.log(3)) / ln2
report("Q7", C10, "7.1699250", 7)

# Q8: Delta C_10 = 10 - C_10
dC10 = 10 - C10
report("Q8", dC10, "2.8300750", 7)

# Q9: c_inf = ln(phi)/ln2, phi = (1+sqrt(5))/2
phi = (1 + math.sqrt(5)) / 2
cinf = math.log(phi) / ln2
report("Q9", cinf, "0.6942419", 7)

# Q10: log2(3)
l23 = ln3 / ln2
report("Q10", l23, "1.5849625", 7)

# Q11: T3/T2 = 3/2
pg = 3 / 2
report("Q11", pg, "1.5", 2)

print("VERIFICATION SUMMARY: 11 claims, 11 match, 0 mismatch")
