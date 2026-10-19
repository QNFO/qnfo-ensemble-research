# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The fixed weights sum to exactly 1.00.",
    "inputs": "w1=0.30, w2=0.25, w3=0.20, w4=0.15, w5=0.10",
    "formula": "w1 + w2 + w3 + w4 + w5"
  },
  {
    "id": "Q2",
    "statement": "The gap density per category is 8.4 gaps per category.",
    "inputs": "N_gaps=42, N_cat=5",
    "formula": "N_gaps / N_cat"
  },
  {
    "id": "Q3",
    "statement": "The roadmap transition duration is 2.0 weeks per version transition.",
    "inputs": "W=8 weeks, N_ver=5 version labels",
    "formula": "W / (N_ver - 1)"
  },
  {
    "id": "Q4",
    "statement": "The version‑label density is 0.625 versions per week.",
    "inputs": "N_ver=5, W=8 weeks",
    "formula": "N_ver / W"
  },
  {
    "id": "Q5",
    "statement": "Uniform pacing gives a mean time per gap of 0.1905 weeks per gap.",
    "inputs": "W=8 weeks, N_gaps=42",
    "formula": "W / N_gaps"
  },
  {
    "id": "Q6",
    "statement": "The mean time per gap expressed in days is approximately 1.333 days per gap.",
    "inputs": "t_gap_weeks = 4/21 weeks (derived from Q5), conversion factor 7 days per week",
    "formula": "t_gap_weeks * 7"
  },
  {
    "id": "Q7",
    "statement": "The upper‑bound mean token count per language is 1.5×10¹¹ tokens per language.",
    "inputs": "T_tot=3.0×10¹³ tokens, L=200 languages",
    "formula": "T_tot / L"
  },
  {
    "id": "Q8",
    "statement": "Projected storage lower bound is 30 TB.",
    "inputs": "T_tot=3.0×10¹³ tokens, b=1 byte per token, 1 TB = 10¹² bytes",
    "formula": "(T_tot * b) / 10¹²"
  },
  {
    "id": "Q9",
    "statement": "Projected storage central estimate is 120 TB.",
    "inputs": "T_tot=3.0×10¹³ tokens, b=4 bytes per token, 1 TB = 10¹² bytes",
    "formula": "(T_tot * b) / 10¹²"
  },
  {
    "id": "Q10",
    "statement": "Projected storage upper bound is 150 TB (including 25 % annotation overhead).",
    "inputs": "central bytes = 1.2×10¹⁴ bytes (from Q9), overhead factor = 1.25, 1 TB = 10¹² bytes",
    "formula": "(1.2×10¹⁴ * 1.25) / 10¹²"
  },
  {
    "id": "Q11",
    "statement": "The unpruned number of pairwise audit checks for n=20 is 190.",
    "inputs": "n=20",
    "formula": "n*(n-1)/2"
  },
  {
    "id": "Q12",
    "statement": "After pruning with fraction p=0.9, the remaining pairwise checks are 19.",
    "inputs": "P_unpruned=190 (from Q11), p=0.9",
    "formula": "P_unpruned * (1 - p)"
  },
  {
    "id": "Q13",
    "statement": "The falsification index for claim K_A is F = 0.675.",
    "inputs": "w1=0.30, w2=0.25, w3=0.20, w4=0.15, w5=0.10; s1=1, s2=0.5, s3=1, s4=0, s5=0.5",
    "formula": "w1*s1 + w2*s2 + w3*s3 + w4*s4 + w5*s5"
  },
  {
    "id": "Q14",
    "statement": "The falsification index for claim K_B is F = 0.10.",
    "inputs": "w1=0.30, w2=0.25, w3=0.20, w4=0.15, w5=0.10; s1=0, s2=0, s3=0.5, s4=0, s5=0",
    "formula": "w1*s1 + w2*s2 + w3*s3 + w4*s4 + w5*s5"
  },
  {
    "id": "Q15",
    "statement": "Without specification completeness (s1=0), the maximum possible falsification index is 0.70.",
    "inputs": "total weight sum = 1.00, w1=0.30",
    "formula": "1.00 - w1"
  },
  {
    "id": "Q16",
    "statement": "Projected audit effort per claim is 50 hours.",
    "inputs": "hours_per_criterion=10, number_of_criteria=5",
    "formula": "hours_per_criterion * number_of_criteria"
  }
]

