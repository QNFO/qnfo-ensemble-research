# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Passive fault‑tolerance threshold for a depth‑3 binary tree is approximately 0.105 (10.5 %).",
    "inputs": "target logical error = 1e-3, depth d = 3",
    "formula": "p_th = (1e-3 / 2^d)^(1/(d+1))"
  },
  {
    "id": "Q2",
    "statement": "Cooling‑power gap between a 4 K cryocooler and the surface‑code operating temperature is approximately 92.2.",
    "inputs": "surface‑code temperature T_sc = 43.4 mK, cryocooler temperature T = 4 K",
    "formula": "gap = T / T_sc"
  },
  {
    "id": "Q3a",
    "statement": "Logical error probability bound for p = 0.10 and depth d = 1 is 0.020.",
    "inputs": "p = 0.10, d = 1",
    "formula": "P_logical ≤ 2^d * p^(d+1)"
  },
  {
    "id": "Q3b",
    "statement": "Logical error probability bound for p = 0.10 and depth d = 2 is 0.004.",
    "inputs": "p = 0.10, d = 2",
    "formula": "P_logical ≤ 2^d * p^(d+1)"
  },
  {
    "id": "Q3c",
    "statement": "Logical error probability bound for p = 0.10 and depth d = 3 is 0.0008.",
    "inputs": "p = 0.10, d = 3",
    "formula": "P_logical ≤ 2^d * p^(d+1)"
  },
  {
    "id": "Q4a",
    "statement": "Logical error probability bound for p = 0.30 and depth d = 1 is 0.180.",
    "inputs": "p = 0.30, d = 1",
    "formula": "P_logical ≤ 2^d * p^(d+1)"
  },
  {
    "id": "Q4b",
    "statement": "Logical error probability bound for p = 0.30 and depth d = 2 is 0.108.",
    "inputs": "p = 0.30, d = 2",
    "formula": "P_logical ≤ 2^d * p^(d+1)"
  },
  {
    "id": "Q4c",
    "statement": "Logical error probability bound for p = 0.30 and depth d = 3 is 0.0648.",
    "inputs": "p = 0.30, d = 3",
    "formula": "P_logical ≤ 2^d * p^(d+1)"
  },
  {
    "id": "Q5a",
    "statement": "Logical error probability bound for p = 0.50 and depth d = 1 is 0.500.",
    "inputs": "p = 0.50, d = 1",
    "formula": "P_logical ≤ 2^d * p^(d+1)"
  },
  {
    "id": "Q5b",
    "statement": "Logical error probability bound for p = 0.50 and depth d = 2 is 0.500.",
    "inputs": "p = 0.50, d = 2",
    "formula": "P_logical ≤ 2^d * p^(d+1)"
  },
  {
    "id": "Q5c",
    "statement": "Logical error probability bound for p = 0.50 and depth d = 3 is 0.500.",
    "inputs": "p = 0.50, d = 3",
    "formula": "P_logical ≤ 2^d * p^(d+1)"
  },
  {
    "id": "Q6",
    "statement": "Exact logical error probability for a depth‑4 binary tree (31 vertices) with p = 0.05 is approximately 0.797.",
    "inputs": "depth d = 4 → N = 2^(d+1)-1 = 31, p = 0.05",
    "formula": "P_logical = 1 - (1-p)^N"
  },
  {
    "id": "Q7",
    "statement": "Exact logical error probability for a depth‑5 binary tree (63 vertices) with p = 0.01 is approximately 0.46909446.",
    "inputs": "depth d = 5 → N = 2^(d+1)-1 = 63, p = 0.01",
    "formula": "P_logical = 1 - (1-p)^N"
  },
  {
    "id": "Q8",
    "statement": "A minimal experimental prototype requires 7 physical qubits (depth‑2 binary tree).",
    "inputs": "depth d = 2 → N = 2^(d+1)-1 = 7",
    "formula": "N = 2^(d+1) - 1"
  },
  {
    "id": "Q9",
    "statement": "Projected hardware cost for a depth‑3 tree (15 qubits) at $1 000 per qubit is $15 000.",
    "inputs": "cost per qubit = 1000, number of qubits = 15",
    "formula": "total cost = cost_per_qubit * number_of_qubits"
  },
  {
    "id": "Q10",
    "statement": "Cooling‑power gap between surface‑code requirement and passive scheme is approximately 2 × 10^4.",
    "inputs": "surface‑code cooling power ≈ few hundred µW (≈0.2 mW), passive scheme cooling power ≈ several watts (≈4 W)",
    "formula": "gap = 4 W / 0.2 mW"
  }
]

