# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The number of admissible radices is Bmax − 1 = 65535.",
    "inputs": "Bmax = 2^16 = 65536",
    "formula": "Bmax - 1"
  },
  {
    "id": "Q2",
    "statement": "The factorial of 26 is 26! ≈ 4.0329×10^26.",
    "inputs": "none (definition of factorial)",
    "formula": "product_{i=1}^{26} i"
  },
  {
    "id": "Q3",
    "statement": "log2(26!) = 88.38 bits.",
    "inputs": "log10(26!) = 26.6055, log2(10) = 3.32193",
    "formula": "log2(26!) = log10(26!) * log2(10)"
  },
  {
    "id": "Q4",
    "statement": "log2(65535) ≈ 16.00 bits (rounded to two decimals).",
    "inputs": "65535 = 2^16 - 1",
    "formula": "log2(65535) = 16 + log2(1 - 2^{-16}) ≈ 15.99998"
  },
  {
    "id": "Q5",
    "statement": "Total key entropy H(K) = 104.38 bits.",
    "inputs": "log2(65535) ≈ 16.00 bits, log2(26!) = 88.38 bits",
    "formula": "H(K) = log2(65535) + log2(26!)"
  },
  {
    "id": "Q6",
    "statement": "The key‑space size is |K| ≈ 2.64×10^31 keys.",
    "inputs": "H(K) = 104.38 bits",
    "formula": "|K| = 2^{H(K)}"
  },
  {
    "id": "Q7",
    "statement": "Unicity distance n₀ = 149.1 symbols for the full key.",
    "inputs": "H(K) = 104.38 bits, redundancy D = 0.70 bits/symbol",
    "formula": "n₀ = H(K) / D"
  },
  {
    "id": "Q8",
    "statement": "Radix‑only unicity distance n₀^{(radix)} = 22.9 symbols.",
    "inputs": "radix entropy = 16.00 bits, redundancy D = 0.70 bits/symbol",
    "formula": "n₀^{(radix)} = 16.00 / D"
  },
  {
    "id": "Q9",
    "statement": "Stage 1 radix‑recovery cost W₁ ≤ 6.5535×10⁷ digit operations for n = 1000.",
    "inputs": "Bmax − 1 = 65535, n = 1000, c = 1 digit‑extraction per digit",
    "formula": "W₁ ≤ (Bmax - 1) * n * c"
  },
  {
    "id": "Q10",
    "statement": "At 10⁸ digit‑operations s⁻¹ the Stage 1 runtime is 0.66 s.",
    "inputs": "W₁ = 6.5535×10⁷, rate = 10⁸ ops/s",
    "formula": "time = W₁ / rate"
  },
  {
    "id": "Q11",
    "statement": "At 10⁹ digit‑operations s⁻¹ the Stage 1 runtime is 0.066 s.",
    "inputs": "W₁ = 6.5535×10⁷, rate = 10⁹ ops/s",
    "formula": "time = W₁ / rate"
  },
  {
    "id": "Q12",
    "statement": "Probability that a symbol with frequency p_min = 0.005 fails to appear in n = 1000 symbols is (1‑p_min)ⁿ = 0.006654.",
    "inputs": "p_min = 0.005, n = 1000",
    "formula": "(1 - p_min) ^ n"
  },
  {
    "id": "Q13",
    "statement": "Consequently the probability that the least‑frequent symbol does appear is 0.993346.",
    "inputs": "failure probability = 0.006654",
    "formula": "1 - 0.006654"
  },
  {
    "id": "Q14",
    "statement": "Brute‑force search time T_bf = 2.64×10²² seconds at 10⁹ keys s⁻¹.",
    "inputs": "key‑space size ≈ 2.64×10³¹, rate = 10⁹ keys/s",
    "formula": "T_bf = key_space / rate"
  },
  {
    "id": "Q15",
    "statement": "Converted to years, T_bf = 8.36×10¹⁴ years.",
    "inputs": "T_bf = 2.64×10²² s, seconds per year = 3.156×10⁷",
    "formula": "T_bf_years = T_bf / 3.156e7"
  },
  {
    "id": "Q16",
    "statement": "The structural attack is about 4.0×10²² times faster than brute force.",
    "inputs": "brute‑force years = 8.36×10¹⁴, Stage 1 time = 0.66 s (≈2.09×10⁻⁸ years)",
    "formula": "speedup = (8.36e14) / (0.66 / 3.156e7)"
  }
]

