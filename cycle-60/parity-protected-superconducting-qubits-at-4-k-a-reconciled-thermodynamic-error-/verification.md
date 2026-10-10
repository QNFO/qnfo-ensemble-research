# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "kB/h = 20.8366 GHz/K",
    "inputs": "kB = 1.380649e-23 J/K; h = 6.62607015e-34 J·s",
    "formula": "kB/h"
  },
  {
    "id": "Q2",
    "statement": "kBT/h = 83.3465 GHz at 4 K and 2.08366 GHz at 0.1 K",
    "inputs": "kB/h = 20.8366 GHz/K; T_warm = 4 K; T_cold = 0.1 K",
    "formula": "(kB/h)*T"
  },
  {
    "id": "Q3",
    "statement": "p_th_Nb(4 K) = 1.5006e-2",
    "inputs": "Delta_Nb/h = 350 GHz; kBT_warm/h = 83.3465 GHz",
    "formula": "exp(-(Delta/h)/(kBT/h))"
  },
  {
    "id": "Q4",
    "statement": "p_th_Nb(0.1 K) ≈ 1.12e-73",
    "inputs": "Delta_Nb/h = 350 GHz; kBT_cold/h = 2.08366 GHz",
    "formula": "exp(-(Delta/h)/(kBT/h))"
  },
  {
    "id": "Q5",
    "statement": "Operating-point penalty factor of order 10^71.13",
    "inputs": "r_warm = 4.1995; r_cold = 167.97",
    "formula": "(r_cold - r_warm)/ln(10)"
  },
  {
    "id": "Q6",
    "statement": "Delta_Al/h = 44.0069 GHz",
    "inputs": "T_c_Al = 1.2 K; BCS factor 1.76; kB/h = 20.8366 GHz/K",
    "formula": "1.76*T_c*(kB/h)"
  },
  {
    "id": "Q7",
    "statement": "p_th_Al(4 K) = 0.5898",
    "inputs": "Delta_Al/h = 44.0069 GHz; kBT_warm/h = 83.3465 GHz",
    "formula": "exp(-(Delta_Al/h)/(kBT/h))"
  },
  {
    "id": "Q8",
    "statement": "p_th_Al(0.1 K) = 6.73e-10",
    "inputs": "Delta_Al/h = 44.0069 GHz; kBT_cold/h = 2.08366 GHz",
    "formula": "exp(-(Delta_Al/h)/(kBT/h))"
  }
]

## Script
```python
import math

kB = 1.380649e-23
h = 6.62607015e-34

# Q1: kB/h in GHz/K
kb_over_h = kB / h  # Hz/K
kb_over_h_GHz = kb_over_h / 1e9
print(f"CLAIM Q1: computed={kb_over_h_GHz:.6f} expected=20.8366 match={'yes' if math.isclose(kb_over_h_GHz, 20.8366, rel_tol=1e-4) else 'no'}")

# Q2: kBT/h at 4 K and 0.1 K (GHz)
kbT_warm = kb_over_h_GHz * 4.0
kbT_cold = kb_over_h_GHz * 0.1
q2_warm_ok = math.isclose(kbT_warm, 83.3465, rel_tol=1e-4)
q2_cold_ok = math.isclose(kbT_cold, 2.08366, rel_tol=1e-4)
print(f"CLAIM Q2: computed={kbT_warm:.4f}/{kbT_cold:.5f} expected=83.3465/2.08366 match={'yes' if q2_warm_ok and q2_cold_ok else 'no'}")

# Q3: p_th_Nb(4 K)
p3 = math.exp(-350.0 / kbT_warm)
print(f"CLAIM Q3: computed={p3:.6e} expected=1.5006e-2 match={'yes' if math.isclose(p3, 1.5006e-2, rel_tol=1e-3) else 'no'}")

# Q4: p_th_Nb(0.1 K)
p4 = math.exp(-350.0 / kbT_cold)
print(f"CLAIM Q4: computed={p4:.4e} expected=1.12e-73 match={'yes' if math.isclose(p4, 1.12e-73, rel_tol=1e-2) else 'no'}")

# Q5: penalty exponent
r_warm = 350.0 / kbT_warm
r_cold = 350.0 / kbT_cold
exponent = (r_cold - r_warm) / math.log(10)
print(f"CLAIM Q5: computed={exponent:.4f} expected=71.13 match={'yes' if math.isclose(exponent, 71.13, rel_tol=1e-3) else 'no'}")

# Q6: Delta_Al/h in GHz
delta_al = 1.76 * 1.2 * kb_over_h_GHz
print(f"CLAIM Q6: computed={delta_al:.4f} expected=44.0069 match={'yes' if math.isclose(delta_al, 44.0069, rel_tol=1e-4) else 'no'}")

# Q7: p_th_Al(4 K)
p7 = math.exp(-delta_al / kbT_warm)
print(f"CLAIM Q7: computed={p7:.4f} expected=0.5898 match={'yes' if math.isclose(p7, 0.5898, rel_tol=1e-3) else 'no'}")

# Q8: p_th_Al(0.1 K)
p8 = math.exp(-delta_al / kbT_cold)
print(f"CLAIM Q8: computed={p8:.4e} expected=6.73e-10 match={'yes' if math.isclose(p8, 6.73e-10, rel_tol=1e-2) else 'no'}")

claims = [kb_over_h_GHz == kb_over_h_GHz, q2_warm_ok and q2_cold_ok,
          math.isclose(p3, 1.5006e-2, rel_tol=1e-3),
          math.isclose(p4, 1.12e-73, rel_tol=1e-2),
          math.isclose(exponent, 71.13, rel_tol=1e-3),
          math.isclose(delta_al, 44.0069, rel_tol=1e-4),
          math.isclose(p7, 0.5898, rel_tol=1e-3),
          math.isclose(p8, 6.73e-10, rel_tol=1e-2)]
n = len(claims)
m = sum(claims)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=20.836619 expected=20.8366 match=yes
CLAIM Q2: computed=83.3465/2.08366 expected=83.3465/2.08366 match=yes
CLAIM Q3: computed=1.500551e-02 expected=1.5006e-2 match=yes
CLAIM Q4: computed=1.1221e-73 expected=1.12e-73 match=yes
CLAIM Q5: computed=71.1262 expected=71.13 match=yes
CLAIM Q6: computed=44.0069 expected=44.0069 match=yes
CLAIM Q7: computed=0.5898 expected=0.5898 match=yes
CLAIM Q8: computed=6.7251e-10 expected=6.73e-10 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
