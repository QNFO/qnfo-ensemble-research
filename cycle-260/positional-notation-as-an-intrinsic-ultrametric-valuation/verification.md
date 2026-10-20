# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The total number of unordered distinct pairs of integers from 0 to 999 is 499,500.",
    "inputs": "N = 1000 (total integers)",
    "formula": "C = N \\times (N-1) / 2"
  },
  {
    "id": "Q2",
    "statement": "The number of unordered pairs of decimal integers 0–999 that share the same last digit (valuation \\(v_{10} \\ge 1\\)) is 49,500.",
    "inputs": "10 residue classes modulo 10, each containing 100 numbers",
    "formula": "10 \\times \\binom{100}{2} = 10 \\times 100 \\times 99 / 2"
  },
  {
    "id": "Q3",
    "statement": "The number of unordered pairs of decimal integers 0–999 that share the same last two digits (valuation \\(v_{10} \\ge 2\\)) is 4,500.",
    "inputs": "100 residue classes modulo 100, each containing 10 numbers",
    "formula": "100 \\times \\binom{10}{2} = 100 \\times 10 \\times 9 / 2"
  },
  {
    "id": "Q4",
    "statement": "The number of unordered pairs of decimal integers 0–999 with valuation \\(v_{10}=0\\) (distance 1) is 450,000.",
    "inputs": "Total pairs = 499,500; pairs with \\(v_{10}\\ge1\\) = 49,500",
    "formula": "499,500 - 49,500"
  },
  {
    "id": "Q5",
    "statement": "The number of unordered pairs of decimal integers 0–999 with valuation \\(v_{10}=1\\) (distance 0.1) is 45,000.",
    "inputs": "Pairs with \\(v_{10}\\ge1\\) = 49,500; pairs with \\(v_{10}\\ge2\\) = 4,500",
    "formula": "49,500 - 4,500"
  },
  {
    "id": "Q6",
    "statement": "The number of unordered pairs of decimal integers 0–999 with valuation \\(v_{10}=2\\) (distance 0.01) is 4,500.",
    "inputs": "Pairs with \\(v_{10}\\ge2\\) = 4,500",
    "formula": "4,500"
  },
  {
    "id": "Q7",
    "statement": "The total number of unordered distinct pairs of integers from 0 to 99 is 4,950.",
    "inputs": "n = 100 (total integers)",
    "formula": "C = n \\times (n-1) / 2"
  },
  {
    "id": "Q8",
    "statement": "Among integers 0–99, 450 unordered pairs share the same last digit (valuation \\(v_{10}=1\\)).",
    "inputs": "10 residue classes modulo 10, each containing 10 numbers",
    "formula": "10 \\times \\binom{10}{2} = 10 \\times 10 \\times 9 / 2"
  },
  {
    "id": "Q9",
    "statement": "The mean \\(10\\)-adic distance for the interval 0–99 is \\(\\frac{101}{110} \\approx 0.9181818\\).",
    "inputs": "450 pairs at distance 0.1, 4,500 pairs at distance 1, total pairs 4,950",
    "formula": "(450 \\times 0.1 + 4,500 \\times 1) / 4,950"
  },
  {
    "id": "Q10",
    "statement": "The sum of all Euclidean differences \\(y-x\\) for 0 \\le x < y \\le 99 is 166,650.",
    "inputs": "n = 100",
    "formula": "(1/6) \\times n \\times (n^{2} - 1)"
  },
  {
    "id": "Q11",
    "statement": "The diameter‑normalized Euclidean mean distance for 0–99 is \\(\\frac{101}{297} \\approx 0.34006734\\).",
    "inputs": "Sum of differences = 166,650; total pairs = 4,950; diameter = 99",
    "formula": "166,650 / (4,950 \\times 99)"
  },
  {
    "id": "Q12",
    "statement": "The ratio of the mean \\(10\\)-adic distance to the normalized Euclidean mean for 0–99 equals 2.70.",
    "inputs": "Mean \\(10\\)-adic = 101/110; mean Euclidean = 101/297",
    "formula": "(101/110) / (101/297) = 297/110"
  },
  {
    "id": "Q13",
    "statement": "The number of unordered pairs of integers 0–99 whose Euclidean distance is at most 9 is 855.",
    "inputs": "For i = 0..90, 9 pairs each; for i = 91..99, decreasing counts 8+7+…+0",
    "formula": "91 \\times 9 + (8+7+6+5+4+3+2+1+0) = 819 + 36"
  },
  {
    "id": "Q14",
    "statement": "For a base \\(b\\) and digit width \\(m\\), the total number of unordered distinct pairs in \\(\\mathcal{I}_{b,m}=\\{0,\\dots,b^{m}-1\\}\\) is \\(\\frac{b^{m}(b^{m}-1)}{2}\\).",
    "inputs": "b (integer \\(\\ge2\\)), m (positive integer)",
    "formula": "\\binom{b^{m}}{2} = b^{m}(b^{m}-1)/2"
  },
  {
    "id": "Q15",
    "statement": "The cumulative number of unordered pairs with valuation at least \\(k\\) is \\(C_{\\ge k}=\\frac{b^{m}(b^{m-k}-1)}{2}\\).",
    "inputs": "b, m, k (0 \\le k \\le m-1)",
    "formula": "C_{\\ge k}=b^{k}\\times \\binom{b^{m-k}}{2}=\\frac{b^{m}(b^{m-k}-1)}{2}"
  },
  {
    "id": "Q16",
    "statement": "The exact number of unordered pairs with valuation exactly \\(k\\) is \\(N_{k}=\\frac{b^{2m-k-1}(b-1)}{2}\\).",
    "inputs": "b, m, k (0 \\le k \\le m-1)",
    "formula": "N_{k}=C_{\\ge k}-C_{\\ge k+1}=\\frac{b^{2m-k-1}(b-1)}{2}"
  }
]

