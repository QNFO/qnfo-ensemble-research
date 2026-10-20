# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The basin radius R equals 0.0114286.",
    "inputs": "N_min = 50, N_max = 70",
    "formula": "R = 2/N_min - 2/N_max"
  },
  {
    "id": "Q2",
    "statement": "The basin volume V_basin equals approximately 4.103×10^{-4}.",
    "inputs": "R = 0.0114286",
    "formula": "V = pi * R^2"
  },
  {
    "id": "Q3",
    "statement": "The constant C equals 1.0258.",
    "inputs": "V_basin = 4.103e-4, N = 50",
    "formula": "C = V_basin * N^2"
  },
  {
    "id": "Q4",
    "statement": "The basin‑volume scaling law is V_basin(N) = 1.0258 N^{-2}.",
    "inputs": "C = 1.0258",
    "formula": "V_basin(N) = C * N^{-2}"
  },
  {
    "id": "Q5",
    "statement": "For tolerance ε = 10^{-3}, the simple dual‑subgradient iteration count T_simple equals 1000.",
    "inputs": "ε = 1e-3",
    "formula": "T_simple = ceil(1/ε)"
  },
  {
    "id": "Q6",
    "statement": "For tolerance ε = 10^{-3}, the sliding dual‑subgradient iteration count T_sliding equals 7.",
    "inputs": "ε = 1e-3",
    "formula": "T_sliding = ceil(ln(1/ε))"
  },
  {
    "id": "Q7",
    "statement": "For tolerance ε = 10^{-6}, T_simple equals 1,000,000.",
    "inputs": "ε = 1e-6",
    "formula": "T_simple = ceil(1/ε)"
  },
  {
    "id": "Q8",
    "statement": "For tolerance ε = 10^{-6}, T_sliding equals 14.",
    "inputs": "ε = 1e-6",
    "formula": "T_sliding = ceil(ln(1/ε))"
  },
  {
    "id": "Q9",
    "statement": "The polygenesis probability at N = 50 is P_poly = 4.103×10^{-4}.",
    "inputs": "C = 1.0258, N = 50",
    "formula": "P_poly = C * N^{-2}"
  },
  {
    "id": "Q10",
    "statement": "The polygenesis probability at N = 60 is P_poly = 2.849×10^{-4}.",
    "inputs": "C = 1.0258, N = 60",
    "formula": "P_poly = C * N^{-2}"
  },
  {
    "id": "Q11",
    "statement": "The ratio P_poly(60)/P_poly(50) equals 0.694.",
    "inputs": "P_poly(60) = 2.849e-4, P_poly(50) = 4.103e-4",
    "formula": "ratio = P_poly(60) / P_poly(50)"
  },
  {
    "id": "Q12",
    "statement": "The pairwise coincidence probability P_2 equals 0.2750.",
    "inputs": "p1 = 0.40, p2 = 0.25, p3 = 0.20, p4 = 0.10, p5 = 0.05",
    "formula": "P_2 = sum(p_i^2) for i=1..5"
  },
  {
    "id": "Q13",
    "statement": "The triple coincidence probability P_3 equals 0.08875.",
    "inputs": "p1 = 0.40, p2 = 0.25, p3 = 0.20, p4 = 0.10, p5 = 0.05",
    "formula": "P_3 = sum(p_i^3) for i=1..5"
  },
  {
    "id": "Q14",
    "statement": "The dominant‑basin share equals 0.582.",
    "inputs": "p1 = 0.40, P_2 = 0.2750",
    "formula": "share = p1^2 / P_2"
  },
  {
    "id": "Q15",
    "statement": "The odds ratio between dominant and runner‑up basins equals 2.56.",
    "inputs": "p1 = 0.40, p2 = 0.25",
    "formula": "odds = (p1 / p2)^2"
  },
  {
    "id": "Q16",
    "statement": "The contraction‑based iteration count to reach ε = 10^{-2} is approximately 458.2.",
    "inputs": "ε = 1e-2, d0 = 1, q = 0.99",
    "formula": "n = ln(ε/d0) / ln(q)"
  }
]

