import math
from fractions import Fraction

results = []

# Q1: smallest n such that 2^{-n} < 10^{-6}, i.e. 2^n > 10^6
n = 0
while 2 ** n <= 10 ** 6:
    n += 1
computed_q1 = n
expected_q1 = 20
match_q1 = math.isclose(computed_q1, expected_q1, rel_tol=1e-6)
results.append(("Q1", computed_q1, expected_q1, match_q1))

# Q2: 2^{-20} = 1/1048576 ≈ 9.5367e-7 < 1e-6
computed_q2 = 2 ** (-20)
expected_q2 = 1 / 1048576
match_q2 = math.isclose(computed_q2, expected_q2, rel_tol=1e-6)
results.append(("Q2", computed_q2, expected_q2, match_q2))

# Q3: log2(10^6) = 6 * log2(10) ≈ 19.93; ceiling = 20
log2_10 = math.log2(10)
computed_q3 = 6 * log2_10
expected_q3 = 19.93
match_q3 = math.isclose(computed_q3, expected_q3, rel_tol=1e-2)
ceil_q3 = math.ceil(computed_q3)
ceil_match = math.isclose(ceil_q3, 20, rel_tol=1e-6)
results.append(("Q3", computed_q3, expected_q3, match_q3))
results.append(("Q3-ceil", ceil_q3, 20, ceil_match))

# Q4: w^{(x+y)}_n = 2^{-n} + 2^{-n} = 2^{-(n-1)}
n_val = 20
computed_q4 = 2 ** (-n_val) + 2 ** (-n_val)
expected_q4 = 2 ** (-(n_val - 1))
match_q4 = math.isclose(computed_q4, expected_q4, rel_tol=1e-6)
results.append(("Q4", computed_q4, expected_q4, match_q4))

# Q5: R_6 <= 1/(6! * 6) = 1/4320
computed_q5 = 1 / (math.factorial(6) * 6)
expected_q5 = 1 / 4320
match_q5 = math.isclose(computed_q5, expected_q5, rel_tol=1e-6)
results.append(("Q5", computed_q5, expected_q5, match_q5))

# Q6: S_6 = sum_{k=0}^{6} 1/k! = 1957/720
S6 = sum(Fraction(1, math.factorial(k)) for k in range(7))
computed_q6 = S6
expected_q6 = Fraction(1957, 720)
match_q6 = (computed_q6 == expected_q6)
results.append(("Q6", float(computed_q6), float(expected_q6), match_q6))

# Q7: enclosure [11742/4320, 11743/4320], width 1/4320
S6_over_4320 = S6 * 4320  # should be 11742
lower = Fraction(11742, 4320)
upper = Fraction(11743, 4320)
width = upper - lower
computed_q7_lower = S6_over_4320
expected_q7_lower = 11742
match_q7_lower = (computed_q7_lower == expected_q7_lower)
computed_q7_width = width
expected_q7_width = Fraction(1, 4320)
match_q7_width = (computed_q7_width == expected_q7_width)
results.append(("Q7-lower", float(computed_q7_lower), float(expected_q7_lower), match_q7_lower))
results.append(("Q7-width", float(computed_q7_width), float(expected_q7_width), match_q7_width))

# Q8: log10(25) ≈ 1.398 decimal digits per step
computed_q8 = math.log10(25)
expected_q8 = 1.398
match_q8 = math.isclose(computed_q8, expected_q8, rel_tol=1e-3)
results.append(("Q8", computed_q8, expected_q8, match_q8))

for cid, comp, exp, m in results:
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if m else 'no'}")

total = len(results)
matched = sum(1 for _, _, _, m in results if m)
mismatch = total - matched
print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {mismatch} mismatch")
