# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The comparison‑strength parameter λ equals 0.058.",
    "inputs": "K = 0.2, η = 0.290",
    "formula": "λ = K * η"
  },
  {
    "id": "Q2",
    "statement": "The interaction scale S equals 7.5.",
    "inputs": "β = 5, σ = 1.5",
    "formula": "S = β * σ"
  },
  {
    "id": "Q3",
    "statement": "The dimensionless ratio r equals 7.73×10⁻³.",
    "inputs": "λ = 0.058, S = 7.5",
    "formula": "r = λ / S"
  },
  {
    "id": "Q4",
    "statement": "The predator‑search exponent α equals 1.30.",
    "inputs": "γ = 2.30",
    "formula": "α = γ - 1"
  },
  {
    "id": "Q5",
    "statement": "The total unordered comparisons for N=10 equal 523 776.",
    "inputs": "N = 10",
    "formula": "M(N) = 2^N * (2^N - 1) / 2"
  },
  {
    "id": "Q6",
    "statement": "The total unordered comparisons for N=20 equal approximately 5.50×10¹¹.",
    "inputs": "N = 20",
    "formula": "M(N) = 2^N * (2^N - 1) / 2"
  },
  {
    "id": "Q7",
    "statement": "The ratio of comparisons to states at N=10 equals 511.5.",
    "inputs": "N = 10",
    "formula": "(2^N - 1) / 2"
  },
  {
    "id": "Q8",
    "statement": "The product k_B T equals 4.141947×10⁻²¹ J.",
    "inputs": "k_B = 1.380649×10⁻²³ J·K⁻¹, T = 300 K",
    "formula": "k_B * T"
  },
  {
    "id": "Q9",
    "statement": "The Landauer energy per bit k_B T ln 2 equals 2.870979×10⁻²¹ J.",
    "inputs": "k_B T = 4.141947×10⁻²¹ J, ln 2 = 0.69314718056",
    "formula": "(k_B * T) * ln 2"
  },
  {
    "id": "Q10",
    "statement": "The minimal thermodynamic cost for full resolution of a 10‑bit state equals 2.87×10⁻²⁰ J.",
    "inputs": "N = 10, k_B T ln 2 = 2.870979×10⁻²¹ J",
    "formula": "E_min = N * (k_B * T * ln 2)"
  },
  {
    "id": "Q11",
    "statement": "The projected thermodynamic cost for exhaustive pairwise comparison at N=20 equals approximately 1.58×10⁻⁹ J.",
    "inputs": "M(20) ≈ 5.4976×10¹¹, k_B T ln 2 = 2.870979×10⁻²¹ J",
    "formula": "E_full = M(20) * (k_B * T * ln 2)"
  },
  {
    "id": "Q12",
    "statement": "The number of internal nodes in the binary tree representation for L=10 equals 2046.",
    "inputs": "L = 10",
    "formula": "2^{L+1} - 2"
  },
  {
    "id": "Q13",
    "statement": "The ultrametric fixed point contains 1023 internal nodes for L=10.",
    "inputs": "L = 10",
    "formula": "2^{L} - 1"
  }
]

## Script
```python
import math

def sig_from_expected(exp):
    # Split off exponent if present
    base = exp.split('e')[0]
    # Remove sign
    base = base.lstrip('+-')
    # Count digits, ignoring decimal point
    digits = [c for c in base if c.isdigit()]
    # Find first non‑zero digit
    first_nz = next((i for i, c in enumerate(digits) if c != '0'), len(digits))
    sig = len(digits) - first_nz
    # If all digits are zero, treat as one significant digit
    return max(sig, 1)

def fmt(val, exp):
    sig = sig_from_expected(exp)
    # Use general format with the required significant digits
    return format(val, f".{sig}g")

# Inputs
K = 0.2
eta = 0.290
beta = 5
sigma = 1.5
gamma = 2.30
N10 = 10
N20 = 20
kB = 1.380649e-23
T = 300.0
ln2 = 0.69314718056
L = 10

# Claims
claims = [
    ("Q1", K * eta, "0.058"),
    ("Q2", beta * sigma, "7.5"),
    ("Q3", (K * eta) / (beta * sigma), "7.73e-3"),
    ("Q4", gamma - 1, "1.30"),
    ("Q5", (2**N10) * (2**N10 - 1) / 2, "523776"),
    ("Q6", (2**N20) * (2**N20 - 1) / 2, "5.50e11"),
    ("Q7", (2**N10 - 1) / 2, "511.5"),
    ("Q8", kB * T, "4.141947e-21"),
    ("Q9", kB * T * ln2, "2.870979e-21"),
    ("Q10", N10 * kB * T * ln2, "2.87e-20"),
    ("Q11", ((2**N20) * (2**N20 - 1) / 2) * kB * T * ln2, "1.58e-9"),
    ("Q12", 2**(L+1) - 2, "2046"),
    ("Q13", 2**L - 1, "1023")
]

for cid, comp, exp in claims:
    comp_fmt = fmt(comp, exp)
    match = "yes" if comp_fmt == exp else "no"
    print(f"CLAIM {cid}: computed={comp_fmt} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, "
      f"{sum(1 for _,c,e in claims if fmt(c,e)==e)} match, "
      f"{sum(1 for _,c,e in claims if fmt(c,e)!=e)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.058 expected=0.058 match=yes
CLAIM Q2: computed=7.5 expected=7.5 match=yes
CLAIM Q3: computed=0.00773 expected=7.73e-3 match=no
CLAIM Q4: computed=1.3 expected=1.30 match=no
CLAIM Q5: computed=523776 expected=523776 match=yes
CLAIM Q6: computed=5.5e+11 expected=5.50e11 match=no
CLAIM Q7: computed=511.5 expected=511.5 match=yes
CLAIM Q8: computed=4.141947e-21 expected=4.141947e-21 match=yes
CLAIM Q9: computed=2.870979e-21 expected=2.870979e-21 match=yes
CLAIM Q10: computed=2.87e-20 expected=2.87e-20 match=yes
CLAIM Q11: computed=1.58e-09 expected=1.58e-9 match=no
CLAIM Q12: computed=2046 expected=2046 match=yes
CLAIM Q13: computed=1023 expected=1023 match=yes
VERIFICATION SUMMARY: 13 claims, 9 match, 4 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.058 | 0.058 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 7.5 | 7.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 0.00773 | 7.73e-3 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 1.3 | 1.30 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 523776 | 523776 | yes | match | 6 significant digits (as printed, at least 3) |
| Q6 | 5.5e+11 | 5.50e11 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 511.5 | 511.5 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 4.141947e-21 | 4.141947e-21 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q9 | 2.870979e-21 | 2.870979e-21 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q10 | 2.87e-20 | 2.87e-20 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 1.58e-09 | 1.58e-9 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 2046 | 2046 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 1023 | 1023 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 13.
