# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Conventional non-adiabatic full-cycle dissipation E_conv = CV² = 25 aJ",
    "inputs": "C = 100e-15 F; V = 0.5e-3 V",
    "formula": "E_conv = C * V^2 = 100e-15 * (0.5e-3)^2 = 2.5e-20 J"
  },
  {
    "id": "Q2",
    "statement": "RC time constant of the charging path is 1 ns",
    "inputs": "R = 10e3 Ω; C = 100e-15 F",
    "formula": "RC = R * C = 10e3 * 100e-15 = 1e-9 s"
  },
  {
    "id": "Q3",
    "statement": "Adiabaticity ratio T/RC = 10 at the design point",
    "inputs": "T = 10e-9 s; RC = 1e-9 s",
    "formula": "T/RC = 10e-9 / 1e-9 = 10"
  },
  {
    "id": "Q4",
    "statement": "Conservative adiabatic clock ceiling is 5 MHz per node",
    "inputs": "RC = 1e-9 s; criterion T = 100*RC = 100e-9 s",
    "formula": "f = 1/(2*T) = 1/(2*100e-9) = 5e6 Hz"
  },
  {
    "id": "Q5",
    "statement": "Adiabatic dissipation per event E_ad = 2.5 zJ",
    "inputs": "RC = 1e-9 s; T = 10e-9 s; C = 100e-15 F; V = 0.5e-3 V",
    "formula": "E_ad = (RC/T)*C*V^2 = (1e-9/10e-9)*100e-15*(0.5e-3)^2 = 2.5e-21 J"
  },
  {
    "id": "Q6",
    "statement": "Static leakage power P_static = 5e-13 W",
    "inputs": "I_leak = 1e-9 A; V = 0.5e-3 V",
    "formula": "P_static = I_leak * V = 1e-9 * 0.5e-3 = 5e-13 W"
  },
  {
    "id": "Q7",
    "statement": "Static leakage energy per event window E_static = 5 zJ",
    "inputs": "P_static = 5e-13 W; T = 10e-9 s",
    "formula": "E_static = P_static * T = 5e-13 * 10e-9 = 5e-21 J"
  },
  {
    "id": "Q8",
    "statement": "Total event energy E_event = 7.5 zJ",
    "inputs": "E_ad = 2.5e-21 J; E_static = 5e-21 J",
    "formula": "E_event = E_ad + E_static = 2.5e-21 + 5e-21 = 7.5e-21 J"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: E_conv = C * V^2
C = 100e-15
V = 0.5e-3
E_conv = C * V**2
results.append(check("Q1", E_conv, 25e-21))

# Q2: RC = R * C
R = 10e3
RC = R * C
results.append(check("Q2", RC, 1e-9))

# Q3: T/RC
T = 10e-9
ratio = T / RC
results.append(check("Q3", ratio, 10.0))

# Q4: f = 1/(2*T) with T = 100*RC
T_cons = 100 * RC
f = 1 / (2 * T_cons)
results.append(check("Q4", f, 5e6))

# Q5: E_ad = (RC/T) * C * V^2
E_ad = (RC / T) * C * V**2
results.append(check("Q5", E_ad, 2.5e-21))

# Q6: P_static = I_leak * V
I_leak = 1e-9
P_static = I_leak * V
results.append(check("Q6", P_static, 5e-13))

# Q7: E_static = P_static * T
E_static = P_static * T
results.append(check("Q7", E_static, 5e-21))

# Q8: E_event = E_ad + E_static
E_event = E_ad + E_static
results.append(check("Q8", E_event, 7.5e-21))

n = len(results)
m = sum(results)
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")

```

## Execution output
```
CLAIM Q1: computed=2.5e-20 expected=2.5e-20 match=yes
CLAIM Q2: computed=1e-09 expected=1e-09 match=yes
CLAIM Q3: computed=10.0 expected=10.0 match=yes
CLAIM Q4: computed=5000000.0 expected=5000000.0 match=yes
CLAIM Q5: computed=2.5000000000000002e-21 expected=2.5e-21 match=yes
CLAIM Q6: computed=5.000000000000001e-13 expected=5e-13 match=yes
CLAIM Q7: computed=5.000000000000001e-21 expected=5e-21 match=yes
CLAIM Q8: computed=7.500000000000002e-21 expected=7.5e-21 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
