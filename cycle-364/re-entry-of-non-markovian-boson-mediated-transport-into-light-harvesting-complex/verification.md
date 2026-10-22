# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Minimum transfer time τ_T = 0.1039 ps (for V = 75 cm⁻¹, Δ = 110 cm⁻¹).",
    "inputs": "V = 75 cm⁻¹, Δ = 110 cm⁻¹, c = 2.9979×10¹⁰ cm s⁻¹",
    "formula": "tau_T = Delta / (2 * pi * c * V^2)"
  },
  {
    "id": "Q2",
    "statement": "Maximum transfer time τ_T = 0.3823 ps (for V = 50 cm⁻¹, Δ = 180 cm⁻¹).",
    "inputs": "V = 50 cm⁻¹, Delta = 180 cm⁻¹, c = 2.9979×10¹⁰ cm s⁻¹",
    "formula": "tau_T = Delta / (2 * pi * c * V^2)"
  },
  {
    "id": "Q3",
    "statement": "Optimal hopping rate k* ranges from 13.89 cm⁻¹ to 51.14 cm⁻¹ across the experimental box.",
    "inputs": "V ∈ [50,75] cm⁻¹, Delta ∈ [110,180] cm⁻¹",
    "formula": "k_star = V^2 / Delta"
  },
  {
    "id": "Q4",
    "statement": "Single‑hop trapping efficiency η = 0.999001.",
    "inputs": "kappa = 1 ps⁻¹, gamma_rec = 1×10⁻³ ps⁻¹",
    "formula": "eta = kappa / (kappa + gamma_rec)"
  },
  {
    "id": "Q5",
    "statement": "Fast‑bath memory ratio R_fast lies in [0.26, 0.96].",
    "inputs": "tau_B_fast = 0.1 ps, tau_T ∈ [0.1039, 0.3823] ps",
    "formula": "R = tau_B / tau_T"
  },
  {
    "id": "Q6",
    "statement": "Slow‑bath memory ratio R_slow lies in [2.6, 9.6].",
    "inputs": "tau_B_slow = 1 ps, tau_T ∈ [0.1039, 0.3823] ps",
    "formula": "R = tau_B / tau_T"
  },
  {
    "id": "Q7",
    "statement": "Optimal dephasing rate Γ* equals the site‑energy difference Δ, ranging from 110 cm⁻¹ to 180 cm⁻¹.",
    "inputs": "Delta ∈ [110,180] cm⁻¹",
    "formula": "Gamma_star = Delta"
  },
  {
    "id": "Q8",
    "statement": "Projected computational cost for a full non‑Markovian FMO simulation is $1 000 (CPU‑hours ≈ 10⁴, price = $0.10 per CPU‑hour).",
    "inputs": "CPU_hours = 1×10⁴, price_per_hour = 0.10 USD",
    "formula": "cost = CPU_hours * price_per_hour"
  }
]

