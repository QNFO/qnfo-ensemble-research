# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The square‑root of two is approximately 1.41421356.",
    "inputs": "",
    "formula": "sqrt(2) ≈ 1.41421356"
  },
  {
    "id": "Q2",
    "statement": "For depth 1 the particle mass is m(1)=1.41421356 (mass units).",
    "inputs": "sqrt(2)=1.41421356, d=1",
    "formula": "m = sqrt(2) * d"
  },
  {
    "id": "Q3",
    "statement": "For depth 2 the particle mass is m(2)=2.82842712 (mass units).",
    "inputs": "sqrt(2)=1.41421356, d=2",
    "formula": "m = sqrt(2) * d"
  },
  {
    "id": "Q4",
    "statement": "For depth 3 the particle mass is m(3)=4.24264068 (mass units).",
    "inputs": "sqrt(2)=1.41421356, d=3",
    "formula": "m = sqrt(2) * d"
  },
  {
    "id": "Q5",
    "statement": "Catalan number C₁ equals 1, computed as C₀·C₀.",
    "inputs": "C₀=1",
    "formula": "C₁ = C₀ * C₀"
  },
  {
    "id": "Q6",
    "statement": "Catalan number C₂ equals 2, computed as C₀·C₁ + C₁·C₀.",
    "inputs": "C₀=1, C₁=1",
    "formula": "C₂ = C₀ * C₁ + C₁ * C₀"
  },
  {
    "id": "Q7",
    "statement": "Catalan number C₃ equals 5, computed as C₀·C₂ + C₁·C₁ + C₂·C₀.",
    "inputs": "C₀=1, C₁=1, C₂=2",
    "formula": "C₃ = C₀ * C₂ + C₁ * C₁ + C₂ * C₀"
  },
  {
    "id": "Q8",
    "statement": "The total number of distinct normal forms for depths ≤ 3 is 9, obtained by summing N(0)=1, N(1)=1, N(2)=2, N(3)=5.",
    "inputs": "N(0)=1, N(1)=1, N(2)=2, N(3)=5",
    "formula": "total = N(0) + N(1) + N(2) + N(3)"
  },
  {
    "id": "Q9",
    "statement": "For depth 5 the predicted particle mass is m(5)=7.07106781 (mass units).",
    "inputs": "sqrt(2)=1.41421356, d=5",
    "formula": "m = sqrt(2) * d"
  }
]

## Script
```python
import math

def round_to_str(value, expected):
    """Round value to the same number of decimal places as expected string."""
    if '.' in expected:
        dp = len(expected.split('.')[1])
        rounded = round(value, dp)
        return f"{rounded:.{dp}f}"
    else:
        # integer expected
        return str(int(round(value)))

def check_claim(claim_id, computed, expected):
    comp_str = round_to_str(computed, expected)
    match = "yes" if comp_str == expected else "no"
    print(f"CLAIM {claim_id}: computed={comp_str} expected={expected} match={match}")
    return match == "yes"

def main():
    matches = 0
    total = 0

    # Q1
    total += 1
    computed = math.sqrt(2)
    expected = "1.41421356"
    if check_claim("Q1", computed, expected):
        matches += 1

    # Q2
    total += 1
    sqrt2 = 1.41421356  # input value
    d = 1
    computed = sqrt2 * d
    expected = "1.41421356"
    if check_claim("Q2", computed, expected):
        matches += 1

    # Q3
    total += 1
    d = 2
    computed = sqrt2 * d
    expected = "2.82842712"
    if check_claim("Q3", computed, expected):
        matches += 1

    # Q4
    total += 1
    d = 3
    computed = sqrt2 * d
    expected = "4.24264068"
    if check_claim("Q4", computed, expected):
        matches += 1

    # Q5
    total += 1
    C0 = 1
    computed = C0 * C0
    expected = "1"
    if check_claim("Q5", computed, expected):
        matches += 1

    # Q6
    total += 1
    C1 = 1
    computed = C0 * C1 + C1 * C0
    expected = "2"
    if check_claim("Q6", computed, expected):
        matches += 1

    # Q7
    total += 1
    C2 = 2
    computed = C0 * C2 + C1 * C1 + C2 * C0
    expected = "5"
    if check_claim("Q7", computed, expected):
        matches += 1

    # Q8
    total += 1
    N0, N1, N2, N3 = 1, 1, 2, 5
    computed = N0 + N1 + N2 + N3
    expected = "9"
    if check_claim("Q8", computed, expected):
        matches += 1

    # Q9
    total += 1
    d = 5
    computed = sqrt2 * d
    expected = "7.07106781"
    if check_claim("Q9", computed, expected):
        matches += 1

    print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {total - matches} mismatch")

if __name__ == "__main__":
    main()

```

## Execution output
```
CLAIM Q1: computed=1.41421356 expected=1.41421356 match=yes
CLAIM Q2: computed=1.41421356 expected=1.41421356 match=yes
CLAIM Q3: computed=2.82842712 expected=2.82842712 match=yes
CLAIM Q4: computed=4.24264068 expected=4.24264068 match=yes
CLAIM Q5: computed=1 expected=1 match=yes
CLAIM Q6: computed=2 expected=2 match=yes
CLAIM Q7: computed=5 expected=5 match=yes
CLAIM Q8: computed=9 expected=9 match=yes
CLAIM Q9: computed=7.07106780 expected=7.07106781 match=no
VERIFICATION SUMMARY: 9 claims, 8 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.41421356 | 1.41421356 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q2 | 1.41421356 | 1.41421356 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q3 | 2.82842712 | 2.82842712 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q4 | 4.24264068 | 4.24264068 | yes | match | 9 significant digits (as the paper states, at least 2) |
| Q5 | 1 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 2 | 2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 5 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 9 | 9 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 7.07106780 | 7.07106781 | no | match | 9 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 9.
