# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Accuracy threshold p* = (s+c)/(b+c) under the baseline calibration b=2, c=1, s=1",
    "inputs": "b=2, c=1, s=1",
    "formula": "(s + c) / (b + c)"
  },
  {
    "id": "Q2",
    "statement": "Expected payoff of falsifiable strategy F at p=0.6, b=2, c=1",
    "inputs": "p=0.6, b=2, c=1",
    "formula": "p*b - (1 - p)*c"
  },
  {
    "id": "Q3",
    "statement": "Expected payoff of post-hoc strategy P under baseline s=1",
    "inputs": "s=1",
    "formula": "s"
  },
  {
    "id": "Q4",
    "statement": "Replicator advantage of P over F at p=0.6: Delta = pi_P - pi_F",
    "inputs": "pi_P=1.0, pi_F=0.8",
    "formula": "pi_P - pi_F"
  },
  {
    "id": "Q5",
    "statement": "Expected payoff of F under reformed configuration b=10, c=1, p=0.6",
    "inputs": "p=0.6, b=10, c=1",
    "formula": "p*b - (1 - p)*c"
  },
  {
    "id": "Q6",
    "statement": "Advantage of F over P under reform: Delta = pi_F - pi_P",
    "inputs": "pi_F=5.6, pi_P=1.0",
    "formula": "pi_F - pi_P"
  },
  {
    "id": "Q7",
    "statement": "Reformed threshold p* = (s+c)/(b+c) with b=10, c=1, s=1",
    "inputs": "b=10, c=1, s=1",
    "formula": "(s + c) / (b + c)"
  },
  {
    "id": "Q8",
    "statement": "Expected payoff of F under weaker reform b=5, c=1, p=0.6",
    "inputs": "p=0.6, b=5, c=1",
    "formula": "p*b - (1 - p)*c"
  },
  {
    "id": "Q9",
    "statement": "Threshold p* under weaker reform b=5, c=1, s=1",
    "inputs": "b=5, c=1, s=1",
    "formula": "(s + c) / (b + c)"
  },
  {
    "id": "Q10",
    "statement": "Best-response flip point in b for p=0.6, c=1, s=1",
    "inputs": "s=1, p=0.6, c=1",
    "formula": "(s + (1 - p)*c) / p"
  },
  {
    "id": "Q11",
    "statement": "Initial system reliability R(0) for N=1000, U=400",
    "inputs": "N=1000, U=400",
    "formula": "(N - U) / N"
  },
  {
    "id": "Q12",
    "statement": "System reliability R(100) after k=100 registered failures removed, N=1000, U=400",
    "inputs": "N=1000, U=400, k=100",
    "formula": "(N - (U - k)) / N"
  },
  {
    "id": "Q13",
    "statement": "Reform timescale to majority t = ln 9 / 0.2 under diluted advantage",
    "inputs": "ratio=9, Delta=0.2",
    "formula": "log(9) / 0.2"
  },
  {
    "id": "Q15",
    "statement": "Flip point in b for population with p=0.4, c=1, s=1",
    "inputs": "s=1, p=0.4, c=1",
    "formula": "(s + (1 - p)*c) / p"
  },
  {
    "id": "Q17",
    "statement": "Reward differential needed to flip a median forecaster at p=0.6: b - s",
    "inputs": "b=2.3333, s=1",
    "formula": "b - s"
  }
]

