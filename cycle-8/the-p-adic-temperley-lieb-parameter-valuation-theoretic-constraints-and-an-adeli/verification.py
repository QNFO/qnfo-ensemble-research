import math
from fractions import Fraction

def vp(frac, p):
    n, d = frac.numerator, frac.denominator
    k = 0
    while n % p == 0:
        n //= p; k += 1
    while d % p == 0:
        d //= p; k -= 1
    return k

def padic_norm(frac, p):
    return float(p) ** (-vp(frac, p))

results = []

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    results.append(match == "yes")

# Q1-Q4: delta_p = p + 1/p, v_p = -1, |delta_p|_p = p
for cid, p, exp_delta, exp_v, exp_norm in [
    ("Q1", 2, Fraction(5, 2), -1, 2.0),
    ("Q2", 3, Fraction(10, 3), -1, 3.0),
    ("Q3", 5, Fraction(26, 5), -1, 5.0),
    ("Q4", 7, Fraction(50, 7), -1, 7.0),
]:
    delta = Fraction(p) + Fraction(1, p)
    v = vp(delta, p)
    norm = padic_norm(delta, p)
    check(cid + "a", delta, exp_delta)
    check(cid + "b", v, exp_v)
    check(cid + "c", norm, exp_norm)

# Q5-Q8: d_2 = (p^4 + p^2 + 1)/p^2, v_p = -2, |d_2|_p = p^2
for cid, p, exp_d, exp_v, exp_norm in [
    ("Q5", 2, Fraction(21, 4), -2, 4.0),
    ("Q6", 3, Fraction(91, 9), -2, 9.0),
    ("Q7", 5, Fraction(651, 25), -2, 25.0),
    ("Q8", 7, Fraction(2451, 49), -2, 49.0),
]:
    d2 = Fraction(p**4 + p**2 + 1, p**2)
    v = vp(d2, p)
    norm = padic_norm(d2, p)
    check(cid + "a", d2, exp_d)
    check(cid + "b", v, exp_v)
    check(cid + "c", norm, exp_norm)

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
