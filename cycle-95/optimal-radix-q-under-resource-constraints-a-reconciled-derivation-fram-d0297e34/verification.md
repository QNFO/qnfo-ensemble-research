# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Continuous optimum of q/ln q is at q = e",
    "inputs": "f(q) = q/ln q",
    "formula": "f'(q) = (ln q - 1)/(ln q)^2 = 0 => q = e"
  },
  {
    "id": "Q2",
    "statement": "Depth n(2) = 20 for N = 10^6",
    "inputs": "N = 1000000, ln N = 13.815511, ln 2 = 0.693147",
    "formula": "n = ceil(ln N / ln q) = ceil(13.815511 / 0.693147)"
  },
  {
    "id": "Q3",
    "statement": "Depth n(3) = 13 for N = 10^6",
    "inputs": "ln N = 13.815511, ln 3 = 1.098612",
    "formula": "n = ceil(13.815511 / 1.098612)"
  },
  {
    "id": "Q4",
    "statement": "Depth n(4) = 10 for N = 10^6",
    "inputs": "ln N = 13.815511, ln 4 = 1.386294",
    "formula": "n = ceil(13.815511 / 1.386294)"
  },
  {
    "id": "Q5",
    "statement": "Depth n(5) = 9 for N = 10^6",
    "inputs": "ln N = 13.815511, ln 5 = 1.609438",
    "formula": "n = ceil(13.815511 / 1.609438)"
  },
  {
    "id": "Q6",
    "statement": "Traversal costs T(2)=40, T(3)=39, T(4)=40, T(5)=45",
    "inputs": "n(2)=20, n(3)=13, n(4)=10, n(5)=9",
    "formula": "T(q) = q * n(q)"
  },
  {
    "id": "Q7",
    "statement": "Unpadded storage per leaf S(2)/N = 2.0000",
    "inputs": "q=2, n=20, N=10^6",
    "formula": "S(q)/N = q*(1 - q^{-n})/(q-1)"
  },
  {
    "id": "Q8",
    "statement": "Unpadded storage per leaf S(3)/N = 1.5000",
    "inputs": "q=3, n=13",
    "formula": "S(q)/N = q*(1 - q^{-n})/(q-1)"
  }
]

## Script
```python
import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: continuous optimum of q/ln q at q = e
q_opt = math.e
f_e = q_opt / math.log(q_opt)
# check derivative zero at e: (ln q - 1)/(ln q)^2
deriv = (math.log(q_opt) - 1) / (math.log(q_opt) ** 2)
match = isclose(deriv, 0.0) and isclose(q_opt, math.e)
results.append(("Q1", q_opt, math.e, match))

# Q2: n(2) = ceil(13.815511 / 0.693147)
lnN = 13.815511
n2 = math.ceil(lnN / 0.693147)
results.append(("Q2", n2, 20, n2 == 20))

# Q3: n(3)
n3 = math.ceil(lnN / 1.098612)
results.append(("Q3", n3, 13, n3 == 13))

# Q4: n(4)
n4 = math.ceil(lnN / 1.386294)
results.append(("Q4", n4, 10, n4 == 10))

# Q5: n(5)
n5 = math.ceil(lnN / 1.609438)
results.append(("Q5", n5, 9, n5 == 9))

# Q6: traversal costs
T2, T3, T4, T5 = 2 * n2, 3 * n3, 4 * n4, 5 * n5
match6 = (T2 == 40) and (T3 == 39) and (T4 == 40) and (T5 == 45)
results.append(("Q6", (T2, T3, T4, T5), (40, 39, 40, 45), match6))

# Q7: S(2)/N = 2*(1 - 2^-20)/(2-1)
s2 = 2 * (1 - 2 ** (-20)) / (2 - 1)
match7 = isclose(s2, 2.0000)
results.append(("Q7", round(s2, 4), 2.0000, match7))

# Q8: S(3)/N = 3*(1 - 3^-13)/(3-1)
s3 = 3 * (1 - 3 ** (-13)) / (3 - 1)
match8 = isclose(s3, 1.5000)
results.append(("Q8", round(s3, 4), 1.5000, match8))

mismatches = 0
for cid, computed, expected, match in results:
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")
    if not match:
        mismatches += 1

print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results) - mismatches} match, {mismatches} mismatch")

```

## Execution output
```
CLAIM Q1: computed=2.718281828459045 expected=2.718281828459045 match=yes
CLAIM Q2: computed=20 expected=20 match=yes
CLAIM Q3: computed=13 expected=13 match=yes
CLAIM Q4: computed=10 expected=10 match=yes
CLAIM Q5: computed=9 expected=9 match=yes
CLAIM Q6: computed=(40, 39, 40, 45) expected=(40, 39, 40, 45) match=yes
CLAIM Q7: computed=2.0 expected=2.0 match=yes
CLAIM Q8: computed=1.5 expected=1.5 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
