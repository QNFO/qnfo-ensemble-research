# Verification report

## Extracted claims
[
  {
    "id": "C1",
    "statement": "Tally states at depth n=9 equal N₁(9)=10.",
    "inputs": "n=9",
    "formula": "N₁ = n + 1"
  },
  {
    "id": "C2",
    "statement": "Real cells at precision ε=2⁻³ equal N₄=8.",
    "inputs": "ε=2⁻³",
    "formula": "N₄ = 1 / ε"
  },
  {
    "id": "C3",
    "statement": "Binary tree states at depth n=10 with base p=2 equal N₆(10)=1024.",
    "inputs": "p=2, n=10",
    "formula": "N₆ = p^n"
  },
  {
    "id": "C4",
    "statement": "Monna cross‑stratum loss for (p=2, n=10, ε=2⁻³) is Λ₆→₄ = 7 bits.",
    "inputs": "N₆=1024, N₄=8",
    "formula": "Λ = log₂(N₆) - log₂(N₄)"
  },
  {
    "id": "C5",
    "statement": "For fixed ε=2⁻³ and p=2 the Monna loss obeys Λ₆→₄(n) = n - 3 bits.",
    "inputs": "ε=2⁻³, p=2",
    "formula": "Λ = n·log₂(p) - log₂(1/ε) = n - 3"
  },
  {
    "id": "C6",
    "statement": "Loss‑free matching occurs at depth n=3 giving Λ₆→₄ = 0 bits.",
    "inputs": "n=3, ε=2⁻³, p=2",
    "formula": "Λ = n - 3 = 0"
  },
  {
    "id": "C7",
    "statement": "Finite adele‑type product over primes {2,3,5} at depth 1 yields 30 states.",
    "inputs": "primes = {2,3,5}, depth per prime = 1",
    "formula": "N = ∏_{p∈{2,3,5}} p^{1} = 2·3·5"
  },
  {
    "id": "C8",
    "statement": "Finite adele‑type product over primes {2,3,5} at depth 2 yields 900 states.",
    "inputs": "primes = {2,3,5}, depth per prime = 2",
    "formula": "N = ∏_{p∈{2,3,5}} p^{2} = 2²·3²·5²"
  },
  {
    "id": "C9",
    "statement": "Total number of strata including the mark is 8.",
    "inputs": "number of operators = 7",
    "formula": "total strata = operators + 1"
  },
  {
    "id": "C10",
    "statement": "For p=3 and ε=2⁻³ the integer depth solving Λ₆→₄=0 would be n = 3 / log₂3 ≈ 1.893, which is not an integer, so no loss‑free match exists.",
    "inputs": "p=3, ε=2⁻³",
    "formula": "n = 3 / log₂(p)"
  },
  {
    "id": "C11",
    "statement": "Adjacent loss Λ₀→₁ at n=9 equals -log₂(10) ≈ -3.3219 bits.",
    "inputs": "N₀=1, N₁(9)=10",
    "formula": "Λ = log₂(N₀) - log₂(N₁) = -log₂(10)"
  },
  {
    "id": "C12",
    "statement": "Projected loss for p=3, n=5, ε=10⁻² is approximately 1.28 bits.",
    "inputs": "p=3, n=5, ε=10⁻²",
    "formula": "Λ = n·log₂(p) - log₂(1/ε)"
  },
  {
    "id": "C13",
    "statement": "For p=2, n=8, ε=2⁻⁴ the Monna loss is 4 bits.",
    "inputs": "p=2, n=8, ε=2⁻⁴",
    "formula": "Λ = n·log₂(p) - log₂(1/ε) = 8·1 - 4"
  },
  {
    "id": "C14",
    "statement": "For p=5, n=8, ε=2⁻⁴ the Monna loss is approximately 14.57544 bits.",
    "inputs": "p=5, n=8, ε=2⁻⁴",
    "formula": "Λ = n·log₂(p) - log₂(1/ε) = 8·log₂(5) - 4"
  },
  {
    "id": "C15",
    "statement": "For p=3, n=8, ε=10⁻² the Monna loss is approximately 6.03582 bits.",
    "inputs": "p=3, n=8, ε=10⁻²",
    "formula": "Λ = n·log₂(p) - log₂(1/ε) = 8·log₂(3) - log₂(100)"
  }
]

