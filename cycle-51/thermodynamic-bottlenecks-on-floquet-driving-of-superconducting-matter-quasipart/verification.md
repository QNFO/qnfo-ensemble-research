# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Gap Delta_0 = 1.76 k_B T_c for aluminum with T_c = 1.2 K",
    "inputs": "k_B = 1.380649e-23 J/K, T_c = 1.2 K, ratio 1.76",
    "formula": "Delta_0 = 1.76 * k_B * T_c"
  },
  {
    "id": "Q2",
    "statement": "Pair-breaking frequency f_pb = 2 Delta_0 / h ≈ 88 GHz",
    "inputs": "Delta_0 = 2.91593e-23 J, h = 6.62607015e-34 J s",
    "formula": "f_pb = 2 * Delta_0 / h"
  },
  {
    "id": "Q3",
    "statement": "Poisoning-limited absorbed power P_abs_max ≈ 5.8e-19 W",
    "inputs": "epsilon_tol = 1e-3, tau_g = 1e-7 s, Delta_0 = 2.91593e-23 J",
    "formula": "P_abs_max = (epsilon_tol / tau_g) * 2 * Delta_0"
  },
  {
    "id": "Q4",
    "statement": "Quasiparticle generation rate Gamma_qp ≈ 1.72e10 s^-1 at 1 pW absorbed",
    "inputs": "P_abs = 1e-12 W, Delta_0 = 2.91593e-23 J",
    "formula": "Gamma_qp = P_abs / (2 * Delta_0)"
  },
  {
    "id": "Q5",
    "statement": "Steady-state quasiparticle density n_qp_ss ≈ 1.0e11 m^-3",
    "inputs": "Gamma_qp = 1.72e10 s^-1, tau_qp = 3e-4 s, V_c = 5e-5 m^3",
    "formula": "n_qp_ss = Gamma_qp * tau_qp / V_c"
  },
  {
    "id": "Q6",
    "statement": "Thermal quasiparticle density at 0.1 K ≈ 1.2e-21 m^-3",
    "inputs": "N_0 = 1.72e10 m^-3 J^-1, Delta_0 = 2.91593e-23 J, k_B = 1.380649e-23 J/K, T = 0.1 K",
    "formula": "n_qp_th = 2 * N_0 * sqrt(2 * pi * Delta_0 * k_B * T) * exp(-Delta_0 / (k_B * T))"
  },
  {
    "id": "Q7",
    "statement": "Ratio of driven to thermal quasiparticle density ≈ 9e31",
    "inputs": "n_qp_ss = 1.0e11 m^-3, n_qp_th = 1.2e-21 m^-3",
    "formula": "ratio = n_qp_ss / n_qp_th"
  },
  {
    "id": "Q8",
    "statement": "Admissible drive field E_max ≈ 14.1 V/m",
    "inputs": "P_alloc = 1e-6 W, sigma = 1e-4 S/m, A = 1e-4 m^2",
    "formula": "E_max = sqrt(2 * P_alloc / (sigma * A))"
  }
]

## Script
```python
import math

kB = 1.380649e-23
h = 6.62607015e-34
e = 1.602176634e-19

# Q1
Delta0 = 1.76 * kB * 1.2
print(f"CLAIM Q1: computed={Delta0:.6e} expected=2.91593e-23 match={math.isclose(Delta0, 2.91593e-23, rel_tol=1e-6)}")

# Q2
f_pb = 2 * Delta0 / h
print(f"CLAIM Q2: computed={f_pb:.6e} expected=8.8e10 match={math.isclose(f_pb, 8.8e10, rel_tol=1e-2)}")

# Q3
eps_tol = 1e-3
tau_g = 1e-7
P_abs_max = (eps_tol / tau_g) * 2 * Delta0
print(f"CLAIM Q3: computed={P_abs_max:.6e} expected=5.8e-19 match={math.isclose(P_abs_max, 5.8e-19, rel_tol=1e-2)}")

# Q4
P_abs = 1e-12
Gamma_qp = P_abs / (2 * Delta0)
print(f"CLAIM Q4: computed={Gamma_qp:.6e} expected=1.72e10 match={math.isclose(Gamma_qp, 1.72e10, rel_tol=1e-2)}")

# Q5
tau_qp = 3e-4
V_c = 5e-5
n_ss = Gamma_qp * tau_qp / V_c
print(f"CLAIM Q5: computed={n_ss:.6e} expected=1.0e11 match={math.isclose(n_ss, 1.0e11, rel_tol=1e-2)}")

# Q6
N0 = 1.72e10
T = 0.1
n_th = 2 * N0 * math.sqrt(2 * math.pi * Delta0 * kB * T) * math.exp(-Delta0 / (kB * T))
print(f"CLAIM Q6: computed={n_th:.6e} expected=1.2e-21 match={math.isclose(n_th, 1.2e-21, rel_tol=1e-2)}")

# Q7
ratio = n_ss / n_th
print(f"CLAIM Q7: computed={ratio:.6e} expected=9e31 match={math.isclose(ratio, 9e31, rel_tol=1e-1)}")

# Q8
P_alloc = 1e-6
sigma = 1e-4
A = 1e-4
E_max = math.sqrt(2 * P_alloc / (sigma * A))
print(f"CLAIM Q8: computed={E_max:.6e} expected=14.1 match={math.isclose(E_max, 14.1, rel_tol=1e-2)}")

results = [
    math.isclose(Delta0, 2.91593e-23, rel_tol=1e-6),
    math.isclose(f_pb, 8.8e10, rel_tol=1e-2),
    math.isclose(P_abs_max, 5.8e-19, rel_tol=1e-2),
    math.isclose(Gamma_qp, 1.72e10, rel_tol=1e-2),
    math.isclose(n_ss, 1.0e11, rel_tol=1e-2),
    math.isclose(n_th, 1.2e-21, rel_tol=1e-2),
    math.isclose(ratio, 9e31, rel_tol=1e-1),
    math.isclose(E_max, 14.1, rel_tol=1e-2),
]
m = sum(results)
print(f"VERIFICATION SUMMARY: {len(results)} claims, {m} match, {len(results)-m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=2.915931e-23 expected=2.91593e-23 match=True
CLAIM Q2: computed=8.801388e+10 expected=8.8e10 match=True
CLAIM Q3: computed=5.831861e-19 expected=5.8e-19 match=True
CLAIM Q4: computed=1.714718e+10 expected=1.72e10 match=True
CLAIM Q5: computed=1.028831e+11 expected=1.0e11 match=False
CLAIM Q6: computed=3.679418e-22 expected=1.2e-21 match=False
CLAIM Q7: computed=2.796179e+32 expected=9e31 match=False
CLAIM Q8: computed=1.414214e+01 expected=14.1 match=True
VERIFICATION SUMMARY: 8 claims, 5 match, 3 mismatch

[exit 0]
```
