# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "At epsilon = 1e-4 exactly, epsilon_L = A = 1 per cycle for every d (zero protection)",
    "inputs": "epsilon = 1e-4, epsilon_th = 1e-4, A = 1",
    "formula": "epsilon_L = A * (epsilon/epsilon_th)^((d+1)/2)"
  },
  {
    "id": "Q2",
    "statement": "At epsilon = 1e-5, reliability target P_fail <= 0.01 over T = 1e9 cycles requires d >= 21",
    "inputs": "T = 1e9, epsilon = 1e-5, epsilon_th = 1e-4, P_fail = 0.01, A = 1",
    "formula": "d >= 2*ln(0.01/(T*A))/ln(epsilon/epsilon_th) - 1"
  },
  {
    "id": "Q3",
    "statement": "At d = 21 on T_3 (q = 3, R = 10), physical sites per logical qubit N_phys = V_3(10) = 88573",
    "inputs": "q = 3, R = 10",
    "formula": "V_q(R) = 1 + q*(q^R - 1)/(q - 1)"
  },
  {
    "id": "Q4",
    "statement": "At d = 21 and f_c = 1e6 s^-1, measurement bandwidth B = 8.8573e10 s^-1 per logical qubit",
    "inputs": "V_3(10) = 88573, f_c = 1e6",
    "formula": "B = V_3(10) * f_c"
  },
  {
    "id": "Q5",
    "statement": "A distance-11 code meets the target only if epsilon <= 1.4678e-6",
    "inputs": "d = 11, T = 1e9, epsilon_th = 1e-4, P_fail = 0.01, A = 1",
    "formula": "epsilon <= epsilon_th * (0.01/(T*A))^(2/(d+1))"
  },
  {
    "id": "Q6",
    "statement": "Factor between hypothesized threshold and d=11 operating point is approx 68.13",
    "inputs": "epsilon_th = 1e-4, epsilon_max = 1.4678e-6",
    "formula": "epsilon_th / epsilon_max"
  },
  {
    "id": "Q7",
    "statement": "At epsilon = 5e-5, target requires d >= 73 (R = 36)",
    "inputs": "epsilon = 5e-5, epsilon_th = 1e-4, T = 1e9, P_fail = 0.01, A = 1",
    "formula": "d >= 2*ln(0.01/(T*A))/ln(epsilon/epsilon_th) - 1"
  },
  {
    "id": "Q8",
    "statement": "At epsilon = 5e-5, N_phys = V_3(36) = 225141952945498681 approx 2.2514e17 sites",
    "inputs": "q = 3, R = 36",
    "formula": "V_q(R) = 1 + q*(q^R - 1)/(q - 1)"
  }
]

## Script
```python
import math

def report(cid, computed, expected):
    if isinstance(computed, float) and isinstance(expected, float):
        match = math.isclose(computed, expected, rel_tol=1e-6)
    else:
        match = (computed == expected)
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

# Q1: epsilon_L at epsilon = epsilon_th
eps, eps_th, A, d = 1e-4, 1e-4, 1.0, 21
epsL = A * (eps / eps_th) ** ((d + 1) / 2)
report("Q1", epsL, 1.0)

# Q2: required distance at epsilon = 1e-5
T, Pfail = 1e9, 0.01
d_req = 2 * math.log(Pfail / (T * A)) / math.log(eps / eps_th) - 1
report("Q2", d_req, 21.0)

# Q3: tree volume V_3(10)
q, R = 3, 10
V = 1 + q * (q**R - 1) // (q - 1)
report("Q3", V, 88573)

# Q4: bandwidth B = V * f_c
f_c = 1e6
B = V * f_c
report("Q4", B, 8.8573e10)

# Q5: max epsilon for d = 11
d2 = 11
eps_max = eps_th * (Pfail / (T * A)) ** (2 / (d2 + 1))
report("Q5", eps_max, 1.4678e-6)

# Q6: ratio eps_th / eps_max
ratio = eps_th / eps_max
report("Q6", ratio, 68.13)

# Q7: required distance at epsilon = 5e-5
eps3 = 5e-5
d_req3 = 2 * math.log(Pfail / (T * A)) / math.log(eps3 / eps_th) - 1
report("Q7", d_req3, 73.0)

# Q8: tree volume V_3(36)
R3 = 36
V3 = 1 + q * (q**R3 - 1) // (q - 1)
report("Q8", V3, 225141952945498681)

n = 8
m = sum(1 for _ in [0]*n)  # placeholder replaced below
# Recount matches explicitly
matches = 0
def check(cid, computed, expected):
    global matches
    if isinstance(computed, float) and isinstance(expected, float):
        ok = math.isclose(computed, expected, rel_tol=1e-6)
    else:
        ok = (computed == expected)
    if ok:
        matches += 1

check("Q1", epsL, 1.0)
check("Q2", d_req, 21.0)
check("Q3", V, 88573)
check("Q4", B, 8.8573e10)
check("Q5", eps_max, 1.4678e-6)
check("Q6", ratio, 68.13)
check("Q7", d_req3, 73.0)
check("Q8", V3, 225141952945498681)

print(f"VERIFICATION SUMMARY: {n} claims, {matches} match, {n - matches} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.0 expected=1.0 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 17, in <module>
ZeroDivisionError: float division by zero

[exit 1]
```
