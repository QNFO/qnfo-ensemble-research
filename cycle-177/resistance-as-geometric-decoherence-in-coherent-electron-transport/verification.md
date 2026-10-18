# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The quantum of resistance is $R_{0}=h/2e^{2}\\approx12.9\\,\\mathrm{k\\Omega}$.",
    "inputs": "h = 6.626×10^{-34} J·s, e = 1.602×10^{-19} C",
    "formula": "R0 = h / (2 * e^2)"
  },
  {
    "id": "Q2",
    "statement": "The resistance slope for $L_{\\phi}=3\\,\\mu\\mathrm{m}$ is $S_{1}=4.30\\times10^{9}\\,\\Omega\\,\\mathrm{m}^{-1}$.",
    "inputs": "R0 = 12.9×10^{3} Ω, L_{\\phi}=3\\,\\mu\\mathrm{m}=3×10^{-6}\\,\\mathrm{m}",
    "formula": "S1 = R0 / L_{\\phi}"
  },
  {
    "id": "Q3",
    "statement": "Expressed per micrometer, the slope is $S_{1}=4.30\\times10^{3}\\,\\Omega\\,\\mu\\mathrm{m}^{-1}=0.333\\,\\mu\\mathrm{m}^{-1}\\times R_{0}$.",
    "inputs": "R0 = 12.9×10^{3} Ω, L_{\\phi}=3\\,\\mu\\mathrm{m}",
    "formula": "S1_{\\mu m} = R0 / L_{\\phi} (with L_{\\phi} in µm)"
  },
  {
    "id": "Q4",
    "statement": "The resistance slope for $L_{\\phi}=10.4\\,\\mu\\mathrm{m}$ is $S_{2}=1.24\\times10^{9}\\,\\Omega\\,\\mathrm{m}^{-1}$.",
    "inputs": "R0 = 12.9×10^{3} Ω, L_{\\phi}=10.4\\,\\mu\\mathrm{m}=10.4×10^{-6}\\,\\mathrm{m}",
    "formula": "S2 = R0 / L_{\\phi}"
  },
  {
    "id": "Q5",
    "statement": "Expressed per micrometer, the slope is $S_{2}=1.24\\times10^{3}\\,\\Omega\\,\\mu\\mathrm{m}^{-1}=0.096\\,\\mu\\mathrm{m}^{-1}\\times R_{0}$.",
    "inputs": "R0 = 12.9×10^{3} Ω, L_{\\phi}=10.4\\,\\mu\\mathrm{m}",
    "formula": "S2_{\\mu m} = R0 / L_{\\phi} (with L_{\\phi} in µm)"
  },
  {
    "id": "Q6",
    "statement": "The optimal lossless‑complexity index is $LCI_{\\mathrm{opt}}=\\ln(2\\pi)\\approx1.83$.",
    "inputs": "none (mathematical constant 2π)",
    "formula": "LCI_opt = ln(2 * pi)"
  },
  {
    "id": "Q7",
    "statement": "For a $10\\,\\mu\\mathrm{m}$ wire with $L_{\\phi}=3\\,\\mu\\mathrm{m}$, the resistance is $R_{1}=43.0\\,\\mathrm{k\\Omega}$.",
    "inputs": "R0 = 12.9\\,\\mathrm{k\\Omega}, L = 10\\,\\mu\\mathrm{m}, L_{\\phi}=3\\,\\mu\\mathrm{m}",
    "formula": "R1 = R0 * (L / L_{\\phi})"
  },
  {
    "id": "Q8",
    "statement": "For a $10\\,\\mu\\mathrm{m}$ wire with $L_{\\phi}=10.4\\,\\mu\\mathrm{m}$, the resistance is $R_{2}=12.4\\,\\mathrm{k\\Omega}$.",
    "inputs": "R0 = 12.9\\,\\mathrm{k\\Omega}, L = 10\\,\\mu\\mathrm{m}, L_{\\phi}=10.4\\,\\mu\\mathrm{m}",
    "formula": "R2 = R0 * (L / L_{\\phi})"
  },
  {
    "id": "Q9",
    "statement": "Increasing $L_{\\phi}$ from $3\\,\\mu\\mathrm{m}$ to $10.4\\,\\mu\\mathrm{m}$ reduces the resistance by a factor of approximately $3.5$.",
    "inputs": "R1 = 43.0\\,\\mathrm{k\\Omega}, R2 = 12.4\\,\\mathrm{k\\Omega}, L_{\\phi1}=3\\,\\mu\\mathrm{m}, L_{\\phi2}=10.4\\,\\mu\\mathrm{m}",
    "formula": "factor = R1 / R2 ≈ L_{\\phi2} / L_{\\phi1}"
  },
  {
    "id": "Q10",
    "statement": "Assuming $L_{\\phi}=15\\,\\mu\\mathrm{m}$, the model predicts $R=8.6\\,\\mathrm{k\\Omega}$ for a $10\\,\\mu\\mathrm{m}$ wire.",
    "inputs": "R0 = 12.9\\,\\mathrm{k\\Omega}, L = 10\\,\\mu\\mathrm{m}, L_{\\phi}=15\\,\\mu\\mathrm{m}",
    "formula": "R = R0 * (L / L_{\\phi})"
  },
  {
    "id": "Q11",
    "statement": "This corresponds to an approximately $80\\%$ reduction relative to the $43.0\\,\\mathrm{k\\Omega}$ case.",
    "inputs": "R_proj = 8.6\\,\\mathrm{k\\Omega}, R1 = 43.0\\,\\mathrm{k\\Omega}",
    "formula": "reduction = 1 - (R_proj / R1)"
  }
]

