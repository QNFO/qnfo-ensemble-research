# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Maximum angular frequency omega_max = 2v/a = 3.710e43 s^-1 for a = 1.616e-35 m and v = 2.998e8 m/s",
    "inputs": "v = 2.998e8 m/s; a = 1.616e-35 m",
    "formula": "omega_max = 2*v/a"
  },
  {
    "id": "Q2",
    "statement": "Channel bandwidth B = omega_max/(2*pi) = 5.905e42 Hz",
    "inputs": "omega_max = 3.710e43 s^-1",
    "formula": "B = omega_max/(2*pi)"
  },
  {
    "id": "Q3",
    "statement": "Suppression at 10*omega_c: S = 1/101 = 9.901e-3",
    "inputs": "omega/omega_c = 10",
    "formula": "S = 1/(1+(omega/omega_c)^2)"
  },
  {
    "id": "Q4",
    "statement": "Suppression at 100*omega_c: S = 1/10001 = 9.999e-5",
    "inputs": "omega/omega_c = 100",
    "formula": "S = 1/(1+(omega/omega_c)^2)"
  },
  {
    "id": "Q5",
    "statement": "Decade suppression ratio S(10 wc)/S(100 wc) = 99.02",
    "inputs": "S(10 wc) = 1/101; S(100 wc) = 1/10001",
    "formula": "ratio = (1/101)/(1/10001)"
  },
  {
    "id": "Q6",
    "statement": "Baseline latency tau_0 = L/v = 3.336e-9 s for L = 1 m, v = 2.998e8 m/s",
    "inputs": "L = 1 m; v = 2.998e8 m/s",
    "formula": "tau_0 = L/v"
  },
  {
    "id": "Q7",
    "statement": "Congested latency tau = 3.339e-9 s at rho/rho_c = 1e-3",
    "inputs": "tau_0 = 3.336e-9 s; rho/rho_c = 1e-3",
    "formula": "tau = tau_0*(1+rho/rho_c)"
  },
  {
    "id": "Q8",
    "statement": "Excess delay Delta_tau = 3.336e-12 s per metre at rho/rho_c = 1e-3",
    "inputs": "tau_0 = 3.336e-9 s; rho/rho_c = 1e-3",
    "formula": "Delta_tau = tau_0*(rho/rho_c)"
  },
  {
    "id": "Q9",
    "statement": "Device-scale cutoff frequency f_c = c/(2*pi*L) = 4.775e10 Hz for L = 1.0e-3 m",
    "inputs": "c = 3.00e8 m/s; L = 1.0e-3 m",
    "formula": "f_c = c/(2*pi*L)"
  },
  {
    "id": "Q10",
    "statement": "Equivalent energy E_c = h*f_c = 3.164e-23 J",
    "inputs": "h = 6.626e-34 J s; f_c = 4.775e10 Hz",
    "formula": "E_c = h*f_c"
  },
  {
    "id": "Q11",
    "statement": "Equivalent energy in eV: E_c = 1.975e-4 eV",
    "inputs": "E_c = 3.164e-23 J; 1 eV = 1.602e-19 J",
    "formula": "E_c_eV = E_c/1.602e-19"
  }
]

## Script
```python
import math

def sig(x, n):
    if x == 0:
        return 0.0
    from math import floor, log10
    d = n - 1 - floor(log10(abs(x)))
    return round(x, d)

results = []

# Q1: omega_max = 2*v/a
v = 2.998e8
a = 1.616e-35
omega_max = 2 * v / a
results.append(("Q1", omega_max, "3.710e43"))

# Q2: B = omega_max/(2*pi)
B = omega_max / (2 * math.pi)
results.append(("Q2", B, "5.905e42"))

# Q3: S(10 wc) = 1/(1+10^2)
S10 = 1 / (1 + 10**2)
results.append(("Q3", S10, "9.901e-3"))

# Q4: S(100 wc) = 1/(1+100^2)
S100 = 1 / (1 + 100**2)
results.append(("Q4", S100, "9.999e-5"))

# Q5: ratio = S10/S100
ratio = S10 / S100
results.append(("Q5", ratio, "99.02"))

# Q6: tau_0 = L/v
L = 1.0
tau0 = L / v
results.append(("Q6", tau0, "3.336e-9"))

# Q7: tau = tau0*(1+rho/rho_c)
rho = 1e-3
tau = tau0 * (1 + rho)
results.append(("Q7", tau, "3.339e-9"))

# Q8: Delta_tau = tau0 * rho
dtau = tau0 * rho
results.append(("Q8", dtau, "3.336e-12"))

# Q9: f_c = c/(2*pi*L)
c = 3.00e8
Ld = 1.0e-3
fc = c / (2 * math.pi * Ld)
results.append(("Q9", fc, "4.775e10"))

# Q10: E_c = h*f_c
h = 6.626e-34
Ec = h * fc
results.append(("Q10", Ec, "3.164e-23"))

# Q11: E_c in eV
eV = 1.602e-19
Ec_eV = Ec / eV
results.append(("Q11", Ec_eV, "1.975e-4"))

match_count = 0
for cid, computed, expected_str in results:
    expected = float(expected_str)
    # number of significant digits in the paper's stated value
    digits = len(expected_str.split("e")[0].replace(".", "").lstrip("0"))
    comp_rounded = sig(computed, digits)
    match = "yes" if abs(comp_rounded - expected) <= expected * 10**(-(digits)) / 2 or comp_rounded == expected else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={computed:.8e} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results)-match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=3.71039604e+43 expected=3.710e43 match=yes
CLAIM Q2: computed=5.90527871e+42 expected=5.905e42 match=yes
CLAIM Q3: computed=9.90099010e-03 expected=9.901e-3 match=yes
CLAIM Q4: computed=9.99900010e-05 expected=9.999e-5 match=yes
CLAIM Q5: computed=9.90198020e+01 expected=99.02 match=yes
CLAIM Q6: computed=3.33555704e-09 expected=3.336e-9 match=yes
CLAIM Q7: computed=3.33889260e-09 expected=3.339e-9 match=yes
CLAIM Q8: computed=3.33555704e-12 expected=3.336e-12 match=yes
CLAIM Q9: computed=4.77464829e+10 expected=4.775e10 match=yes
CLAIM Q10: computed=3.16368196e-23 expected=3.164e-23 match=yes
CLAIM Q11: computed=1.97483268e-04 expected=1.975e-4 match=yes
VERIFICATION SUMMARY: 11 claims, 11 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 3.71039604e+43 | 3.710e43 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 5.90527871e+42 | 5.905e42 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 9.90099010e-03 | 9.901e-3 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 9.99900010e-05 | 9.999e-5 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 9.90198020e+01 | 99.02 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 3.33555704e-09 | 3.336e-9 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 3.33889260e-09 | 3.339e-9 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 3.33555704e-12 | 3.336e-12 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 4.77464829e+10 | 4.775e10 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 3.16368196e-23 | 3.164e-23 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 1.97483268e-04 | 1.975e-4 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 11.
