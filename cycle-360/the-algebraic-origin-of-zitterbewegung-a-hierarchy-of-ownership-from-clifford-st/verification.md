# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The ratio of the two unit‑system values of Planck’s constant is \\(1.6023\\times10^{-19}\\) J/eV.",
    "inputs": "ħ_Js = 1.0546×10⁻³⁴ J·s, ħ_eVs = 6.582×10⁻¹⁶ eV·s",
    "formula": "ħ_Js / ħ_eVs"
  },
  {
    "id": "Q2",
    "statement": "The electron rest energy is \\(8.187\\times10^{-14}\\) J.",
    "inputs": "m_e = 9.109×10⁻³¹ kg, c = 2.998×10⁸ m/s",
    "formula": "m_e * c^2"
  },
  {
    "id": "Q3",
    "statement": "The electron rest energy expressed in electronvolts is \\(5.111\\times10^{5}\\) eV (or \\(0.5111\\) MeV).",
    "inputs": "m_e c^2 = 8.187×10⁻¹⁴ J, conversion factor = 1.602×10⁻¹⁹ J/eV",
    "formula": "(m_e c^2) / (1.602×10⁻¹⁹)"
  },
  {
    "id": "Q4",
    "statement": "The rest‑frame Zitterbewegung angular frequency is \\(1.5526\\times10^{21}\\) rad/s.",
    "inputs": "m_e c^2 = 8.187×10⁻¹⁴ J, ħ_Js = 1.0546×10⁻³⁴ J·s",
    "formula": "2 * (m_e c^2) / ħ_Js"
  },
  {
    "id": "Q5",
    "statement": "The rest‑frame Zitterbewegung ordinary frequency is \\(2.471\\times10^{20}\\) Hz.",
    "inputs": "ω₀ = 1.5526×10²¹ rad/s, π = 3.1416",
    "formula": "ω₀ / (2π)"
  },
  {
    "id": "Q6",
    "statement": "Using electron‑volt units, the rest‑frame angular frequency is \\(1.553\\times10^{21}\\) rad/s, agreeing with the J‑unit calculation to four figures.",
    "inputs": "E = 0.5111 MeV = 0.5111×10⁶ eV, ħ_eVs = 6.582×10⁻¹⁶ eV·s",
    "formula": "2 * E / ħ_eVs"
  },
  {
    "id": "Q7",
    "statement": "The rest‑frame Zitterbewegung position‑amplitude scale is \\(1.931\\times10^{-13}\\) m.",
    "inputs": "ħ_Js = 1.0546×10⁻³⁴ J·s, m_e = 9.109×10⁻³¹ kg, c = 2.998×10⁸ m/s",
    "formula": "ħ_Js / (2 * m_e * c)"
  },
  {
    "id": "Q8",
    "statement": "For a gapped Dirac material with gap \\(2Δ = 0.2\\) eV, the Zitterbewegung ordinary frequency is \\(4.836\\times10^{13}\\) Hz.",
    "inputs": "Δ = 0.1 eV, ħ_eVs = 6.582×10⁻¹⁶ eV·s, π = 3.1416",
    "formula": "(2Δ) / (2π * ħ_eVs)"
  },
  {
    "id": "Q9",
    "statement": "The corresponding period is \\(2.0678\\times10^{-14}\\) s (≈ 20.7 fs).",
    "inputs": "f = 4.836×10¹³ Hz",
    "formula": "1 / f"
  },
  {
    "id": "Q10",
    "statement": "The universal conversion factor between an energy gap (in eV) and a Zitterbewegung frequency is \\(2.418\\times10^{14}\\) Hz/eV.",
    "inputs": "Planck constant in eV·s, h = 2π ħ_eVs = 4.136×10⁻¹⁵ eV·s",
    "formula": "1 / (4.136×10⁻¹⁵)"
  }
]

