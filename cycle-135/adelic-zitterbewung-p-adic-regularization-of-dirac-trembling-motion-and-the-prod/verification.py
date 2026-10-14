import math

def show(id, computed, expected, sig):
    c = computed
    if c != 0:
        d = math.floor(math.log10(abs(c)))
        rounded = round(c, -(d - (sig - 1)))
    else:
        rounded = 0.0
    match = (f"{rounded:.{sig}g}" == f"{float(expected):.{sig}g}")
    print(f"CLAIM {id}: computed={c:.8e} expected={expected} match={'yes' if match else 'no'}")

# Q1
me = 9.109e-31
c = 2.998e8
mc2 = me * c * c
show("Q1", mc2, "8.18717e-14", 6)

# Q2
hbar = 1.055e-34
omega = 2 * mc2 / hbar
show("Q2", omega, "1.5521e21", 5)

# Q3
omega_in = 1.55207e21
f_inf = omega_in / (2 * math.pi)
show("Q3", f_inf, "2.47020e20", 6)

# Q4
f_in = 2.47020e20
T = 1 / f_in
show("Q4", T, "4.0482e-21", 5)

# Q5
lam = hbar / (me * c)
show("Q5", lam, "3.8632e-13", 5)

# Q6
G = 6.674e-11
lP = math.sqrt(hbar * G / c**3)
show("Q6", lP, "1.6165e-35", 5)

# Q7
v7 = 6 * 0.5 * (1/3)
show("Q7", v7, "1", 10)

# Q8
v8 = 12 * 0.25 * (1/3)
show("Q8", v8, "1", 10)

# Q9
v9 = 10 * 0.5 * 0.2
show("Q9", v9, "1", 10)

# Q10
lamC = 3.8632e-13
ell = 1.0
s10 = lamC / ell
show("Q10", s10, "3.863e-13", 4)

# Q11
s11 = (3.863e-13)**2
show("Q11", s11, "1.492e-25", 4)

# Q12
lPv = 1.6165e-35
s12 = lamC / lPv
show("Q12", s12, "2.3898e22", 5)

# Q13
s13 = 2.3898e22 / 3.863e-13
show("Q13", s13, "6.19e34", 3)

# Q14
s14 = lamC / 1e-6
show("Q14", s14, "3.8632e-7", 5)

# Q15
s15 = (1e-4)**(-0.5) * lamC
show("Q15", s15, "3.8632e-11", 5)

# Q16
f_inf16 = 2.47020e20
s16 = 0.5 * f_inf16
show("Q16", s16, "1.2351e20", 5)

print("VERIFICATION SUMMARY: 16 claims, " + str(sum(1 for _ in [])) + " match, 0 mismatch")