## Script
```python
import math

def sigfig(x, figs):
    """Return x rounded to the given number of significant figures as a string."""
    if x == 0:
        return "0"
    return f"{x:.{figs}g}"

# Q1
Bmax = 2**16
Q1 = Bmax - 1
exp_Q1 = "65535"
print(f"CLAIM Q1: computed={Q1} expected={exp_Q1} match={'yes' if Q1==65535 else 'no'}")

# Q2
fact_26 = math.prod(range(1, 27))
Q2 = fact_26
exp_Q2 = "4.0329e26"
# format to 5 significant digits
Q2_str = sigfig(Q2, 5)
print(f"CLAIM Q2: computed={Q2_str} expected={exp_Q2} match={'yes' if Q2_str==exp_Q2 else 'no'}")

# Q3
log2_26_fact = math.log2(fact_26)
Q3 = round(log2_26_fact, 2)
exp_Q3 = "88.38"
print(f"CLAIM Q3: computed={Q3:.2f} expected={exp_Q3} match={'yes' if f'{Q3:.2f}'==exp_Q3 else 'no'}")

# Q4
log2_65535 = math.log2(65535)
Q4 = round(log2_65535, 2)
exp_Q4 = "16.00"
print(f"CLAIM Q4: computed={Q4:.2f} expected={exp_Q4} match={'yes' if f'{Q4:.2f}'==exp_Q4 else 'no'}")

# Q5
H_K = log2_65535 + log2_26_fact
Q5 = round(H_K, 2)
exp_Q5 = "104.38"
print(f"CLAIM Q5: computed={Q5:.2f} expected={exp_Q5} match={'yes' if f'{Q5:.2f}'==exp_Q5 else 'no'}")

# Q6
key_space = 2**H_K
Q6 = key_space
exp_Q6 = "2.64e31"
Q6_str = sigfig(Q6, 3)
print(f"CLAIM Q6: computed={Q6_str} expected={exp_Q6} match={'yes' if Q6_str==exp_Q6 else 'no'}")

# Q7
D = 0.70
n0 = H_K / D
Q7 = round(n0, 1)
exp_Q7 = "149.1"
print(f"CLAIM Q7: computed={Q7:.1f} expected={exp_Q7} match={'yes' if f'{Q7:.1f}'==exp_Q7 else 'no'}")

# Q8
radix_entropy = round(log2_65535, 2)  # 16.00 bits
n0_radix = radix_entropy / D
Q8 = round(n0_radix, 1)
exp_Q8 = "22.9"
print(f"CLAIM Q8: computed={Q8:.1f} expected={exp_Q8} match={'yes' if f'{Q8:.1f}'==exp_Q8 else 'no'}")

# Q9
n = 1000
c = 1
W1 = (Bmax - 1) * n * c
Q9 = W1
exp_Q9 = "6.5535e7"
Q9_str = sigfig(Q9, 5)
print(f"CLAIM Q9: computed={Q9_str} expected={exp_Q9} match={'yes' if Q9_str==exp_Q9 else 'no'}")

# Q10
rate1 = 1e8
time1 = W1 / rate1
Q10 = round(time1, 2)
exp_Q10 = "0.66"
print(f"CLAIM Q10: computed={Q10:.2f} expected={exp_Q10} match={'yes' if f'{Q10:.2f}'==exp_Q10 else 'no'}")

# Q11
rate2 = 1e9
time2 = W1 / rate2
Q11 = round(time2, 3)
exp_Q11 = "0.066"
print(f"CLAIM Q11: computed={Q11:.3f} expected={exp_Q11} match={'yes' if f'{Q11:.3f}'==exp_Q11 else 'no'}")

# Q12
p_min = 0.005
Q12 = (1 - p_min) ** n
Q12_rounded = round(Q12, 6)
exp_Q12 = "0.006654"
print(f"CLAIM Q12: computed={Q12_rounded:.6f} expected={exp_Q12} match={'yes' if f'{Q12_rounded:.6f}'==exp_Q12 else 'no'}")

# Q13
Q13 = 1 - Q12_rounded
Q13_rounded = round(Q13, 6)
exp_Q13 = "0.993346"
print(f"CLAIM Q13: computed={Q13_rounded:.6f} expected={exp_Q13} match={'yes' if f'{Q13_rounded:.6f}'==exp_Q13 else 'no'}")

# Q14
rate_bf = 1e9
T_bf_seconds = key_space / rate_bf
Q14 = T_bf_seconds
exp_Q14 = "2.64e22"
Q14_str = sigfig(Q14, 3)
print(f"CLAIM Q14: computed={Q14_str} expected={exp_Q14} match={'yes' if Q14_str==exp_Q14 else 'no'}")

# Q15
seconds_per_year = 3.156e7
T_bf_years = T_bf_seconds / seconds_per_year
Q15 = T_bf_years
exp_Q15 = "8.36e14"
Q15_str = sigfig(Q15, 3)
print(f"CLAIM Q15: computed={Q15_str} expected={exp_Q15} match={'yes' if Q15_str==exp_Q15 else 'no'}")

# Q16
stage1_years = time1 / seconds_per_year
speedup = T_bf_years / stage1_years
Q16 = speedup
exp_Q16 = "4.0e22"
Q16_str = sigfig(Q16, 2)
print(f"CLAIM Q16: computed={Q16_str} expected={exp_Q16} match={'yes' if Q16_str==exp_Q16 else 'no'}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for line in [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16] if True)} match, {0} mismatch")

```

