import math

def fmt(x, sig=8):
    # format with at least sig significant digits, removing trailing zeros
    s = f"{x:.{sig}g}"
    return s

# Q1
baseline = 61.15
explanation = 69.29
delta = explanation - baseline
expected_q1 = "8.14"
match_q1 = fmt(delta, 4) == expected_q1
print(f"CLAIM Q1: computed={fmt(delta,8)} expected={expected_q1} match={'yes' if match_q1 else 'no'}")

# Q2
sd = 0.022
n = 14
se = sd / math.sqrt(n)
expected_q2 = "0.00588"
# round to 5 decimal places for comparison
match_q2 = f"{se:.5f}" == expected_q2
print(f"CLAIM Q2: computed={fmt(se,8)} expected={expected_q2} match={'yes' if match_q2 else 'no'}")

# Q3
z = 1.96
me = z * se
expected_q3 = "0.0115"
match_q3 = f"{me:.4f}" == expected_q3
print(f"CLAIM Q3: computed={fmt(me,8)} expected={expected_q3} match={'yes' if match_q3 else 'no'}")

# Q4
mean_perf = 0.821
lower = mean_perf - me
expected_q4 = "0.8095"
match_q4 = f"{lower:.4f}" == expected_q4
print(f"CLAIM Q4: computed={fmt(lower,8)} expected={expected_q4} match={'yes' if match_q4 else 'no'}")

# Q5
upper = mean_perf + me
expected_q5 = "0.8325"
match_q5 = f"{upper:.4f}" == expected_q5
print(f"CLAIM Q5: computed={fmt(upper,8)} expected={expected_q5} match={'yes' if match_q5 else 'no'}")

# Q6
sum_delta = delta  # only one study
count = 1
avg_delta = sum_delta / count
expected_q6 = "8.14"
match_q6 = fmt(avg_delta,4) == expected_q6
print(f"CLAIM Q6: computed={fmt(avg_delta,8)} expected={expected_q6} match={'yes' if match_q6 else 'no'}")

# Q7
pm_salary = 120000
pm_fte = 0.2
analyst_salary = 90000
analyst_fte = 0.2
duration_factor = 0.5
cost = (pm_salary * pm_fte + analyst_salary * analyst_fte) * duration_factor
expected_q7 = "21000"
match_q7 = f"{cost:.0f}" == expected_q7
print(f"CLAIM Q7: computed={fmt(cost,8)} expected={expected_q7} match={'yes' if match_q7 else 'no'}")

# Q8
software = 5000
incentives = 4000
total = cost + software + incentives
expected_q8 = "30000"
match_q8 = f"{total:.0f}" == expected_q8
print(f"CLAIM Q8: computed={fmt(total,8)} expected={expected_q8} match={'yes' if match_q8 else 'no'}")

print(f"VERIFICATION SUMMARY: 8 claims, {sum([match_q1, match_q2, match_q3, match_q4, match_q5, match_q6, match_q7, match_q8])} match, {8 - sum([match_q1, match_q2, match_q3, match_q4, match_q5, match_q6, match_q7, match_q8])} mismatch")
