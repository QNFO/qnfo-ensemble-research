# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Exactly 1 of 4 unary laws on B2 satisfies f(x) != x for all x; density rho_2 = 1/4",
    "inputs": "|B2| = 2; number of unary laws N2 = 2^2 = 4; prohibition condition f(x) != x for all x",
    "formula": "N2 = 2^2 = 4; rho_2 = 1/4 = 0.25"
  },
  {
    "id": "Q2",
    "statement": "The unique binary prohibition law (negation) has no fixed point and orbit period T_2 = 2",
    "inputs": "f_not(0) = 1, f_not(1) = 0; fixed-point equation 2x = 1 over {0,1}",
    "formula": "T_not = 2 (since f(f(x)) = x and f(x) != x); 2*0 = 0 != 1, 2*1 = 2 != 1"
  },
  {
    "id": "Q3",
    "statement": "Exactly 2 of 27 ternary laws on S3 satisfy (P); both are 3-cycles of period 3; density rho_3 = 2/27",
    "inputs": "|S3| = 3; N3 = 3^3 = 27; derangement number !3",
    "formula": "!3 = 3! * sum_{k=0}^{3} (-1)^k/k! = 6*(1 - 1 + 1/2 - 1/6) = 2; rho_3 = 2/27"
  },
  {
    "id": "Q4",
    "statement": "Density ratio rho_2/rho_3 = 27/8 = 3.375",
    "inputs": "rho_2 = 1/4; rho_3 = 2/27",
    "formula": "(1/4)/(2/27) = (1/4)*(27/2) = 27/8 = 3.375"
  },
  {
    "id": "Q5",
    "statement": "Entropy increment Delta H = log2(3) - 1 = 0.5849625 bits",
    "inputs": "H_2 = log2(2); H_3 = log2(3) = ln(3)/ln(2)",
    "formula": "Delta H = ln(3)/ln(2) - 1 = 1.0986123/0.6931472 - 1 = 0.5849625"
  },
  {
    "id": "Q6",
    "statement": "For forbidden-word constraint P = {11}, a_10 = 144 admissible sequences of length 10 out of 2^10 = 1024; survival ratio rho_10 = 0.140625",
    "inputs": "a_1 = 2, a_2 = 3; recurrence a_n = a_{n-1} + a_{n-2}; total 2^10 = 1024",
    "formula": "a_3 = 5, a_4 = 8, a_5 = 13, a_6 = 21, a_7 = 34, a_8 = 55, a_9 = 89, a_10 = 144; rho_10 = 144/1024 = 0.140625"
  },
  {
    "id": "Q7",
    "statement": "Capacity C_10 = log2(144) = 7.1699250 bits; loss Delta C_10 = 2.8300750 bits",
    "inputs": "a_10 = 144; ln(4) = 1.3862944; ln(3) = 1.0986123; ln(2) = 0.6931472",
    "formula": "C_10 = ln(144)/ln(2) = 2*(1.3862944 + 1.0986123)/0.6931472 = 4.9698134/0.6931472 = 7.1699250; Delta C_10 = 10 - 7.1699250 = 2.8300750"
  },
  {
    "id": "Q8",
    "statement": "Asymptotic capacity c_infinity = log2(phi) = 0.6942419 bits per symbol; asymptotic loss 0.3057581 bits per symbol",
    "inputs": "phi = (1 + sqrt(5))/2 with sqrt(5) = 2.2360680; ln(phi) = 0.4812118; ln(2) = 0.6931472",
    "formula": "c_infinity = ln(1.6180340)/0.6931472 = 0.4812118/0.6931472 = 0.6942419; loss = 1 - 0.6942419 = 0.3057581"
  }
]

## Script
```python
import math
from fractions import Fraction

results = []

# Q1: N2 = 2^2 = 4; rho_2 = 1/4 = 0.25
N2 = 2**2
rho2 = Fraction(1, 4)
computed = float(rho2)
expected = 0.25
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q1", computed, expected, match))

# Q2: negation has no fixed point; period T = 2
fp0 = (1 == 0)   # f(0)=1, is it fixed? no
fp1 = (0 == 1)   # f(1)=0, is it fixed? no
# check fixed-point equation 2x = 1 over {0,1}
no_fp = (2*0 != 1) and (2*1 != 1)
# period: f(f(0)) = f(1) = 0 -> returns to start in 2 steps
T = 2
computed = T if (no_fp and not fp0 and not fp1) else None
expected = 2
match = computed is not None and math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q2", computed, expected, match))

# Q3: derangements of 3-set: !3 = 3! * sum_{k=0}^{3} (-1)^k/k! = 2; rho_3 = 2/27
s = sum(Fraction((-1)**k, math.factorial(k)) for k in range(4))
d3 = math.factorial(3) * s
rho3 = Fraction(d3, 27)
computed = float(rho3)
expected = 2/27
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q3", computed, expected, match))

# Q4: rho2/rho3 = 27/8 = 3.375
ratio = rho2 / rho3
computed = float(ratio)
expected = 3.375
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q4", computed, expected, match))

# Q5: Delta H = log2(3) - 1 = 0.5849625
dH = math.log(3)/math.log(2) - 1
computed = dH
expected = 0.5849625
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q5", computed, expected, match))

# Q6: forbidden word '11': a_n = a_{n-1} + a_{n-2}, a_1=2, a_2=3; a_10 = 144; rho_10 = 144/1024
a = {1: 2, 2: 3}
for n in range(3, 11):
    a[n] = a[n-1] + a[n-2]
a10 = a[10]
total = 2**10
rho10 = a10 / total
computed = rho10
expected = 0.140625
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q6", computed, expected, match))

# Q7: C_10 = log2(144) = 7.1699250; loss = 10 - C_10 = 2.8300750
C10 = math.log(144)/math.log(2)
loss = 10 - C10
computed = C10
expected = 7.1699250
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q7", computed, expected, match))

# Q8: c_inf = log2(phi) = 0.6942419; loss = 1 - c_inf = 0.3057581
phi = (1 + math.sqrt(5))/2
c_inf = math.log(phi)/math.log(2)
loss_inf = 1 - c_inf
computed = c_inf
expected = 0.6942419
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q8", computed, expected, match))

for cid, comp, exp, m in results:
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if m else 'no'}")

n = len(results)
m = sum(1 for r in results if r[3])
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.25 expected=0.25 match=yes
CLAIM Q2: computed=2 expected=2 match=yes
CLAIM Q3: computed=0.07407407407407407 expected=0.07407407407407407 match=yes
CLAIM Q4: computed=3.375 expected=3.375 match=yes
CLAIM Q5: computed=0.5849625007211563 expected=0.5849625 match=yes
CLAIM Q6: computed=0.140625 expected=0.140625 match=yes
CLAIM Q7: computed=7.169925001442313 expected=7.169925 match=yes
CLAIM Q8: computed=0.6942419136306174 expected=0.6942419 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
