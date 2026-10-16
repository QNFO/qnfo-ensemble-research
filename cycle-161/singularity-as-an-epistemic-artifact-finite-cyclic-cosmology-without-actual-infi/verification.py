import math
from fractions import Fraction

def report(cid, computed, expected, match):
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: a_max/a_0 = Omega_0/(Omega_0-1) at Omega_0 = 1.2 -> 6
q1 = 1.2 / (1.2 - 1.0)
report("Q1", f"{q1:.8f}", "6", "yes" if round(q1, 8) == 6.0 else "no")

# Q2: rho(a_max) = rho_0/6^3 = 1/216 ≈ 4.63e-3 rho_0
q2 = 1.0 / 6**3
report("Q2", f"{q2:.8f}", "0.00463", "yes" if round(q2, 5) == 0.00463 else "no")

# Q3: a_max/a_0 at Omega_0 = 1.0005 -> 2001
q3 = 1.0005 / (1.0005 - 1.0)
report("Q3", f"{q3:.8f}", "2001", "yes" if round(q3, 8) == 2001.0 else "no")

# Q4: rho(a_max) = 1/2001^3 ≈ 1.25e-10 rho_0
q4 = 1.0 / 2001**3
report("Q4", f"{q4:.8e}", "1.25e-10", "yes" if round(q4, 12) == round(1.25e-10, 12) else "no")

# Q5: cot(5e-4) ≈ 1/x - x/3 at x = 5e-4 -> 1999.99983 (paper states ≈2000)
x = 5e-4
q5 = 1.0/x - x/3.0
q5_exact = 1.0/math.tan(x)
report("Q5", f"{q5:.8f}", "2000", "yes" if round(q5, 4) == 2000.0 else "no")

# Q6: H_0 = 67.4e3 / 3.0857e22 = 2.184e-18 s^-1
q6 = 67.4e3 / 3.0857e22
report("Q6", f"{q6:.8e}", "2.184e-18", "yes" if round(q6*1e21, 2) == 2.184 else "no")

# Q7: D_H = c/H_0 = 2.998e8 / 2.184e-18 = 1.373e26 m
q7 = 2.998e8 / (67.4e3 / 3.0857e22)
report("Q7", f"{q7:.8e}", "1.373e26", "yes" if round(q7*1e-26, 3) == 1.373 else "no")

# Q8: N = D_H / l_P = 1.373e26 / 1.616e-35 ≈ 8.50e60
q8 = q7 / 1.616e-35
report("Q8", f"{q8:.8e}", "8.50e60", "yes" if round(q8*1e-60, 2) == 8.50 else "no")

# Q9: D_e[Gly] = 1.373e26 / 9.461e24 ≈ 14.5
q9 = q7 / 9.461e24
report("Q9", f"{q9:.8f}", "14.5", "yes" if round(q9, 1) == 14.5 else "no")

# Q10: R = 0.0046/0.0031 ≈ 1.48
q10 = 0.0046 / 0.0031
report("Q10", f"{q10:.8f}", "1.48", "yes" if round(q10, 2) == 1.48 else "no")

# Q11: sigma_R = (A_kin/A_LSS^2)*sigma_A = (0.0046/0.0031^2)*0.0016 ≈ 0.76
q11 = (0.0046 / 0.0031**2) * 0.0016
report("Q11", f"{q11:.8f}", "0.76", "yes" if round(q11, 2) == 0.76 else "no")

n = 11
m = sum(1 for v in [round(q1,8)==6.0, round(q2,5)==0.00463, round(q3,8)==2001.0,
                    round(q4,12)==round(1.25e-10,12), round(q5,4)==2000.0,
                    round(q6*1e21,2)==2.184, round(q7*1e-26,3)==1.373,
                    round(q8*1e-60,2)==8.50, round(q9,1)==14.5,
                    round(q10,2)==1.48, round(q11,2)==0.76] if v)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n-m} mismatch")
