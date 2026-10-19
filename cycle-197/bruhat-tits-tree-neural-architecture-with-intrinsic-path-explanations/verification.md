# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "A depth‑5 BT‑TNA with prime p=2 can represent 48 distinct hierarchical classes.",
    "inputs": "p=2, D=5",
    "formula": "N = (p+1) * p^(D-1)"
  },
  {
    "id": "Q2",
    "statement": "A depth‑10 BT‑TNA with prime p=2 can represent 1 536 distinct hierarchical classes.",
    "inputs": "p=2, D=10",
    "formula": "N = (p+1) * p^(D-1)"
  },
  {
    "id": "Q3",
    "statement": "For p=2 and depth D=5 the total number of vertices in the truncated tree is 94.",
    "inputs": "p=2, D=5",
    "formula": "V = 1 + (p+1)*(p^D - 1)/(p-1)"
  },
  {
    "id": "Q4",
    "statement": "For p=2 and depth D=10 the total number of vertices in the truncated tree is 3 070.",
    "inputs": "p=2, D=10",
    "formula": "V = 1 + (p+1)*(p^D - 1)/(p-1)"
  },
  {
    "id": "Q5",
    "statement": "A quantum walk on a depth‑100 tree is 100 × faster than a classical random walk when β/α = 1.",
    "inputs": "D=100, beta/alpha=1",
    "formula": "S = (beta/alpha) * D"
  },
  {
    "id": "Q6",
    "statement": "The explanation‑cost ratio for depth D=5 and F=20 features is 209 715.2.",
    "inputs": "D=5, F=20",
    "formula": "R = 2^F / D"
  },
  {
    "id": "Q7",
    "statement": "The explanation‑cost ratio for depth D=10 and F=20 features is 104 857.6.",
    "inputs": "D=10, F=20",
    "formula": "R = 2^F / D"
  },
  {
    "id": "Q8",
    "statement": "BT‑TNA achieves a 6.6‑fold improvement over the transformer baseline.",
    "inputs": "factor=6.6",
    "formula": "A_BT = factor * A_tr"
  },
  {
    "id": "Q9",
    "statement": "The token‑calculus protocol improves detection by 100 percentage points (100 % vs 0 %).",
    "inputs": "detection_BT=100%, detection_baseline=0%",
    "formula": "improvement = detection_BT - detection_baseline"
  },
  {
    "id": "Q10",
    "statement": "Assuming α=1 and β/α=1, a quantum walk traverses a depth‑10 tree in 10 steps versus 100 steps for a classical walk, a 10 × speed‑up.",
    "inputs": "D=10, alpha=1, beta/alpha=1",
    "formula": "quantum_steps = alpha * D; classical_steps = beta * D^2; speedup = classical_steps / quantum_steps"
  }
]

## Script
```python
import math

def fmt(val):
    # Format with at least 8 significant digits, removing trailing zeros
    if isinstance(val, float):
        s = f"{val:.10g}"
    else:
        s = str(val)
    return s

claims = [
    {
        "id": "Q1",
        "computed": (2+1) * 2**(5-1),  # N = (p+1) * p^(D-1)
        "expected": "48"
    },
    {
        "id": "Q2",
        "computed": (2+1) * 2**(10-1),
        "expected": "1536"
    },
    {
        "id": "Q3",
        "computed": 1 + (2+1)*(2**5 - 1)//(2-1),  # integer division safe here
        "expected": "94"
    },
    {
        "id": "Q4",
        "computed": 1 + (2+1)*(2**10 - 1)//(2-1),
        "expected": "3070"
    },
    {
        "id": "Q5",
        "computed": (1) * 100,  # S = (beta/alpha) * D, beta/alpha=1, D=100
        "expected": "100"
    },
    {
        "id": "Q6",
        "computed": 2**20 / 5,  # R = 2^F / D, F=20, D=5
        "expected": "209715.2"
    },
    {
        "id": "Q7",
        "computed": 2**20 / 10,
        "expected": "104857.6"
    },
    {
        "id": "Q8",
        "computed": 6.6,  # factor itself
        "expected": "6.6"
    },
    {
        "id": "Q9",
        "computed": 100 - 0,  # improvement = detection_BT - detection_baseline
        "expected": "100"
    },
    {
        "id": "Q10",
        "computed": (1 * 10**2) / (1 * 10),  # speedup = classical_steps / quantum_steps
        "expected": "10"
    }
]

for c in claims:
    comp = c["computed"]
    exp = c["expected"]
    match = "yes" if fmt(comp) == exp else "no"
    print(f"CLAIM {c['id']}: computed={fmt(comp)} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, "
      f"{sum(1 for c in claims if fmt(c['computed']) == c['expected'])} match, "
      f"{sum(1 for c in claims if fmt(c['computed']) != c['expected'])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=48 expected=48 match=yes
CLAIM Q2: computed=1536 expected=1536 match=yes
CLAIM Q3: computed=94 expected=94 match=yes
CLAIM Q4: computed=3070 expected=3070 match=yes
CLAIM Q5: computed=100 expected=100 match=yes
CLAIM Q6: computed=209715.2 expected=209715.2 match=yes
CLAIM Q7: computed=104857.6 expected=104857.6 match=yes
CLAIM Q8: computed=6.6 expected=6.6 match=yes
CLAIM Q9: computed=100 expected=100 match=yes
CLAIM Q10: computed=10 expected=10 match=yes
VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 48 | 48 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 1536 | 1536 | yes | match | 4 significant digits (as printed, at least 3) |
| Q3 | 94 | 94 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 3070 | 3070 | yes | match | 4 significant digits (as printed, at least 3) |
| Q5 | 100 | 100 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 209715.2 | 209715.2 | yes | match | 7 significant digits (as printed, at least 3) |
| Q7 | 104857.6 | 104857.6 | yes | match | 7 significant digits (as printed, at least 3) |
| Q8 | 6.6 | 6.6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 100 | 100 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 10 | 10 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 10.
