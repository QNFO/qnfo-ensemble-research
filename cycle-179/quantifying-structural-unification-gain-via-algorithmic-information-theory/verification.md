# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Average accuracy gain of the Info‑Gain Sampler is 3.0 percentage points.",
    "inputs": "accuracy gains: 3.1 pp, 2.9 pp",
    "formula": "(3.1 + 2.9) / 2"
  },
  {
    "id": "Q2",
    "statement": "Average cumulative‑entropy reduction is 36.05 % of the greedy baseline.",
    "inputs": "entropy percentages of baseline: 65.9 %, 62.0 %",
    "formula": "((100 - 65.9) + (100 - 62.0)) / 2"
  },
  {
    "id": "Q3",
    "statement": "Mean runtime with XOR optimization is 6.34 seconds.",
    "inputs": "runtimes with optimization (seconds): 3.3, 0.1, 9.1, 9.6, 9.6",
    "formula": "(3.3 + 0.1 + 9.1 + 9.6 + 9.6) / 5"
  },
  {
    "id": "Q4",
    "statement": "GTSP preprocessing compression ratio is 0.375.",
    "inputs": "reduced preprocessing time 0.45 s, original preprocessing time 1.20 s",
    "formula": "0.45 / 1.20"
  },
  {
    "id": "Q5",
    "statement": "Projected cost for running the benchmark suite for 10 hours is approximately $1.00.",
    "inputs": "electricity cost rate $0.10 per hour, duration 10 hours",
    "formula": "0.10 * 10"
  }
]

## Script
```python
import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    else:
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

claims = {
    "Q1": {"inputs": (3.1, 2.9), "formula": lambda a,b: (a + b) / 2, "expected": "3.0", "sig": 2},
    "Q2": {"inputs": (65.9, 62.0), "formula": lambda p1,p2: ((100 - p1) + (100 - p2)) / 2, "expected": "36.05", "sig": 4},
    "Q3": {"inputs": (3.3, 0.1, 9.1, 9.6, 9.6), "formula": lambda *vals: sum(vals) / len(vals), "expected": "6.34", "sig": 3},
    "Q4": {"inputs": (0.45, 1.20), "formula": lambda a,b: a / b, "expected": "0.375", "sig": 3},
    "Q5": {"inputs": (0.10, 10), "formula": lambda rate, hrs: rate * hrs, "expected": "1.00", "sig": 3},
}

for cid, data in claims.items():
    computed = data["formula"](*data["inputs"])
    # high-precision display (at least 8 significant digits)
    computed_str = f"{computed:.10g}"
    # round to required significant figures for comparison
    rounded = round_sig(computed, data["sig"])
    # format rounded to match expected string length (preserve trailing zeros)
    if '.' in data["expected"]:
        # determine number of decimal places in expected
        dec_places = len(data["expected"].split('.')[1])
        rounded_str = f"{rounded:.{dec_places}f}"
    else:
        rounded_str = str(int(round(rounded)))
    match = "yes" if rounded_str == data["expected"] else "no"
    print(f"CLAIM {cid}: computed={computed_str} expected={data['expected']} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for d in claims.values() if round_sig(d['formula'](*d['inputs']), d['sig']) == float(d['expected']))} match, {len(claims) - sum(1 for d in claims.values() if round_sig(d['formula'](*d['inputs']), d['sig']) == float(d['expected']))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=3 expected=3.0 match=yes
CLAIM Q2: computed=36.05 expected=36.05 match=yes
CLAIM Q3: computed=6.34 expected=6.34 match=yes
CLAIM Q4: computed=0.375 expected=0.375 match=yes
CLAIM Q5: computed=1 expected=1.00 match=yes
VERIFICATION SUMMARY: 5 claims, 5 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 3 | 3.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 36.05 | 36.05 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 6.34 | 6.34 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.375 | 0.375 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 1 | 1.00 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 5.
