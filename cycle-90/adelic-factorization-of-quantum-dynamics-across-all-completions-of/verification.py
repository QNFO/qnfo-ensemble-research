import math

f1 = 0.9990
f2 = 0.9956
f3 = 0.9870

# Q1
mean = (f1 + f2 + f3) / 3
expected_mean = 0.9938666666666667
match1 = math.isclose(mean, expected_mean, rel_tol=1e-6)
print(f"CLAIM Q1: computed={mean:.10f} expected={expected_mean:.10f} match={'yes' if match1 else 'no'}")

# Q2
prod = f1 * f2 * f3
expected_prod = 0.9816745428
match2 = math.isclose(prod, expected_prod, rel_tol=1e-6)
print(f"CLAIM Q2: computed={prod:.10f} expected={expected_prod:.10f} match={'yes' if match2 else 'no'}")

# Q3
gap = mean - prod
expected_gap = 0.0121921238
match3 = math.isclose(gap, expected_gap, rel_tol=1e-6)
print(f"CLAIM Q3: computed={gap:.10f} expected={expected_gap:.10f} match={'yes' if match3 else 'no'}")

total = 3
matched = sum([match1, match2, match3])
print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {total - matched} mismatch")
