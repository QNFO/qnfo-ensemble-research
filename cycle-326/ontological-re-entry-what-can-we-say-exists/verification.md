# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Number of states for N=64 is 2^{64}=1.8446744×10^{19}.",
    "inputs": "N = 64",
    "formula": "2^N"
  },
  {
    "id": "Q2",
    "statement": "Number of admissible predicates is 2^{2^{64}}≈10^{5.553×10^{18}}.",
    "inputs": "N = 64",
    "formula": "2^{2^N}"
  },
  {
    "id": "Q3",
    "statement": "Reachable short predicates (≤9 literals) count ≈1.53×10^{13}.",
    "inputs": "N = 64, max literals = 9",
    "formula": "sum_{k=1}^{9} C(N, k) * 2^{k}"
  },
  {
    "id": "Q4",
    "statement": "Fraction of reachable predicates ≈0.",
    "inputs": "reachable count from Q3, total count from Q2",
    "formula": "reachable / total"
  },
  {
    "id": "Q5",
    "statement": "Landauer erasure energy per bit at 300 K is 2.8709×10^{-21} J.",
    "inputs": "k_B = 1.380649×10^{-23} J·K^{-1}, T = 300 K, ln2 ≈ 0.693147",
    "formula": "k_B * T * ln2"
  },
  {
    "id": "Q6",
    "statement": "Erasure power for 10^{9} distinctions at 1 Hz is 2.8709×10^{-12} W.",
    "inputs": "f_cycle = 1 Hz, N_dist = 10^{9}, E_bit from Q5",
    "formula": "f_cycle * N_dist * E_bit"
  },
  {
    "id": "Q7",
    "statement": "Maximum distinguishable bits for a 10^{-12} W observer is 3.48×10^{8}.",
    "inputs": "P_obs = 1×10^{-12} W, τ = 1 s, E_bit from Q5",
    "formula": "(P_obs * τ) / E_bit"
  },
  {
    "id": "Q8",
    "statement": "Ultrametric compression factor from 2^{30} fine balls to 2^{10} coarse balls is 1.05×10^{6}.",
    "inputs": "fine exponent = 30, coarse exponent = 10",
    "formula": "2^{30-10}"
  },
  {
    "id": "Q9",
    "statement": "Probability that a coarse ball contains exactly one object is 3.78×10^{-41}.",
    "inputs": "m = 1×10^{5} objects, coarse balls = 2^{10} = 1024",
    "formula": "λ = m / 1024; p1 = λ * exp(-λ)"
  },
  {
    "id": "Q10",
    "statement": "Expected number of resolvable objects after compression is 3.9×10^{-38} ≈0.",
    "inputs": "coarse balls = 1024, p1 from Q9",
    "formula": "1024 * p1"
  },
  {
    "id": "Q12",
    "statement": "Excess precision for unre‑enterable predicate is 36 bits.",
    "inputs": "n_prec = 100 bits, N = 64 bits",
    "formula": "n_prec - N"
  }
]

