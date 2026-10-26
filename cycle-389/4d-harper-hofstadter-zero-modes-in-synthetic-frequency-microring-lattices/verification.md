# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Resonance angular frequency $\\omega_{c}=1.216\\times10^{15}\\ \\text{rad\\,s}^{-1}$.",
    "inputs": "c = 3\\times10^{8}\\ \\text{m\\,s}^{-1}, \\lambda = 1.55\\times10^{-6}\\ \\text{m}",
    "formula": "omega_c = 2 * pi * c / lambda"
  },
  {
    "id": "Q2",
    "statement": "Cavity energy decay rate $\\kappa = 1.216\\times10^{5}\\ \\text{rad\\,s}^{-1}$.",
    "inputs": "omega_c = 1.216\\times10^{15}\\ \\text{rad\\,s}^{-1}, Q = 10^{10}",
    "formula": "kappa = omega_c / Q"
  },
  {
    "id": "Q3",
    "statement": "Cavity linewidth $\\kappa/(2\\pi) = 19.4\\ \\text{kHz}$.",
    "inputs": "kappa = 1.216\\times10^{5}\\ \\text{rad\\,s}^{-1}",
    "formula": "kappa_over_2pi = kappa / (2 * pi)"
  },
  {
    "id": "Q4",
    "statement": "Photon lifetime $\\tau = 8.22\\ \\mu\\text{s}$.",
    "inputs": "kappa = 1.216\\times10^{5}\\ \\text{rad\\,s}^{-1}",
    "formula": "tau = 1 / kappa"
  },
  {
    "id": "Q5",
    "statement": "Synthetic hopping rate in rad/s $J_{\\text{rad}} = 2.267\\times10^{11}\\ \\text{rad\\,s}^{-1}$.",
    "inputs": "J = 3.606\\times10^{10}\\ \\text{Hz}",
    "formula": "J_rad = 2 * pi * J"
  },
  {
    "id": "Q6",
    "statement": "Hopping‑to‑loss ratio $J/\\kappa \\approx 1.86\\times10^{6}$.",
    "inputs": "J_rad = 2.267\\times10^{11}\\ \\text{rad\\,s}^{-1}, kappa = 1.216\\times10^{5}\\ \\text{rad\\,s}^{-1}",
    "formula": "ratio = J_rad / kappa"
  },
  {
    "id": "Q7",
    "statement": "Thermal photon occupation at 80\\,K $n = 0.1396$.",
    "inputs": "hnu_over_kB = 167.9\\ \\text{K}, T = 80\\ \\text{K}",
    "formula": "n = 1 / (exp(hnu_over_kB / T) - 1)"
  },
  {
    "id": "Q8",
    "statement": "Effective per‑hop error probability $p_{\\text{eff}} = 1.396\\times10^{-4}$.",
    "inputs": "p_sc = 1e-3, n = 0.1396",
    "formula": "p_eff = p_sc * n"
  },
  {
    "id": "Q9",
    "statement": "Transport fidelity after 100 hops $F(100) = 0.9861$.",
    "inputs": "p_eff = 1.396\\times10^{-4}, N = 100",
    "formula": "F = (1 - p_eff) ^ N"
  },
  {
    "id": "Q10",
    "statement": "Second Chern number $C_{2}=1$ for flux $\\phi=2\\pi/10$.",
    "inputs": "p = 1",
    "formula": "C2 = p ^ 2"
  }
]

## Script
```python
import math

def sig_round(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0.0
    else:
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Inputs
c = 3e8                     # m/s
lam = 1.55e-6               # m
Q = 1e10
hnu_over_kB = 167.9         # K
T = 80.0                    # K
p_sc = 1e-3
J_hz = 3.606e10             # Hz
N = 100

# Derived quantities
omega_c = 2 * math.pi * c / lam
kappa = omega_c / Q
kappa_over_2pi = kappa / (2 * math.pi)
tau = 1 / kappa
J_rad = 2 * math.pi * J_hz
ratio = J_rad / kappa
n = 1 / (math.exp(hnu_over_kB / T) - 1)
p_eff = p_sc * n
F = (1 - p_eff) ** N
C2 = 1 ** 2  # p = 1

# Expected values (as strings from the paper)
expected = {
    "Q1": "1.216e15",
    "Q2": "1.216e5",
    "Q3": "1.94e4",   # 19.4 kHz -> 1.94e4 Hz
    "Q4": "8.22e-6",
    "Q5": "2.267e11",
    "Q6": "1.86e6",
    "Q7": "0.1396",
    "Q8": "1.396e-4",
    "Q9": "0.9861",
    "Q10": "1"
}

# Helper to format computed value with appropriate sig figs
def format_match(comp, exp_str):
    # Determine number of significant digits in expected string
    # Remove exponent part if present
    if 'e' in exp_str:
        mantissa, _ = exp_str.split('e')
    else:
        mantissa = exp_str
    # Count digits ignoring leading zeros and decimal point
    mantissa = mantissa.lstrip('0').replace('.', '')
    sig = len(mantissa)
    comp_rounded = sig_round(comp, sig)
    # Use scientific notation with lower-case e
    comp_str = f"{comp_rounded:.{sig-1}e}"
    match = "yes" if comp_str == exp_str else "no"
    return comp_str, match

# Compute and print results
claims = {
    "Q1": omega_c,
    "Q2": kappa,
    "Q3": kappa_over_2pi,
    "Q4": tau,
    "Q5": J_rad,
    "Q6": ratio,
    "Q7": n,
    "Q8": p_eff,
    "Q9": F,
    "Q10": C2
}

for cid, value in claims.items():
    exp = expected[cid]
    comp_str, match = format_match(value, exp)
    print(f"CLAIM {cid}: computed={comp_str} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for cid in claims if format_match(claims[cid], expected[cid])[1]=='yes')} match, {sum(1 for cid in claims if format_match(claims[cid], expected[cid])[1]=='no')} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.216e+15 expected=1.216e15 match=no
CLAIM Q2: computed=1.216e+05 expected=1.216e5 match=no
CLAIM Q3: computed=1.94e+04 expected=1.94e4 match=no
CLAIM Q4: computed=8.22e-06 expected=8.22e-6 match=no
CLAIM Q5: computed=2.266e+11 expected=2.267e11 match=no
CLAIM Q6: computed=1.86e+06 expected=1.86e6 match=no
CLAIM Q7: computed=1.397e-01 expected=0.1396 match=no
CLAIM Q8: computed=1.397e-04 expected=1.396e-4 match=no
CLAIM Q9: computed=9.861e-01 expected=0.9861 match=no
CLAIM Q10: computed=1e+00 expected=1 match=no
VERIFICATION SUMMARY: 10 claims, 0 match, 10 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.216e+15 | 1.216e15 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 1.216e+05 | 1.216e5 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 1.94e+04 | 1.94e4 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 8.22e-06 | 8.22e-6 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 2.266e+11 | 2.267e11 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 1.86e+06 | 1.86e6 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 1.397e-01 | 0.1396 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 1.397e-04 | 1.396e-4 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 9.861e-01 | 0.9861 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 1e+00 | 1 | no | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 10.
