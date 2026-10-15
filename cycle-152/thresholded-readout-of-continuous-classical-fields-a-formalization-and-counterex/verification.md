# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Quadratic calculus detection probability at Theta=1, g=1: P1_Q = 0.3174",
    "inputs": "Phi(1)=0.8413",
    "formula": "P1_Q = 2*(1 - Phi(1))"
  },
  {
    "id": "Q2",
    "statement": "Linear calculus detection probability at Theta=1, g=1: P1_L = 0.1587",
    "inputs": "Phi(1)=0.8413",
    "formula": "P1_L = 1 - Phi(1)"
  },
  {
    "id": "Q3",
    "statement": "Difference between calculi: Delta P = 0.1587",
    "inputs": "P1_Q=0.3174, P1_L=0.1587",
    "formula": "Delta P = P1_Q - P1_L"
  },
  {
    "id": "Q4",
    "statement": "Ratio of detection probabilities approx 2.000",
    "inputs": "P1_Q=0.3174, P1_L=0.1587",
    "formula": "ratio = P1_Q / P1_L"
  },
  {
    "id": "Q5",
    "statement": "Slope-matched noise sigma_n = sqrt(2/pi) approx 0.7978846",
    "inputs": "sqrt(2)=1.4142136, sqrt(pi)=1.7724539",
    "formula": "sigma_n = sqrt(2)/sqrt(pi)"
  },
  {
    "id": "Q6",
    "statement": "Threshold model value at alpha=0: Phi(1.2533141) approx 0.8950",
    "inputs": "cos(0)=1, sigma_n=0.7978846, Phi(1.25)=0.8944, Phi(1.26)=0.8962",
    "formula": "z = 1/0.7978846; Phi(z) = Phi(1.25) + 0.33*(Phi(1.26)-Phi(1.25))"
  },
  {
    "id": "Q7",
    "statement": "Threshold model value at alpha=pi/6: approx 0.8611",
    "inputs": "cos(pi/6)=0.8660254, sigma_n=0.7978846, Phi(1.08)=0.8599, Phi(1.09)=0.8621",
    "formula": "z = 0.8660254/0.7978846; Phi(z) = Phi(1.08) + 0.54*(Phi(1.09)-Phi(1.08))"
  },
  {
    "id": "Q8",
    "statement": "Threshold model value at alpha=pi/4: approx 0.8123",
    "inputs": "cos(pi/4)=0.7071068, sigma_n=0.7978846, Phi(0.88)=0.8106, Phi(0.89)=0.8133",
    "formula": "z = 0.7071068/0.7978846; Phi(z) = Phi(0.88) + 0.62*(Phi(0.89)-Phi(0.88))"
  },
  {
    "id": "Q9",
    "statement": "Threshold model value at alpha=pi/3: approx 0.7346",
    "inputs": "cos(pi/3)=0.5, sigma_n=0.7978846, Phi(0.62)=0.7324, Phi(0.63)=0.7357",
    "formula": "z = 0.5/0.7978846; Phi(z) = Phi(0.62) + 0.67*(Phi(0.63)-Phi(0.62))"
  },
  {
    "id": "Q10",
    "statement": "Maximum deviation from Born rule: 0.1050 at alpha=0",
    "inputs": "Phi(1.2533141)=0.8950, P_QM(0)=1.0000",
    "formula": "Delta(0) = 0.8950 - 1.0000"
  },
  {
    "id": "Q11",
    "statement": "RMS deviation over five angles: 0.0602",
    "inputs": "deviations 0.1050, 0.0719, 0.0413, 0.0154, 0",
    "formula": "RMS = sqrt((0.1050^2 + 0.0719^2 + 0.0413^2 + 0.0154^2 + 0^2)/5)"
  },
  {
    "id": "Q12",
    "statement": "Quantum CHSH value |S| = 2*sqrt(2) approx 2.8284",
    "inputs": "sqrt(2)=1.4142136",
    "formula": "|S| = 2*sqrt(2)"
  },
  {
    "id": "Q13",
    "statement": "CHSH gap: 0.8284",
    "inputs": "2.8284271, 2",
    "formula": "gap = 2*sqrt(2) - 2"
  },
  {
    "id": "Q14",
    "statement": "Quadratic detection probability at Theta=4: 0.0456",
    "inputs": "Phi(2)=0.9772",
    "formula": "P1_Q = 2*(1 - Phi(2))"
  },
  {
    "id": "Q15",
    "statement": "Linear detection probability at Theta=4: 0.0228",
    "inputs": "Phi(2)=0.9772",
    "formula": "P1_L = 1 - Phi(2)"
  },
  {
    "id": "Q16",
    "statement": "Trials per calculus for 3-sigma discrimination: n approx 130 (129.6)",
    "inputs": "P1_Q=0.3174, P1_L=0.1587",
    "formula": "pbar = (P1_Q+P1_L)/2; se = sqrt(2*pbar*(1-pbar)/n); n = (3*sqrt(2*pbar*(1-pbar))/DeltaP)^2"
  }
]

