import math
from fractions import Fraction

def check(cid, computed, expected):
    if expected is None:
        match = "n/a"
    else:
        if isinstance(computed, float) or isinstance(expected, float):
            match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
        else:
            match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: absorbing fraction f(3) = (4^3 - 3^3)/4^3
total3 = 4**3          # 64
free3 = 3**3           # 27
absorbing3 = total3 - free3
f3 = Fraction(absorbing3, total3)
results.append(check("Q1", f3, Fraction(37, 64)))
print(f"  (decimal: {float(f3)})")

# Q2: total epistemic profiles 4^3
results.append(check("Q2", 4**3, 64))

# Q3: absorbing contradictory profiles 64 - 27
results.append(check("Q3", 64 - 27, 37))

# Q3b: contradiction-free profiles 3^3
results.append(check("Q3b", 3**3, 27))

# Q4: f(10) = 1 - (3/4)^10 = 989527/1048576
num10 = 4**10 - 3**10
den10 = 4**10
f10 = Fraction(num10, den10)
results.append(check("Q4", f10, Fraction(989527, 1048576)))
print(f"  (decimal: {float(f10):.7f})")

# Q5: average profiles per perceived move set 64/8
results.append(check("Q5", Fraction(64, 8), Fraction(8, 1)))

# Q6: number of distinct perceived move sets at most 2^3
results.append(check("Q6", 2**3, 8))

# Q7: preimage profiles per move set 2^3
results.append(check("Q7", 2**3, 8))

n = len(results)
m = sum(1 for r in results if r)
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")
