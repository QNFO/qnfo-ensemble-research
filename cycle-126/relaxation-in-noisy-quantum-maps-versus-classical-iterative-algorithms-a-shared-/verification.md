# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "At epsilon=0.01, D0=1, delta=1e-6, the relaxation step count is 1374.6 steps.",
    "inputs": "epsilon=0.01, D0=1, delta=1e-6, ln10=2.302585",
    "formula": "t_delta = ln(delta/D0)/ln(1-epsilon)"
  },
  {
    "id": "Q2",
    "statement": "At epsilon=0.001, the step count is 13808.6 steps.",
    "inputs": "epsilon=0.001, D0=1, delta=1e-6",
    "formula": "t_delta = ln(delta/D0)/ln(1-epsilon)"
  },
  {
    "id": "Q3",
    "statement": "Reducing epsilon from 0.01 to 0.001 multiplies the step count by 10.045.",
    "inputs": "t_delta(0.01)=1374.6, t_delta(0.001)=13808.6",
    "formula": "ratio = t_delta(0.001)/t_delta(0.01)"
  },
  {
    "id": "Q4",
    "statement": "A pure qubit state crosses the fidelity threshold F=0.874 after 28.9 steps at epsilon=0.01.",
    "inputs": "F*=0.874, epsilon=0.01",
    "formula": "t* = ln(2F*-1)/ln(1-epsilon)"
  },
  {
    "id": "Q5",
    "statement": "At epsilon=0.1 the threshold F=0.874 is crossed after 2.756 steps.",
    "inputs": "F*=0.874, epsilon=0.1",
    "formula": "t* = ln(2F*-1)/ln(1-epsilon)"
  },
  {
    "id": "Q6",
    "statement": "At epsilon=0.001 the threshold F=0.874 is crossed after 290.2 steps.",
    "inputs": "F*=0.874, epsilon=0.001",
    "formula": "t* = ln(2F*-1)/ln(1-epsilon)"
  },
  {
    "id": "Q7",
    "statement": "A tenfold reduction in tolerance adds about 229.1 steps at epsilon=0.01.",
    "inputs": "ln10=2.302585, ln(0.99)=-0.010050336",
    "formula": "delta_t = ln10/(-ln(0.99))"
  }
]

## Script
```python
import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

ln10 = math.log(10)

# Q1
t1 = math.log(1e-6 / 1) / math.log(0.99)
# Q2
t2 = math.log(1e-6 / 1) / math.log(0.999)
# Q3
r3 = t2 / t1
# Q4
t4 = math.log(2 * 0.874 - 1) / math.log(0.99)
# Q5
t5 = math.log(2 * 0.874 - 1) / math.log(0.9)
# Q6
t6 = math.log(2 * 0.874 - 1) / math.log(0.999)
# Q7
dt7 = ln10 / (-math.log(0.99))

print("CLAIM Q1: computed=%.8f expected=1374.6 match=%s" % (t1, "yes" if sig(t1, 5) == 1374.6 else "no"))
print("CLAIM Q2: computed=%.8f expected=13808.6 match=%s" % (t2, "yes" if sig(t2, 6) == 13808.6 else "no"))
print("CLAIM Q3: computed=%.8f expected=10.045 match=%s" % (r3, "yes" if sig(r3, 4) == 10.045 else "no"))
print("CLAIM Q4: computed=%.8f expected=28.9 match=%s" % (t4, "yes" if sig(t4, 3) == 28.9 else "no"))
print("CLAIM Q5: computed=%.8f expected=2.756 match=%s" % (t5, "yes" if sig(t5, 4) == 2.756 else "no"))
print("CLAIM Q6: computed=%.8f expected=290.2 match=%s" % (t6, "yes" if sig(t6, 4) == 290.2 else "no"))
print("CLAIM Q7: computed=%.8f expected=229.1 match=%s" % (dt7, "yes" if sig(dt7, 4) == 229.1 else "no"))

claims = [sig(t1,5)==1374.6, sig(t2,6)==13808.6, sig(r3,4)==10.045, sig(t4,3)==28.9, sig(t5,4)==2.756, sig(t6,4)==290.2, sig(dt7,4)==229.1]
m = sum(claims)
print("VERIFICATION SUMMARY: %d claims, %d match, %d mismatch" % (len(claims), m, len(claims) - m))

```

## Execution output
```
CLAIM Q1: computed=1374.63172966 expected=1374.6 match=yes
CLAIM Q2: computed=13808.60165082 expected=13808.6 match=yes
CLAIM Q3: computed=10.04530985 expected=10.045 match=no
CLAIM Q4: computed=28.88981077 expected=28.9 match=yes
CLAIM Q5: computed=2.75579803 expected=2.756 match=yes
CLAIM Q6: computed=290.20710065 expected=290.2 match=yes
CLAIM Q7: computed=229.10528828 expected=229.1 match=yes
VERIFICATION SUMMARY: 7 claims, 6 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1374.63172966 | 1374.6 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 13808.60165082 | 13808.6 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q3 | 10.04530985 | 10.045 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q4 | 28.88981077 | 28.9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 2.75579803 | 2.756 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 290.20710065 | 290.2 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 229.10528828 | 229.1 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 7.
