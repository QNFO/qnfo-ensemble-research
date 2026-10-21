# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The code size for p=3, t=1 is n_1 = 5.",
    "inputs": "p = 3, t = 1",
    "formula": "n_t = 1 + \\frac{(p+1)(p^{t}-1)}{p-1}"
  },
  {
    "id": "Q2",
    "statement": "The code size for p=3, t=2 is n_2 = 17.",
    "inputs": "p = 3, t = 2",
    "formula": "n_t = 1 + \\frac{(p+1)(p^{t}-1)}{p-1}"
  },
  {
    "id": "Q3",
    "statement": "The code size for p=3, t=3 is n_3 = 53.",
    "inputs": "p = 3, t = 3",
    "formula": "n_t = 1 + \\frac{(p+1)(p^{t}-1)}{p-1}"
  },
  {
    "id": "Q4",
    "statement": "The code size for p=2, t=1 is n_1 = 4.",
    "inputs": "p = 2, t = 1",
    "formula": "n_t = 1 + \\frac{(p+1)(p^{t}-1)}{p-1}"
  },
  {
    "id": "Q5",
    "statement": "The code size for p=2, t=2 is n_2 = 10.",
    "inputs": "p = 2, t = 2",
    "formula": "n_t = 1 + \\frac{(p+1)(p^{t}-1)}{p-1}"
  },
  {
    "id": "Q6",
    "statement": "The code size for p=2, t=3 is n_3 = 22.",
    "inputs": "p = 2, t = 3",
    "formula": "n_t = 1 + \\frac{(p+1)(p^{t}-1)}{p-1}"
  },
  {
    "id": "Q7",
    "statement": "The code distance for t=1 is d = 3.",
    "inputs": "t = 1",
    "formula": "d = 2t + 1"
  },
  {
    "id": "Q8",
    "statement": "The passive logical‑failure probability for p=3, t=1, ε=10^{-3} is P_{\\mathrm{pass}} ≈ 9.98\\times10^{-6}.",
    "inputs": "n = 5, ε = 10^{-3}",
    "formula": "P_{\\mathrm{pass}} = \\sum_{k=2}^{5} \\binom{5}{k} \\varepsilon^{k} (1-\\varepsilon)^{5-k}"
  },
  {
    "id": "Q9",
    "statement": "The suppression factor ε / P_{\\mathrm{pass}} ≈ 100.2.",
    "inputs": "ε = 10^{-3}, P_{\\mathrm{pass}} = 9.98\\times10^{-6}",
    "formula": "(ε) / (P_{\\mathrm{pass}})"
  },
  {
    "id": "Q10",
    "statement": "The passive logical‑failure probability for p=3, t=2, ε=10^{-3} is P_{\\mathrm{pass}}^{(2)} ≈ 6.73\\times10^{-7}.",
    "inputs": "n = 17, ε = 10^{-3}",
    "formula": "P_{\\mathrm{pass}}^{(2)} = \\sum_{k=3}^{17} \\binom{17}{k} \\varepsilon^{k} (1-\\varepsilon)^{17-k}"
  },
  {
    "id": "Q11",
    "statement": "The suppression factor ε / P_{\\mathrm{pass}}^{(2)} ≈ 1.49\\times10^{3}.",
    "inputs": "ε = 10^{-3}, P_{\\mathrm{pass}}^{(2)} = 6.73\\times10^{-7}",
    "formula": "(ε) / (P_{\\mathrm{pass}}^{(2)})"
  },
  {
    "id": "Q12",
    "statement": "The barrier height for d=3 is B(3) = 8.",
    "inputs": "d = 3",
    "formula": "B(d) = 2^{d}"
  },
  {
    "id": "Q13",
    "statement": "The barrier height for d=4 is B(4) = 16.",
    "inputs": "d = 4",
    "formula": "B(d) = 2^{d}"
  },
  {
    "id": "Q14",
    "statement": "The logical‑error bound for d=3 with p_{\\mathrm{err}}=0.40 is p_L(3) = 6.5536\\times10^{-4}.",
    "inputs": "p_{\\mathrm{err}} = 0.40, B = 8",
    "formula": "p_L(d) = p_{\\mathrm{err}}^{B(d)}"
  },
  {
    "id": "Q15",
    "statement": "The logical‑error bound for d=4 with p_{\\mathrm{err}}=0.40 is p_L(4) = 4.295\\times10^{-7}.",
    "inputs": "p_{\\mathrm{err}} = 0.40, B = 16",
    "formula": "p_L(d) = p_{\\mathrm{err}}^{B(d)}"
  },
  {
    "id": "Q16",
    "statement": "The suppression factor p_{\\mathrm{err}} / p_L(3) ≈ 6.10\\times10^{2}.",
    "inputs": "p_{\\mathrm{err}} = 0.40, p_L(3) = 6.5536\\times10^{-4}",
    "formula": "(p_{\\mathrm{err}}) / (p_L(3))"
  }
]

