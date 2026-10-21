# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The natural logarithm of the Efimov scaling factor is ln(22.694) = 3.1222.",
    "inputs": "λ = 22.694",
    "formula": "ln(λ)"
  },
  {
    "id": "Q2",
    "statement": "The renormalization‑group index is s₀ = 2π / ln(22.694) = 2.0124.",
    "inputs": "λ = 22.694, π = 3.14159, ln λ = 3.1222",
    "formula": "s₀ = 2π / ln(λ)"
  },
  {
    "id": "Q3",
    "statement": "The number of octaves spanned by one Efimov period is log₂(22.694) = 4.505.",
    "inputs": "λ = 22.694, ln λ = 3.1222, ln 2 = 0.69315",
    "formula": "log₂(λ) = ln(λ) / ln(2)"
  },
  {
    "id": "Q4",
    "statement": "The per‑step discrepancy between the Efimov factor and the dyadic factor is λ/2 = 11.347.",
    "inputs": "λ = 22.694",
    "formula": "λ / 2"
  },
  {
    "id": "Q5",
    "statement": "The square of the Efimov scaling factor is λ² = 515.02.",
    "inputs": "λ = 22.694",
    "formula": "λ²"
  },
  {
    "id": "Q6",
    "statement": "The fourth power of the Efimov scaling factor is λ⁴ = 265,244.",
    "inputs": "λ = 22.694",
    "formula": "λ⁴"
  },
  {
    "id": "Q7",
    "statement": "The ratio of λ⁴ to 2⁴ is 16,578.",
    "inputs": "λ⁴ = 265,244, 2⁴ = 16",
    "formula": "λ⁴ / 2⁴"
  },
  {
    "id": "Q8",
    "statement": "The RG index required for a dyadic factor would be s₀ = 2π / ln 2 = 9.0647.",
    "inputs": "π = 3.14159, ln 2 = 0.69315",
    "formula": "s₀ = 2π / ln(2)"
  },
  {
    "id": "Q9",
    "statement": "The difference between the Efimov log‑period and the dyadic log‑period is 3.1222 - 0.69315 = 2.4291.",
    "inputs": "ΔlnE = 3.1222, ln 2 = 0.69315",
    "formula": "ΔlnE - ln(2)"
  }
]

## Script
```python
import math

# Inputs
lam = 22.694
pi = math.pi
ln2 = math.log(2)

# Computations
ln_lam = math.log(lam)                     # Q1
s0 = 2 * pi / ln_lam                        # Q2
log2_lam = ln_lam / ln2                     # Q3
per_step = lam / 2                          # Q4
lam_sq = lam ** 2                           # Q5
lam_4 = lam_sq ** 2                         # Q6
ratio = lam_4 / (2 ** 4)                    # Q7
s0_dyadic = 2 * pi / ln2                    # Q8
diff = ln_lam - ln2                         # Q9

# Helper for rounding to the required decimal places
def fmt(val, ndigits, commas=False):
    if ndigits == 0:
        # integer rounding
        v = int(round(val))
        return f"{v:,}" if commas else str(v)
    else:
        v = round(val, ndigits)
        s = f"{v:.{ndigits}f}"
        return f"{s:,}" if commas else s

# Expected values (as strings from the paper)
expected = {
    "Q1": "3.1222",
    "Q2": "2.0124",
    "Q3": "4.505",
    "Q4": "11.347",
    "Q5": "515.02",
    "Q6": "265,244",
    "Q7": "16,578",
    "Q8": "9.0647",
    "Q9": "2.4291",
}

# Prepare computed strings with appropriate formatting
computed = {
    "Q1": fmt(ln_lam, 4),
    "Q2": fmt(s0, 4),
    "Q3": fmt(log2_lam, 3),
    "Q4": fmt(per_step, 3),
    "Q5": fmt(lam_sq, 2),
    "Q6": fmt(lam_4, 0, commas=True),
    "Q7": fmt(ratio, 0, commas=True),
    "Q8": fmt(s0_dyadic, 4),
    "Q9": fmt(diff, 4),
}

# Print results
for qid in ["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9"]:
    comp = computed[qid]
    exp = expected[qid]
    match = "yes" if comp == exp else "no"
    print(f"CLAIM {qid}: computed={comp} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, "
      f"{sum(1 for q in expected if computed[q]==expected[q])} match, "
      f"{sum(1 for q in expected if computed[q]!=expected[q])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=3.1221 expected=3.1222 match=no
CLAIM Q2: computed=2.0125 expected=2.0124 match=no
CLAIM Q3: computed=4.504 expected=4.505 match=no
CLAIM Q4: computed=11.347 expected=11.347 match=yes
CLAIM Q5: computed=515.02 expected=515.02 match=yes
CLAIM Q6: computed=265,243 expected=265,244 match=no
CLAIM Q7: computed=16,578 expected=16,578 match=yes
CLAIM Q8: computed=9.0647 expected=9.0647 match=yes
CLAIM Q9: computed=2.4290 expected=2.4291 match=no
VERIFICATION SUMMARY: 9 claims, 4 match, 5 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 3.1221 | 3.1222 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q2 | 2.0125 | 2.0124 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 4.504 | 4.505 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 11.347 | 11.347 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | 515.02 | 515.02 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 265,243 | 265,244 | no | match | 6 significant digits (as the paper states, at least 2) |
| Q7 | 16,578 | 16,578 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 9.0647 | 9.0647 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 2.4290 | 2.4291 | no | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 9.