## Script
```python
import math

# Expected values as strings from the paper
expected = {
    "Q1": "0.6667",
    "Q2": "0.8",
    "Q3": "1.0",
    "Q4": "0.2",
    "Q5": "5.6",
    "Q6": "4.6",
    "Q7": "0.1818",
    "Q8": "2.6",
    "Q9": "0.3333",
    "Q10": "2.3333",
    "Q11": "0.6",
    "Q12": "0.7",
    "Q13": "10.99",
    "Q15": "4.0",
    "Q17": "1.3333"
}

def round_to_match(val, target_str):
    """Round val to the same number of decimal places as target_str."""
    if "." in target_str:
        nd = len(target_str.split(".")[1])
    else:
        nd = 0
    rounded = round(val, nd)
    # format to keep trailing zeros
    fmt = f"{{:.{nd}f}}" if nd > 0 else "{}"
    return fmt.format(rounded), nd

# Compute each claim
results = {}

# Q1
val = (1 + 1) / (2 + 1)  # (s+c)/(b+c) with s=1,c=1,b=2
results["Q1"] = val

# Q2
val = 0.6 * 2 - (1 - 0.6) * 1
results["Q2"] = val

# Q3
val = 1.0
results["Q3"] = val

# Q4
val = 1.0 - 0.8
results["Q4"] = val

# Q5
val = 0.6 * 10 - (1 - 0.6) * 1
results["Q5"] = val

# Q6
val = 5.6 - 1.0
results["Q6"] = val

# Q7
val = (1 + 1) / (10 + 1)
results["Q7"] = val

# Q8
val = 0.6 * 5 - (1 - 0.6) * 1
results["Q8"] = val

# Q9
val = (1 + 1) / (5 + 1)
results["Q9"] = val

# Q10
val = (1 + (1 - 0.6) * 1) / 0.6
results["Q10"] = val

# Q11
val = (1000 - 400) / 1000
results["Q11"] = val

# Q12
val = (1000 - (400 - 100)) / 1000
results["Q12"] = val

# Q13
val = math.log(9) / 0.2
results["Q13"] = val

# Q15
val = (1 + (1 - 0.4) * 1) / 0.4
results["Q15"] = val

# Q17
val = 2.3333 - 1.0
results["Q17"] = val

# Print claims
for qid in sorted(expected.keys(), key=lambda x: int(x[1:]) if x[1:].isdigit() else x):
    comp = results[qid]
    comp_str, nd = round_to_match(comp, expected[qid])
    match = "yes" if comp_str == expected[qid] else "no"
    print(f"CLAIM {qid}: computed={comp_str} expected={expected[qid]} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if round_to_match(results[q], expected[q])[0]==expected[q])} match, {len(expected)-sum(1 for q in expected if round_to_match(results[q], expected[q])[0]==expected[q])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.6667 expected=0.6667 match=yes
CLAIM Q2: computed=0.8 expected=0.8 match=yes
CLAIM Q3: computed=1.0 expected=1.0 match=yes
CLAIM Q4: computed=0.2 expected=0.2 match=yes
CLAIM Q5: computed=5.6 expected=5.6 match=yes
CLAIM Q6: computed=4.6 expected=4.6 match=yes
CLAIM Q7: computed=0.1818 expected=0.1818 match=yes
CLAIM Q8: computed=2.6 expected=2.6 match=yes
CLAIM Q9: computed=0.3333 expected=0.3333 match=yes
CLAIM Q10: computed=2.3333 expected=2.3333 match=yes
CLAIM Q11: computed=0.6 expected=0.6 match=yes
CLAIM Q12: computed=0.7 expected=0.7 match=yes
CLAIM Q13: computed=10.99 expected=10.99 match=yes
CLAIM Q15: computed=4.0 expected=4.0 match=yes
CLAIM Q17: computed=1.3333 expected=1.3333 match=yes
VERIFICATION SUMMARY: 15 claims, 15 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.6667 | 0.6667 | yes | match | 4 significant digits (as printed, at least 3) |
| Q2 | 0.8 | 0.8 | yes | match | 3 significant digits (as printed, at least 3) |
| Q3 | 1.0 | 1.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.2 | 0.2 | yes | match | 3 significant digits (as printed, at least 3) |
| Q5 | 5.6 | 5.6 | yes | match | 3 significant digits (as printed, at least 3) |
| Q6 | 4.6 | 4.6 | yes | match | 3 significant digits (as printed, at least 3) |
| Q7 | 0.1818 | 0.1818 | yes | match | 4 significant digits (as printed, at least 3) |
| Q8 | 2.6 | 2.6 | yes | match | 3 significant digits (as printed, at least 3) |
| Q9 | 0.3333 | 0.3333 | yes | match | 4 significant digits (as printed, at least 3) |
| Q10 | 2.3333 | 2.3333 | yes | match | 5 significant digits (as printed, at least 3) |
| Q11 | 0.6 | 0.6 | yes | match | 3 significant digits (as printed, at least 3) |
| Q12 | 0.7 | 0.7 | yes | match | 3 significant digits (as printed, at least 3) |
| Q13 | 10.99 | 10.99 | yes | match | 4 significant digits (as printed, at least 3) |
| Q15 | 4.0 | 4.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q17 | 1.3333 | 1.3333 | yes | match | 5 significant digits (as printed, at least 3) |

Mismatches: 0 of 15.
