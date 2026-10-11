# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Per-operation error rates epsilon_1, epsilon_2, epsilon_r",
    "inputs": "F1=0.9990, F2=0.9956, Fr=0.987",
    "formula": "epsilon = 1 - F"
  },
  {
    "id": "Q2",
    "statement": "Arithmetic mean fidelity Fbar approx 99.39%",
    "inputs": "F1=0.9990, F2=0.9956, Fr=0.987",
    "formula": "Fbar = (F1 + F2 + Fr)/3"
  },
  {
    "id": "Q3",
    "statement": "Three-step composite error Perr approx 1.8325%",
    "inputs": "F1=0.9990, F2=0.9956, Fr=0.987",
    "formula": "Perr = 1 - F1*F2*Fr"
  },
  {
    "id": "Q4",
    "statement": "Hilbert space dimension D105 = 2^105 approx 4.056e31",
    "inputs": "N=105",
    "formula": "D = 2^N"
  },
  {
    "id": "Q5",
    "statement": "Generic pure state parameter count 2^106 - 2 approx 8.113e31",
    "inputs": "N=105",
    "formula": "2*2^N - 2"
  },
  {
    "id": "Q6",
    "statement": "Parameters per qubit approx 7.7266e29",
    "inputs": "N=105",
    "formula": "(2^(N+1) - 2)/N"
  },
  {
    "id": "Q7",
    "statement": "Two-qubit serial budget n=157 at 50% aggregate fidelity",
    "inputs": "F2=0.9956, threshold=0.5",
    "formula": "n = floor(ln(0.5)/ln(F2))"
  },
  {
    "id": "Q8",
    "statement": "Two-qubit budget n=154 with one final readout",
    "inputs": "F2=0.9956, Fr=0.987, threshold=0.5",
    "formula": "n = floor(ln(0.5/Fr)/ln(F2))"
  }
]

## Script
```python
import math

F1 = 0.9990
F2 = 0.9956
Fr = 0.987
N = 105

# Q1
eps1 = 1 - F1
eps2 = 1 - F2
epsr = 1 - Fr
print(f"CLAIM Q1: computed=({eps1:.10g},{eps2:.10g},{epsr:.10g}) expected=(0.001,0.0044,0.013) match="
      f"{math.isclose(eps1,0.001,rel_tol=1e-6) and math.isclose(eps2,0.0044,rel_tol=1e-6) and math.isclose(epsr,0.013,rel_tol=1e-6)}")

# Q2
Fbar = (F1 + F2 + Fr) / 3
print(f"CLAIM Q2: computed={Fbar:.10g} expected=0.9939 match={math.isclose(Fbar,0.9939,rel_tol=1e-6)}")

# Q3
Perr = 1 - F1 * F2 * Fr
print(f"CLAIM Q3: computed={Perr:.10g} expected=0.0183254572 match={math.isclose(Perr,0.0183254572,rel_tol=1e-6)}")

# Q4
D105 = 2 ** 105
print(f"CLAIM Q4: computed={D105:.6e} expected=4.0564819e31 match={math.isclose(D105,4.0564819e31,rel_tol=1e-6)}")

# Q5
params = 2 ** 106 - 2
print(f"CLAIM Q5: computed={params:.6e} expected=8.1129638e31 match={math.isclose(params,8.1129638e31,rel_tol=1e-6)}")

# Q6
per_qubit = (2 ** 106 - 2) / 105
print(f"CLAIM Q6: computed={per_qubit:.6e} expected=7.7266e29 match={math.isclose(per_qubit,7.7266e29,rel_tol=1e-4)}")

# Q7
n7 = math.floor(math.log(0.5) / math.log(F2))
print(f"CLAIM Q7: computed={n7} expected=157 match={n7 == 157}")

# Q8
n8 = math.floor(math.log(0.5 / Fr) / math.log(F2))
print(f"CLAIM Q8: computed={n8} expected=154 match={n8 == 154}")

claims = 8
matches = sum([
    math.isclose(eps1,0.001,rel_tol=1e-6) and math.isclose(eps2,0.0044,rel_tol=1e-6) and math.isclose(epsr,0.013,rel_tol=1e-6),
    math.isclose(Fbar,0.9939,rel_tol=1e-6),
    math.isclose(Perr,0.0183254572,rel_tol=1e-6),
    math.isclose(D105,4.0564819e31,rel_tol=1e-6),
    math.isclose(params,8.1129638e31,rel_tol=1e-6),
    math.isclose(per_qubit,7.7266e29,rel_tol=1e-4),
    n7 == 157,
    n8 == 154,
])
print(f"VERIFICATION SUMMARY: {claims} claims, {matches} match, {claims - matches} mismatch")

```

## Execution output
```
CLAIM Q1: computed=(0.001,0.0044,0.013) expected=(0.001,0.0044,0.013) match=True
CLAIM Q2: computed=0.9938666667 expected=0.9939 match=False
CLAIM Q3: computed=0.0183254572 expected=0.0183254572 match=True
CLAIM Q4: computed=4.056482e+31 expected=4.0564819e31 match=True
CLAIM Q5: computed=8.112964e+31 expected=8.1129638e31 match=True
CLAIM Q6: computed=7.726632e+29 expected=7.7266e29 match=True
CLAIM Q7: computed=157 expected=157 match=True
CLAIM Q8: computed=154 expected=154 match=True
VERIFICATION SUMMARY: 8 claims, 7 match, 1 mismatch

[exit 0]
```
