# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The observed spectral gap is δ = 2 - μ ≈ 0.016.",
    "inputs": "μ = 1.984",
    "formula": "δ = 2 - μ"
  },
  {
    "id": "Q2",
    "statement": "The universal prime lower bound for the Laplacian eigenvalue is λ_gap = (p+1) - 2√p ≈ 0.17157288 when p = 2.",
    "inputs": "p = 2",
    "formula": "λ_gap = (p+1) - 2*sqrt(p)"
  },
  {
    "id": "Q3",
    "statement": "The number of vertices at exact depth 10 for a (p+1)-regular tree with p = 2 is N₁₀ = 1536.",
    "inputs": "p = 2, d = 10",
    "formula": "N_d = (p+1) * p^{d-1}"
  },
  {
    "id": "Q4",
    "statement": "The total number of vertices in the ball of radius 10 for p = 2 is V₁₀ = 3070.",
    "inputs": "p = 2, d = 10",
    "formula": "V_d = 1 + (p+1)*(p^{d} - 1)/(p-1)"
  },
  {
    "id": "Q5",
    "statement": "The total number of vertices in the ball of radius 12 for p = 2 is V₁₂ = 12286.",
    "inputs": "p = 2, d = 12",
    "formula": "V_d = 1 + (p+1)*(p^{d} - 1)/(p-1)"
  },
  {
    "id": "Q6",
    "statement": "The number of vertices at exact depth 7 for p = 2 is N₇ = 192.",
    "inputs": "p = 2, d = 7",
    "formula": "N_d = (p+1) * p^{d-1}"
  },
  {
    "id": "Q7",
    "statement": "The total number of vertices in the ball of radius 7 for p = 2 is V₇ = 382.",
    "inputs": "p = 2, d = 7",
    "formula": "V_d = 1 + (p+1)*(p^{d} - 1)/(p-1)"
  },
  {
    "id": "Q8",
    "statement": "For a composite integer with depth D = 7 the spectral‑gap bound satisfies λ ≤ C/D ≤ 2/7 ≈ 0.2857.",
    "inputs": "C = 2, D = 7",
    "formula": "λ ≤ C/D"
  },
  {
    "id": "Q9",
    "statement": "For the composite integer N = 255 with depth D = 9 the composite‑gap bound gives λ ≤ C/D = 2/9 ≈ 0.222.",
    "inputs": "C = 2, D = 9",
    "formula": "λ ≤ C/D"
  },
  {
    "id": "Q10",
    "statement": "The depth for N = 101 is D = ⌈log₂ 101⌉ = 7.",
    "inputs": "N = 101",
    "formula": "D = ceil(log₂ N)"
  },
  {
    "id": "Q11",
    "statement": "The depth for N = 100 is D = ⌈log₂ 100⌉ = 7.",
    "inputs": "N = 100",
    "formula": "D = ceil(log₂ N)"
  },
  {
    "id": "Q12",
    "statement": "The depth for N = 257 is D = ⌈log₂ 257⌉ = 9.",
    "inputs": "N = 257",
    "formula": "D = ceil(log₂ N)"
  },
  {
    "id": "Q13",
    "statement": "The total number of vertices in the ball of radius 9 for p = 2 is V₉ = 1534.",
    "inputs": "p = 2, d = 9",
    "formula": "V_d = 1 + (p+1)*(p^{d} - 1)/(p-1)"
  },
  {
    "id": "Q14",
    "statement": "The projected bit‑operation cost for a 1024‑bit integer is ≈5×10²·(1024)⁶ ≈ 5.8×10²⁰.",
    "inputs": "factor = 5×10², log₂ N = 1024",
    "formula": "cost = 5e2 * (log₂ N)^6"
  },
  {
    "id": "Q15",
    "statement": "The linear depth model predicts f_res = (α+β+γ)·D = 0.9·6 = 5.4 for D = 6 with α = 0.40, β = 0.30, γ = 0.20.",
    "inputs": "α = 0.40, β = 0.30, γ = 0.20, D = 6",
    "formula": "f_res = (α + β + γ) * D"
  }
]

