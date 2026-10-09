# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Coherence after N=10^6 kicks is C = exp(-0.5) ≈ 0.606531",
    "inputs": "sigma_phi = 1e-3 rad, N = 1e6 kicks",
    "formula": "C_N = exp(-N*sigma_phi^2/2)"
  },
  {
    "id": "Q2",
    "statement": "1/e coherence time T2 = 200 s for sigma_phi = 1e-3 rad and Gamma_kick = 1e4 s^-1",
    "inputs": "sigma_phi = 1e-3 rad, Gamma_kick = 1e4 s^-1",
    "formula": "T2 = 2/(Gamma_kick * sigma_phi^2)"
  },
  {
    "id": "Q3",
    "statement": "Reducing kick rate tenfold to Gamma_kick' = 1e3 s^-1 gives T2' = 2000 s",
    "inputs": "sigma_phi = 1e-3 rad, Gamma_kick' = 1e3 s^-1",
    "formula": "T2' = 2/(Gamma_kick' * sigma_phi^2)"
  },
  {
    "id": "Q4",
    "statement": "40 MHz readout cycle period is 2.5e-8 s",
    "inputs": "f = 40e6 s^-1",
    "formula": "t_cycle = 1/f"
  },
  {
    "id": "Q5",
    "statement": "Ratio of 40 MHz cycle to Zeno crossover time is 2.5e7",
    "inputs": "t_cycle = 2.5e-8 s, t_Z = 1e-15 s",
    "formula": "ratio = t_cycle/t_Z"
  },
  {
    "id": "Q6",
    "statement": "For N1 = 1e5 modes with Gamma_k = 1e-10 s^-1, T2 = 1e5 s",
    "inputs": "N1 = 1e5, Gamma_k = 1e-10 s^-1",
    "formula": "T2 = 1/(N1*Gamma_k)"
  },
  {
    "id": "Q7",
    "statement": "For N2 = 1e9 modes with Gamma_k = 1e-10 s^-1, T2 = 10 s",
    "inputs": "N2 = 1e9, Gamma_k = 1e-10 s^-1",
    "formula": "T2 = 1/(N2*Gamma_k)"
  },
  {
    "id": "Q8",
    "statement": "Ratio of coherence times T2(1)/T2(2) = 1e4 = N2/N1",
    "inputs": "N1 = 1e5, N2 = 1e9",
    "formula": "ratio = N2/N1"
  }
]

## Script
```python
import math

claims = []

# Q1: C = exp(-N*sigma_phi^2/2), sigma_phi=1e-3, N=1e6
sigma_phi = 1e-3
N = 1e6
C = math.exp(-N * sigma_phi**2 / 2)
claims.append(("Q1", C, math.exp(-0.5)))

# Q2: T2 = 2/(Gamma_kick * sigma_phi^2), Gamma_kick=1e4
Gamma_kick = 1e4
T2 = 2 / (Gamma_kick * sigma_phi**2)
claims.append(("Q2", T2, 200.0))

# Q3: T2' = 2/(Gamma_kick' * sigma_phi^2), Gamma_kick'=1e3
Gamma_kick_p = 1e3
T2p = 2 / (Gamma_kick_p * sigma_phi**2)
claims.append(("Q3", T2p, 2000.0))

# Q4: t_cycle = 1/f, f=40e6
f = 40e6
t_cycle = 1 / f
claims.append(("Q4", t_cycle, 2.5e-8))

# Q5: ratio = t_cycle / t_Z, t_Z=1e-15
t_Z = 1e-15
ratio = t_cycle / t_Z
claims.append(("Q5", ratio, 2.5e7))

# Q6: T2 = 1/(N1*Gamma_k), N1=1e5, Gamma_k=1e-10
N1 = 1e5
Gamma_k = 1e-10
T2_1 = 1 / (N1 * Gamma_k)
claims.append(("Q6", T2_1, 1e5))

# Q7: T2 = 1/(N2*Gamma_k), N2=1e9
N2 = 1e9
T2_2 = 1 / (N2 * Gamma_k)
claims.append(("Q7", T2_2, 10.0))

# Q8: ratio = N2/N1
ratio_T = N2 / N1
claims.append(("Q8", ratio_T, 1e4))

match_count = 0
for cid, computed, expected in claims:
    match = math.isclose(computed, expected, rel_tol=1e-6)
    if match:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.6065306597126334 expected=0.6065306597126334 match=yes
CLAIM Q2: computed=200.0 expected=200.0 match=yes
CLAIM Q3: computed=2000.0 expected=2000.0 match=yes
CLAIM Q4: computed=2.5e-08 expected=2.5e-08 match=yes
CLAIM Q5: computed=24999999.999999996 expected=25000000.0 match=yes
CLAIM Q6: computed=99999.99999999999 expected=100000.0 match=yes
CLAIM Q7: computed=10.0 expected=10.0 match=yes
CLAIM Q8: computed=10000.0 expected=10000.0 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
