# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "For the rational $x=2/3$, the product of its Archimedean and $p$‑adic absolute values equals 1.",
    "inputs": "$|2/3|_2=1/2$, $|2/3|_3=3$, $|2/3|_\\infty=2/3$",
    "formula": "(1/2) \\times 3 \\times (2/3) = 1"
  },
  {
    "id": "Q2",
    "statement": "For the rational $x=5/7$, the product of its Archimedean and $p$‑adic absolute values equals 1.",
    "inputs": "$|5/7|_5=1/5$, $|5/7|_7=7$, $|5/7|_\\infty=5/7$",
    "formula": "(1/5) \\times 7 \\times (5/7) = 1"
  },
  {
    "id": "Q3",
    "statement": "For the rational $x=3/4$, the product of its Archimedean and $p$‑adic absolute values equals 1.",
    "inputs": "$|3/4|_2=4$, $|3/4|_\\infty=3/4$, $|3/4|_3=1/3$",
    "formula": "4 \\times (3/4) \\times (1/3) = 1"
  },
  {
    "id": "Q4",
    "statement": "The number of vertices at distance $n=1$ from the root in the $p=2$ Bruhat–Tits tree is $N_1=3$.",
    "inputs": "branching factor $p+1=3$",
    "formula": "N_1 = p+1 = 3"
  },
  {
    "id": "Q5",
    "statement": "The number of vertices at distance $n=2$ in the $p=2$ tree is $N_2=6$.",
    "inputs": "$p=2$, branching factor $3$",
    "formula": "N_2 = (p+1)\\,p^{1}=3\\times2=6"
  },
  {
    "id": "Q6",
    "statement": "The number of vertices at distance $n=3$ in the $p=2$ tree is $N_3=12$.",
    "inputs": "$p=2$",
    "formula": "N_3 = (p+1)\\,p^{2}=3\\times4=12"
  },
  {
    "id": "Q7",
    "statement": "The number of vertices at distance $n=4$ in the $p=2$ tree is $N_4=24$.",
    "inputs": "$p=2$",
    "formula": "N_4 = (p+1)\\,p^{3}=3\\times8=24"
  },
  {
    "id": "Q8",
    "statement": "The number of vertices at distance $n=5$ in the $p=2$ tree is $N_5=48$.",
    "inputs": "$p=2$",
    "formula": "N_5 = (p+1)\\,p^{4}=3\\times16=48"
  },
  {
    "id": "Q9",
    "statement": "The cumulative vertex count through depth $5$ for $p=2$ is $S_2(5)=94$.",
    "inputs": "$p=2$, $N=5$, formula $S_p(N)=1+(p+1)\\frac{p^{N}-1}{p-1}$",
    "formula": "S_2(5)=1+3\\frac{2^{5}-1}{1}=1+3\\times31=94"
  },
  {
    "id": "Q10",
    "statement": "The number of vertices at distance $n=1$ in the $p=3$ tree is $N_1=4$.",
    "inputs": "branching factor $p+1=4$",
    "formula": "N_1 = p+1 = 4"
  },
  {
    "id": "Q11",
    "statement": "The number of vertices at distance $n=2$ in the $p=3$ tree is $N_2=12$.",
    "inputs": "$p=3$",
    "formula": "N_2 = (p+1)\\,p^{1}=4\\times3=12"
  },
  {
    "id": "Q12",
    "statement": "The number of vertices at distance $n=3$ in the $p=3$ tree is $N_3=36$.",
    "inputs": "$p=3$",
    "formula": "N_3 = (p+1)\\,p^{2}=4\\times9=36"
  },
  {
    "id": "Q13",
    "statement": "The number of vertices at distance $n=4$ in the $p=3$ tree is $N_4=108$.",
    "inputs": "$p=3$",
    "formula": "N_4 = (p+1)\\,p^{3}=4\\times27=108"
  },
  {
    "id": "Q14",
    "statement": "The number of vertices at distance $n=5$ in the $p=3$ tree is $N_5=324$.",
    "inputs": "$p=3$",
    "formula": "N_5 = (p+1)\\,p^{4}=4\\times81=324"
  },
  {
    "id": "Q15",
    "statement": "The cumulative vertex count through depth $5$ for $p=3$ is $S_3(5)=485$.",
    "inputs": "$p=3$, $N=5$, formula $S_p(N)=1+(p+1)\\frac{p^{N}-1}{p-1}$",
    "formula": "S_3(5)=1+4\\frac{3^{5}-1}{2}=1+4\\times121=485"
  },
  {
    "id": "Q16",
    "statement": "With the normalization $\\hbar\\omega=E_0=1$, the Archimedean spectral gap is $\\Delta E^{(\\infty)}_n = 1$ for all $n$.",
    "inputs": "$\\hbar\\omega=E_0=1$",
    "formula": "$\\Delta E^{(\\infty)}_n = E_0 = 1$"
  }
]

