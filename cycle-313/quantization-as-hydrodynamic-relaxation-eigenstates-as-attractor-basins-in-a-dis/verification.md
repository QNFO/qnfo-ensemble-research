# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The universal decay rate of linear perturbations equals γ/2, which for γ = 10⁹ s⁻¹ gives 5.0×10⁸ s⁻¹.",
    "inputs": "γ = 1.0e9 s⁻¹",
    "formula": "rate = γ / 2"
  },
  {
    "id": "Q2",
    "statement": "The per‑period phase‑space contraction factor is exp(‑4π γ/ω); with γ/ω = 0.01 this evaluates to 0.881911.",
    "inputs": "γ/ω = 0.01",
    "formula": "factor = exp(-4 * pi * (γ/ω))"
  },
  {
    "id": "Q3",
    "statement": "The diffusion time across L = 1 µm using the Einstein relation D = k_B T/(m γ) is t_D = 2.2×10⁻¹³ s.",
    "inputs": "k_B = 1.381e-23 J·K⁻¹, T = 300 K, m = 9.109e-31 kg, γ = 1.0e9 s⁻¹, L = 1.0e-6 m",
    "formula": "D = k_B * T / (m * γ); t_D = L^2 / D"
  },
  {
    "id": "Q4",
    "statement": "The energy‑relaxation timescale τ_E = 1/γ equals 1.0×10⁻⁹ s for γ = 10⁹ s⁻¹.",
    "inputs": "γ = 1.0e9 s⁻¹",
    "formula": "τ_E = 1 / γ"
  },
  {
    "id": "Q5",
    "statement": "The level‑to‑level relaxation time from n=1 to n=0 is t_{1→0}=0.549306/γ, which for γ = 10⁹ s⁻¹ gives 5.49306×10⁻¹⁰ s.",
    "inputs": "γ = 1.0e9 s⁻¹",
    "formula": "t_{1→0} = 0.549306 / γ"
  },
  {
    "id": "Q6",
    "statement": "The relaxation time from n=2 to n=1 is t_{2→1}=0.255413/γ, which for γ = 10⁹ s⁻¹ gives 2.55413×10⁻¹⁰ s.",
    "inputs": "γ = 1.0e9 s⁻¹",
    "formula": "t_{2→1} = 0.255413 / γ"
  },
  {
    "id": "Q7",
    "statement": "The amplitude decay time from the linearized analysis is τ_lin = 2/γ = 2.0×10⁻⁹ s for γ = 10⁹ s⁻¹.",
    "inputs": "γ = 1.0e9 s⁻¹",
    "formula": "τ_lin = 2 / γ"
  },
  {
    "id": "Q8",
    "statement": "The overdamped crossover frequency ħ k²/m evaluates to 1.16×10¹⁰ s⁻¹ for k = 10⁷ m⁻¹, m = 9.109×10⁻³¹ kg.",
    "inputs": "ħ = 1.055e-34 J·s, k = 1.0e7 m⁻¹, m = 9.109e-31 kg",
    "formula": "ω_c = ħ * k^2 / m"
  },
  {
    "id": "Q9",
    "statement": "The underdamped oscillation frequency ω_k ≈ ħ k²/(2m) equals 5.8×10⁹ rad·s⁻¹ for the same k and m.",
    "inputs": "ħ = 1.055e-34 J·s, k = 1.0e7 m⁻¹, m = 9.109e-31 kg",
    "formula": "ω_k = ħ * k^2 / (2 * m)"
  },
  {
    "id": "Q10",
    "statement": "The arithmetic mean of the hardware fidelities is 0.993866 (≈99.39 %).",
    "inputs": "f1 = 0.9990, f2 = 0.9956, f_r = 0.9870",
    "formula": "mean = (f1 + f2 + f_r) / 3"
  },
  {
    "id": "Q11",
    "statement": "The qubit‑weighted composite fidelity is 0.98727 (≈98.73 %).",
    "inputs": "f1 = 0.9990, f2 = 0.9956, f_r = 0.9870, weights: 1, 2, 105",
    "formula": "F_eff = (1*f1 + 2*f2 + 105*f_r) / (1+2+105)"
  },
  {
    "id": "Q12",
    "statement": "Assuming an engineered damping γ = 10⁶ s⁻¹, the first‑level relaxation time is t_{1→0}=0.549306×10⁻⁶ s = 5.49×10⁻⁷ s (≈0.55 µs).",
    "inputs": "γ = 1.0e6 s⁻¹",
    "formula": "t_{1→0} = 0.549306 / γ"
  },
  {
    "id": "Q13",
    "statement": "The radial contraction per period is exp(‑γ T) = 0.939101 for γ/ω = 0.01.",
    "inputs": "γ/ω = 0.01",
    "formula": "radial_factor = exp(-γ * (2π/ω)) = exp(-2π * (γ/ω))"
  },
  {
    "id": "Q14",
    "statement": "After ten periods the phase‑space area contracts by a factor exp(‑2π·10·0.01) = 0.533488.",
    "inputs": "γ/ω = 0.01, number of periods = 10",
    "formula": "factor = exp(-2π * periods * (γ/ω))"
  },
  {
    "id": "Q15",
    "statement": "The ratio of the energy‑relaxation timescale to the diffusion time is τ_E / t_D ≈ 4.5×10³.",
    "inputs": "τ_E = 1.0e-9 s, t_D = 2.2e-13 s",
    "formula": "ratio = τ_E / t_D"
  }
]

