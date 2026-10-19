# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The number of leaves in a depth‑$k$ $p$‑adic tree is $p^{k}=27$.",
    "inputs": "p = 3, k = 3",
    "formula": "p^k"
  },
  {
    "id": "Q2",
    "statement": "Each leaf carries equal weight $w = 1/p^{k}=1/27 \\approx 0.037037$.",
    "inputs": "p = 3, k = 3",
    "formula": "1/(p^k)"
  },
  {
    "id": "Q3",
    "statement": "The Shannon entropy of the uniform leaf distribution is $H = \\log_{2}(p^{k}) = \\log_{2}(27) \\approx 4.7548875$ bits.",
    "inputs": "p = 3, k = 3",
    "formula": "log2(p^k)"
  },
  {
    "id": "Q4",
    "statement": "The modulation amplitude from truncation is $\\epsilon = |p^{k}-1|/p^{k}=26/27 \\approx 0.96296$.",
    "inputs": "p = 3, k = 3",
    "formula": "abs(p^k - 1) / (p^k)"
  },
  {
    "id": "Q5",
    "statement": "The effective normalized amplitude used in the log‑periodic term is $\\epsilon_{\\text{eff}} = 1/p^{k}=1/27 \\approx 0.03704$.",
    "inputs": "p = 3, k = 3",
    "formula": "1/(p^k)"
  },
  {
    "id": "Q6",
    "statement": "A prototype operating at a 100 MHz clock would produce a raw bit rate of $R = H \\times f = 4.7548875\\times10^{8} \\approx 475.5$ Mbit/s.",
    "inputs": "H = 4.7548875 bits, f = 100e6 Hz",
    "formula": "H * f"
  },
  {
    "id": "Q7",
    "statement": "With $10^{6}$ trials and $27$ possible output bins, the expected count per bin is $n_{\\text{exp}} = 10^{6}/27 \\approx 37037$.",
    "inputs": "trials = 1000000, bins = 27",
    "formula": "trials / bins"
  },
  {
    "id": "Q8",
    "statement": "The step height of the discrete density on each interval is $p^{k}=27$.",
    "inputs": "p = 3, k = 3",
    "formula": "p^k"
  }
]

## Script
```python
import math

def fmt(val, digits):
    """Format value with given number of decimal places (digits)."""
    if digits == 0:
        return str(int(round(val)))
    fmt_str = "{:." + str(digits) + "f}"
    return fmt_str.format(round(val, digits))

claims = [
    # Q1
    {
        "id": "Q1",
        "computed": 3 ** 3,
        "expected": "27",
        "match": None,
        "digits": 0
    },
    # Q2
    {
        "id": "Q2",
        "computed": 1 / (3 ** 3),
        "expected": "0.037037",
        "match": None,
        "digits": 6
    },
    # Q3
    {
        "id": "Q3",
        "computed": math.log(3 ** 3, 2),
        "expected": "4.7548875",
        "match": None,
        "digits": 7
    },
    # Q4
    {
        "id": "Q4",
        "computed": abs(3 ** 3 - 1) / (3 ** 3),
        "expected": "0.96296",
        "match": None,
        "digits": 5
    },
    # Q5
    {
        "id": "Q5",
        "computed": 1 / (3 ** 3),
        "expected": "0.03704",
        "match": None,
        "digits": 5
    },
    # Q6
    {
        "id": "Q6",
        "computed": (4.7548875 * 100e6) / 1e6,  # convert to Mbit/s
        "expected": "475.5",
        "match": None,
        "digits": 1
    },
    # Q7
    {
        "id": "Q7",
        "computed": 1_000_000 / 27,
        "expected": "37037",
        "match": None,
        "digits": 0
    },
    # Q8
    {
        "id": "Q8",
        "computed": 3 ** 3,
        "expected": "27",
        "match": None,
        "digits": 0
    },
]

for c in claims:
    comp_str = fmt(c["computed"], c["digits"])
    c["match"] = "yes" if comp_str == c["expected"] else "no"
    print(f"CLAIM {c['id']}: computed={comp_str} expected={c['expected']} match={c['match']}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, "
      f"{sum(1 for c in claims if c['match']=='yes')} match, "
      f"{sum(1 for c in claims if c['match']=='no')} mismatch")

```

## Execution output
```
CLAIM Q1: computed=27 expected=27 match=yes
CLAIM Q2: computed=0.037037 expected=0.037037 match=yes
CLAIM Q3: computed=4.7548875 expected=4.7548875 match=yes
CLAIM Q4: computed=0.96296 expected=0.96296 match=yes
CLAIM Q5: computed=0.03704 expected=0.03704 match=yes
CLAIM Q6: computed=475.5 expected=475.5 match=yes
CLAIM Q7: computed=37037 expected=37037 match=yes
CLAIM Q8: computed=27 expected=27 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 27 | 27 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.037037 | 0.037037 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 4.7548875 | 4.7548875 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q4 | 0.96296 | 0.96296 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | 0.03704 | 0.03704 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 475.5 | 475.5 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 37037 | 37037 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 27 | 27 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 8.
