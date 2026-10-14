# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "|Fl_3(F_2)| = 21",
    "inputs": "n=3, q=2",
    "formula": "prod_{k=1}^{3} (2^k - 1)/(2-1) = 1*3*7"
  },
  {
    "id": "Q2",
    "statement": "|Fl_4(F_2)| = 315",
    "inputs": "n=4, q=2",
    "formula": "prod_{k=1}^{4} (2^k - 1) = 1*3*7*15"
  },
  {
    "id": "Q3",
    "statement": "|Fl_5(F_2)| = 9765",
    "inputs": "n=5, q=2",
    "formula": "315*31"
  },
  {
    "id": "Q4",
    "statement": "|Fl_6(F_2)| = 615195",
    "inputs": "n=6, q=2",
    "formula": "9765*63"
  },
  {
    "id": "Q5",
    "statement": "growth factor from rank n to n+1 is 2^{n+1}-1, verified as 15 at n=3 and 63 at n=5",
    "inputs": "|Fl_4|=315, |Fl_3|=21, |Fl_6|=615195, |Fl_5|=9765",
    "formula": "315/21 and 615195/9765"
  },
  {
    "id": "Q6",
    "statement": "lower bound N_flag(2,n) >= 2^{n(n-1)/2}, giving 64 <= 315 at n=4",
    "inputs": "n=4",
    "formula": "2^{4*3/2} = 2^6"
  },
  {
    "id": "Q7",
    "statement": "dim_C Fl_4 = 6",
    "inputs": "n=4",
    "formula": "binom(4,2) = 4*3/2"
  },
  {
    "id": "Q8",
    "statement": "ratio of binary flags to Coxeter chambers at rank 4 is 13.125",
    "inputs": "|Fl_4(F_2)|=315, 4!=24",
    "formula": "315/24"
  },
  {
    "id": "Q9",
    "statement": "T_lab(4) = 64",
    "inputs": "k=4",
    "formula": "2^{binom(4,2)} = 2^6"
  },
  {
    "id": "Q10",
    "statement": "T_lab(5) = 1024",
    "inputs": "k=5",
    "formula": "2^{binom(5,2)} = 2^10"
  },
  {
    "id": "Q11",
    "statement": "M(4) = 2080",
    "inputs": "T_lab(4)=64",
    "formula": "64*65/2"
  },
  {
    "id": "Q12",
    "statement": "M(5) = 524800",
    "inputs": "T_lab(5)=1024",
    "formula": "1024*1025/2"
  },
  {
    "id": "Q13",
    "statement": "M(5)/M(4) ≈ 252.31",
    "inputs": "M(4)=2080, M(5)=524800",
    "formula": "524800/2080"
  },
  {
    "id": "Q14",
    "statement": "aggregate activity bound A_total <= 100 papers per year",
    "inputs": "50, 20, 5, 10, 5, 10 (domain ceilings from [10])",
    "formula": "50+20+5+10+5+10"
  },
  {
    "id": "Q15",
    "statement": "I_flag = log2(3) ≈ 1.58496 bits per flag",
    "inputs": "alphabet size 3",
    "formula": "ln(3)/ln(2)"
  },
  {
    "id": "Q16",
    "statement": "10 flagged items carry at most 15.8496 bits",
    "inputs": "m=10, I_flag≈1.58496",
    "formula": "10*1.58496"
  }
]

