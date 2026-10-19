# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The sum of the three fidelity numbers is 2.9816.",
    "inputs": "f1 = 0.9990, f2 = 0.9956, f3 = 0.9870",
    "formula": "sum = f1 + f2 + f3"
  },
  {
    "id": "Q2",
    "statement": "The arithmetic mean fidelity \\(\\bar{F}\\) equals 0.993866666666667.",
    "inputs": "sum = 2.9816, divisor = 3",
    "formula": "mean = sum / divisor"
  },
  {
    "id": "Q3",
    "statement": "The product of the single‑qubit and two‑qubit fidelities is 0.9946044.",
    "inputs": "f1 = 0.9990, f2 = 0.9956",
    "formula": "product12 = f1 * f2"
  },
  {
    "id": "Q4",
    "statement": "The overall product fidelity \\(F_{\\text{prod}}\\) equals 0.9816745428.",
    "inputs": "product12 = 0.9946044, f3 = 0.9870",
    "formula": "F_prod = product12 * f3"
  },
  {
    "id": "Q5",
    "statement": "The gap between the mean fidelity and the product fidelity is 0.0121921238.",
    "inputs": "mean = 0.993866666666667, F_prod = 0.9816745428",
    "formula": "Δ = mean - F_prod"
  },
  {
    "id": "Q6",
    "statement": "For \\(x = 6\\), the product \\(|x|_{\\infty}\\prod_{p}|x|_{p}\\) equals 1.",
    "inputs": "x = 6 = 2^1 \\cdot 3^1, |6|_{\\infty}=6, |6|_{2}=2^{-1}=0.5, |6|_{3}=3^{-1}=1/3",
    "formula": "6 * 0.5 * (1/3) = 1"
  },
  {
    "id": "Q7",
    "statement": "For \\(x = 10\\), the product \\(|x|_{\\infty}\\prod_{p}|x|_{p}\\) equals 1.",
    "inputs": "x = 10 = 2^1 \\cdot 5^1, |10|_{\\infty}=10, |10|_{2}=0.5, |10|_{5}=0.2",
    "formula": "10 * 0.5 * 0.2 = 1"
  },
  {
    "id": "Q8",
    "statement": "For \\(x = 12\\), the product \\(|x|_{\\infty}\\prod_{p}|x|_{p}\\) equals 1.",
    "inputs": "x = 12 = 2^2 \\cdot 3^1, |12|_{\\infty}=12, |12|_{2}=2^{-2}=0.25, |12|_{3}=1/3",
    "formula": "12 * 0.25 * (1/3) = 1"
  },
  {
    "id": "Q9",
    "statement": "The crossover length derived from the suppression law is \\(\\ell = 2.4263\\times10^{-6}\\,\\text{m}\\).",
    "inputs": "λ_C = 2.4263\\times10^{-12}\\,\\text{m}, target ratio = 10^{-6}",
    "formula": "ℓ = λ_C / (10^{-6})"
  },
  {
    "id": "Q10",
    "statement": "The mean fidelity expressed as a percentage is 99.3867\\%.",
    "inputs": "mean = 0.993866666666667",
    "formula": "percent = mean \\times 100"
  },
  {
    "id": "Q11",
    "statement": "The product fidelity expressed as a percentage is 98.16745428\\%.",
    "inputs": "F_prod = 0.9816745428",
    "formula": "percent = F_prod \\times 100"
  }
]