## Script
```python
import math

def fmt(val, sig=6):
    # format with given significant digits, removing trailing zeros
    return f"{val:.{sig}g}"

claims = [
    ("Q1", "5.0e8", fmt(1.0e9/2)),
    ("Q2", "0.881911", fmt(math.exp(-4*math.pi*0.01), 6)),
    ("Q3", "2.2e-13", fmt((1e-12) / (1.381e-23*300/(9.109e-31*1e9)), 6)),
    ("Q4", "1.0e-9", fmt(1/1e9, 6)),
    ("Q5", "5.49306e-10", fmt(0.549306/1e9, 6)),
    ("Q6", "2.55413e-10", fmt(0.255413/1e9, 6)),
    ("Q7", "2.0e-9", fmt(2/1e9, 6)),
    ("Q8", "1.16e10", fmt(1.055e-34*1e14/9.109e-31, 6)),
    ("Q9", "5.8e9", fmt(1.055e-34*1e14/(2*9.109e-31), 6)),
    ("Q10", "0.993866", fmt((0.9990+0.9956+0.9870)/3, 6)),
    ("Q11", "0.98727", fmt((0.9990+2*0.9956+105*0.9870)/(1+2+105), 6)),
    ("Q12", "5.49e-7", fmt(0.549306/1e6, 6)),
    ("Q13", "0.939101", fmt(math.exp(-2*math.pi*0.01), 6)),
    ("Q14", "0.533488", fmt(math.exp(-2*math.pi*10*0.01), 6)),
    ("Q15", "4.5e3", fmt(1e-9/2.2e-13, 2)),
]

for cid, expected, computed in claims:
    match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,e,c in claims if c==e)} match, {sum(1 for _,e,c in claims if c!=e)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=5e+08 expected=5.0e8 match=no
CLAIM Q2: computed=0.881911 expected=0.881911 match=yes
CLAIM Q3: computed=2.19865e-13 expected=2.2e-13 match=no
CLAIM Q4: computed=1e-09 expected=1.0e-9 match=no
CLAIM Q5: computed=5.49306e-10 expected=5.49306e-10 match=yes
CLAIM Q6: computed=2.55413e-10 expected=2.55413e-10 match=yes
CLAIM Q7: computed=2e-09 expected=2.0e-9 match=no
CLAIM Q8: computed=1.1582e+10 expected=1.16e10 match=no
CLAIM Q9: computed=5.79098e+09 expected=5.8e9 match=no
CLAIM Q10: computed=0.993867 expected=0.993866 match=no
CLAIM Q11: computed=0.98727 expected=0.98727 match=yes
CLAIM Q12: computed=5.49306e-07 expected=5.49e-7 match=no
CLAIM Q13: computed=0.939101 expected=0.939101 match=yes
CLAIM Q14: computed=0.533488 expected=0.533488 match=yes
CLAIM Q15: computed=4.5e+03 expected=4.5e3 match=no
VERIFICATION SUMMARY: 15 claims, 6 match, 9 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 5e+08 | 5.0e8 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.881911 | 0.881911 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q3 | 2.19865e-13 | 2.2e-13 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 1e-09 | 1.0e-9 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 5.49306e-10 | 5.49306e-10 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q6 | 2.55413e-10 | 2.55413e-10 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q7 | 2e-09 | 2.0e-9 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 1.1582e+10 | 1.16e10 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 5.79098e+09 | 5.8e9 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 0.993867 | 0.993866 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q11 | 0.98727 | 0.98727 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q12 | 5.49306e-07 | 5.49e-7 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 0.939101 | 0.939101 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q14 | 0.533488 | 0.533488 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q15 | 4.5e+03 | 4.5e3 | no | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 15.
