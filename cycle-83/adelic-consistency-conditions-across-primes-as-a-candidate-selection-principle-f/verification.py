import math
from fractions import Fraction

def p_adic_norm(n, p):
    if n == 0:
        return 0.0
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return p ** (-v)

def p_adic_norm_frac(fr, p):
    num, den = fr.numerator, fr.denominator
    return p_adic_norm(num, p) * p_adic_norm(den, p)  # |a/b|_p = |a|_p * |b|_p^{-1}? careful below

def p_adic_norm_frac_correct(fr, p):
    # |a/b|_p = p^{-v_p(a) + v_p(b)}
    def vp(n):
        n = abs(n); v = 0
        while n and n % p == 0:
            n //= p; v += 1
        return v
    return p ** (-(vp(fr.numerator) - vp(fr.denominator)))

results = {}

# Q1: x = 12
val12 = 12 * Fraction(1, 4) * Fraction(1, 3)
results["Q1"] = (float(val12), 1.0)

# Q2: x = 3/5
val35 = Fraction(3, 5) * Fraction(1, 3) * 5
results["Q2"] = (float(val35), 1.0)

# Q3: x = 137
val137 = 137 * Fraction(1, 137)
results["Q3"] = (float(val137), 1.0)

# Q4: D_P(137) with P >= 137
prod = 137 * (1 / 137)
D = abs(math.log(prod))
results["Q4"] = (D, 0.0)

# Q5: d_2(1,3)
def v_p(a, b, p):
    d = abs(a - b); v = 0
    while d % p == 0:
        d //= p; v += 1
    return v
d13 = 2 ** (-v_p(1, 3, 2))
results["Q5"] = (d13, 0.5)

# Q6: d_2(3,7)
d37 = 2 ** (-v_p(3, 7, 2))
results["Q6"] = (d37, 0.25)

# Q7: d_2(1,7) and ultrametric check
d17 = 2 ** (-v_p(1, 7, 2))
ultra = d17 <= max(d13, d37)
results["Q7"] = (d17, 0.5)
print(f"CLAIM Q7-ultra: computed={ultra} expected=True match={'yes' if ultra else 'no'}")

# Q8: S_10 = sum over primes <= 10 of p^-2
S10 = sum(Fraction(1, p * p) for p in [2, 3, 5, 7])
results["Q8"] = (float(S10), 0.421519)

for qid, (comp, exp) in results.items():
    if exp is None:
        match = "no"
    else:
        match = "yes" if math.isclose(comp, exp, rel_tol=1e-6) else "no"
    print(f"CLAIM {qid}: computed={comp} expected={exp} match={match}")

n = len(results) + 1
m = sum(1 for qid, (comp, exp) in results.items() if exp is not None and math.isclose(comp, exp, rel_tol=1e-6)) + (1 if ultra else 0)
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")