## Script
```python
# Verification script for quantitative claims Q1–Q16

def compute_Q1():
    N = 1000
    C = N * (N - 1) // 2
    return C, "499500"

def compute_Q2():
    # 10 residue classes, each with 100 numbers
    pairs_per_class = 100 * 99 // 2
    total = 10 * pairs_per_class
    return total, "49500"

def compute_Q3():
    # 100 residue classes, each with 10 numbers
    pairs_per_class = 10 * 9 // 2
    total = 100 * pairs_per_class
    return total, "4500"

def compute_Q4():
    total_pairs = 499500
    ge1 = 49500
    result = total_pairs - ge1
    return result, "450000"

def compute_Q5():
    ge1 = 49500
    ge2 = 4500
    result = ge1 - ge2
    return result, "45000"

def compute_Q6():
    result = 4500
    return result, "4500"

def compute_Q7():
    n = 100
    C = n * (n - 1) // 2
    return C, "4950"

def compute_Q8():
    # 10 residue classes, each with 10 numbers
    pairs_per_class = 10 * 9 // 2
    total = 10 * pairs_per_class
    return total, "450"

def compute_Q9():
    pairs_0_1 = 450   # distance 0.1
    pairs_1_0 = 4500  # distance 1
    total_pairs = 4950
    mean = (pairs_0_1 * 0.1 + pairs_1_0 * 1) / total_pairs
    # exact fraction 101/110
    return mean, "101/110"

def compute_Q10():
    n = 100
    total = (1/6) * n * (n**2 - 1)
    return int(total), "166650"

def compute_Q11():
    sum_diff = 166650
    total_pairs = 4950
    diameter = 99
    mean = sum_diff / (total_pairs * diameter)
    # exact fraction 101/297
    return mean, "101/297"

def compute_Q12():
    ratio = (101/110) / (101/297)
    return ratio, "2.70"

def compute_Q13():
    count = 91 * 9 + sum(range(9))  # sum 0..8 = 36
    return count, "855"

def compute_Q14():
    # Use the same parameters as the 0–99 case: b=10, m=2
    b = 10
    m = 2
    total = b**m * (b**m - 1) // 2
    return total, "4950"

def compute_Q15():
    # Use b=10, m=2, k=1 (valuation at least 1)
    b = 10
    m = 2
    k = 1
    C_ge_k = b**m * (b**(m - k) - 1) // 2
    return C_ge_k, "450"

def compute_Q16():
    # Use b=10, m=2, k=1 (valuation exactly 1)
    b = 10
    m = 2
    k = 1
    N_k = b**(2*m - k - 1) * (b - 1) // 2
    return N_k, "450"

def main():
    claims = [
        ("Q1", *compute_Q1()),
        ("Q2", *compute_Q2()),
        ("Q3", *compute_Q3()),
        ("Q4", *compute_Q4()),
        ("Q5", *compute_Q5()),
        ("Q6", *compute_Q6()),
        ("Q7", *compute_Q7()),
        ("Q8", *compute_Q8()),
        ("Q9", *compute_Q9()),
        ("Q10", *compute_Q10()),
        ("Q11", *compute_Q11()),
        ("Q12", *compute_Q12()),
        ("Q13", *compute_Q13()),
        ("Q14", *compute_Q14()),
        ("Q15", *compute_Q15()),
        ("Q16", *compute_Q16()),
    ]

    match_count = 0
    for cid, computed, expected in claims:
        # Determine if computed matches expected within the precision implied by expected
        if "/" in expected:  # fraction
            exp_num, exp_den = map(int, expected.split("/"))
            # Compare as exact rational
            if isinstance(computed, float):
                # convert float to fraction with limited denominator
                from fractions import Fraction
                frac = Fraction(computed).limit_denominator()
                match = (frac.numerator == exp_num) and (frac.denominator == exp_den)
            else:
                match = (computed == exp_num / exp_den)
        elif "." in expected:  # decimal with given digits
            # count digits after decimal
            dec_digits = len(expected.split(".")[1])
            fmt = f"{{:.{dec_digits}f}}"
            match = fmt.format(computed) == expected
        else:
            # integer comparison
            match = int(computed) == int(expected.replace(",", ""))
        match_str = "yes" if match else "no"
        if match:
            match_count += 1
        print(f"CLAIM {cid}: computed={computed} expected={expected} match={match_str}")

    total = len(claims)
    print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {total - match_count} mismatch")

if __name__ == "__main__":
    main()

```