## Script
```python
import math

def fmt(x):
    # format with at least 8 significant digits, removing trailing zeros
    if isinstance(x, int):
        return str(x)
    s = f"{x:.10g}"
    # ensure at least 8 significant digits
    if 'e' in s or '.' in s:
        return s
    return s

# Q1
R = 2/50 - 2/70
exp_Q1 = "0.0114286"
print(f"CLAIM Q1: computed={fmt(R)} expected={exp_Q1} match={'yes' if round(R,7)==float(exp_Q1) else 'no'}")

# Q2
V = math.pi * R**2
exp_Q2 = "0.0004103"
print(f"CLAIM Q2: computed={fmt(V)} expected={exp_Q2} match={'yes' if round(V,7)==float(exp_Q2) else 'no'}")

# Q3
C = V * 50**2
exp_Q3 = "1.0258"
print(f"CLAIM Q3: computed={fmt(C)} expected={exp_Q3} match={'yes' if round(C,4)==float(exp_Q3) else 'no'}")

# Q4 (use N=50 to produce numeric V)
V_N50 = C * 50**-2
exp_Q4 = "0.0004103"
print(f"CLAIM Q4: computed={fmt(V_N50)} expected={exp_Q4} match={'yes' if round(V_N50,7)==float(exp_Q4) else 'no'}")

# Q5
eps = 1e-3
T_simple = math.ceil(1/eps)
exp_Q5 = "1000"
print(f"CLAIM Q5: computed={fmt(T_simple)} expected={exp_Q5} match={'yes' if T_simple==int(exp_Q5) else 'no'}")

# Q6
T_sliding = math.ceil(math.log(1/eps))
exp_Q6 = "7"
print(f"CLAIM Q6: computed={fmt(T_sliding)} expected={exp_Q6} match={'yes' if T_sliding==int(exp_Q6) else 'no'}")

# Q7
eps = 1e-6
T_simple = math.ceil(1/eps)
exp_Q7 = "1000000"
print(f"CLAIM Q7: computed={fmt(T_simple)} expected={exp_Q7} match={'yes' if T_simple==int(exp_Q7) else 'no'}")

# Q8
T_sliding = math.ceil(math.log(1/eps))
exp_Q8 = "14"
print(f"CLAIM Q8: computed={fmt(T_sliding)} expected={exp_Q8} match={'yes' if T_sliding==int(exp_Q8) else 'no'}")

# Q9
P50 = C * 50**-2
exp_Q9 = "0.0004103"
print(f"CLAIM Q9: computed={fmt(P50)} expected={exp_Q9} match={'yes' if round(P50,7)==float(exp_Q9) else 'no'}")

# Q10
P60 = C * 60**-2
exp_Q10 = "0.0002849"
print(f"CLAIM Q10: computed={fmt(P60)} expected={exp_Q10} match={'yes' if round(P60,7)==float(exp_Q10) else 'no'}")

# Q11
ratio = P60 / P50
exp_Q11 = "0.694"
print(f"CLAIM Q11: computed={fmt(ratio)} expected={exp_Q11} match={'yes' if round(ratio,3)==float(exp_Q11) else 'no'}")

# Q12
p = [0.40,0.25,0.20,0.10,0.05]
P2 = sum([pi**2 for pi in p])
exp_Q12 = "0.2750"
print(f"CLAIM Q12: computed={fmt(P2)} expected={exp_Q12} match={'yes' if round(P2,4)==float(exp_Q12) else 'no'}")

# Q13
P3 = sum([pi**3 for pi in p])
exp_Q13 = "0.08875"
print(f"CLAIM Q13: computed={fmt(P3)} expected={exp_Q13} match={'yes' if round(P3,5)==float(exp_Q13) else 'no'}")

# Q14
share = p[0]**2 / P2
exp_Q14 = "0.582"
print(f"CLAIM Q14: computed={fmt(share)} expected={exp_Q14} match={'yes' if round(share,3)==float(exp_Q14) else 'no'}")

# Q15
odds = (p[0]/p[1])**2
exp_Q15 = "2.56"
print(f"CLAIM Q15: computed={fmt(odds)} expected={exp_Q15} match={'yes' if round(odds,2)==float(exp_Q15) else 'no'}")

# Q16
epsilon = 1e-2
d0 = 1.0
q = 0.99
n = math.log(epsilon/d0) / math.log(q)
exp_Q16 = "458.2"
print(f"CLAIM Q16: computed={fmt(n)} expected={exp_Q16} match={'yes' if round(n,1)==float(exp_Q16) else 'no'}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for line in open(__file__) if 'match=yes' in line)} match, {16 - sum(1 for line in open(__file__) if 'match=yes' in line)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.01142857143 expected=0.0114286 match=yes
CLAIM Q2: computed=0.000410330469 expected=0.0004103 match=yes
CLAIM Q3: computed=1.025826173 expected=1.0258 match=yes
CLAIM Q4: computed=0.000410330469 expected=0.0004103 match=yes
CLAIM Q5: computed=1000 expected=1000 match=yes
CLAIM Q6: computed=7 expected=7 match=yes
CLAIM Q7: computed=1000000 expected=1000000 match=yes
CLAIM Q8: computed=14 expected=14 match=yes
CLAIM Q9: computed=0.000410330469 expected=0.0004103 match=yes
CLAIM Q10: computed=0.0002849517146 expected=0.0002849 match=no
CLAIM Q11: computed=0.6944444444 expected=0.694 match=yes
CLAIM Q12: computed=0.275 expected=0.2750 match=yes
CLAIM Q13: computed=0.08875 expected=0.08875 match=yes
CLAIM Q14: computed=0.5818181818 expected=0.582 match=yes
CLAIM Q15: computed=2.56 expected=2.56 match=yes
CLAIM Q16: computed=458.2105766 expected=458.2 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 99, in <module>
NameError: name '__file__' is not defined. Did you mean: '__name__'?

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.01142857143 | 0.0114286 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q2 | 0.000410330469 | 0.0004103 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 1.025826173 | 1.0258 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q4 | 0.000410330469 | 0.0004103 | yes | match | 4 significant digits (as printed, at least 3) |
| Q5 | 1000 | 1000 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 7 | 7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 1000000 | 1000000 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q8 | 14 | 14 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 0.000410330469 | 0.0004103 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 0.0002849517146 | 0.0002849 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 0.6944444444 | 0.694 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 0.275 | 0.2750 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 0.08875 | 0.08875 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q14 | 0.5818181818 | 0.582 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 2.56 | 2.56 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 458.2105766 | 458.2 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
