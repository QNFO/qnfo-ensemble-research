# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The number of orientation bins is 720.",
    "inputs": "full circle = 360°, angular accuracy Δθ = 0.5°",
    "formula": "N_theta = 360 / Δθ"
  },
  {
    "id": "Q2",
    "statement": "The orientation information per sample is approximately 9.49 bits.",
    "inputs": "N_theta = 720",
    "formula": "I_theta = log2(N_theta)"
  },
  {
    "id": "Q3",
    "statement": "The number of position bins per dimension is 500.",
    "inputs": "workspace side L = 10 m, localization precision Δp = 0.02 m",
    "formula": "N_p = L / Δp"
  },
  {
    "id": "Q4",
    "statement": "The information per dimension for position is approximately 8.97 bits.",
    "inputs": "N_p = 500",
    "formula": "bits_per_dim = log2(N_p)"
  },
  {
    "id": "Q5",
    "statement": "The total position information per sample is approximately 26.91 bits.",
    "inputs": "bits per dimension = 8.97 bits",
    "formula": "I_p = 3 * log2(N_p)"
  },
  {
    "id": "Q6",
    "statement": "The raw per‑sample information budget is 36.40 bits.",
    "inputs": "I_theta = 9.49 bits, I_p = 26.91 bits",
    "formula": "I_raw = I_theta + I_p"
  },
  {
    "id": "Q7",
    "statement": "The effective bandwidth is set to 30 samples per second.",
    "inputs": "frame rate of VIGS‑SLAM = 30 Hz",
    "formula": "B = 30"
  },
  {
    "id": "Q8",
    "statement": "The raw signal‑to‑noise ratio is 36.40 (unit noise power assumed).",
    "inputs": "I_raw = 36.40, P_noise = 1",
    "formula": "SNR0 = I_raw / P_noise"
  },
  {
    "id": "Q9",
    "statement": "The channel capacity without filtering is approximately 156.6 bits s⁻¹.",
    "inputs": "B = 30, SNR0 = 36.40",
    "formula": "C1 = B * log2(1 + SNR0)"
  },
  {
    "id": "Q10",
    "statement": "With a 20 % reduction in filtering (α = 0.8), the filtered SNR is 23.30.",
    "inputs": "α = 0.8, SNR0 = 36.40",
    "formula": "SNR_α = α^2 * SNR0"
  },
  {
    "id": "Q11",
    "statement": "The channel capacity with α = 0.8 is approximately 138.0 bits s⁻¹.",
    "inputs": "B = 30, SNR_α = 23.30",
    "formula": "C0.8 = B * log2(1 + SNR_α)"
  },
  {
    "id": "Q12",
    "statement": "The capacity drop due to the 20 % reduction is 18.6 bits s⁻¹.",
    "inputs": "C1 = 156.6 bits s⁻¹, C0.8 = 138.0 bits s⁻¹",
    "formula": "ΔC = C1 - C0.8"
  },
  {
    "id": "Q13",
    "statement": "The per‑sample capacity change is 0.62 bits.",
    "inputs": "ΔC = 18.6 bits s⁻¹, B = 30 samples s⁻¹",
    "formula": "ΔC_per_sample = ΔC / B"
  },
  {
    "id": "Q14",
    "statement": "With a modest 10 % reduction (α = 0.9), the information budget is 29.48 bits.",
    "inputs": "α = 0.9, I_raw = 36.40",
    "formula": "I_0.9 = α^2 * I_raw"
  },
  {
    "id": "Q15",
    "statement": "With α = 0.8, the information budget is 23.30 bits.",
    "inputs": "α = 0.8, I_raw = 36.40",
    "formula": "I_0.8 = α^2 * I_raw"
  },
  {
    "id": "Q16",
    "statement": "The difference between the 10 % and 20 % reductions is 6.18 bits.",
    "inputs": "I_0.9 = 29.48 bits, I_0.8 = 23.30 bits",
    "formula": "ΔI = I_0.9 - I_0.8"
  }
]

