# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Scenario 1 total information delay tau_d = 50 ms",
    "inputs": "h = 5 hops, tau = 10 ms = 0.01 s",
    "formula": "tau_d = h * tau"
  },
  {
    "id": "Q2",
    "statement": "Scenario 1 Network Tracing Capacity Theta = 20 s^-1",
    "inputs": "tau_d = 0.05 s",
    "formula": "Theta = 1 / tau_d"
  },
  {
    "id": "Q3",
    "statement": "Horizon test product lambda*tau_d = 1.75 > 1",
    "inputs": "lambda = 35 s^-1, tau_d = 0.05 s",
    "formula": "lambda * tau_d"
  },
  {
    "id": "Q4",
    "statement": "Growth factor across full delay e^1.75 ≈ 5.75",
    "inputs": "lambda = 35 s^-1, tau_d = 0.05 s",
    "formula": "exp(lambda * tau_d)"
  },
  {
    "id": "Q5",
    "statement": "1/(lambda*tau) ≈ 2.86, horizon hop h* = 3",
    "inputs": "lambda = 35 s^-1, tau = 0.01 s",
    "formula": "1 / (lambda * tau), h* = ceil(1 / (lambda * tau))"
  },
  {
    "id": "Q6",
    "statement": "Scenario 2 delay tau_d = 0.01 s and Theta = 100 s^-1",
    "inputs": "h = 5, tau = 2 ms = 0.002 s",
    "formula": "tau_d = h * tau; Theta = 1 / tau_d"
  },
  {
    "id": "Q7",
    "statement": "Scenario 2 growth factor e^0.35 ≈ 1.42",
    "inputs": "lambda = 35 s^-1, tau_d = 0.01 s",
    "formula": "exp(lambda * tau_d)"
  },
  {
    "id": "Q8",
    "statement": "Cumulative walk count D_<=3 = 44",
    "inputs": "D1 = 4, D2 = 12, D3 = 28",
    "formula": "D1 + D2 + D3"
  },
  {
    "id": "Q9",
    "statement": "Closed form D_<=5 = 228",
    "inputs": "L = 5",
    "formula": "D_<=L = 2^(L+3) - 8 - 4L"
  },
  {
    "id": "Q10",
    "statement": "Closed form D_<=10 = 8144",
    "inputs": "L = 10",
    "formula": "D_<=L = 2^(L+3) - 8 - 4L"
  },
  {
    "id": "Q11",
    "statement": "Single-step rate scale kappa_NTC^(1)/tau = 4e3 s^-1",
    "inputs": "kappa_NTC^(1) = 4, tau = 1e-3 s",
    "formula": "kappa / tau"
  },
  {
    "id": "Q12",
    "statement": "Five-step rate scale kappa_NTC^(5)/tau = 2.2e5 s^-1",
    "inputs": "kappa_NTC^(5) = 220, tau = 1e-3 s",
    "formula": "kappa / tau"
  },
  {
    "id": "Q13",
    "statement": "Projection: at tau = 1e-4 s and lambda = 100 s^-1, max hops h < 100",
    "inputs": "tau = 1e-4 s, lambda = 100 s^-1",
    "formula": "h < 1 / (lambda * tau)"
  },
  {
    "id": "Q14",
    "statement": "Projection: at tau = 10 ms and lambda = 35 s^-1, h < 2.86, i.e. h <= 2",
    "inputs": "tau = 0.01 s, lambda = 35 s^-1",
    "formula": "h < 1 / (lambda * tau)"
  }
]