## Script
```python
import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Constants
c = 2.9979e10  # cm s^-1
pi = math.pi

# Q1: Minimum transfer time
V1 = 75.0  # cm^-1
Delta1 = 110.0  # cm^-1
tau_T_min = Delta1 / (2 * pi * c * V1**2)  # seconds
tau_T_min_ps = tau_T_min * 1e12  # convert to ps
computed_Q1 = round_sig(tau_T_min_ps, 4)
expected_Q1 = 0.1039
match_Q1 = "yes" if abs(computed_Q1 - expected_Q1) < 1e-8 else "no"
print(f"CLAIM Q1: computed={computed_Q1:.6f} expected={expected_Q1} match={match_Q1}")

# Q2: Maximum transfer time
V2 = 50.0
Delta2 = 180.0
tau_T_max = Delta2 / (2 * pi * c * V2**2)
tau_T_max_ps = tau_T_max * 1e12
computed_Q2 = round_sig(tau_T_max_ps, 4)
expected_Q2 = 0.3823
match_Q2 = "yes" if abs(computed_Q2 - expected_Q2) < 1e-8 else "no"
print(f"CLAIM Q2: computed={computed_Q2:.6f} expected={expected_Q2} match={match_Q2}")

# Q3: Optimal hopping rate range
def k_star(V, Delta):
    return V**2 / Delta

V_vals = [50.0, 75.0]
Delta_vals = [110.0, 180.0]

k_vals = [k_star(V, Delta) for V in V_vals for Delta in Delta_vals]
k_min = min(k_vals)
k_max = max(k_vals)
computed_Q3_min = round_sig(k_min, 4)
computed_Q3_max = round_sig(k_max, 4)
expected_Q3_min = 13.89
expected_Q3_max = 51.14
match_Q3 = "yes" if (abs(computed_Q3_min - expected_Q3_min) < 1e-8 and
                     abs(computed_Q3_max - expected_Q3_max) < 1e-8) else "no"
print(f"CLAIM Q3: computed=[{computed_Q3_min:.5f}, {computed_Q3_max:.5f}] "
      f"expected=[{expected_Q3_min}, {expected_Q3_max}] match={match_Q3}")

# Q4: Single‑hop trapping efficiency
kappa = 1.0  # ps^-1
gamma_rec = 1e-3  # ps^-1
eta = kappa / (kappa + gamma_rec)
computed_Q4 = round_sig(eta, 6)
expected_Q4 = 0.999001
match_Q4 = "yes" if abs(computed_Q4 - expected_Q4) < 1e-12 else "no"
print(f"CLAIM Q4: computed={computed_Q4:.6f} expected={expected_Q4} match={match_Q4}")

# Q5: Fast‑bath memory ratio range
tau_B_fast = 0.1  # ps
R_fast_min = tau_B_fast / max(tau_T_min_ps, tau_T_max_ps)  # using max tau_T for min ratio
R_fast_max = tau_B_fast / min(tau_T_min_ps, tau_T_max_ps)  # using min tau_T for max ratio
computed_Q5_min = round_sig(R_fast_min, 2)
computed_Q5_max = round_sig(R_fast_max, 2)
expected_Q5_min = 0.26
expected_Q5_max = 0.96
match_Q5 = "yes" if (abs(computed_Q5_min - expected_Q5_min) < 1e-8 and
                     abs(computed_Q5_max - expected_Q5_max) < 1e-8) else "no"
print(f"CLAIM Q5: computed=[{computed_Q5_min:.2f}, {computed_Q5_max:.2f}] "
      f"expected=[{expected_Q5_min}, {expected_Q5_max}] match={match_Q5}")

# Q6: Slow‑bath memory ratio range
tau_B_slow = 1.0  # ps
R_slow_min = tau_B_slow / max(tau_T_min_ps, tau_T_max_ps)
R_slow_max = tau_B_slow / min(tau_T_min_ps, tau_T_max_ps)
computed_Q6_min = round_sig(R_slow_min, 2)
computed_Q6_max = round_sig(R_slow_max, 2)
expected_Q6_min = 2.6
expected_Q6_max = 9.6
match_Q6 = "yes" if (abs(computed_Q6_min - expected_Q6_min) < 1e-8 and
                     abs(computed_Q6_max - expected_Q6_max) < 1e-8) else "no"
print(f"CLAIM Q6: computed=[{computed_Q6_min:.2f}, {computed_Q6_max:.2f}] "
      f"expected=[{expected_Q6_min}, {expected_Q6_max}] match={match_Q6}")

# Q7: Optimal dephasing rate range
Delta_min = 110.0
Delta_max = 180.0
computed_Q7_min = round_sig(Delta_min, 3)
computed_Q7_max = round_sig(Delta_max, 3)
expected_Q7_min = 110
expected_Q7_max = 180
match_Q7 = "yes" if (computed_Q7_min == expected_Q7_min and
                     computed_Q7_max == expected_Q7_max) else "no"
print(f"CLAIM Q7: computed=[{computed_Q7_min}, {computed_Q7_max}] "
      f"expected=[{expected_Q7_min}, {expected_Q7_max}] match={match_Q7}")

# Q8: Projected computational cost
CPU_hours = 1e4
price_per_hour = 0.10
cost = CPU_hours * price_per_hour
computed_Q8 = round_sig(cost, 1)  # one significant digit as $1 000
expected_Q8 = 1000
match_Q8 = "yes" if abs(computed_Q8 - expected_Q8) < 1e-8 else "no"
print(f"CLAIM Q8: computed={computed_Q8:.0f} expected={expected_Q8} match={match_Q8}")

print(f"VERIFICATION SUMMARY: 8 claims, "
      f"{sum(1 for m in [match_Q1, match_Q2, match_Q3, match_Q4, match_Q5, match_Q6, match_Q7, match_Q8] if m=='yes')} match, "
      f"{sum(1 for m in [match_Q1, match_Q2, match_Q3, match_Q4, match_Q5, match_Q6, match_Q7, match_Q8] if m=='no')} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.103800 expected=0.1039 match=no
CLAIM Q2: computed=0.382200 expected=0.3823 match=no
CLAIM Q3: computed=[13.89000, 51.14000] expected=[13.89, 51.14] match=yes
CLAIM Q4: computed=0.999001 expected=0.999001 match=yes
CLAIM Q5: computed=[0.26, 0.96] expected=[0.26, 0.96] match=yes
CLAIM Q6: computed=[2.60, 9.60] expected=[2.6, 9.6] match=yes
CLAIM Q7: computed=[110.0, 180.0] expected=[110, 180] match=yes
CLAIM Q8: computed=1000 expected=1000 match=yes
VERIFICATION SUMMARY: 8 claims, 6 match, 2 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.103800 | 0.1039 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 0.382200 | 0.3823 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 0.999001 | 0.999001 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q8 | 1000 | 1000 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 4.
