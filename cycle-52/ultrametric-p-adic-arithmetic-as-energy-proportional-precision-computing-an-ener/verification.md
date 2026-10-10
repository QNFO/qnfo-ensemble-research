# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Break-even precision at 45 nm: k*(45) = 19 binary p-adic digits",
    "inputs": "E_f(45) = 3.7 pJ, e_d = 0.01 pJ",
    "formula": "k* = floor(sqrt(E_f / e_d)) = floor(sqrt(3.7/0.01))"
  },
  {
    "id": "Q2",
    "statement": "Break-even precision at 7 nm: k*(7) = 9 binary p-adic digits",
    "inputs": "E_f(7) = 0.9 pJ, e_d = 0.01 pJ",
    "formula": "k* = floor(sqrt(E_f / e_d)) = floor(sqrt(0.9/0.01))"
  },
  {
    "id": "Q3",
    "statement": "p-adic MAC energy at k = 19 digits is 3.629 pJ (< 3.7 pJ)",
    "inputs": "k = 19, e_d = 0.01 pJ, e_a = 0.001 pJ",
    "formula": "E_p(k) = k^2 * e_d + k * e_a = 19^2 * 0.01 + 19 * 0.001"
  },
  {
    "id": "Q4",
    "statement": "p-adic MAC energy at k = 20 digits is 4.020 pJ (> 3.7 pJ)",
    "inputs": "k = 20, e_d = 0.01 pJ, e_a = 0.001 pJ",
    "formula": "E_p(k) = k^2 * e_d + k * e_a = 20^2 * 0.01 + 20 * 0.001"
  },
  {
    "id": "Q5",
    "statement": "p-adic MAC energy at k = 9 digits is 0.819 pJ (< 0.9 pJ)",
    "inputs": "k = 9, e_d = 0.01 pJ, e_a = 0.001 pJ",
    "formula": "E_p(k) = k^2 * e_d + k * e_a = 9^2 * 0.01 + 9 * 0.001"
  },
  {
    "id": "Q6",
    "statement": "p-adic MAC energy at k = 10 digits is 1.010 pJ (> 0.9 pJ)",
    "inputs": "k = 10, e_d = 0.01 pJ, e_a = 0.001 pJ",
    "formula": "E_p(k) = k^2 * e_d + k * e_a = 10^2 * 0.01 + 10 * 0.001"
  },
  {
    "id": "Q7",
    "statement": "Required digits for tolerance eps = 1e-2 with p = 2 is k = 7",
    "inputs": "eps = 1e-2, p = 2",
    "formula": "k(eps) = ceil(ln(1/eps) / ln(p)) = ceil(ln(100)/ln(2))"
  },
  {
    "id": "Q8",
    "statement": "p-adic MAC energy at k = 7 digits is 0.497 pJ",
    "inputs": "k = 7, e_d = 0.01 pJ, e_a = 0.001 pJ",
    "formula": "E_p(k) = k^2 * e_d + k * e_a = 49 * 0.01 + 7 * 0.001"
  }
]

## Script
```python
import math

def Ep(k, ed, ea):
    return k * k * ed + k * ea

claims = []

# Q1
k1 = math.floor(math.sqrt(3.7 / 0.01))
claims.append(("Q1", k1, 19))

# Q2
k2 = math.floor(math.sqrt(0.9 / 0.01))
claims.append(("Q2", k2, 9))

# Q3
v3 = Ep(19, 0.01, 0.001)
claims.append(("Q3", v3, 3.629))

# Q4
v4 = Ep(20, 0.01, 0.001)
claims.append(("Q4", v4, 4.020))

# Q5
v5 = Ep(9, 0.01, 0.001)
claims.append(("Q5", v5, 0.819))

# Q6
v6 = Ep(10, 0.01, 0.001)
claims.append(("Q6", v6, 1.010))

# Q7
k7 = math.ceil(math.log(1 / 1e-2) / math.log(2))
claims.append(("Q7", k7, 7))

# Q8
v8 = Ep(7, 0.01, 0.001)
claims.append(("Q8", v8, 0.497))

match_count = 0
for cid, computed, expected in claims:
    if isinstance(expected, int):
        ok = (computed == expected)
    else:
        ok = math.isclose(computed, expected, rel_tol=1e-6)
    if ok:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=19 expected=19 match=yes
CLAIM Q2: computed=9 expected=9 match=yes
CLAIM Q3: computed=3.629 expected=3.629 match=yes
CLAIM Q4: computed=4.02 expected=4.02 match=yes
CLAIM Q5: computed=0.8190000000000001 expected=0.819 match=yes
CLAIM Q6: computed=1.01 expected=1.01 match=yes
CLAIM Q7: computed=7 expected=7 match=yes
CLAIM Q8: computed=0.497 expected=0.497 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
