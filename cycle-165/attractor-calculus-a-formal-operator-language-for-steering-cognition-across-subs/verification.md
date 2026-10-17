# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Barrier height of the canonical potential is 0.25",
    "inputs": "V(x)=x^4/4-x^2/2; V(0)=0; V(±1)=-1/4",
    "formula": "DeltaV = V(0) - V(±1) = 0 - (-1/4)"
  },
  {
    "id": "Q2",
    "statement": "Minimal impulse cost E_imp = 2*DeltaV = 0.5",
    "inputs": "DeltaV=0.25",
    "formula": "E_imp = 2*DeltaV"
  },
  {
    "id": "Q3",
    "statement": "Impulse amplitude p ≈ 0.707107",
    "inputs": "DeltaV=0.25",
    "formula": "p = sqrt(2*DeltaV) = sqrt(0.5)"
  },
  {
    "id": "Q4",
    "statement": "Critical tilt u_c ≈ 0.384900",
    "inputs": "double root x=-1/sqrt(3); u_c = x^3 - x at x=-1/sqrt(3)",
    "formula": "u_c = 2/(3*sqrt(3))"
  },
  {
    "id": "Q5",
    "statement": "Tilt cost rate u_c^2 = 4/27 ≈ 0.148148",
    "inputs": "u_c = 2/(3*sqrt(3))",
    "formula": "u_c^2 = (2/(3*sqrt(3)))^2 = 4/27"
  },
  {
    "id": "Q6",
    "statement": "Break-even horizon T* = 27/8 = 3.375",
    "inputs": "E_imp=0.5; tilt rate 4/27",
    "formula": "T* = E_imp / (4/27) = 0.5*27/4"
  },
  {
    "id": "Q7",
    "statement": "Generalized barrier height DeltaV(a) = a^2/4",
    "inputs": "V_a(x)=x^4/4 - a x^2/2; minima at x=±sqrt(a) with V=-a^2/4; saddle V(0)=0",
    "formula": "DeltaV(a) = 0 - (-a^2/4)"
  },
  {
    "id": "Q8",
    "statement": "Generalized impulse cost E_imp(a) = a^2/2",
    "inputs": "DeltaV(a)=a^2/4",
    "formula": "E_imp(a) = 2*DeltaV(a)"
  },
  {
    "id": "Q9",
    "statement": "Generalized tilt cost rate u_c^2(a) = 4a^3/27",
    "inputs": "double root x=-sqrt(a/3); u_c(a)=2a^{3/2}/(3*sqrt(3))",
    "formula": "u_c(a)^2 = (2a^{3/2}/(3*sqrt(3)))^2 = 4a^3/27"
  },
  {
    "id": "Q10",
    "statement": "Generalized break-even horizon T*(a) = 27/(8a)",
    "inputs": "E_imp(a)=a^2/2; tilt rate 4a^3/27",
    "formula": "T*(a) = (a^2/2)/(4a^3/27)"
  },
  {
    "id": "Q11",
    "statement": "-ln(1-10^-3) ≈ 0.0010005",
    "inputs": "eps=10^-3",
    "formula": "-ln(1-eps)"
  },
  {
    "id": "Q12",
    "statement": "T_d / (-ln(1-eps)) ≈ 9.99500e8",
    "inputs": "T_d=10^6; -ln(1-eps)≈0.0010005",
    "formula": "10^6 / 0.0010005"
  },
  {
    "id": "Q13",
    "statement": "ln(9.99500e8) ≈ 20.722766",
    "inputs": "ratio ≈ 9.99500e8",
    "formula": "ln(9.99500e8)"
  },
  {
    "id": "Q14",
    "statement": "Required deepened barrier DeltaV' ≈ 1.0361383",
    "inputs": "D=0.05; ln ratio ≈ 20.722766",
    "formula": "DeltaV' = D * ln(T_d/(-ln(1-eps)))"
  },
  {
    "id": "Q15",
    "statement": "Required depth increase delta d ≈ 0.786138",
    "inputs": "DeltaV'≈1.0361383; DeltaV=0.25",
    "formula": "delta d = DeltaV' - DeltaV"
  },
  {
    "id": "Q16",
    "statement": "Deepened impulse cost E_imp' ≈ 2.072277",
    "inputs": "DeltaV'≈1.0361383",
    "formula": "E_imp' = 2*DeltaV'"
  }
]

