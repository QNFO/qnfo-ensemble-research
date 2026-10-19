# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The sum of the nine multilingual parsing scores equals 708.4 percentage points.",
    "inputs": "Czech = 87.1, English = 83.8, Hebrew = 68.7, Italian = 73.0, Polish = 75.0, Portuguese = 88.9, Serbian = 86.6, Swedish = 86.6, Turkish = 58.7",
    "formula": "S = 87.1 + 83.8 + 68.7 + 73.0 + 75.0 + 88.9 + 86.6 + 86.6 + 58.7"
  },
  {
    "id": "Q2",
    "statement": "The average multilingual parsing score across the nine languages is 78.711… % (rounded to 78.7 %).",
    "inputs": "Sum S = 708.4, Number of languages N = 9",
    "formula": "Average = S / N"
  },
  {
    "id": "Q3",
    "statement": "A full binary tree of depth D = 5 contains V = 63 vertices.",
    "inputs": "Tree depth D = 5",
    "formula": "V = 2^(D+1) - 1"
  },
  {
    "id": "Q4",
    "statement": "The expected number of stochastic noise events per logical gate is E = 0.063.",
    "inputs": "Per‑vertex noise rate r = 10^-3 per ns, Gate time t_g = 1 ns, Number of vertices V = 63",
    "formula": "E = r * t_g * V"
  },
  {
    "id": "Q5",
    "statement": "The error‑suppression factor exceeds S = 6.3×10^10.",
    "inputs": "Raw error probability p_raw = 0.063, Logical error bound p_logical = 10^-12",
    "formula": "S > p_raw / p_logical"
  }
]

## Script
```python
# Compute and verify quantitative claims from the paper

def sig_round(value, sig_digits):
    """Round value to the given number of significant digits."""
    from math import log10, floor
    if value == 0:
        return 0.0
    digits = sig_digits - int(floor(log10(abs(value)))) - 1
    return round(value, digits)

claims = [
    {
        "id": "Q1",
        "computed": 87.1 + 83.8 + 68.7 + 73.0 + 75.0 + 88.9 + 86.6 + 86.6 + 58.7,
        "expected_str": "708.4",
        "sig": 4  # 4 significant digits in 708.4
    },
    {
        "id": "Q2",
        "computed": (87.1 + 83.8 + 68.7 + 73.0 + 75.0 + 88.9 + 86.6 + 86.6 + 58.7) / 9,
        "expected_str": "78.711",
        "sig": 6  # 6 significant digits in 78.711
    },
    {
        "id": "Q3",
        "computed": 2**(5 + 1) - 1,
        "expected_str": "63",
        "sig": 2  # 2 significant digits in 63
    },
    {
        "id": "Q4",
        "computed": 1e-3 * 1 * 63,
        "expected_str": "0.063",
        "sig": 3  # 3 significant digits in 0.063
    },
    {
        "id": "Q5",
        "computed": 0.063 / 1e-12,
        "expected_str": "6.3e10",
        "sig": 2  # 2 significant digits in 6.3e10
    },
]

for c in claims:
    expected = float(c["expected_str"].replace("e", "E"))
    rounded = sig_round(c["computed"], c["sig"])
    match = "yes" if abs(rounded - expected) < 1e-12 else "no"
    # format computed with at least 8 significant digits
    comp_str = f"{c['computed']:.12g}"
    exp_str = c["expected_str"]
    print(f"CLAIM {c['id']}: computed={comp_str} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, "
      f"{sum(1 for c in claims if sig_round(c['computed'], c['sig']) == float(c['expected_str'].replace('e','E')))} match, "
      f"{sum(1 for c in claims if sig_round(c['computed'], c['sig']) != float(c['expected_str'].replace('e','E')))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=708.4 expected=708.4 match=yes
CLAIM Q2: computed=78.7111111111 expected=78.711 match=no
CLAIM Q3: computed=63 expected=63 match=yes
CLAIM Q4: computed=0.063 expected=0.063 match=yes
CLAIM Q5: computed=63000000000 expected=6.3e10 match=yes
VERIFICATION SUMMARY: 5 claims, 4 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 708.4 | 708.4 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 78.7111111111 | 78.711 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 63 | 63 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.063 | 0.063 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 63000000000 | 6.3e10 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 5.
