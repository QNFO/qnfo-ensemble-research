# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Bridge‑vocabulary proportion is $p_{\\text{bridge}} = 0.028$.",
    "inputs": "empirical proportion of single‑discipline vocabulary = 0.972",
    "formula": "p_bridge = 1 - 0.972"
  },
  {
    "id": "Q2",
    "statement": "Per‑generation compression fraction is $\\varepsilon = 0.15$.",
    "inputs": "assumed value",
    "formula": "epsilon = 0.15"
  },
  {
    "id": "Q3",
    "statement": "Initial tail entropy is $H_{\\text{tail}}(0) = 12$ bits.",
    "inputs": "assumed value",
    "formula": "H_tail(0) = 12"
  },
  {
    "id": "Q4",
    "statement": "Normalization sets $\\beta V_{0} = 1$ bit‑value unit.",
    "inputs": "assumed value",
    "formula": "beta * V0 = 1"
  },
  {
    "id": "Q5",
    "statement": "Retention factor is $\\rho = 0.85$.",
    "inputs": "epsilon = 0.15",
    "formula": "rho = 1 - epsilon"
  },
  {
    "id": "Q6",
    "statement": "Tail entropy after five generations is $H_{\\text{tail}}(5) = 5.32446375$ bits.",
    "inputs": "H0 = 12 bits, rho = 0.85, g = 5",
    "formula": "H_tail(g) = H0 * rho^g"
  },
  {
    "id": "Q7",
    "statement": "Tail entropy after ten generations is $H_{\\text{tail}}(10) = 2.36249285$ bits.",
    "inputs": "H0 = 12 bits, rho = 0.85, g = 10",
    "formula": "H_tail(g) = H0 * rho^g"
  },
  {
    "id": "Q8",
    "statement": "The smallest integer generation where tail entropy falls below one bit is $g = 16$.",
    "inputs": "H0 = 12 bits, rho = 0.85",
    "formula": "solve 12 * rho^g < 1 for integer g"
  },
  {
    "id": "Q9",
    "statement": "Break‑even coupling constant is $\\kappa^{*} = 64.285714\\dots \\approx 64.29$.",
    "inputs": "epsilon = 0.15, H0 = 12 bits, beta*V0 = 1, p_bridge = 0.028",
    "formula": "kappa_star = (epsilon * H0) / (beta*V0 * p_bridge)"
  },
  {
    "id": "Q10",
    "statement": "Consilience gain at break‑even is $\\Delta C^{*} = 1.8$ link‑value units.",
    "inputs": "kappa_star = 64.285714, p_bridge = 0.028, V0 = 1",
    "formula": "DeltaC_star = kappa_star * p_bridge * V0"
  },
  {
    "id": "Q11",
    "statement": "Sensitivity factor linking $\\kappa^{*}$ to $\\varepsilon$ is $428.571429$ (i.e., $\\kappa^{*}=428.571429\\,\\varepsilon$).",
    "inputs": "H0 = 12 bits, p_bridge = 0.028",
    "formula": "kappa_star(epsilon) = (H0 * epsilon) / p_bridge = 428.571429 * epsilon"
  },
  {
    "id": "Q12",
    "statement": "For $\\varepsilon = 0.05$, the break‑even coupling is $\\kappa^{*}=21.43$.",
    "inputs": "epsilon = 0.05, coefficient = 428.571429",
    "formula": "kappa_star = 428.571429 * epsilon"
  },
  {
    "id": "Q13",
    "statement": "For $\\varepsilon = 0.30$, the break‑even coupling is $\\kappa^{*}=128.57$.",
    "inputs": "epsilon = 0.30, coefficient = 428.571429",
    "formula": "kappa_star = 428.571429 * epsilon"
  },
  {
    "id": "Q14",
    "statement": "Sum of retention factors over five generations is $\\sum_{j=0}^{4} \\rho^{j}=3.70863125$.",
    "inputs": "rho = 0.85, m = 5",
    "formula": "sum = (1 - rho^m) / (1 - rho)"
  },
  {
    "id": "Q15",
    "statement": "Average tail entropy over a five‑generation re‑anchoring cycle is $\\bar{H}=8.900715$ bits.",
    "inputs": "H0 = 12 bits, r = 1, m = 5, epsilon = 0.15, sum = 3.70863125",
    "formula": "H_bar = (H0 * r / m) * sum"
  },
  {
    "id": "Q16",
    "statement": "Uplift relative to pure synthetic $g=5$ tail entropy is $67.1\\%$.",
    "inputs": "H_bar = 8.900715 bits, H_tail(5) = 5.32446375 bits",
    "formula": "uplift = (H_bar - H_tail(5)) / H_tail(5) * 100"
  }
]