## Script
```python
import math

def claim(cid, computed, expected, match):
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: tau_d = h * tau = 5 * 0.01 = 0.05 s = 50 ms
q1 = 5 * 0.01
claim("Q1", q1, "0.05", "yes" if round(q1, 10) == 0.05 else "no")

# Q2: Theta = 1 / tau_d = 1 / 0.05 = 20
q2 = 1 / q1
claim("Q2", q2, "20", "yes" if round(q2, 8) == 20 else "no")

# Q3: lambda * tau_d = 35 * 0.05 = 1.75
q3 = 35 * q1
claim("Q3", q3, "1.75", "yes" if round(q3, 8) == 1.75 else "no")

# Q4: exp(lambda * tau_d) = exp(1.75) ≈ 5.75
q4 = math.exp(q3)
claim("Q4", q4, "5.75", "yes" if round(q4, 2) == 5.75 else "no")

# Q5: 1/(lambda*tau) = 1/(35*0.01) = 1/0.35 ≈ 2.857142..., h* = ceil = 3
q5a = 1 / (35 * 0.01)
q5b = math.ceil(q5a)
claim("Q5", q5a, "2.86", "yes" if round(q5a, 2) == 2.86 else "no")
claim("Q5b", q5b, "3", "yes" if q5b == 3 else "no")

# Q6: tau_d = 5 * 0.002 = 0.01 s; Theta = 1/0.01 = 100
q6a = 5 * 0.002
q6b = 1 / q6a
claim("Q6", q6b, "100", "yes" if round(q6b, 8) == 100 else "no")

# Q7: exp(35 * 0.01) = exp(0.35) ≈ 1.42
q7 = math.exp(35 * 0.01)
claim("Q7", q7, "1.42", "yes" if round(q7, 2) == 1.42 else "no")

# Q8: D1 + D2 + D3 = 4 + 12 + 28 = 44
q8 = 4 + 12 + 28
claim("Q8", q8, "44", "yes" if q8 == 44 else "no")

# Q9: D_<=5 = 2^(5+3) - 8 - 4*5 = 256 - 8 - 20 = 228
q9 = 2 ** (5 + 3) - 8 - 4 * 5
claim("Q9", q9, "228", "yes" if q9 == 228 else "no")

# Q10: D_<=10 = 2^(10+3) - 8 - 4*10 = 8192 - 8 - 40 = 8144
q10 = 2 ** (10 + 3) - 8 - 4 * 10
claim("Q10", q10, "8144", "yes" if q10 == 8144 else "no")

# Q11: kappa_NTC^(1) / tau = 4 / 1e-3 = 4000
q11 = 4 / 1e-3
claim("Q11", q11, "4000", "yes" if round(q11, 6) == 4000 else "no")

# Q12: kappa_NTC^(5) / tau = 220 / 1e-3 = 220000
q12 = 220 / 1e-3
claim("Q12", q12, "220000", "yes" if round(q12, 6) == 220000 else "no")

# Q13: h < 1/(lambda*tau) = 1/(100 * 1e-4) = 1/0.01 = 100
q13 = 1 / (100 * 1e-4)
claim("Q13", q13, "100", "yes" if round(q13, 8) == 100 else "no")

# Q14: h < 1/(35 * 0.01) = 1/0.35 ≈ 2.857142..., so h <= 2
q14 = 1 / (35 * 0.01)
claim("Q14", q14, "2.86", "yes" if round(q14, 2) == 2.86 else "no")

print("VERIFICATION SUMMARY: 15 claims, 15 match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.05 expected=0.05 match=yes
CLAIM Q2: computed=20.0 expected=20 match=yes
CLAIM Q3: computed=1.75 expected=1.75 match=yes
CLAIM Q4: computed=5.754602676005731 expected=5.75 match=yes
CLAIM Q5: computed=2.8571428571428568 expected=2.86 match=yes
CLAIM Q5b: computed=3 expected=3 match=yes
CLAIM Q6: computed=100.0 expected=100 match=yes
CLAIM Q7: computed=1.4190675485932573 expected=1.42 match=yes
CLAIM Q8: computed=44 expected=44 match=yes
CLAIM Q9: computed=228 expected=228 match=yes
CLAIM Q10: computed=8144 expected=8144 match=yes
CLAIM Q11: computed=4000.0 expected=4000 match=yes
CLAIM Q12: computed=220000.0 expected=220000 match=yes
CLAIM Q13: computed=100.0 expected=100 match=yes
CLAIM Q14: computed=2.8571428571428568 expected=2.86 match=yes
VERIFICATION SUMMARY: 15 claims, 15 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.05 | 0.05 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 20.0 | 20 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 1.75 | 1.75 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 5.754602676005731 | 5.75 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 2.8571428571428568 | 2.86 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5b | 3 | 3 | yes | match | 3 significant digits (as printed, at least 3) |
| Q6 | 100.0 | 100 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 1.4190675485932573 | 1.42 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 44 | 44 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 228 | 228 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 8144 | 8144 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 4000.0 | 4000 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 220000.0 | 220000 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 100.0 | 100 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 2.8571428571428568 | 2.86 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 15.
