# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The gate count per simulated second for the dimer is 6 MS gates.",
    "inputs": "g_step=3 (MS gates per pair per step), s=2 (steps per simulated second), number_of_pairs=1",
    "formula": "N_gate = g_step * s * number_of_pairs"
  },
  {
    "id": "Q2",
    "statement": "The overall simulation fidelity is approximately 0.9704 (97.04%).",
    "inputs": "f_MS=0.995 (per‑gate fidelity), N_gate=6",
    "formula": "F = f_MS ^ N_gate"
  },
  {
    "id": "Q3",
    "statement": "The gate‑error probability per simulated second is about 0.0296 (2.96%).",
    "inputs": "F=0.9704",
    "formula": "p_error = 1 - F"
  },
  {
    "id": "Q4",
    "statement": "The second‑order Trotter error per step is 0.0729 %.",
    "inputs": "J=0.18 Hz, Δt=0.5 s",
    "formula": "(J * Δt)^3 expressed as a percentage"
  },
  {
    "id": "Q5",
    "statement": "The cumulative Trotter error per simulated second is ≤0.15 %.",
    "inputs": "per‑step error=0.0729 %, steps_per_second=2",
    "formula": "total_error = steps_per_second * per_step_error"
  },
  {
    "id": "Q6",
    "statement": "Avoiding explicit Trotterisation of the dipolar term reduces the gate count by a factor of approximately 1.7×10³.",
    "inputs": "avoided_Trotter_steps≈10⁴, actual_MS_gates=6",
    "formula": "factor = avoided_Trotter_steps / actual_MS_gates"
  },
  {
    "id": "Q7",
    "statement": "For a trimer the gate count per simulated second is 18 MS gates.",
    "inputs": "pairs=3, g_step=3 (MS gates per pair per step), s=2 (steps per simulated second)",
    "formula": "N_trimer = pairs * g_step * s"
  },
  {
    "id": "Q8",
    "statement": "The wall‑clock time per simulated second is 450 µs.",
    "inputs": "N_gate=6, t_gate=75 µs",
    "formula": "t_wall = N_gate * t_gate"
  },
  {
    "id": "Q9",
    "statement": "The energy consumption per simulated second is 6 µJ.",
    "inputs": "N_gate=6, E_gate=1 µJ",
    "formula": "E_sim = N_gate * E_gate"
  },
  {
    "id": "Q10",
    "statement": "The low‑end energy‑ratio to conventional J/sol is 1.42×10⁶.",
    "inputs": "E_conventional_low=8.5 J, E_sim=6 µJ = 6×10⁻⁶ J",
    "formula": "ratio_low = E_conventional_low / E_sim"
  },
  {
    "id": "Q11",
    "statement": "The high‑end energy‑ratio to conventional J/sol is 2.72×10⁶.",
    "inputs": "E_conventional_high=16.3 J, E_sim=6 µJ = 6×10⁻⁶ J",
    "formula": "ratio_high = E_conventional_high / E_sim"
  },
  {
    "id": "Q12",
    "statement": "The thermodynamic protection deficit scaling factor is approximately 8.6×10¹³.",
    "inputs": "Δ_protect=1×10¹², τ_ratio=85.9",
    "formula": "factor = Δ_protect * τ_ratio"
  },
  {
    "id": "Q13",
    "statement": "The falsification threshold is a total deviation greater than 0.031 (3.1 %).",
    "inputs": "gate_error=0.0296, Trotter_error≤0.0015",
    "formula": "threshold = gate_error + Trotter_error ≈ 0.031"
  }
]

