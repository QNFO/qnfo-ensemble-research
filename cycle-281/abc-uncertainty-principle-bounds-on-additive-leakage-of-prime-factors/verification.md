# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The logarithm of the inverse complementarity constant is $\\log_2(1/c)=1$ bit.",
    "inputs": "c = 1/2",
    "formula": "$\\log_2\\bigl(1/c\\bigr)$"
  },
  {
    "id": "Q2",
    "statement": "The GUP reduction factor is $0.60$, obtained from a $40\\%$ reduction.",
    "inputs": "reduction = 40\\% = 0.40",
    "formula": "$1 - 0.40$"
  },
  {
    "id": "Q3",
    "statement": "The raw information‑exclusion bound $r$ equals $1$ bit.",
    "inputs": "c = 1/2",
    "formula": "$r = \\log_2\\bigl(1/c\\bigr)$"
  },
  {
    "id": "Q4",
    "statement": "Applying the GUP factor yields $r_{\\text{eff}} = 0.60$ bits.",
    "inputs": "r = 1 bit, GUP factor = 0.60",
    "formula": "$r_{\\text{eff}} = r \\times 0.60$"
  },
  {
    "id": "Q5",
    "statement": "The final leakage bound is $I(R\\!:\\!B) \\le 0.60$ bits.",
    "inputs": "r_{\\text{eff}} = 0.60 bits",
    "formula": "$I \\le r_{\\text{eff}}$"
  },
  {
    "id": "Q6",
    "statement": "For $c=0.8$, $\\log_2(1/c)=0.321928$ bits.",
    "inputs": "c = 0.8",
    "formula": "$\\log_2\\bigl(1/0.8\\bigr)$"
  },
  {
    "id": "Q7",
    "statement": "For $c=0.8$, the effective bound is $I_{\\text{eff}} = 0.193157$ bits.",
    "inputs": "c = 0.8, GUP factor = 0.60",
    "formula": "$I_{\\text{eff}} = 0.60 \\times \\log_2(1/0.8)$"
  },
  {
    "id": "Q8",
    "statement": "For $c=0.9$, $\\log_2(1/c)=0.152003$ bits and $I_{\\text{eff}} = 0.091202$ bits.",
    "inputs": "c = 0.9, GUP factor = 0.60",
    "formula": "$I_{\\text{eff}} = 0.60 \\times \\log_2(1/0.9)$"
  },
  {
    "id": "Q9",
    "statement": "For $c=0.99$, $\\log_2(1/c)=0.014355$ bits and $I_{\\text{eff}} = 0.008613$ bits.",
    "inputs": "c = 0.99, GUP factor = 0.60",
    "formula": "$I_{\\text{eff}} = 0.60 \\times \\log_2(1/0.99)$"
  },
  {
    "id": "Q10",
    "statement": "With a conditional min‑entropy $h=0.2$ bits, the bound becomes $I_{\\text{eff}} = 0.80$ bits.",
    "inputs": "GUP factor = 0.60, $\\log_2(1/c)=1$ bit, $h=0.2$ bits",
    "formula": "$I_{\\text{eff}} = 0.60 \\times 1 + 0.2$"
  },
  {
    "id": "Q11",
    "statement": "The holographic entropy bound converts to $S_{\\text{max}}^{\\text{bits}} \\approx 9.06$ bits.",
    "inputs": "$\\pi \\approx 3.14159265$, $\\ln 2 \\approx 0.69314718$",
    "formula": "$S_{\\text{max}}^{\\text{bits}} = \\frac{2\\pi}{\\ln 2}$"
  },
  {
    "id": "Q12",
    "statement": "Applying the GUP factor to the holographic bound gives $S_{\\text{eff}}^{\\text{bits}} = 5.44$ bits.",
    "inputs": "S_{\\text{max}}^{\\text{bits}} \\approx 9.06, GUP factor = 0.60",
    "formula": "$S_{\\text{eff}}^{\\text{bits}} = 0.60 \\times 9.06$"
  },
  {
    "id": "Q13",
    "statement": "The anharmonic leakage fraction is $L_2 = 0.02$.",
    "inputs": "$\\Omega/|\\alpha| = 0.05$, $\\sin^2(\\alpha T_g/2)=1$",
    "formula": "$L_2 = 8\\times (0.05)^2 \\times 1$"
  },
  {
    "id": "Q14",
    "statement": "The corresponding mutual information is $I_{\\text{anh}} \\approx 0.112$ bits.",
    "inputs": "L_2 = 0.02",
    "formula": "$I_{\\text{anh}} = -L_2\\log_2 L_2 -(1-L_2)\\log_2(1-L_2)$"
  },
  {
    "id": "Q15",
    "statement": "The projected cost for a validation experiment is approximately $\\$25{,}000$.",
    "inputs": "2 person‑months cost $\\$15{,}000$, oscilloscope cost $\\$10{,}000$",
    "formula": "$\\$15{,}000 + \\$10{,}000$"
  }
]

