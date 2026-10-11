# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Number of extensionally distinct admissible existence predicates over N=64 distinctions is 2^(2^64), with log10 approx 5.553e18",
    "inputs": "N=64, log10(2)=0.30103",
    "formula": "log10(2^(2^N)) = 2^N * log10(2)"
  },
  {
    "id": "Q2",
    "statement": "Number of short conjunctions of at most 8 literals from 128 literals is approx 1.53e12",
    "inputs": "2N=128 literals, k_lit=8, binom(128,8) approx 1.4298e12",
    "formula": "sum_{j=0}^{8} binom(128, j) approx binom(128,8)*(1+1/15+...)"
  },
  {
    "id": "Q3",
    "statement": "Landauer erasure cost of one bit at T=300 K is approx 2.8709e-21 J",
    "inputs": "k_B=1.380649e-23 J/K, T=300 K, ln2=0.693147",
    "formula": "E_bit = k_B * T * ln(2)"
  },
  {
    "id": "Q4",
    "statement": "Erasure power for 1e9 distinctions cycled at 1 s^-1 is approx 2.8709e-12 W",
    "inputs": "N_dist=1e9, f_cycle=1 s^-1, E_bit=2.8709e-21 J",
    "formula": "P_erase = f_cycle * N_dist * E_bit"
  },
  {
    "id": "Q5",
    "statement": "Erasure power for 1e20 distinctions cycled at 1e9 s^-1 is approx 2.87e8 W (labeled projection)",
    "inputs": "N_dist=1e20, f_cycle=1e9 s^-1, E_bit=2.8709e-21 J",
    "formula": "P_erase = f_cycle * N_dist * E_bit"
  },
  {
    "id": "Q6",
    "statement": "Nanowatt observer with 1 s coherence sustains at most approx 3.4832e8 bit-distinctions per second",
    "inputs": "P_obs=1e-12 W, tau=1 s, k_B*T*ln2=2.8709e-21 J/bit",
    "formula": "N_max = P_obs * tau / (k_B * T * ln 2)"
  },
  {
    "id": "Q7",
    "statement": "Thermodynamic entropy of 40 uniform bits is approx 3.82785e-22 J/K",
    "inputs": "N=40, k_B=1.380649e-23 J/K, ln2=0.693147",
    "formula": "S = N * k_B * ln(2)"
  },
  {
    "id": "Q8",
    "statement": "Full erasure cost of 40 bits at 300 K is approx 1.14836e-19 J",
    "inputs": "S=3.82785e-22 J/K, T=300 K",
    "formula": "E_erase = S * T"
  }
]

## Script
```python
import math

kB = 1.380649e-23
T = 300.0
ln2 = math.log(2)

# Q1: log10(2^(2^64)) = 2^64 * log10(2)
log10_2 = math.log10(2)
q1 = (2**64) * log10_2
print(f"CLAIM Q1: computed={q1:.6e} expected=5.553e18 match="
      f"{'yes' if math.isclose(q1, 5.553e18, rel_tol=1e-3) else 'no'}")

# Q2: sum_{j=0}^{8} binom(128, j)
from math import comb
q2 = sum(comb(128, j) for j in range(9))
print(f"CLAIM Q2: computed={q2:.6e} expected=1.53e12 match="
      f"{'yes' if math.isclose(q2, 1.53e12, rel_tol=1e-2) else 'no'}")

# Q3: E_bit = kB * T * ln2
q3 = kB * T * ln2
print(f"CLAIM Q3: computed={q3:.6e} expected=2.8709e-21 match="
      f"{'yes' if math.isclose(q3, 2.8709e-21, rel_tol=1e-4) else 'no'}")

# Q4: P_erase = f_cycle * N_dist * E_bit, f=1, N=1e9
q4 = 1.0 * 1e9 * q3
print(f"CLAIM Q4: computed={q4:.6e} expected=2.8709e-12 match="
      f"{'yes' if math.isclose(q4, 2.8709e-12, rel_tol=1e-4) else 'no'}")

# Q5: P_erase = 1e9 * 1e20 * E_bit
q5 = 1e9 * 1e20 * q3
print(f"CLAIM Q5: computed={q5:.6e} expected=2.87e8 match="
      f"{'yes' if math.isclose(q5, 2.87e8, rel_tol=1e-3) else 'no'}")

# Q6: N_max = P_obs * tau / (kB*T*ln2), P_obs=1e-12, tau=1
q6 = 1e-12 * 1.0 / (kB * T * ln2)
print(f"CLAIM Q6: computed={q6:.6e} expected=3.4832e8 match="
      f"{'yes' if math.isclose(q6, 3.4832e8, rel_tol=1e-4) else 'no'}")

# Q7: S = 40 * kB * ln2
q7 = 40 * kB * ln2
print(f"CLAIM Q7: computed={q7:.6e} expected=3.82785e-22 match="
      f"{'yes' if math.isclose(q7, 3.82785e-22, rel_tol=1e-4) else 'no'}")

# Q8: E_erase = S * T
q8 = q7 * T
print(f"CLAIM Q8: computed={q8:.6e} expected=1.14836e-19 match="
      f"{'yes' if math.isclose(q8, 1.14836e-19, rel_tol=1e-4) else 'no'}")

claims = [q1, q2, q3, q4, q5, q6, q7, q8]
expected = [5.553e18, 1.53e12, 2.8709e-21, 2.8709e-12, 2.87e8, 3.4832e8, 3.82785e-22, 1.14836e-19]
tols = [1e-3, 1e-2, 1e-4, 1e-4, 1e-3, 1e-4, 1e-4, 1e-4]
m = sum(1 for c, e, t_ in zip(claims, expected, tols) if math.isclose(c, e, rel_tol=t_))
print(f"VERIFICATION SUMMARY: 8 claims, {m} match, {8 - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=5.553023e+18 expected=5.553e18 match=yes
CLAIM Q2: computed=1.529928e+12 expected=1.53e12 match=yes
CLAIM Q3: computed=2.870979e-21 expected=2.8709e-21 match=yes
CLAIM Q4: computed=2.870979e-12 expected=2.8709e-12 match=yes
CLAIM Q5: computed=2.870979e+08 expected=2.87e8 match=yes
CLAIM Q6: computed=3.483133e+08 expected=3.4832e8 match=yes
CLAIM Q7: computed=3.827972e-22 expected=3.82785e-22 match=yes
CLAIM Q8: computed=1.148392e-19 expected=1.14836e-19 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
