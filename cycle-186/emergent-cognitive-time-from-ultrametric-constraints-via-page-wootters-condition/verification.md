# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The elementary reference step is Δt = 12.5 ms.",
    "inputs": "f_θ = 8 Hz, M = 10",
    "formula": "Δt = (1 / f_θ) / M"
  },
  {
    "id": "Q2",
    "statement": "The theta period is T_θ = 125 ms.",
    "inputs": "f_θ = 8 Hz",
    "formula": "T_θ = 1 / f_θ"
  },
  {
    "id": "Q3",
    "statement": "The number of free pairwise overlaps is N_f = 2016.",
    "inputs": "N = 64",
    "formula": "N_f = N·(N‑1) / 2"
  },
  {
    "id": "Q4",
    "statement": "The cocycle condition contributes N_c = 43680 independent equations.",
    "inputs": "N = 64, L = 6",
    "formula": "N_c = (N^3 / 6)·(1 ‑ 4^(‑L))"
  },
  {
    "id": "Q5",
    "statement": "The overdetermination ratio is ρ = 65/3 ≈ 21.6667.",
    "inputs": "N_c = 43680, N_f = 2016",
    "formula": "ρ = N_c / N_f"
  },
  {
    "id": "Q6",
    "statement": "Using the alternative bookkeeping convention the cocycle count is N_c = 41664.",
    "inputs": "N = 64",
    "formula": "N_c = N·(N‑1)·(N‑2) / 6"
  },
  {
    "id": "Q7",
    "statement": "Page–Wootters conditioning adds at most N_PW = 184320 cross‑reference agreement conditions.",
    "inputs": "M = 10, N = 64",
    "formula": "N_PW = (M·(M‑1) / 2)·N^2"
  },
  {
    "id": "Q8",
    "statement": "Predicted reaction times follow RT(k) = 100 ms + k·12.5 ms; for k=8 this gives 200 ms and for k=12 it gives 250 ms.",
    "inputs": "t_0 = 100 ms, Δt = 12.5 ms, k = 8 or 12",
    "formula": "RT(k) = t_0 + k·Δt"
  },
  {
    "id": "Q9",
    "statement": "If the reference frequency is 6 Hz the step is Δt = 16.67 ms; if it is 10 Hz the step is Δt = 10 ms.",
    "inputs": "f_θ = 6 Hz or 10 Hz, M = 10",
    "formula": "Δt = (1 / f_θ) / M"
  },
  {
    "id": "Q10",
    "statement": "At depth‑2 resolution the number of possible conditional histories is 4^{10} = 1 048 576.",
    "inputs": "base = 4, exponent = 10",
    "formula": "4^10"
  },
  {
    "id": "Q11",
    "statement": "The number of possible total orderings of three reference states is 3! = 6.",
    "inputs": "N = 3",
    "formula": "N! = 3·2·1"
  },
  {
    "id": "Q12",
    "statement": "With the alternative cocycle count the overdetermination ratio is ρ = 62/3 ≈ 20.6667.",
    "inputs": "N_c = 41664, N_f = 2016",
    "formula": "ρ = N_c / N_f"
  }
]

