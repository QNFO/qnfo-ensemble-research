# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Landauer limit at physiological temperature (310 K) is $2.97\\times10^{-21}\\,\\mathrm{J}$ per bit.",
    "inputs": "k_B = 1.380649e-23 J·K^{-1}, T = 310 K, ln2 = 0.693147",
    "formula": "E_L = k_B * T * ln2"
  },
  {
    "id": "Q2",
    "statement": "Mechanical switching energy for the soft stiffness limit ($k_{\\text{eff}}=0.01\\,\\mathrm{N\\,m^{-1}}$) is $5.0\\times10^{-21}\\,\\mathrm{J}$.",
    "inputs": "k_eff = 0.01 N·m^{-1}, x = 1.0e-9 m",
    "formula": "E_m = 0.5 * k_eff * x^2"
  },
  {
    "id": "Q3",
    "statement": "Mechanical switching energy for the stiff stiffness limit ($k_{\\text{eff}}=1.0\\,\\mathrm{N\\,m^{-1}}$) is $5.0\\times10^{-19}\\,\\mathrm{J}$.",
    "inputs": "k_eff = 1.0 N·m^{-1}, x = 1.0e-9 m",
    "formula": "E_m = 0.5 * k_eff * x^2"
  },
  {
    "id": "Q4",
    "statement": "Soft‑limit mechanical energy corresponds to $1.168\\,k_{B}T$.",
    "inputs": "E_m = 5.0e-21 J, k_B = 1.380649e-23 J·K^{-1}, T = 310 K",
    "formula": "(E_m) / (k_B * T)"
  },
  {
    "id": "Q5",
    "statement": "Stiff‑limit mechanical energy corresponds to $116.8\\,k_{B}T$.",
    "inputs": "E_m = 5.0e-19 J, k_B = 1.380649e-23 J·K^{-1}, T = 310 K",
    "formula": "(E_m) / (k_B * T)"
  },
  {
    "id": "Q6",
    "statement": "Soft‑limit mechanical energy is $1.69$ times the Landauer limit.",
    "inputs": "E_m = 5.0e-21 J, E_L = 2.96666e-21 J",
    "formula": "E_m / E_L"
  },
  {
    "id": "Q7",
    "statement": "Stiff‑limit mechanical energy is $168.5$ times the Landauer limit.",
    "inputs": "E_m = 5.0e-19 J, E_L = 2.96666e-21 J",
    "formula": "E_m / E_L"
  },
  {
    "id": "Q8",
    "statement": "Dipole‑field energy difference between β‑ and α‑monomers is $2.138\\times10^{-20}\\,\\mathrm{J}$.",
    "inputs": "Δp = 641 D = 2.138e-27 C·m, E = 1.0e7 V·m^{-1}",
    "formula": "ΔU = Δp * E"
  },
  {
    "id": "Q9",
    "statement": "Monomer dipole‑field energy difference equals $4.99\\,k_{B}T$.",
    "inputs": "ΔU = 2.138e-20 J, k_B = 1.380649e-23 J·K^{-1}, T = 310 K",
    "formula": "ΔU / (k_B * T)"
  },
  {
    "id": "Q10",
    "statement": "Dipole‑field energy of the αβ‑dimer in the field is $5.80464\\times10^{-20}\\,\\mathrm{J}$.",
    "inputs": "p_{αβ} = 1740 D = 5.803e-27 C·m, E = 1.0e7 V·m^{-1}",
    "formula": "U_{αβ} = p_{αβ} * E"
  },
  {
    "id": "Q11",
    "statement": "Dimer dipole‑field energy equals $13.56\\,k_{B}T$.",
    "inputs": "U_{αβ} = 5.80464e-20 J, k_B = 1.380649e-23 J·K^{-1}, T = 310 K",
    "formula": "U_{αβ} / (k_B * T)"
  },
  {
    "id": "Q12",
    "statement": "Effective energy gap (average of monomer and dimer contributions) is approximately $9.28\\,k_{B}T$.",
    "inputs": "monomer gap = 4.99 k_B T, dimer gap = 13.56 k_B T",
    "formula": "(4.99 + 13.56) / 2"
  },
  {
    "id": "Q13",
    "statement": "Thermal error probability for the effective gap $9.28\\,k_{B}T$ is $9.3\\times10^{-5}$.",
    "inputs": "ΔU_eff = 9.28 * k_B * T, k_B = 1.380649e-23 J·K^{-1}, T = 310 K",
    "formula": "P_error = exp(-ΔU_eff / (k_B * T))"
  },
  {
    "id": "Q14",
    "statement": "Thermal error probability for the dimer gap $13.56\\,k_{B}T$ is $1.3\\times10^{-6}$.",
    "inputs": "ΔU = 13.56 * k_B * T, k_B = 1.380649e-23 J·K^{-1}, T = 310 K",
    "formula": "P_error = exp(-13.56)"
  },
  {
    "id": "Q15",
    "statement": "Screened dipole‑dipole interaction energy between adjacent dimers is $7.39335\\times10^{-21}\\,\\mathrm{J}$.",
    "inputs": "p = 5.803e-27 C·m, ε0 = 8.854e-12 F·m^{-1}, ε_r = 80, r = 8.0e-9 m",
    "formula": "U_dd = p^2 / (4π ε0 ε_r r^3)"
  },
  {
    "id": "Q16",
    "statement": "The unscreened dipole‑dipole energy equals $1.73\\,k_{B}T$.",
    "inputs": "U_dd = 7.39335e-21 J, k_B = 1.380649e-23 J·K^{-1}, T = 310 K",
    "formula": "U_dd / (k_B * T)"
  }
]

