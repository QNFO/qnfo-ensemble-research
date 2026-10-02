# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Sphere of radius n has size (p+1)p^{n-1}",
    "inputs": "p (prime), n>=1",
    "formula": "|S_n| = (p+1)*p^(n-1)"
  },
  {
    "id": "Q2",
    "statement": "Ball of radius N contains 1 + (p+1)(p^N - 1)/(p-1) vertices",
    "inputs": "p (prime), N>=1",
    "formula": "V(N) = 1 + (p+1)*(p^N - 1)/(p - 1)"
  },
  {
    "id": "Q3",
    "statement": "Number of edges in ball of radius N equals V(N) - 1",
    "inputs": "V(N)",
    "formula": "E(N) = V(N) - 1"
  },
  {
    "id": "Q4",
    "statement": "For p=3, radius-2 ball contains 17 vertices and 16 edges",
    "inputs": "p=3, N=2",
    "formula": "V(2) = 1 + 4*(9-1)/2 = 17; E(2) = 17 - 1 = 16"
  },
  {
    "id": "Q5",
    "statement": "For p=3, radius-3 ball contains 53 vertices and 52 edges",
    "inputs": "p=3, N=3",
    "formula": "V(3) = 1 + 4*(27-1)/2 = 53; E(3) = 53 - 1 = 52"
  },
  {
    "id": "Q6",
    "statement": "For p=3, radius-4 ball contains 161 vertices",
    "inputs": "p=3, N=4",
    "formula": "V(4) = 1 + 4*(81-1)/2 = 161"
  },
  {
    "id": "Q7",
    "statement": "Asymptotic ball growth V(N) ~ ((p+1)/(p-1)) p^N",
    "inputs": "p",
    "formula": "V(N) ~ ((p+1)/(p-1))*p^N"
  },
  {
    "id": "Q8",
    "statement": "Order of SL_2(F_p) is p(p^2-1)",
    "inputs": "p",
    "formula": "|SL_2(F_p)| = (p+1)*p*(p-1) = p*(p^2-1)"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: sphere size |S_n| = (p+1)*p^(n-1), test p=3, n=2
p, n = 3, 2
S = (p + 1) * p ** (n - 1)
results.append(check("Q1", S, 12))

# Q2: ball size V(N) = 1 + (p+1)(p^N - 1)/(p-1), test p=3, N=3
p, N = 3, 3
V = 1 + (p + 1) * (p ** N - 1) // (p - 1)
results.append(check("Q2", V, 53))

# Q3: edges in ball E(N) = V(N) - 1, test V(N)=53
VN = 53
E = VN - 1
results.append(check("Q3", E, 52))

# Q4: p=3, N=2: V(2)=17, E(2)=16
p, N = 3, 2
V2 = 1 + (p + 1) * (p ** N - 1) // (p - 1)
E2 = V2 - 1
results.append(check("Q4", (V2, E2), (17, 16)))

# Q5: p=3, N=3: V(3)=53, E(3)=52
p, N = 3, 3
V3 = 1 + (p + 1) * (p ** N - 1) // (p - 1)
E3 = V3 - 1
results.append(check("Q5", (V3, E3), (53, 52)))

# Q6: p=3, N=4: V(4)=161
p, N = 3, 4
V4 = 1 + (p + 1) * (p ** N - 1) // (p - 1)
results.append(check("Q6", V4, 161))

# Q7: asymptotic V(N) ~ ((p+1)/(p-1))*p^N; check ratio V(N)/p^N -> (p+1)/(p-1)
p = 3
N = 20
Vn = 1 + (p + 1) * (p ** N - 1) / (p - 1)
ratio = Vn / p ** N
target = (p + 1) / (p - 1)
results.append(check("Q7", round(ratio, 6), round(target, 6)))

# Q8: |SL_2(F_p)| = p(p^2-1), computed as (p+1)*p*(p-1), test p=3
p = 3
order = (p + 1) * p * (p - 1)
results.append(check("Q8", order, p * (p ** 2 - 1)))

m = sum(results)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {m} match, {len(results) - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=12 expected=12 match=yes
CLAIM Q2: computed=53 expected=53 match=yes
CLAIM Q3: computed=52 expected=52 match=yes
CLAIM Q4: computed=(17, 16) expected=(17, 16) match=yes
CLAIM Q5: computed=(53, 52) expected=(53, 52) match=yes
CLAIM Q6: computed=161 expected=161 match=yes
CLAIM Q7: computed=2.0 expected=2.0 match=yes
CLAIM Q8: computed=24 expected=24 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
