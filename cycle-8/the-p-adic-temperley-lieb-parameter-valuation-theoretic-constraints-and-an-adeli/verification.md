# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "For p=2, δ_2 = 2 + 1/2 = 5/2 with v_2(δ_2) = −1 and |δ_2|_2 = 2.",
    "inputs": "p=2",
    "formula": "δ_p = p + p^(-1); v_p(δ_p) = -1; |δ_p|_p = p^1"
  },
  {
    "id": "Q2",
    "statement": "For p=3, δ_3 = 3 + 1/3 = 10/3 with v_3(δ_3) = −1 and |δ_3|_3 = 3.",
    "inputs": "p=3",
    "formula": "δ_p = p + p^(-1); v_p(δ_p) = -1; |δ_p|_p = p^1"
  },
  {
    "id": "Q3",
    "statement": "For p=5, δ_5 = 5 + 1/5 = 26/5 with v_5(δ_5) = −1 and |δ_5|_5 = 5.",
    "inputs": "p=5",
    "formula": "δ_p = p + p^(-1); v_p(δ_p) = -1; |δ_p|_p = p^1"
  },
  {
    "id": "Q4",
    "statement": "For p=7, δ_7 = 7 + 1/7 = 50/7 with v_7(δ_7) = −1 and |δ_7|_7 = 7.",
    "inputs": "p=7",
    "formula": "δ_p = p + p^(-1); v_p(δ_p) = -1; |δ_p|_p = p^1"
  },
  {
    "id": "Q5",
    "statement": "For p=2, d_2 = 21/4 with v_2(d_2) = −2 and |d_2|_2 = 4.",
    "inputs": "p=2; p^4+p^2+1 = 21",
    "formula": "d_2 = (p^4 + p^2 + 1)/p^2; v_p(d_2) = -2; |d_2|_p = p^2"
  },
  {
    "id": "Q6",
    "statement": "For p=3, d_2 = 91/9 with v_3(d_2) = −2 and |d_2|_3 = 9.",
    "inputs": "p=3; p^4+p^2+1 = 91",
    "formula": "d_2 = (p^4 + p^2 + 1)/p^2; v_p(d_2) = -2; |d_2|_p = p^2"
  },
  {
    "id": "Q7",
    "statement": "For p=5, d_2 = 651/25 with v_5(d_2) = −2 and |d_2|_5 = 25.",
    "inputs": "p=5; p^4+p^2+1 = 651",
    "formula": "d_2 = (p^4 + p^2 + 1)/p^2; v_p(d_2) = -2; |d_2|_p = p^2"
  },
  {
    "id": "Q8",
    "statement": "For p=7, d_2 = 2451/49 with v_7(d_2) = −2 and |d_2|_7 = 49.",
    "inputs": "p=7; p^4+p^2+1 = 2451",
    "formula": "d_2 = (p^4 + p^2 + 1)/p^2; v_p(d_2) = -2; |d_2|_p = p^2"
  }
]

## Script
```python
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

```

## Execution output
```
CLAIM Q1a: computed=5/2 expected=5/2 match=yes
CLAIM Q1b: computed=-1 expected=-1 match=yes
CLAIM Q1c: computed=2.0 expected=2.0 match=yes
CLAIM Q2a: computed=10/3 expected=10/3 match=yes
CLAIM Q2b: computed=-1 expected=-1 match=yes
CLAIM Q2c: computed=3.0 expected=3.0 match=yes
CLAIM Q3a: computed=26/5 expected=26/5 match=yes
CLAIM Q3b: computed=-1 expected=-1 match=yes
CLAIM Q3c: computed=5.0 expected=5.0 match=yes
CLAIM Q4a: computed=50/7 expected=50/7 match=yes
CLAIM Q4b: computed=-1 expected=-1 match=yes
CLAIM Q4c: computed=7.0 expected=7.0 match=yes
CLAIM Q5a: computed=21/4 expected=21/4 match=yes
CLAIM Q5b: computed=-2 expected=-2 match=yes
CLAIM Q5c: computed=4.0 expected=4.0 match=yes
CLAIM Q6a: computed=91/9 expected=91/9 match=yes
CLAIM Q6b: computed=-2 expected=-2 match=yes
CLAIM Q6c: computed=9.0 expected=9.0 match=yes
CLAIM Q7a: computed=651/25 expected=651/25 match=yes
CLAIM Q7b: computed=-2 expected=-2 match=yes
CLAIM Q7c: computed=25.0 expected=25.0 match=yes
CLAIM Q8a: computed=2451/49 expected=2451/49 match=yes
CLAIM Q8b: computed=-2 expected=-2 match=yes
CLAIM Q8c: computed=49.0 expected=49.0 match=yes
VERIFICATION SUMMARY: 24 claims, 24 match, 0 mismatch

[exit 0]
```