## Script
```python
from fractions import Fraction

def fmt(val):
    # format with at least 8 significant digits, remove trailing .0 for integers
    s = f"{float(val):.8g}"
    if s.endswith('.0'):
        s = s[:-2]
    return s

expected = {
    "Q1": "1",
    "Q2": "1",
    "Q3": "1",
    "Q4": "3",
    "Q5": "6",
    "Q6": "12",
    "Q7": "24",
    "Q8": "48",
    "Q9": "94",
    "Q10": "4",
    "Q11": "12",
    "Q12": "36",
    "Q13": "108",
    "Q14": "324",
    "Q15": "485",
    "Q16": "1",
}

# Q1
c1 = Fraction(1,2) * 3 * Fraction(2,3)
# Q2
c2 = Fraction(1,5) * 7 * Fraction(5,7)
# Q3
c3 = 4 * Fraction(3,4) * Fraction(1,3)
# Q4
c4 = 3
# Q5
c5 = 3 * 2
# Q6
c6 = 3 * 4
# Q7
c7 = 3 * 8
# Q8
c8 = 3 * 16
# Q9
c9 = 1 + 3 * (2**5 - 1) // 1  # integer arithmetic
# Q10
c10 = 4
# Q11
c11 = 4 * 3
# Q12
c12 = 4 * 9
# Q13
c13 = 4 * 27
# Q14
c14 = 4 * 81
# Q15
c15 = 1 + 4 * (3**5 - 1) // 2
# Q16
c16 = 1

claims = {
    "Q1": c1,
    "Q2": c2,
    "Q3": c3,
    "Q4": c4,
    "Q5": c5,
    "Q6": c6,
    "Q7": c7,
    "Q8": c8,
    "Q9": c9,
    "Q10": c10,
    "Q11": c11,
    "Q12": c12,
    "Q13": c13,
    "Q14": c14,
    "Q15": c15,
    "Q16": c16,
}

match_count = 0
for qid, val in claims.items():
    comp = fmt(val)
    exp = expected[qid]
    match = "yes" if comp == exp else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {qid}: computed={comp} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims)-match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1 expected=1 match=yes
CLAIM Q2: computed=1 expected=1 match=yes
CLAIM Q3: computed=1 expected=1 match=yes
CLAIM Q4: computed=3 expected=3 match=yes
CLAIM Q5: computed=6 expected=6 match=yes
CLAIM Q6: computed=12 expected=12 match=yes
CLAIM Q7: computed=24 expected=24 match=yes
CLAIM Q8: computed=48 expected=48 match=yes
CLAIM Q9: computed=94 expected=94 match=yes
CLAIM Q10: computed=4 expected=4 match=yes
CLAIM Q11: computed=12 expected=12 match=yes
CLAIM Q12: computed=36 expected=36 match=yes
CLAIM Q13: computed=108 expected=108 match=yes
CLAIM Q14: computed=324 expected=324 match=yes
CLAIM Q15: computed=485 expected=485 match=yes
CLAIM Q16: computed=1 expected=1 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 6 | 6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 12 | 12 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 24 | 24 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 48 | 48 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 94 | 94 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 12 | 12 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 36 | 36 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 108 | 108 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 324 | 324 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 485 | 485 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
