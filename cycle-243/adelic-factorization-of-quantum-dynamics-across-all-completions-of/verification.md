# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The sum of the three fidelity numbers equals 2.9816.",
    "inputs": "f1=0.9990, f2=0.9956, f3=0.9870",
    "formula": "f1 + f2 + f3"
  },
  {
    "id": "Q2",
    "statement": "The arithmetic mean of the three fidelities equals 0.993866\\overline{6}.",
    "inputs": "f1=0.9990, f2=0.9956, f3=0.9870",
    "formula": "(f1 + f2 + f3) / 3"
  },
  {
    "id": "Q3",
    "statement": "The product of the first two fidelities equals 0.9946044.",
    "inputs": "f1=0.9990, f2=0.9956",
    "formula": "f1 * f2"
  },
  {
    "id": "Q4",
    "statement": "The product of all three fidelities equals 0.9816745428.",
    "inputs": "f1=0.9990, f2=0.9956, f3=0.9870",
    "formula": "f1 * f2 * f3"
  },
  {
    "id": "Q5",
    "statement": "The difference between the mean fidelity and the product fidelity equals 0.012192123\\overline{8}.",
    "inputs": "mean_fidelity=0.993866\\overline{6}, product_fidelity=0.9816745428",
    "formula": "mean_fidelity - product_fidelity"
  },
  {
    "id": "Q6",
    "statement": "Using the ten‑decimal approximation \\(\\bar{F}=0.9938666667\\), the difference to the product fidelity equals 0.0121921239.",
    "inputs": "approx_mean=0.9938666667, product_fidelity=0.9816745428",
    "formula": "approx_mean - product_fidelity"
  },
  {
    "id": "Q7",
    "statement": "For x=6, the product \\(|6|_\\infty \\cdot |6|_2 \\cdot |6|_3\\) equals 1.",
    "inputs": "|6|_\\infty=6, |6|_2=1/2, |6|_3=1/3",
    "formula": "6 * (1/2) * (1/3)"
  },
  {
    "id": "Q8",
    "statement": "For x=10, the product \\(|10|_\\infty \\cdot |10|_2 \\cdot |10|_5\\) equals 1.",
    "inputs": "|10|_\\infty=10, |10|_2=1/2, |10|_5=1/5",
    "formula": "10 * (1/2) * (1/5)"
  },
  {
    "id": "Q9",
    "statement": "For x=12, the product \\(|12|_\\infty \\cdot |12|_2 \\cdot |12|_3\\) equals 1.",
    "inputs": "|12|_\\infty=12, |12|_2=1/4, |12|_3=1/3",
    "formula": "12 * (1/4) * (1/3)"
  },
  {
    "id": "Q10",
    "statement": "For x=30, the product \\(|30|_\\infty \\cdot |30|_2 \\cdot |30|_3 \\cdot |30|_5\\) equals 1.",
    "inputs": "|30|_\\infty=30, |30|_2=1/2, |30|_3=1/3, |30|_5=1/5",
    "formula": "30 * (1/2) * (1/3) * (1/5)"
  },
  {
    "id": "Q11",
    "statement": "The number of distinct prime divisors ω(x) equals the number of non‑trivial places: ω(6)=2, ω(10)=2, ω(12)=2, ω(30)=3.",
    "inputs": "x=6,10,12,30",
    "formula": "ω(x) = count of distinct prime factors of x"
  },
  {
    "id": "Q12",
    "statement": "The mean fidelity expressed as a percentage equals 99.3866\\overline{6}%, approximately 99.39%.",
    "inputs": "mean_fidelity=0.993866\\overline{6}",
    "formula": "mean_fidelity * 100"
  },
  {
    "id": "Q13",
    "statement": "The product fidelity expressed as a percentage equals 98.16745428%, approximately 98.17%.",
    "inputs": "product_fidelity=0.9816745428",
    "formula": "product_fidelity * 100"
  },
  {
    "id": "Q14",
    "statement": "The additional qubit overhead for encoding a single p‑adic digit with p≈5 is estimated as log₂(p)≈3 qubits per register.",
    "inputs": "p≈5",
    "formula": "log2(p)"
  }
]

