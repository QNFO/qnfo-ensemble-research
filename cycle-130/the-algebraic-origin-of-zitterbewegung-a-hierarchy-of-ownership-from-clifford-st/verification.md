# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Electron rest energy m_e c^2 = 8.187e-14 J",
    "inputs": "c = 2.998e8 m/s, m_e = 9.109e-31 kg",
    "formula": "m_e c^2 = m_e * c^2"
  },
  {
    "id": "Q2",
    "statement": "Electron rest energy = 0.5111 MeV",
    "inputs": "m_e c^2 = 8.187e-14 J, e = 1.602e-19 J/eV",
    "formula": "E = m_e c^2 / e"
  },
  {
    "id": "Q3",
    "statement": "Rest-frame ZB angular frequency omega_0 = 1.5526e21 rad/s",
    "inputs": "m_e c^2 = 8.187e-14 J, hbar = 1.0546e-34 J s",
    "formula": "omega_0 = 2 m_e c^2 / hbar"
  },
  {
    "id": "Q4",
    "statement": "Rest-frame ZB frequency f_0 = 2.471e20 Hz",
    "inputs": "omega_0 = 1.5526e21 rad/s",
    "formula": "f_0 = omega_0 / (2 pi)"
  },
  {
    "id": "Q5",
    "statement": "Rest-frame oscillation period T_0 = 4.047e-21 s",
    "inputs": "f_0 = 2.471e20 Hz",
    "formula": "T_0 = 1 / f_0"
  },
  {
    "id": "Q6",
    "statement": "Rest-frame position amplitude a_0 = 1.931e-13 m",
    "inputs": "hbar = 1.0546e-34 J s, m_e = 9.109e-31 kg, c = 2.998e8 m/s",
    "formula": "a_0 = hbar / (2 m_e c)"
  },
  {
    "id": "Q7",
    "statement": "Gapped Dirac material frequency f = 4.836e13 Hz for Delta = 0.1 eV",
    "inputs": "Delta = 0.1 eV, hbar_eV = 6.582e-16 eV s",
    "formula": "f = 2 Delta / (2 pi hbar_eV)"
  },
  {
    "id": "Q8",
    "statement": "Material oscillation period T = 2.068e-14 s (approx 20.7 fs)",
    "inputs": "f = 4.836e13 Hz",
    "formula": "T = 1 / f"
  },
  {
    "id": "Q9",
    "statement": "Universal scaling factor 2.418e14 Hz/eV",
    "inputs": "hbar_eV = 6.582e-16 eV s",
    "formula": "1 / (2 pi hbar_eV)"
  },
  {
    "id": "Q10",
    "statement": "Ratio of hbar values = 1.6023e-19 J/eV",
    "inputs": "hbar_J = 1.0546e-34 J s, hbar_eV = 6.582e-16 eV s",
    "formula": "hbar_J / hbar_eV"
  },
  {
    "id": "Q11",
    "statement": "Amplitude ratio to Bohr radius = 3.65e-3",
    "inputs": "a_0 = 1.931e-13 m, a_Bohr = 5.29e-11 m",
    "formula": "a_0 / a_Bohr"
  }
]

## Script
```python
import math

def sig(x, n=8):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

# Inputs (as stated in the paper)
c = 2.998e8          # m/s
m_e = 9.109e-31      # kg
hbar_J = 1.0546e-34  # J s
hbar_eV = 6.582e-16  # eV s
e = 1.602e-19        # J/eV
Delta = 0.1          # eV
a_Bohr = 5.29e-11    # m

# Q1: m_e c^2
q1 = m_e * c**2
# Q2: rest energy in MeV
q2 = (8.187e-14 / e) / 1e6
# Q3: omega_0 = 2 m_e c^2 / hbar
q3 = 2 * 8.187e-14 / hbar_J
# Q4: f_0 = omega_0 / (2 pi)
q4 = q3 / (2 * math.pi)
# Q5: T_0 = 1 / f_0
q5 = 1 / q4
# Q6: a_0 = hbar / (2 m_e c)
q6 = hbar_J / (2 * m_e * c)
# Q7: f = 2 Delta / (2 pi hbar_eV)
q7 = 2 * Delta / (2 * math.pi * hbar_eV)
# Q8: T = 1 / f
q8 = 1 / q7
# Q9: 1 / (2 pi hbar_eV)
q9 = 1 / (2 * math.pi * hbar_eV)
# Q10: hbar_J / hbar_eV
q10 = hbar_J / hbar_eV
# Q11: a_0 / a_Bohr
q11 = q6 / a_Bohr

claims = [
    ("Q1", q1, "8.187e-14"),
    ("Q2", q2, "0.5111"),
    ("Q3", q3, "1.5526e21"),
    ("Q4", q4, "2.471e20"),
    ("Q5", q5, "4.047e-21"),
    ("Q6", q6, "1.931e-13"),
    ("Q7", q7, "4.836e13"),
    ("Q8", q8, "2.068e-14"),
    ("Q9", q9, "2.418e14"),
    ("Q10", q10, "1.6023e-19"),
    ("Q11", q11, "3.65e-3"),
]

def match(computed, expected_str, stated_sig):
    exp_val = float(expected_str)
    comp_rounded = sig(computed, stated_sig)
    exp_rounded = sig(exp_val, stated_sig)
    return comp_rounded == exp_rounded

sig_digits = {"Q1": 4, "Q2": 4, "Q3": 5, "Q4": 4, "Q5": 4, "Q6": 4,
              "Q7": 4, "Q8": 4, "Q9": 4, "Q10": 5, "Q11": 3}

m_count = 0
for cid, comp, exp in claims:
    ok = match(comp, exp, sig_digits[cid])
    if ok:
        m_count += 1
    print(f"CLAIM {cid}: computed={comp:.8e} expected={exp} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {m_count} match, {len(claims) - m_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=8.18717284e-14 expected=8.187e-14 match=yes
CLAIM Q2: computed=5.11048689e-01 expected=0.5111 match=no
CLAIM Q3: computed=1.55262659e+21 expected=1.5526e21 match=yes
CLAIM Q4: computed=2.47108196e+20 expected=2.471e20 match=yes
CLAIM Q5: computed=4.04681032e-21 expected=4.047e-21 match=yes
CLAIM Q6: computed=1.93088070e-13 expected=1.931e-13 match=yes
CLAIM Q7: computed=4.83606634e+13 expected=4.836e13 match=yes
CLAIM Q8: computed=2.06779628e-14 expected=2.068e-14 match=yes
CLAIM Q9: computed=2.41803317e+14 expected=2.418e14 match=yes
CLAIM Q10: computed=1.60224856e-19 expected=1.6023e-19 match=no
CLAIM Q11: computed=3.65005803e-03 expected=3.65e-3 match=yes
VERIFICATION SUMMARY: 11 claims, 9 match, 2 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 8.18717284e-14 | 8.187e-14 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 5.11048689e-01 | 0.5111 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 1.55262659e+21 | 1.5526e21 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q4 | 2.47108196e+20 | 2.471e20 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 4.04681032e-21 | 4.047e-21 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 1.93088070e-13 | 1.931e-13 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 4.83606634e+13 | 4.836e13 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 2.06779628e-14 | 2.068e-14 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 2.41803317e+14 | 2.418e14 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 1.60224856e-19 | 1.6023e-19 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q11 | 3.65005803e-03 | 3.65e-3 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 11.
