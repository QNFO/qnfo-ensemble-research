# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Thermal energy at 1 K is $E_T(1\\ \\mathrm{K}) = 8.62\\times10^{-5}\\ \\mathrm{eV}$.",
    "inputs": "Boltzmann constant $k_B = 8.617333\\times10^{-5}\\ \\mathrm{eV/K}$, temperature $T = 1\\ \\mathrm{K}$",
    "formula": "$E_T = k_B \\times T$"
  },
  {
    "id": "Q2",
    "statement": "Thermal energy at 0.1 K is $E_T(0.1\\ \\mathrm{K}) = 8.62\\times10^{-6}\\ \\mathrm{eV}$.",
    "inputs": "Boltzmann constant $k_B = 8.617333\\times10^{-5}\\ \\mathrm{eV/K}$, temperature $T = 0.1\\ \\mathrm{K}$",
    "formula": "$E_T = k_B \\times T$"
  },
  {
    "id": "Q3",
    "statement": "Thermal energy at 20 K is $E_T(20\\ \\mathrm{K}) = 1.72\\times10^{-3}\\ \\mathrm{eV}$.",
    "inputs": "Boltzmann constant $k_B = 8.617333\\times10^{-5}\\ \\mathrm{eV/K}$, temperature $T = 20\\ \\mathrm{K}$",
    "formula": "$E_T = k_B \\times T$"
  },
  {
    "id": "Q4",
    "statement": "The ratio of thermal energies $E_T(1\\ \\mathrm{K})/E_T(0.1\\ \\mathrm{K}) = 10.0$.",
    "inputs": "Thermal energies from Q1 and Q2",
    "formula": "$\\frac{E_T(1\\ \\mathrm{K})}{E_T(0.1\\ \\mathrm{K})}$"
  },
  {
    "id": "Q5",
    "statement": "The Schottky‑anomaly peak position is $x^{*}=2.3993$.",
    "inputs": "Solution of the equation $\\frac{2}{x}=\\tanh\\left(\\frac{x}{2}\\right)$ by fixed‑point iteration",
    "formula": "Find $x$ such that $\\frac{2}{x}=\\tanh\\left(\\frac{x}{2}\\right)$"
  },
  {
    "id": "Q6",
    "statement": "The dimensionless peak height is $C_{\\max}/R = 0.439$.",
    "inputs": "Peak position $x^{*}=2.3993$",
    "formula": "$\\frac{C_{\\max}}{R}=\\frac{{x^{*}}^{2}}{4\\cosh^{2}(x^{*}/2)}$"
  },
  {
    "id": "Q7",
    "statement": "The Schottky peak heat capacity is $C_{\\max}=3.65\\ \\mathrm{J\\,mol^{-1}\\,K^{-1}}$.",
    "inputs": "Gas constant $R=8.314\\ \\mathrm{J\\,mol^{-1}\\,K^{-1}}$, dimensionless height $C_{\\max}/R=0.439$",
    "formula": "$C_{\\max}=0.439\\times R$"
  },
  {
    "id": "Q8",
    "statement": "The temperature at which the Schottky peak occurs satisfies $T^{*}=0.4168\\,\\Delta/k_{B}$.",
    "inputs": "Peak position $x^{*}=2.3993$, Boltzmann constant $k_{B}$",
    "formula": "$T^{*}=\\frac{\\Delta}{x^{*}k_{B}}$ (numerically $1/x^{*}=0.4168$)"
  },
  {
    "id": "Q9",
    "statement": "For a level splitting $\\Delta=1.72\\times10^{-3}\\ \\mathrm{eV}$ the Schottky peak temperature is $T^{*}=8.32\\ \\mathrm{K}$.",
    "inputs": "$\\Delta=1.72\\times10^{-3}\\ \\mathrm{eV}$, $x^{*}=2.3993$, $k_{B}=8.617333\\times10^{-5}\\ \\mathrm{eV/K}$",
    "formula": "$T^{*}=\\frac{\\Delta}{x^{*}k_{B}}$"
  },
  {
    "id": "Q10",
    "statement": "The stoichiometric tolerance window width is $\\Delta y = 0.9$.",
    "inputs": "Oxygen‑deficiency range $-0.4<y<0.5$",
    "formula": "$\\Delta y = y_{\\text{max}} - y_{\\text{min}}$"
  },
  {
    "id": "Q11",
    "statement": "The midpoint of the stoichiometric window is $y_{\\text{mid}} = 0.05$.",
    "inputs": "Range $-0.4<y<0.5$",
    "formula": "$y_{\\text{mid}} = (y_{\\text{max}} + y_{\\text{min}})/2$"
  },
  {
    "id": "Q12",
    "statement": "The excess‑side advantage is $11.1\\%$ of the window width.",
    "inputs": "Window width $\\Delta y = 0.9$, excess side length $0.1$",
    "formula": "$\\frac{0.1}{0.9}\\times100\\%$"
  },
  {
    "id": "Q13",
    "statement": "The synthesis temperature in kelvin is $T = 1873.15\\ \\mathrm{K}$.",
    "inputs": "Synthesis temperature $1600^{\\circ}\\mathrm{C}$, conversion $+273.15$",
    "formula": "$T = 1600 + 273.15$"
  },
  {
    "id": "Q14",
    "statement": "The thermal energy at the synthesis temperature is $k_{B}T = 0.16142\\ \\mathrm{eV}$.",
    "inputs": "Boltzmann constant $k_{B}=8.617333\\times10^{-5}\\ \\mathrm{eV/K}$, temperature $T=1873.15\\ \\mathrm{K}$",
    "formula": "$k_{B}T = k_{B}\\times T$"
  },
  {
    "id": "Q15",
    "statement": "The synthesis pressure is $P = 1.33\\times10^{-3}\\ \\mathrm{Pa}$.",
    "inputs": "Pressure in Torr $10^{-5}\\ \\mathrm{Torr}$, conversion $1\\ \\mathrm{Torr}=133.322\\ \\mathrm{Pa}$",
    "formula": "$P = 10^{-5}\\times133.322$"
  }
]