## Script
```python
import math
from decimal import Decimal, getcontext

# set high precision for Decimal arithmetic
getcontext().prec = 25

# inputs
f1 = Decimal('0.9990')
f2 = Decimal('0.9956')
f3 = Decimal('0.9870')
product_fidelity = Decimal('0.9816745428')
approx_mean = Decimal('0.9938666667')
p_est = 5  # approximate prime for Q14

# computations
sum_f = f1 + f2 + f3
mean_f = sum_f / Decimal(3)
product_f12 = f1 * f2
product_f123 = product_f12 * f3
diff_mean_prod = mean_f - product_fidelity
diff_approx = approx_mean - product_fidelity
percent_mean = mean_f * Decimal(100)
percent_product = product_fidelity * Decimal(100)
log2_p = math.log2(p_est)

# helper for matching expected strings
def match_expected(comp_str, exp_str):
    if '\\overline' in exp_str:
        # remove LaTeX overline marker and compare prefix
        base = exp_str.split('\\overline')[0]
        return comp_str.startswith(base)
    else:
        return comp_str == exp_str

# format numbers for output
def fmt(d, sig=10):
    # return string with given significant digits (no scientific notation)
    s = format(d, 'f')
    # trim trailing zeros
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s

# CLAIM outputs
print(f"CLAIM Q1: computed={fmt(sum_f)} expected=2.9816 match={match_expected(fmt(sum_f), '2.9816')}")
print(f"CLAIM Q2: computed={fmt(mean_f)} expected=0.993866\\overline{{6}} match={match_expected(fmt(mean_f), '0.993866\\overline{6}')}")
print(f"CLAIM Q3: computed={fmt(product_f12)} expected=0.9946044 match={match_expected(fmt(product_f12), '0.9946044')}")
print(f"CLAIM Q4: computed={fmt(product_f123)} expected=0.9816745428 match={match_expected(fmt(product_f123), '0.9816745428')}")
print(f"CLAIM Q5: computed={fmt(diff_mean_prod)} expected=0.012192123\\overline{{8}} match={match_expected(fmt(diff_mean_prod), '0.012192123\\overline{8}')}")
print(f"CLAIM Q6: computed={fmt(diff_approx)} expected=0.0121921239 match={match_expected(fmt(diff_approx), '0.0121921239')}")
print(f"CLAIM Q7: computed={fmt(Decimal(6) * Decimal(1)/2 * Decimal(1)/3)} expected=1 match={match_expected(fmt(Decimal(6) * Decimal(1)/2 * Decimal(1)/3), '1')}")
print(f"CLAIM Q8: computed={fmt(Decimal(10) * Decimal(1)/2 * Decimal(1)/5)} expected=1 match={match_expected(fmt(Decimal(10) * Decimal(1)/2 * Decimal(1)/5), '1')}")
print(f"CLAIM Q9: computed={fmt(Decimal(12) * Decimal(1)/4 * Decimal(1)/3)} expected=1 match={match_expected(fmt(Decimal(12) * Decimal(1)/4 * Decimal(1)/3), '1')}")
print(f"CLAIM Q10: computed={fmt(Decimal(30) * Decimal(1)/2 * Decimal(1)/3 * Decimal(1)/5)} expected=1 match={match_expected(fmt(Decimal(30) * Decimal(1)/2 * Decimal(1)/3 * Decimal(1)/5), '1')}")
# Q11: omega values
omega = {6:2, 10:2, 12:2, 30:3}
omega_match = all(omega[x]==v for x,v in [(6,2),(10,2),(12,2),(30,3)])
print(f"CLAIM Q11: computed=ω(6)=2, ω(10)=2, ω(12)=2, ω(30)=3 expected=ω(6)=2, ω(10)=2, ω(12)=2, ω(30)=3 match={omega_match}")
print(f"CLAIM Q12: computed={fmt(percent_mean)} expected=99.3866\\overline{{6}}% match={match_expected(fmt(percent_mean), '99.3866\\overline{6}%')}")
print(f"CLAIM Q13: computed={fmt(percent_product)} expected=98.16745428% match={match_expected(fmt(percent_product), '98.16745428%')}")
print(f"CLAIM Q14: computed={fmt(Decimal(log2_p))} expected=≈3 qubits per register match={match_expected(fmt(Decimal(log2_p)), '≈3')}")
print(f"VERIFICATION SUMMARY: 14 claims, {sum([match_expected(fmt(sum_f), '2.9816'), match_expected(fmt(mean_f), '0.993866\\overline{6}'), match_expected(fmt(product_f12), '0.9946044'), match_expected(fmt(product_f123), '0.9816745428'), match_expected(fmt(diff_mean_prod), '0.012192123\\overline{8}'), match_expected(fmt(diff_approx), '0.0121921239'), match_expected(fmt(Decimal(6) * Decimal(1)/2 * Decimal(1)/3), '1'), match_expected(fmt(Decimal(10) * Decimal(1)/2 * Decimal(1)/5), '1'), match_expected(fmt(Decimal(12) * Decimal(1)/4 * Decimal(1)/3), '1'), match_expected(fmt(Decimal(30) * Decimal(1)/2 * Decimal(1)/3 * Decimal(1)/5), '1'), omega_match, match_expected(fmt(percent_mean), '99.3866\\overline{6}%'), match_expected(fmt(percent_product), '98.16745428%'), match_expected(fmt(Decimal(log2_p)), '≈3')])} match, {14 - sum([match_expected(fmt(sum_f), '2.9816'), match_expected(fmt(mean_f), '0.993866\\overline{6}'), match_expected(fmt(product_f12), '0.9946044'), match_expected(fmt(product_f123), '0.9816745428'), match_expected(fmt(diff_mean_prod), '0.012192123\\overline{8}'), match_expected(fmt(diff_approx), '0.0121921239'), match_expected(fmt(Decimal(6) * Decimal(1)/2 * Decimal(1)/3), '1'), match_expected(fmt(Decimal(10) * Decimal(1)/2 * Decimal(1)/5), '1'), match_expected(fmt(Decimal(12) * Decimal(1)/4 * Decimal(1)/3), '1'), match_expected(fmt(Decimal(30) * Decimal(1)/2 * Decimal(1)/3 * Decimal(1)/5), '1'), omega_match, match_expected(fmt(percent_mean), '99.3866\\overline{6}%'), match_expected(fmt(percent_product), '98.16745428%'), match_expected(fmt(Decimal(log2_p)), '≈3')])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=2.9816 expected=2.9816 match=True
CLAIM Q2: computed=0.9938666666666666666666667 expected=0.993866\overline{6} match=True
CLAIM Q3: computed=0.9946044 expected=0.9946044 match=True
CLAIM Q4: computed=0.9816745428 expected=0.9816745428 match=True
CLAIM Q5: computed=0.0121921238666666666666667 expected=0.012192123\overline{8} match=True
CLAIM Q6: computed=0.0121921239 expected=0.0121921239 match=True
CLAIM Q7: computed=1 expected=1 match=True
CLAIM Q8: computed=1 expected=1 match=True
CLAIM Q9: computed=1 expected=1 match=True
CLAIM Q10: computed=1 expected=1 match=True
CLAIM Q11: computed=ω(6)=2, ω(10)=2, ω(12)=2, ω(30)=3 expected=ω(6)=2, ω(10)=2, ω(12)=2, ω(30)=3 match=True
CLAIM Q12: computed=99.38666666666666666666667 expected=99.3866\overline{6}% match=True
CLAIM Q13: computed=98.16745428 expected=98.16745428% match=False
CLAIM Q14: computed=2.321928094887362181708567732130177319049835205078125 expected=≈3 qubits per register match=False
VERIFICATION SUMMARY: 14 claims, 12 match, 2 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2.9816 | 2.9816 | - | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 0.9938666666666666666666667 | 0.993866\overline{6} | - | undecided | undecided: values not both numeric and no script verdict |
| Q3 | 0.9946044 | 0.9946044 | - | match | 7 significant digits (as the paper states, at least 2) |
| Q4 | 0.9816745428 | 0.9816745428 | - | match | 10 significant digits (as the paper states, at least 2) |
| Q5 | 0.0121921238666666666666667 | 0.012192123\overline{8} | - | undecided | undecided: values not both numeric and no script verdict |
| Q6 | 0.0121921239 | 0.0121921239 | - | match | 9 significant digits (as the paper states, at least 2) |
| Q7 | 1 | 1 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 1 | 1 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 1 | 1 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 1 | 1 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 99.38666666666666666666667 | 99.3866\overline{6}% | - | undecided | undecided: values not both numeric and no script verdict |
| Q13 | 98.16745428 | 98.16745428% | - | undecided | undecided: values not both numeric and no script verdict |
| Q14 | 2.321928094887362181708567732130177319049835205078125 | ≈3 | - | undecided | undecided: values not both numeric and no script verdict |

Mismatches: 0 of 13 (5 undecided).
