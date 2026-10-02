# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "[3]_φ = 4 exactly",
    "inputs": "φ^3 = 4.236068, φ^(-3) = 0.236068",
    "formula": "[3]_φ = φ^3 − φ^(-3) = 4.236068 − 0.236068 = 4"
  },
  {
    "id": "Q2",
    "statement": "[4]_φ = 3√5 ≈ 6.708204",
    "inputs": "φ^4 = 6.854102, φ^(-4) = 0.145898, √5 = 2.236068",
    "formula": "[4]_φ = φ^4 − φ^(-4) = 6.854102 − 0.145898 = 6.708204 = 3√5"
  },
  {
    "id": "Q3",
    "statement": "[5]_φ = 11 exactly",
    "inputs": "φ^5 = 11.090170, φ^(-5) = 0.090170",
    "formula": "[5]_φ = 11.090170 − 0.090170 = 11"
  },
  {
    "id": "Q4",
    "statement": "[6]_φ = 8√5 ≈ 17.888544",
    "inputs": "φ^6 = 17.944272, φ^(-6) = 0.055728, √5 = 2.236068",
    "formula": "[6]_φ = 17.944272 − 0.055728 = 17.888544 = 8√5"
  },
  {
    "id": "Q5",
    "statement": "Fibonacci ultrametric counterexample violates strong triangle inequality",
    "inputs": "m=2, n=3, ℓ=6",
    "formula": "d(2,3) = 2^(−1) = 1/2 > max(d(2,6), d(3,6)) = max(1/4, 1/8) = 1/4"
  },
  {
    "id": "Q6",
    "statement": "10 of the 25 primes below 100 satisfy p ≡ ±1 (mod 5), fraction 0.4",
    "inputs": "admissible primes: 11, 19, 29, 31, 41, 59, 61, 71, 79, 89; total 25 primes below 100",
    "formula": "10/25 = 0.4"
  },
  {
    "id": "Q7",
    "statement": "[3]_e ≈ 8.524391",
    "inputs": "e^3 = 20.085537, e^(−3) = 0.049787, e − e^(−1) = 2.350402",
    "formula": "[3]_e = (20.085537 − 0.049787)/2.350402 ≈ 8.524391"
  },
  {
    "id": "Q8",
    "statement": "[3]_π ≈ 10.970926",
    "inputs": "π^3 = 31.006277, π^(−3) = 0.032252, π − π^(−1) = 2.823283",
    "formula": "[3]_π = (31.006277 − 0.032252)/2.823283 ≈ 10.970926"
  }
]

## Script
```python
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

```

## Execution output
```
CLAIM Q1: computed=4.0 expected=4.0 match=yes
CLAIM Q2: computed=6.70820393249937 expected=6.708203932499369 match=yes
CLAIM Q3: computed=11.000000000000002 expected=11.0 match=yes
CLAIM Q4: computed=17.888543819998322 expected=17.88854381999832 match=yes
CLAIM Q5: computed=True expected=True match=yes
CLAIM Q6: computed=(10, 25, 0.4) expected=(10, 25, 0.4) match=yes
CLAIM Q7: computed=8.524391382167263 expected=8.524391 match=yes
CLAIM Q8: computed=10.970925584731695 expected=10.970926 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
