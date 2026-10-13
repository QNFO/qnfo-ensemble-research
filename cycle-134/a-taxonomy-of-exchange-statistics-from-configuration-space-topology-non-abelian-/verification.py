import math
from fractions import Fraction

def sig(x, n=10):
    if x == 0:
        return 0.0
    from math import floor, log10
    d = floor(log10(abs(x)))
    return round(x, -(d - n + 1))

def match(computed, expected_str, sigdigits):
    exp = float(expected_str)
    # round computed to the significant digits of the stated value
    from math import floor, log10
    d = floor(log10(abs(exp)))
    comp_rounded = round(computed, -(d - (sigdigits - 1) + 1))
    return abs(comp_rounded - exp) <= abs(exp) * 10**(-(sigdigits)) * 5

# Inputs (as stated in the paper)
pi2 = 9.869604401            # paper's stated pi^2
kB  = 1.380649e-23           # J/K, exact 2019-SI
h   = 6.62607015e-34         # J s, exact 2019-SI

# Q8: k_B^2
kB2 = kB * kB
print("CLAIM Q8: computed=%.10g expected=1.906191661e-46 match=%s" % (kB2, "yes" if match(kB2, "1.906191661e-46", 10) else "no"))

# Q9: pi^2 * k_B^2
pi2kB2 = pi2 * kB2
print("CLAIM Q9: computed=%.10g expected=1.881335761e-45 match=%s" % (pi2kB2, "yes" if match(pi2kB2, "1.881335761e-45", 10) else "no"))

# Q10: 3h
three_h = 3 * h
print("CLAIM Q10: computed=%.10g expected=1.987821045e-33 match=%s" % (three_h, "yes" if match(three_h, "1.987821045e-33", 10) else "no"))

# Q1: kappa_0 = pi^2 k_B^2 / (3h)
kappa0 = pi2kB2 / three_h
print("CLAIM Q1: computed=%.10g expected=9.464311516e-13 match=%s" % (kappa0, "yes" if match(kappa0, "9.464311516e-13", 10) else "no"))

# Q2: c_- = 1/2
k_half = kappa0 * 0.5
print("CLAIM Q2: computed=%.10g expected=4.732155758e-13 match=%s" % (k_half, "yes" if match(k_half, "4.732155758e-13", 10) else "no"))

# Q3: c_- = 3/2
k_32 = kappa0 * 1.5
print("CLAIM Q3: computed=%.10g expected=1.419646727e-12 match=%s" % (k_32, "yes" if match(k_32, "1.419646727e-12", 10) else "no"))

# Q4: c_- = 5/2
k_52 = kappa0 * 2.5
print("CLAIM Q4: computed=%.10g expected=2.366077879e-12 match=%s" % (k_52, "yes" if match(k_52, "2.366077879e-12", 10) else "no"))

# Q5: absolute at T = 10 mK, c_- = 3/2
k_abs_10mK = k_32 * 0.010
print("CLAIM Q5: computed=%.10g expected=1.419646727e-14 match=%s" % (k_abs_10mK, "yes" if match(k_abs_10mK, "1.419646727e-14", 10) else "no"))

# Q6: absolute at T = 100 mK, c_- = 3/2
k_abs_100mK = k_32 * 0.100
print("CLAIM Q6: computed=%.10g expected=1.419646727e-13 match=%s" % (k_abs_100mK, "yes" if match(k_abs_100mK, "1.419646727e-13", 10) else "no"))

# Q7: discriminator ratio
ratio = 1.5 / 0.5
print("CLAIM Q7: computed=%.10g expected=3 match=%s" % (ratio, "yes" if ratio == 3.0 else "no"))

print("VERIFICATION SUMMARY: 10 claims, %d match, %d mismatch" % (
    sum(1 for r in [
        match(kB2, "1.906191661e-46", 10),
        match(pi2kB2, "1.881335761e-45", 10),
        match(three_h, "1.987821045e-33", 10),
        match(kappa0, "9.464311516e-13", 10),
        match(k_half, "4.732155758e-13", 10),
        match(k_32, "1.419646727e-12", 10),
        match(k_52, "2.366077879e-12", 10),
        match(k_abs_10mK, "1.419646727e-14", 10),
        match(k_abs_100mK, "1.419646727e-13", 10),
        ratio == 3.0,
    ] if r),
    sum(1 for r in [
        match(kB2, "1.906191661e-46", 10),
        match(pi2kB2, "1.881335761e-45", 10),
        match(three_h, "1.987821045e-33", 10),
        match(kappa0, "9.464311516e-13", 10),
        match(k_half, "4.732155758e-13", 10),
        match(k_32, "1.419646727e-12", 10),
        match(k_52, "2.366077879e-12", 10),
        match(k_abs_10mK, "1.419646727e-14", 10),
        match(k_abs_100mK, "1.419646727e-13", 10),
        ratio == 3.0,
    ] if not r),
))
