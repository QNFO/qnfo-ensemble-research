# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Partition function Z of the thermal U(1) link at beta*g^2 = 0.5 equals 3.544908",
    "inputs": "Boltzmann exponent coefficient 0.25 per n^2 (from beta*g^2 = 0.5); Z = 1 + 2*sum_{n=1}^{inf} exp(-0.25*n^2)",
    "formula": "Z = 1 + 2*sum_{n=1}^{inf} exp(-0.25*n^2)"
  },
  {
    "id": "Q2",
    "statement": "State infidelity at truncation level n_max = 3 is 1.150e-2",
    "inputs": "Boltzmann coefficient 0.25; n_max = 3; Z = 3.544908; tail sum n>=4 of exp(-0.25*n^2) = 0.020374",
    "formula": "epsilon_tr(3) = 2 * sum_{n=4}^{inf} exp(-0.25*n^2) / Z"
  },
  {
    "id": "Q3",
    "statement": "State infidelity at truncation level n_max = 5 is 7.242e-5",
    "inputs": "Boltzmann coefficient 0.25; n_max = 5; Z = 3.544908; tail sum n>=6 of exp(-0.25*n^2) = 0.00012831",
    "formula": "epsilon_tr(5) = 2 * sum_{n=6}^{inf} exp(-0.25*n^2) / Z"
  },
  {
    "id": "Q4",
    "statement": "State infidelity at truncation level n_max = 7 is 6.44e-8",
    "inputs": "Boltzmann coefficient 0.25; n_max = 7; Z = 3.544908; tail sum n>=8 of exp(-0.25*n^2) = 1.14140e-7",
    "formula": "epsilon_tr(7) = 2 * sum_{n=8}^{inf} exp(-0.25*n^2) / Z"
  },
  {
    "id": "Q5",
    "statement": "Relative energy bias delta_E(n_max) = (sum_{|n|>n_max} n^2 exp(-0.25 n^2)) / (sum_{n=-inf}^{inf} n^2 exp(-0.25 n^2))",
    "inputs": "Boltzmann coefficient 0.25; truncation levels n_max in {3, 5, 7}",
    "formula": "delta_E(n_max) = (2 * sum_{n=n_max+1}^{inf} n^2 * exp(-0.25*n^2)) / (2 * sum_{n=1}^{inf} n^2 * exp(-0.25*n^2))"
  }
]

## Script
```python
import math

def boltz(n):
    return math.exp(-0.25 * n * n)

# Q1: partition function Z = 1 + 2*sum_{n=1}^{inf} exp(-0.25 n^2)
inner = sum(boltz(n) for n in range(1, 200))
Z = 1 + 2 * inner
Z_expected = 3.544908
match1 = math.isclose(Z, Z_expected, rel_tol=1e-6)
print(f"CLAIM Q1: computed={Z:.6f} expected={Z_expected} match={'yes' if match1 else 'no'}")

# Q2: epsilon_tr(3) = 2 * sum_{n=4}^{inf} exp(-0.25 n^2) / Z
tail3 = sum(boltz(n) for n in range(4, 200))
eps3 = 2 * tail3 / Z
eps3_expected = 1.150e-2
match2 = math.isclose(eps3, eps3_expected, rel_tol=1e-3)
print(f"CLAIM Q2: computed={eps3:.6e} expected={eps3_expected} match={'yes' if match2 else 'no'}")

# Q3: epsilon_tr(5) = 2 * sum_{n=6}^{inf} exp(-0.25 n^2) / Z
tail5 = sum(boltz(n) for n in range(6, 200))
eps5 = 2 * tail5 / Z
eps5_expected = 7.242e-5
match3 = math.isclose(eps5, eps5_expected, rel_tol=1e-3)
print(f"CLAIM Q3: computed={eps5:.6e} expected={eps5_expected} match={'yes' if match3 else 'no'}")

# Q4: epsilon_tr(7) = 2 * sum_{n=8}^{inf} exp(-0.25 n^2) / Z
tail7 = sum(boltz(n) for n in range(8, 200))
eps7 = 2 * tail7 / Z
eps7_expected = 6.44e-8
match4 = math.isclose(eps7, eps7_expected, rel_tol=1e-2)
print(f"CLAIM Q4: computed={eps7:.6e} expected={eps7_expected} match={'yes' if match4 else 'no'}")

# Q5: delta_E(n_max) = (2*sum_{n=n_max+1}^{inf} n^2 exp(-0.25 n^2)) / (2*sum_{n=1}^{inf} n^2 exp(-0.25 n^2))
denom = 2 * sum(n * n * boltz(n) for n in range(1, 200))
for n_max in (3, 5, 7):
    numer = 2 * sum(n * n * boltz(n) for n in range(n_max + 1, 200))
    dE = numer / denom
    print(f"CLAIM Q5(n_max={n_max}): computed={dE:.6e} expected=None match=n/a")

total = 5
matched = sum([match1, match2, match3, match4])
print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {total - matched} mismatch")

```

## Execution output
```
CLAIM Q1: computed=3.544908 expected=3.544908 match=yes
CLAIM Q2: computed=1.149503e-02 expected=0.0115 match=yes
CLAIM Q3: computed=7.239064e-05 expected=7.242e-05 match=yes
CLAIM Q4: computed=6.440470e-08 expected=6.44e-08 match=yes
CLAIM Q5(n_max=3): computed=9.760371e-02 expected=None match=n/a
CLAIM Q5(n_max=5): computed=1.321489e-03 expected=None match=n/a
CLAIM Q5(n_max=7): computed=2.068791e-06 expected=None match=n/a
VERIFICATION SUMMARY: 5 claims, 4 match, 1 mismatch

[exit 0]
```
