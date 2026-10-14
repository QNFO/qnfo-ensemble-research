# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Thin-film screening length Lambda = 400 nm",
    "inputs": "lambda_L = 1.0e-7 m, d = 5.0e-8 m",
    "formula": "Lambda = 2*lambda_L^2/d"
  },
  {
    "id": "Q2",
    "statement": "Confinement parameter Gamma = 0.40 for R = 1.0 um",
    "inputs": "Lambda = 4.0e-7 m, R = 1.0e-6 m",
    "formula": "Gamma = Lambda/R"
  },
  {
    "id": "Q3",
    "statement": "Vortex-entry threshold H0 = 6.589e-4 T at R = 1.0 um",
    "inputs": "Phi_0 = 2.07e-15 Wb, R = 1.0e-6 m",
    "formula": "H0 = Phi_0/(pi*R^2)"
  },
  {
    "id": "Q4",
    "statement": "Threshold at R = 10 um is 6.589e-6 T (R^-2 scaling)",
    "inputs": "H0(1um) = 6.589e-4 T, radius factor 10",
    "formula": "H0(10um) = H0(1um)*10^-2"
  },
  {
    "id": "Q5",
    "statement": "Dome radius b = 62.996 um at mu0*Ha = 0.025 T",
    "inputs": "mu0*Ha = 0.025 T, B* = 0.100 T, gamma = 1, R = 100 um",
    "formula": "b/R = (mu0*Ha/B*)^(1/(gamma+2))"
  },
  {
    "id": "Q6",
    "statement": "Dome radius b = 79.370 um at mu0*Ha = 0.050 T",
    "inputs": "mu0*Ha = 0.050 T, B* = 0.100 T, gamma = 1, R = 100 um",
    "formula": "b/R = (mu0*Ha/B*)^(1/3)"
  },
  {
    "id": "Q7",
    "statement": "Dome mean induction B_d = 0.062996 T at 0.025 T",
    "inputs": "B* = 0.100 T, b/R = 0.62996",
    "formula": "B_d = B*(b/R)"
  },
  {
    "id": "Q8",
    "statement": "Vortex count N = 3.7942e5 at mu0*Ha = 0.025 T, R = 100 um",
    "inputs": "mu0*Ha = 0.025 T, R = 1.0e-4 m, Phi_0 = 2.07e-15 Wb",
    "formula": "N = mu0*Ha*pi*R^2/Phi_0"
  },
  {
    "id": "Q9",
    "statement": "Vortex count N = 7.588e5 at 0.050 T",
    "inputs": "N(0.025 T) = 3.7942e5",
    "formula": "N = 2*N(0.025 T) (linear in field)"
  },
  {
    "id": "Q10",
    "statement": "Vortex count N = 1.518e6 at 0.100 T",
    "inputs": "N(0.025 T) = 3.7942e5",
    "formula": "N = 4*N(0.025 T) (linear in field)"
  },
  {
    "id": "Q11",
    "statement": "Mixing frequency f0 = 10.0 MHz",
    "inputs": "f1 = 5.00e9 Hz, f2 = 4.99e9 Hz",
    "formula": "f0 = f1 - f2"
  },
  {
    "id": "Q12",
    "statement": "Coherence phase-space product omega*tau = 3.1416e6",
    "inputs": "f_q = 5.0e9 Hz, tau = 1.0e-4 s",
    "formula": "omega*tau = 2*pi*f_q*tau"
  },
  {
    "id": "Q13",
    "statement": "kappa_eff/kappa_c = 95.286 at eta = 0.05",
    "inputs": "kappa_s/kappa_c = 100, eta = 0.05, p_s = 1/(1+eta)",
    "formula": "kappa_eff/kappa_c = p_s*100 + (1-p_s)"
  },
  {
    "id": "Q14",
    "statement": "kappa_eff/kappa_c = 83.500 at eta = 0.20",
    "inputs": "kappa_s/kappa_c = 100, eta = 0.20, p_s = 1/(1+eta)",
    "formula": "kappa_eff/kappa_c = p_s*100 + (1-p_s)"
  },
  {
    "id": "Q15",
    "statement": "Unconfined reference kappa_eff/kappa_c = 50.5",
    "inputs": "kappa_s/kappa_c = 100, p_s = 0.5",
    "formula": "kappa_eff/kappa_c = 0.5*100 + 0.5"
  },
  {
    "id": "Q16",
    "statement": "Participation ratio 1.887 relative to unconfined case (eta = 0.05)",
    "inputs": "kappa_eff/kappa_c = 95.286, reference = 50.5",
    "formula": "ratio = 95.286/50.5"
  }
]

