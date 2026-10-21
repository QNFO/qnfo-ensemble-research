# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The propositional assignment space for n=3 islanders is 2^3 = 8.",
    "inputs": "n = 3",
    "formula": "2^n"
  },
  {
    "id": "Q2",
    "statement": "Exactly one assignment satisfies all three consistency constraints in the liars‑and‑truth‑tellers puzzle.",
    "inputs": "total assignments = 8, survivors = 1",
    "formula": "survivors = 1"
  },
  {
    "id": "Q3",
    "statement": "The elimination rate for the puzzle is 7/8 = 0.875.",
    "inputs": "total assignments = 8, survivors = 1",
    "formula": "(total assignments - survivors) / total assignments"
  },
  {
    "id": "Q4",
    "statement": "For n=10 islanders the raw propositional space contains 2^10 = 1 024 assignments.",
    "inputs": "n = 10",
    "formula": "2^n"
  },
  {
    "id": "Q5",
    "statement": "The number of arbitrary binary accessibility relations on |W| = 8 worlds is 2^{8·8} = 2^{64} = 18 446 744 073 709 551 616 ≈ 1.84×10^{19}.",
    "inputs": " |W| = 8 ",
    "formula": "2^{|W|·|W|}"
  },
  {
    "id": "Q6",
    "statement": "The number of reflexive relations on |W| = 8 worlds is 2^{56} = 72 057 594 037 927 936 ≈ 7.21×10^{16}.",
    "inputs": " |W| = 8 ",
    "formula": "2^{|W|·|W| - |W|}"
  },
  {
    "id": "Q7",
    "statement": "The initial Wise Men model contains 2^3 = 8 possible worlds.",
    "inputs": "number of agents = 3",
    "formula": "2^{number of agents}"
  },
  {
    "id": "Q8",
    "statement": "After the king’s public announcement the model size is reduced to 7 worlds.",
    "inputs": "initial worlds = 8, eliminated worlds = 1",
    "formula": "initial worlds - eliminated worlds"
  },
  {
    "id": "Q9",
    "statement": "After agent a’s “I don’t know” announcement the model size becomes 6 worlds.",
    "inputs": "previous worlds = 7, eliminated worlds = 1",
    "formula": "previous worlds - eliminated worlds"
  },
  {
    "id": "Q10",
    "statement": "After agent b’s analogous announcement the model size becomes 4 worlds.",
    "inputs": "previous worlds = 6, eliminated worlds = 2",
    "formula": "previous worlds - eliminated worlds"
  },
  {
    "id": "Q11",
    "statement": "The overall shrinkage factor from the first announcement onward is 7/4 = 1.75.",
    "inputs": "worlds after first announcement = 7, worlds after last announcement = 4",
    "formula": "7 / 4"
  },
  {
    "id": "Q12",
    "statement": "A DEL action model with |E| = 3 events applied to the original 8 worlds yields a product model of size 8·3 = 24 worlds.",
    "inputs": " |W| = 8 , |E| = 3 ",
    "formula": "|W|·|E|"
  },
  {
    "id": "Q13",
    "statement": "Boolos’s proof‑length recurrence gives L₁ = 2^{L₀} = 2.",
    "inputs": "L₀ = 1",
    "formula": "L₁ = 2^{L₀}"
  },
  {
    "id": "Q14",
    "statement": "L₂ = 2^{L₁} = 4.",
    "inputs": "L₁ = 2",
    "formula": "L₂ = 2^{L₁}"
  },
  {
    "id": "Q15",
    "statement": "L₃ = 2^{L₂} = 16.",
    "inputs": "L₂ = 4",
    "formula": "L₃ = 2^{L₂}"
  },
  {
    "id": "Q16",
    "statement": "L₄ = 2^{L₃} = 65 536.",
    "inputs": "L₃ = 16",
    "formula": "L₄ = 2^{L₃}"
  }
]

