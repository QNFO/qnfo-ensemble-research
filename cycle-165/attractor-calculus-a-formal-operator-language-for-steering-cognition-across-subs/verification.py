import math

def claim(qid, computed, expected, match):
    print(f"CLAIM {qid}: computed={computed:.8f} expected={expected} match={match}")

# Q1: DeltaV = 0 - (-1/4)
dV = 0 - (-1/4)
claim("Q1", dV, "0.25", round(dV, 8) == 0.25)

# Q2: E_imp = 2*DeltaV
E = 2 * dV
claim("Q2", E, "0.5", round(E, 8) == 0.5)

# Q3: p = sqrt(0.5)
p = math.sqrt(2 * dV)
claim("Q3", p, "0.707107", round(p, 6) == 0.707107)

# Q4: u_c = 2/(3*sqrt(3))
uc = 2 / (3 * math.sqrt(3))
claim("Q4", uc, "0.384900", round(uc, 6) == 0.384900)

# Q5: u_c^2 = 4/27
uc2 = uc ** 2
claim("Q5", uc2, "0.148148", round(uc2, 6) == 0.148148)

# Q6: T* = 0.5*27/4
Tstar = 0.5 * 27 / 4
claim("Q6", Tstar, "3.375", round(Tstar, 8) == 3.375)

# Q7: DeltaV(a) = a^2/4 at a=1
a = 1
dVa = 0 - (-(a**2) / 4)
claim("Q7", dVa, "0.25", round(dVa, 8) == 0.25)

# Q8: E_imp(a) = 2*DeltaV(a)
Ea = 2 * dVa
claim("Q8", Ea, "0.5", round(Ea, 8) == 0.5)

# Q9: u_c(a)^2 = 4a^3/27
uca = 2 * a**1.5 / (3 * math.sqrt(3))
uca2 = uca ** 2
claim("Q9", uca2, "0.148148", round(uca2, 6) == 0.148148)

# Q10: T*(a) = (a^2/2)/(4a^3/27)
Ta = (a**2 / 2) / (4 * a**3 / 27)
claim("Q10", Ta, "3.375", round(Ta, 8) == 3.375)

# Q11: -ln(1-eps)
eps = 1e-3
v11 = -math.log(1 - eps)
claim("Q11", v11, "0.0010005", round(v11, 7) == 0.0010005)

# Q12: T_d / (-ln(1-eps))
v12 = 1e6 / v11
claim("Q12", v12, "9.99500e8", round(v12, 4) == 9.99500e8)

# Q13: ln(ratio)
v13 = math.log(v12)
claim("Q13", v13, "20.722766", round(v13, 6) == 20.722766)

# Q14: DeltaV' = D * ln(ratio)
D = 0.05
v14 = D * v13
claim("Q14", v14, "1.0361383", round(v14, 7) == 1.0361383)

# Q15: delta d = DeltaV' - DeltaV
v15 = v14 - dV
claim("Q15", v15, "0.786138", round(v15, 6) == 0.786138)

# Q16: E_imp' = 2*DeltaV'
v16 = 2 * v14
claim("Q16", v16, "2.072277", round(v16, 6) == 2.072277)

n = 16
m = sum(1 for _ in [1]*n)  # placeholder replaced below
# Recount matches properly
matches = [
    round(dV, 8) == 0.25,
    round(E, 8) == 0.5,
    round(p, 6) == 0.707107,
    round(uc, 6) == 0.384900,
    round(uc2, 6) == 0.148148,
    round(Tstar, 8) == 3.375,
    round(dVa, 8) == 0.25,
    round(Ea, 8) == 0.5,
    round(uca2, 6) == 0.148148,
    round(Ta, 8) == 3.375,
    round(v11, 7) == 0.0010005,
    round(v12, 4) == 9.99500e8,
    round(v13, 6) == 20.722766,
    round(v14, 7) == 1.0361383,
    round(v15, 6) == 0.786138,
    round(v16, 6) == 2.072277,
]
m = sum(matches)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