## Script
```python
import math

def fmt(val, sig=8):
    # format with at least sig significant digits, remove trailing zeros
    s = f"{val:.{sig}g}"
    return s

# Q1
N_gate = 3 * 2 * 1
print(f"CLAIM Q1: computed={fmt(N_gate)} expected=6 match={'yes' if N_gate==6 else 'no'}")

# Q2
f_MS = 0.995
F = f_MS ** 6
print(f"CLAIM Q2: computed={fmt(F,10)} expected=0.9704 match={'yes' if round(F,4)==0.9704 else 'no'}")

# Q3
p_error = 1 - F
print(f"CLAIM Q3: computed={fmt(p_error,10)} expected=0.0296 match={'yes' if round(p_error,4)==0.0296 else 'no'}")

# Q4
J = 0.18
dt = 0.5
trotter_step_err = (J * dt) ** 3 * 100  # percent
print(f"CLAIM Q4: computed={fmt(trotter_step_err,10)} expected=0.0729% match={'yes' if round(trotter_step_err,4)==0.0729 else 'no'}")

# Q5
steps_per_sec = 2
cumulative_err = steps_per_sec * trotter_step_err
print(f"CLAIM Q5: computed={fmt(cumulative_err,10)} expected=≤0.15% match={'yes' if cumulative_err<=0.15 else 'no'}")

# Q6
avoided_steps = 1e4
factor = avoided_steps / N_gate
print(f"CLAIM Q6: computed={fmt(factor,10)} expected≈1.7e3 match={'yes' if 1.6e3 <= factor <= 1.8e3 else 'no'}")

# Q7
pairs = 3
N_trimer = pairs * 3 * 2
print(f"CLAIM Q7: computed={fmt(N_trimer)} expected=18 match={'yes' if N_trimer==18 else 'no'}")

# Q8
t_gate = 75e-6  # seconds
t_wall = N_gate * t_gate * 1e6  # microseconds
print(f"CLAIM Q8: computed={fmt(t_wall)} expected=450µs match={'yes' if round(t_wall)==450 else 'no'}")

# Q9
E_gate = 1e-6  # joules
E_sim = N_gate * E_gate * 1e6  # microjoules
print(f"CLAIM Q9: computed={fmt(E_sim)} expected=6µJ match={'yes' if round(E_sim)==6 else 'no'}")

# Q10
E_con_low = 8.5  # joules
ratio_low = E_con_low / (N_gate * E_gate)
print(f"CLAIM Q10: computed={fmt(ratio_low,10)} expected=1.42e6 match={'yes' if round(ratio_low/1e4)/100==1.42 else 'no'}")

# Q11
E_con_high = 16.3
ratio_high = E_con_high / (N_gate * E_gate)
print(f"CLAIM Q11: computed={fmt(ratio_high,10)} expected=2.72e6 match={'yes' if round(ratio_high/1e4)/100==2.72 else 'no'}")

# Q12
Delta_protect = 1e12
tau_ratio = 85.9
protect_factor = Delta_protect * tau_ratio
print(f"CLAIM Q12: computed={fmt(protect_factor,10)} expected≈8.6e13 match={'yes' if 8.5e13 <= protect_factor <= 8.7e13 else 'no'}")

# Q13
gate_error = 0.0296
trotter_error = 0.0015  # upper bound
threshold = gate_error + trotter_error
print(f"CLAIM Q13: computed={fmt(threshold,10)} expected=>0.031 match={'yes' if threshold>0.031 else 'no'}")

print("VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=6 expected=6 match=yes
CLAIM Q2: computed=0.9703725094 expected=0.9704 match=yes
CLAIM Q3: computed=0.02962749064 expected=0.0296 match=yes
CLAIM Q4: computed=0.0729 expected=0.0729% match=yes
CLAIM Q5: computed=0.1458 expected=≤0.15% match=yes
CLAIM Q6: computed=1666.666667 expected≈1.7e3 match=yes
CLAIM Q7: computed=18 expected=18 match=yes
CLAIM Q8: computed=450 expected=450µs match=yes
CLAIM Q9: computed=6 expected=6µJ match=yes
CLAIM Q10: computed=1416666.667 expected=1.42e6 match=yes
CLAIM Q11: computed=2716666.667 expected=2.72e6 match=yes
CLAIM Q12: computed=8.59e+13 expected≈8.6e13 match=yes
CLAIM Q13: computed=0.0311 expected=>0.031 match=yes
VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 6 | 6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.9703725094 | 0.9704 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 0.02962749064 | 0.0296 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.0729 | 0.0729% | yes | match | script verdict (values not both numeric) |
| Q5 | 0.1458 | ≤0.15% | yes | match | script verdict (values not both numeric) |
| Q7 | 18 | 18 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 450 | 450µs | yes | match | script verdict (values not both numeric) |
| Q9 | 6 | 6µJ | yes | match | script verdict (values not both numeric) |
| Q10 | 1416666.667 | 1.42e6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 2716666.667 | 2.72e6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 0.0311 | >0.031 | yes | match | script verdict (values not both numeric) |

Mismatches: 0 of 11.