## Script
```python
import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: Lambda = 2*lambda_L^2/d
lam = 1.0e-7
d = 5.0e-8
Lam = 2 * lam**2 / d
results.append(("Q1", Lam, "400e-9", 2))

# Q2: Gamma = Lambda/R
Lam_c = 2 * lam**2 / d
R = 1.0e-6
Gam = Lam_c / R
results.append(("Q2", Gam, "0.40", 2))

# Q3: H0 = Phi0/(pi R^2)
Phi0 = 2.07e-15
R1 = 1.0e-6
H0 = Phi0 / (math.pi * R1**2)
results.append(("Q3", H0, "6.589e-4", 4))

# Q4: H0(10um) = H0(1um)*1e-2
H0_10 = Phi0 / (math.pi * (10.0e-6)**2)
results.append(("Q4", H0_10, "6.589e-6", 4))

# Q5: b/R = (mu0Ha/B*)^(1/3), b = 62.996 um
mu0Ha = 0.025
Bstar = 0.100
gamma = 1
Rd = 100.0e-6
b5 = Rd * (mu0Ha / Bstar)**(1.0 / (gamma + 2))
results.append(("Q5", b5 * 1e6, "62.996", 5))

# Q6: b at 0.050 T
mu0Ha6 = 0.050
b6 = Rd * (mu0Ha6 / Bstar)**(1.0 / (gamma + 2))
results.append(("Q6", b6 * 1e6, "79.370", 5))

# Q7: B_d = B*(b/R)
bR5 = (mu0Ha / Bstar)**(1.0 / (gamma + 2))
Bd = Bstar * bR5
results.append(("Q7", Bd, "0.062996", 6))

# Q8: N = mu0Ha*pi*R^2/Phi0
N8 = mu0Ha * math.pi * Rd**2 / Phi0
results.append(("Q8", N8, "3.7942e5", 5))

# Q9: N at 0.050 T = 2*N(0.025)
N9 = 2 * (0.025 * math.pi * Rd**2 / Phi0)
results.append(("Q9", N9, "7.588e5", 4))

# Q10: N at 0.100 T = 4*N(0.025)
N10 = 4 * (0.025 * math.pi * Rd**2 / Phi0)
results.append(("Q10", N10, "1.518e6", 4))

# Q11: f0 = f1 - f2
f1 = 5.00e9
f2 = 4.99e9
f0 = f1 - f2
results.append(("Q11", f0, "10.0e6", 3))

# Q12: omega*tau = 2*pi*fq*tau
fq = 5.0e9
tau = 1.0e-4
wt = 2 * math.pi * fq * tau
results.append(("Q12", wt, "3.1416e6", 5))

# Q13: kappa_eff/kappa_c at eta=0.05
kRatio = 100.0
eta13 = 0.05
ps13 = 1.0 / (1.0 + eta13)
k13 = ps13 * kRatio + (1 - ps13)
results.append(("Q13", k13, "95.286", 5))

# Q14: at eta=0.20
eta14 = 0.20
ps14 = 1.0 / (1.0 + eta14)
k14 = ps14 * kRatio + (1 - ps14)
results.append(("Q14", k14, "83.500", 5))

# Q15: unconfined reference
k15 = 0.5 * kRatio + 0.5
results.append(("Q15", k15, "50.5", 3))

# Q16: ratio = k13/k15
ratio16 = k13 / k15
results.append(("Q16", ratio16, "1.887", 4))

mismatch = 0
for cid, comp, exp_str, nsig in results:
    exp = float(exp_str)
    comp_r = sig(comp, nsig)
    match = "yes" if abs(comp_r - exp) <= abs(exp) * 10**(-nsig + 1) * 1.01 else "no"
    if match == "no":
        mismatch += 1
    print(f"CLAIM {cid}: computed={comp:.8g} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results)-mismatch} match, {mismatch} mismatch")

```

## Execution output
```
CLAIM Q1: computed=4e-07 expected=400e-9 match=yes
CLAIM Q2: computed=0.4 expected=0.40 match=yes
CLAIM Q3: computed=0.00065890146 expected=6.589e-4 match=yes
CLAIM Q4: computed=6.5890146e-06 expected=6.589e-6 match=yes
CLAIM Q5: computed=62.996052 expected=62.996 match=yes
CLAIM Q6: computed=79.370053 expected=79.370 match=yes
CLAIM Q7: computed=0.062996052 expected=0.062996 match=yes
CLAIM Q8: computed=379419.4 expected=3.7942e5 match=yes
CLAIM Q9: computed=758838.81 expected=7.588e5 match=yes
CLAIM Q10: computed=1517677.6 expected=1.518e6 match=yes
CLAIM Q11: computed=10000000 expected=10.0e6 match=yes
CLAIM Q12: computed=3141592.7 expected=3.1416e6 match=yes
CLAIM Q13: computed=95.285714 expected=95.286 match=yes
CLAIM Q14: computed=83.5 expected=83.500 match=yes
CLAIM Q15: computed=50.5 expected=50.5 match=yes
CLAIM Q16: computed=1.8868458 expected=1.887 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 4e-07 | 400e-9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 0.4 | 0.40 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.00065890146 | 6.589e-4 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 6.5890146e-06 | 6.589e-6 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 62.996052 | 62.996 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 79.370053 | 79.370 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 0.062996052 | 0.062996 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 379419.4 | 3.7942e5 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 758838.81 | 7.588e5 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 1517677.6 | 1.518e6 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 10000000 | 10.0e6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 3141592.7 | 3.1416e6 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q13 | 95.285714 | 95.286 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q14 | 83.5 | 83.500 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q15 | 50.5 | 50.5 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 1.8868458 | 1.887 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
