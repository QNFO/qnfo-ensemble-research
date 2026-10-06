# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "With L=100, R=60, e=5, c_t=1, a=0.3, the optimal team size is n*=5.",
    "inputs": "L=100, R=60, e=5, c_t=1, a=0.3",
    "formula": "n* = ceil( ln((c_t + e*a)/(B*a)) / ln(1-a) ), B = L - R + e = 45; ratio = 2.5/13.5 = 0.18519; ln(0.18519)/ln(0.7) = -1.68546/-0.35668 = 4.72554; ceil = 5"
  },
  {
    "id": "Q2",
    "statement": "Marginal cost of the 5th thread: Delta C(4) = -0.74135 < 0.",
    "inputs": "c_t=1, e=5, a=0.3, B=45, n=4",
    "formula": "Delta C(n) = c_t + e*a - B*a*(1-a)^n = 2.5 - 13.5*0.7^4 = 2.5 - 3.24135 = -0.74135"
  },
  {
    "id": "Q3",
    "statement": "Marginal cost of the 6th thread: Delta C(5) = +0.231055 > 0.",
    "inputs": "c_t=1, e=5, a=0.3, B=45, n=5",
    "formula": "Delta C(n) = c_t + e*a - B*a*(1-a)^n = 2.5 - 13.5*0.7^5 = 2.5 - 2.268945 = 0.231055"
  },
  {
    "id": "Q4",
    "statement": "Expected cost at (n,a)=(5,0.3) is 78.38245.",
    "inputs": "R=60, L-R=40, c_t=1, e=5, n=5, a=0.3",
    "formula": "C = R + (L-R)(1-a)^n + c_t*n + e*(n*a - (1-a)^n) = 60 + 40*0.16807 + 5 + 5*(1.5 - 0.16807) = 78.38245"
  },
  {
    "id": "Q5",
    "statement": "At n=5 in the fixed point search, p*=10.97296 and the implied n*(a)=4 != 5.",
    "inputs": "c=10, L-R-e=35, lambda=0.5, n=5, c_t=1, e=5, B=45",
    "formula": "p* = c + ln(35/5)/((n-1)*lambda) = 10 + 1.94591/2 = 10.97296; a = 1 - e^{-0.48648} = 0.38523; n*(a) = ceil(ln((c_t+e*a)/(B*a))/ln(1-a)) = ceil(-1.77966/-0.48648) = ceil(3.65756) = 4"
  },
  {
    "id": "Q6",
    "statement": "At n=4, p*=11.29727 and the implied n*(a)=3 != 4.",
    "inputs": "c=10, ln7=1.94591, lambda=0.5, n=4, c_t=1, e=5, B=45",
    "formula": "p* = 10 + 1.94591/1.5 = 11.29727; a = 1 - e^{-0.64864} = 0.47731; n*(a) = ceil(-1.84751/-0.64864) = ceil(2.84844) = 3"
  },
  {
    "id": "Q7",
    "statement": "At n=3, p*=11.94591 and the implied n*(a)=2 != 3.",
    "inputs": "c=10, ln7=1.94591, lambda=0.5, n=3, c_t=1, e=5, B=45",
    "formula": "p* = 10 + 1.94591/1 = 11.94591; a = 1 - e^{-0.97296} = 0.62204; n*(a) = ceil(-1.91841/-0.97296) = ceil(1.97202) = 2"
  },
  {
    "id": "Q8",
    "statement": "The interior fixed point over n>=2 is (n*, p*) = (2, 13.89182).",
    "inputs": "c=10, ln7=1.94591, lambda=0.5, n=2, c_t=1, e=5, B=45",
    "formula": "p* = 10 + 1.94591/0.5 = 13.89182; a = 1 - e^{-1.94591} = 6/7 = 0.85714; n*(a) = ceil(-1.98793/-1.94591) = ceil(1.02157) = 2"
  }
]

## Script
```python
import math

def close(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(float(a), float(b), rel_tol=1e-6)
    return a == b

results = []

def check(cid, computed, expected):
    match = "yes" if (expected is None or close(computed, expected)) else "no"
    results.append(match == "yes")
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1
L, R, e, c_t, a = 100, 60, 5, 1, 0.3
B = L - R + e
ratio = (c_t + e * a) / (B * a)
quot = math.log(ratio) / math.log(1 - a)
n_star = math.ceil(quot)
check("Q1", n_star, 5)

# Q2
dc4 = c_t + e * a - B * a * (1 - a) ** 4
check("Q2", round(dc4, 5), -0.74135)

# Q3
dc5 = c_t + e * a - B * a * (1 - a) ** 5
check("Q3", round(dc5, 6), 0.231055)

# Q4
C = R + (L - R) * (1 - a) ** 5 + c_t * 5 + e * (5 * a - (1 - a) ** 5)
check("Q4", round(C, 5), 78.38245)

# Fixed point setup
c, lam = 10, 0.5
ln7 = math.log(7)
Bf = 45

def n_of_a(av):
    r = (c_t + e * av) / (Bf * av)
    return math.ceil(math.log(r) / math.log(1 - av))

# Q5
n = 5
p = c + ln7 / ((n - 1) * lam)
av = 1 - math.exp(-lam * (p - c))
nn = n_of_a(av)
check("Q5", (round(p, 5), nn), (10.97296, 4))

# Q6
n = 4
p = c + ln7 / ((n - 1) * lam)
av = 1 - math.exp(-lam * (p - c))
nn = n_of_a(av)
check("Q6", (round(p, 5), nn), (11.29727, 3))

# Q7
n = 3
p = c + ln7 / ((n - 1) * lam)
av = 1 - math.exp(-lam * (p - c))
nn = n_of_a(av)
check("Q7", (round(p, 5), nn), (11.94591, 2))

# Q8
n = 2
p = c + ln7 / ((n - 1) * lam)
av = 1 - math.exp(-lam * (p - c))
nn = n_of_a(av)
check("Q8", (nn, round(p, 5)), (2, 13.89182))

m = sum(results)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {m} match, {len(results) - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=5 expected=5 match=yes
CLAIM Q2: computed=-0.74135 expected=-0.74135 match=yes
CLAIM Q3: computed=0.231055 expected=0.231055 match=yes
CLAIM Q4: computed=78.38245 expected=78.38245 match=yes
CLAIM Q5: computed=(10.97296, 4) expected=(10.97296, 4) match=yes
CLAIM Q6: computed=(11.29727, 3) expected=(11.29727, 3) match=yes
CLAIM Q7: computed=(11.94591, 2) expected=(11.94591, 2) match=yes
CLAIM Q8: computed=(2, 13.89182) expected=(2, 13.89182) match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
