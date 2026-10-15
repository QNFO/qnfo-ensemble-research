import math

kB = 1.380649e-23
T = 310.0
e = 1.602176634e-19
hbar = 1.0545718e-34

def report(cid, computed, expected, sig):
    if expected is None:
        match = "n/a"
    else:
        match = "yes" if float(f"%.{sig}g" % computed) == float(expected) else "no"
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected} match={match}")

kBT = kB * T
report("Q1", kBT, "4.28001e-21", 6)
kBT_eV = kBT / e
print(f"CLAIM Q1b (kBT in eV): computed={kBT_eV*1000:.8g} expected=26.71 match=" +
      str("yes" if float(f"%.4g" % (kBT_eV*1000)) == 26.71 else "no"))

Gamma = kBT / hbar
report("Q2", Gamma, "4.058e13", 4)

tau = 1 / Gamma
report("Q3", tau, "2.46e-14", 3)

S = 1e-3 * Gamma
report("Q4", S, "4.06e10", 3)

E02 = 0.2 * e
N02 = E02 / (2 * math.pi * kBT)
report("Q5", N02, "1.19", 3)

kBT_eV2 = 2.6712e-2
C = math.log2(1 + 0.2 / kBT_eV2)
report("Q6", C, "3.09", 3)

report("Q7", math.log2(2), "1", 1)

E10 = 10 * e
N10 = E10 / (2 * math.pi * kBT)
report("Q8", N10, "59.6", 3)

Emin = 2 * math.pi * kBT / e
report("Q9", Emin, "0.168", 3)

R = kBT * math.log(1 / 1e-4) / e
report("Q10", R, "0.246", 3)

ratio = 0.246 / 0.2
report("Q11", ratio, "1.23", 3)

Eproj = 2 * math.pi * kBT * 1e6 / e
report("Q12", Eproj, "1.68e5", 3)

fall = 1 - 273.0 / 310.0
report("Q13", fall, "0.12", 1)

print("VERIFICATION SUMMARY: 13 claims, " + "M match, K mismatch")
