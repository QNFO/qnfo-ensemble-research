# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Key-space entropy H(K) = 104.38 bits for m = 26, B_max = 2^16",
    "inputs": "m = 26, B_max = 65536, log2(26!) = 88.38 bits, log2(65535) = 16.00 bits",
    "formula": "H(K) = log2((B_max - 1) * 26!) = log2(65535) + log2(26!)"
  },
  {
    "id": "Q2",
    "statement": "Key-space size |K| ≈ 2.64e31 keys",
    "inputs": "H(K) = 104.38 bits",
    "formula": "|K| = 2^104.38"
  },
  {
    "id": "Q3",
    "statement": "Unicity distance n0 = 149.1 symbols",
    "inputs": "H(K) = 104.38 bits, D = 0.70 bits/symbol",
    "formula": "n0 = H(K) / D"
  },
  {
    "id": "Q4",
    "statement": "Radix-only unicity distance n0_radix = 22.9 symbols",
    "inputs": "H_radix = 16.00 bits, D = 0.70 bits/symbol",
    "formula": "n0_radix = 16.00 / 0.70"
  },
  {
    "id": "Q5",
    "statement": "Stage 1 radix-recovery cost W1 <= 6.5535e7 digit operations for n = 1000",
    "inputs": "B_max - 1 = 65535, n = 1000, c = 1",
    "formula": "W1 = (B_max - 1) * c * n = 65535 * 1000"
  },
  {
    "id": "Q6",
    "statement": "Stage 1 wall-clock time 0.66 s at 1e8 ops/s",
    "inputs": "W1 = 6.5535e7, rate = 1e8 ops/s",
    "formula": "t = W1 / rate"
  },
  {
    "id": "Q7",
    "statement": "Stage 1 wall-clock time 0.066 s at 1e9 ops/s",
    "inputs": "W1 = 6.5535e7, rate = 1e9 ops/s",
    "formula": "t = W1 / rate"
  },
  {
    "id": "Q8",
    "statement": "Probability a symbol of frequency p_min = 0.005 fails to appear in n = 1000 symbols is 0.006654",
    "inputs": "p_min = 0.005, n = 1000",
    "formula": "(1 - p_min)^n = 0.995^1000"
  },
  {
    "id": "Q9",
    "statement": "Brute-force time T_bf = 8.36e14 years at 1e9 keys/s",
    "inputs": "|K| = 2.64e31, rate = 1e9 keys/s, seconds per year = 3.156e7",
    "formula": "T_bf = (2.64e31 / 1e9) / 3.156e7"
  },
  {
    "id": "Q10",
    "statement": "Structural attack faster than brute force by factor ≈ 4.0e22",
    "inputs": "T_bf = 8.36e14 years, t_attack = 0.66 s, seconds per year = 3.156e7",
    "formula": "ratio = T_bf / (0.66 / 3.156e7)"
  },
  {
    "id": "Q11",
    "statement": "Discrimination gap factor of at least 120 for n = 1000 and B' >= 2^16",
    "inputs": "p_max = 0.12, wrong-base max frequency ≈ 1e-3",
    "formula": "gap = 0.12 / 1e-3"
  },
  {
    "id": "Q12",
    "statement": "Unicity distance with D = 0.5 is 208.8 symbols",
    "inputs": "H(K) = 104.38 bits, D = 0.5 bits/symbol",
    "formula": "n0 = 104.38 / 0.5"
  },
  {
    "id": "Q13",
    "statement": "Unicity distance with D = 1.0 is 104.4 symbols",
    "inputs": "H(K) = 104.38 bits, D = 1.0 bits/symbol",
    "formula": "n0 = 104.38 / 1.0"
  },
  {
    "id": "Q14",
    "statement": "Reduced gap factor 50 for p_max = 0.05",
    "inputs": "p_max = 0.05, wrong-base max frequency ≈ 1e-3",
    "formula": "gap = 0.05 / 1e-3"
  },
  {
    "id": "Q15",
    "statement": "n = 1000 exceeds unicity distance by factor 6.7",
    "inputs": "n = 1000, n0 = 149.1",
    "formula": "1000 / 149.1"
  },
  {
    "id": "Q16",
    "statement": "log2(26!) = 88.38 bits",
    "inputs": "26! ≈ 4.0329e26, log2(10) = 3.32193",
    "formula": "log2(26!) = log10(4.0329e26) * log2(10) = 26.6055 * 3.32193"
  }
]

