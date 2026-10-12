# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Deformation-space size N_def(L) = 2^((4^(L+1)-4)/3); at L=3, N_def(3) = 2^84 ≈ 1.93e25",
    "inputs": "L=3",
    "formula": "N_def(L) = 2^((4^(L+1)-4)/3)"
  },
  {
    "id": "Q2",
    "statement": "N_def(2) = 2^20 = 1,048,576",
    "inputs": "L=2",
    "formula": "N_def(L) = 2^((4^(L+1)-4)/3)"
  },
  {
    "id": "Q3",
    "statement": "N_def(4) = 2^340 ≈ 2.24e102",
    "inputs": "L=4",
    "formula": "N_def(L) = 2^((4^(L+1)-4)/3)"
  },
  {
    "id": "Q4",
    "statement": "Physical qubits n_L = 4^L; at L=3, n_3 = 64",
    "inputs": "L=3",
    "formula": "n_L = 4^L"
  },
  {
    "id": "Q5",
    "statement": "Distance d_L = 2^L; at L=3, d_3 = 8",
    "inputs": "L=3",
    "formula": "d_L = 2^L"
  },
  {
    "id": "Q6",
    "statement": "Rate r_L = 4^(-L); at L=3, r_3 ≈ 1.5625e-2",
    "inputs": "L=3",
    "formula": "r_L = 4^(-L)"
  },
  {
    "id": "Q7",
    "statement": "Projected total logical error rate at L=2, eta=10, p0=1e-3: p_tot = 2.160216e-6",
    "inputs": "alpha=6, p0=1e-3, eta=10, L=2",
    "formula": "p_tot^(L) = alpha^(2^L - 1) * (p0)^(2^L) + alpha^(2^L - 1) * (eta*p0)^(2^L)"
  },
  {
    "id": "Q8",
    "statement": "Z share of total at L=2 exceeds 99.99%",
    "inputs": "p_X^(2)=2.16e-10, p_Z^(2)=2.16e-6",
    "formula": "p_Z/(p_X+p_Z)"
  },
  {
    "id": "Q9",
    "statement": "Skew ratio eta^(2^L): 1e2, 1e4, 1e8 at L=1,2,3 with eta=10",
    "inputs": "eta=10, L=1,2,3",
    "formula": "eta^(2^L)"
  },
  {
    "id": "Q10",
    "statement": "Greedy evaluation count G(3) = 336",
    "inputs": "L=3, 16 evaluations per block",
    "formula": "G(L) = 16*(4^L - 1)/3"
  },
  {
    "id": "Q11",
    "statement": "Reduction factor N_def(3)/G(3) = 2^80/21 ≈ 5.7568e22",
    "inputs": "N_def(3)=2^84, G(3)=336",
    "formula": "2^84 / 336"
  },
  {
    "id": "Q12",
    "statement": "Exhaustive sweep time at L=2 ≈ 1.05 s at R=1e6 evaluations/s",
    "inputs": "N_def(2)=1,048,576, R=1e6",
    "formula": "N_def(2)/R"
  },
  {
    "id": "Q13",
    "statement": "Exhaustive sweep time at L=3 ≈ 1.93e19 s ≈ 6.13e11 years",
    "inputs": "N_def(3)=2^84, R=1e6, 1 year=3.156e7 s",
    "formula": "N_def(3)/(R*3.156e7)"
  },
  {
    "id": "Q14",
    "statement": "Ratio N_def(3)/N_def(2) = 2^64 ≈ 1.8e19",
    "inputs": "L=3, L=2",
    "formula": "2^((4^4-4)/3 - (4^3-4)/3) = 2^64"
  },
  {
    "id": "Q15",
    "statement": "Projected total at L=3 ≈ 2.79936e-11",
    "inputs": "alpha=6, p0=1e-3, eta=10, L=3",
    "formula": "alpha^(2^3-1) * (eta*p0)^(2^3)"
  }
]