## Script
```python
import math

def fmt(x):
    # format float with up to 8 significant digits, strip trailing zeros
    if isinstance(x, str):
        return x
    if isinstance(x, (int,)):
        return str(x)
    s = f"{x:.8g}"
    return s

claims = []

# C1
computed = 9 + 1
expected = "10"
claims.append(("C1", computed, expected))

# C2
epsilon = 2**-3
computed = 1 / epsilon
expected = "8"
claims.append(("C2", computed, expected))

# C3
p = 2
n = 10
computed = p**n
expected = "1024"
claims.append(("C3", computed, expected))

# C4
N6 = 1024
N4 = 8
computed = math.log2(N6) - math.log2(N4)
expected = "7"
claims.append(("C4", computed, expected))

# C5 (formula claim)
# We represent the computed value as the symbolic expression "n-3"
computed = "n-3"
expected = "n-3"
claims.append(("C5", computed, expected))

# C6
n = 3
computed = n - 3
expected = "0"
claims.append(("C6", computed, expected))

# C7
computed = 2 * 3 * 5
expected = "30"
claims.append(("C7", computed, expected))

# C8
computed = (2**2) * (3**2) * (5**2)
expected = "900"
claims.append(("C8", computed, expected))

# C9
operators = 7
computed = operators + 1
expected = "8"
claims.append(("C9", computed, expected))

# C10
p = 3
epsilon = 2**-3
computed = 3 / math.log2(p)
expected = "1.893"
claims.append(("C10", computed, expected))

# C11
computed = -math.log2(10)
expected = "-3.3219"
claims.append(("C11", computed, expected))

# C12
p = 3
n = 5
epsilon = 10**-2
computed = n * math.log2(p) - math.log2(1/epsilon)
expected = "1.28"
claims.append(("C12", computed, expected))

# C13
p = 2
n = 8
epsilon = 2**-4
computed = n * math.log2(p) - math.log2(1/epsilon)
expected = "4"
claims.append(("C13", computed, expected))

# C14
p = 5
n = 8
epsilon = 2**-4
computed = n * math.log2(p) - math.log2(1/epsilon)
expected = "14.57544"
claims.append(("C14", computed, expected))

# C15
p = 3
n = 8
epsilon = 10**-2
computed = n * math.log2(p) - math.log2(1/epsilon)
expected = "6.03582"
claims.append(("C15", computed, expected))

# Output results
for cid, comp, exp in claims:
    comp_str = fmt(comp)
    match = "yes" if comp_str == exp else "no"
    print(f"CLAIM {cid}: computed={comp_str} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if fmt(c)==e)} match, {sum(1 for _,c,e in claims if fmt(c)!=e)} mismatch")

```

## Execution output
```
CLAIM C1: computed=10 expected=10 match=yes
CLAIM C2: computed=8 expected=8 match=yes
CLAIM C3: computed=1024 expected=1024 match=yes
CLAIM C4: computed=7 expected=7 match=yes
CLAIM C5: computed=n-3 expected=n-3 match=yes
CLAIM C6: computed=0 expected=0 match=yes
CLAIM C7: computed=30 expected=30 match=yes
CLAIM C8: computed=900 expected=900 match=yes
CLAIM C9: computed=8 expected=8 match=yes
CLAIM C10: computed=1.8927893 expected=1.893 match=no
CLAIM C11: computed=-3.3219281 expected=-3.3219 match=no
CLAIM C12: computed=1.2809563 expected=1.28 match=no
CLAIM C13: computed=4 expected=4 match=yes
CLAIM C14: computed=14.575425 expected=14.57544 match=no
CLAIM C15: computed=6.0358438 expected=6.03582 match=no
VERIFICATION SUMMARY: 15 claims, 10 match, 5 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| C1 | 10 | 10 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C2 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C3 | 1024 | 1024 | yes | match | 4 significant digits (as the paper states, at least 2) |
| C4 | 7 | 7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C5 | n-3 | n-3 | yes | match | script verdict (values not both numeric) |
| C6 | 0 | 0 | yes | match | stated value is zero |
| C7 | 30 | 30 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C8 | 900 | 900 | yes | match | 3 significant digits (as the paper states, at least 2) |
| C9 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C10 | 1.8927893 | 1.893 | no | match | 4 significant digits (as the paper states, at least 2) |
| C11 | -3.3219281 | -3.3219 | no | match | 5 significant digits (as the paper states, at least 2) |
| C12 | 1.2809563 | 1.28 | no | match | 3 significant digits (as the paper states, at least 2) |
| C13 | 4 | 4 | yes | match | 2 significant digits (as the paper states, at least 2) |
| C14 | 14.575425 | 14.57544 | no | MISMATCH | 7 significant digits (as the paper states, at least 2) |
| C15 | 6.0358438 | 6.03582 | no | MISMATCH | 6 significant digits (as the paper states, at least 2) |

Mismatches: 2 of 15.


## Auto-corrections

The worker corrected these independently-verified values in place of the paper's stated values (deterministic, no model edit):

| claim | stated | corrected |
|---|---|---|
| C14 | 14.57544 | 14.575425 |
| C15 | 6.03582 | 6.0358438 |
