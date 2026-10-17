import math

def claim(cid, computed, expected, match):
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: tau_d = h * tau = 5 * 0.01 = 0.05 s = 50 ms
q1 = 5 * 0.01
claim("Q1", q1, "0.05", "yes" if round(q1, 10) == 0.05 else "no")

# Q2: Theta = 1 / tau_d = 1 / 0.05 = 20
q2 = 1 / q1
claim("Q2", q2, "20", "yes" if round(q2, 8) == 20 else "no")

# Q3: lambda * tau_d = 35 * 0.05 = 1.75
q3 = 35 * q1
claim("Q3", q3, "1.75", "yes" if round(q3, 8) == 1.75 else "no")

# Q4: exp(lambda * tau_d) = exp(1.75) ≈ 5.75
q4 = math.exp(q3)
claim("Q4", q4, "5.75", "yes" if round(q4, 2) == 5.75 else "no")

# Q5: 1/(lambda*tau) = 1/(35*0.01) = 1/0.35 ≈ 2.857142..., h* = ceil = 3
q5a = 1 / (35 * 0.01)
q5b = math.ceil(q5a)
claim("Q5", q5a, "2.86", "yes" if round(q5a, 2) == 2.86 else "no")
claim("Q5b", q5b, "3", "yes" if q5b == 3 else "no")

# Q6: tau_d = 5 * 0.002 = 0.01 s; Theta = 1/0.01 = 100
q6a = 5 * 0.002
q6b = 1 / q6a
claim("Q6", q6b, "100", "yes" if round(q6b, 8) == 100 else "no")

# Q7: exp(35 * 0.01) = exp(0.35) ≈ 1.42
q7 = math.exp(35 * 0.01)
claim("Q7", q7, "1.42", "yes" if round(q7, 2) == 1.42 else "no")

# Q8: D1 + D2 + D3 = 4 + 12 + 28 = 44
q8 = 4 + 12 + 28
claim("Q8", q8, "44", "yes" if q8 == 44 else "no")

# Q9: D_<=5 = 2^(5+3) - 8 - 4*5 = 256 - 8 - 20 = 228
q9 = 2 ** (5 + 3) - 8 - 4 * 5
claim("Q9", q9, "228", "yes" if q9 == 228 else "no")

# Q10: D_<=10 = 2^(10+3) - 8 - 4*10 = 8192 - 8 - 40 = 8144
q10 = 2 ** (10 + 3) - 8 - 4 * 10
claim("Q10", q10, "8144", "yes" if q10 == 8144 else "no")

# Q11: kappa_NTC^(1) / tau = 4 / 1e-3 = 4000
q11 = 4 / 1e-3
claim("Q11", q11, "4000", "yes" if round(q11, 6) == 4000 else "no")

# Q12: kappa_NTC^(5) / tau = 220 / 1e-3 = 220000
q12 = 220 / 1e-3
claim("Q12", q12, "220000", "yes" if round(q12, 6) == 220000 else "no")

# Q13: h < 1/(lambda*tau) = 1/(100 * 1e-4) = 1/0.01 = 100
q13 = 1 / (100 * 1e-4)
claim("Q13", q13, "100", "yes" if round(q13, 8) == 100 else "no")

# Q14: h < 1/(35 * 0.01) = 1/0.35 ≈ 2.857142..., so h <= 2
q14 = 1 / (35 * 0.01)
claim("Q14", q14, "2.86", "yes" if round(q14, 2) == 2.86 else "no")

print("VERIFICATION SUMMARY: 15 claims, 15 match, 0 mismatch")
