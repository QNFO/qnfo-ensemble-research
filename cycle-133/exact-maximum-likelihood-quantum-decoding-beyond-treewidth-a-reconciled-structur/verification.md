# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "P(L_0 | 00) = 0.756 for the three-qubit repetition code at p = 0.1",
    "inputs": "n = 3, p = 0.1, 1-p = 0.9",
    "formula": "P(L_0|00) = C(3,0)(0.9)^3 + C(3,2)(0.1)^2(0.9)"
  },
  {
    "id": "Q2",
    "statement": "P(L_1 | 00) = 0.244 for the three-qubit repetition code at p = 0.1",
    "inputs": "n = 3, p = 0.1, 1-p = 0.9",
    "formula": "P(L_1|00) = C(3,1)(0.1)(0.9)^2 + C(3,3)(0.1)^3"
  },
  {
    "id": "Q3",
    "statement": "Dominant-pattern-only estimate is 0.729, relative underestimate 0.027/0.756 ≈ 0.0357",
    "inputs": "P(L_0|00) = 0.756, dominant pattern probability = 0.9^3 = 0.729",
    "formula": "relative gap = (0.756 - 0.729)/0.756"
  },
  {
    "id": "Q4",
    "statement": "Rank DP cost at n = 1023 with rw = 4 is ≈ 1.07e9 operations",
    "inputs": "n = 1023, rw = 4",
    "formula": "T = n^3 + n*4^4"
  },
  {
    "id": "Q5",
    "statement": "Tensor-network cost at n = 1023 with tw = sqrt(n) is ≈ 4.35e12 operations",
    "inputs": "n = 1023, tw ≈ sqrt(1023) ≈ 31.984",
    "formula": "T_TN = n * 2^tw"
  },
  {
    "id": "Q6",
    "statement": "Complexity ratio T_TN / T_RankDP ≈ 4.05e3",
    "inputs": "T_TN ≈ 4.35e12, T_RankDP ≈ 1.07e9",
    "formula": "ratio = T_TN / T_RankDP"
  },
  {
    "id": "Q7",
    "statement": "Floating-point relative error bound ≈ 2.3e-13 for m = 1023 DP steps",
    "inputs": "u = 2^-53 ≈ 1.1102e-16, m = 1023, two roundings per step",
    "formula": "bound = (1+u)^(2m) - 1 ≈ 2m*u"
  },
  {
    "id": "Q8",
    "statement": "Log-likelihood optimality gap ≈ 0.0364 nats",
    "inputs": "P_ML = 0.756, P_dec = 0.729",
    "formula": "gap = ln(0.756) - ln(0.729)"
  },
  {
    "id": "Q9",
    "statement": "Steane-concatenated projection at t = 3: Rank DP ≈ 8.78e5 operations",
    "inputs": "t = 3, n = 7^3 = 343, k_* = 4, c = 10",
    "formula": "T = c * n * 4^k_*"
  },
  {
    "id": "Q10",
    "statement": "Steane-concatenated projection at t = 3: tensor-network ≈ 4.60e10 operations",
    "inputs": "n = 343, tw = d = 3^3 = 27",
    "formula": "T_TN = n * 2^27"
  },
  {
    "id": "Q11",
    "statement": "Steane-concatenated separation ratio ≈ 5.2e4 at t = 3",
    "inputs": "T_TN ≈ 4.60e10, T_RankDP ≈ 8.78e5",
    "formula": "ratio = T_TN / T_RankDP"
  },
  {
    "id": "Q12",
    "statement": "ML threshold p* = 0.5 for the length-n repetition code",
    "inputs": "binomial symmetry C(n,j) = C(n,n-j)",
    "formula": "Z_0 = Z_1 = 1/2 at p = 1/2"
  }
]

