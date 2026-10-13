import math

def stirling_ln_fact(k, lnk):
    return k*lnk - k + 0.5*(1.837877 + lnk) + 1.0/(12.0*k)

LN100 = 4.605170
LN110 = 4.700480
LN120 = 4.787492
LN125 = 4.828314
LN130 = 4.867534
LN2PI = 1.837877
LAM = 100.0

# Q1
lnP110 = -LAM + 110*LN100 - stirling_ln_fact(110, LN110)
# Q2
half = 0.5*(LN2PI + LN100)
lnG110 = -half - (110-LAM)**2/(2*LAM)
# Q3
d1 = lnP110 - lnG110
# Q4
lnP120 = -LAM + 120*LN100 - stirling_ln_fact(120, LN120)
lnG120 = -half - (120-LAM)**2/(2*LAM)
d2 = lnP120 - lnG120
# Q6
lnP125 = -LAM + 125*LN100 - stirling_ln_fact(125, LN125)
lnG125 = -half - (125-LAM)**2/(2*LAM)
d25 = lnP125 - lnG125
# Q8
lnP130 = -LAM + 130*LN100 - stirling_ln_fact(130, LN130)
lnG130 = -half - (130-LAM)**2/(2*LAM)
d3 = lnP130 - lnG130
ratio3 = math.exp(d3)
# Q10, Q11
rel1 = math.exp(0.0325) - 1
rel25 = math.exp(0.1197) - 1
# Q12, Q13
g1 = 1.0/math.sqrt(LAM)
kurt = 1.0/LAM
# Q14
x14 = 2 + 0.5*(0.05 - 0.0296)/(0.1197 - 0.0296)
# Q15
x15 = 2.10 + 0.01*0.039/0.103
# Q16
f16 = 100.0**(1.0/6.0)

def line(cid, computed, expected, match):
    print(f"CLAIM {cid}: computed={computed:.8f} expected={expected} match={match}")

def close(computed, expected_str, sig):
    return round(computed, sig - int(math.floor(math.log10(abs(float(expected_str)))))-1) == float(expected_str)

line("Q1", lnP110, "-3.7540", "yes" if abs(round(lnP110,4) - (-3.7540)) < 1e-9 else "no")
line("Q2", lnG110, "-3.721524", "yes" if abs(round(lnG110,6) - (-3.721524)) < 1e-9 else "no")
line("Q3", d1, "-0.0325", "yes" if abs(round(d1,4) - (-0.0325)) < 1e-9 else "no")
line("Q4", lnP120, "-5.1920", "yes" if abs(round(lnP120,4) - (-5.1920)) < 1e-9 else "no")
line("Q5", d2, "0.0296", "yes" if abs(round(d2,4) - 0.0296) < 1e-9 else "no")
line("Q6", lnP125, "-6.2268", "yes" if abs(round(lnP125,4) - (-6.2268)) < 1e-9 else "no")
line("Q7", d25, "0.1197", "yes" if abs(round(d25,4) - 0.1197) < 1e-9 else "no")
line("Q8", lnP130, "-7.4607", "yes" if abs(round(lnP130,4) - (-7.4607)) < 1e-9 else "no")
line("Q9", ratio3, "1.298", "yes" if abs(round(ratio3,3) - 1.298) < 1e-9 else "no")
line("Q10", rel1, "0.0330", "yes" if abs(round(rel1,4) - 0.0330) < 1e-9 else "no")
line("Q11", rel25, "0.127", "yes" if abs(round(rel25,3) - 0.127) < 1e-9 else "no")
line("Q12", g1, "0.1", "yes" if abs(round(g1,1) - 0.1) < 1e-9 else "no")
line("Q13", kurt, "0.01", "yes" if abs(round(kurt,2) - 0.01) < 1e-9 else "no")
line("Q14", x14, "2.113", "yes" if abs(round(x14,3) - 2.113) < 1e-9 else "no")
line("Q15", x15, "2.104", "yes" if abs(round(x15,3) - 2.104) < 1e-9 else "no")
line("Q16", f16, "2.154", "yes" if abs(round(f16,3) - 2.154) < 1e-9 else "no")

results = [
    abs(round(lnP110,4) - (-3.7540)) < 1e-9,
    abs(round(lnG110,6) - (-3.721524)) < 1e-9,
    abs(round(d1,4) - (-0.0325)) < 1e-9,
    abs(round(lnP120,4) - (-5.1920)) < 1e-9,
    abs(round(d2,4) - 0.0296) < 1e-9,
    abs(round(lnP125,4) - (-6.2268)) < 1e-9,
    abs(round(d25,4) - 0.1197) < 1e-9,
    abs(round(lnP130,4) - (-7.4607)) < 1e-9,
    abs(round(ratio3,3) - 1.298) < 1e-9,
    abs(round(rel1,4) - 0.0330) < 1e-9,
    abs(round(rel25,3) - 0.127) < 1e-9,
    abs(round(g1,1) - 0.1) < 1e-9,
    abs(round(kurt,2) - 0.01) < 1e-9,
    abs(round(x14,3) - 2.113) < 1e-9,
    abs(round(x15,3) - 2.104) < 1e-9,
    abs(round(f16,3) - 2.154) < 1e-9,
]
m = sum(results)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {m} match, {len(results)-m} mismatch")