## Script
```python
import math

# Constants
kB = 1.380649e-23  # J·K^{-1}
T = 310.0          # K
ln2 = 0.693147
kBT = kB * T

# Expected values as strings
expected = {
    "Q1": "2.97e-21",
    "Q2": "5.0e-21",
    "Q3": "5.0e-19",
    "Q4": "1.168",
    "Q5": "116.8",
    "Q6": "1.69",
    "Q7": "168.5",
    "Q8": "2.138e-20",
    "Q9": "4.99",
    "Q10": "5.80464e-20",
    "Q11": "13.56",
    "Q12": "9.28",
    "Q13": "9.3e-05",
    "Q14": "1.3e-06",
    "Q15": "7.39335e-21",
    "Q16": "1.73",
}

# Computations
results = {}

# Q1: Landauer limit
E_L = kBT * ln2
results["Q1"] = f"{E_L:.2e}"

# Q2: Soft stiffness mechanical energy
k_eff_soft = 0.01
x = 1.0e-9
E_m_soft = 0.5 * k_eff_soft * x**2
results["Q2"] = f"{E_m_soft:.1e}"

# Q3: Stiff stiffness mechanical energy
k_eff_stiff = 1.0
E_m_stiff = 0.5 * k_eff_stiff * x**2
results["Q3"] = f"{E_m_stiff:.1e}"

# Q4: Soft energy in kBT
results["Q4"] = f"{E_m_soft / kBT:.3f}"

# Q5: Stiff energy in kBT
results["Q5"] = f"{E_m_stiff / kBT:.1f}"

# Q6: Soft energy / Landauer
results["Q6"] = f"{E_m_soft / E_L:.2f}"

# Q7: Stiff energy / Landauer
results["Q7"] = f"{E_m_stiff / E_L:.1f}"

# Q8: Dipole-field difference (Δp * E)
delta_p = 641 * 3.336e-30  # C·m
E_field = 1.0e7            # V·m^{-1}
delta_U = delta_p * E_field
results["Q8"] = f"{delta_U:.3e}"

# Q9: ΔU in kBT
results["Q9"] = f"{delta_U / kBT:.2f}"

# Q10: Dimer dipole-field energy
p_ab = 1740 * 3.336e-30
U_ab = p_ab * E_field
results["Q10"] = f"{U_ab:.5e}"

# Q11: Dimer energy in kBT
results["Q11"] = f"{U_ab / kBT:.2f}"

# Q12: Average gap in kBT
gap_avg = (4.99 + 13.56) / 2.0
results["Q12"] = f"{gap_avg:.2f}"

# Q13: Error probability for average gap
P_err_avg = math.exp(-gap_avg)
results["Q13"] = f"{P_err_avg:.1e}"

# Q14: Error probability for dimer gap
P_err_dim = math.exp(-13.56)
results["Q14"] = f"{P_err_dim:.1e}"

# Q15: Screened dipole-dipole interaction (unscreened value)
p = p_ab
epsilon0 = 8.854e-12
epsilon_r = 80.0
r = 8.0e-9
U_dd = p**2 / (4 * math.pi * epsilon0 * epsilon_r * r**3)
results["Q15"] = f"{U_dd:.5e}"

# Q16: U_dd in kBT
results["Q16"] = f"{U_dd / kBT:.2f}"

# Print verification lines
for qid in sorted(expected.keys()):
    computed = results[qid]
    exp = expected[qid]
    match = "yes" if computed == exp else "no"
    print(f"CLAIM {qid}: computed={computed} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if results[q]==expected[q])} match, {sum(1 for q in expected if results[q]!=expected[q])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=2.97e-21 expected=2.97e-21 match=yes
CLAIM Q10: computed=5.80464e-20 expected=5.80464e-20 match=yes
CLAIM Q11: computed=13.56 expected=13.56 match=yes
CLAIM Q12: computed=9.28 expected=9.28 match=yes
CLAIM Q13: computed=9.4e-05 expected=9.3e-05 match=no
CLAIM Q14: computed=1.3e-06 expected=1.3e-06 match=yes
CLAIM Q15: computed=7.39335e-21 expected=7.39335e-21 match=yes
CLAIM Q16: computed=1.73 expected=1.73 match=yes
CLAIM Q2: computed=5.0e-21 expected=5.0e-21 match=yes
CLAIM Q3: computed=5.0e-19 expected=5.0e-19 match=yes
CLAIM Q4: computed=1.168 expected=1.168 match=yes
CLAIM Q5: computed=116.8 expected=116.8 match=yes
CLAIM Q6: computed=1.69 expected=1.69 match=yes
CLAIM Q7: computed=168.5 expected=168.5 match=yes
CLAIM Q8: computed=2.138e-20 expected=2.138e-20 match=yes
CLAIM Q9: computed=5.00 expected=4.99 match=no
VERIFICATION SUMMARY: 16 claims, 14 match, 2 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2.97e-21 | 2.97e-21 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 5.80464e-20 | 5.80464e-20 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q11 | 13.56 | 13.56 | yes | match | 4 significant digits (as printed, at least 3) |
| Q12 | 9.28 | 9.28 | yes | match | 3 significant digits (as printed, at least 3) |
| Q13 | 9.4e-05 | 9.3e-05 | no | MISMATCH | 2 significant digits (as the paper states, at least 2) |
| Q14 | 1.3e-06 | 1.3e-06 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 7.39335e-21 | 7.39335e-21 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q16 | 1.73 | 1.73 | yes | match | 3 significant digits (as printed, at least 3) |
| Q2 | 5.0e-21 | 5.0e-21 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 5.0e-19 | 5.0e-19 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 1.168 | 1.168 | yes | match | 4 significant digits (as printed, at least 3) |
| Q5 | 116.8 | 116.8 | yes | match | 4 significant digits (as printed, at least 3) |
| Q6 | 1.69 | 1.69 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 168.5 | 168.5 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 2.138e-20 | 2.138e-20 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 5.00 | 4.99 | no | match | 3 significant digits (as printed, at least 3) |

Mismatches: 1 of 16.


## Auto-corrections

The worker corrected these independently-verified values in place of the paper's stated values (deterministic, no model edit):

| claim | stated | corrected |
|---|---|---|
| Q13 | 9.3 | 9.4 |
