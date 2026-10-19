import math

def fmt(value, template):
    """Format value to have the same number of decimal places as the template string."""
    if '.' in template:
        dec = len(template.split('.')[-1])
        fmt_str = f"{{:.{dec}f}}"
        return fmt_str.format(value)
    else:
        # integer template
        return str(int(round(value)))

# Q1: H = ln(p) / λ
p = 2
lam = 1
H = math.log(p) / lam
expected_Q1 = "0.693"
computed_Q1 = fmt(H, expected_Q1)
match_Q1 = "yes" if computed_Q1 == expected_Q1 else "no"
print(f"CLAIM Q1: computed={computed_Q1} expected={expected_Q1} match={match_Q1}")

# Q2: N = p^n
n = 5
N5 = p ** n
expected_Q2 = "32"
computed_Q2 = fmt(N5, expected_Q2)
match_Q2 = "yes" if computed_Q2 == expected_Q2 else "no"
print(f"CLAIM Q2: computed={computed_Q2} expected={expected_Q2} match={match_Q2}")

# Q3: I = p^n
n = 10
I10 = p ** n
expected_Q3 = "1024"
computed_Q3 = fmt(I10, expected_Q3)
match_Q3 = "yes" if computed_Q3 == expected_Q3 else "no"
print(f"CLAIM Q3: computed={computed_Q3} expected={expected_Q3} match={match_Q3}")

# Q4: A = c * p^{2n/3}
c = 1
n = 10
A10 = c * (p ** (2 * n / 3))
expected_Q4 = "101.6"
computed_Q4 = fmt(A10, expected_Q4)
match_Q4 = "yes" if computed_Q4 == expected_Q4 else "no"
print(f"CLAIM Q4: computed={computed_Q4} expected={expected_Q4} match={match_Q4}")

# Q5: S = (c/4) * p^{2n/3}
S10_max = (c / 4) * (p ** (2 * n / 3))
expected_Q5 = "25.4"
computed_Q5 = fmt(S10_max, expected_Q5)
match_Q5 = "yes" if computed_Q5 == expected_Q5 else "no"
print(f"CLAIM Q5: computed={computed_Q5} expected={expected_Q5} match={match_Q5}")

# Q6: ratio = I10 / S10_max
ratio = I10 / S10_max
expected_Q6 = "40.3"
computed_Q6 = fmt(ratio, expected_Q6)
match_Q6 = "yes" if computed_Q6 == expected_Q6 else "no"
print(f"CLAIM Q6: computed={computed_Q6} expected={expected_Q6} match={match_Q6}")

# Q7: period = ln(p)
period = math.log(p)
expected_Q7 = "0.693"
computed_Q7 = fmt(period, expected_Q7)
match_Q7 = "yes" if computed_Q7 == expected_Q7 else "no"
print(f"CLAIM Q7: computed={computed_Q7} expected={expected_Q7} match={match_Q7}")

# Q8: c = 4 * I10 / p^{2n/3}
c_needed = 4 * I10 / (p ** (2 * n / 3))
expected_Q8 = "40"
computed_Q8 = fmt(c_needed, expected_Q8)
match_Q8 = "yes" if computed_Q8 == expected_Q8 else "no"
print(f"CLAIM Q8: computed={computed_Q8} expected={expected_Q8} match={match_Q8}")

print(f"VERIFICATION SUMMARY: 8 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8].count('yes'))} match, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8].count('no'))} mismatch")
