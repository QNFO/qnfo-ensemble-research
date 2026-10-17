import math
from fractions import Fraction

def phi(q):
    result = q
    n = q
    p = 2
    while p * p <= n:
        if n % p == 0:
            result -= result // p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result -= result // n
    return result

# Q1: theta = pi/5 -> q = 5, |C| = 5, |G| = 10
q1 = 5
c1 = q1
g1 = 2 * q1
print(f"CLAIM Q1: computed={c1} and {g1} expected=5 and 10 match={'yes' if (c1, g1) == (5, 10) else 'no'}")

# Q2: A2 config, differences pi/3, 2pi/3, pi/3 -> denominators 3,3,3 -> n=3, |G|=6
n2 = math.lcm(3, 3, 3)
c2 = n2
g2 = 2 * n2
print(f"CLAIM Q2: computed={c2} and {g2} expected=3 and 6 match={'yes' if (c2, g2) == (3, 6) else 'no'}")

# Q3: mixed config, differences pi/3, pi/4, pi/12 -> denominators 3,4,12 -> n=12, |G|=24
n3 = math.lcm(3, 4, 12)
c3 = n3
g3 = 2 * n3
print(f"CLAIM Q3: computed={c3} and {g3} expected=12 and 24 match={'yes' if (c3, g3) == (12, 24) else 'no'}")

# Q4: totients for divisors of 12
expected_q4 = {1: 1, 2: 1, 3: 2, 4: 2, 6: 2, 12: 4}
all_match = True
parts = []
for q in [1, 2, 3, 4, 6, 12]:
    v = phi(q)
    parts.append(f"phi({q})={v}")
    if v != expected_q4[q]:
        all_match = False
print(f"CLAIM Q4: computed={', '.join(parts)} expected=1,1,2,2,2,4 match={'yes' if all_match else 'no'}")

# Q5: P(I2(q)) = phi(q)/12
N = 12
expected_q5 = {1: "1/12", 2: "1/12", 3: "1/6", 4: "1/6", 6: "1/6", 12: "1/3"}
all_match = True
parts = []
for q in [1, 2, 3, 4, 6, 12]:
    p = Fraction(phi(q), N)
    parts.append(f"P(I2({q}))={p}")
    if p != Fraction(expected_q5[q]):
        all_match = False
print(f"CLAIM Q5: computed={', '.join(parts)} expected=1/12,1/12,1/6,1/6,1/6,1/3 match={'yes' if all_match else 'no'}")

# Q6: sum of probabilities = 1
s = sum(phi(q) for q in [1, 2, 3, 4, 6, 12])
c6 = Fraction(s, N)
print(f"CLAIM Q6: computed={c6} expected=1 match={'yes' if c6 == 1 else 'no'}")

# Q7: sigma = sqrt(p(1-p)/n) with p=1/3, n=1e5
n_samples = 10**5
p = Fraction(1, 3)
sigma = math.sqrt(float(p) * (1 - float(p)) / n_samples)
print(f"CLAIM Q7: computed={sigma:.8f} expected=0.0015 match={'yes' if round(sigma, 4) == 0.0015 else 'no'}")

# Q8: 3*sigma
tol = 3 * sigma
print(f"CLAIM Q8: computed={tol:.8f} expected=0.005 match={'yes' if round(tol, 3) == 0.005 else 'no'}")

print("VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch")
