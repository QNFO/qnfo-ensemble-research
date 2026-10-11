# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Expected positional deletion error for four-digit numbers in [1000,3999] with uniform deletion position is 2187.5",
    "inputs": "E[d3]=4.5 (uniform digit mean); E[d2]=E[d1]=4.5; leading-digit deletion error E[d3]*10^3 = 2000; other positions each 2250",
    "formula": "(2000 + 2250 + 2250 + 2250)/4 = 2187.5"
  },
  {
    "id": "Q2",
    "statement": "Expected additive deletion error is approximately 449.4",
    "inputs": "total symbol value = sum_{N=1}^{3999} N = 7998000; total symbol count = 4.45 * 3999 = 17795.55",
    "formula": "7998000 / 17795.55 ≈ 449.4"
  },
  {
    "id": "Q3",
    "statement": "Average greedy-additive symbol count over N in [1,3999] is 4.45",
    "inputs": "expected count for N in [1,999] = 0.5+0.9+0.5+0.9+0.5+0.4 = 3.7; each thousands block adds 1",
    "formula": "(3.7 + 3*4.7)/4 = 17.8/4 = 4.45"
  },
  {
    "id": "Q4",
    "statement": "Compactness ratio of additive to positional is about 1.11",
    "inputs": "L_add = 4.45; L_pos = 4",
    "formula": "4.45/4 ≈ 1.11"
  },
  {
    "id": "Q5",
    "statement": "Cost-model crossover lambda/mu is approximately 0.26",
    "inputs": "L_add - L_pos = 0.45; E_pos - E_add = 2187.5 - 449.4 = 1738.1",
    "formula": "(0.45 * 1000)/1738.1 ≈ 0.26"
  },
  {
    "id": "Q6",
    "statement": "Worked example: deleting hundreds digit of 5284 gives error 4700",
    "inputs": "H=5, d_k=2, k=2",
    "formula": "(9*5 + 2)*10^2 = 47*100 = 4700"
  },
  {
    "id": "Q7",
    "statement": "Worst-case deletion error ratio positional/additive over [1,3999] is 3",
    "inputs": "positional worst = 3999 - 999 = 3000; additive worst = 1000",
    "formula": "3000/1000 = 3"
  },
  {
    "id": "Q8",
    "statement": "Expected positional transposition error per adjacent pair at position k is 3.3*10^k",
    "inputs": "digits uniform on {0,...,9}; E|d_{k+1}-d_k| = 3.3",
    "formula": "10^k * 3.3 = 3.3*10^k"
  }
]

## Script
```python
```python
import math
from fractions import Fraction

# Independent verification of the quantitative claims in
# "Numeral Systems as Evolving Cognitive Technologies".
# Convention: each claim is recomputed from its stated inputs/formula.
# Where the claim's derivation rests on distributional expectations
# (uniform digits / uniform N), those expectations are recomputed exactly
# by enumeration rather than accepted as asserted.  For comparison with a
# rounded claimed value, the computed value is rounded to the same number
# of decimals before applying math.isclose(rel_tol=1e-6).

def greedy_count(n):
    """Symbol count of the greedy additive system with values
    V = {1000, 500, 100, 50, 10, 5, 1}, no subtractive rules."""
    c = 0
    for v in (1000, 500, 100, 50, 10, 5, 1):
        c += n // v
        n %= v
    return c

def report(cid, computed, expected, decimals):
    c = round(computed, decimals)
    match = math.isclose(c, expected, rel_tol=1e-6)
    print(f"CLAIM {cid}: computed={computed} expected={expected} "
          f"match={'yes' if match else 'no'}")
    return match

matches = []

# --- Q1: expected positional deletion error, N in [1000,3999],
#         deletion position uniform among the 4 digits.
total_err = 0
events = 0
for N in range(1000, 4000):
    d3, rem = divmod(N, 1000)
    d2, rem = divmod(rem, 100)
    d1, d0 = divmod(rem, 10)
    # read values after deleting each digit (blocks merge)
    reads = [d2 * 100 + d1 * 10 + d0,   # delete d3
             d3 * 100 + d1 * 10 + d0,   # delete d2
             d3 * 100 + d2 * 10 + d0,   # delete d1
             d3 * 100 + d2 * 10 + d1]   # delete d0
    for Np in reads:
        total_err += abs(N - Np)
        events += 1
E_pos = total_err / events
matches.append(report("Q1", E_pos, 2187.5, 1))

# --- Q2: expected additive deletion error.
# Total symbol value: sum_{N=1}^{3999} N = 3999*4000/2
total_value = 3999 * 4000 // 2
assert total_value == 7998000
# Total symbol count: recomputed exactly by greedy enumeration
total_count = sum(greedy_count(N) for N in range(1, 4000))
E_add = total_value / total_count
matches.append(report("Q2", E_add, 449.4, 1))

# --- Q3: average greedy-additive symbol count over N in [1,3999].
# The paper's decomposition asserts per-term expectations
# (0.5 + 0.9 + 0.5 + 0.9 + 0.5 + 0.4 = 3.7 for N in [1,999]);
# each term is recomputed exactly here by enumeration.
terms = {
    "floor(N/500)":          sum(N // 500 for N in range(1, 1000)),
    "floor((N%500)/100)":    sum((N % 500) // 100 for N in range(1, 1000)),
    "floor((N%100)/50)":     sum((N % 100) // 50 for N in range(1, 1000)),
    "floor((N%50)/10)":      sum((N % 50) // 10 for N in range(1, 1000)),
    "floor((N%10
```

## Execution output
```

[stderr]
  File "<string>", line 69
    "floor((N%10
    ^
SyntaxError: unterminated string literal (detected at line 69)

[exit 1]
```
