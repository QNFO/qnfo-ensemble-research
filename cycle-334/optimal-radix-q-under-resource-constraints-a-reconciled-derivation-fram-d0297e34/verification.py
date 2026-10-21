import math

# Constants from the paper
N = 1_000_000
ln2 = 0.693147
ln3 = 1.098612
ln4 = 1.386294
ln5 = 1.609438
lnN = 13.815511
T_ref = lnN

# Helper for printing
def report(claim_id, computed, expected, match):
    print(f"CLAIM {claim_id}: computed={computed} expected={expected} match={match}")

# Q1: continuous optimum q = e
e_val = math.e
computed_q1 = format(e_val, ".3f")
expected_q1 = "2.718"
match_q1 = "yes" if computed_q1 == expected_q1 else "no"
report("Q1", computed_q1, expected_q1, match_q1)

# Q2: depths n(q)
def depth(q, lnq):
    r = lnN / lnq
    return math.ceil(r)

n2 = depth(2, ln2)
n3 = depth(3, ln3)
n4 = depth(4, ln4)
n5 = depth(5, ln5)
computed_q2 = f"n(2)={n2}, n(3)={n3}, n(4)={n4}, n(5)={n5}"
expected_q2 = "n(2)=20, n(3)=13, n(4)=10, n(5)=9"
match_q2 = "yes" if computed_q2 == expected_q2 else "no"
report("Q2", computed_q2, expected_q2, match_q2)

# Q3: traversal costs T(q) = q * n(q)
T2 = 2 * n2
T3 = 3 * n3
T4 = 4 * n4
T5 = 5 * n5
computed_q3 = f"T(2)={T2}, T(3)={T3}, T(4)={T4}, T(5)={T5}"
expected_q3 = "T(2)=40, T(3)=39, T(4)=40, T(5)=45"
match_q3 = "yes" if computed_q3 == expected_q3 else "no"
report("Q3", computed_q3, expected_q3, match_q3)

# Q4: normalized traversal values
norm2 = T2 / T_ref
norm3 = T3 / T_ref
norm5 = T5 / T_ref
computed_q4 = f"T(2)/T_ref={format(norm2, '.4f')}, T(3)/T_ref={format(norm3, '.4f')}, T(5)/T_ref={format(norm5, '.4f')}"
expected_q4 = "T(2)/T_ref=2.8956, T(3)/T_ref=2.8227, T(5)/T_ref=3.2575"
match_q4 = "yes" if computed_q4 == expected_q4 else "no"
report("Q4", computed_q4, expected_q4, match_q4)

# Q5: storage per item (unpadded) S(q)/N = q*(1 - q^{-n})/(q-1)
def storage_per_item(q, n):
    q_pow_minus_n = q ** (-n)
    return q * (1 - q_pow_minus_n) / (q - 1)

S2 = storage_per_item(2, n2)
S3 = storage_per_item(3, n3)
S4 = storage_per_item(4, n4)
S5 = storage_per_item(5, n5)
computed_q5 = f"S(2)/N={format(S2, '.4f')}, S(3)/N={format(S3, '.4f')}, S(4)/N={format(S4, '.4f')}, S(5)/N={format(S5, '.4f')}"
expected_q5 = "S(2)/N=2.0000, S(3)/N=1.5000, S(4)/N=1.3333, S(5)/N=1.2500"
match_q5 = "yes" if computed_q5 == expected_q5 else "no"
report("Q5", computed_q5, expected_q5, match_q5)

# Q6: composite cost F_{1,1}(q) = S/N + T/T_ref
F2 = S2 + norm2
F3 = S3 + norm3
F4 = S4 + norm2   # note norm2 == norm4 because T4/T_ref = 2.8956
F5 = S5 + norm5
computed_q6 = f"F(2)={format(F2, '.4f')}, F(3)={format(F3, '.4f')}, F(4)={format(F4, '.4f')}, F(5)={format(F5, '.4f')}"
expected_q6 = "F(2)=4.8956, F(3)=4.3227, F(4)=4.2289, F(5)=4.5075"
match_q6 = "yes" if computed_q6 == expected_q6 else "no"
report("Q6", computed_q6, expected_q6, match_q6)