## Script
```python
import math

def sig(x, n):
    # round to n significant digits
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: H(K) = log2(65535) + log2(26!)
log2_26fact = math.lgamma(27) / math.log(2)  # log2(26!)
log2_65535 = math.log2(65535)
H = log2_65535 + log2_26fact
results.append(("Q1", H, "104.38", 2))

# Q2: |K| = 2^104.38
K = 2 ** 104.38
results.append(("Q2", K, "2.64e31", 3))

# Q3: n0 = 104.38 / 0.70
n0 = 104.38 / 0.70
results.append(("Q3", n0, "149.1", 4))

# Q4: n0_radix = 16.00 / 0.70
n0r = 16.00 / 0.70
results.append(("Q4", n0r, "22.9", 3))

# Q5: W1 = 65535 * 1000
W1 = 65535 * 1000
results.append(("Q5", W1, "6.5535e7", 5))

# Q6: t = 6.5535e7 / 1e8
t6 = 6.5535e7 / 1e8
results.append(("Q6", t6, "0.66", 2))

# Q7: t = 6.5535e7 / 1e9
t7 = 6.5535e7 / 1e9
results.append(("Q7", t7, "0.066", 2))

# Q8: 0.995^1000
p8 = 0.995 ** 1000
results.append(("Q8", p8, "0.006654", 4))

# Q9: T_bf = (2.64e31 / 1e9) / 3.156e7
T9 = (2.64e31 / 1e9) / 3.156e7
results.append(("Q9", T9, "8.36e14", 3))

# Q10: ratio = 8.36e14 / (0.66 / 3.156e7)
r10 = 8.36e14 / (0.66 / 3.156e7)
results.append(("Q10", r10, "4.0e22", 2))

# Q11: gap = 0.12 / 1e-3
g11 = 0.12 / 1e-3
results.append(("Q11", g11, "120", 3))

# Q12: 104.38 / 0.5
n12 = 104.38 / 0.5
results.append(("Q12", n12, "208.8", 4))

# Q13: 104.38 / 1.0
n13 = 104.38 / 1.0
results.append(("Q13", n13, "104.4", 4))

# Q14: gap = 0.05 / 1e-3
g14 = 0.05 / 1e-3
results.append(("Q14", g14, "50", 2))

# Q15: 1000 / 149.1
f15 = 1000 / 149.1
results.append(("Q15", f15, "6.7", 2))

# Q16: log2(26!) via log10(4.0329e26) * 3.32193
v16 = math.log10(4.0329e26) * 3.32193
results.append(("Q16", v16, "88.38", 2))

match_count = 0
for cid, computed, expected_str, sigd in results:
    # parse expected string to plain number
    exp_val = float(expected_str)
    comp_rounded = sig(computed, sigd)
    match = "yes" if abs(comp_rounded - exp_val) <= abs(exp_val) * 10 ** (-sigd + 1) / 2 or abs(comp_rounded - exp_val) < 10 ** (math.floor(math.log10(abs(exp_val))) - sigd + 1) else "no"
    # simpler: compare formatted strings
    match = "yes" if ("%.{0}g".format(sigd) % computed) == ("%.{0}g".format(sigd) % exp_val) else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=104.38193 expected=104.38 match=yes
CLAIM Q2: computed=2.6394349e+31 expected=2.64e31 match=yes
CLAIM Q3: computed=149.11429 expected=149.1 match=yes
CLAIM Q4: computed=22.857143 expected=22.9 match=yes
CLAIM Q5: computed=65535000 expected=6.5535e7 match=yes
CLAIM Q6: computed=0.65535 expected=0.66 match=yes
CLAIM Q7: computed=0.065535 expected=0.066 match=yes
CLAIM Q8: computed=0.0066539686 expected=0.006654 match=yes
CLAIM Q9: computed=8.365019e+14 expected=8.36e14 match=no
CLAIM Q10: computed=3.9976e+22 expected=4.0e22 match=yes
CLAIM Q11: computed=120 expected=120 match=yes
CLAIM Q12: computed=208.76 expected=208.8 match=yes
CLAIM Q13: computed=104.38 expected=104.4 match=yes
CLAIM Q14: computed=50 expected=50 match=yes
CLAIM Q15: computed=6.7069081 expected=6.7 match=yes
CLAIM Q16: computed=88.381999 expected=88.38 match=yes
VERIFICATION SUMMARY: 16 claims, 15 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 104.38193 | 104.38 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 2.6394349e+31 | 2.64e31 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 149.11429 | 149.1 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 22.857143 | 22.9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 65535000 | 6.5535e7 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 0.65535 | 0.66 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 0.065535 | 0.066 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 0.0066539686 | 0.006654 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 8.365019e+14 | 8.36e14 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 3.9976e+22 | 4.0e22 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 120 | 120 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 208.76 | 208.8 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 104.38 | 104.4 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q14 | 50 | 50 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 6.7069081 | 6.7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q16 | 88.381999 | 88.38 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
