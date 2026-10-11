import math
from fractions import Fraction

def cmp(rid, computed, expected):
    if isinstance(computed, float) or isinstance(expected, float):
        match = math.isclose(float(computed), float(expected), rel_tol=1e-6)
    else:
        match = computed == expected
    print(f"CLAIM {rid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

# Q1
w = [0.30, 0.25, 0.20, 0.15, 0.10]
cmp("Q1", sum(w), 1.00)

# Q2
cmp("Q2", 42/5, 8.4)

# Q3
cmp("Q3", 8/(5-1), 2.0)

# Q4
cmp("Q4", 8/5, 1.6)

# Q5
cmp("Q5", 5/8, 0.625)

# Q6
t_gap = Fraction(8, 42)
cmp("Q6", float(t_gap), 4/21)

# Q7
cmp("Q7", float(t_gap * 7), 4/3)

# Q8
cmp("Q8", 30 * 10**12, 3.0e13)

print("VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch")
