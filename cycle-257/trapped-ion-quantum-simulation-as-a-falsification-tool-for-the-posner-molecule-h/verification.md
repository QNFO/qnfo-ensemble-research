# Verification report

## Extracted claims
[
  {
    "id": "Q2",
    "statement": "The total number of MS gates required per simulated second is six.",
    "inputs": "g_step = 3 (MS gates per Trotter step), s = 2 (steps per simulated second)",
    "formula": "g_total = g_step * s"
  },
  {
    "id": "Q3",
    "statement": "The overall simulation fidelity after six MS gates is approximately 0.9703 (97.0%).",
    "inputs": "f_MS = 0.995 (per‑gate fidelity), N = 6 (number of gates)",
    "formula": "F = f_MS ^ N"
  },
  {
    "id": "Q4",
    "statement": "The second‑order Trotter error per Trotter step is about 7.3×10⁻⁴ (0.07%).",
    "inputs": "J = 0.18 Hz (scalar coupling), Δt = 0.5 s (step duration)",
    "formula": "(J * Δt) ^ 3"
  },
  {
    "id": "Q5",
    "statement": "The cumulative Trotter error per simulated second is below 0.15 %.",
    "inputs": "error_per_step = 7.3×10⁻⁴ (from Q4), steps_per_second = 2",
    "formula": "cumulative_error = 2 * error_per_step"
  },
  {
    "id": "Q6",
    "statement": "A three‑spin trimer requires nine MS gates per simulated second.",
    "inputs": "pairs = 3 (number of spin pairs in a trimer), gates_per_pair = 3",
    "formula": "g_trimer = pairs * gates_per_pair"
  },
  {
    "id": "Q7",
    "statement": "The wall‑clock time needed to simulate one second of Posner dynamics is 450 µs.",
    "inputs": "N_gate = 6 (MS gates per simulated second), t_gate = 75 µs (duration of one MS gate)",
    "formula": "t_wall = N_gate * t_gate"
  },
  {
    "id": "Q8",
    "statement": "The projected energy consumption per simulated second is 6 µJ.",
    "inputs": "N_gate = 6, E_gate = 1 µJ (energy per MS gate)",
    "formula": "E_sim = N_gate * E_gate"
  },
  {
    "id": "Q9",
    "statement": "Compared with the low‑end trapped‑ion joule‑per‑solution figure (8.5 J), the simulation uses about 1.42×10⁶ times less energy.",
    "inputs": "E_sol_low = 8.5 J, E_sim = 6 µJ",
    "formula": "R_low = E_sol_low / E_sim"
  },
  {
    "id": "Q10",
    "statement": "Compared with the high‑end trapped‑ion joule‑per‑solution figure (16.3 J), the simulation uses about 2.72×10⁶ times less energy.",
    "inputs": "E_sol_high = 16.3 J, E_sim = 6 µJ",
    "formula": "R_high = E_sol_high / E_sim"
  },
  {
    "id": "Q11",
    "statement": "The projected energetic requirement for a biologically realistic coherence time is roughly 8.6×10¹³ times the energy of the Willow superconducting processor.",
    "inputs": "Δ_protect = 1×10¹² (protection deficit), τ_bio = 25 ms, τ_Willow = 291 µs",
    "formula": "scale_factor = Δ_protect * (τ_bio / τ_Willow)"
  },
  {
    "id": "Q12",
    "statement": "The fidelity loss per simulated second due to gate errors is about 0.0297 (2.97%).",
    "inputs": "f_MS = 0.995, N = 6",
    "formula": "p_error = 1 - f_MS ^ N"
  },
  {
    "id": "Q13",
    "statement": "The effective error rate per wall‑clock second is approximately 66.0 errors per second.",
    "inputs": "p_error = 0.029701 (from Q12), t_wall = 450 µs",
    "formula": "error_rate = p_error / t_wall * 1 s"
  },
  {
    "id": "Q14",
    "statement": "The midpoint duration of a typical MS gate is 75 µs.",
    "inputs": "t_low = 50 µs, t_high = 100 µs",
    "formula": "t_gate = (t_low + t_high) / 2"
  }
]

