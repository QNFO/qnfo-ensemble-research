# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Ancilla bit‑flip rate Γ₍bf₎ = (2.22 ± 0.34) × 10³ s⁻¹",
    "inputs": "T₁^{bf} = 451 µs ± 70 µs",
    "formula": "Γ = 1 / T"
  },
  {
    "id": "Q2",
    "statement": "Fraction of logical decay removed = 0.371 ± 0.020 (37.1 %)",
    "inputs": "F = 1.59 ± 0.05",
    "formula": "removed = 1 - 1/F"
  },
  {
    "id": "Q3",
    "statement": "Residual fraction of logical decay = 0.629 ± 0.020 (62.9 %)",
    "inputs": "F = 1.59 ± 0.05",
    "formula": "residual = 1/F"
  },
  {
    "id": "Q4",
    "statement": "Per‑cycle ancilla bit‑flip probability p_{bf}^{flx} = 0.0219 ± 0.0034 (2.19 % ± 0.34 %)",
    "inputs": "Γ_{bf} = 2.2173 × 10³ s⁻¹, T_{cyc} = 10 µs",
    "formula": "p = 1 - exp(-Γ·T_{cyc})"
  },
  {
    "id": "Q5",
    "statement": "Transmon baseline per‑cycle error p_{bf}^{tm} ≈ 0.2835 (28.3 %)",
    "inputs": "T₁^{tm} = 30 µs, T_{cyc} = 10 µs",
    "formula": "p = 1 - exp(- (1/T₁^{tm})·T_{cyc})"
  },
  {
    "id": "Q6",
    "statement": "Ratio of per‑cycle errors (transmon / fluxonium) = 12.9",
    "inputs": "p_{bf}^{tm} = 0.2835, p_{bf}^{flx} = 0.0219",
    "formula": "ratio = p_{bf}^{tm} / p_{bf}^{flx}"
  },
  {
    "id": "Q7",
    "statement": "Ratio of bit‑flip rates (transmon / fluxonium) = 15.0",
    "inputs": "T₁^{bf} = 451 µs, T₁^{tm} = 30 µs",
    "formula": "ratio = T₁^{bf} / T₁^{tm}"
  },
  {
    "id": "Q8",
    "statement": "Steady‑state ancilla‑induced logical error rate Γ_{anc} = 221.7 s⁻¹",
    "inputs": "η = 0.1, Γ_{bf} = 2.2173 × 10³ s⁻¹",
    "formula": "Γ_{anc} = η·Γ_{bf}"
  },
  {
    "id": "Q9",
    "statement": "Ancilla‑limited corrected logical lifetime T_L^{(1)} ≈ 4.51 ms",
    "inputs": "Γ_{anc} = 221.7 s⁻¹",
    "formula": "T = 1 / Γ"
  },
  {
    "id": "Q10",
    "statement": "Photon‑budget advantage lower bound = 8.0 ×",
    "inputs": "lower photon‑budget ratio = 5, F = 1.59",
    "formula": "advantage = 5 × F"
  },
  {
    "id": "Q11",
    "statement": "Photon‑budget advantage upper bound = 64 ×",
    "inputs": "upper photon‑budget ratio = 40, F = 1.59",
    "formula": "advantage = 40 × F"
  }
]

## Script
```python
import math

# Inputs
T1_bf = 451e-6          # seconds
sigma_T1_bf = 70e-6     # seconds (unused for central values)
F = 1.59
T_cyc = 10e-6           # seconds
T1_tm = 30e-6           # seconds
eta = 0.1

# Computations
Gamma_bf = 1.0 / T1_bf
removed = 1.0 - 1.0 / F
residual = 1.0 / F
p_flx = 1.0 - math.exp(-Gamma_bf * T_cyc)
Gamma_tm = 1.0 / T1_tm
p_tm = 1.0 - math.exp(-Gamma_tm * T_cyc)
ratio_per_cycle = p_tm / p_flx
ratio_rates = T1_bf / T1_tm
Gamma_anc = eta * Gamma_bf
T_L1 = 1.0 / Gamma_anc
adv_lower = 5.0 * F
adv_upper = 40.0 * F

# Helper for rounding to match expected significant digits
def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Expected values (central) for comparison
expected = {
    "Q1": 2.22e3,
    "Q2": 0.371,
    "Q3": 0.629,
    "Q4": 0.0219,
    "Q5": 0.2835,
    "Q6": 12.9,
    "Q7": 15.0,
    "Q8": 221.7,
    "Q9": 4.51e-3,
    "Q10": 8.0,
    "Q11": 64.0,
}

# Rounding to match expected precision
computed = {
    "Q1": round_sig(Gamma_bf, 3),          # 3 sig figs
    "Q2": round(Gamma_bf, 0),  # placeholder not used
    "Q2": round(removed, 3),               # 3 decimal places
    "Q3": round(residual, 3),              # 3 decimal places
    "Q4": round(p_flx, 4),                 # 4 decimal places
    "Q5": round(p_tm, 4),                  # 4 decimal places
    "Q6": round(ratio_per_cycle, 1),       # 1 decimal place
    "Q7": round(ratio_rates, 1),           # 1 decimal place
    "Q8": round(Gamma_anc, 1),             # 1 decimal place
    "Q9": round(T_L1, 5),                  # 5 significant digits (0.004508)
    "Q10": round(adv_lower, 1),            # 1 decimal place
    "Q11": round(adv_upper, 0),            # integer
}

# Function to format numbers consistently
def fmt(x):
    if isinstance(x, float):
        # Use scientific notation if magnitude is large or small
        if abs(x) >= 1e4 or (0 < abs(x) < 1e-3):
            return f"{x:.3e}"
        else:
            return f"{x}"
    return str(x)

# Print results
for qid in sorted(expected.keys()):
    comp = computed[qid]
    exp = expected[qid]
    match = "yes" if round(comp, 10) == round(exp, 10) else "no"
    print(f"CLAIM {qid}: computed={fmt(comp)} expected={fmt(exp)} match={match}")

```

## Execution output
```
CLAIM Q1: computed=2220.0 expected=2220.0 match=yes
CLAIM Q10: computed=8.0 expected=8.0 match=yes
CLAIM Q11: computed=64.0 expected=64.0 match=yes
CLAIM Q2: computed=0.371 expected=0.371 match=yes
CLAIM Q3: computed=0.629 expected=0.629 match=yes
CLAIM Q4: computed=0.0219 expected=0.0219 match=yes
CLAIM Q5: computed=0.2835 expected=0.2835 match=yes
CLAIM Q6: computed=12.9 expected=12.9 match=yes
CLAIM Q7: computed=15.0 expected=15.0 match=yes
CLAIM Q8: computed=221.7 expected=221.7 match=yes
CLAIM Q9: computed=0.00451 expected=0.00451 match=yes

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2220.0 | 2220.0 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 8.0 | 8.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 64.0 | 64.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.371 | 0.371 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 0.629 | 0.629 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.0219 | 0.0219 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 0.2835 | 0.2835 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 12.9 | 12.9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 15.0 | 15.0 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 221.7 | 221.7 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 0.00451 | 0.00451 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 11.