## Script
```python
import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Q1
N = 64
computed_Q1 = 2**N
expected_Q1 = "1.8446744e19"
match_Q1 = "yes" if round_sig(computed_Q1, 8) == 1.8446744e19 else "no"
print(f"CLAIM Q1: computed={computed_Q1:.8e} expected={expected_Q1} match={match_Q1}")

# Q2
# Compute exponent = 2^N * log10(2)
exponent = (2**N) * math.log10(2)
computed_Q2 = exponent  # we compare exponent part
expected_Q2 = "10^{5.553e18}"
# round exponent to 4 significant digits as in paper (5.553×10^{18})
rounded_exp = round_sig(exponent, 4)
match_Q2 = "yes" if abs(rounded_exp - 5.553e18) < 1e14 else "no"
print(f"CLAIM Q2: computed={rounded_exp:.3e} expected={expected_Q2} match={match_Q2}")

# Q3
max_literals = 9
reachable = 0
for k in range(1, max_literals + 1):
    reachable += math.comb(N, k) * (2**k)
computed_Q3 = reachable
expected_Q3 = "1.53e13"
match_Q3 = "yes" if round_sig(computed_Q3, 3) == 1.53e13 else "no"
print(f"CLAIM Q3: computed={computed_Q3:.3e} expected={expected_Q3} match={match_Q3}")

# Q4
# total predicates ≈ 10^{5.553e18}, effectively infinite for float
# fraction is essentially zero
computed_Q4 = 0.0
expected_Q4 = "0"
match_Q4 = "yes" if computed_Q4 == 0.0 else "no"
print(f"CLAIM Q4: computed={computed_Q4:.1e} expected={expected_Q4} match={match_Q4}")

# Q5
k_B = 1.380649e-23  # J/K
T = 300.0
ln2 = 0.693147
computed_Q5 = k_B * T * ln2
expected_Q5 = "2.8709e-21"
match_Q5 = "yes" if round_sig(computed_Q5, 5) == 2.8709e-21 else "no"
print(f"CLAIM Q5: computed={computed_Q5:.5e} expected={expected_Q5} match={match_Q5}")

# Q6
f_cycle = 1.0  # Hz
N_dist = 1e9
computed_Q6 = f_cycle * N_dist * computed_Q5
expected_Q6 = "2.8709e-12"
match_Q6 = "yes" if round_sig(computed_Q6, 5) == 2.8709e-12 else "no"
print(f"CLAIM Q6: computed={computed_Q6:.5e} expected={expected_Q6} match={match_Q6}")

# Q7
P_obs = 1e-12  # W
tau = 1.0      # s
computed_Q7 = (P_obs * tau) / computed_Q5
expected_Q7 = "3.48e8"
match_Q7 = "yes" if round_sig(computed_Q7, 3) == 3.48e8 else "no"
print(f"CLAIM Q7: computed={computed_Q7:.3e} expected={expected_Q7} match={match_Q7}")

# Q8
computed_Q8 = 2**(30-10)
expected_Q8 = "1.05e6"
match_Q8 = "yes" if round_sig(computed_Q8, 3) == 1.05e6 else "no"
print(f"CLAIM Q8: computed={computed_Q8:.3e} expected={expected_Q8} match={match_Q8}")

# Q9
m = 1e5
coarse = 2**10  # 1024
lam = m / coarse
p1 = lam * math.exp(-lam)
computed_Q9 = p1
expected_Q9 = "3.78e-41"
match_Q9 = "yes" if round_sig(computed_Q9, 3) == 3.78e-41 else "no"
print(f"CLAIM Q9: computed={computed_Q9:.3e} expected={expected_Q9} match={match_Q9}")

# Q10
computed_Q10 = coarse * p1
expected_Q10 = "3.9e-38"
match_Q10 = "yes" if round_sig(computed_Q10, 2) == 3.9e-38 else "no"
print(f"CLAIM Q10: computed={computed_Q10:.2e} expected={expected_Q10} match={match_Q10}")

# Q12
n_prec = 100
computed_Q12 = n_prec - N
expected_Q12 = "36"
match_Q12 = "yes" if computed_Q12 == 36 else "no"
print(f"CLAIM Q12: computed={computed_Q12} expected={expected_Q12} match={match_Q12}")

print(f"VERIFICATION SUMMARY: 11 claims, {sum(1 for m in [match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10,match_Q12] if m=='yes')} match, {sum(1 for m in [match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10,match_Q12] if m=='no')} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.84467441e+19 expected=1.8446744e19 match=yes
CLAIM Q2: computed=5.553e+18 expected=10^{5.553e18} match=yes
CLAIM Q3: computed=1.532e+13 expected=1.53e13 match=yes
CLAIM Q4: computed=0.0e+00 expected=0 match=yes
CLAIM Q5: computed=2.87098e-21 expected=2.8709e-21 match=no
CLAIM Q6: computed=2.87098e-12 expected=2.8709e-12 match=no
CLAIM Q7: computed=3.483e+08 expected=3.48e8 match=yes
CLAIM Q8: computed=1.049e+06 expected=1.05e6 match=yes
CLAIM Q9: computed=3.786e-41 expected=3.78e-41 match=no
CLAIM Q10: computed=3.88e-38 expected=3.9e-38 match=yes
CLAIM Q12: computed=36 expected=36 match=yes
VERIFICATION SUMMARY: 11 claims, 8 match, 3 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.84467441e+19 | 1.8446744e19 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q2 | 5.553e+18 | 10^{5.553e18} | yes | match | script verdict (values not both numeric) |
| Q3 | 1.532e+13 | 1.53e13 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.0e+00 | 0 | yes | match | stated value is zero |
| Q5 | 2.87098e-21 | 2.8709e-21 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 2.87098e-12 | 2.8709e-12 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 3.483e+08 | 3.48e8 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 1.049e+06 | 1.05e6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 3.786e-41 | 3.78e-41 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 3.88e-38 | 3.9e-38 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 36 | 36 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 11.