## Script
```python
import math

def fmt(val, fmt_type):
    """Format val according to the expected representation."""
    if fmt_type == "int":
        return f"{int(round(val))}"
    if fmt_type == "int_no_round":
        return f"{int(val)}"
    if fmt_type == "float_4dp":
        return f"{val:.4f}"
    if fmt_type == "float_5dp":
        return f"{val:.5f}"
    if fmt_type == "float_1dp":
        return f"{val:.1f}"
    if fmt_type == "float_2dp":
        return f"{val:.2f}"
    if fmt_type == "sci_2sd":
        return f"{val:.2e}"
    if fmt_type == "sci_3sd":
        return f"{val:.3e}"
    if fmt_type == "sci_1sd":
        return f"{val:.1e}"
    raise ValueError

# Inputs
g_step = 3          # MS gates per Trotter step
s = 2               # steps per simulated second
f_MS = 0.995        # per-gate fidelity
N = 6               # number of gates
J = 0.18            # Hz
dt = 0.5            # s
pairs = 3
gates_per_pair = 3
t_low = 50e-6       # s
t_high = 100e-6     # s
t_gate = (t_low + t_high) / 2   # s
N_gate = 6
E_gate = 1e-6       # J (1 µJ)
E_sol_low = 8.5     # J
E_sol_high = 16.3   # J
Delta_protect = 1e12
tau_bio = 25e-3     # s
tau_willow = 291e-6 # s

# Computations
g_total = g_step * s
F = f_MS ** N
trot_err_step = (J * dt) ** 3
cumulative_error = 2 * trot_err_step
g_trimer = pairs * gates_per_pair
t_wall = N_gate * t_gate
E_sim = N_gate * E_gate
R_low = E_sol_low / E_sim
R_high = E_sol_high / E_sim
scale_factor = Delta_protect * (tau_bio / tau_willow)
p_error = 1 - f_MS ** N
error_rate = p_error / t_wall  # per second

# Expected representations
expected = {
    "Q2": ("6", fmt(g_total, "int")),
    "Q3": ("0.9703", fmt(F, "float_4dp")),
    "Q4": ("7.3e-4", fmt(trot_err_step, "sci_1sd")),
    "Q5": ("0.00146", fmt(cumulative_error, "float_5dp")),
    "Q6": ("9", fmt(g_trimer, "int")),
    "Q7": ("450", fmt(t_wall * 1e6, "int")),  # µs
    "Q8": ("6", fmt(E_sim * 1e6, "int")),    # µJ
    "Q9": ("1.42e6", fmt(R_low, "sci_3sd")),
    "Q10": ("2.72e6", fmt(R_high, "sci_3sd")),
    "Q11": ("8.6e13", fmt(scale_factor, "sci_2sd")),
    "Q12": ("0.0297", fmt(p_error, "float_4dp")),
    "Q13": ("66.0", fmt(error_rate, "float_1dp")),
    "Q14": ("75", fmt(t_gate * 1e6, "int")),  # µs
}

# Reporting
for qid, (exp_str, comp_str) in expected.items():
    match = "yes" if exp_str == comp_str else "no"
    print(f"CLAIM {qid}: computed={comp_str} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for _,(_,c) in expected.items() if c==expected[_][0])} match, {len(expected)-sum(1 for _,(_,c) in expected.items() if c==expected[_][0])} mismatch")

```

## Execution output
```
CLAIM Q2: computed=6 expected=6 match=yes
CLAIM Q3: computed=0.9704 expected=0.9703 match=no
CLAIM Q4: computed=7.3e-04 expected=7.3e-4 match=no
CLAIM Q5: computed=0.00146 expected=0.00146 match=yes
CLAIM Q6: computed=9 expected=9 match=yes
CLAIM Q7: computed=450 expected=450 match=yes
CLAIM Q8: computed=6 expected=6 match=yes
CLAIM Q9: computed=1.417e+06 expected=1.42e6 match=no
CLAIM Q10: computed=2.717e+06 expected=2.72e6 match=no
CLAIM Q11: computed=8.59e+13 expected=8.6e13 match=no
CLAIM Q12: computed=0.0296 expected=0.0297 match=no
CLAIM Q13: computed=65.8 expected=66.0 match=no
CLAIM Q14: computed=75 expected=75 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 81, in <module>
  File "<string>", line 81, in <genexpr>
KeyError: '6'

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q2 | 6 | 6 | yes | match | 3 significant digits (as printed, at least 3) |
| Q3 | 0.9704 | 0.9703 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 7.3e-04 | 7.3e-4 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.00146 | 0.00146 | yes | match | 3 significant digits (as printed, at least 3) |
| Q6 | 9 | 9 | yes | match | 3 significant digits (as printed, at least 3) |
| Q7 | 450 | 450 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 6 | 6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 1.417e+06 | 1.42e6 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 2.717e+06 | 2.72e6 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 8.59e+13 | 8.6e13 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 0.0296 | 0.0297 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 65.8 | 66.0 | no | MISMATCH | 3 significant digits (as the paper states, at least 2) |
| Q14 | 75 | 75 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 1 of 13.


## Auto-corrections

The worker corrected these independently-verified values in place of the paper's stated values (deterministic, no model edit):

| claim | stated | corrected |
|---|---|---|
| Q13 | 66.0 | 65.8 |
