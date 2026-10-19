# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Tree-distance attention total elementary-operation count for N=1024 tokens, with unit cost for a comparison and a distance evaluation",
    "inputs": "N=1024, log2(N)=10, comparison cost a=1, distance-evaluation cost b=1",
    "formula": "C_tree = N*log2(N) + 2*N - 2"
  },
  {
    "id": "Q2",
    "statement": "Standard dot-product attention elementary-operation count for N=1024 tokens",
    "inputs": "N=1024",
    "formula": "C_dot = N^2"
  },
  {
    "id": "Q4",
    "statement": "Dot-product attention multiply-accumulate count for N=512 tokens and head dimension d=64",
    "inputs": "N=512, d=64",
    "formula": "C_dot = N^2 * d"
  },
  {
    "id": "Q5",
    "statement": "Tree-score cost from exponent vectors of length k=8 for N=512 tokens",
    "inputs": "N=512, k=8",
    "formula": "C_tree = N^2 * k"
  },
  {
    "id": "Q8",
    "statement": "Vertex count of the (p+1)-regular Bruhat-Tits tree truncated at depth D=5 for p=2",
    "inputs": "p=2, D=5",
    "formula": "B_p(D) = 1 + (p+1)*(p^D - 1)/(p - 1)"
  },
  {
    "id": "Q9",
    "statement": "Vertex count of the (p+1)-regular Bruhat-Tits tree truncated at depth D=5 for p=3",
    "inputs": "p=3, D=5",
    "formula": "B_p(D) = 1 + (p+1)*(p^D - 1)/(p - 1)"
  },
  {
    "id": "Q10",
    "statement": "Product of vertex counts for p=2 and p=3 truncations at radius 2",
    "inputs": "B_2(2)=10, B_3(2)=17",
    "formula": "B_2(2) * B_3(2)"
  },
  {
    "id": "Q11",
    "statement": "Vertex count of the p=2 truncated tree at depth 2",
    "inputs": "p=2, D=2",
    "formula": "B_p(D) = 1 + (p+1)*(p^D - 1)/(p - 1)"
  },
  {
    "id": "Q12",
    "statement": "Vertex count of the p=3 truncated tree at depth 2",
    "inputs": "p=3, D=2",
    "formula": "B_p(D) = 1 + (p+1)*(p^D - 1)/(p - 1)"
  },
  {
    "id": "Q13",
    "statement": "Spectral radius of the classical random walk on a 3-regular tree for p=2",
    "inputs": "p=2",
    "formula": "rho = 2*sqrt(p)/(p+1)"
  },
  {
    "id": "Q14",
    "statement": "Spectral gap of the classical random walk on the 3-regular tree",
    "inputs": "rho=2*sqrt(2)/3",
    "formula": "Delta = 1 - rho"
  },
  {
    "id": "Q15",
    "statement": "Classical mixing time upper bound for total-variation distance epsilon=0.01",
    "inputs": "epsilon=0.01, Delta=1-2*sqrt(2)/3",
    "formula": "T_mix <= ln(1/epsilon)/Delta"
  },
  {
    "id": "Q16",
    "statement": "Quantum-walk effective spectral gap taken as twice the classical spectral gap",
    "inputs": "Delta=1-2*sqrt(2)/3",
    "formula": "Delta_q = 2*Delta"
  },
  {
    "id": "Q17",
    "statement": "Quantum-walk mixing time upper bound for total-variation distance epsilon=0.01",
    "inputs": "epsilon=0.01, Delta_q=2*(1-2*sqrt(2)/3)",
    "formula": "T_mix^q <= ln(1/epsilon)/Delta_q"
  },
  {
    "id": "Q18",
    "statement": "Classical diffusive steps to reach depth D=5 in the 1-dimensional proxy",
    "inputs": "D=5",
    "formula": "t_cl(D) = D^2"
  },
  {
    "id": "Q19",
    "statement": "Ballistic steps to reach depth D=5 in the 1-dimensional proxy",
    "inputs": "D=5",
    "formula": "t_bal(D) = D"
  }
]

