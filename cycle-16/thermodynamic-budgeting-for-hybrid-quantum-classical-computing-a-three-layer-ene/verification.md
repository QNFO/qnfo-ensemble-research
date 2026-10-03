# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Statistical resolution of 10,000 shots is ~1%",
    "inputs": "N_shots=10000",
    "formula": "1/sqrt(10000) = 0.01"
  },
  {
    "id": "Q2",
    "statement": "Active quantum time per cycle t_Q = 1.0 s",
    "inputs": "N_shots=10000, t_shot=1e-4 s",
    "formula": "t_Q = N_shots * t_shot = 10000 * 1e-4"
  },
  {
    "id": "Q3",
    "statement": "Cycle time t_cycle = 1.05 s",
    "inputs": "t_Q=1.0 s, t_opt=0.05 s",
    "formula": "t_cycle = t_Q + t_opt = 1.0 + 0.05"
  },
  {
    "id": "Q4",
    "statement": "Quantum term E_Q = 27,250 J per cycle",
    "inputs": "P_cryo=25000 W, t_cycle=1.05 s, P_q_op=1000 W, t_Q=1.0 s",
    "formula": "E_Q = P_cryo*t_cycle + P_q_op*t_Q = 25000*1.05 + 1000*1.0"
  },
  {
    "id": "Q5",
    "statement": "Interface term E_IF = 135 J per cycle",
    "inputs": "N_shots=10000, E_ctrl=0.001 J, E_ro=0.002 J, P_sync=100 W, t_cycle=1.05 s",
    "formula": "E_IF = N_shots*(E_ctrl+E_ro) + P_sync*t_cycle = 10000*0.003 + 100*1.05"
  },
  {
    "id": "Q6",
    "statement": "Classical term E_C = 335 J per cycle",
    "inputs": "P_host=400 W, t_opt=0.05 s, P_orch=300 W, t_cycle=1.05 s",
    "formula": "E_C = P_host*t_opt + P_orch*t_cycle = 400*0.05 + 300*1.05"
  },
  {
    "id": "Q7",
    "statement": "Per-cycle energy E_cycle = 27,720 J",
    "inputs": "E_Q=27250 J, E_IF=135 J, E_C=335 J",
    "formula": "E_cycle = E_Q + E_IF + E_C = 27250 + 135 + 335"
  },
  {
    "id": "Q8",
    "statement": "Quantum share of cycle energy = 98.304%",
    "inputs": "E_Q=27250 J, E_cycle=27720 J",
    "formula": "E_Q/E_cycle = 27250/27720"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: statistical resolution 1/sqrt(N_shots)
N_shots = 10000
q1 = 1 / math.sqrt(N_shots)
results.append(check("Q1", q1, 0.01))

# Q2: t_Q = N_shots * t_shot
t_shot = 1e-4
t_Q = N_shots * t_shot
results.append(check("Q2", t_Q, 1.0))

# Q3: t_cycle = t_Q + t_opt
t_opt = 0.05
t_cycle = t_Q + t_opt
results.append(check("Q3", t_cycle, 1.05))

# Q4: E_Q = P_cryo*t_cycle + P_q_op*t_Q
P_cryo = 25000.0
P_q_op = 1000.0
E_Q = P_cryo * t_cycle + P_q_op * t_Q
results.append(check("Q4", E_Q, 27250.0))

# Q5: E_IF = N_shots*(E_ctrl+E_ro) + P_sync*t_cycle
E_ctrl = 0.001
E_ro = 0.002
P_sync = 100.0
E_IF = N_shots * (E_ctrl + E_ro) + P_sync * t_cycle
results.append(check("Q5", E_IF, 135.0))

# Q6: E_C = P_host*t_opt + P_orch*t_cycle
P_host = 400.0
P_orch = 300.0
E_C = P_host * t_opt + P_orch * t_cycle
results.append(check("Q6", E_C, 335.0))

# Q7: E_cycle = E_Q + E_IF + E_C
E_cycle = E_Q + E_IF + E_C
results.append(check("Q7", E_cycle, 27720.0))

# Q8: quantum share = E_Q / E_cycle
share = E_Q / E_cycle
results.append(check("Q8", share, 27250.0 / 27720.0))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.01 expected=0.01 match=yes
CLAIM Q2: computed=1.0 expected=1.0 match=yes
CLAIM Q3: computed=1.05 expected=1.05 match=yes
CLAIM Q4: computed=27250.0 expected=27250.0 match=yes
CLAIM Q5: computed=135.0 expected=135.0 match=yes
CLAIM Q6: computed=335.0 expected=335.0 match=yes
CLAIM Q7: computed=27720.0 expected=27720.0 match=yes
CLAIM Q8: computed=0.983044733044733 expected=0.983044733044733 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
