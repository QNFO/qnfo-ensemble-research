# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Adelic product formula for x=12: product over all places of |12|_v equals 1",
    "inputs": "|12|_inf=12, |12|_2=1/4, |12|_3=1/3, |12|_p=1 for p not in {2,3}",
    "formula": "12 * (1/4) * (1/3) = 1"
  },
  {
    "id": "Q2",
    "statement": "Adelic product formula for x=3/5: product over all places equals 1",
    "inputs": "|3/5|_inf=3/5, |3/5|_3=1/3, |3/5|_5=5, |3/5|_p=1 otherwise",
    "formula": "(3/5) * (1/3) * 5 = 1"
  },
  {
    "id": "Q3",
    "statement": "Adelic product formula for x=137 (prime): 137 * 137^{-1} = 1",
    "inputs": "|137|_inf=137, |137|_137=1/137, |137|_p=1 for p != 137",
    "formula": "137 * (1/137) = 1"
  },
  {
    "id": "Q4",
    "statement": "Closure defect D_P(r) = 0 for all r in Q^x and all sufficiently large P (e.g. D_P(137)=0 for P>=137)",
    "inputs": "r=137, P=137, |137|_inf=137, |137|_137=1/137",
    "formula": "D_P(r) = |log( |r|_inf * product_{p<=P} |r|_p )| = |log(137 * 1/137)| = |log(1)| = 0"
  },
  {
    "id": "Q5",
    "statement": "2-adic distance d_2(1,3) = 0.5",
    "inputs": "x=1, y=3, v_2(1-3)=v_2(-2)=1",
    "formula": "d_2(1,3) = 2^{-1} = 0.5"
  },
  {
    "id": "Q6",
    "statement": "2-adic distance d_2(3,7) = 0.25",
    "inputs": "y=3, z=7, v_2(3-7)=v_2(-4)=2",
    "formula": "d_2(3,7) = 2^{-2} = 0.25"
  },
  {
    "id": "Q7",
    "statement": "2-adic distance d_2(1,7) = 0.5 and ultrametric inequality d_2(1,7) <= max(d_2(1,3), d_2(3,7)) holds",
    "inputs": "x=1, z=7, v_2(1-7)=v_2(-6)=1, d_2(1,3)=0.5, d_2(3,7)=0.25",
    "formula": "d_2(1,7) = 2^{-1} = 0.5 <= max(0.5, 0.25) = 0.5"
  },
  {
    "id": "Q8",
    "statement": "Partial sum of sum over primes p<=10 of p^{-2} equals S_10 = 0.421519",
    "inputs": "primes 2,3,5,7; 1/4, 1/9, 1/25, 1/49",
    "formula": "S_10 = 1/4 + 1/9 + 1/25 + 1/49"
  }
]

## Script
```python
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

```

## Execution output
```
CLAIM Q7-ultra: computed=True expected=True match=yes
CLAIM Q1: computed=1.0 expected=1.0 match=yes
CLAIM Q2: computed=1.0 expected=1.0 match=yes
CLAIM Q3: computed=1.0 expected=1.0 match=yes
CLAIM Q4: computed=0.0 expected=0.0 match=yes
CLAIM Q5: computed=0.5 expected=0.5 match=yes
CLAIM Q6: computed=0.25 expected=0.25 match=yes
CLAIM Q7: computed=0.5 expected=0.5 match=yes
CLAIM Q8: computed=0.42151927437641723 expected=0.421519 match=yes
VERIFICATION SUMMARY: 9 claims, 9 match, 0 mismatch

[exit 0]
```