## Script
```python
import math
from fractions import Fraction

results = []

def check(cid, computed, expected_str, sig=None):
    if expected_str is None:
        match = "no"
        results.append((cid, computed, "none", match))
        return
    exp_val = float(expected_str)
    if sig is None:
        match = "yes" if abs(computed - exp_val) <= 1e-9 * max(1.0, abs(exp_val)) else "no"
    else:
        # round computed to sig significant digits
        if computed == 0:
            rounded = 0.0
        else:
            rounded = round(computed, sig - int(math.floor(math.log10(abs(computed)))) - 1)
        match = "yes" if abs(rounded - exp_val) <= 1e-9 * max(1.0, abs(exp_val)) else "no"
    results.append((cid, computed, expected_str, match))

# Q1: C_tree = N*log2(N) + 2N - 2, N=1024
N = 1024
log2N = math.log2(N)
c_tree = N * log2N + 2 * N - 2
check("Q1", c_tree, "12286", sig=5)

# Q2: C_dot = N^2, N=1024
N = 1024
c_dot = N ** 2
check("Q2", c_dot, "1048576", sig=7)

# Q4: C_dot = N^2 * d, N=512, d=64
N = 512
d = 64
c_dot2 = N ** 2 * d
check("Q4", c_dot2, "16777216", sig=8)

# Q5: C_tree = N^2 * k, N=512, k=8
N = 512
k = 8
c_tree2 = N ** 2 * k
check("Q5", c_tree2, "2097152", sig=7)

def B(p, D):
    return 1 + (p + 1) * (p ** D - 1) / (p - 1)

# Q8: B_2(5)
b = B(2, 5)
check("Q8", b, "94", sig=2)

# Q9: B_3(5)
b = B(3, 5)
check("Q9", b, "485", sig=3)

# Q10: B_2(2)*B_3(2)
b = B(2, 2) * B(3, 2)
check("Q10", b, "170", sig=3)

# Q11: B_2(2)
b = B(2, 2)
check("Q11", b, "10", sig=2)

# Q12: B_3(2)
b = B(3, 2)
check("Q12", b, "17", sig=2)

# Q13: rho = 2*sqrt(p)/(p+1), p=2
p = 2
rho = 2 * math.sqrt(p) / (p + 1)
check("Q13", rho, "0.9428", sig=4)

# Q14: Delta = 1 - rho
delta = 1.0 - rho
check("Q14", delta, "0.0572", sig=3)

# Q15: T_mix = ln(1/eps)/Delta, eps=0.01
eps = 0.01
t_mix = math.log(1.0 / eps) / delta
check("Q15", t_mix, "80.5", sig=3)

# Q16: Delta_q = 2*Delta
delta_q = 2 * delta
check("Q16", delta_q, "0.1144", sig=4)

# Q17: T_mix_q = ln(1/eps)/Delta_q
t_mix_q = math.log(1.0 / eps) / delta_q
check("Q17", t_mix_q, "40.3", sig=3)

# Q18: t_cl(5) = 25
check("Q18", 5 ** 2, "25", sig=2)

# Q19: t_bal(5) = 5
check("Q19", 5, "5", sig=1)

for cid, computed, expected, match in results:
    print("CLAIM %s: computed=%.8g expected=%s match=%s" % (cid, computed, expected, match))

n = len(results)
m = sum(1 for r in results if r[3] == "yes")
k_mis = n - m
print("VERIFICATION SUMMARY: %d claims, %d match, %d mismatch" % (n, m, k_mis))

```

## Execution output
```
CLAIM Q1: computed=12286 expected=12286 match=yes
CLAIM Q2: computed=1048576 expected=1048576 match=yes
CLAIM Q4: computed=16777216 expected=16777216 match=yes
CLAIM Q5: computed=2097152 expected=2097152 match=yes
CLAIM Q8: computed=94 expected=94 match=yes
CLAIM Q9: computed=485 expected=485 match=yes
CLAIM Q10: computed=170 expected=170 match=yes
CLAIM Q11: computed=10 expected=10 match=yes
CLAIM Q12: computed=17 expected=17 match=yes
CLAIM Q13: computed=0.94280904 expected=0.9428 match=yes
CLAIM Q14: computed=0.057190958 expected=0.0572 match=yes
CLAIM Q15: computed=80.522696 expected=80.5 match=yes
CLAIM Q16: computed=0.11438192 expected=0.1144 match=yes
CLAIM Q17: computed=40.261348 expected=40.3 match=yes
CLAIM Q18: computed=25 expected=25 match=yes
CLAIM Q19: computed=5 expected=5 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 12286 | 12286 | yes | match | 5 significant digits (as printed, at least 3) |
| Q2 | 1048576 | 1048576 | yes | match | 7 significant digits (as printed, at least 3) |
| Q4 | 16777216 | 16777216 | yes | match | 8 significant digits (as printed, at least 3) |
| Q5 | 2097152 | 2097152 | yes | match | 7 significant digits (as printed, at least 3) |
| Q8 | 94 | 94 | yes | match | 3 significant digits (as printed, at least 3) |
| Q9 | 485 | 485 | yes | match | 3 significant digits (as printed, at least 3) |
| Q10 | 170 | 170 | yes | match | 3 significant digits (as printed, at least 3) |
| Q11 | 10 | 10 | yes | match | 3 significant digits (as printed, at least 3) |
| Q12 | 17 | 17 | yes | match | 3 significant digits (as printed, at least 3) |
| Q13 | 0.94280904 | 0.9428 | yes | match | 4 significant digits (as printed, at least 3) |
| Q14 | 0.057190958 | 0.0572 | yes | match | 3 significant digits (as printed, at least 3) |
| Q15 | 80.522696 | 80.5 | yes | match | 3 significant digits (as printed, at least 3) |
| Q16 | 0.11438192 | 0.1144 | yes | match | 4 significant digits (as printed, at least 3) |
| Q17 | 40.261348 | 40.3 | yes | match | 3 significant digits (as printed, at least 3) |
| Q18 | 25 | 25 | yes | match | 3 significant digits (as printed, at least 3) |
| Q19 | 5 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