## Script
```python
import math

# Constants
k_B = 8.617333e-5          # eV/K
R = 8.314                  # J·mol⁻¹·K⁻¹

# Expected values (as strings)
expected = {
    "Q1": "8.62e-5",
    "Q2": "8.62e-6",
    "Q3": "1.72e-3",
    "Q4": "10.0",
    "Q5": "2.3993",
    "Q6": "0.439",
    "Q7": "3.65",
    "Q8": "0.4168",
    "Q9": "8.32",
    "Q10": "0.9",
    "Q11": "0.05",
    "Q12": "11.1",
    "Q13": "1873.15",
    "Q14": "0.16142",
    "Q15": "1.33e-3"
}

def sig_round(value, sig):
    """Round value to given number of significant figures."""
    if value == 0:
        return 0.0
    else:
        return round(value, sig - int(math.floor(math.log10(abs(value)))) - 1)

def compare(comp, exp_str):
    """Compare computed value to expected string."""
    # Convert expected string to float (handle scientific notation)
    exp_val = float(exp_str.replace('e', 'E'))
    # Determine number of significant digits in expected string
    # Remove leading zeros, decimal point, and exponent part
    mantissa = exp_str.split('e')[0] if 'e' in exp_str else exp_str
    mantissa = mantissa.replace('.', '').lstrip('0')
    sig = len(mantissa)
    # Round computed to same sig figs
    comp_rounded = sig_round(comp, sig)
    match = math.isclose(comp_rounded, exp_val, rel_tol=1e-12, abs_tol=0)
    return comp_rounded, match

# Compute claims
results = {}

# Q1
E1 = k_B * 1.0
results["Q1"] = E1

# Q2
E2 = k_B * 0.1
results["Q2"] = E2

# Q3
E3 = k_B * 20.0
results["Q3"] = E3

# Q4
results["Q4"] = E1 / E2

# Q5 – solve 2/x = tanh(x/2) by fixed‑point iteration
x = 2.0
for _ in range(20):
    x = 2.0 / math.tanh(x/2.0)
results["Q5"] = x

# Q6
x_star = results["Q5"]
Cmax_R = (x_star**2) / (4 * math.cosh(x_star/2.0)**2)
results["Q6"] = Cmax_R

# Q7
results["Q7"] = Cmax_R * R

# Q8
results["Q8"] = 1.0 / x_star

# Q9
Delta = 1.72e-3  # eV
T_star = Delta / (x_star * k_B)
results["Q9"] = T_star

# Q10
y_min, y_max = -0.4, 0.5
results["Q10"] = y_max - y_min

# Q11
results["Q11"] = (y_max + y_min) / 2.0

# Q12
excess = 0.1
results["Q12"] = (excess / results["Q10"]) * 100.0

# Q13
results["Q13"] = 1600.0 + 273.15

# Q14
results["Q14"] = k_B * results["Q13"]

# Q15
results["Q15"] = 1e-5 * 133.322

# Print verification lines
for qid in sorted(expected.keys(), key=lambda x: int(x[1:])):
    comp = results[qid]
    comp_rounded, is_match = compare(comp, expected[qid])
    # Use scientific notation for very small/large numbers to match expected format
    if "e" in expected[qid]:
        comp_str = f"{comp_rounded:.2e}"
    else:
        # Preserve the number of decimal places in expected string
        dec_places = expected[qid].split('.')[-1]
        if 'e' in dec_places:
            # fallback
            comp_str = f"{comp_rounded}"
        else:
            comp_str = f"{comp_rounded:.{len(dec_places)}f}"
    print(f"CLAIM {qid}: computed={comp_str} expected={expected[qid]} match={'yes' if is_match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for v in expected if compare(results[v], expected[v])[1])} match, {len(expected) - sum(1 for v in expected if compare(results[v], expected[v])[1])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=8.62e-05 expected=8.62e-5 match=yes
CLAIM Q2: computed=8.62e-06 expected=8.62e-6 match=yes
CLAIM Q3: computed=1.72e-03 expected=1.72e-3 match=yes
CLAIM Q4: computed=10.0 expected=10.0 match=yes
CLAIM Q5: computed=2.3994 expected=2.3993 match=no
CLAIM Q6: computed=0.439 expected=0.439 match=yes
CLAIM Q7: computed=3.65 expected=3.65 match=yes
CLAIM Q8: computed=0.4168 expected=0.4168 match=yes
CLAIM Q9: computed=8.32 expected=8.32 match=yes
CLAIM Q10: computed=0.9 expected=0.9 match=yes
CLAIM Q11: computed=0.05 expected=0.05 match=yes
CLAIM Q12: computed=11.1 expected=11.1 match=yes
CLAIM Q13: computed=1873.15 expected=1873.15 match=yes
CLAIM Q14: computed=0.16142 expected=0.16142 match=yes
CLAIM Q15: computed=1.33e-03 expected=1.33e-3 match=yes
VERIFICATION SUMMARY: 15 claims, 14 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 8.62e-05 | 8.62e-5 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 8.62e-06 | 8.62e-6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 1.72e-03 | 1.72e-3 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 10.0 | 10.0 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 2.3994 | 2.3993 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 0.439 | 0.439 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 3.65 | 3.65 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 0.4168 | 0.4168 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 8.32 | 8.32 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 0.9 | 0.9 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 0.05 | 0.05 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 11.1 | 11.1 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 1873.15 | 1873.15 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q14 | 0.16142 | 0.16142 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q15 | 1.33e-03 | 1.33e-3 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 15.