## Execution output
```
CLAIM Q1: computed=499500 expected=499500 match=yes
CLAIM Q2: computed=49500 expected=49500 match=yes
CLAIM Q3: computed=4500 expected=4500 match=yes
CLAIM Q4: computed=450000 expected=450000 match=yes
CLAIM Q5: computed=45000 expected=45000 match=yes
CLAIM Q6: computed=4500 expected=4500 match=yes
CLAIM Q7: computed=4950 expected=4950 match=yes
CLAIM Q8: computed=450 expected=450 match=yes
CLAIM Q9: computed=0.9181818181818182 expected=101/110 match=yes
CLAIM Q10: computed=166649 expected=166650 match=no
CLAIM Q11: computed=0.3400673400673401 expected=101/297 match=yes
CLAIM Q12: computed=2.7 expected=2.70 match=yes
CLAIM Q13: computed=855 expected=855 match=yes
CLAIM Q14: computed=4950 expected=4950 match=yes
CLAIM Q15: computed=450 expected=450 match=yes
CLAIM Q16: computed=450 expected=450 match=yes
VERIFICATION SUMMARY: 16 claims, 15 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 499500 | 499500 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q2 | 49500 | 49500 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 4500 | 4500 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 450000 | 450000 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q5 | 45000 | 45000 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 4500 | 4500 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 4950 | 4950 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 450 | 450 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 0.9181818181818182 | 101/110 | yes | match | script verdict (values not both numeric) |
| Q10 | 166649 | 166650 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q11 | 0.3400673400673401 | 101/297 | yes | match | script verdict (values not both numeric) |
| Q12 | 2.7 | 2.70 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 855 | 855 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 4950 | 4950 | yes | match | 4 significant digits (as printed, at least 3) |
| Q15 | 450 | 450 | yes | match | 3 significant digits (as printed, at least 3) |
| Q16 | 450 | 450 | yes | match | 3 significant digits (as printed, at least 3) |

Mismatches: 0 of 16.
