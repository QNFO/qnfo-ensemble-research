# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Wall thermal conductance G_th = kA/d = 4.0 W/K for the macroscopic wall",
    "inputs": "k=0.04 W/m/K, A=10 m^2, d=0.1 m",
    "formula": "G_th = k*A/d"
  },
  {
    "id": "Q2",
    "statement": "Macroscopic wall dissipates P = 1.20e2 W",
    "inputs": "G_th=4.0 W/K, DeltaT=30 K",
    "formula": "P = G_th * DeltaT"
  },
  {
    "id": "Q3",
    "statement": "Wall heat capacity C = 45000 J/K",
    "inputs": "m=50 kg, c=900 J/kg/K",
    "formula": "C = m*c"
  },
  {
    "id": "Q4",
    "statement": "Stored thermal energy Delta E = 1.35e6 J",
    "inputs": "C=45000 J/K, DeltaT=30 K",
    "formula": "DeltaE = C*DeltaT"
  },
  {
    "id": "Q5",
    "statement": "Characteristic coherence time tau = 11250 s = 3.125 h (approx 3.13 h)",
    "inputs": "DeltaE=1.35e6 J, P=120.0 W",
    "formula": "tau = DeltaE/P"
  },
  {
    "id": "Q6",
    "statement": "Sensitivity: halving k to 0.02 W/m/K gives P = 60.0 W and tau = 22500 s = 6.25 h",
    "inputs": "k=0.02 W/m/K, A=10 m^2, DeltaT=30 K, d=0.1 m, DeltaE=1.35e6 J",
    "formula": "P = k*A*DeltaT/d; tau = DeltaE/P"
  },
  {
    "id": "Q7",
    "statement": "Cryogenic wall conductance G_th = 1.0e-7 W/K",
    "inputs": "k=1.0e-4 W/m/K, A=1.0e-6 m^2, d=1.0e-3 m",
    "formula": "G_th = k*A/d"
  },
  {
    "id": "Q8",
    "statement": "Cryogenic wall power P_wall = 1.0e-10 W",
    "inputs": "G_th=1.0e-7 W/K, DeltaT=1.0e-3 K",
    "formula": "P_wall = G_th*DeltaT"
  }
]

## Script
```python
import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: G_th = k*A/d = 4.0 W/K
k, A, d = 0.04, 10.0, 0.1
G_th = k * A / d
results.append(("Q1", G_th, 4.0))

# Q2: P = G_th * DeltaT = 120.0 W
DeltaT = 30.0
P = G_th * DeltaT
results.append(("Q2", P, 120.0))

# Q3: C = m*c = 45000 J/K
m, c = 50.0, 900.0
C = m * c
results.append(("Q3", C, 45000.0))

# Q4: DeltaE = C * DeltaT = 1.35e6 J
DeltaE = C * DeltaT
results.append(("Q4", DeltaE, 1.35e6))

# Q5: tau = DeltaE / P = 11250 s
tau = DeltaE / P
results.append(("Q5", tau, 11250.0))

# Q6: halving k -> P = 60.0 W, tau = 22500 s
k2 = 0.02
P2 = k2 * A * DeltaT / d
tau2 = DeltaE / P2
results.append(("Q6a", P2, 60.0))
results.append(("Q6b", tau2, 22500.0))

# Q7: cryogenic G_th = 1.0e-7 W/K
k_c, A_c, d_c = 1.0e-4, 1.0e-6, 1.0e-3
G_c = k_c * A_c / d_c
results.append(("Q7", G_c, 1.0e-7))

# Q8: P_wall = G_c * DeltaT_c = 1.0e-10 W
DeltaT_c = 1.0e-3
P_wall = G_c * DeltaT_c
results.append(("Q8", P_wall, 1.0e-10))

n_match = 0
for cid, computed, expected in results:
    match = isclose(computed, expected)
    if match:
        n_match += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

total = len(results)
print(f"VERIFICATION SUMMARY: {total} claims, {n_match} match, {total - n_match} mismatch")

```

## Execution output
```
CLAIM Q1: computed=4.0 expected=4.0 match=yes
CLAIM Q2: computed=120.0 expected=120.0 match=yes
CLAIM Q3: computed=45000.0 expected=45000.0 match=yes
CLAIM Q4: computed=1350000.0 expected=1350000.0 match=yes
CLAIM Q5: computed=11250.0 expected=11250.0 match=yes
CLAIM Q6a: computed=60.0 expected=60.0 match=yes
CLAIM Q6b: computed=22500.0 expected=22500.0 match=yes
CLAIM Q7: computed=1e-07 expected=1e-07 match=yes
CLAIM Q8: computed=1e-10 expected=1e-10 match=yes
VERIFICATION SUMMARY: 9 claims, 9 match, 0 mismatch

[exit 0]
```
