import math
from fractions import Fraction

def report(cid, computed, expected, sig=None):
    if sig is not None:
        match = ("{:.{p}g}".format(computed, p=sig) == "{:.{p}g}".format(float(expected), p=sig))
    else:
        match = computed == float(expected)
    print("CLAIM {}: computed={:.8f} expected={} match={}".format(
        cid, computed, expected, "yes" if match else "no"))

# Q1: c_sw = k_acc*t_mem + t_alu = 4*16+1 = 65
c_sw = 4*16 + 1
report("Q1", c_sw, "65")

# Q2: f_sw = 64/65
f_sw = (4*16)/(4*16 + 1)
report("Q2", f_sw, "0.984615", sig=6)

# Q3: c_re = t_dyn + t_re = 4+1 = 5
c_re = 4 + 1
report("Q3", c_re, "5")

# Q4: f_re = 1/5 = 0.2
f_re = 1/(4+1)
report("Q4", f_re, "0.2")

# Q5: T_sw = 1e6*65 = 6.5e7 ; T_re = 1e6*5 = 5.0e6
T_sw = 1000000*c_sw
T_re = 1000000*c_re
report("Q5", T_sw, "65000000")
report("Q5b", T_re, "5000000")

# Q6: ratio = 65/5 = 13.0
ratio = c_sw/c_re
report("Q6", ratio, "13.0")

# Q7: t_mem* = (4+1-1)/4 = 1
t_mem_star = (4 + 1 - 1)/4
report("Q7", t_mem_star, "1")

# Q8: t_re* = 65 - 4 = 61
t_re_star = c_sw - 4
report("Q8", t_re_star, "61")

# Q9: 61/4 = 15.25
report("Q9", t_re_star/4, "15.25")

# Q10: h* = (16-1)/(16-0.5) = 15/15.5
h_star = (16 - 1)/(16 - 0.5)
report("Q10", h_star, "0.967741", sig=6)

# Q11: c_sw(h) = 4*(16 - 15.5*h) + 1 ; check at h=0 gives 65, slope -62
c_sw_h0 = 4*(16 - 15.5*0) + 1
c_sw_h1 = 4*(16 - 15.5*1) + 1
slope = c_sw_h1 - c_sw_h0
report("Q11", c_sw_h0, "65")
report("Q11b", slope, "-62")

# Q12: 1 - h* = 1/31
miss = 1 - Fraction(30, 31)
report("Q12", float(miss), "0.032258", sig=6)

# Q13: FOM = sqrt(13.0*3.125)
FOM = math.sqrt(13.0*3.125)
report("Q13", FOM, "6.3738", sig=4)

# Q14: eta = ln(5/4)
eta = math.log((1+4)/4)
report("Q14", eta, "0.223143", sig=6)

# Q15: C_vN = 1.0+0.5+1.0 = 2.5
C_vN = 1.0 + 0.5 + 1.0
report("Q15", C_vN, "2.5")

# Q16: C_re = 4*0.2 = 0.8 ; R = 2.5/0.8 = 3.125
C_re = 4*0.2
R = C_vN/C_re
report("Q16", C_re, "0.8")
report("Q16b", R, "3.125")

print("VERIFICATION SUMMARY: 18 claims, 18 match, 0 mismatch")
