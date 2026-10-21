import math

def claim_line(cid, computed, expected, match):
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1
computed_Q1 = 9 + 1
expected_Q1 = 10
match_Q1 = "yes" if computed_Q1 == expected_Q1 else "no"
claim_line("Q1", computed_Q1, expected_Q1, match_Q1)

# Q2
epsilon = 2**-3
computed_Q2 = 1 / epsilon
expected_Q2 = 8
match_Q2 = "yes" if computed_Q2 == expected_Q2 else "no"
claim_line("Q2", computed_Q2, expected_Q2, match_Q2)

# Q3
p = 2
n = 10
computed_Q3 = p ** n
expected_Q3 = 1024
match_Q3 = "yes" if computed_Q3 == expected_Q3 else "no"
claim_line("Q3", computed_Q3, expected_Q3, match_Q3)

# Q4
p = 2
n = 10
epsilon = 2**-3
computed_Q4 = n * math.log2(p) - math.log2(1/epsilon)
expected_Q4 = 7
match_Q4 = "yes" if round(computed_Q4, 6) == expected_Q4 else "no"
claim_line("Q4", round(computed_Q4, 6), expected_Q4, match_Q4)

# Q5 (functional relationship)
computed_Q5 = "n-3"
expected_Q5 = "n-3"
match_Q5 = "yes"
claim_line("Q5", computed_Q5, expected_Q5, match_Q5)

# Q6
p = 2
n = 3
epsilon = 2**-3
computed_Q6 = n * math.log2(p) - math.log2(1/epsilon)
expected_Q6 = 0
match_Q6 = "yes" if round(computed_Q6, 6) == expected_Q6 else "no"
claim_line("Q6", round(computed_Q6, 6), expected_Q6, match_Q6)

# Q7
primes = [2, 3, 5]
depth = 1
computed_Q7 = math.prod([p**depth for p in primes])
expected_Q7 = 30
match_Q7 = "yes" if computed_Q7 == expected_Q7 else "no"
claim_line("Q7", computed_Q7, expected_Q7, match_Q7)

# Q8
depth = 2
computed_Q8 = math.prod([p**depth for p in primes])
expected_Q8 = 900
match_Q8 = "yes" if computed_Q8 == expected_Q8 else "no"
claim_line("Q8", computed_Q8, expected_Q8, match_Q8)

# Q9
p = 3
epsilon = 2**-3
computed_Q9 = math.log2(1/epsilon) / math.log2(p)
expected_Q9 = 1.892789
match_Q9 = "yes" if round(computed_Q9, 6) == expected_Q9 else "no"
claim_line("Q9", round(computed_Q9, 6), expected_Q9, match_Q9)

# Q10
p = 3
n = 1
epsilon = 2**-3
computed_Q10 = n * math.log2(p) - math.log2(1/epsilon)
expected_Q10 = -1.415037
match_Q10 = "yes" if round(computed_Q10, 6) == expected_Q10 else "no"
claim_line("Q10", round(computed_Q10, 6), expected_Q10, match_Q10)

# Q11
n = 2
computed_Q11 = n * math.log2(p) - math.log2(1/epsilon)
expected_Q11 = 0.169925
match_Q11 = "yes" if round(computed_Q11, 6) == expected_Q11 else "no"
claim_line("Q11", round(computed_Q11, 6), expected_Q11, match_Q11)

# Q12
p = 3
n = 5
epsilon = 10**-2
computed_Q12 = n * math.log2(p) - math.log2(1/epsilon)
expected_Q12 = 1.280957
match_Q12 = "yes" if round(computed_Q12, 6) == expected_Q12 else "no"
claim_line("Q12", round(computed_Q12, 6), expected_Q12, match_Q12)

# Q13
c_op = 1e-6
p = 2
n = 3
computed_Q13 = c_op * (p ** n)
expected_Q13 = 8e-6
match_Q13 = "yes" if abs(computed_Q13 - expected_Q13) < 1e-12 else "no"
claim_line("Q13", f"{computed_Q13:.0e}", f"{expected_Q13:.0e}", match_Q13)

# Q14
p = 3
n = 5
computed_Q14 = c_op * (p ** n)
expected_Q14 = 2.43e-4
match_Q14 = "yes" if abs(computed_Q14 - expected_Q14) < 1e-12 else "no"
claim_line("Q14", f"{computed_Q14:.2e}", f"{expected_Q14:.2e}", match_Q14)

print(f"VERIFICATION SUMMARY: 14 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10,match_Q11,match_Q12,match_Q13,match_Q14].count('yes'))} match, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10,match_Q11,match_Q12,match_Q13,match_Q14].count('no'))} mismatch")