## Script
```python
import math

def fmt(x):
    # format with at least 8 significant digits, removing trailing zeros
    s = f"{x:.10g}"
    return s

# Q1
p_th = (1e-3 / (2**3))**(1/(3+1))
expected_q1 = "0.105"
match_q1 = "yes" if round(p_th, 3) == float(expected_q1) else "no"
print(f"CLAIM Q1: computed={fmt(p_th)} expected={expected_q1} match={match_q1}")

# Q2
gap = 4.0 / 0.0434  # temperatures in K (4 K / 43.4 mK = 4 / 0.0434)
expected_q2 = "92.2"
match_q2 = "yes" if round(gap, 1) == float(expected_q2) else "no"
print(f"CLAIM Q2: computed={fmt(gap)} expected={expected_q2} match={match_q2}")

# Q3a
P_q3a = (2**1) * (0.10**(1+1))
expected_q3a = "0.020"
match_q3a = "yes" if abs(P_q3a - 0.020) < 1e-12 else "no"
print(f"CLAIM Q3a: computed={fmt(P_q3a)} expected={expected_q3a} match={match_q3a}")

# Q3b
P_q3b = (2**2) * (0.10**(2+1))
expected_q3b = "0.004"
match_q3b = "yes" if abs(P_q3b - 0.004) < 1e-12 else "no"
print(f"CLAIM Q3b: computed={fmt(P_q3b)} expected={expected_q3b} match={match_q3b}")

# Q3c
P_q3c = (2**3) * (0.10**(3+1))
expected_q3c = "0.0008"
match_q3c = "yes" if abs(P_q3c - 0.0008) < 1e-12 else "no"
print(f"CLAIM Q3c: computed={fmt(P_q3c)} expected={expected_q3c} match={match_q3c}")

# Q4a
P_q4a = (2**1) * (0.30**(1+1))
expected_q4a = "0.180"
match_q4a = "yes" if abs(P_q4a - 0.180) < 1e-12 else "no"
print(f"CLAIM Q4a: computed={fmt(P_q4a)} expected={expected_q4a} match={match_q4a}")

# Q4b
P_q4b = (2**2) * (0.30**(2+1))
expected_q4b = "0.108"
match_q4b = "yes" if abs(P_q4b - 0.108) < 1e-12 else "no"
print(f"CLAIM Q4b: computed={fmt(P_q4b)} expected={expected_q4b} match={match_q4b}")

# Q4c
P_q4c = (2**3) * (0.30**(3+1))
expected_q4c = "0.0648"
match_q4c = "yes" if abs(P_q4c - 0.0648) < 1e-12 else "no"
print(f"CLAIM Q4c: computed={fmt(P_q4c)} expected={expected_q4c} match={match_q4c}")

# Q5a
P_q5a = (2**1) * (0.50**(1+1))
expected_q5a = "0.500"
match_q5a = "yes" if abs(P_q5a - 0.500) < 1e-12 else "no"
print(f"CLAIM Q5a: computed={fmt(P_q5a)} expected={expected_q5a} match={match_q5a}")

# Q5b
P_q5b = (2**2) * (0.50**(2+1))
expected_q5b = "0.500"
match_q5b = "yes" if abs(P_q5b - 0.500) < 1e-12 else "no"
print(f"CLAIM Q5b: computed={fmt(P_q5b)} expected={expected_q5b} match={match_q5b}")

# Q5c
P_q5c = (2**3) * (0.50**(3+1))
expected_q5c = "0.500"
match_q5c = "yes" if abs(P_q5c - 0.500) < 1e-12 else "no"
print(f"CLAIM Q5c: computed={fmt(P_q5c)} expected={expected_q5c} match={match_q5c}")

# Q6
N6 = 2**(4+1) - 1  # depth 4
p6 = 0.05
P_q6 = 1 - (1 - p6)**N6
expected_q6 = "0.797"
match_q6 = "yes" if round(P_q6, 3) == float(expected_q6) else "no"
print(f"CLAIM Q6: computed={fmt(P_q6)} expected={expected_q6} match={match_q6}")

# Q7
N7 = 2**(5+1) - 1  # depth 5
p7 = 0.01
P_q7 = 1 - (1 - p7)**N7
expected_q7 = "0.46909446"
match_q7 = "yes" if abs(P_q7 - 0.46909446) < 1e-9 else "no"
print(f"CLAIM Q7: computed={fmt(P_q7)} expected={expected_q7} match={match_q7}")

# Q8
d8 = 2
N8 = 2**(d8+1) - 1
expected_q8 = "7"
match_q8 = "yes" if N8 == int(expected_q8) else "no"
print(f"CLAIM Q8: computed={fmt(N8)} expected={expected_q8} match={match_q8}")

# Q9
cost_per_qubit = 1000
num_qubits = 15
total_cost = cost_per_qubit * num_qubits
expected_q9 = "15000"
match_q9 = "yes" if total_cost == int(expected_q9) else "no"
print(f"CLAIM Q9: computed={fmt(total_cost)} expected={expected_q9} match={match_q9}")

# Q10
gap_q10 = 4.0 / 0.0002  # 4 W / 0.2 mW
expected_q10 = "20000"
match_q10 = "yes" if int(gap_q10) == int(expected_q10) else "no"
print(f"CLAIM Q10: computed={fmt(gap_q10)} expected={expected_q10} match={match_q10}")

print(f"VERIFICATION SUMMARY: 10 claims, {sum([match_q1,match_q2,match_q3a,match_q3b,match_q3c,match_q4a,match_q4b,match_q4c,match_q5a,match_q5b,match_q5c,match_q6,match_q7,match_q8,match_q9,match_q10].count('yes'))} match, {sum([match_q1,match_q2,match_q3a,match_q3b,match_q3c,match_q4a,match_q4b,match_q4c,match_q5a,match_q5b,match_q5c,match_q6,match_q7,match_q8,match_q9,match_q10].count('no'))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.1057371263 expected=0.105 match=no
CLAIM Q2: computed=92.16589862 expected=92.2 match=yes
CLAIM Q3a: computed=0.02 expected=0.020 match=yes
CLAIM Q3b: computed=0.004 expected=0.004 match=yes
CLAIM Q3c: computed=0.0008 expected=0.0008 match=yes
CLAIM Q4a: computed=0.18 expected=0.180 match=yes
CLAIM Q4b: computed=0.108 expected=0.108 match=yes
CLAIM Q4c: computed=0.0648 expected=0.0648 match=yes
CLAIM Q5a: computed=0.5 expected=0.500 match=yes
CLAIM Q5b: computed=0.5 expected=0.500 match=yes
CLAIM Q5c: computed=0.5 expected=0.500 match=yes
CLAIM Q6: computed=0.7960931743 expected=0.797 match=no
CLAIM Q7: computed=0.469094457 expected=0.46909446 match=no
CLAIM Q8: computed=7 expected=7 match=yes
CLAIM Q9: computed=15000 expected=15000 match=yes
CLAIM Q10: computed=20000 expected=20000 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 111, in <module>
TypeError: 'int' object is not iterable

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.1057371263 | 0.105 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 92.16589862 | 92.2 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3a | 0.02 | 0.020 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3b | 0.004 | 0.004 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3c | 0.0008 | 0.0008 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4a | 0.18 | 0.180 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4b | 0.108 | 0.108 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4c | 0.0648 | 0.0648 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5a | 0.5 | 0.500 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5b | 0.5 | 0.500 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5c | 0.5 | 0.500 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 0.7960931743 | 0.797 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 0.469094457 | 0.46909446 | no | match | 8 significant digits (as the paper states, at least 2) |
| Q8 | 7 | 7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 15000 | 15000 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 20000 | 20000 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
