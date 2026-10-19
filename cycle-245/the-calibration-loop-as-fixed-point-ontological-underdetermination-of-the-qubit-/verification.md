# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Per‑shot readout error probability is ε₍ro₎ = 9×10⁻⁵.",
    "inputs": "f₍ro₎ = 0.99991 (readout fidelity from Input 1)",
    "formula": "ε₍ro₎ = 1 - f₍ro₎"
  },
  {
    "id": "Q2",
    "statement": "Expected number of misidentifications in 10⁶ trials is μ = 90.",
    "inputs": "N₍trials₎ = 10⁶ (number of trials from Input 1), ε₍ro₎ = 9×10⁻⁵ (from Q1)",
    "formula": "μ = N₍trials₎ × ε₍ro₎"
  },
  {
    "id": "Q3",
    "statement": "One‑sigma uncertainty on the readout fidelity is σ_f ≈ 9.4864061×10⁻⁶.",
    "inputs": "f₍ro₎ = 0.99991 (Input 1), N₍trials₎ = 10⁶ (Input 1)",
    "formula": "σ_f = sqrt( f₍ro₎ × (1 - f₍ro₎) / N₍trials₎ )"
  },
  {
    "id": "Q4",
    "statement": "Adaptive‑technique error probability is ε₍ad₎ = 1×10⁻⁵.",
    "inputs": "f₍ad₎ = 0.99999 (readout fidelity from Input 2)",
    "formula": "ε₍ad₎ = 1 - f₍ad₎"
  },
  {
    "id": "Q5",
    "statement": "The adaptive error is a factor ≈0.11111 of the time‑resolved error.",
    "inputs": "ε₍ad₎ = 1×10⁻⁵ (from Q4), ε₍ro₎ = 9×10⁻⁵ (from Q1)",
    "formula": "ratio = ε₍ad₎ / ε₍ro₎"
  },
  {
    "id": "Q6",
    "statement": "Calibration error after k iterations is e_k = 0.1 × 0.5^k.",
    "inputs": "e₀ = 0.1 (initial error from Input 4), contraction factor |1 - g s| = 0.5 (Input 4)",
    "formula": "e_k = e₀ × (0.5)^k"
  },
  {
    "id": "Q7",
    "statement": "After 11 iterations the calibration error is e₁₁ = 4.8828125×10⁻⁵, which is below the readout error floor.",
    "inputs": "e₀ = 0.1, contraction factor = 0.5, k = 11",
    "formula": "e₁₁ = e₀ × (0.5)^{11}"
  },
  {
    "id": "Q8",
    "statement": "The minimum number of iterations required to reach the readout noise floor is k_min = 11.",
    "inputs": "e₀ = 0.1, contraction factor = 0.5, ε₍ro₎ = 9×10⁻⁵ (from Q1)",
    "formula": "Find smallest integer k such that e₀ × (0.5)^k ≤ ε₍ro₎"
  },
  {
    "id": "Q9",
    "statement": "Total‑variation distance between the two ontologies is D_TV = 0 when the measurement does not resolve the third level.",
    "inputs": "None (derived analytically from the model)",
    "formula": "D_TV = ½ Σ_m |p_A(m) - p_B(m)| = 0"
  },
  {
    "id": "Q10",
    "statement": "When a leakage‑resolving measurement is used, D_TV = |c|² = 0.01.",
    "inputs": "|c|² = 0.01 (leakage probability from Input 3)",
    "formula": "D_TV = |c|²"
  },
  {
    "id": "Q11",
    "statement": "A one‑sigma resolution of Δp = 0.01 requires at least N ≥ 2500 shots.",
    "inputs": "Δp = 0.01 (difference in outcome probabilities from Q10)",
    "formula": "N ≥ 1 / (4 × Δp²)"
  },
  {
    "id": "Q12",
    "statement": "A three‑sigma resolution of the same Δp requires at least N ≥ 22500 shots.",
    "inputs": "Δp = 0.01",
    "formula": "N ≥ 9 / (4 × Δp²)"
  },
  {
    "id": "Q13",
    "statement": "The noise‑floor margin is approximately 111.",
    "inputs": "|c|² = 0.01 (Input 3), ε₍ro₎ = 9×10⁻⁵ (Q1)",
    "formula": "margin = |c|² / ε₍ro₎"
  },
  {
    "id": "Q14",
    "statement": "In the weak‑drive regime the leakage probability satisfies |c|² ≤ (Ω / (2Δ))² = 2.5×10⁻³.",
    "inputs": "Ω/Δ = 0.1 (Input 5)",
    "formula": "bound = (Ω / (2Δ))²"
  },
  {
    "id": "Q15",
    "statement": "Tomographic shot noise for N_tom = 10⁴ shots per element is σ = 5.0×10⁻³.",
    "inputs": "N_tom = 10⁴ (Input 5), p = 0.5 (worst‑case binomial)",
    "formula": "σ = sqrt( p (1-p) / N_tom )"
  },
  {
    "id": "Q16",
    "statement": "Resolving a leakage probability of 2.5×10⁻³ at one sigma requires N ≥ 4.0×10⁴ shots per element.",
    "inputs": "target = 2.5×10⁻³ (bound from Q14)",
    "formula": "N ≥ 0.25 / target²"
  }
]

