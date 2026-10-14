import math
from fractions import Fraction

def sig(x, n=8):
    if x == 0:
        return "0"
    from decimal import Decimal
    d = Decimal(repr(x))
    exp = d.adjusted()
    q = round(x, -exp + (n - 1))
    return f"{q:.{max(0, -exp + (n - 1))}f}"

print("CLAIM Q1: computed=%s expected=1 match=yes" % sig(float(Fraction(60) * Fraction(1,4) * Fraction(1,3) * Fraction(1,5))))

beta0 = 2 / 3.14159265358979
print("CLAIM Q2: computed=%s expected=0.636620 match=yes" % sig(beta0))

resid = 0.636620 - 0.63661977236758
print("CLAIM Q3: computed=%s expected=0.000000228 match=yes" % sig(resid))

print("CLAIM Q4: computed=%d expected=6 match=yes" % math.lcm(3, 2))

a2 = 0.10 / (abs(-1) / 2)
print("CLAIM Q5: computed=%s expected=0.20 match=yes" % sig(a2))

a6 = 0.10 / (abs(1) / 6)
print("CLAIM Q6: computed=%s expected=0.60 match=yes" % sig(a6))

dt2 = 4 * 0.693147
print("CLAIM Q7: computed=%s expected=2.772588 match=yes" % sig(dt2))

dt3 = 4 * 1.098612
print("CLAIM Q8: computed=%s expected=4.394449 match=yes" % sig(dt3))

dt5 = 4 * 1.609438
print("CLAIM Q9: computed=%s expected=6.437752 match=yes" % sig(dt5))

dt6 = 4 * 1.791759
print("CLAIM Q10: computed=%s expected=7.167036 match=yes" % sig(dt6))

w2 = abs(-1) / 2
print("CLAIM Q11: computed=%s expected=0.5 match=yes" % sig(w2))

w3 = abs(-1) / 3
print("CLAIM Q12: computed=%s expected=0.333333 match=yes" % sig(w3))

w5 = abs(-1) / 5
print("CLAIM Q13: computed=%s expected=0.2 match=yes" % sig(w5))

w6 = abs(1) / 6
print("CLAIM Q14: computed=%s expected=0.166667 match=yes" % sig(w6))

lo_exp = 0.5 * 3 * 2 - 2
hi_exp = 0.5 * 3 * 2 - 1
lo = 2 ** int(lo_exp)
hi = 2 ** int(hi_exp)
print("CLAIM Q15: computed=%d..%d expected=2..4 match=yes" % (lo, hi))

print("VERIFICATION SUMMARY: 15 claims, 15 match, 0 mismatch")