## Script
```python
import math

def show(x):
    return f"{x:.10g}"

results = []

# Q6-Q9 interpolation fractions as stated in the paper
def phi_interp(z, lo, hi, phi_lo, phi_hi):
    frac = (z - lo) / (hi - lo)
    return phi_lo + frac * (phi_hi - phi_lo)

# Q1
pL = 1 - 0.8413
results.append(("Q1", pL, "0.1587"))

# Q2
pQ = 2 * (1 - 0.8413)
results.append(("Q2", pQ, "0.3174"))

# Q3
dP = pQ - pL
results.append(("Q3", dP, "0.1587"))

# Q4
ratio = pQ / pL
results.append(("Q4", ratio, "2.000"))

# Q5
sigma_n = 1.4142136 / 1.7724539
results.append(("Q5", sigma_n, "0.7978846"))

# Q6
z0 = 1 / sigma_n
phi0 = phi_interp(z0, 1.25, 1.26, 0.8944, 0.8962)
results.append(("Q6", phi0, "0.8950"))

# Q7
z1 = 0.8660254 / sigma_n
phi1 = phi_interp(z1, 1.08, 1.09, 0.8599, 0.8621)
results.append(("Q7", phi1, "0.8611"))

# Q8
z2 = 0.7071068 / sigma_n
phi2 = phi_interp(z2, 0.88, 0.89, 0.8106, 0.8133)
results.append(("Q8", phi2, "0.8123"))

# Q9
z3 = 0.5 / sigma_n
phi3 = phi_interp(z3, 0.62, 0.63, 0.7324, 0.7357)
results.append(("Q9", phi3, "0.7346"))

# Q10
dev0 = phi0 - 1.0000
results.append(("Q10", dev0, "-0.1050"))

# Q11
dev1 = phi1 - (1 + 0.8660254) / 2
dev2 = phi2 - (1 + 0.7071068) / 2
dev3 = phi3 - (1 + 0.5) / 2
rms = math.sqrt((dev0**2 + dev1**2 + dev2**2 + dev3**2 + 0.0**2) / 5)
results.append(("Q11", rms, "0.0602"))

# Q12
chsh = 2 * 1.4142136
results.append(("Q12", chsh, "2.8284"))

# Q13
gap = chsh - 2
results.append(("Q13", gap, "0.8284"))

# Q14
pQ4 = 2 * (1 - 0.9772)
results.append(("Q14", pQ4, "0.0456"))

# Q15
pL4 = 1 - 0.9772
results.append(("Q15", pL4, "0.0228"))

# Q16
pbar = (pQ + pL) / 2
n_req = (3 * math.sqrt(2 * pbar * (1 - pbar)) / dP) ** 2
results.append(("Q16", n_req, "129.6"))

match_count = 0
for cid, computed, expected in results:
    exp_val = float(expected)
    # round computed to the significant digits of the expected string
    sig = len(expected.replace("-", "").replace(".", "").lstrip("0"))
    rounded = float(f"%.{sig}g" % computed)
    match = "yes" if abs(rounded - exp_val) < 10 ** (-(sig)) * max(1, abs(exp_val)) * 1.0 else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={show(computed)} expected={expected} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.1587 expected=0.1587 match=yes
CLAIM Q2: computed=0.3174 expected=0.3174 match=yes
CLAIM Q3: computed=0.1587 expected=0.1587 match=yes
CLAIM Q4: computed=2 expected=2.000 match=yes
CLAIM Q5: computed=0.7978845599 expected=0.7978846 match=yes
CLAIM Q6: computed=0.894996545 expected=0.8950 match=yes
CLAIM Q7: computed=0.8610884132 expected=0.8611 match=yes
CLAIM Q8: computed=0.8122812765 expected=0.8123 match=yes
CLAIM Q9: computed=0.7345968329 expected=0.7346 match=yes
CLAIM Q10: computed=-0.105003455 expected=-0.1050 match=yes
CLAIM Q11: computed=0.06023200866 expected=0.0602 match=yes
CLAIM Q12: computed=2.8284272 expected=2.8284 match=yes
CLAIM Q13: computed=0.8284272 expected=0.8284 match=yes
CLAIM Q14: computed=0.0456 expected=0.0456 match=yes
CLAIM Q15: computed=0.0228 expected=0.0228 match=yes
CLAIM Q16: computed=129.6323251 expected=129.6 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.1587 | 0.1587 | yes | match | 4 significant digits (as printed, at least 3) |
| Q2 | 0.3174 | 0.3174 | yes | match | 4 significant digits (as printed, at least 3) |
| Q3 | 0.1587 | 0.1587 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 2 | 2.000 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 0.7978845599 | 0.7978846 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q6 | 0.894996545 | 0.8950 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 0.8610884132 | 0.8611 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 0.8122812765 | 0.8123 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 0.7345968329 | 0.7346 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | -0.105003455 | -0.1050 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 0.06023200866 | 0.0602 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 2.8284272 | 2.8284 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q13 | 0.8284272 | 0.8284 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q14 | 0.0456 | 0.0456 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 0.0228 | 0.0228 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 129.6323251 | 129.6 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
