# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Single-bit erasure floor at 300 K is 2.871e-21 J",
    "inputs": "k = 1.380649e-23 J/K; T = 300 K; ln 2 = 0.6931472",
    "formula": "k*T*ln(2)"
  },
  {
    "id": "Q2",
    "statement": "Gate-based logical operation floor lower end is 2.871e-19 J",
    "inputs": "N_ec = 100; kTln2 = 2.870976e-21 J",
    "formula": "N_ec * kTln2"
  },
  {
    "id": "Q3",
    "statement": "Gate-based logical operation floor upper end is 2.871e-18 J",
    "inputs": "N_ec = 1000; kTln2 = 2.870976e-21 J",
    "formula": "N_ec * kTln2"
  },
  {
    "id": "Q4",
    "statement": "Single-relaxation machine per-instance floor with n_out = 20 is 6.029e-20 J",
    "inputs": "n_out = 20; kTln2 = 2.870976e-21 J",
    "formula": "(n_out + 1) * kTln2"
  },
  {
    "id": "Q5",
    "statement": "Energy ratio for N_gates = 1e6, N_ec = 100, n_out = 20 is 4.762e6",
    "inputs": "N_gates = 1000000; N_ec = 100; n_out = 20",
    "formula": "(N_gates * N_ec) / (n_out + 1)"
  },
  {
    "id": "Q6",
    "statement": "If N_ec = 1, the ratio drops to approximately 4.76e4",
    "inputs": "N_gates = 1000000; N_ec = 1; n_out = 20",
    "formula": "(N_gates * N_ec) / (n_out + 1)"
  },
  {
    "id": "Q7",
    "statement": "Projected per-instance energy with 1e3 programming/readout overhead is approximately 6.0e-17 J",
    "inputs": "overhead factor = 1000; E_relax = 6.029e-20 J",
    "formula": "1000 * E_relax"
  }
]

## Script
```python
import math

k = 1.380649e-23
T = 300.0
ln2 = math.log(2)  # use exact ln 2; paper states 0.6931472

kTln2 = k * T * ln2

claims = []

# Q1
computed = k * T * ln2
claims.append(("Q1", computed, "2.871e-21"))

# Q2
computed = 100 * kTln2
claims.append(("Q2", computed, "2.871e-19"))

# Q3
computed = 1000 * kTln2
claims.append(("Q3", computed, "2.871e-18"))

# Q4
computed = 21 * kTln2
claims.append(("Q4", computed, "6.029e-20"))

# Q5
computed = (1000000 * 100) / 21
claims.append(("Q5", computed, "4.762e6"))

# Q6
computed = (1000000 * 1) / 21
claims.append(("Q6", computed, "4.76e4"))

# Q7
computed = 1000 * 6.029e-20
claims.append(("Q7", computed, "6.0e-17"))

sig = {"Q1": 4, "Q2": 4, "Q3": 4, "Q4": 4, "Q5": 4, "Q6": 3, "Q7": 2}

def round_sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

match_count = 0
for cid, computed, expected_str in claims:
    expected = float(expected_str)
    c_rounded = round_sig(computed, sig[cid])
    match = "yes" if abs(c_rounded - expected) <= abs(expected) * 1e-3 + 1e-300 else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={computed:.8e} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=2.87097889e-21 expected=2.871e-21 match=yes
CLAIM Q2: computed=2.87097889e-19 expected=2.871e-19 match=yes
CLAIM Q3: computed=2.87097889e-18 expected=2.871e-18 match=yes
CLAIM Q4: computed=6.02905566e-20 expected=6.029e-20 match=yes
CLAIM Q5: computed=4.76190476e+06 expected=4.762e6 match=yes
CLAIM Q6: computed=4.76190476e+04 expected=4.76e4 match=yes
CLAIM Q7: computed=6.02900000e-17 expected=6.0e-17 match=yes
VERIFICATION SUMMARY: 7 claims, 7 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2.87097889e-21 | 2.871e-21 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 2.87097889e-19 | 2.871e-19 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 2.87097889e-18 | 2.871e-18 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 6.02905566e-20 | 6.029e-20 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 4.76190476e+06 | 4.762e6 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 4.76190476e+04 | 4.76e4 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 6.02900000e-17 | 6.0e-17 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 7.