## Script
```python
import math

def fmt(v, sig=6):
    # format number with given significant digits, removing trailing zeros
    s = f"{v:.{sig}g}"
    return s

# Claim Q1
f_theta = 8.0  # Hz
M = 10.0
delta_t_sec = (1.0 / f_theta) / M
delta_t_ms = delta_t_sec * 1000.0
print(f"CLAIM Q1: computed={fmt(delta_t_ms)} ms expected=12.5 ms match={'yes' if abs(delta_t_ms-12.5)<1e-9 else 'no'}")

# Claim Q2
T_theta_sec = 1.0 / f_theta
T_theta_ms = T_theta_sec * 1000.0
print(f"CLAIM Q2: computed={fmt(T_theta_ms)} ms expected=125 ms match={'yes' if abs(T_theta_ms-125.0)<1e-9 else 'no'}")

# Claim Q3
N = 64
N_f = N * (N - 1) // 2
print(f"CLAIM Q3: computed={N_f} expected=2016 match={'yes' if N_f==2016 else 'no'}")

# Claim Q4
L = 6
N_c = (N**3 / 6.0) * (1 - 4**(-L))
N_c_int = int(round(N_c))
print(f"CLAIM Q4: computed={N_c_int} expected=43680 match={'yes' if N_c_int==43680 else 'no'}")

# Claim Q5
rho = N_c_int / N_f
expected_rho = 65/3
print(f"CLAIM Q5: computed={fmt(rho)} expected=65/3 ≈ 21.6667 match={'yes' if abs(rho-expected_rho)<1e-9 else 'no'}")

# Claim Q6
N_c_alt = N * (N - 1) * (N - 2) // 6
print(f"CLAIM Q6: computed={N_c_alt} expected=41664 match={'yes' if N_c_alt==41664 else 'no'}")

# Claim Q7
N_PW = (M * (M - 1) / 2) * N**2
N_PW_int = int(N_PW)
print(f"CLAIM Q7: computed={N_PW_int} expected=184320 match={'yes' if N_PW_int==184320 else 'no'}")

# Claim Q8
t0 = 100.0  # ms
delta_t = 12.5  # ms
rt_k8 = t0 + 8 * delta_t
rt_k12 = t0 + 12 * delta_t
print(f"CLAIM Q8: computed={fmt(rt_k8)} ms and {fmt(rt_k12)} ms expected=200 ms and 250 ms match={'yes' if (abs(rt_k8-200)<1e-9 and abs(rt_k12-250)<1e-9) else 'no'}")

# Claim Q9
for f in (6.0, 10.0):
    dt = (1.0 / f) / M * 1000.0
    print(f"CLAIM Q9 (f={int(f)} Hz): computed={fmt(dt)} ms expected={'16.67 ms' if f==6 else '10 ms'} match={'yes' if (abs(dt-16.6666667)<1e-3 if f==6 else abs(dt-10.0)<1e-9) else 'no'}")

# Claim Q10
histories = 4**10
print(f"CLAIM Q10: computed={histories} expected=1048576 match={'yes' if histories==1048576 else 'no'}")

# Claim Q11
orderings = math.factorial(3)
print(f"CLAIM Q11: computed={orderings} expected=6 match={'yes' if orderings==6 else 'no'}")

# Claim Q12
rho_alt = N_c_alt / N_f
expected_rho_alt = 62/3
print(f"CLAIM Q12: computed={fmt(rho_alt)} expected=62/3 ≈ 20.6667 match={'yes' if abs(rho_alt-expected_rho_alt)<1e-9 else 'no'}")

```

## Execution output
```
CLAIM Q1: computed=12.5 ms expected=12.5 ms match=yes
CLAIM Q2: computed=125 ms expected=125 ms match=yes
CLAIM Q3: computed=2016 expected=2016 match=yes
CLAIM Q4: computed=43680 expected=43680 match=yes
CLAIM Q5: computed=21.6667 expected=65/3 ≈ 21.6667 match=yes
CLAIM Q6: computed=41664 expected=41664 match=yes
CLAIM Q7: computed=184320 expected=184320 match=yes
CLAIM Q8: computed=200 ms and 250 ms expected=200 ms and 250 ms match=yes
CLAIM Q9 (f=6 Hz): computed=16.6667 ms expected=16.67 ms match=yes
CLAIM Q9 (f=10 Hz): computed=10 ms expected=10 ms match=yes
CLAIM Q10: computed=1048576 expected=1048576 match=yes
CLAIM Q11: computed=6 expected=6 match=yes
CLAIM Q12: computed=20.6667 expected=62/3 ≈ 20.6667 match=yes

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q3 | 2016 | 2016 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 43680 | 43680 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | 21.6667 | 65/3 | - | undecided | undecided: values not both numeric and no script verdict |
| Q6 | 41664 | 41664 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 184320 | 184320 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q10 | 1048576 | 1048576 | yes | match | 7 significant digits (as printed, at least 3) |
| Q11 | 6 | 6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 20.6667 | 62/3 | - | undecided | undecided: values not both numeric and no script verdict |

Mismatches: 0 of 8 (2 undecided).
