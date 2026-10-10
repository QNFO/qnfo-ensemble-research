# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Switching cost per operation c_sw = 65 time units",
    "inputs": "k_acc=4, t_mem=16, t_alu=1",
    "formula": "c_sw = k_acc*t_mem + t_alu"
  },
  {
    "id": "Q2",
    "statement": "Switching overhead fraction f_sw = 64/65 = 0.984615...",
    "inputs": "k_acc=4, t_mem=16, t_alu=1",
    "formula": "f_sw = (k_acc*t_mem)/(k_acc*t_mem + t_alu)"
  },
  {
    "id": "Q3",
    "statement": "Re-entry cost per operation c_re = 5 time units",
    "inputs": "t_dyn=4, t_re=1",
    "formula": "c_re = t_dyn + t_re"
  },
  {
    "id": "Q4",
    "statement": "Re-entry overhead fraction f_re = 0.2",
    "inputs": "t_dyn=4, t_re=1",
    "formula": "f_re = t_re/(t_dyn + t_re)"
  },
  {
    "id": "Q5",
    "statement": "Total switching time T_sw = 6.5e7 time units for N_op = 1e6",
    "inputs": "N_op=1000000, c_sw=65",
    "formula": "T_sw = N_op*c_sw"
  },
  {
    "id": "Q6",
    "statement": "Total re-entry time T_re = 5.0e6 time units for N_op = 1e6",
    "inputs": "N_op=1000000, c_re=5",
    "formula": "T_re = N_op*c_re"
  },
  {
    "id": "Q7",
    "statement": "Total-time ratio T_sw/T_re = 13.0",
    "inputs": "c_sw=65, c_re=5",
    "formula": "ratio = c_sw/c_re"
  },
  {
    "id": "Q8",
    "statement": "Break-even memory time t_mem* = 1 time unit",
    "inputs": "t_dyn=4, t_re=1, t_alu=1, k_acc=4",
    "formula": "t_mem* = (t_dyn + t_re - t_alu)/k_acc"
  }
]

## Script
```python
import math
from fractions import Fraction

# Stated inputs from the paper (Section 4: Inputs 1 and 2)
k_acc = 4        # memory accesses per operation (structural integer)
t_mem = 16       # time units per memory access (assumed)
t_alu = 1        # time units for logical work (assumed normalization)
t_dyn = 4        # time units per useful dynamical segment (assumed)
t_re = 1         # time units re-entry overhead (assumed)
N_op = 10**6     # operations in Derivation 5

results = []

def check(cid, computed, expected):
    if expected is None:
        match = "n/a"
    else:
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    results.append(match)
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: c_sw = k_acc*t_mem + t_alu
c_sw = k_acc * t_mem + t_alu
check("Q1", c_sw, 65)

# Q2: f_sw = (k_acc*t_mem)/(k_acc*t_mem + t_alu)
f_sw = Fraction(k_acc * t_mem, k_acc * t_mem + t_alu)
check("Q2", float(f_sw), 64 / 65)

# Q3: c_re = t_dyn + t_re
c_re = t_dyn + t_re
check("Q3", c_re, 5)

# Q4: f_re = t_re/(t_dyn + t_re)
f_re = Fraction(t_re, t_dyn + t_re)
check("Q4", float(f_re), 0.2)

# Q5: T_sw = N_op * c_sw
T_sw = N_op * c_sw
check("Q5", T_sw, 6.5e7)

# Q6: T_re = N_op * c_re
T_re = N_op * c_re
check("Q6", T_re, 5.0e6)

# Q7: ratio = c_sw / c_re
ratio = Fraction(c_sw, c_re)
check("Q7", float(ratio), 13.0)

# Q8: t_mem* = (t_dyn + t_re - t_alu)/k_acc
t_mem_star = Fraction(t_dyn + t_re - t_alu, k_acc)
check("Q8", float(t_mem_star), 1)

n = len(results)
m = sum(1 for r in results if r == "yes")
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")

```

## Execution output
```
CLAIM Q1: computed=65 expected=65 match=yes
CLAIM Q2: computed=0.9846153846153847 expected=0.9846153846153847 match=yes
CLAIM Q3: computed=5 expected=5 match=yes
CLAIM Q4: computed=0.2 expected=0.2 match=yes
CLAIM Q5: computed=65000000 expected=65000000.0 match=yes
CLAIM Q6: computed=5000000 expected=5000000.0 match=yes
CLAIM Q7: computed=13.0 expected=13.0 match=yes
CLAIM Q8: computed=1.0 expected=1 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