## Script
```python
import math

# Constants
h = 6.626e-34          # J·s
e = 1.602e-19          # C
R0 = h / (2 * e**2)    # Ω
R0_kΩ = R0 / 1e3       # kΩ

# Input parameters
L_phi1 = 3e-6          # m
L_phi2 = 10.4e-6       # m
L = 10e-6              # m
L_phi_proj = 15e-6     # m

# Computations
S1 = R0 / L_phi1                       # Ω·m⁻¹
S1_per_um = R0 / 3.0                    # Ω·µm⁻¹ (L_phi1 = 3 µm)
S2 = R0 / L_phi2                       # Ω·m⁻¹
S2_per_um = R0 / 10.4                   # Ω·µm⁻¹ (L_phi2 = 10.4 µm)
LCI_opt = math.log(2 * math.pi)        # dimensionless
R1 = R0 * (L / L_phi1)                 # Ω
R2 = R0 * (L / L_phi2)                 # Ω
factor = R1 / R2                        # dimensionless
R_proj = R0 * (L / L_phi_proj)         # Ω
reduction = 1 - (R_proj / R1)          # dimensionless (fraction)

# Expected values (as plain numbers in the same units as computed)
expected = {
    "Q1": 12.9e3,          # Ω
    "Q2": 4.30e9,          # Ω·m⁻¹
    "Q3": 4.30e3,          # Ω·µm⁻¹
    "Q4": 1.24e9,          # Ω·m⁻¹
    "Q5": 1.24e3,          # Ω·µm⁻¹
    "Q6": 1.83,            # dimensionless
    "Q7": 43.0e3,          # Ω
    "Q8": 12.4e3,          # Ω
    "Q9": 3.5,             # dimensionless
    "Q10": 8.6e3,          # Ω
    "Q11": 80.0,           # percent
}

# Helper to round to the same number of significant figures as the expected value
def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Determine matches
matches = {}
matches["Q1"] = "yes" if round_sig(R0, 3) == round_sig(expected["Q1"], 3) else "no"
matches["Q2"] = "yes" if round_sig(S1, 3) == round_sig(expected["Q2"], 3) else "no"
matches["Q3"] = "yes" if round_sig(S1_per_um, 3) == round_sig(expected["Q3"], 3) else "no"
matches["Q4"] = "yes" if round_sig(S2, 3) == round_sig(expected["Q4"], 3) else "no"
matches["Q5"] = "yes" if round_sig(S2_per_um, 3) == round_sig(expected["Q5"], 3) else "no"
matches["Q6"] = "yes" if round_sig(LCI_opt, 3) == round_sig(expected["Q6"], 3) else "no"
matches["Q7"] = "yes" if round_sig(R1, 3) == round_sig(expected["Q7"], 3) else "no"
matches["Q8"] = "yes" if round_sig(R2, 3) == round_sig(expected["Q8"], 3) else "no"
matches["Q9"] = "yes" if round_sig(factor, 2) == round_sig(expected["Q9"], 2) else "no"
matches["Q10"] = "yes" if round_sig(R_proj, 3) == round_sig(expected["Q10"], 3) else "no"
matches["Q11"] = "yes" if round_sig(reduction*100, 2) == round_sig(expected["Q11"], 2) else "no"

# Print results
print(f"CLAIM Q1: computed={R0:.8g} expected={expected['Q1']:.8g} match={matches['Q1']}")
print(f"CLAIM Q2: computed={S1:.8g} expected={expected['Q2']:.8g} match={matches['Q2']}")
print(f"CLAIM Q3: computed={S1_per_um:.8g} expected={expected['Q3']:.8g} match={matches['Q3']}")
print(f"CLAIM Q4: computed={S2:.8g} expected={expected['Q4']:.8g} match={matches['Q4']}")
print(f"CLAIM Q5: computed={S2_per_um:.8g} expected={expected['Q5']:.8g} match={matches['Q5']}")
print(f"CLAIM Q6: computed={LCI_opt:.8g} expected={expected['Q6']:.8g} match={matches['Q6']}")
print(f"CLAIM Q7: computed={R1:.8g} expected={expected['Q7']:.8g} match={matches['Q7']}")
print(f"CLAIM Q8: computed={R2:.8g} expected={expected['Q8']:.8g} match={matches['Q8']}")
print(f"CLAIM Q9: computed={factor:.8g} expected={expected['Q9']:.8g} match={matches['Q9']}")
print(f"CLAIM Q10: computed={R_proj:.8g} expected={expected['Q10']:.8g} match={matches['Q10']}")
print(f"CLAIM Q11: computed={reduction*100:.8g} expected={expected['Q11']:.8g} match={matches['Q11']}")
print(f"VERIFICATION SUMMARY: 11 claims, {list(matches.values()).count('yes')} match, {list(matches.values()).count('no')} mismatch")

```