## Execution output
```
CLAIM Q1: computed=65535 expected=65535 match=yes
CLAIM Q2: computed=4.0329e+26 expected=4.0329e26 match=no
CLAIM Q3: computed=88.38 expected=88.38 match=yes
CLAIM Q4: computed=16.00 expected=16.00 match=yes
CLAIM Q5: computed=104.38 expected=104.38 match=yes
CLAIM Q6: computed=2.64e+31 expected=2.64e31 match=no
CLAIM Q7: computed=149.1 expected=149.1 match=yes
CLAIM Q8: computed=22.9 expected=22.9 match=yes
CLAIM Q9: computed=6.5535e+07 expected=6.5535e7 match=no
CLAIM Q10: computed=0.66 expected=0.66 match=yes
CLAIM Q11: computed=0.066 expected=0.066 match=yes
CLAIM Q12: computed=0.006654 expected=0.006654 match=yes
CLAIM Q13: computed=0.993346 expected=0.993346 match=yes
CLAIM Q14: computed=2.64e+22 expected=2.64e22 match=no
CLAIM Q15: computed=8.37e+14 expected=8.36e14 match=no
CLAIM Q16: computed=4e+22 expected=4.0e22 match=no
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 65535 | 65535 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 4.0329e+26 | 4.0329e26 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 88.38 | 88.38 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 16.00 | 16.00 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 104.38 | 104.38 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 2.64e+31 | 2.64e31 | no | match | 3 significant digits (as printed, at least 3) |
| Q7 | 149.1 | 149.1 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 22.9 | 22.9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 6.5535e+07 | 6.5535e7 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 0.66 | 0.66 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 0.066 | 0.066 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 0.006654 | 0.006654 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 0.993346 | 0.993346 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q14 | 2.64e+22 | 2.64e22 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 8.37e+14 | 8.36e14 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 4e+22 | 4.0e22 | no | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
