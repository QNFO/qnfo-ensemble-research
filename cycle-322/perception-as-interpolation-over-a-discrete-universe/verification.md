# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Each shift map $s_i$ has Lipschitz constant $L(s_i)=\\tfrac12$.",
    "inputs": "None (directly stated from [1, §3])",
    "formula": "L(s_i)=1/2"
  },
  {
    "id": "Q2",
    "statement": "The maximal Lipschitz constant $L_{\\max}=\\max_i L(s_i)$ equals $\\tfrac12$.",
    "inputs": "L(s_i)=1/2",
    "formula": "L_{\\max}=\\max_i L(s_i)=1/2"
  },
  {
    "id": "Q3",
    "statement": "The assumed maximal sampling interval is $\\Delta x = 0.1\\;\\text{mm}$.",
    "inputs": "Assumption (A1)",
    "formula": "\\Delta x = 0.1\\;\\text{mm}"
  },
  {
    "id": "Q4",
    "statement": "The worst‑case interpolation error bound is $\\|e\\|_{\\infty} \\le 0.05\\;\\text{mm}$.",
    "inputs": "L_{\\max}=1/2, \\Delta x=0.1\\;\\text{mm}",
    "formula": "\\|e\\|_{\\infty} \\le L_{\\max}\\,\\Delta x = \\tfrac12 \\times 0.1\\;\\text{mm}=0.05\\;\\text{mm}"
  },
  {
    "id": "Q5",
    "statement": "If the sampling interval is halved to $\\Delta x=0.05\\;\\text{mm}$, the bound becomes $0.025\\;\\text{mm}$.",
    "inputs": "L_{\\max}=1/2, \\Delta x=0.05\\;\\text{mm}",
    "formula": "\\|e\\|_{\\infty} \\le \\tfrac12 \\times 0.05\\;\\text{mm}=0.025\\;\\text{mm}"
  },
  {
    "id": "Q6",
    "statement": "For $\\Delta x=0.05\\;\\text{mm}$ the bound corresponds to a relative error of $2.5\\%$ with respect to a typical receptive‑field diameter $d\\approx1\\;\\text{mm}$.",
    "inputs": "Bound $0.025\\;\\text{mm}$, $d=1\\;\\text{mm}$",
    "formula": "Relative error = (0.025/1)\\times100\\% = 2.5\\%"
  },
  {
    "id": "Q7",
    "statement": "If the sampling interval is $\\Delta x=0.02\\;\\text{mm}$, the bound becomes $0.01\\;\\text{mm}$.",
    "inputs": "L_{\\max}=1/2, \\Delta x=0.02\\;\\text{mm}",
    "formula": "\\|e\\|_{\\infty} \\le \\tfrac12 \\times 0.02\\;\\text{mm}=0.01\\;\\text{mm}"
  },
  {
    "id": "Q8",
    "statement": "For $\\Delta x=0.02\\;\\text{mm}$ the bound corresponds to a relative error of $1\\%$ with respect to $d\\approx1\\;\\text{mm}$.",
    "inputs": "Bound $0.01\\;\\text{mm}$, $d=1\\;\\text{mm}$",
    "formula": "Relative error = (0.01/1)\\times100\\% = 1\\%"
  },
  {
    "id": "Q9",
    "statement": "Using an alternative Lipschitz constant $\\lambda=0.3$ with $\\Delta x=0.1\\;\\text{mm}$ yields a bound of $0.03\\;\\text{mm}$.",
    "inputs": "\\lambda=0.3, \\Delta x=0.1\\;\\text{mm}",
    "formula": "\\|e\\|_{\\infty} \\le \\lambda\\,\\Delta x = 0.3 \\times 0.1\\;\\text{mm}=0.03\\;\\text{mm}"
  },
  {
    "id": "Q10",
    "statement": "Assuming a prosthetic device with $\\Delta x=0.08\\;\\text{mm}$, the bound becomes $0.04\\;\\text{mm}$.",
    "inputs": "L_{\\max}=1/2, \\Delta x=0.08\\;\\text{mm}",
    "formula": "\\|e\\|_{\\infty} \\le \\tfrac12 \\times 0.08\\;\\text{mm}=0.04\\;\\text{mm}"
  },
  {
    "id": "Q11",
    "statement": "Reducing the sampling interval from $0.1\\;\\text{mm}$ to $0.08\\;\\text{mm}$ (a 20 % reduction) increases the sampling density by 25 %.",
    "inputs": "Original $\\Delta x_{0}=0.1\\;\\text{mm}$, new $\\Delta x_{1}=0.08\\;\\text{mm}$, density $\\propto 1/\\Delta x$",
    "formula": "Density factor = \\Delta x_{0}/\\Delta x_{1}=0.1/0.08=1.25 \\;(25\\%\\ increase)"
  }
]

