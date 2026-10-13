import math
from fractions import Fraction

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: P(L_0|00) = C(3,0)(0.9)^3 + C(3,2)(0.1)^2(0.9)
q1 = math.comb(3,0)*0.9**3 + math.comb(3,2)*0.1**2*0.9
results.append(("Q1", q1, "0.756", 3))

# Q2: P(L_1|00) = C(3,1)(0.1)(0.9)^2 + C(3,3)(0.1)^3
q2 = math.comb(3,1)*0.1*0.9**2 + math.comb(3,3)*0.1**3
results.append(("Q2", q2, "0.244", 3))

# Q3: relative gap = (0.756 - 0.729)/0.756
q3 = (0.756 - 0.729)/0.756
results.append(("Q3", q3, "0.0357", 3))

# Q4: T = n^3 + n*4^4, n = 1023, rw = 4
n = 1023
q4 = n**3 + n*4**4
results.append(("Q4", q4, "1.07e9", 3))

# Q5: T_TN = n * 2^tw, tw = sqrt(1023)
tw = math.sqrt(1023)
q5 = n * 2**tw
results.append(("Q5", q5, "4.35e12", 3))

# Q6: ratio = T_TN / T_RankDP
q6 = q5 / q4
results.append(("Q6", q6, "4.05e3", 3))

# Q7: bound = (1+u)^(2m) - 1 ≈ 2m*u, u = 2^-53, m = 1023
u = 2.0**-53
m = 1023
q7 = 2*m*u
results.append(("Q7", q7, "2.3e-13", 2))

# Q8: gap = ln(0.756) - ln(0.729)
q8 = math.log(0.756) - math.log(0.729)
results.append(("Q8", q8, "0.0364", 3))

# Q9: T = c * n * 4^k_*, t=3, n=343, k_*=4, c=10
q9 = 10 * 343 * 4**4
results.append(("Q9", q9, "8.78e5", 3))

# Q10: T_TN = n * 2^27, n = 343
q10 = 343 * 2**27
results.append(("Q10", q10, "4.60e10", 3))

# Q11: ratio = T_TN / T_RankDP (Steane)
q11 = q10 / q9
results.append(("Q11", q11, "5.2e4", 2))

# Q12: ML threshold p* = 0.5; check Z_0 = Z_1 = 1/2 at p = 1/2 for n = 3
p = 0.5
z0 = sum(math.comb(3,j)*p**j*(1-p)**(3-j) for j in range(4) if j % 2 == 0)
z1 = sum(math.comb(3,j)*p**j*(1-p)**(3-j) for j in range(4) if j % 2 == 1)
q12 = z0  # should equal 0.5
results.append(("Q12", q12, "0.5", 1))

match_count = 0
for rid, computed, expected_str, nsig in results:
    expected = float(expected_str)
    match = "yes" if sig(computed, nsig) == expected else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {rid}: computed={computed:.8g} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results)-match_count} mismatch")
