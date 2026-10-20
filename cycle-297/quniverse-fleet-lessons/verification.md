# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Effective unresolved‑failure probability $p_{\\text{eff}} = 0.06$.",
    "inputs": "p_f=0.12, alpha=0.5",
    "formula": "p_eff = p_f * (1 - alpha)"
  },
  {
    "id": "Q2",
    "statement": "Expected monthly unresolved failures $E[F] = 2.16$.",
    "inputs": "N_w=36, p_f=0.12, alpha=0.5",
    "formula": "E[F] = N_w * p_f * (1 - alpha)"
  },
  {
    "id": "Q3",
    "statement": "Count‑derived mitigation factor $\\alpha_{\\text{counts}} \\approx 0.599$.",
    "inputs": "H=1889, X=1264",
    "formula": "alpha_counts = H / (H + X)"
  },
  {
    "id": "Q4",
    "statement": "Effective failure probability using $\\alpha_{\\text{counts}}$ is $p_{\\text{eff}}^{\\text{counts}} = 0.04812$.",
    "inputs": "p_f=0.12, alpha_counts=0.599",
    "formula": "p_eff_counts = p_f * (1 - alpha_counts)"
  },
  {
    "id": "Q5",
    "statement": "Expected failures using $\\alpha_{\\text{counts}}$ is $E[F]^{\\text{counts}} \\approx 1.73$.",
    "inputs": "N_w=36, p_eff_counts=0.04812",
    "formula": "E[F]_counts = N_w * p_eff_counts"
  },
  {
    "id": "Q6",
    "statement": "Variance of the failure count $\\operatorname{Var}[F] = 2.0304$.",
    "inputs": "N_w=36, p_eff=0.06",
    "formula": "Var[F] = N_w * p_eff * (1 - p_eff)"
  },
  {
    "id": "Q7",
    "statement": "Standard deviation $\\sigma_F \\approx 1.425$.",
    "inputs": "Var[F]=2.0304",
    "formula": "sigma_F = sqrt(Var[F])"
  },
  {
    "id": "Q8",
    "statement": "Papers per active project $= 9.65$.",
    "inputs": "P_total=917, N_proj=95",
    "formula": "P_total / N_proj"
  },
  {
    "id": "Q9",
    "statement": "High‑severity gap proportion $= 11.9\\%$.",
    "inputs": "G_high=5, G_total=42",
    "formula": "(G_high / G_total) * 100"
  },
  {
    "id": "Q10",
    "statement": "Vector‑index size $S_{vi} \\approx 16.922\\ \\text{MiB}$.",
    "inputs": "rows=34657, bytes_per_row=512, 1\\ MiB=1048576\\ B",
    "formula": "rows * bytes_per_row / 1048576"
  },
  {
    "id": "Q11",
    "statement": "Total storage $S_{\\text{tot}} \\approx 320.9\\ \\text{MB}$.",
    "inputs": "S_db=304\\ MB, S_vi=16.922\\ MB (interchangeable)",
    "formula": "S_db + S_vi"
  },
  {
    "id": "Q12",
    "statement": "Baseline composite autonomy score $C_{\\text{base}} = 4.26$.",
    "inputs": "w_c=0.4, w_{sh}=0.3, w_{oc}=0.3, S_c=4.5, S_{sh}=4.0, S_{oc}=4.2",
    "formula": "C_base = w_c*S_c + w_{sh}*S_{sh} + w_{oc}*S_{oc}"
  },
  {
    "id": "Q13",
    "statement": "Improved composite autonomy score $C_{\\text{new}} = 4.66$.",
    "inputs": "w_c=0.4, w_{sh}=0.3, w_{oc}=0.3, S_c'=4.9, S_{sh}'=4.4, S_{oc}'=4.6",
    "formula": "C_new = w_c*S_c' + w_{sh}*S_{sh}' + w_{oc}*S_{oc}'"
  },
  {
    "id": "Q14",
    "statement": "Score increment $= 0.40$.",
    "inputs": "C_new=4.66, C_base=4.26",
    "formula": "C_new - C_base"
  },
  {
    "id": "Q15",
    "statement": "Baseline extra cost $= \\$10.8$.",
    "inputs": "E[F]=2.16, c_f=5\\ \\text{USD}",
    "formula": "E[F] * c_f"
  },
  {
    "id": "Q16",
    "statement": "Projected baseline spend $= \\$160.8$.",
    "inputs": "cap=150\\ USD, extra_cost=10.8\\ USD",
    "formula": "cap + extra_cost"
  }
]

