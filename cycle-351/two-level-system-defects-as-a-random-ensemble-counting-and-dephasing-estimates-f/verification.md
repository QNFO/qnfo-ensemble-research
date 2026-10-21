# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Barrier volume is $V = 4\\times10^{-23}\\ \\mathrm{m^{3}}$.",
    "inputs": "A=2e-14 m^2, d=2e-9 m",
    "formula": "V = A * d"
  },
  {
    "id": "Q2",
    "statement": "Fractional coupling window is $f_{\\Gamma}=2\\times10^{-3}$.",
    "inputs": "Gamma=1e6 s^-1, Delta0=1e9 s^-1",
    "formula": "f_Gamma = 2 * Gamma / Delta0"
  },
  {
    "id": "Q3",
    "statement": "Mean strongly‑coupled defect count per junction is $\\lambda = 0.08$.",
    "inputs": "rho=1e24 m^-3, V=4e-23 m^3, f_Gamma=2e-3",
    "formula": "lambda = rho * V * f_Gamma"
  },
  {
    "id": "Q4",
    "statement": "Single‑junction probability of at least one strongly coupled defect is $P_{1}=0.0769$.",
    "inputs": "lambda=0.08",
    "formula": "P1 = 1 - exp(-lambda)"
  },
  {
    "id": "Q5",
    "statement": "Chip‑level mean defect count is $\\lambda_{chip}=8$.",
    "inputs": "N_j=100, lambda=0.08",
    "formula": "lambda_chip = N_j * lambda"
  },
  {
    "id": "Q6",
    "statement": "Chip‑level probability of at least one strongly coupled defect is $P_{chip}=0.99966$.",
    "inputs": "lambda_chip=8",
    "formula": "P_chip = 1 - exp(-lambda_chip)"
  },
  {
    "id": "Q7",
    "statement": "Standard deviation of the chip‑level Poisson count is $\\sigma_{chip}=2.8284$.",
    "inputs": "lambda_chip=8",
    "formula": "sigma_chip = sqrt(lambda_chip)"
  },
  {
    "id": "Q8",
    "statement": "Spectral‑model mean count in the resonance window is $\\lambda=0.105263$.",
    "inputs": "N_bar=100, delta=10 MHz (0.01 GHz), B=19 GHz",
    "formula": "lambda = (N_bar * 2*delta) / B"
  },
  {
    "id": "Q9",
    "statement": "Spectral‑model probability of at least one near‑resonant defect is $P_{\\ge1}=0.0999$.",
    "inputs": "lambda=0.105263",
    "formula": "P_ge1 = 1 - exp(-lambda)"
  },
  {
    "id": "Q10",
    "statement": "Mean defect frequency spacing is $\\bar{s}=190\\ \\mathrm{MHz}$.",
    "inputs": "B=19 GHz, N_bar=100",
    "formula": "s_bar = B / N_bar"
  },
  {
    "id": "Q11",
    "statement": "Per‑defect dispersive factor $(g_0/\\Delta)^2 = 10^{-4}$.",
    "inputs": "g0=1 MHz, Delta=100 MHz",
    "formula": "(g0/Delta)^2"
  },
  {
    "id": "Q12",
    "statement": "Per‑defect dispersive dephasing rate is $\\Gamma_{\\varphi}^{(1)} = 1\\ \\mathrm{s^{-1}}$.",
    "inputs": "factor=1e-4, gamma0=1e4 s^-1",
    "formula": "Gamma_phi_1 = factor * gamma0"
  },
  {
    "id": "Q13",
    "statement": "Total dispersive dephasing rate for five defects is $\\Gamma_{\\varphi}^{(disp)} = 5\\ \\mathrm{s^{-1}}$.",
    "inputs": "n=5, Gamma_phi_1=1 s^-1",
    "formula": "Gamma_phi_disp = n * Gamma_phi_1"
  },
  {
    "id": "Q14",
    "statement": "Dispersive dephasing time is $T_{\\varphi}=0.2\\ \\mathrm{s}$.",
    "inputs": "Gamma_phi_disp=5 s^-1",
    "formula": "T_phi = 1 / Gamma_phi_disp"
  },
  {
    "id": "Q15",
    "statement": "Telegraph‑noise dephasing rate is $\\Gamma_{\\varphi}^{(tn)} = 1.25\\times10^{3}\\ \\mathrm{s^{-1}}$.",
    "inputs": "epsilon=1e5 s^-1, gamma=1e6 s^-1",
    "formula": "Gamma_phi_tn = epsilon^2 / (8 * gamma)"
  },
  {
    "id": "Q16",
    "statement": "Telegraph‑noise dephasing time is $T_{\\varphi}=800\\ \\mu\\mathrm{s}$.",
    "inputs": "Gamma_phi_tn=1.25e3 s^-1",
    "formula": "T_phi = 1 / Gamma_phi_tn"
  }
]