## Execution output
```
CLAIM Q1: computed=12909.113 expected=12900 match=yes
CLAIM Q2: computed=4.3030378e+09 expected=4.3e+09 match=yes
CLAIM Q3: computed=4303.0378 expected=4300 match=yes
CLAIM Q4: computed=1.2412609e+09 expected=1.24e+09 match=yes
CLAIM Q5: computed=1241.2609 expected=1240 match=yes
CLAIM Q6: computed=1.8378771 expected=1.83 match=no
CLAIM Q7: computed=43030.378 expected=43000 match=yes
CLAIM Q8: computed=12412.609 expected=12400 match=yes
CLAIM Q9: computed=3.4666667 expected=3.5 match=yes
CLAIM Q10: computed=8606.0755 expected=8600 match=no
CLAIM Q11: computed=80 expected=80 match=yes
VERIFICATION SUMMARY: 11 claims, 9 match, 2 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 12909.113 | 12900 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 4.3030378e+09 | 4.3e+09 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 4303.0378 | 4300 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 1.2412609e+09 | 1.24e+09 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 1241.2609 | 1240 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 1.8378771 | 1.83 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 43030.378 | 43000 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 12412.609 | 12400 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 3.4666667 | 3.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 8606.0755 | 8600 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 80 | 80 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 11.
