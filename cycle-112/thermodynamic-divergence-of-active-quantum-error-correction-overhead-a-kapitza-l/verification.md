# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Quadratic-overhead critical qubit count N_c = 390",
    "inputs": "P0=1e-10 W, alpha=1e-11 W, beta=4, G_K=1e-7 W/K, Delta_T_max=1e-2 K",
    "formula": "N_c = (beta*G_K*Delta_T_max - P0)/alpha"
  },
  {
    "id": "Q2",
    "statement": "Exponential-overhead critical qubit count N_c(exp) = 737.7758 (approx 738)",
    "inputs": "N_e=200, P0=1e-10 W, beta=4, G_K=1e-7 W/K, Delta_T_max=1e-2 K",
    "formula": "N_c_exp = N_e * ln(beta*G_K*Delta_T_max / P0)"
  },
  {
    "id": "Q3",
    "statement": "Sensitivity: N_c = 190 if Delta_T_max halved to 5e-3 K",
    "inputs": "P0=1e-10 W, alpha=1e-11 W, beta=4, G_K=1e-7 W/K, Delta_T_max=5e-3 K",
    "formula": "N_c = (beta*G_K*Delta_T_max - P0)/alpha"
  },
  {
    "id": "Q4",
    "statement": "Sensitivity: N_c = 3990 if G_K improves tenfold to 1e-6 W/K",
    "inputs": "P0=1e-10 W, alpha=1e-11 W, beta=4, G_K=1e-6 W/K, Delta_T_max=1e-2 K",
    "formula": "N_c = (beta*G_K*Delta_T_max - P0)/alpha"
  },
  {
    "id": "Q5",
    "statement": "Logical-qubit budget: 15 logical qubits at code distance d=5",
    "inputs": "N_c=390, d=5",
    "formula": "floor(N_c / d^2)"
  },
  {
    "id": "Q6",
    "statement": "Logical-qubit budget: 7 logical qubits at code distance d=7",
    "inputs": "N_c=390, d=7",
    "formula": "floor(N_c / d^2)"
  },
  {
    "id": "Q7",
    "statement": "Heat balance check at N=390: generated heat equals extractable heat, both 1.560e-6 W",
    "inputs": "P0=1e-10 W, alpha=1e-11 W, N=390, beta=4, G_K=1e-7 W/K, Delta_T_max=1e-2 K",
    "formula": "P_tot = P0*N + alpha*N^2 ; P_ext = beta*G_K*Delta_T_max*N"
  },
  {
    "id": "Q8",
    "statement": "Stability bound: maximum tolerable dissipation-temperature feedback coefficient is beta*G_K = 4e-7 W/K per qubit",
    "inputs": "beta=4, G_K=1e-7 W/K",
    "formula": "beta*G_K"
  }
]

## Script
```python
import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

# Q1
P0 = 1e-10; alpha = 1e-11; beta = 4; GK = 1e-7; dT = 1e-2
Nc = (beta * GK * dT - P0) / alpha
print(f"CLAIM Q1: computed={Nc} expected=390 match={'yes' if isclose(Nc, 390) else 'no'}")

# Q2
Ne = 200
Nc_exp = Ne * math.log(beta * GK * dT / P0)
print(f"CLAIM Q2: computed={Nc_exp} expected=737.7758 match={'yes' if isclose(Nc_exp, 737.7758) else 'no'}")

# Q3
dT_half = 5e-3
Nc3 = (beta * GK * dT_half - P0) / alpha
print(f"CLAIM Q3: computed={Nc3} expected=190 match={'yes' if isclose(Nc3, 190) else 'no'}")

# Q4
GK10 = 1e-6
Nc4 = (beta * GK10 * dT - P0) / alpha
print(f"CLAIM Q4: computed={Nc4} expected=3990 match={'yes' if isclose(Nc4, 3990) else 'no'}")

# Q5
Nc5 = math.floor(390 / 5**2)
print(f"CLAIM Q5: computed={Nc5} expected=15 match={'yes' if Nc5 == 15 else 'no'}")

# Q6
Nc6 = math.floor(390 / 7**2)
print(f"CLAIM Q6: computed={Nc6} expected=7 match={'yes' if Nc6 == 7 else 'no'}")

# Q7
N = 390
P_tot = P0 * N + alpha * N**2
P_ext = beta * GK * dT * N
print(f"CLAIM Q7: computed={P_tot} expected=1.560e-6 match={'yes' if isclose(P_tot, 1.560e-6) and isclose(P_ext, P_tot) else 'no'}")

# Q8
stab = beta * GK
print(f"CLAIM Q8: computed={stab} expected=4e-7 match={'yes' if isclose(stab, 4e-7) else 'no'}")

results = [Q1_ok := isclose(Nc, 390), isclose(Nc_exp, 737.7758), isclose(Nc3, 190),
           isclose(Nc4, 3990), Nc5 == 15, Nc6 == 7,
           isclose(P_tot, 1.560e-6) and isclose(P_ext, P_tot), isclose(stab, 4e-7)]
print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(results)} match, {len(results) - sum(results)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=390.00000000000006 expected=390 match=yes
CLAIM Q2: computed=737.7758908227872 expected=737.7758 match=yes
CLAIM Q3: computed=190.00000000000003 expected=190 match=yes
CLAIM Q4: computed=3990.0000000000005 expected=3990 match=yes
CLAIM Q5: computed=15 expected=15 match=yes
CLAIM Q6: computed=7 expected=7 match=yes
CLAIM Q7: computed=1.5599999999999999e-06 expected=1.560e-6 match=yes
CLAIM Q8: computed=4e-07 expected=4e-7 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