## Script
```python
# Verification script for quantitative claims in the paper
# Computes each claim from the stated inputs and compares to the expected values.

def fmt(x, sig):
    """Format number with given significant digits (or decimal places)."""
    return f"{x:.{sig}g}"

def round_to_places(x, places):
    """Round x to a given number of decimal places."""
    return round(x, places)

def main():
    # Inputs
    f1 = 0.9990
    f2 = 0.9956
    f3 = 0.9870
    lambda_C = 2.4263e-12
    target_ratio = 1e-6

    # Q1
    sum_f = f1 + f2 + f3
    exp_Q1 = "2.9816"
    match_Q1 = "yes" if abs(sum_f - 2.9816) < 1e-12 else "no"
    print(f"CLAIM Q1: computed={sum_f:.10f} expected={exp_Q1} match={match_Q1}")

    # Q2
    mean = sum_f / 3
    exp_Q2 = "0.993866666666667"
    # round to 15 decimal places to compare (as many as in expected)
    match_Q2 = "yes" if round(mean, 15) == 0.993866666666667 else "no"
    print(f"CLAIM Q2: computed={mean:.15f} expected={exp_Q2} match={match_Q2}")

    # Q3
    prod12 = f1 * f2
    exp_Q3 = "0.9946044"
    match_Q3 = "yes" if abs(prod12 - 0.9946044) < 1e-12 else "no"
    print(f"CLAIM Q3: computed={prod12:.7f} expected={exp_Q3} match={match_Q3}")

    # Q4
    F_prod = prod12 * f3
    exp_Q4 = "0.9816745428"
    match_Q4 = "yes" if abs(F_prod - 0.9816745428) < 1e-12 else "no"
    print(f"CLAIM Q4: computed={F_prod:.10f} expected={exp_Q4} match={match_Q4}")

    # Q5
    delta = mean - F_prod
    exp_Q5 = "0.0121921238"
    # statement has 10 decimal places; round computed to 10 places for comparison
    delta_rounded = round(delta, 10)
    match_Q5 = "yes" if delta_rounded == 0.0121921238 else "no"
    print(f"CLAIM Q5: computed={delta:.13f} expected={exp_Q5} match={match_Q5}")

    # Q6
    prod6 = 6 * 0.5 * (1/3)
    exp_Q6 = "1"
    match_Q6 = "yes" if abs(prod6 - 1) < 1e-12 else "no"
    print(f"CLAIM Q6: computed={prod6:.1f} expected={exp_Q6} match={match_Q6}")

    # Q7
    prod10 = 10 * 0.5 * 0.2
    exp_Q7 = "1"
    match_Q7 = "yes" if abs(prod10 - 1) < 1e-12 else "no"
    print(f"CLAIM Q7: computed={prod10:.1f} expected={exp_Q7} match={match_Q7}")

    # Q8
    prod12_abs = 12 * 0.25 * (1/3)
    exp_Q8 = "1"
    match_Q8 = "yes" if abs(prod12_abs - 1) < 1e-12 else "no"
    print(f"CLAIM Q8: computed={prod12_abs:.1f} expected={exp_Q8} match={match_Q8}")

    # Q9
    ell = lambda_C / target_ratio
    exp_Q9 = "2.4263e-06"
    match_Q9 = "yes" if abs(ell - 2.4263e-6) < 1e-12 else "no"
    print(f"CLAIM Q9: computed={ell:.10e} expected={exp_Q9} match={match_Q9}")

    # Q10
    percent_mean = mean * 100
    exp_Q10 = "99.3867%"
    # round to 4 decimal places as in statement
    percent_mean_rounded = round(percent_mean, 4)
    match_Q10 = "yes" if percent_mean_rounded == 99.3867 else "no"
    print(f"CLAIM Q10: computed={percent_mean_rounded:.4f}% expected={exp_Q10} match={match_Q10}")

    # Q11
    percent_F = F_prod * 100
    exp_Q11 = "98.16745428%"
    # round to 8 decimal places as in statement
    percent_F_rounded = round(percent_F, 8)
    match_Q11 = "yes" if percent_F_rounded == 98.16745428 else "no"
    print(f"CLAIM Q11: computed={percent_F_rounded:.8f}% expected={exp_Q11} match={match_Q11}")

    # Summary
    total = 11
    matches = sum(1 for m in [match_Q1, match_Q2, match_Q3, match_Q4, match_Q5,
                              match_Q6, match_Q7, match_Q8, match_Q9,
                              match_Q10, match_Q11] if m == "yes")
    mismatches = total - matches
    print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {mismatches} mismatch")

if __name__ == "__main__":
    main()

```

## Execution output
```
CLAIM Q1: computed=2.9816000000 expected=2.9816 match=yes
CLAIM Q2: computed=0.993866666666667 expected=0.993866666666667 match=yes
CLAIM Q3: computed=0.9946044 expected=0.9946044 match=yes
CLAIM Q4: computed=0.9816745428 expected=0.9816745428 match=yes
CLAIM Q5: computed=0.0121921238667 expected=0.0121921238 match=no
CLAIM Q6: computed=1.0 expected=1 match=yes
CLAIM Q7: computed=1.0 expected=1 match=yes
CLAIM Q8: computed=1.0 expected=1 match=yes
CLAIM Q9: computed=2.4263000000e-06 expected=2.4263e-06 match=yes
CLAIM Q10: computed=99.3867% expected=99.3867% match=yes
CLAIM Q11: computed=98.16745428% expected=98.16745428% match=yes
VERIFICATION SUMMARY: 11 claims, 10 match, 1 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2.9816000000 | 2.9816 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 0.993866666666667 | 0.993866666666667 | yes | match | 15 significant digits (as the paper states, at least 2) |
| Q3 | 0.9946044 | 0.9946044 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q4 | 0.9816745428 | 0.9816745428 | yes | match | 10 significant digits (as the paper states, at least 2) |
| Q5 | 0.0121921238667 | 0.0121921238 | no | match | 9 significant digits (as the paper states, at least 2) |
| Q6 | 1.0 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 1.0 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 1.0 | 1 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 2.4263000000e-06 | 2.4263e-06 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 99.3867% | 99.3867% | yes | match | script verdict (values not both numeric) |
| Q11 | 98.16745428% | 98.16745428% | yes | match | script verdict (values not both numeric) |

Mismatches: 0 of 11.
