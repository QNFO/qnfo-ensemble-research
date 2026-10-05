# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Number of noise locations for a d=3, R=4 rotated surface code is n_c = 228.",
    "inputs": "per-round locations = 57 (9 idle + 4*8=32 gate + 8 prep + 8 measurement), rounds R = 4",
    "formula": "n_c = 4 * 57 = 228"
  },
  {
    "id": "Q2",
    "statement": "Hotspot fraction 5%-7% corresponds to 11 to 16 components.",
    "inputs": "n_c = 228, f_low = 0.05, f_high = 0.07",
    "formula": "m = f * n_c; 0.05*228 ≈ 11, 0.07*228 ≈ 16"
  },
  {
    "id": "Q3",
    "statement": "Sensitivity contrast required for rho = 2 at f = 0.05 is r ≈ 2.111.",
    "inputs": "rho = 2, f = 0.05",
    "formula": "r = 2(1-f)/(1-2f) = (2*0.95)/(1-0.10) = 1.90/0.90 ≈ 2.111"
  },
  {
    "id": "Q4",
    "statement": "Sensitivity contrast required for rho = 2 at f = 0.07 is r ≈ 2.163.",
    "inputs": "rho = 2, f = 0.07",
    "formula": "r = 2(1-f)/(1-2f) = (2*0.93)/(1-0.14) = 1.86/0.86 ≈ 2.163"
  },
  {
    "id": "Q5",
    "statement": "For r = 3, hotspot fraction giving rho = 2 is f = 0.20.",
    "inputs": "r = 3, rho = 2",
    "formula": "f = (r-2)/(2r-1) = (3-2)/(6-1) = 1/5 = 0.20"
  },
  {
    "id": "Q6",
    "statement": "Midpoint contrast r ≈ 2.136 at f = 0.06 gives rho = 2 exactly.",
    "inputs": "f = 0.06, r = 1.88/0.88 ≈ 2.136",
    "formula": "rho = r/(f*r + 1 - f) = 2.136/(0.06*2.136 + 0.94) = 2.136/1.0682 = 2.000"
  },
  {
    "id": "Q7",
    "statement": "Linearized logical error rate P_L ≈ 0.2435 s.",
    "inputs": "n_c = 228, p = 10^-3, s = 1, f = 0.06, r = 2.136",
    "formula": "P_L = n_c * p * s * (1 + f(r-1)) = 228 * 10^-3 * 1.0682 ≈ 0.2435"
  },
  {
    "id": "Q8",
    "statement": "First-order targeted fractional reduction G_tgt ≈ 0.0614 (6.14%).",
    "inputs": "m = 14, r = 2.136, n_c = 228, f = 0.06",
    "formula": "G_tgt = m*r / (2*n_c*(1 + f(r-1))) = (14*2.136)/(2*228*1.0682) = 29.904/487.10 ≈ 0.0614"
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

# Q1: n_c = 4 * 57
per_round = 9 + 4*8 + 8 + 8
n_c = 4 * per_round
results.append(check("Q1", n_c, 228))

# Q2: m = f * n_c
m_low = 0.05 * n_c
m_high = 0.07 * n_c
results.append(check("Q2", round(m_low), 11))
results.append(check("Q2", round(m_high), 16))

# Q3: r = 2(1-f)/(1-2f) at f=0.05
r3 = 2*(1-0.05)/(1-2*0.05)
results.append(check("Q3", r3, 2.111))

# Q4: r at f=0.07
r4 = 2*(1-0.07)/(1-2*0.07)
results.append(check("Q4", r4, 2.163))

# Q5: f = (r-2)/(2r-1) at r=3
f5 = (3-2)/(2*3-1)
results.append(check("Q5", f5, 0.20))

# Q6: rho = r/(f*r+1-f) at f=0.06, r=1.88/0.88
r6 = 1.88/0.88
rho6 = r6/(0.06*r6 + 1 - 0.06)
results.append(check("Q6", rho6, 2.000))

# Q7: P_L = n_c * p * s * (1 + f(r-1))
p = 1e-3
s = 1.0
f = 0.06
r = 2.136
P_L = n_c * p * s * (1 + f*(r-1))
results.append(check("Q7", P_L, 0.2435))

# Q8: G_tgt = m*r / (2*n_c*(1 + f(r-1)))
m = 14
G_tgt = m*r / (2*n_c*(1 + f*(r-1)))
results.append(check("Q8", G_tgt, 0.0614))

N = len(results)
M = sum(results)
K = N - M
print(f"VERIFICATION SUMMARY: {N} claims, {M} match, {K} mismatch")

```

## Execution output
```
Network connection lost.
```