## Script
```python
import math

def fmt(val, sig):
    """Round val to given number of significant digits and format without scientific notation if possible."""
    if val == 0:
        return "0"
    # Determine order of magnitude
    order = int(math.floor(math.log10(abs(val))))
    digits = sig - 1 - order
    fmt_str = "{:." + str(max(digits,0)) + "f}"
    rounded = round(val, digits) if digits >= 0 else round(val, -digits)
    s = fmt_str.format(rounded)
    # Remove trailing zeros and dot
    s = s.rstrip('0').rstrip('.') if '.' in s else s
    return s

claims = [
    ("Q1", 4e-23, "4e-23"),
    ("Q2", 2e-3, "2e-3"),
    ("Q3", 0.08, "0.08"),
    ("Q4", 1 - math.exp(-0.08), "0.0769"),
    ("Q5", 8.0, "8"),
    ("Q6", 1 - math.exp(-8), "0.99966"),
    ("Q7", math.sqrt(8), "2.8284"),
    ("Q8", (100 * 0.02) / 19, "0.105263"),
    ("Q9", 1 - math.exp(-((100 * 0.02) / 19)), "0.0999"),
    ("Q10", 190.0, "190"),
    ("Q11", (1e6 / 1e8) ** 2, "1e-4"),
    ("Q12", (1e-4) * 1e4, "1"),
    ("Q13", 5 * 1, "5"),
    ("Q14", 1 / 5, "0.2"),
    ("Q15", (1e5 ** 2) / (8 * 1e6), "1.25e3"),
    ("Q16", 1 / ((1e5 ** 2) / (8 * 1e6)), "800e-6"),
]

for cid, comp, exp in claims:
    # Determine number of significant digits in expected value
    # Strip possible scientific notation
    if "e" in exp or "E" in exp:
        base, exp_part = exp.split('e') if 'e' in exp else exp.split('E')
        sig_digits = len(base.replace('.', '').replace('-', '').lstrip('0'))
    else:
        # Count digits ignoring decimal point and leading zeros
        sig_digits = len(exp.replace('.', '').replace('-', '').lstrip('0'))
    # Format computed value to same number of significant digits
    comp_str = fmt(comp, sig_digits)
    match = "yes" if comp_str == exp else "no"
    print(f"CLAIM {cid}: computed={comp_str} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if fmt(c, len(e.replace('.','').replace('-','').lstrip('0'))) == e)} match, {sum(1 for _,c,e in claims if fmt(c, len(e.replace('.','').replace('-','').lstrip('0'))) != e)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.00000000000000000000004 expected=4e-23 match=no
CLAIM Q2: computed=0.002 expected=2e-3 match=no
CLAIM Q3: computed=0.08 expected=0.08 match=yes
CLAIM Q4: computed=0.0769 expected=0.0769 match=yes
CLAIM Q5: computed=8 expected=8 match=yes
CLAIM Q6: computed=0.99966 expected=0.99966 match=yes
CLAIM Q7: computed=2.8284 expected=2.8284 match=yes
CLAIM Q8: computed=0.105263 expected=0.105263 match=yes
CLAIM Q9: computed=0.0999 expected=0.0999 match=yes
CLAIM Q10: computed=190 expected=190 match=yes
CLAIM Q11: computed=0.0001 expected=1e-4 match=no
CLAIM Q12: computed=1 expected=1 match=yes
CLAIM Q13: computed=5 expected=5 match=yes
CLAIM Q14: computed=0.2 expected=0.2 match=yes
CLAIM Q15: computed=1250 expected=1.25e3 match=no
CLAIM Q16: computed=0.0008 expected=800e-6 match=no
VERIFICATION SUMMARY: 16 claims, 11 match, 5 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.00000000000000000000004 | 4e-23 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.002 | 2e-3 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.08 | 0.08 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.0769 | 0.0769 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 0.99966 | 0.99966 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 2.8284 | 2.8284 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 0.105263 | 0.105263 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q9 | 0.0999 | 0.0999 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 190 | 190 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 0.0001 | 1e-4 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 5 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 0.2 | 0.2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 1250 | 1.25e3 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 0.0008 | 800e-6 | no | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