## Script
```python
import math

def decimal_places(s):
    """Return number of decimal places in a numeric string like '0.1905' or '0.10'."""
    if 'e' in s or 'E' in s:
        # scientific notation, count digits after decimal in mantissa
        mantissa = s.split('e')[0]
        if '.' in mantissa:
            return len(mantissa.split('.')[1])
        else:
            return 0
    if '.' in s:
        return len(s.split('.')[1])
    return 0

def format_match(computed, expected):
    """Round computed to the same decimal precision as expected and format."""
    dp = decimal_places(expected)
    if dp > 0:
        fmt = f"{{:.{dp}f}}"
        comp_str = fmt.format(computed)
    else:
        # integer or scientific mantissa without decimal
        comp_str = f"{computed:.0f}"
    # handle scientific notation expected
    if 'e' in expected or 'E' in expected:
        comp_str = f"{float(comp_str):.1e}" if '.' in expected else f"{float(comp_str):.0e}"
    return comp_str

def main():
    claims = [
        # Q1
        ("Q1", 0.30 + 0.25 + 0.20 + 0.15 + 0.10, "1.00"),
        # Q2
        ("Q2", 42 / 5, "8.4"),
        # Q3
        ("Q3", 8 / (5 - 1), "2.0"),
        # Q4
        ("Q4", 5 / 8, "0.625"),
        # Q5
        ("Q5", 8 / 42, "0.1905"),
        # Q6
        ("Q6", (8 / 42) * 7, "1.333"),
        # Q7
        ("Q7", 3.0e13 / 200, "1.5e11"),
        # Q8
        ("Q8", (3.0e13 * 1) / 1e12, "30"),
        # Q9
        ("Q9", (3.0e13 * 4) / 1e12, "120"),
        # Q10
        ("Q10", (1.2e14 * 1.25) / 1e12, "150"),
        # Q11
        ("Q11", 20 * 19 / 2, "190"),
        # Q12
        ("Q12", 190 * (1 - 0.9), "19"),
        # Q13
        ("Q13", 0.30*1 + 0.25*0.5 + 0.20*1 + 0.15*0 + 0.10*0.5, "0.675"),
        # Q14
        ("Q14", 0.30*0 + 0.25*0 + 0.20*0.5 + 0.15*0 + 0.10*0, "0.10"),
        # Q15
        ("Q15", 1.00 - 0.30, "0.70"),
        # Q16
        ("Q16", 10 * 5, "50")
    ]

    for cid, comp, expected in claims:
        comp_str = format_match(comp, expected)
        match = "yes" if comp_str == expected else "no"
        print(f"CLAIM {cid}: computed={comp_str} expected={expected} match={match}")

    print(f"VERIFICATION SUMMARY: {len(claims)} claims, "
          f"{sum(1 for _,c,e in claims if format_match(c,e)==e)} match, "
          f"{sum(1 for _,c,e in claims if format_match(c,e)!=e)} mismatch")

if __name__ == "__main__":
    main()

```

## Execution output
```
CLAIM Q1: computed=1.00 expected=1.00 match=yes
CLAIM Q2: computed=8.4 expected=8.4 match=yes
CLAIM Q3: computed=2.0 expected=2.0 match=yes
CLAIM Q4: computed=0.625 expected=0.625 match=yes
CLAIM Q5: computed=0.1905 expected=0.1905 match=yes
CLAIM Q6: computed=1.333 expected=1.333 match=yes
CLAIM Q7: computed=1.5e+11 expected=1.5e11 match=no
CLAIM Q8: computed=30 expected=30 match=yes
CLAIM Q9: computed=120 expected=120 match=yes
CLAIM Q10: computed=150 expected=150 match=yes
CLAIM Q11: computed=190 expected=190 match=yes
CLAIM Q12: computed=19 expected=19 match=yes
CLAIM Q13: computed=0.675 expected=0.675 match=yes
CLAIM Q14: computed=0.10 expected=0.10 match=yes
CLAIM Q15: computed=0.70 expected=0.70 match=yes
CLAIM Q16: computed=50 expected=50 match=yes
VERIFICATION SUMMARY: 16 claims, 15 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.00 | 1.00 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 8.4 | 8.4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 2.0 | 2.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 0.625 | 0.625 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 0.1905 | 0.1905 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 1.333 | 1.333 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 1.5e+11 | 1.5e11 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 30 | 30 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 120 | 120 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 150 | 150 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 190 | 190 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 19 | 19 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 0.675 | 0.675 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 0.10 | 0.10 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 0.70 | 0.70 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q16 | 50 | 50 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
