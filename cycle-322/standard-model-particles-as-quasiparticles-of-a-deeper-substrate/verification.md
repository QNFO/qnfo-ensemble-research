# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The exclusion‑factor ratio for Higgs masses 115 GeV and 160 GeV is R ≈ 4.43.",
    "inputs": "F115 = 6.2, F160 = 1.4",
    "formula": "R = F115 / F160"
  },
  {
    "id": "Q2",
    "statement": "The bound on the relative self‑energy at 115 GeV is |Σ|/E² ≤ 1.49.",
    "inputs": "F115 = 6.2",
    "formula": "δ ≤ sqrt(F115) - 1 ; |Σ|/E² ≤ δ"
  },
  {
    "id": "Q3",
    "statement": "The bound on the relative self‑energy at 160 GeV is |Σ|/E² ≤ 0.18.",
    "inputs": "F160 = 1.4",
    "formula": "δ ≤ sqrt(F160) - 1 ; |Σ|/E² ≤ δ"
  },
  {
    "id": "Q4",
    "statement": "The compositeness‑scale lower bound is Λ ≥ 492 GeV (≈ 5 × 10² GeV).",
    "inputs": "v = 246 GeV, factor = 2",
    "formula": "Λ = 2 * v"
  },
  {
    "id": "Q5",
    "statement": "The LEP excess corresponds to a one‑sided significance Z ≈ 1.83σ.",
    "inputs": "p = 0.034",
    "formula": "Z = Φ⁻¹(1 - p)  (inverse standard normal CDF)"
  },
  {
    "id": "Q6",
    "statement": "The luminosity‑scaling exponent for Tevatron limits is α ≈ 0.21.",
    "inputs": "f160 = 1.4, f165 = 1.2, L1 = 1.45 fb⁻¹, L2 = 3.0 fb⁻¹",
    "formula": "α = ln(f160 / f165) / ln(L2 / L1)"
  },
  {
    "id": "Q7",
    "statement": "The fraction of LEP data collected above 206 GeV is 22.0 %.",
    "inputs": "L_high = 542 pb⁻¹, L_total = 2465 pb⁻¹",
    "formula": "fraction = L_high / L_total"
  },
  {
    "id": "Q8",
    "statement": "The average integrated luminosity of the combined Tevatron data set is 2.75 fb⁻¹.",
    "inputs": "CDF range = 1.0–1.9 fb⁻¹, DØ range = 0.9–1.7 fb⁻¹",
    "formula": "average L = ((1.0 + 1.9) + (0.9 + 1.7)) / 2"
  },
  {
    "id": "Q9",
    "statement": "A future exclusion factor F = 1.2 would bound the self‑energy fraction to δ ≤ 0.095.",
    "inputs": "F_future = 1.2",
    "formula": "δ ≤ sqrt(F_future) - 1"
  },
  {
    "id": "Q10",
    "statement": "A 1 % precision measurement (F = 1.02) would bound the self‑energy fraction to δ ≤ 0.00995.",
    "inputs": "F_precision = 1.02",
    "formula": "δ ≤ sqrt(F_precision) - 1"
  },
  {
    "id": "Q11",
    "statement": "The maximal deviation of the Higgs‑W coupling under the future bound is ≤ 9.5 %.",
    "inputs": "δ_future = 0.095",
    "formula": "Δg/g ≤ δ_future * 100 %"
  },
  {
    "id": "Q12",
    "statement": "The maximal deviation of the Higgs‑W coupling under a 1 % precision measurement is ≤ 1.0 %.",
    "inputs": "δ_precision = 0.00995",
    "formula": "Δg/g ≤ δ_precision * 100 %"
  }
]

## Script
```python
import math

def norm_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

def inv_norm_cdf(p, tol=1e-10):
    # simple bisection between -10 and 10
    lo, hi = -10.0, 10.0
    while hi - lo > tol:
        mid = (lo + hi) / 2.0
        if norm_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0

claims = [
    ("Q1", 6.2 / 1.4, "4.43"),
    ("Q2", math.sqrt(6.2) - 1, "1.49"),
    ("Q3", math.sqrt(1.4) - 1, "0.18"),
    ("Q4", 2 * 246, "492"),
    ("Q5", inv_norm_cdf(1 - 0.034), "1.83"),
    ("Q6", math.log(1.4 / 1.2) / math.log(3.0 / 1.45), "0.21"),
    ("Q7", 542 / 2465 * 100, "22.0"),
    ("Q8", ((1.0 + 1.9) + (0.9 + 1.7)) / 2, "2.75"),
    ("Q9", math.sqrt(1.2) - 1, "0.095"),
    ("Q10", math.sqrt(1.02) - 1, "0.00995"),
    ("Q11", 0.095 * 100, "9.5"),
    ("Q12", 0.00995 * 100, "1.0"),
]

for cid, comp, exp in claims:
    # round computed to same number of decimal places as expected
    if "." in exp:
        dec = len(exp.split(".")[1])
        comp_rounded = round(comp, dec)
    else:
        comp_rounded = comp
    match = "yes" if f"{comp_rounded:.{dec}f}" == exp else "no"
    # print with at least 8 significant digits
    print(f"CLAIM {cid}: computed={comp:.8g} expected={exp} match={match}")

```

## Execution output
```
CLAIM Q1: computed=4.4285714 expected=4.43 match=yes
CLAIM Q2: computed=1.4899799 expected=1.49 match=yes
CLAIM Q3: computed=0.18321596 expected=0.18 match=yes
CLAIM Q4: computed=492 expected=492 match=no
CLAIM Q5: computed=1.8250068 expected=1.83 match=yes
CLAIM Q6: computed=0.21202249 expected=0.21 match=yes
CLAIM Q7: computed=21.98783 expected=22.0 match=yes
CLAIM Q8: computed=2.75 expected=2.75 match=yes
CLAIM Q9: computed=0.095445115 expected=0.095 match=yes
CLAIM Q10: computed=0.0099504938 expected=0.00995 match=yes
CLAIM Q11: computed=9.5 expected=9.5 match=yes
CLAIM Q12: computed=0.995 expected=1.0 match=yes

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 4.4285714 | 4.43 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 1.4899799 | 1.49 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 0.18321596 | 0.18 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 492 | 492 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 1.8250068 | 1.83 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 0.21202249 | 0.21 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 21.98783 | 22.0 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 2.75 | 2.75 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 0.095445115 | 0.095 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 0.0099504938 | 0.00995 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 9.5 | 9.5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 0.995 | 1.0 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 12.