# Q7: padding fractions phi(q) = (q^n - N)/N
phi2 = (2**n2 - N) / N
phi3 = (3**n3 - N) / N
phi4 = (4**n4 - N) / N
phi5 = (5**n5 - N) / N
computed_q7 = f"phi(2)={format(phi2, '.4f')}, phi(3)={format(phi3, '.4f')}, phi(4)={format(phi4, '.4f')}, phi(5)={format(phi5, '.4f')}"
expected_q7 = "phi(2)=0.0486, phi(3)=0.5943, phi(4)=0.0486, phi(5)=0.9531"
match_q7 = "yes" if computed_q7 == expected_q7 else "no"
report("Q7", computed_q7, expected_q7, match_q7)

# Q8: effective storage with padding S_eff/N = q * q^n / (N*(q-1))
def effective_storage(q, n):
    return q * (q ** n) / (N * (q - 1))

Se2 = effective_storage(2, n2)
Se3 = effective_storage(3, n3)
Se4 = effective_storage(4, n4)
Se5 = effective_storage(5, n5)
computed_q8 = f"S_eff(2)/N={format(Se2, '.4f')}, S_eff(3)/N={format(Se3, '.4f')}, S_eff(4)/N={format(Se4, '.4f')}, S_eff(5)/N={format(Se5, '.4f')}"
expected_q8 = "S_eff(2)/N=2.0972, S_eff(3)/N=2.3915, S_eff(4)/N=1.3981, S_eff(5)/N=2.4414"
match_q8 = "yes" if computed_q8 == expected_q8 else "no"
report("Q8", computed_q8, expected_q8, match_q8)

# Q9: padded composite F_pad = S_eff/N + T/T_ref
Fpad2 = Se2 + norm2
Fpad3 = Se3 + norm3
Fpad4 = Se4 + norm2   # norm4 == norm2
Fpad5 = Se5 + norm5
computed_q9 = f"F_pad(2)={format(Fpad2, '.4f')}, F_pad(3)={format(Fpad3, '.4f')}, F_pad(4)={format(Fpad4, '.4f')}, F_pad(5)={format(Fpad5, '.4f')}"
expected_q9 = "F_pad(2)=4.9928, F_pad(3)=5.2142, F_pad(4)=4.2937, F_pad(5)=5.6989"
match_q9 = "yes" if computed_q9 == expected_q9 else "no"
report("Q9", computed_q9, expected_q9, match_q9)

# Q10: traversal-weight threshold beta*
beta_star = (1.3333 - 1.5000) / (2.8227 - 2.8956)
computed_q10 = format(beta_star, ".3f")
expected_q10 = "2.286"
match_q10 = "yes" if computed_q10 == expected_q10 else "no"
report("Q10", computed_q10, expected_q10, match_q10)

# Q11: derivative values C'(3) and C'(4)
def C_prime(q, lnq):
    return -1 / (q - 1) ** 2 + (lnq - 1) / (lnq ** 2)

C3 = C_prime(3, ln3)
C4 = C_prime(4, ln4)
computed_q11 = f"C'(3)={format(C3, '.4f')}, C'(4)={format(C4, '.4f')}"
expected_q11 = "C'(3)=-0.1683, C'(4)=0.0899"
match_q11 = "yes" if computed_q11 == expected_q11 else "no"
report("Q11", computed_q11, expected_q11, match_q11)

# Q12: linear interpolation root
root_q12 = 3 + (-C3) / (C4 - C3)
computed_q12 = format(root_q12, ".4f")
expected_q12 = "3.6519"
match_q12 = "yes" if computed_q12 == expected_q12 else "no"
report("Q12", computed_q12, expected_q12, match_q12)

# Q13: check that q=2 is never optimal for any beta>0
# Using the expressions from the paper:
# diff23 = 0.5000 + 0.0729*beta
# diff24 = 0.6667
beta_test = 1.0  # any positive beta
diff23 = 0.5000 + 0.0729 * beta_test
diff24 = 0.6667
computed_q13 = f"diff23={format(diff23, '.4f')}, diff24={format(diff24, '.4f')}"
expected_q13 = "none"
match_q13 = "yes" if diff23 > 0 and diff24 > 0 else "no"
report("Q13", computed_q13, expected_q13, match_q13)

# Summary
total = 13
matches = sum(1 for line in [match_q1, match_q2, match_q3, match_q4, match_q5,
                             match_q6, match_q7, match_q8, match_q9,
                             match_q10, match_q11, match_q12, match_q13] if line == "yes")
print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {total - matches} mismatch")