## Script
```python
import math

def claim(qid, computed, expected, match):
    print(f"CLAIM {qid}: computed={computed:.8f} expected={expected} match={match}")

# Q1: DeltaV = 0 - (-1/4)
dV = 0 - (-1/4)
claim("Q1", dV, "0.25", round(dV, 8) == 0.25)

# Q2: E_imp = 2*DeltaV
E = 2 * dV
claim("Q2", E, "0.5", round(E, 8) == 0.5)

# Q3: p = sqrt(0.5)
p = math.sqrt(2 * dV)
claim("Q3", p, "0.707107", round(p, 6) == 0.707107)

# Q4: u_c = 2/(3*sqrt(3))
uc = 2 / (3 * math.sqrt(3))
claim("Q4", uc, "0.384900", round(uc, 6) == 0.384900)

# Q5: u_c^2 = 4/27
uc2 = uc ** 2
claim("Q5", uc2, "0.148148", round(uc2, 6) == 0.148148)

# Q6: T* = 0.5*27/4
Tstar = 0.5 * 27 / 4
claim("Q6", Tstar, "3.375", round(Tstar, 8) == 3.375)

# Q7: DeltaV(a) = a^2/4 at a=1
a = 1
dVa = 0 - (-(a**2) / 4)
claim("Q7", dVa, "0.25", round(dVa, 8) == 0.25)

# Q8: E_imp(a) = 2*DeltaV(a)
Ea = 2 * dVa
claim("Q8", Ea, "0.5", round(Ea, 8) == 0.5)

# Q9: u_c(a)^2 = 4a^3/27
uca = 2 * a**1.5 / (3 * math.sqrt(3))
uca2 = uca ** 2
claim("Q9", uca2, "0.148148", round(uca2, 6) == 0.148148)

# Q10: T*(a) = (a^2/2)/(4a^3/27)
Ta = (a**2 / 2) / (4 * a**3 / 27)
claim("Q10", Ta, "3.375", round(Ta, 8) == 3.375)

# Q11: -ln(1-eps)
eps = 1e-3
v11 = -math.log(1 - eps)
claim("Q11", v11, "0.0010005", round(v11, 7) == 0.0010005)

# Q12: T_d / (-ln(1-eps))
v12 = 1e6 / v11
claim("Q12", v12, "9.99500e8", round(v12, 4) == 9.99500e8)

# Q13: ln(ratio)
v13 = math.log(v12)
claim("Q13", v13, "20.722766", round(v13, 6) == 20.722766)

# Q14: DeltaV' = D * ln(ratio)
D = 0.05
v14 = D * v13
claim("Q14", v14, "1.0361383", round(v14, 7) == 1.0361383)

# Q15: delta d = DeltaV' - DeltaV
v15 = v14 - dV
claim("Q15", v15, "0.786138", round(v15, 6) == 0.786138)

# Q16: E_imp' = 2*DeltaV'
v16 = 2 * v14
claim("Q16", v16, "2.072277", round(v16, 6) == 2.072277)

n = 16
m = sum(1 for _ in [1]*n)  # placeholder replaced below
# Recount matches properly
matches = [
    round(dV, 8) == 0.25,
    round(E, 8) == 0.5,
    round(p, 6) == 0.707107,
    round(uc, 6) == 0.384900,
    round(uc2, 6) == 0.148148,
    round(Tstar, 8) == 3.375,
    round(dVa, 8) == 0.25,
    round(Ea, 8) == 0.5,
    round(uca2, 6) == 0.148148,
    round(Ta, 8) == 3.375,
    round(v11, 7) == 0.0010005,
    round(v12, 4) == 9.99500e8,
    round(v13, 6) == 20.722766,
    round(v14, 7) == 1.0361383,
    round(v15, 6) == 0.786138,
    round(v16, 6) == 2.072277,
]
m = sum(matches)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.25000000 expected=0.25 match=True
CLAIM Q2: computed=0.50000000 expected=0.5 match=True
CLAIM Q3: computed=0.70710678 expected=0.707107 match=True
CLAIM Q4: computed=0.38490018 expected=0.384900 match=True
CLAIM Q5: computed=0.14814815 expected=0.148148 match=True
CLAIM Q6: computed=3.37500000 expected=3.375 match=True
CLAIM Q7: computed=0.25000000 expected=0.25 match=True
CLAIM Q8: computed=0.50000000 expected=0.5 match=True
CLAIM Q9: computed=0.14814815 expected=0.148148 match=True
CLAIM Q10: computed=3.37500000 expected=3.375 match=True
CLAIM Q11: computed=0.00100050 expected=0.0010005 match=True
CLAIM Q12: computed=999499916.62497270 expected=9.99500e8 match=False
CLAIM Q13: computed=20.72276563 expected=20.722766 match=True
CLAIM Q14: computed=1.03613828 expected=1.0361383 match=True
CLAIM Q15: computed=0.78613828 expected=0.786138 match=True
CLAIM Q16: computed=2.07227656 expected=2.072277 match=True
VERIFICATION SUMMARY: 16 claims, 15 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.25000000 | 0.25 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.50000000 | 0.5 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.70710678 | 0.707107 | - | match | 6 significant digits (as the paper states, at least 2) |
| Q4 | 0.38490018 | 0.384900 | - | match | 6 significant digits (as the paper states, at least 2) |
| Q5 | 0.14814815 | 0.148148 | - | match | 6 significant digits (as the paper states, at least 2) |
| Q6 | 3.37500000 | 3.375 | - | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 0.25000000 | 0.25 | - | match | 3 significant digits (as printed, at least 3) |
| Q8 | 0.50000000 | 0.5 | - | match | 3 significant digits (as printed, at least 3) |
| Q9 | 0.14814815 | 0.148148 | - | match | 6 significant digits (as printed, at least 3) |
| Q10 | 3.37500000 | 3.375 | - | match | 4 significant digits (as printed, at least 3) |
| Q11 | 0.00100050 | 0.0010005 | - | match | 5 significant digits (as the paper states, at least 2) |
| Q12 | 999499916.62497270 | 9.99500e8 | - | match | 6 significant digits (as the paper states, at least 2) |
| Q13 | 20.72276563 | 20.722766 | - | match | 8 significant digits (as the paper states, at least 2) |
| Q14 | 1.03613828 | 1.0361383 | - | match | 8 significant digits (as the paper states, at least 2) |
| Q15 | 0.78613828 | 0.786138 | - | match | 6 significant digits (as the paper states, at least 2) |
| Q16 | 2.07227656 | 2.072277 | - | match | 7 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