## Script
```python
import math

# Inputs from the paper
f_ro = 0.99991          # readout fidelity
N_trials = 10**6        # number of trials
f_ad = 0.99999          # adaptive measurement fidelity
e0 = 0.1                # initial calibration error
contraction = 0.5       # |1 - g*s|
c_sq = 0.01             # leakage probability |c|^2
Omega_over_Delta = 0.1  # weak-drive ratio
N_tom = 10**4           # tomographic shots per element
delta_p = 0.01          # probability difference to resolve

# Q1
eps_ro = 1 - f_ro
exp1 = "9×10⁻⁵"
match1 = "yes" if abs(eps_ro - 9e-5) < 1e-12 else "no"
print(f"CLAIM Q1: computed={eps_ro:.8g} expected={exp1} match={match1}")

# Q2
mu = N_trials * eps_ro
exp2 = "90"
match2 = "yes" if mu == 90 else "no"
print(f"CLAIM Q2: computed={mu:.8g} expected={exp2} match={match2}")

# Q3
sigma_f = math.sqrt(f_ro * (1 - f_ro) / N_trials)
exp3 = "9.4864061×10⁻⁶"
# round to 8 significant digits for comparison
sigma_f_rounded = round(sigma_f, 13)  # enough to capture 8 sig figs
match3 = "yes" if abs(sigma_f_rounded - 9.4864061e-6) < 1e-13 else "no"
print(f"CLAIM Q3: computed={sigma_f:.10g} expected={exp3} match={match3}")

# Q4
eps_ad = 1 - f_ad
exp4 = "1×10⁻⁵"
match4 = "yes" if abs(eps_ad - 1e-5) < 1e-12 else "no"
print(f"CLAIM Q4: computed={eps_ad:.8g} expected={exp4} match={match4}")

# Q5
ratio = eps_ad / eps_ro
exp5 = "0.11111"
# round ratio to 5 decimal places as in the paper
ratio_rounded = round(ratio, 5)
match5 = "yes" if abs(ratio_rounded - 0.11111) < 1e-10 else "no"
print(f"CLAIM Q5: computed={ratio_rounded:.5f} expected={exp5} match={match5}")

# Q6 (formula only, no numeric expected)
exp6 = "none"
print(f"CLAIM Q6: computed=0.1*0.5**k (formula) expected={exp6} match=none")

# Q7
e11 = e0 * (contraction ** 11)
exp7 = "4.8828125×10⁻⁵"
match7 = "yes" if abs(e11 - 4.8828125e-5) < 1e-12 else "no"
print(f"CLAIM Q7: computed={e11:.10g} expected={exp7} match={match7}")

# Q8
# find smallest integer k such that e0 * contraction**k <= eps_ro
k = 0
while e0 * (contraction ** k) > eps_ro:
    k += 1
exp8 = "11"
match8 = "yes" if k == 11 else "no"
print(f"CLAIM Q8: computed={k} expected={exp8} match={match8}")

# Q9
D_TV_subspace = 0.0
exp9 = "0"
match9 = "yes" if D_TV_subspace == 0 else "no"
print(f"CLAIM Q9: computed={D_TV_subspace:.1f} expected={exp9} match={match9}")

# Q10
D_TV_leak = c_sq
exp10 = "0.01"
match10 = "yes" if abs(D_TV_leak - 0.01) < 1e-12 else "no"
print(f"CLAIM Q10: computed={D_TV_leak:.2f} expected={exp10} match={match10}")

# Q11
N_min_1sigma = 1 / (4 * delta_p ** 2)
exp11 = "2500"
match11 = "yes" if abs(N_min_1sigma - 2500) < 1e-9 else "no"
print(f"CLAIM Q11: computed={int(N_min_1sigma)} expected={exp11} match={match11}")

# Q12
N_min_3sigma = 9 / (4 * delta_p ** 2)
exp12 = "22500"
match12 = "yes" if abs(N_min_3sigma - 22500) < 1e-6 else "no"
print(f"CLAIM Q12: computed={int(N_min_3sigma)} expected={exp12} match={match12}")

# Q13
margin = c_sq / eps_ro
exp13 = "111"
# round to nearest integer as paper gives approx 111
margin_rounded = round(margin)
match13 = "yes" if margin_rounded == 111 else "no"
print(f"CLAIM Q13: computed={margin:.6f} expected={exp13} match={match13}")

# Q14
bound = (Omega_over_Delta / 2) ** 2
exp14 = "2.5×10⁻³"
match14 = "yes" if abs(bound - 2.5e-3) < 1e-12 else "no"
print(f"CLAIM Q14: computed={bound:.8g} expected={exp14} match={match14}")

# Q15
sigma_tom = math.sqrt(0.5 * 0.5 / N_tom)
exp15 = "5.0×10⁻³"
match15 = "yes" if abs(sigma_tom - 5.0e-3) < 1e-12 else "no"
print(f"CLAIM Q15: computed={sigma_tom:.8g} expected={exp15} match={match15}")

# Q16
target = bound  # 2.5e-3
N_needed = 0.25 / (target ** 2)
exp16 = "4.0×10⁴"
match16 = "yes" if abs(N_needed - 40000) < 1e-6 else "no"
print(f"CLAIM Q16: computed={int(N_needed)} expected={exp16} match={match16}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum([match1,match2,match3,match4,match5,match7,match8,match9,match10,match11,match12,match13,match14,match15,match16].count('yes'))} match, {sum([match1,match2,match3,match4,match5,match7,match8,match9,match10,match11,match12,match13,match14,match15,match16].count('no'))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=9e-05 expected=9×10⁻⁵ match=yes
CLAIM Q2: computed=90 expected=90 match=no
CLAIM Q3: computed=9.486406063e-06 expected=9.4864061×10⁻⁶ match=yes
CLAIM Q4: computed=1e-05 expected=1×10⁻⁵ match=yes
CLAIM Q5: computed=0.11111 expected=0.11111 match=yes
CLAIM Q6: computed=0.1*0.5**k (formula) expected=none match=none
CLAIM Q7: computed=4.8828125e-05 expected=4.8828125×10⁻⁵ match=yes
CLAIM Q8: computed=11 expected=11 match=yes
CLAIM Q9: computed=0.0 expected=0 match=yes
CLAIM Q10: computed=0.01 expected=0.01 match=yes
CLAIM Q11: computed=2500 expected=2500 match=yes
CLAIM Q12: computed=22500 expected=22500 match=yes
CLAIM Q13: computed=111.111111 expected=111 match=yes
CLAIM Q14: computed=0.0025 expected=2.5×10⁻³ match=yes
CLAIM Q15: computed=0.005 expected=5.0×10⁻³ match=yes
CLAIM Q16: computed=39999 expected=4.0×10⁴ match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 118, in <module>
TypeError: 'int' object is not iterable

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 9e-05 | 9×10⁻⁵ | yes | match | script verdict (values not both numeric) |
| Q2 | 90 | 90 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 9.486406063e-06 | 9.4864061×10⁻⁶ | yes | match | script verdict (values not both numeric) |
| Q4 | 1e-05 | 1×10⁻⁵ | yes | match | script verdict (values not both numeric) |
| Q5 | 0.11111 | 0.11111 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 4.8828125e-05 | 4.8828125×10⁻⁵ | yes | match | script verdict (values not both numeric) |
| Q8 | 11 | 11 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 0.0 | 0 | yes | match | stated value is zero |
| Q10 | 0.01 | 0.01 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 2500 | 2500 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 22500 | 22500 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q13 | 111.111111 | 111 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 0.0025 | 2.5×10⁻³ | yes | match | script verdict (values not both numeric) |
| Q15 | 0.005 | 5.0×10⁻³ | yes | match | script verdict (values not both numeric) |
| Q16 | 39999 | 4.0×10⁴ | yes | match | script verdict (values not both numeric) |

Mismatches: 0 of 15.
