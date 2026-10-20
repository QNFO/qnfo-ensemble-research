# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The propositional state space for 3 islanders is $2^{3}=8$ assignments.",
    "inputs": "n = 3",
    "formula": "2^n"
  },
  {
    "id": "Q2",
    "statement": "The elimination rate for the 3‑islander puzzle is $7/8 = 0.875$.",
    "inputs": "total assignments = 8, surviving assignments = 1",
    "formula": "(total assignments - surviving assignments) / total assignments"
  },
  {
    "id": "Q3",
    "statement": "For 10 islanders the raw propositional space is $2^{10}=1{,}024$.",
    "inputs": "n = 10",
    "formula": "2^n"
  },
  {
    "id": "Q4",
    "statement": "The number of arbitrary binary accessibility relations on $|W|=8$ worlds is $2^{8\\times8}=2^{64}=18{,}446{,}744{,}073{,}709{,}551{,}616$.",
    "inputs": "W = 8",
    "formula": "2^(W*W)"
  },
  {
    "id": "Q5",
    "statement": "The number of reflexive accessibility relations on $|W|=8$ worlds is $2^{56}=72{,}057{,}594{,}037{,}927{,}936$.",
    "inputs": "W = 8",
    "formula": "2^(W*(W-1))"
  },
  {
    "id": "Q6",
    "statement": "The initial world set for the Wise Men puzzle has size $2^{3}=8$.",
    "inputs": "agents = 3",
    "formula": "2^agents"
  },
  {
    "id": "Q7",
    "statement": "After the king’s public announcement the world set size is $8-1=7$.",
    "inputs": "initial worlds = 8, eliminated worlds = 1",
    "formula": "initial worlds - eliminated worlds"
  },
  {
    "id": "Q8",
    "statement": "After agent a’s “I don’t know” announcement the world set size is $7-1=6$.",
    "inputs": "previous worlds = 7, eliminated worlds = 1",
    "formula": "previous worlds - eliminated worlds"
  },
  {
    "id": "Q9",
    "statement": "After agent b’s announcement the world set size is $6-2=4$.",
    "inputs": "previous worlds = 6, eliminated worlds = 2",
    "formula": "previous worlds - eliminated worlds"
  },
  {
    "id": "Q10",
    "statement": "The shrinkage factor from the first to the final Wise Men model is $7/4 = 1.75$.",
    "inputs": "size after king = 7, final size = 4",
    "formula": "size after king / final size"
  },
  {
    "id": "Q11",
    "statement": "A DEL action model with $|E|=3$ events over the original $8$ worlds yields $8\\times3=24$ worlds.",
    "inputs": "W = 8, E = 3",
    "formula": "W * E"
  },
  {
    "id": "Q12",
    "statement": "The fifth term of Boolos’s proof‑length tower is $L_{5}=2^{65{,}536}\\approx10^{19{,}728}$.",
    "inputs": "L5 exponent = 65,536, log10(2) = 0.30103",
    "formula": "10^(65,536 * log10(2))"
  },
  {
    "id": "Q13",
    "statement": "The first‑order interpretation space with domain size $d=10$ and one binary predicate is $2^{d^{2}}=2^{100}=1{,}267{,}650{,}600{,}228{,}229{,}401{,}496{,}703{,}205{,}376$.",
    "inputs": "d = 10",
    "formula": "2^(d^2)"
  },
  {
    "id": "Q14",
    "statement": "A propositional instantiation with $k=10$ atoms yields $2^{10}=1{,}024$ rows.",
    "inputs": "k = 10",
    "formula": "2^k"
  },
  {
    "id": "Q15",
    "statement": "With $m=2$ obligations the deontic fulfillment profile count is $2^{2}=4$.",
    "inputs": "m = 2",
    "formula": "2^m"
  },
  {
    "id": "Q16",
    "statement": "With $m=3$ obligations the deontic fulfillment profile count is $2^{3}=8$.",
    "inputs": "m = 3",
    "formula": "2^m"
  }
]

