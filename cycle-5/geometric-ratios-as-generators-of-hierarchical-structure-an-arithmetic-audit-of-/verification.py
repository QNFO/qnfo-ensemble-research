import math
from fractions import Fraction

phi = (1 + math.sqrt(5)) / 2

def report(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) and isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: [3]_phi = phi^3 - phi^-3 = 4 exactly
c = phi**3 - phi**-3
results.append(report("Q1", c, 4.0))

# Q2: [4]_phi = 3*sqrt(5)
c = phi**4 - phi**-4
results.append(report("Q2", c, 3 * math.sqrt(5)))

# Q3: [5]_phi = 11 exactly
c = phi**5 - phi**-5
results.append(report("Q3", c, 11.0))

# Q4: [6]_phi = 8*sqrt(5)
c = phi**6 - phi**-6
results.append(report("Q4", c, 8 * math.sqrt(5)))

# Q5: Fibonacci ultrametric counterexample
d23 = Fraction(1, 2) ** 1          # 2^-gcd(2,3) = 2^-1
d26 = Fraction(1, 4)               # 2^-gcd(2,6) = 2^-2
d36 = Fraction(1, 8)               # 2^-gcd(3,6) = 2^-3
violates = d23 > max(d26, d36)
results.append(report("Q5", violates, True))

# Q6: 10 of 25 primes below 100 satisfy p ≡ ±1 (mod 5)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [p for p in range(2, 100) if is_prime(p)]
adm = [p for p in primes if p % 5 in (1, 4)]
frac = len(adm) / len(primes)
results.append(report("Q6", (len(adm), len(primes), frac), (10, 25, 0.4)))

# Q7: [3]_e
e = math.e
c = (e**3 - e**-3) / (e - e**-1)
results.append(report("Q7", c, 8.524391))

# Q8: [3]_pi
p = math.pi
c = (p**3 - p**-3) / (p - p**-1)
results.append(report("Q8", c, 10.970926))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