## Script
```python
import math

def round_sig(x, sig):
    """Round x to sig significant digits."""
    if x == 0:
        return 0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Claims data: (computed formula lambda, expected value, sig digits)
claims = {
    "Q1": (lambda: 1/2, 0.5, 1),               # 0.5 (1 sig digit)
    "Q2": (lambda: max([1/2]), 0.5, 1),        # 0.5
    "Q3": (lambda: 0.1, 0.1, 1),               # 0.1
    "Q4": (lambda: 0.5 * 0.1, 0.05, 2),        # 0.05
    "Q5": (lambda: 0.5 * 0.05, 0.025, 3),      # 0.025
    "Q6": (lambda: (0.025/1.0)*100, 2.5, 2),   # 2.5%
    "Q7": (lambda: 0.5 * 0.02, 0.01, 2),       # 0.01
    "Q8": (lambda: (0.01/1.0)*100, 1.0, 2),    # 1%
    "Q9": (lambda: 0.3 * 0.1, 0.03, 2),        # 0.03
    "Q10":(lambda: 0.5 * 0.08, 0.04, 2),       # 0.04
    "Q11":(lambda: 0.1/0.08, 1.25, 3),         # 1.25
}

for cid, (calc, expected, sig) in claims.items():
    computed = calc()
    # Round both to the required significant digits for comparison
    comp_rounded = round_sig(computed, sig)
    exp_rounded = round_sig(expected, sig)
    match = "yes" if comp_rounded == exp_rounded else "no"
    # Format with enough digits (8 significant)
    print(f"CLAIM {cid}: computed={computed:.8g} expected={expected} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for v in claims.values() if round_sig(v[0](), v[2])==round_sig(v[1], v[2]))} match, {sum(1 for v in claims.values() if round_sig(v[0](), v[2])!=round_sig(v[1], v[2]))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.5 expected=0.5 match=yes
CLAIM Q2: computed=0.5 expected=0.5 match=yes
CLAIM Q3: computed=0.1 expected=0.1 match=yes
CLAIM Q4: computed=0.05 expected=0.05 match=yes
CLAIM Q5: computed=0.025 expected=0.025 match=yes
CLAIM Q6: computed=2.5 expected=2.5 match=yes
CLAIM Q7: computed=0.01 expected=0.01 match=yes
CLAIM Q8: computed=1 expected=1.0 match=yes
CLAIM Q9: computed=0.03 expected=0.03 match=yes
CLAIM Q10: computed=0.04 expected=0.04 match=yes
CLAIM Q11: computed=1.25 expected=1.25 match=yes
VERIFICATION SUMMARY: 11 claims, 11 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.5 | 0.5 | yes | match | 3 significant digits (as printed, at least 3) |
| Q2 | 0.5 | 0.5 | yes | match | 3 significant digits (as printed, at least 3) |
| Q3 | 0.1 | 0.1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.05 | 0.05 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.025 | 0.025 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 2.5 | 2.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 0.01 | 0.01 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 1 | 1.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 0.03 | 0.03 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 0.04 | 0.04 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 1.25 | 1.25 | yes | match | 3 significant digits (as printed, at least 3) |

Mismatches: 0 of 11.