## Script
```python
import math

def fmt(val, digits):
    """Format a float with a given number of decimal places, removing trailing zeros."""
    fmt_str = f"{{:.{digits}f}}".format(val)
    # Remove trailing zeros and possible trailing decimal point
    if '.' in fmt_str:
        fmt_str = fmt_str.rstrip('0').rstrip('.')
    return fmt_str

# Claims definitions with inputs and expected values
claims = [
    {
        "id": "Q1",
        "statement": "Effective unresolved‑failure probability $p_{\\text{eff}} = 0.06$.",
        "compute": lambda: 0.12 * (1 - 0.5),
        "expected": "0.06",
        "digits": 2
    },
    {
        "id": "Q2",
        "statement": "Expected monthly unresolved failures $E[F] = 2.16$.",
        "compute": lambda: 36 * 0.12 * (1 - 0.5),
        "expected": "2.16",
        "digits": 2
    },
    {
        "id": "Q3",
        "statement": "Count‑derived mitigation factor $\\alpha_{\\text{counts}} \\approx 0.599$.",
        "compute": lambda: 1889 / (1889 + 1264),
        "expected": "0.599",
        "digits": 3
    },
    {
        "id": "Q4",
        "statement": "Effective failure probability using $\\alpha_{\\text{counts}}$ is $p_{\\text{eff}}^{\\text{counts}} = 0.04812$.",
        "compute": lambda: 0.12 * (1 - (1889 / (1889 + 1264))),
        "expected": "0.04812",
        "digits": 5
    },
    {
        "id": "Q5",
        "statement": "Expected failures using $\\alpha_{\\text{counts}}$ is $E[F]^{\\text{counts}} \\approx 1.73$.",
        "compute": lambda: 36 * (0.12 * (1 - (1889 / (1889 + 1264)))),
        "expected": "1.73",
        "digits": 2
    },
    {
        "id": "Q6",
        "statement": "Variance of the failure count $\\operatorname{Var}[F] = 2.0304$.",
        "compute": lambda: 36 * 0.06 * (1 - 0.06),
        "expected": "2.0304",
        "digits": 4
    },
    {
        "id": "Q7",
        "statement": "Standard deviation $\\sigma_F \\approx 1.425$.",
        "compute": lambda: math.sqrt(36 * 0.06 * (1 - 0.06)),
        "expected": "1.425",
        "digits": 3
    },
    {
        "id": "Q8",
        "statement": "Papers per active project $= 9.65$.",
        "compute": lambda: 917 / 95,
        "expected": "9.65",
        "digits": 2
    },
    {
        "id": "Q9",
        "statement": "High‑severity gap proportion $= 11.9\\%$.",
        "compute": lambda: (5 / 42) * 100,
        "expected": "11.9",
        "digits": 1
    },
    {
        "id": "Q10",
        "statement": "Vector‑index size $S_{vi} \\approx 16.922\\ \\text{MiB}$.",
        "compute": lambda: (34657 * 512) / 1048576,
        "expected": "16.922",
        "digits": 3
    },
    {
        "id": "Q11",
        "statement": "Total storage $S_{\\text{tot}} \\approx 320.9\\ \\text{MB}$.",
        "compute": lambda: 304 + ((34657 * 512) / 1048576),
        "expected": "320.9",
        "digits": 1
    },
    {
        "id": "Q12",
        "statement": "Baseline composite autonomy score $C_{\\text{base}} = 4.26$.",
        "compute": lambda: 0.4*4.5 + 0.3*4.0 + 0.3*4.2,
        "expected": "4.26",
        "digits": 2
    },
    {
        "id": "Q13",
        "statement": "Improved composite autonomy score $C_{\\text{new}} = 4.66$.",
        "compute": lambda: 0.4*4.9 + 0.3*4.4 + 0.3*4.6,
        "expected": "4.66",
        "digits": 2
    },
    {
        "id": "Q14",
        "statement": "Score increment $= 0.40$.",
        "compute": lambda: (0.4*4.9 + 0.3*4.4 + 0.3*4.6) - (0.4*4.5 + 0.3*4.0 + 0.3*4.2),
        "expected": "0.40",
        "digits": 2
    },
    {
        "id": "Q15",
        "statement": "Baseline extra cost $= \\$10.8$.",
        "compute": lambda: 2.16 * 5,
        "expected": "10.8",
        "digits": 1
    },
    {
        "id": "Q16",
        "statement": "Projected baseline spend $= \\$160.8$.",
        "compute": lambda: 150 + (2.16 * 5),
        "expected": "160.8",
        "digits": 1
    }
]

for c in claims:
    computed = c["compute"]()
    # Round/format to the required number of significant digits as per expected string
    formatted = fmt(computed, c["digits"])
    match = "yes" if formatted == c["expected"] else "no"
    print(f"CLAIM {c['id']}: computed={formatted} expected={c['expected']} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for c in claims if fmt(c['compute'](), c['digits']) == c['expected'])} match, {sum(1 for c in claims if fmt(c['compute'](), c['digits']) != c['expected'])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.06 expected=0.06 match=yes
CLAIM Q2: computed=2.16 expected=2.16 match=yes
CLAIM Q3: computed=0.599 expected=0.599 match=yes
CLAIM Q4: computed=0.04811 expected=0.04812 match=no
CLAIM Q5: computed=1.73 expected=1.73 match=yes
CLAIM Q6: computed=2.0304 expected=2.0304 match=yes
CLAIM Q7: computed=1.425 expected=1.425 match=yes
CLAIM Q8: computed=9.65 expected=9.65 match=yes
CLAIM Q9: computed=11.9 expected=11.9 match=yes
CLAIM Q10: computed=16.922 expected=16.922 match=yes
CLAIM Q11: computed=320.9 expected=320.9 match=yes
CLAIM Q12: computed=4.26 expected=4.26 match=yes
CLAIM Q13: computed=4.66 expected=4.66 match=yes
CLAIM Q14: computed=0.4 expected=0.40 match=no
CLAIM Q15: computed=10.8 expected=10.8 match=yes
CLAIM Q16: computed=160.8 expected=160.8 match=yes
VERIFICATION SUMMARY: 16 claims, 14 match, 2 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.06 | 0.06 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 2.16 | 2.16 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 0.599 | 0.599 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.04811 | 0.04812 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 1.73 | 1.73 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 2.0304 | 2.0304 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 1.425 | 1.425 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 9.65 | 9.65 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 11.9 | 11.9 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 16.922 | 16.922 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q11 | 320.9 | 320.9 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 4.26 | 4.26 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 4.66 | 4.66 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 0.4 | 0.40 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 10.8 | 10.8 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 160.8 | 160.8 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