## Script
```python
import math

# Helper to round a number to n significant figures and format as scientific string
def fmt_sig(x, n):
    if x == 0:
        return f"{0:.{n-1}e}"
    exponent = int(math.floor(math.log10(abs(x))))
    factor = 10**(n-1-exponent)
    rounded = round(x * factor) / factor
    return f"{rounded:.{n-1}e}"

# Expected values (as strings) and their significant-figure counts
expected = {
    "Q1": ("1.6023e-19", 5),
    "Q2": ("8.187e-14", 4),
    "Q3": ("5.111e5", 4),
    "Q4": ("1.5526e21", 5),
    "Q5": ("2.471e20", 4),
    "Q6": ("1.553e21", 4),
    "Q7": ("1.931e-13", 4),
    "Q8": ("4.836e13", 4),
    "Q9": ("2.0678e-14", 5),
    "Q10": ("2.418e14", 4),
}

# Physical constants
c = 2.998e8            # m/s
m_e = 9.109e-31        # kg
hbar_Js = 1.0546e-34   # J·s
hbar_eVs = 6.582e-16   # eV·s
pi = math.pi

# Computations
results = {}

# Q1: ratio of ħ values
results["Q1"] = hbar_Js / hbar_eVs

# Q2: electron rest energy (J)
results["Q2"] = m_e * c**2

# Q3: rest energy in eV
results["Q3"] = results["Q2"] / 1.602e-19

# Q4: rest‑frame angular frequency (rad/s)
results["Q4"] = 2 * results["Q2"] / hbar_Js

# Q5: ordinary frequency (Hz)
results["Q5"] = results["Q4"] / (2 * pi)

# Q6: angular frequency using eV units
E_meV = 0.5111e6      # eV
results["Q6"] = 2 * E_meV / hbar_eVs

# Q7: position‑amplitude scale (m)
results["Q7"] = hbar_Js / (2 * m_e * c)

# Q8: ZB frequency for Δ=0.1 eV
Delta = 0.1            # eV
results["Q8"] = (2 * Delta) / (2 * pi * hbar_eVs)

# Q9: period corresponding to Q8
results["Q9"] = 1 / results["Q8"]

# Q10: universal conversion factor Hz/eV
h = 2 * pi * hbar_eVs
results["Q10"] = 1 / h

# Verification and reporting
match_count = 0
total = len(expected)

for qid, (exp_str, sig) in expected.items():
    comp = results[qid]
    comp_str = fmt_sig(comp, sig)
    match = "yes" if comp_str == exp_str else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {qid}: computed={comp_str} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {total - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.6022e-19 expected=1.6023e-19 match=no
CLAIM Q2: computed=8.187e-14 expected=8.187e-14 match=yes
CLAIM Q3: computed=5.111e+05 expected=5.111e5 match=no
CLAIM Q4: computed=1.5527e+21 expected=1.5526e21 match=no
CLAIM Q5: computed=2.471e+20 expected=2.471e20 match=no
CLAIM Q6: computed=1.553e+21 expected=1.553e21 match=no
CLAIM Q7: computed=1.931e-13 expected=1.931e-13 match=yes
CLAIM Q8: computed=4.836e+13 expected=4.836e13 match=no
CLAIM Q9: computed=2.0678e-14 expected=2.0678e-14 match=yes
CLAIM Q10: computed=2.418e+14 expected=2.418e14 match=no
VERIFICATION SUMMARY: 10 claims, 3 match, 7 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.6022e-19 | 1.6023e-19 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 8.187e-14 | 8.187e-14 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 5.111e+05 | 5.111e5 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 1.5527e+21 | 1.5526e21 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | 2.471e+20 | 2.471e20 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 1.553e+21 | 1.553e21 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 1.931e-13 | 1.931e-13 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 4.836e+13 | 4.836e13 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 2.0678e-14 | 2.0678e-14 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 2.418e+14 | 2.418e14 | no | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 10.
