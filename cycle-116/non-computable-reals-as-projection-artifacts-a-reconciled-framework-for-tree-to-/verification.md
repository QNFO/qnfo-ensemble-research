# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Sum of Euler totients for k=1..20 equals 128",
    "inputs": "totient values phi(1)=1, phi(2)=1, phi(3)=2, phi(4)=2, phi(5)=4, phi(6)=2, phi(7)=6, phi(8)=4, phi(9)=6, phi(10)=4, phi(11)=10, phi(12)=4, phi(13)=12, phi(14)=6, phi(15)=8, phi(16)=8, phi(17)=16, phi(18)=6, phi(19)=18, phi(20)=8",
    "formula": "sum_{k=1}^{20} phi(k)"
  },
  {
    "id": "Q2",
    "statement": "Farey sequence of order 20 has 129 elements",
    "inputs": "sum_{k=1}^{20} phi(k) = 128",
    "formula": "|F_20| = 1 + sum_{k=1}^{20} phi(k)"
  },
  {
    "id": "Q3",
    "statement": "Definable fraction at depth 20 is 129/2^20 = 1.23024e-4",
    "inputs": "|F_20| = 129, 2^20 = 1048576",
    "formula": "f_20 = 129 / 1048576"
  },
  {
    "id": "Q4",
    "statement": "Number of binary programs of length at most 100 is 2^101 - 1 = 2535301200456458802993406410751",
    "inputs": "lengths k = 0..100, count per length = 2^k",
    "formula": "sum_{k=0}^{100} 2^k = 2^101 - 1"
  },
  {
    "id": "Q5",
    "statement": "Total covering length for computable shadows is epsilon, so measure zero",
    "inputs": "radius of j-th interval = eps * 2^(-j-1), j = 1,2,...",
    "formula": "sum_{j=1}^{inf} 2 * eps * 2^(-j-1) = eps * sum_{j=1}^{inf} 2^(-j) = eps"
  },
  {
    "id": "Q6",
    "statement": "Upper bound on definable fraction at n=20 is 401/2^20 ≈ 3.82423e-4",
    "inputs": "n = 20, 2^20 = 1048576",
    "formula": "(1 + n^2) / 2^n = 401 / 1048576"
  },
  {
    "id": "Q7",
    "statement": "Regular-tree rays at p=2, depth 4: 54",
    "inputs": "p = 2, n = 4",
    "formula": "p * (p+1)^(n-1) = 2 * 3^3"
  },
  {
    "id": "Q8",
    "statement": "Regular-tree rays at p=2, depth 8: 4374",
    "inputs": "p = 2, n = 8",
    "formula": "p * (p+1)^(n-1) = 2 * 3^7"
  }
]

## Script
```python
import math

def phi(n):
    result = n
    m = n
    d = 2
    while d * d <= m:
        if m % d == 0:
            while m % d == 0:
                m //= d
            result -= result // d
        d += 1
    if m > 1:
        result -= result // m
    return result

claims = []

# Q1: sum of totients k=1..20
s = sum(phi(k) for k in range(1, 21))
claims.append(("Q1", s, 128))

# Q2: Farey order 20 cardinality
f20 = 1 + s
claims.append(("Q2", f20, 129))

# Q3: definable fraction at depth 20
f_20 = 129 / 1048576
claims.append(("Q3", f_20, 1.23024e-4))

# Q4: programs of length at most 100
prog = sum(2**k for k in range(0, 101))
claims.append(("Q4", prog, 2**101 - 1))

# Q5: total covering length = eps * sum 2^-j (use eps=1 for the series value)
eps = 1.0
total = sum(2 * eps * 2**(-j - 1) for j in range(1, 10000))
claims.append(("Q5", total, eps))

# Q6: upper bound (1 + n^2)/2^n at n=20
ub = (1 + 20**2) / 2**20
claims.append(("Q6", ub, 401 / 1048576))

# Q7: regular-tree rays p=2, n=4
r7 = 2 * 3**(4 - 1)
claims.append(("Q7", r7, 54))

# Q8: regular-tree rays p=2, n=8
r8 = 2 * 3**(8 - 1)
claims.append(("Q8", r8, 4374))

match_count = 0
for cid, computed, expected in claims:
    if isinstance(computed, float) or isinstance(expected, float):
        ok = math.isclose(float(computed), float(expected), rel_tol=1e-6)
    else:
        ok = computed == expected
    if ok:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=128 expected=128 match=yes
CLAIM Q2: computed=129 expected=129 match=yes
CLAIM Q3: computed=0.00012302398681640625 expected=0.000123024 match=yes
CLAIM Q4: computed=2535301200456458802993406410751 expected=2535301200456458802993406410751 match=yes
CLAIM Q5: computed=1.0 expected=1.0 match=yes
CLAIM Q6: computed=0.00038242340087890625 expected=0.00038242340087890625 match=yes
CLAIM Q7: computed=54 expected=54 match=yes
CLAIM Q8: computed=4374 expected=4374 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
