# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "With initial state x₀=0 and input u₀=0.1 the pure integrator yields ΔV = 0.005 and supply u₀y₀ = 0.005, confirming exact passivity.",
    "inputs": "x₀=0, u₀=0.1",
    "formula": "ΔV = ½[(x₀+u₀)² - x₀²] = ½*u₀²; y₀ = x₀ + ½u₀; supply = u₀*y₀"
  },
  {
    "id": "Q2",
    "statement": "For the leaky integrator with α=0.1, x₀=2, u₀=0 the storage change is ΔV = -0.38, which equals –δ x₀² with δ=0.095.",
    "inputs": "α=0.1, x₀=2, u₀=0",
    "formula": "δ = α - α²/2; x₁ = (1-α)x₀ + u₀; V(x)=½x²; ΔV = V(x₁)-V(x₀); –δ x₀² = -δ*x₀²"
  },
  {
    "id": "Q3",
    "statement": "For the leaky integrator with α=0.1, x₀=2, u₀=0.5 the storage change is ΔV = 0.645, the supply is u₀y₀ = 1.025, and ΔV – u₀y₀ = –0.38 = –δ x₀².",
    "inputs": "α=0.1, x₀=2, u₀=0.5",
    "formula": "δ = α - α²/2; x₁ = (1-α)x₀ + u₀; V(x)=½x²; ΔV = V(x₁)-V(x₀); y₀ = (1-α)x₀ + ½u₀; supply = u₀*y₀; ΔV - supply = -δ*x₀²"
  },
  {
    "id": "Q4",
    "statement": "Using the naive output yₖ = xₖ, for α=0.1, xₖ=1, uₖ=–1 the passivity expression equals +0.505, showing violation.",
    "inputs": "α=0.1, x=1, u=–1",
    "formula": "expression = –δ x² – α x u + ½u², with δ = α - α²/2"
  },
  {
    "id": "Q5",
    "statement": "Uniform output quantization with resolution q=0.1, input bound |uₖ|≤1, and horizon N=100 yields a worst‑case cumulative degradation Δ_quant = 5.0 energy units.",
    "inputs": "q=0.1, U_max=1, N=100",
    "formula": "Δ_quant = N * U_max * q / 2"
  },
  {
    "id": "Q6",
    "statement": "The degradation budget is tolerable only when the constant state magnitude satisfies x_* ≥ 0.726.",
    "inputs": "δ=0.095, N=100, Δ_quant=5.0",
    "formula": "x_* = sqrt(Δ_quant / (δ * N))"
  },
  {
    "id": "Q7",
    "statement": "With crossover frequency ω_c=1.0 rad s⁻¹ and transport delay T_d=0.5 s, the phase lag is φ_d = 0.5 rad ≈ 28.65°.",
    "inputs": "ω_c=1.0, T_d=0.5",
    "formula": "φ_d = ω_c * T_d"
  },
  {
    "id": "Q8",
    "statement": "The combined dissipative margin proxy is M = k_S(ε_S+ε_W) = 0.6.",
    "inputs": "k_S=2.0, ε_S=0.1, ε_W=0.2",
    "formula": "M = k_S * (ε_S + ε_W)"
  },
  {
    "id": "Q9",
    "statement": "The normalized delay loss is ℓ_d = φ_d/(2π) ≈ 0.0796.",
    "inputs": "φ_d=0.5",
    "formula": "ℓ_d = φ_d / (2π)"
  },
  {
    "id": "Q10",
    "statement": "The normalized margin is M_n = M/(1+M) = 0.375.",
    "inputs": "M=0.6",
    "formula": "M_n = M / (1 + M)"
  },
  {
    "id": "Q11",
    "statement": "The safety ratio is ρ = M_n / ℓ_d ≈ 4.71.",
    "inputs": "M_n=0.375, ℓ_d≈0.0796",
    "formula": "ρ = M_n / ℓ_d"
  },
  {
    "id": "Q12",
    "statement": "The quantization energy cost per packet is E_q ≤ 0.025 J.",
    "inputs": "Δ=0.05, u_max=1.0",
    "formula": "E_q = (Δ/2) * u_max"
  },
  {
    "id": "Q13",
    "statement": "Relative overhead of quantization is 2.5 % (E_q/E_0 = 0.025).",
    "inputs": "E_q=0.025, E_0 = u_max² = 1.0",
    "formula": "overhead = E_q / E_0"
  },
  {
    "id": "Q14",
    "statement": "The attractor radius due to quantization is r_q = 0.05 (normalized Worker units).",
    "inputs": "Δ=0.05, λ_W=0.5",
    "formula": "r_q = (Δ/2) / λ_W"
  },
  {
    "id": "Q15",
    "statement": "The robustness budget allows margin erosion up to 16.7 % of the combined loop margin (δ/M ≈ 0.1667).",
    "inputs": "δ=0.1, M=0.6",
    "formula": "fraction = δ / M"
  },
  {
    "id": "Q16",
    "statement": "The dissipation rate for the leaky integrator is δ = α – α²/2; for α∈[0,1] this yields δ∈[0,0.5].",
    "inputs": "α∈[0,1]",
    "formula": "δ = α - α²/2"
  }
]

