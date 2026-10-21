# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The electron Compton angular frequency is ω_C = 7.763×10^{20} s^{-1}.",
    "inputs": "m_e = 9.10938356×10^{-31} kg; c = 2.99792458×10^{8} m s^{-1}; ħ = 1.054571817×10^{-34} J s",
    "formula": "ω_C = (m_e * c^2) / ħ"
  },
  {
    "id": "Q2",
    "statement": "The Zitterbewegung period is T_Z = 8.1×10^{-21} s.",
    "inputs": "ω_C = 7.763×10^{20} s^{-1}",
    "formula": "T_Z = 2π / ω_C"
  },
  {
    "id": "Q3",
    "statement": "The fine‑structure‑scaled period is T_α = 1.77×10^{-19} s.",
    "inputs": "α = 7.2973525693×10^{-3}; α^{-1} = 137.035999084; ω_C = 7.763×10^{20} s^{-1}",
    "formula": "T_α = α^{-1} / ω_C"
  },
  {
    "id": "Q4",
    "statement": "Approximately k = 9.403 nesting levels separate the Zitterbewegung tick from a one‑second clock.",
    "inputs": "T_target = 1 s; T_Z = 8.1×10^{-21} s; λ = α^{-1} = 137.035999084",
    "formula": "k = ln(T_target / T_Z) / ln(λ)"
  },
  {
    "id": "Q5",
    "statement": "A level‑2 frozen time with coupling Δ = 10 yields t_2 = 8.1×10^{-23} s when interpreted as a decrease of frozen duration.",
    "inputs": "τ_0 = T_Z = 8.1×10^{-21} s; Δ = 10",
    "formula": "t_2 = τ_0 * Δ^{-2}"
  },
  {
    "id": "Q6",
    "statement": "A level‑2 frozen time with coupling Δ = 10 yields t_2 = 8.1×10^{-19} s when interpreted as an increase of frozen duration.",
    "inputs": "τ_0 = T_Z = 8.1×10^{-21} s; Δ = 10",
    "formula": "t_2 = τ_0 * Δ^{2}"
  },
  {
    "id": "Q7",
    "statement": "The conjectural quantum‑jump timescale is τ_jump = 1.77×10^{-19} s.",
    "inputs": "α^{-1} = 137.035999084; ω_C = 7.763×10^{20} s^{-1}",
    "formula": "τ_jump = α^{-1} / ω_C"
  },
  {
    "id": "Q8",
    "statement": "The projected signal‑to‑noise ratio is SNR ≈ 8.1×10^{3}.",
    "inputs": "t_2 (increase) = 8.1×10^{-19} s; σ_t = 1.0×10^{-22} s",
    "formula": "SNR = t_2 / σ_t"
  }
]

## Script
```python
import math

def round_sig(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Inputs
m_e = 9.10938356e-31          # kg
c = 2.99792458e8              # m/s
hbar = 1.054571817e-34        # J·s
alpha = 7.2973525693e-3
alpha_inv = 1/alpha           # ≈137.035999084
T_target = 1.0                # s
tau0 = 8.1e-21                # s
Delta = 10.0
sigma_t = 1.0e-22             # s

# Claim Q1
omega_C = (m_e * c**2) / hbar
computed_Q1 = omega_C
expected_Q1 = 7.763e20
match_Q1 = round_sig(computed_Q1, 4) == round_sig(expected_Q1, 4)

# Claim Q2
T_Z = 2 * math.pi / omega_C
computed_Q2 = T_Z
expected_Q2 = 8.1e-21
match_Q2 = round_sig(computed_Q2, 2) == round_sig(expected_Q2, 2)

# Claim Q3
T_alpha = alpha_inv / omega_C
computed_Q3 = T_alpha
expected_Q3 = 1.77e-19
match_Q3 = round_sig(computed_Q3, 3) == round_sig(expected_Q3, 3)

# Claim Q4
lam = alpha_inv
k = math.log(T_target / T_Z) / math.log(lam)
computed_Q4 = k
expected_Q4 = 9.403
match_Q4 = round_sig(computed_Q4, 4) == round_sig(expected_Q4, 4)

# Claim Q5
t2_decrease = tau0 * Delta**-2
computed_Q5 = t2_decrease
expected_Q5 = 8.1e-23
match_Q5 = round_sig(computed_Q5, 2) == round_sig(expected_Q5, 2)

# Claim Q6
t2_increase = tau0 * Delta**2
computed_Q6 = t2_increase
expected_Q6 = 8.1e-19
match_Q6 = round_sig(computed_Q6, 2) == round_sig(expected_Q6, 2)

# Claim Q7
tau_jump = alpha_inv / omega_C
computed_Q7 = tau_jump
expected_Q7 = 1.77e-19
match_Q7 = round_sig(computed_Q7, 3) == round_sig(expected_Q7, 3)

# Claim Q8
SNR = t2_increase / sigma_t
computed_Q8 = SNR
expected_Q8 = 8.1e3
match_Q8 = round_sig(computed_Q8, 2) == round_sig(expected_Q8, 2)

# Output
print(f"CLAIM Q1: computed={computed_Q1:.8e} expected={expected_Q1:.8e} match={'yes' if match_Q1 else 'no'}")
print(f"CLAIM Q2: computed={computed_Q2:.8e} expected={expected_Q2:.8e} match={'yes' if match_Q2 else 'no'}")
print(f"CLAIM Q3: computed={computed_Q3:.8e} expected={expected_Q3:.8e} match={'yes' if match_Q3 else 'no'}")
print(f"CLAIM Q4: computed={computed_Q4:.8e} expected={expected_Q4:.8e} match={'yes' if match_Q4 else 'no'}")
print(f"CLAIM Q5: computed={computed_Q5:.8e} expected={expected_Q5:.8e} match={'yes' if match_Q5 else 'no'}")
print(f"CLAIM Q6: computed={computed_Q6:.8e} expected={expected_Q6:.8e} match={'yes' if match_Q6 else 'no'}")
print(f"CLAIM Q7: computed={computed_Q7:.8e} expected={expected_Q7:.8e} match={'yes' if match_Q7 else 'no'}")
print(f"CLAIM Q8: computed={computed_Q8:.8e} expected={expected_Q8:.8e} match={'yes' if match_Q8 else 'no'}")
print(f"VERIFICATION SUMMARY: 8 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8])} match, {8 - sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=7.76344059e+20 expected=7.76300000e+20 match=yes
CLAIM Q2: computed=8.09329992e-21 expected=8.10000000e-21 match=yes
CLAIM Q3: computed=1.76514520e-19 expected=1.77000000e-19 match=yes
CLAIM Q4: computed=9.40263402e+00 expected=9.40300000e+00 match=yes
CLAIM Q5: computed=8.10000000e-23 expected=8.10000000e-23 match=yes
CLAIM Q6: computed=8.10000000e-19 expected=8.10000000e-19 match=yes
CLAIM Q7: computed=1.76514520e-19 expected=1.77000000e-19 match=yes
CLAIM Q8: computed=8.10000000e+03 expected=8.10000000e+03 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 7.76344059e+20 | 7.76300000e+20 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 8.09329992e-21 | 8.10000000e-21 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 1.76514520e-19 | 1.77000000e-19 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 9.40263402e+00 | 9.40300000e+00 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 8.10000000e-23 | 8.10000000e-23 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 8.10000000e-19 | 8.10000000e-19 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 1.76514520e-19 | 1.77000000e-19 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 8.10000000e+03 | 8.10000000e+03 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 8.