## Script
```python
import math

def round_to_match(value, expected_str):
    """Round value to the same number of decimal places as in expected_str."""
    if '.' in expected_str:
        dec_places = len(expected_str.split('.')[1])
        fmt = f"{{:.{dec_places}f}}"
        return fmt.format(value)
    else:
        # integer expected
        return str(int(round(value)))

def check_match(computed, expected_str):
    """Return 'yes' if rounded computed matches expected string, else 'no'."""
    rounded = round_to_match(computed, expected_str)
    return 'yes' if rounded == expected_str else 'no', rounded

claims = [
    # Q1
    ("Q1", lambda: math.log2(1/(0.5)), "1"),
    # Q2
    ("Q2", lambda: 1 - 0.40, "0.60"),
    # Q3
    ("Q3", lambda: math.log2(1/(0.5)), "1"),
    # Q4
    ("Q4", lambda: math.log2(1/(0.5)) * 0.60, "0.60"),
    # Q5
    ("Q5", lambda: 0.60, "0.60"),
    # Q6
    ("Q6", lambda: math.log2(1/0.8), "0.321928"),
    # Q7
    ("Q7", lambda: 0.60 * math.log2(1/0.8), "0.193157"),
    # Q8
    ("Q8", lambda: 0.60 * math.log2(1/0.9), "0.091202"),
    # Q9
    ("Q9", lambda: 0.60 * math.log2(1/0.99), "0.008613"),
    # Q10
    ("Q10", lambda: 0.60 * 1 + 0.2, "0.80"),
    # Q11
    ("Q11", lambda: (2 * math.pi) / math.log(2), "9.06"),
    # Q12
    ("Q12", lambda: 0.60 * ((2 * math.pi) / math.log(2)), "5.44"),
    # Q13
    ("Q13", lambda: 8 * (0.05 ** 2) * 1, "0.02"),
    # Q14
    ("Q14", lambda: -0.02 * math.log2(0.02) - 0.98 * math.log2(0.98), "0.112"),
    # Q15
    ("Q15", lambda: 15000 + 10000, "25000"),
]

for cid, func, expected in claims:
    computed = func()
    match, rounded = check_match(computed, expected)
    print(f"CLAIM {cid}: computed={rounded} expected={expected} match={match}")
print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,_,e in claims if check_match(_, e)[0]=='yes') } match, {sum(1 for _,_,e in claims if check_match(_, e)[0]=='no') } mismatch")

```

## Execution output
```
CLAIM Q1: computed=1 expected=1 match=yes
CLAIM Q2: computed=0.60 expected=0.60 match=yes
CLAIM Q3: computed=1 expected=1 match=yes
CLAIM Q4: computed=0.60 expected=0.60 match=yes
CLAIM Q5: computed=0.60 expected=0.60 match=yes
CLAIM Q6: computed=0.321928 expected=0.321928 match=yes
CLAIM Q7: computed=0.193157 expected=0.193157 match=yes
CLAIM Q8: computed=0.091202 expected=0.091202 match=yes
CLAIM Q9: computed=0.008700 expected=0.008613 match=no
CLAIM Q10: computed=0.80 expected=0.80 match=yes
CLAIM Q11: computed=9.06 expected=9.06 match=yes
CLAIM Q12: computed=5.44 expected=5.44 match=yes
CLAIM Q13: computed=0.02 expected=0.02 match=yes
CLAIM Q14: computed=0.141 expected=0.112 match=no
CLAIM Q15: computed=25000 expected=25000 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 55, in <module>
  File "<string>", line 55, in <genexpr>
  File "<string>", line 15, in check_match
  File "<string>", line 11, in round_to_match
TypeError: type function doesn't define __round__ method

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.60 | 0.60 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.60 | 0.60 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.60 | 0.60 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 0.321928 | 0.321928 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q7 | 0.193157 | 0.193157 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q8 | 0.091202 | 0.091202 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 0.008700 | 0.008613 | no | MISMATCH | 4 significant digits (as the paper states, at least 2) |
| Q10 | 0.80 | 0.80 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 9.06 | 9.06 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 5.44 | 5.44 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 0.02 | 0.02 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 0.141 | 0.112 | no | MISMATCH | 3 significant digits (as the paper states, at least 2) |
| Q15 | 25000 | 25000 | yes | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 2 of 15.


## Auto-corrections

The worker corrected these independently-verified values in place of the paper's stated values (deterministic, no model edit):

| claim | stated | corrected |
|---|---|---|
| Q9 | 0.008613 | 0.008700 |
| Q14 | 0.112 | 0.141 |