## Script
```python
import math
from fractions import Fraction

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: P(L_0|00) = C(3,0)(0.9)^3 + C(3,2)(0.1)^2(0.9)
q1 = math.comb(3,0)*0.9**3 + math.comb(3,2)*0.1**2*0.9
results.append(("Q1", q1, "0.756", 3))

# Q2: P(L_1|00) = C(3,1)(0.1)(0.9)^2 + C(3,3)(0.1)^3
q2 = math.comb(3,1)*0.1*0.9**2 + math.comb(3,3)*0.1**3
results.append(("Q2", q2, "0.244", 3))

# Q3: relative gap = (0.756 - 0.729)/0.756
q3 = (0.756 - 0.729)/0.756
results.append(("Q3", q3, "0.0357", 3))

# Q4: T = n^3 + n*4^4, n = 1023, rw = 4
n = 1023
q4 = n**3 + n*4**4
results.append(("Q4", q4, "1.07e9", 3))

# Q5: T_TN = n * 2^tw, tw = sqrt(1023)
tw = math.sqrt(1023)
q5 = n * 2**tw
results.append(("Q5", q5, "4.35e12", 3))

# Q6: ratio = T_TN / T_RankDP
q6 = q5 / q4
results.append(("Q6", q6, "4.05e3", 3))

# Q7: bound = (1+u)^(2m) - 1 ≈ 2m*u, u = 2^-53, m = 1023
u = 2.0**-53
m = 1023
q7 = 2*m*u
results.append(("Q7", q7, "2.3e-13", 2))

# Q8: gap = ln(0.756) - ln(0.729)
q8 = math.log(0.756) - math.log(0.729)
results.append(("Q8", q8, "0.0364", 3))

# Q9: T = c * n * 4^k_*, t=3, n=343, k_*=4, c=10
q9 = 10 * 343 * 4**4
results.append(("Q9", q9, "8.78e5", 3))

# Q10: T_TN = n * 2^27, n = 343
q10 = 343 * 2**27
results.append(("Q10", q10, "4.60e10", 3))

# Q11: ratio = T_TN / T_RankDP (Steane)
q11 = q10 / q9
results.append(("Q11", q11, "5.2e4", 2))

# Q12: ML threshold p* = 0.5; check Z_0 = Z_1 = 1/2 at p = 1/2 for n = 3
p = 0.5
z0 = sum(math.comb(3,j)*p**j*(1-p)**(3-j) for j in range(4) if j % 2 == 0)
z1 = sum(math.comb(3,j)*p**j*(1-p)**(3-j) for j in range(4) if j % 2 == 1)
q12 = z0  # should equal 0.5
results.append(("Q12", q12, "0.5", 1))

match_count = 0
for rid, computed, expected_str, nsig in results:
    expected = float(expected_str)
    match = "yes" if sig(computed, nsig) == expected else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {rid}: computed={computed:.8g} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results)-match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.756 expected=0.756 match=yes
CLAIM Q2: computed=0.244 expected=0.244 match=yes
CLAIM Q3: computed=0.035714286 expected=0.0357 match=yes
CLAIM Q4: computed=1.0708611e+09 expected=1.07e9 match=yes
CLAIM Q5: computed=4.3464106e+12 expected=4.35e12 match=yes
CLAIM Q6: computed=4058.7998 expected=4.05e3 match=no
CLAIM Q7: computed=2.2715163e-13 expected=2.3e-13 match=yes
CLAIM Q8: computed=0.036367644 expected=0.0364 match=yes
CLAIM Q9: computed=878080 expected=8.78e5 match=yes
CLAIM Q10: computed=4.6036681e+10 expected=4.60e10 match=yes
CLAIM Q11: computed=52428.8 expected=5.2e4 match=yes
CLAIM Q12: computed=0.5 expected=0.5 match=yes
VERIFICATION SUMMARY: 12 claims, 11 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.756 | 0.756 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 0.244 | 0.244 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 0.035714286 | 0.0357 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 1.0708611e+09 | 1.07e9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 4.3464106e+12 | 4.35e12 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 4058.7998 | 4.05e3 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 2.2715163e-13 | 2.3e-13 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 0.036367644 | 0.0364 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 878080 | 8.78e5 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 4.6036681e+10 | 4.60e10 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 52428.8 | 5.2e4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 0.5 | 0.5 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 12.