## Script
```python
import math

def sig(x, n=8):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: N_def(3) = 2^((4^4-4)/3) = 2^84
Nd3 = 2 ** ((4 ** (3 + 1) - 4) // 3)
computed = Nd3
expected = "1.93e25"
comp_sig = sig(computed, 3)
match = "yes" if abs(comp_sig - 1.93e25) / 1.93e25 < 0.005 else "no"
results.append(("Q1", computed, expected, match))

# Q2: N_def(2) = 2^20
Nd2 = 2 ** ((4 ** 3 - 4) // 3)
computed = Nd2
expected = "1048576"
match = "yes" if computed == 1048576 else "no"
results.append(("Q2", computed, expected, match))

# Q3: N_def(4) = 2^340
Nd4 = 2.0 ** ((4 ** 5 - 4) // 3)
computed = Nd4
expected = "2.24e102"
comp_sig = sig(computed, 3)
match = "yes" if abs(comp_sig - 2.24e102) / 2.24e102 < 0.005 else "no"
results.append(("Q3", computed, expected, match))

# Q4: n_3 = 4^3
computed = 4 ** 3
expected = "64"
match = "yes" if computed == 64 else "no"
results.append(("Q4", computed, expected, match))

# Q5: d_3 = 2^3
computed = 2 ** 3
expected = "8"
match = "yes" if computed == 8 else "no"
results.append(("Q5", computed, expected, match))

# Q6: r_3 = 4^-3
computed = 4.0 ** (-3)
expected = "0.015625"
match = "yes" if computed == 0.015625 else "no"
results.append(("Q6", computed, expected, match))

# Q7: p_tot at L=2, alpha=6, p0=1e-3, eta=10
alpha, p0, eta, L = 6.0, 1e-3, 10.0, 2
pX = alpha ** (2 ** L - 1) * p0 ** (2 ** L)
pZ = alpha ** (2 ** L - 1) * (eta * p0) ** (2 ** L)
computed = pX + pZ
expected = "2.160216e-6"
match = "yes" if abs(computed - 2.160216e-6) < 1e-15 else "no"
results.append(("Q7", computed, expected, match))

# Q8: Z share at L=2
computed = pZ / (pX + pZ)
expected = "0.9999 (share > 99.99%)"
match = "yes" if computed > 0.9999 else "no"
results.append(("Q8", computed, expected, match))

# Q9: skew ratios eta^(2^L) at L=1,2,3
for L in (1, 2, 3):
    computed = eta ** (2 ** L)
    expected = {1: "100", 2: "10000", 3: "100000000"}[L]
    match = "yes" if computed == float(expected) else "no"
    results.append((f"Q9(L={L})", computed, expected, match))

# Q10: G(3) = 16*(4^3-1)/3
computed = 16 * (4 ** 3 - 1) // 3
expected = "336"
match = "yes" if computed == 336 else "no"
results.append(("Q10", computed, expected, match))

# Q11: reduction factor 2^84/336
computed = Nd3 / 336.0
expected = "5.7568e22"
comp_sig = sig(computed, 5)
match = "yes" if abs(comp_sig - 5.7568e22) / 5.7568e22 < 0.00005 else "no"
results.append(("Q11", computed, expected, match))

# Q12: sweep time at L=2, R=1e6
R = 1e6
computed = Nd2 / R
expected = "1.05"
comp_sig = sig(computed, 3)
match = "yes" if abs(comp_sig - 1.05) < 0.005 else "no"
results.append(("Q12", computed, expected, match))

# Q13: sweep time at L=3 in seconds and years
computed_s = Nd3 / R
year = 3.156e7
computed_y = computed_s / year
expected = "6.13e11"
comp_sig = sig(computed_y, 3)
match = "yes" if abs(comp_sig - 6.13e11) / 6.13e11 < 0.005 else "no"
results.append(("Q13", computed_y, expected, match))

# Q14: N_def(3)/N_def(2) = 2^64
computed = Nd3 / Nd2
expected = "1.8e19"
comp_sig = sig(computed, 2)
match = "yes" if abs(comp_sig - 1.8e19) / 1.8e19 < 0.05 else "no"
results.append(("Q14", computed, expected, match))

# Q15: p_tot at L=3
L = 3
pZ3 = alpha ** (2 ** L - 1) * (eta * p0) ** (2 ** L)
pX3 = alpha ** (2 ** L - 1) * p0 ** (2 ** L)
computed = pX3 + pZ3
expected = "2.79936e-11"
match = "yes" if abs(computed - 2.79936e-11) < 1e-20 else "no"
results.append(("Q15", computed, expected, match))

n_match = 0
for cid, computed, expected, match in results:
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected} match={match}")
    if match == "yes":
        n_match += 1
print(f"VERIFICATION SUMMARY: {len(results)} claims, {n_match} match, {len(results) - n_match} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.9342813e+25 expected=1.93e25 match=yes
CLAIM Q2: computed=1048576 expected=1048576 match=yes
CLAIM Q3: computed=2.2397447e+102 expected=2.24e102 match=yes
CLAIM Q4: computed=64 expected=64 match=yes
CLAIM Q5: computed=8 expected=8 match=yes
CLAIM Q6: computed=0.015625 expected=0.015625 match=yes
CLAIM Q7: computed=2.160216e-06 expected=2.160216e-6 match=yes
CLAIM Q8: computed=0.99990001 expected=0.9999 (share > 99.99%) match=yes
CLAIM Q9(L=1): computed=100 expected=100 match=yes
CLAIM Q9(L=2): computed=10000 expected=10000 match=yes
CLAIM Q9(L=3): computed=1e+08 expected=100000000 match=yes
CLAIM Q10: computed=336 expected=336 match=yes
CLAIM Q11: computed=5.7567896e+22 expected=5.7568e22 match=yes
CLAIM Q12: computed=1.048576 expected=1.05 match=yes
CLAIM Q13: computed=6.1289015e+11 expected=6.13e11 match=yes
CLAIM Q14: computed=1.8446744e+19 expected=1.8e19 match=yes
CLAIM Q15: computed=2.79936e-11 expected=2.79936e-11 match=no
VERIFICATION SUMMARY: 17 claims, 16 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.9342813e+25 | 1.93e25 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 1048576 | 1048576 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q3 | 2.2397447e+102 | 2.24e102 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 64 | 64 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 0.015625 | 0.015625 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 2.160216e-06 | 2.160216e-6 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q8 | 0.99990001 | 0.9999 | - | match | 4 significant digits (as the paper states, at least 2) |
| Q9(L=1) | 100 | 100 | yes | match | 3 significant digits (as printed, at least 3) |
| Q9(L=2) | 10000 | 10000 | yes | match | 5 significant digits (as printed, at least 3) |
| Q9(L=3) | 1e+08 | 100000000 | yes | match | 9 significant digits (as printed, at least 3) |
| Q10 | 336 | 336 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 5.7567896e+22 | 5.7568e22 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q12 | 1.048576 | 1.05 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 6.1289015e+11 | 6.13e11 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 1.8446744e+19 | 1.8e19 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 2.79936e-11 | 2.79936e-11 | no | match | 6 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 17.