## Script
```python
import math
from decimal import Decimal, getcontext

# set precision sufficient for the huge exponentiation in Q12
getcontext().prec = 12  # enough for mantissa, exponent will be huge

def claim_line(cid, computed, expected, match):
    return f"CLAIM {cid}: computed={computed} expected={expected} match={match}"

def approx_equal(a, b, rel_tol=1e-12, abs_tol=0.0):
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)

# Q1
c1 = 2 ** 3
e1 = "8"
m1 = "yes" if c1 == 8 else "no"
print(claim_line("Q1", c1, e1, m1))

# Q2
c2 = (8 - 1) / 8
e2 = "0.875"
m2 = "yes" if abs(c2 - 0.875) < 1e-12 else "no"
print(claim_line("Q2", c2, e2, m2))

# Q3
c3 = 2 ** 10
e3 = "1024"
m3 = "yes" if c3 == 1024 else "no"
print(claim_line("Q3", c3, e3, m3))

# Q4
c4 = 2 ** (8 * 8)
e4 = "18446744073709551616"
m4 = "yes" if c4 == 18446744073709551616 else "no"
print(claim_line("Q4", c4, e4, m4))

# Q5
c5 = 2 ** (8 * (8 - 1))
e5 = "72057594037927936"
m5 = "yes" if c5 == 72057594037927936 else "no"
print(claim_line("Q5", c5, e5, m5))

# Q6
c6 = 2 ** 3
e6 = "8"
m6 = "yes" if c6 == 8 else "no"
print(claim_line("Q6", c6, e6, m6))

# Q7
c7 = 8 - 1
e7 = "7"
m7 = "yes" if c7 == 7 else "no"
print(claim_line("Q7", c7, e7, m7))

# Q8
c8 = 7 - 1
e8 = "6"
m8 = "yes" if c8 == 6 else "no"
print(claim_line("Q8", c8, e8, m8))

# Q9
c9 = 6 - 2
e9 = "4"
m9 = "yes" if c9 == 4 else "no"
print(claim_line("Q9", c9, e9, m9))

# Q10
c10 = 7 / 4
e10 = "1.75"
m10 = "yes" if abs(c10 - 1.75) < 1e-12 else "no"
print(claim_line("Q10", c10, e10, m10))

# Q11
c11 = 8 * 3
e11 = "24"
m11 = "yes" if c11 == 24 else "no"
print(claim_line("Q11", c11, e11, m11))

# Q12
# Compute 10^(65536 * log10(2)) ≈ 10^19728.3, expected as 10^{19728}
exponent = Decimal(65536) * Decimal('0.30103')
c12 = (Decimal(10) ** exponent)
e12 = "10^{19728}"
# Since c12 is a huge number, we compare only the exponent part
# Extract exponent from Decimal's scientific notation
c12_str = format(c12, 'E')
# Example format: '1.000000E+19728'
c12_exp = int(c12_str.split('E')[1])
m12 = "yes" if c12_exp == 19728 else "no"
print(claim_line("Q12", c12_str, e12, m12))

# Q13
c13 = 2 ** (10 ** 2)  # 2^(10^2) = 2^100
e13 = "1267650600228229401496703205376"
m13 = "yes" if c13 == 1267650600228229401496703205376 else "no"
print(claim_line("Q13", c13, e13, m13))

# Q14
c14 = 2 ** 10
e14 = "1024"
m14 = "yes" if c14 == 1024 else "no"
print(claim_line("Q14", c14, e14, m14))

# Q15
c15 = 2 ** 2
e15 = "4"
m15 = "yes" if c15 == 4 else "no"
print(claim_line("Q15", c15, e15, m15))

# Q16
c16 = 2 ** 3
e16 = "8"
m16 = "yes" if c16 == 8 else "no"
print(claim_line("Q16", c16, e16, m16))

print(f"VERIFICATION SUMMARY: 16 claims, {sum([m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16].count('yes'))} match, {sum([m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16].count('no'))} mismatch")

```

## Execution output
```
CLAIM Q1: computed=8 expected=8 match=yes
CLAIM Q2: computed=0.875 expected=0.875 match=yes
CLAIM Q3: computed=1024 expected=1024 match=yes
CLAIM Q4: computed=18446744073709551616 expected=18446744073709551616 match=yes
CLAIM Q5: computed=72057594037927936 expected=72057594037927936 match=yes
CLAIM Q6: computed=8 expected=8 match=yes
CLAIM Q7: computed=7 expected=7 match=yes
CLAIM Q8: computed=6 expected=6 match=yes
CLAIM Q9: computed=4 expected=4 match=yes
CLAIM Q10: computed=1.75 expected=1.75 match=yes
CLAIM Q11: computed=24 expected=24 match=yes
CLAIM Q12: computed=2.00484129877E+19728 expected=10^{19728} match=yes
CLAIM Q13: computed=1267650600228229401496703205376 expected=1267650600228229401496703205376 match=yes
CLAIM Q14: computed=1024 expected=1024 match=yes
CLAIM Q15: computed=4 expected=4 match=yes
CLAIM Q16: computed=8 expected=8 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 116, in <module>
TypeError: 'int' object is not iterable

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.875 | 0.875 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 1024 | 1024 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 18446744073709551616 | 18446744073709551616 | yes | match | 20 significant digits (as the paper states, at least 2) |
| Q5 | 72057594037927936 | 72057594037927936 | yes | match | 17 significant digits (as the paper states, at least 2) |
| Q6 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 7 | 7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 6 | 6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 1.75 | 1.75 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 24 | 24 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 2.00484129877E+19728 | 10^{19728} | yes | match | script verdict (values not both numeric) |
| Q13 | 1267650600228229401496703205376 | 1267650600228229401496703205376 | yes | match | 31 significant digits (as the paper states, at least 2) |
| Q14 | 1024 | 1024 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q15 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q16 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