## Script
```python
# Verification script for quantitative claims Q1–Q16

def fmt(val):
    """Format numbers with at least 8 significant digits."""
    if isinstance(val, float):
        # Use 8 significant digits, remove trailing zeros
        s = f"{val:.8g}"
    else:
        s = str(val)
    return s

# Q1: 2^n with n=3
n1 = 3
c1 = 2 ** n1
e1 = "8"
print(f"CLAIM Q1: computed={fmt(c1)} expected={e1} match={'yes' if fmt(c1)==e1 else 'no'}")

# Q2: survivors = 1 (given)
c2 = 1
e2 = "1"
print(f"CLAIM Q2: computed={fmt(c2)} expected={e2} match={'yes' if fmt(c2)==e2 else 'no'}")

# Q3: elimination rate = (total - survivors)/total = (8-1)/8 = 7/8
total3 = 8
survivors3 = 1
c3 = (total3 - survivors3) / total3
e3 = "0.875"
print(f"CLAIM Q3: computed={fmt(c3)} expected={e3} match={'yes' if fmt(c3)==e3 else 'no'}")

# Q4: 2^n with n=10
n4 = 10
c4 = 2 ** n4
e4 = "1024"
print(f"CLAIM Q4: computed={fmt(c4)} expected={e4} match={'yes' if fmt(c4)==e4 else 'no'}")

# Q5: 2^{|W|*|W|} with |W|=8 => 2^{64}
W5 = 8
c5 = 2 ** (W5 * W5)
e5 = "18446744073709551616"
print(f"CLAIM Q5: computed={fmt(c5)} expected={e5} match={'yes' if fmt(c5)==e5 else 'no'}")

# Q6: 2^{|W|*|W| - |W|} = 2^{56}
c6 = 2 ** (W5 * W5 - W5)
e6 = "72057594037927936"
print(f"CLAIM Q6: computed={fmt(c6)} expected={e6} match={'yes' if fmt(c6)==e6 else 'no'}")

# Q7: initial Wise Men worlds = 2^3
agents7 = 3
c7 = 2 ** agents7
e7 = "8"
print(f"CLAIM Q7: computed={fmt(c7)} expected={e7} match={'yes' if fmt(c7)==e7 else 'no'}")

# Q8: after king announcement = initial - 1
c8 = 8 - 1
e8 = "7"
print(f"CLAIM Q8: computed={fmt(c8)} expected={e8} match={'yes' if fmt(c8)==e8 else 'no'}")

# Q9: after agent a announcement = previous - 1
c9 = 7 - 1
e9 = "6"
print(f"CLAIM Q9: computed={fmt(c9)} expected={e9} match={'yes' if fmt(c9)==e9 else 'no'}")

# Q10: after agent b announcement = previous - 2
c10 = 6 - 2
e10 = "4"
print(f"CLAIM Q10: computed={fmt(c10)} expected={e10} match={'yes' if fmt(c10)==e10 else 'no'}")

# Q11: shrinkage factor = 7 / 4
c11 = 7 / 4
e11 = "1.75"
print(f"CLAIM Q11: computed={fmt(c11)} expected={e11} match={'yes' if fmt(c11)==e11 else 'no'}")

# Q12: product model size = |W| * |E| = 8 * 3
W12 = 8
E12 = 3
c12 = W12 * E12
e12 = "24"
print(f"CLAIM Q12: computed={fmt(c12)} expected={e12} match={'yes' if fmt(c12)==e12 else 'no'}")

# Q13: L1 = 2^{L0} with L0=1
L0 = 1
c13 = 2 ** L0
e13 = "2"
print(f"CLAIM Q13: computed={fmt(c13)} expected={e13} match={'yes' if fmt(c13)==e13 else 'no'}")

# Q14: L2 = 2^{L1}
L1 = c13
c14 = 2 ** L1
e14 = "4"
print(f"CLAIM Q14: computed={fmt(c14)} expected={e14} match={'yes' if fmt(c14)==e14 else 'no'}")

# Q15: L3 = 2^{L2}
L2 = c14
c15 = 2 ** L2
e15 = "16"
print(f"CLAIM Q15: computed={fmt(c15)} expected={e15} match={'yes' if fmt(c15)==e15 else 'no'}")

# Q16: L4 = 2^{L3}
L3 = c15
c16 = 2 ** L3
e16 = "65536"
print(f"CLAIM Q16: computed={fmt(c16)} expected={e16} match={'yes' if fmt(c16)==e16 else 'no'}")

# Summary
total = 16
matches = sum(1 for line in [
    fmt(c1)==e1, fmt(c2)==e2, fmt(c3)==e3, fmt(c4)==e4,
    fmt(c5)==e5, fmt(c6)==e6, fmt(c7)==e7, fmt(c8)==e8,
    fmt(c9)==e9, fmt(c10)==e10, fmt(c11)==e11, fmt(c12)==e12,
    fmt(c13)==e13, fmt(c14)==e14, fmt(c15)==e15, fmt(c16)==e16
] if line)
mismatches = total - matches
print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {mismatches} mismatch")

```

## Execution output
```
CLAIM Q1: computed=8 expected=8 match=yes
CLAIM Q2: computed=1 expected=1 match=yes
CLAIM Q3: computed=0.875 expected=0.875 match=yes
CLAIM Q4: computed=1024 expected=1024 match=yes
CLAIM Q5: computed=18446744073709551616 expected=18446744073709551616 match=yes
CLAIM Q6: computed=72057594037927936 expected=72057594037927936 match=yes
CLAIM Q7: computed=8 expected=8 match=yes
CLAIM Q8: computed=7 expected=7 match=yes
CLAIM Q9: computed=6 expected=6 match=yes
CLAIM Q10: computed=4 expected=4 match=yes
CLAIM Q11: computed=1.75 expected=1.75 match=yes
CLAIM Q12: computed=24 expected=24 match=yes
CLAIM Q13: computed=2 expected=2 match=yes
CLAIM Q14: computed=4 expected=4 match=yes
CLAIM Q15: computed=16 expected=16 match=yes
CLAIM Q16: computed=65536 expected=65536 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 1 | 1 | yes | match | 3 significant digits (as printed, at least 3) |
| Q3 | 0.875 | 0.875 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 1024 | 1024 | yes | match | 4 significant digits (as printed, at least 3) |
| Q5 | 18446744073709551616 | 18446744073709551616 | yes | match | 20 significant digits (as printed, at least 3) |
| Q6 | 72057594037927936 | 72057594037927936 | yes | match | 17 significant digits (as printed, at least 3) |
| Q7 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 7 | 7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 6 | 6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 1.75 | 1.75 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 24 | 24 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 2 | 2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 16 | 16 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q16 | 65536 | 65536 | yes | match | 5 significant digits (as printed, at least 3) |

Mismatches: 0 of 16.