## Script
```python
import math

def round_to_sig(value, expected_str):
    """Round value to the same number of decimal places as expected_str."""
    if '.' in expected_str:
        dec_places = len(expected_str.split('.')[-1])
        return round(value, dec_places)
    else:
        return round(value)

def print_claim(id_, computed, expected):
    rounded = round_to_sig(computed, expected)
    match = "yes" if str(rounded) == expected else "no"
    print(f"CLAIM {id_}: computed={computed:.10g} expected={expected} match={match}")

# Q1
x0 = 0.0
u0 = 0.1
deltaV = 0.5 * ((x0 + u0) ** 2 - x0 ** 2)
y0 = x0 + 0.5 * u0
supply = u0 * y0
print_claim("Q1", deltaV, "0.005")  # ΔV and supply are both 0.005

# Q2
alpha = 0.1
x0 = 2.0
u0 = 0.0
delta = alpha - alpha ** 2 / 2
x1 = (1 - alpha) * x0 + u0
V0 = 0.5 * x0 ** 2
V1 = 0.5 * x1 ** 2
deltaV = V1 - V0
neg_delta_x2 = -delta * x0 ** 2
print_claim("Q2", deltaV, "-0.38")

# Q3
alpha = 0.1
x0 = 2.0
u0 = 0.5
delta = alpha - alpha ** 2 / 2
x1 = (1 - alpha) * x0 + u0
V0 = 0.5 * x0 ** 2
V1 = 0.5 * x1 ** 2
deltaV = V1 - V0
y0 = (1 - alpha) * x0 + 0.5 * u0
supply = u0 * y0
diff = deltaV - supply
print_claim("Q3", deltaV, "0.645")

# Q4
alpha = 0.1
delta = alpha - alpha ** 2 / 2
x = 1.0
u = -1.0
expr = -delta * x ** 2 - alpha * x * u + 0.5 * u ** 2
print_claim("Q4", expr, "0.505")

# Q5
q = 0.1
U_max = 1.0
N = 100
delta_quant = N * U_max * q / 2
print_claim("Q5", delta_quant, "5.0")

# Q6
delta = 0.095
N = 100
delta_quant = 5.0
x_star = math.sqrt(delta_quant / (delta * N))
print_claim("Q6", x_star, "0.726")

# Q7
omega_c = 1.0
T_d = 0.5
phi_d = omega_c * T_d
print_claim("Q7", phi_d, "0.5")

# Q8
k_S = 2.0
epsilon_S = 0.1
epsilon_W = 0.2
M = k_S * (epsilon_S + epsilon_W)
print_claim("Q8", M, "0.6")

# Q9
phi_d = 0.5
ell_d = phi_d / (2 * math.pi)
print_claim("Q9", ell_d, "0.0796")

# Q10
M = 0.6
M_n = M / (1 + M)
print_claim("Q10", M_n, "0.375")

# Q11
M_n = 0.375
ell_d = 0.5 / (2 * math.pi)  # same as in Q9
rho = M_n / ell_d
print_claim("Q11", rho, "4.71")

# Q12
Delta = 0.05
u_max = 1.0
E_q = (Delta / 2) * u_max
print_claim("Q12", E_q, "0.025")

# Q13
E_0 = u_max ** 2
overhead = E_q / E_0
print_claim("Q13", overhead, "0.025")

# Q14
Delta = 0.05
lambda_W = 0.5
r_q = (Delta / 2) / lambda_W
print_claim("Q14", r_q, "0.05")

# Q15
delta = 0.1
M = 0.6
fraction = delta / M
print_claim("Q15", fraction, "0.1667")

# Q16
# Show the maximum δ at α=1
alpha = 1.0
delta_max = alpha - alpha ** 2 / 2
print_claim("Q16", delta_max, "0.5")

```

## Execution output
```
CLAIM Q1: computed=0.005 expected=0.005 match=yes
CLAIM Q2: computed=-0.38 expected=-0.38 match=yes
CLAIM Q3: computed=0.645 expected=0.645 match=yes
CLAIM Q4: computed=0.505 expected=0.505 match=yes
CLAIM Q5: computed=5 expected=5.0 match=yes
CLAIM Q6: computed=0.7254762501 expected=0.726 match=no
CLAIM Q7: computed=0.5 expected=0.5 match=yes
CLAIM Q8: computed=0.6 expected=0.6 match=yes
CLAIM Q9: computed=0.07957747155 expected=0.0796 match=yes
CLAIM Q10: computed=0.375 expected=0.375 match=yes
CLAIM Q11: computed=4.71238898 expected=4.71 match=yes
CLAIM Q12: computed=0.025 expected=0.025 match=yes
CLAIM Q13: computed=0.025 expected=0.025 match=yes
CLAIM Q14: computed=0.05 expected=0.05 match=yes
CLAIM Q15: computed=0.1666666667 expected=0.1667 match=yes
CLAIM Q16: computed=0.5 expected=0.5 match=yes

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.005 | 0.005 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | -0.38 | -0.38 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.645 | 0.645 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.505 | 0.505 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 5 | 5.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 0.7254762501 | 0.726 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 0.5 | 0.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 0.6 | 0.6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 0.07957747155 | 0.0796 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 0.375 | 0.375 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 4.71238898 | 4.71 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 0.025 | 0.025 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 0.025 | 0.025 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 0.05 | 0.05 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 0.1666666667 | 0.1667 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q16 | 0.5 | 0.5 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