## Script
```python
import math
from fractions import Fraction

def round_sig(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Claims data: (id, computed function, expected string, sig figs)
claims = [
    ("Q1", lambda: 1 + ((3+1)*(3**1 - 1)) // (3-1), "5", 1),
    ("Q2", lambda: 1 + ((3+1)*(3**2 - 1)) // (3-1), "17", 2),
    ("Q3", lambda: 1 + ((3+1)*(3**3 - 1)) // (3-1), "53", 2),
    ("Q4", lambda: 1 + ((2+1)*(2**1 - 1)) // (2-1), "4", 1),
    ("Q5", lambda: 1 + ((2+1)*(2**2 - 1)) // (2-1), "10", 2),
    ("Q6", lambda: 1 + ((2+1)*(2**3 - 1)) // (2-1), "22", 2),
    ("Q7", lambda: 2*1 + 1, "3", 1),
    ("Q8", lambda: sum(math.comb(5, k) * (1e-3)**k * (1-1e-3)**(5-k) for k in range(2,6)),
     "9.98e-6", 3),
    ("Q9", lambda: 1e-3 / (9.98e-6), "100.2", 4),
    ("Q10", lambda: sum(math.comb(17, k) * (1e-3)**k * (1-1e-3)**(17-k) for k in range(3,18)),
     "6.73e-7", 3),
    ("Q11", lambda: 1e-3 / (6.73e-7), "1.49e3", 3),
    ("Q12", lambda: 2**3, "8", 1),
    ("Q13", lambda: 2**4, "16", 2),
    ("Q14", lambda: 0.40**8, "6.5536e-4", 5),
    ("Q15", lambda: 0.40**16, "4.295e-7", 4),
    ("Q16", lambda: 0.40 / (6.5536e-4), "6.10e2", 3),
]

def parse_expected(s):
    """Convert expected string to float."""
    return float(s.replace('e', 'E'))

def match_value(comp, exp_str, sig):
    exp = parse_expected(exp_str)
    comp_rounded = round_sig(comp, sig)
    exp_rounded = round_sig(exp, sig)
    return comp_rounded == exp_rounded

print("VERIFICATION SUMMARY:")
match_count = 0
for cid, func, exp_str, sig in claims:
    comp = func()
    is_match = match_value(comp, exp_str, sig)
    match_word = "yes" if is_match else "no"
    if is_match:
        match_count += 1
    # format computed with enough digits
    if abs(comp) >= 1e-3:
        comp_str = f"{comp:.8g}"
    else:
        comp_str = f"{comp:.8e}"
    print(f"CLAIM {cid}: computed={comp_str} expected={exp_str} match={match_word}")

total = len(claims)
print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {total - match_count} mismatch")

```

## Execution output
```
VERIFICATION SUMMARY:
CLAIM Q1: computed=5 expected=5 match=yes
CLAIM Q2: computed=17 expected=17 match=yes
CLAIM Q3: computed=53 expected=53 match=yes
CLAIM Q4: computed=4 expected=4 match=yes
CLAIM Q5: computed=10 expected=10 match=yes
CLAIM Q6: computed=22 expected=22 match=yes
CLAIM Q7: computed=3 expected=3 match=yes
CLAIM Q8: computed=9.98001500e-06 expected=9.98e-6 match=yes
CLAIM Q9: computed=100.2004 expected=100.2 match=yes
CLAIM Q10: computed=6.72897005e-07 expected=6.73e-7 match=yes
CLAIM Q11: computed=1485.8841 expected=1.49e3 match=yes
CLAIM Q12: computed=8 expected=8 match=yes
CLAIM Q13: computed=16 expected=16 match=yes
CLAIM Q14: computed=6.55360000e-04 expected=6.5536e-4 match=yes
CLAIM Q15: computed=4.29496730e-07 expected=4.295e-7 match=yes
CLAIM Q16: computed=610.35156 expected=6.10e2 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 5 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 17 | 17 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 53 | 53 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 10 | 10 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 22 | 22 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 9.98001500e-06 | 9.98e-6 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 100.2004 | 100.2 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 6.72897005e-07 | 6.73e-7 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 1485.8841 | 1.49e3 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 16 | 16 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 6.55360000e-04 | 6.5536e-4 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q15 | 4.29496730e-07 | 4.295e-7 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q16 | 610.35156 | 6.10e2 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