## Script
```python
import math

def fmt(x, fmt_str):
    return fmt_str.format(x)

def compare(computed, expected_str):
    # Remove any approx symbols and whitespace
    exp = expected_str.replace('≈', '').replace('~', '').strip()
    # Determine if expected is in scientific notation
    if 'e' in exp or 'E' in exp:
        # Compare as float with tolerance relative
        return abs(computed - float(exp)) / float(exp) < 1e-6
    # Determine decimal places
    if '.' in exp:
        dec = len(exp.split('.')[1])
        return round(computed, dec) == round(float(exp), dec)
    else:
        return int(round(computed)) == int(round(float(exp)))

claims = [
    ("Q1", 2 - 1.984, "0.016"),
    ("Q2", (2+1) - 2*math.sqrt(2), "0.17157288"),
    ("Q3", (2+1)*2**(10-1), "1536"),
    ("Q4", 1 + (2+1)*(2**10 - 1)//(2-1), "3070"),
    ("Q5", 1 + (2+1)*(2**12 - 1)//(2-1), "12286"),
    ("Q6", (2+1)*2**(7-1), "192"),
    ("Q7", 1 + (2+1)*(2**7 - 1)//(2-1), "382"),
    ("Q8", 2/7, "0.2857"),
    ("Q9", 2/9, "0.222"),
    ("Q10", math.ceil(math.log2(101)), "7"),
    ("Q11", math.ceil(math.log2(100)), "7"),
    ("Q12", math.ceil(math.log2(257)), "9"),
    ("Q13", 1 + (2+1)*(2**9 - 1)//(2-1), "1534"),
    ("Q14", 5e2 * (1024**6), "5.8e20"),
    ("Q15", (0.40+0.30+0.20)*6, "5.4"),
]

for cid, comp, exp in claims:
    match = "yes" if compare(comp, exp) else "no"
    # Use scientific notation for large numbers
    if abs(comp) >= 1e6:
        comp_str = "{:.8e}".format(comp)
    else:
        comp_str = "{:.8f}".format(comp).rstrip('0').rstrip('.')
    print(f"CLAIM {cid}: computed={comp_str} expected={exp} match={match}")

print("VERIFICATION SUMMARY: {} claims, {} match, {} mismatch".format(
    len(claims),
    sum(1 for _,c,e in claims if compare(c,e)),
    sum(1 for _,c,e in claims if not compare(c,e))
))

```

## Execution output
```
CLAIM Q1: computed=0.016 expected=0.016 match=yes
CLAIM Q2: computed=0.17157288 expected=0.17157288 match=yes
CLAIM Q3: computed=1536 expected=1536 match=yes
CLAIM Q4: computed=3070 expected=3070 match=yes
CLAIM Q5: computed=12286 expected=12286 match=yes
CLAIM Q6: computed=192 expected=192 match=yes
CLAIM Q7: computed=382 expected=382 match=yes
CLAIM Q8: computed=0.28571429 expected=0.2857 match=yes
CLAIM Q9: computed=0.22222222 expected=0.222 match=yes
CLAIM Q10: computed=7 expected=7 match=yes
CLAIM Q11: computed=7 expected=7 match=yes
CLAIM Q12: computed=9 expected=9 match=yes
CLAIM Q13: computed=1534 expected=1534 match=yes
CLAIM Q14: computed=5.76460752e+20 expected=5.8e20 match=no
CLAIM Q15: computed=5.4 expected=5.4 match=yes
VERIFICATION SUMMARY: 15 claims, 14 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.016 | 0.016 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.17157288 | 0.17157288 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q3 | 1536 | 1536 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 3070 | 3070 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 12286 | 12286 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 192 | 192 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q7 | 382 | 382 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 0.28571429 | 0.2857 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 0.22222222 | 0.222 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 7 | 7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 7 | 7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 9 | 9 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 1534 | 1534 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q14 | 5.76460752e+20 | 5.8e20 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 5.4 | 5.4 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 15.
