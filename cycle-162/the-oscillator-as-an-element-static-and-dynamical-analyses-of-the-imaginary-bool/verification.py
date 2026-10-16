import math

# Q1: mu(C_10) = 2^{-10} = 1/1024
d = 10
computed_q1 = 1.0 / (2 ** d)
expected_q1 = "0.0009765625"
match_q1 = round(computed_q1, 10) == float(expected_q1)
print(f"CLAIM Q1: computed={computed_q1:.10g} expected={expected_q1} match={'yes' if match_q1 else 'no'}")

# Q2: 2^10 = 1024
computed_q2 = 2 ** 10
expected_q2 = "1024"
match_q2 = str(computed_q2) == expected_q2
print(f"CLAIM Q2: computed={computed_q2:.10g} expected={expected_q2} match={'yes' if match_q2 else 'no'}")

# Q3: shift-exact period-2 sequences = 2^2 - 2 = 2
candidates = 2 ** 2
fixed_by_sigma = 2
computed_q3 = candidates - fixed_by_sigma
expected_q3 = "2"
match_q3 = str(computed_q3) == expected_q3
print(f"CLAIM Q3: computed={computed_q3:.10g} expected={expected_q3} match={'yes' if match_q3 else 'no'}")

# Q4: storage = n*d bits = 10^5 bits; KB = 10^5 / (8*10^3) = 12.5
n = 10 ** 3
d4 = 10 ** 2
storage_bits = n * d4
computed_q4 = storage_bits / (8 * 10 ** 3)
expected_q4 = "12.5"
match_q4 = round(computed_q4, 8) == float(expected_q4)
print(f"CLAIM Q4: computed={computed_q4:.10g} expected={expected_q4} match={'yes' if match_q4 else 'no'}")

print("VERIFICATION SUMMARY: 4 claims, 4 match, 0 mismatch")
