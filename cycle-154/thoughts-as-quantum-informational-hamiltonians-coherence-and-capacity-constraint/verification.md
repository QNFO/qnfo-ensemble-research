# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Thermal energy at 310 K: k_B T = 4.28001e-21 J = 26.71 meV",
    "inputs": "k_B = 1.380649e-23 J/K; T = 310 K; e = 1.602176634e-19 J/eV",
    "formula": "k_B T = k_B * T; in eV: k_B T / e"
  },
  {
    "id": "Q2",
    "statement": "Bare thermal decoherence rate Gamma_th = 4.058e13 s^-1",
    "inputs": "k_B T = 4.28001e-21 J; hbar = 1.0545718e-34 J·s",
    "formula": "Gamma_th = k_B T / hbar"
  },
  {
    "id": "Q3",
    "statement": "Bare thermal decoherence time tau_th = 2.46e-14 s",
    "inputs": "Gamma_th = 4.058e13 s^-1",
    "formula": "tau_th = 1 / Gamma_th"
  },
  {
    "id": "Q4",
    "statement": "Suppression factor for ms coherence S = 4.06e10",
    "inputs": "t_neuron = 1e-3 s; Gamma_th = 4.058e13 s^-1",
    "formula": "S = t_neuron * Gamma_th"
  },
  {
    "id": "Q5",
    "statement": "Coherent cycles at E = 0.2 eV: N_cyc = 1.19",
    "inputs": "E = 0.2 eV = 3.20435e-20 J; k_B T = 4.28001e-21 J",
    "formula": "N_cyc = E / (2*pi*k_B*T)"
  },
  {
    "id": "Q6",
    "statement": "Shannon-type capacity at E = 0.2 eV: C = 3.09 bits per mode",
    "inputs": "E = 0.2 eV; k_B T = 2.6712e-2 eV",
    "formula": "C = log2(1 + E/(k_B T))"
  },
  {
    "id": "Q7",
    "statement": "Dimension bound at d = 2: log2 d = 1 bit",
    "inputs": "d = 2",
    "formula": "log2(d)"
  },
  {
    "id": "Q8",
    "statement": "Coherent cycles at E = 10 eV: N_cyc = 59.6",
    "inputs": "E = 10 eV = 1.60218e-18 J; k_B T = 4.28001e-21 J",
    "formula": "N_cyc = E / (2*pi*k_B*T)"
  },
  {
    "id": "Q9",
    "statement": "Minimum transition energy for one cycle E_min = 0.168 eV",
    "inputs": "k_B T = 4.28001e-21 J; e = 1.602176634e-19 J/eV",
    "formula": "E_min = 2*pi*k_B*T / e"
  },
  {
    "id": "Q10",
    "statement": "Translation cost at alpha_r = 1e-4: R = 0.246 eV",
    "inputs": "k_B T = 4.28001e-21 J; alpha_r = 1e-4; e = 1.602176634e-19 J/eV",
    "formula": "R = k_B T * ln(1/alpha_r) / e"
  },
  {
    "id": "Q11",
    "statement": "Ratio of translation cost to receptor energy R/E = 1.23",
    "inputs": "R = 0.246 eV; E = 0.2 eV",
    "formula": "R / E"
  },
  {
    "id": "Q12",
    "statement": "Required E for 1e6 cycles: 1.68e5 eV (projection)",
    "inputs": "k_B T = 4.28001e-21 J; N = 1e6; e = 1.602176634e-19 J/eV",
    "formula": "E = 2*pi*k_B*T*N / e"
  },
  {
    "id": "Q13",
    "statement": "Thermal decoherence rate at 273 K falls by 12% relative to 310 K",
    "inputs": "T1 = 310 K; T2 = 273 K",
    "formula": "1 - T2/T1"
  }
]

## Script
```python
import math

kB = 1.380649e-23
T = 310.0
e = 1.602176634e-19
hbar = 1.0545718e-34

def report(cid, computed, expected, sig):
    if expected is None:
        match = "n/a"
    else:
        match = "yes" if float(f"%.{sig}g" % computed) == float(expected) else "no"
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected} match={match}")

kBT = kB * T
report("Q1", kBT, "4.28001e-21", 6)
kBT_eV = kBT / e
print(f"CLAIM Q1b (kBT in eV): computed={kBT_eV*1000:.8g} expected=26.71 match=" +
      str("yes" if float(f"%.4g" % (kBT_eV*1000)) == 26.71 else "no"))

Gamma = kBT / hbar
report("Q2", Gamma, "4.058e13", 4)

tau = 1 / Gamma
report("Q3", tau, "2.46e-14", 3)

S = 1e-3 * Gamma
report("Q4", S, "4.06e10", 3)

E02 = 0.2 * e
N02 = E02 / (2 * math.pi * kBT)
report("Q5", N02, "1.19", 3)

kBT_eV2 = 2.6712e-2
C = math.log2(1 + 0.2 / kBT_eV2)
report("Q6", C, "3.09", 3)

report("Q7", math.log2(2), "1", 1)

E10 = 10 * e
N10 = E10 / (2 * math.pi * kBT)
report("Q8", N10, "59.6", 3)

Emin = 2 * math.pi * kBT / e
report("Q9", Emin, "0.168", 3)

R = kBT * math.log(1 / 1e-4) / e
report("Q10", R, "0.246", 3)

ratio = 0.246 / 0.2
report("Q11", ratio, "1.23", 3)

Eproj = 2 * math.pi * kBT * 1e6 / e
report("Q12", Eproj, "1.68e5", 3)

fall = 1 - 273.0 / 310.0
report("Q13", fall, "0.12", 1)

print("VERIFICATION SUMMARY: 13 claims, " + "M match, K mismatch")

```

## Execution output
```
CLAIM Q1: computed=4.2800119e-21 expected=4.28001e-21 match=yes
CLAIM Q1b (kBT in eV): computed=26.713733 expected=26.71 match=yes
CLAIM Q2: computed=4.0585306e+13 expected=4.058e13 match=no
CLAIM Q3: computed=2.463946e-14 expected=2.46e-14 match=yes
CLAIM Q4: computed=4.0585306e+10 expected=4.06e10 match=yes
CLAIM Q5: computed=1.191559 expected=1.19 match=yes
CLAIM Q6: computed=3.0853009 expected=3.09 match=yes
CLAIM Q7: computed=1 expected=1 match=yes
CLAIM Q8: computed=59.577949 expected=59.6 match=yes
CLAIM Q9: computed=0.16784734 expected=0.168 match=yes
CLAIM Q10: computed=0.24604257 expected=0.246 match=yes
CLAIM Q11: computed=1.23 expected=1.23 match=yes
CLAIM Q12: computed=167847.34 expected=1.68e5 match=yes
CLAIM Q13: computed=0.11935484 expected=0.12 match=no
VERIFICATION SUMMARY: 13 claims, M match, K mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 4.2800119e-21 | 4.28001e-21 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q2 | 4.0585306e+13 | 4.058e13 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 2.463946e-14 | 2.46e-14 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 4.0585306e+10 | 4.06e10 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 1.191559 | 1.19 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 3.0853009 | 3.09 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 59.577949 | 59.6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 0.16784734 | 0.168 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 0.24604257 | 0.246 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 1.23 | 1.23 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 167847.34 | 1.68e5 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 0.11935484 | 0.12 | no | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 13.
