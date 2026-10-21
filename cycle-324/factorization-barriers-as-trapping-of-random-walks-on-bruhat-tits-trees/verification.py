import math

def fmt(x, digits):
    """Format number x with given significant digits after decimal."""
    return f"{x:.{digits}f}"

# Q1
p = 2
D = 7
V = 1 + (p + 1) * (p**D - 1) / (p - 1)
expected_Q1 = 382
match_Q1 = "yes" if V == expected_Q1 else "no"
print(f"CLAIM Q1: computed={int(V)} expected={expected_Q1} match={match_Q1}")

# Q2
d = 3
prefactor = d / ((d - 2) * math.log(d - 1))
expected_Q2 = 4.32808
# round to 5 decimal places for comparison
prefactor_rounded = round(prefactor, 5)
match_Q2 = "yes" if prefactor_rounded == expected_Q2 else "no"
print(f"CLAIM Q2: computed={fmt(prefactor,5)} expected={expected_Q2} match={match_Q2}")

# Q3 (no fixed numeric expectation)
# We just display the formula result for a generic n; no match evaluation.
print(f"CLAIM Q3: computed= prefactor * log(n) expected=None match=no")

# Q4
n4 = 382
log_n4 = math.log(n4)
T_mix_4 = prefactor * log_n4
expected_Q4 = 25.73
T_mix_4_rounded = round(T_mix_4, 2)
match_Q4 = "yes" if T_mix_4_rounded == expected_Q4 else "no"
print(f"CLAIM Q4: computed={fmt(T_mix_4,2)} expected={expected_Q4} match={match_Q4}")

# Q5
n5 = 10**6
log_n5 = math.log(n5)
T_mix_5 = prefactor * log_n5
expected_Q5 = 59.8
T_mix_5_rounded = round(T_mix_5, 1)
match_Q5 = "yes" if T_mix_5_rounded == expected_Q5 else "no"
print(f"CLAIM Q5: computed={fmt(T_mix_5,1)} expected={expected_Q5} match={match_Q5}")

# Q6
C = 1
lambda_upper = C / D
expected_Q6 = 0.1429
lambda_upper_rounded = round(lambda_upper, 4)
match_Q6 = "yes" if lambda_upper_rounded == expected_Q6 else "no"
print(f"CLAIM Q6: computed={fmt(lambda_upper,4)} expected={expected_Q6} match={match_Q6}")

# Q7
adj_low = -2 * math.sqrt(p - 1)
adj_high = 2 * math.sqrt(p - 1)
expected_Q7 = "[-2, 2]"
computed_Q7 = f"[{fmt(adj_low,0)}, {fmt(adj_high,0)}]"
match_Q7 = "yes" if computed_Q7 == expected_Q7 else "no"
print(f"CLAIM Q7: computed={computed_Q7} expected={expected_Q7} match={match_Q7}")

print(f"VERIFICATION SUMMARY: 7 claims, {sum([match_Q1, match_Q2, match_Q4, match_Q5, match_Q6, match_Q7].count('yes'))} match, {7 - sum([match_Q1, match_Q2, match_Q4, match_Q5, match_Q6, match_Q7].count('yes'))} mismatch")
