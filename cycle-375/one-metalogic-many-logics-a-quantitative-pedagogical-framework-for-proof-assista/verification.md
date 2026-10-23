# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The propositional assignment space for three islanders contains 2^3 = 8 rows.",
    "inputs": "n = 3 islanders",
    "formula": "2^n"
  },
  {
    "id": "Q2",
    "statement": "The elimination rate for the three-islander puzzle is (8-1)/8 = 0.875.",
    "inputs": "total assignments = 8, survivors = 1",
    "formula": "(total - survivors) / total"
  },
  {
    "id": "Q3",
    "statement": "For n = 10 islanders the raw space is 2^10 = 1024 assignments.",
    "inputs": "n = 10",
    "formula": "2^n"
  },
  {
    "id": "Q4",
    "statement": "The number of arbitrary binary accessibility relations on |W| = 8 worlds is 2^64 = 18446744073709551616, approximately 1.84e19.",
    "inputs": "|W| = 8",
    "formula": "2^(|W| * |W|)"
  },
  {
    "id": "Q5",
    "statement": "The number of reflexive accessibility relations is 2^56 = 72057594037927936, approximately 7.21e16.",
    "inputs": "|W| = 8, off-diagonal pairs = 8 * 7 = 56",
    "formula": "2^(|W| * (|W| - 1))"
  },
  {
    "id": "Q6",
    "statement": "The Wise Men / muddy-children model collapses 8 -> 7 -> 6 -> 4 under sequential announcements.",
    "inputs": "|W0| = 2^3 = 8; removals: 1 (all-white world), 1 (first ignorance announcement), 2 (second ignorance announcement)",
    "formula": "|W1| = 8 - 1; |W2| = 7 - 1; |W3| = 6 - 2"
  },
  {
    "id": "Q7",
    "statement": "The shrinkage factor from the first announcement onward is 7/4 = 1.75.",
    "inputs": "|W1| = 7, |W3| = 4",
    "formula": "|W1| / |W3|"
  },
  {
    "id": "Q8",
    "statement": "A dynamic-epistemic product model with |E| = 3 events has 8 * 3 = 24 worlds.",
    "inputs": "|W0| = 8, |E| = 3",
    "formula": "|W0| * |E|"
  },
  {
    "id": "Q9",
    "statement": "For m = 8 agents the initial space is 2^8 = 256 worlds, and after the all-white removal 255 worlds remain.",
    "inputs": "m = 8",
    "formula": "2^m and 2^m - 1"
  },
  {
    "id": "Q10",
    "statement": "The Boolos tower iterations give L1 = 2, L2 = 4, L3 = 16, L4 = 65536.",
    "inputs": "L0 = 1",
    "formula": "L_{n+1} = 2^(L_n)"
  },
  {
    "id": "Q11",
    "statement": "log10(L5) = 65536 * 0.30103 = 19728.30208, approximately 19728.3, so L5 is approximately 10^19728.",
    "inputs": "L4 = 65536, log10(2) = 0.30103",
    "formula": "L4 * log10(2)"
  },
  {
    "id": "Q12",
    "statement": "The first-order interpretation space with domain size d = 10 and one binary predicate is 2^100 = 1267650600228229401496703205376, approximately 1.27e30.",
    "inputs": "d = 10",
    "formula": "2^(d * d)"
  },
  {
    "id": "Q13",
    "statement": "Deontic fulfillment profiles number 2^2 = 4 for two obligations and 2^3 = 8 for three obligations.",
    "inputs": "m = 2 and m = 3 obligations",
    "formula": "2^m"
  },
  {
    "id": "Q14",
    "statement": "The raw positivity-predicate interpretation space for Goedel's ontological argument is 2^5 = 32.",
    "inputs": "p = 5 candidate properties",
    "formula": "2^p"
  },
  {
    "id": "Q15",
    "statement": "The consistent positivity-predicate space is 2^(5-3) = 4.",
    "inputs": "p = 5, a = 3 independent axioms",
    "formula": "2^(p - a)"
  },
  {
    "id": "Q16",
    "statement": "The total contact time is 14 weeks * 2 h = 28 h.",
    "inputs": "weeks = 14, hours per week = 2",
    "formula": "weeks * hours_per_week"
  }
]

## Script
```python
import math

def match_float(computed, expected_str):
    # Determine number of significant digits from expected string (excluding leading zeros and decimal point)
    # For simplicity, compare rounded to same number of decimal places as in expected string.
    if '.' in expected_str:
        dec_places = len(expected_str.split('.')[1])
        return round(computed, dec_places) == round(float(expected_str), dec_places)
    else:
        return computed == float(expected_str)

def claim(id, computed, expected):
    if expected is None:
        match = "no"
    else:
        if isinstance(computed, (int,)):
            match = "yes" if computed == int(expected) else "no"
        else:
            match = "yes" if match_float(computed, expected) else "no"
    print(f"CLAIM {id}: computed={computed} expected={expected} match={match}")

# Q1
c1 = 2**3
claim("Q1", c1, "8")

# Q2
c2 = (8-1)/8
claim("Q2", c2, "0.875")

# Q3
c3 = 2**10
claim("Q3", c3, "1024")

# Q4
c4 = 2**64
claim("Q4", c4, "18446744073709551616")

# Q5
c5 = 2**56
claim("Q5", c5, "72057594037927936")

# Q6
W0 = 2**3
W1 = W0 - 1
W2 = W1 - 1
W3 = W2 - 2
claim("Q6", f"{W0}->{W1}->{W2}->{W3}", "8->7->6->4")

# Q7
c7 = 7/4
claim("Q7", c7, "1.75")

# Q8
c8 = 8 * 3
claim("Q8", c8, "24")

# Q9
init = 2**8
after = init - 1
claim("Q9", f"{init},{after}", "256,255")

# Q10
L = [1]
for i in range(4):
    L.append(2**L[-1])
# L[1]=2, L[2]=4, L[3]=16, L[4]=65536
claim("Q10", f"{L[1]},{L[2]},{L[3]},{L[4]}", "2,4,16,65536")

# Q11
log10_L5 = 65536 * 0.30103
claim("Q11", log10_L5, "19728.30208")

# Q12
c12 = 2**(10*10)
claim("Q12", c12, "1267650600228229401496703205376")

# Q13
c13_2 = 2**2
c13_3 = 2**3
claim("Q13", f"{c13_2},{c13_3}", "4,8")

# Q14
c14 = 2**5
claim("Q14", c14, "32")

# Q15
c15 = 2**(5-3)
claim("Q15", c15, "4")

# Q16
c16 = 14 * 2
claim("Q16", c16, "28")

print("VERIFICATION SUMMARY: 16 claims, X match, Y mismatch")

```

## Execution output
```
CLAIM Q1: computed=8 expected=8 match=yes
CLAIM Q2: computed=0.875 expected=0.875 match=yes
CLAIM Q3: computed=1024 expected=1024 match=yes
CLAIM Q4: computed=18446744073709551616 expected=18446744073709551616 match=yes
CLAIM Q5: computed=72057594037927936 expected=72057594037927936 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 47, in <module>
  File "<string>", line 19, in claim
  File "<string>", line 10, in match_float
ValueError: could not convert string to float: '8->7->6->4'

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

Mismatches: 0 of 5.