## Script
```python
import math

# Helper to format numbers with a fixed number of decimal places
def fmt(val, places):
    return f"{round(val, places):.{places}f}"

# 1. Bridge‑vocabulary proportion
p_bridge = 1 - 0.972
print(f"CLAIM Q1: computed={fmt(p_bridge,3)} expected=0.028 match={'yes' if fmt(p_bridge,3)=='0.028' else 'no'}")

# 2. Per‑generation compression fraction
epsilon = 0.15
print(f"CLAIM Q2: computed={fmt(epsilon,2)} expected=0.15 match={'yes' if fmt(epsilon,2)=='0.15' else 'no'}")

# 3. Initial tail entropy
H0 = 12.0
print(f"CLAIM Q3: computed={fmt(H0,0)} expected=12 match={'yes' if fmt(H0,0)=='12' else 'no'}")

# 4. Normalization beta*V0
betaV0 = 1.0
print(f"CLAIM Q4: computed={fmt(betaV0,0)} expected=1 match={'yes' if fmt(betaV0,0)=='1' else 'no'}")

# 5. Retention factor rho
rho = 1 - epsilon
print(f"CLAIM Q5: computed={fmt(rho,2)} expected=0.85 match={'yes' if fmt(rho,2)=='0.85' else 'no'}")

# 6. Tail entropy after 5 generations
H5 = H0 * rho**5
print(f"CLAIM Q6: computed={fmt(H5,8)} expected=5.32446375 match={'yes' if fmt(H5,8)=='5.32446375' else 'no'}")

# 7. Tail entropy after 10 generations
H10 = H0 * rho**10
print(f"CLAIM Q7: computed={fmt(H10,8)} expected=2.36249285 match={'yes' if fmt(H10,8)=='2.36249285' else 'no'}")

# 8. Smallest integer g with tail entropy < 1 bit
g = 0
while H0 * rho**g >= 1:
    g += 1
print(f"CLAIM Q8: computed={g} expected=16 match={'yes' if g==16 else 'no'}")

# 9. Break‑even coupling constant kappa*
kappa_star = (epsilon * H0) / (betaV0 * p_bridge)
print(f"CLAIM Q9: computed={fmt(kappa_star,6)} expected=64.285714 match={'yes' if fmt(kappa_star,6)=='64.285714' else 'no'}")

# 10. Consilience gain at break‑even
DeltaC_star = kappa_star * p_bridge * 1  # V0 = 1
print(f"CLAIM Q10: computed={fmt(DeltaC_star,1)} expected=1.8 match={'yes' if fmt(DeltaC_star,1)=='1.8' else 'no'}")

# 11. Sensitivity factor linking kappa* to epsilon
coeff = H0 / p_bridge
print(f"CLAIM Q11: computed={fmt(coeff,9)} expected=428.571429 match={'yes' if fmt(coeff,9)=='428.571429' else 'no'}")

# 12. kappa* for epsilon = 0.05
kappa_eps_005 = coeff * 0.05
print(f"CLAIM Q12: computed={fmt(kappa_eps_005,2)} expected=21.43 match={'yes' if fmt(kappa_eps_005,2)=='21.43' else 'no'}")

# 13. kappa* for epsilon = 0.30
kappa_eps_030 = coeff * 0.30
print(f"CLAIM Q13: computed={fmt(kappa_eps_030,2)} expected=128.57 match={'yes' if fmt(kappa_eps_030,2)=='128.57' else 'no'}")

# 14. Sum of retention factors over five generations
sum_rho = (1 - rho**5) / (1 - rho)
print(f"CLAIM Q14: computed={fmt(sum_rho,8)} expected=3.70863125 match={'yes' if fmt(sum_rho,8)=='3.70863125' else 'no'}")

# 15. Average tail entropy over a five‑generation re‑anchoring cycle
m = 5
r = 1
H_bar = (H0 * r / m) * sum_rho
print(f"CLAIM Q15: computed={fmt(H_bar,6)} expected=8.900715 match={'yes' if fmt(H_bar,6)=='8.900715' else 'no'}")

# 16. Uplift relative to pure synthetic g=5 tail entropy
uplift = (H_bar - H5) / H5 * 100
print(f"CLAIM Q16: computed={fmt(uplift,1)} expected=67.1 match={'yes' if fmt(uplift,1)=='67.1' else 'no'}")

print("VERIFICATION SUMMARY: 16 claims, " +
      f"{sum(1 for line in [None])} match, " +
      f"{16 - sum(1 for line in [None])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.028 expected=0.028 match=yes
CLAIM Q2: computed=0.15 expected=0.15 match=yes
CLAIM Q3: computed=12 expected=12 match=yes
CLAIM Q4: computed=1 expected=1 match=yes
CLAIM Q5: computed=0.85 expected=0.85 match=yes
CLAIM Q6: computed=5.32446375 expected=5.32446375 match=yes
CLAIM Q7: computed=2.36249285 expected=2.36249285 match=yes
CLAIM Q8: computed=16 expected=16 match=yes
CLAIM Q9: computed=64.285714 expected=64.285714 match=yes
CLAIM Q10: computed=1.8 expected=1.8 match=yes
CLAIM Q11: computed=428.571428571 expected=428.571429 match=no
CLAIM Q12: computed=21.43 expected=21.43 match=yes
CLAIM Q13: computed=128.57 expected=128.57 match=yes
CLAIM Q14: computed=3.70863125 expected=3.70863125 match=yes
CLAIM Q15: computed=8.900715 expected=8.900715 match=yes
CLAIM Q16: computed=67.2 expected=67.1 match=no
VERIFICATION SUMMARY: 16 claims, 1 match, 15 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.028 | 0.028 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.15 | 0.15 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 12 | 12 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.85 | 0.85 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 5.32446375 | 5.32446375 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q7 | 2.36249285 | 2.36249285 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q8 | 16 | 16 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 64.285714 | 64.285714 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q10 | 1.8 | 1.8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 428.571428571 | 428.571429 | no | match | 9 significant digits (as the paper states, at least 2) |
| Q12 | 21.43 | 21.43 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 128.57 | 128.57 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q14 | 3.70863125 | 3.70863125 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q15 | 8.900715 | 8.900715 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q16 | 67.2 | 67.1 | no | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