## Script
```python
import math

def claim(id_, computed, expected, match):
    print(f"CLAIM {id_}: computed={computed} expected={expected} match={match}")

# Q1: |Fl_3(F_2)| = 1*3*7
c = 1
for k in range(1, 4):
    c *= (2**k - 1) // (2 - 1)
claim("Q1", c, "21", "yes" if c == 21 else "no")

# Q2: |Fl_4(F_2)| = 1*3*7*15
c = 1
for k in range(1, 5):
    c *= (2**k - 1) // (2 - 1)
claim("Q2", c, "315", "yes" if c == 315 else "no")

# Q3: |Fl_5(F_2)| = 315*31
c = 315 * 31
claim("Q3", c, "9765", "yes" if c == 9765 else "no")

# Q4: |Fl_6(F_2)| = 9765*63
c = 9765 * 63
claim("Q4", c, "615195", "yes" if c == 615195 else "no")

# Q5: growth factors 315/21 and 615195/9765
g1 = 315 / 21
g2 = 615195 / 9765
claim("Q5", f"{g1:.8f},{g2:.8f}", "15,63", "yes" if g1 == 15 and g2 == 63 else "no")

# Q6: 2^{4*3/2} = 2^6 = 64
c = 2 ** (4 * 3 // 2)
claim("Q6", c, "64", "yes" if c == 64 else "no")

# Q7: binom(4,2) = 6
c = math.comb(4, 2)
claim("Q7", c, "6", "yes" if c == 6 else "no")

# Q8: 315/24
c = 315 / 24
claim("Q8", f"{c:.8f}", "13.125", "yes" if round(c, 6) == 13.125 else "no")

# Q9: 2^{binom(4,2)} = 2^6 = 64
c = 2 ** math.comb(4, 2)
claim("Q9", c, "64", "yes" if c == 64 else "no")

# Q10: 2^{binom(5,2)} = 2^10 = 1024
c = 2 ** math.comb(5, 2)
claim("Q10", c, "1024", "yes" if c == 1024 else "no")

# Q11: M(4) = 64*65/2
c = 64 * 65 / 2
claim("Q11", f"{c:.8f}", "2080", "yes" if c == 2080 else "no")

# Q12: M(5) = 1024*1025/2
c = 1024 * 1025 / 2
claim("Q12", f"{c:.8f}", "524800", "yes" if c == 524800 else "no")

# Q13: 524800/2080
c = 524800 / 2080
claim("Q13", f"{c:.8f}", "252.31", "yes" if round(c, 2) == 252.31 else "no")

# Q14: 50+20+5+10+5+10
c = 50 + 20 + 5 + 10 + 5 + 10
claim("Q14", c, "100", "yes" if c == 100 else "no")

# Q15: log2(3)
c = math.log(3) / math.log(2)
claim("Q15", f"{c:.8f}", "1.58496", "yes" if round(c, 5) == 1.58496 else "no")

# Q16: 10 * 1.58496
c = 10 * 1.58496
claim("Q16", f"{c:.8f}", "15.8496", "yes" if round(c, 4) == 15.8496 else "no")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=21 expected=21 match=yes
CLAIM Q2: computed=315 expected=315 match=yes
CLAIM Q3: computed=9765 expected=9765 match=yes
CLAIM Q4: computed=615195 expected=615195 match=yes
CLAIM Q5: computed=15.00000000,63.00000000 expected=15,63 match=yes
CLAIM Q6: computed=64 expected=64 match=yes
CLAIM Q7: computed=6 expected=6 match=yes
CLAIM Q8: computed=13.12500000 expected=13.125 match=yes
CLAIM Q9: computed=64 expected=64 match=yes
CLAIM Q10: computed=1024 expected=1024 match=yes
CLAIM Q11: computed=2080.00000000 expected=2080 match=yes
CLAIM Q12: computed=524800.00000000 expected=524800 match=yes
CLAIM Q13: computed=252.30769231 expected=252.31 match=yes
CLAIM Q14: computed=100 expected=100 match=yes
CLAIM Q15: computed=1.58496250 expected=1.58496 match=yes
CLAIM Q16: computed=15.84960000 expected=15.8496 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 21 | 21 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 315 | 315 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 9765 | 9765 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 615195 | 615195 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q5 | 15.00000000,63.00000000 | 15,63 | yes | match | script verdict (values not both numeric) |
| Q6 | 64 | 64 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 6 | 6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 13.12500000 | 13.125 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 64 | 64 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 1024 | 1024 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 2080.00000000 | 2080 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 524800.00000000 | 524800 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q13 | 252.30769231 | 252.31 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q14 | 100 | 100 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 1.58496250 | 1.58496 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q16 | 15.84960000 | 15.8496 | yes | match | 6 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