## Script
```python
import math

def round_sig(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0.0
    else:
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Expected values and their formatting (decimal places)
expected = {
    "Q1": ("720", 0),
    "Q2": ("9.49", 2),
    "Q3": ("500", 0),
    "Q4": ("8.97", 2),
    "Q5": ("26.91", 2),
    "Q6": ("36.40", 2),
    "Q7": ("30", 0),
    "Q8": ("36.40", 2),
    "Q9": ("156.6", 1),
    "Q10": ("23.30", 2),
    "Q11": ("138.0", 1),
    "Q12": ("18.6", 1),
    "Q13": ("0.62", 2),
    "Q14": ("29.48", 2),
    "Q15": ("23.30", 2),
    "Q16": ("6.18", 2),
}

# 1. Orientation bins
N_theta = 360 / 0.5  # Q1
# 2. Orientation info
I_theta = math.log2(N_theta)  # Q2
# 3. Position bins per dimension
L = 10.0
delta_p = 0.02
N_p = L / delta_p  # Q3
# 4. Bits per dimension
bits_per_dim = math.log2(N_p)  # Q4
# 5. Total position info
I_p = 3 * bits_per_dim  # Q5
# 6. Raw per-sample info
I_raw = I_theta + I_p  # Q6
# 7. Bandwidth
B = 30  # Q7
# 8. Raw SNR (noise power = 1)
SNR0 = I_raw / 1.0  # Q8
# 9. Capacity without filtering
C1 = B * math.log2(1 + SNR0)  # Q9
# 10. Filtered SNR with alpha=0.8
alpha = 0.8
SNR_alpha = alpha**2 * SNR0  # Q10
# 11. Capacity with alpha=0.8
C0_8 = B * math.log2(1 + SNR_alpha)  # Q11
# 12. Capacity drop
delta_C = C1 - C0_8  # Q12
# 13. Per-sample capacity change
delta_C_per_sample = delta_C / B  # Q13
# 14. Information budget with alpha=0.9
I_09 = 0.9**2 * I_raw  # Q14
# 15. Information budget with alpha=0.8
I_08 = 0.8**2 * I_raw  # Q15
# 16. Difference between the two budgets
delta_I = I_09 - I_08  # Q16

# Mapping of computed values to claim IDs
computed = {
    "Q1": N_theta,
    "Q2": I_theta,
    "Q3": N_p,
    "Q4": bits_per_dim,
    "Q5": I_p,
    "Q6": I_raw,
    "Q7": B,
    "Q8": SNR0,
    "Q9": C1,
    "Q10": SNR_alpha,
    "Q11": C0_8,
    "Q12": delta_C,
    "Q13": delta_C_per_sample,
    "Q14": I_09,
    "Q15": I_08,
    "Q16": delta_I,
}

# Helper to format rounded value with required decimal places
def fmt(val, dec):
    fmt_str = f"{{:.{dec}f}}"
    return fmt_str.format(val)

# Verification loop
for qid in sorted(expected.keys(), key=lambda x: int(x[1:])):  # Q1, Q2, ...
    exp_str, dec = expected[qid]
    # Determine sig figs from expected string (ignoring leading zeros and decimal point)
    # For simplicity we use the decimal places already stored.
    comp_raw = computed[qid]
    # Round to the same number of significant figures as the expected value
    # Count significant figures: digits excluding leading zeros and decimal point.
    # Here we approximate by rounding to the same number of decimal places.
    comp_rounded = round(comp_raw, dec)
    comp_str = fmt(comp_rounded, dec)
    match = "yes" if comp_str == exp_str else "no"
    print(f"CLAIM {qid}: computed={comp_str} expected={exp_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if fmt(round(computed[q], expected[q][1]), expected[q][1]) == expected[q][0])} match, {len(expected) - sum(1 for q in expected if fmt(round(computed[q], expected[q][1]), expected[q][1]) == expected[q][0])} mismatch")

```

## Execution output
```
CLAIM Q1: computed=720 expected=720 match=yes
CLAIM Q2: computed=9.49 expected=9.49 match=yes
CLAIM Q3: computed=500 expected=500 match=yes
CLAIM Q4: computed=8.97 expected=8.97 match=yes
CLAIM Q5: computed=26.90 expected=26.91 match=no
CLAIM Q6: computed=36.39 expected=36.40 match=no
CLAIM Q7: computed=30 expected=30 match=yes
CLAIM Q8: computed=36.39 expected=36.40 match=no
CLAIM Q9: computed=156.7 expected=156.6 match=no
CLAIM Q10: computed=23.29 expected=23.30 match=no
CLAIM Q11: computed=138.1 expected=138.0 match=no
CLAIM Q12: computed=18.7 expected=18.6 match=no
CLAIM Q13: computed=0.62 expected=0.62 match=yes
CLAIM Q14: computed=29.48 expected=29.48 match=yes
CLAIM Q15: computed=23.29 expected=23.30 match=no
CLAIM Q16: computed=6.19 expected=6.18 match=no
VERIFICATION SUMMARY: 16 claims, 7 match, 9 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 720 | 720 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 9.49 | 9.49 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q3 | 500 | 500 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 8.97 | 8.97 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 26.90 | 26.91 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 36.39 | 36.40 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 30 | 30 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 36.39 | 36.40 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 156.7 | 156.6 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 23.29 | 23.30 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q11 | 138.1 | 138.0 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q12 | 18.7 | 18.6 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 0.62 | 0.62 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 29.48 | 29.48 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q15 | 23.29 | 23.30 | no | match | 4 significant digits (as the paper states, at least 2) |
| Q16 | 6.19 | 6.18 | no | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
