# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "For d=4, n=64, the Born-rule probability deviation bound is epsilon_P <= 1.084202e-19",
    "inputs": "d=4, n=64, delta=2^(-n-1)=2^(-65)",
    "formula": "epsilon_P = (2+delta)*sqrt(d)*delta"
  },
  {
    "id": "Q2",
    "statement": "For d=4, n=53, epsilon_P <= 2.220446e-16",
    "inputs": "d=4, n=53, delta=2^(-54)",
    "formula": "epsilon_P = (2+delta)*sqrt(d)*delta"
  },
  {
    "id": "Q3",
    "statement": "For d=4 and target tolerance 1e-12, n=41 fractional bits suffice",
    "inputs": "d=4, epsilon_target=1e-12",
    "formula": "n = ceil(0.5*log2(d) + log2(1/epsilon_target))"
  },
  {
    "id": "Q4",
    "statement": "For d=4 and target tolerance 1e-6, n=21 fractional bits suffice",
    "inputs": "d=4, epsilon_target=1e-6",
    "formula": "n = ceil(0.5*log2(d) + log2(1/epsilon_target))"
  },
  {
    "id": "Q5",
    "statement": "Check: sqrt(d)*2^(-41) = 2^(-40) ≈ 9.0949e-13 < 1e-12",
    "inputs": "d=4, n=41",
    "formula": "sqrt(d)*2^(-n)"
  },
  {
    "id": "Q6",
    "statement": "Information budget of a two-qubit rational state: 512 bits at n=64 and 328 bits at n=41",
    "inputs": "d=4, n=64 and n=41",
    "formula": "bits = 2*d*n"
  },
  {
    "id": "Q7",
    "statement": "Grid-rounding bound: |p-q| <= 5.0e-4 at N=1e3 and <= 5.0e-7 at N=1e6",
    "inputs": "N=1e3 and N=1e6",
    "formula": "|p-q| <= 1/(2*N)"
  },
  {
    "id": "Q8",
    "statement": "Information cost at n=21 for two-qubit state is 168 bits",
    "inputs": "d=4, n=21",
    "formula": "bits = 2*d*n"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if expected is None:
        match = "n/a"
    else:
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    print(f"CLAIM {cid}: computed={computed:.12g} expected={expected if expected is not None else 'none'} match={match}")
    return match == "yes"

results = []

# Q1: d=4, n=64, delta=2^-65, eps=(2+delta)*sqrt(d)*delta
d, n = 4, 64
delta = 2.0**(-n-1)
eps1 = (2 + delta) * math.sqrt(d) * delta
results.append(check("Q1", eps1, 1.0842021724e-19))

# Q2: d=4, n=53, delta=2^-54
d, n = 4, 53
delta = 2.0**(-n-1)
eps2 = (2 + delta) * math.sqrt(d) * delta
results.append(check("Q2", eps2, 2.2204460493e-16))

# Q3: n = ceil(0.5*log2(d) + log2(1/eps_target)), d=4, eps=1e-12
d, eps = 4, 1e-12
n3 = math.ceil(0.5 * math.log2(d) + math.log2(1.0 / eps))
results.append(check("Q3", n3, 41))

# Q4: same, eps=1e-6
d, eps = 4, 1e-6
n4 = math.ceil(0.5 * math.log2(d) + math.log2(1.0 / eps))
results.append(check("Q4", n4, 21))

# Q5: sqrt(d)*2^-41 = 2^-40
d, n = 4, 41
v5 = math.sqrt(d) * 2.0**(-n)
results.append(check("Q5", v5, 9.0949470177e-13))
print(f"  (Q5 check < 1e-12: {v5 < 1e-12})")

# Q6: bits = 2*d*n for n=64 and n=41
d = 4
b64 = 2 * d * 64
b41 = 2 * d * 41
results.append(check("Q6a", b64, 512))
results.append(check("Q6b", b41, 328))

# Q7: |p-q| <= 1/(2N)
v7a = 1.0 / (2 * 1e3)
v7b = 1.0 / (2 * 1e6)
results.append(check("Q7a", v7a, 5.0e-4))
results.append(check("Q7b", v7b, 5.0e-7))

# Q8: bits = 2*d*n, n=21
results.append(check("Q8", 2 * 4 * 21, 168))

m = sum(results)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {m} match, {len(results)-m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.08420217249e-19 expected=1.0842021724e-19 match=yes
CLAIM Q2: computed=2.22044604925e-16 expected=2.2204460493e-16 match=yes
CLAIM Q3: computed=41 expected=41 match=yes
CLAIM Q4: computed=21 expected=21 match=yes
CLAIM Q5: computed=9.09494701773e-13 expected=9.0949470177e-13 match=yes
  (Q5 check < 1e-12: True)
CLAIM Q6a: computed=512 expected=512 match=yes
CLAIM Q6b: computed=328 expected=328 match=yes
CLAIM Q7a: computed=0.0005 expected=0.0005 match=yes
CLAIM Q7b: computed=5e-07 expected=5e-07 match=yes
CLAIM Q8: computed=168 expected=168 match=yes
VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch

[exit 0]
```
