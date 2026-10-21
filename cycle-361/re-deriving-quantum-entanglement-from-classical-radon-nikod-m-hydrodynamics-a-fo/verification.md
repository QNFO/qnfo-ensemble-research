# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Mermin violation factor equals 2.",
    "inputs": "classical bound M_LHV = 2, quantum value M_Q = 4",
    "formula": "violation factor = M_Q / M_LHV"
  },
  {
    "id": "Q2",
    "statement": "CHSH violation factor equals sqrt(2) ≈ 1.414214.",
    "inputs": "classical bound = 2, quantum maximum = 2*sqrt(2)",
    "formula": "violation factor = (2*sqrt(2)) / 2"
  },
  {
    "id": "Q3",
    "statement": "Required simulation timestep for barrier width L = 1.0×10^{-3} m is ≤ 3.333333×10^{-13} s (≈ 333 fs).",
    "inputs": "maximum signal speed v_max = 3.0×10^8 m/s, barrier width L = 1.0×10^{-3} m, timestep rule Δt = t_min / 10",
    "formula": "t_min = L / v_max; Δt = t_min / 10"
  },
  {
    "id": "Q4",
    "statement": "Minimum propagation time for barrier width L = 1.0×10^{-3} m is 3.333333×10^{-12} s (≈ 3.33 ps).",
    "inputs": "maximum signal speed v_max = 3.0×10^8 m/s, barrier width L = 1.0×10^{-3} m",
    "formula": "t_min = L / v_max"
  },
  {
    "id": "Q5",
    "statement": "Number of timesteps required for one crossing at L = 1.0×10^{-3} m is 10.",
    "inputs": "minimum propagation time t_min = 3.333333×10^{-12} s, timestep Δt = 3.333333×10^{-13} s",
    "formula": "N_steps = t_min / Δt"
  },
  {
    "id": "Q6",
    "statement": "Minimum propagation time for barrier width L = 1.0 m is 3.333333×10^{-9} s (≈ 3.33 ns).",
    "inputs": "maximum signal speed v_max = 3.0×10^8 m/s, barrier width L = 1.0 m",
    "formula": "t_min = L / v_max"
  },
  {
    "id": "Q7",
    "statement": "Required simulation timestep for barrier width L = 1.0 m is ≤ 3.333333×10^{-10} s (≈ 333 ps).",
    "inputs": "minimum propagation time t_min = 3.333333×10^{-9} s, timestep rule Δt = t_min / 10",
    "formula": "Δt = t_min / 10"
  },
  {
    "id": "Q8",
    "statement": "Number of timesteps required for one crossing at L = 1.0 m under the primary convention is 10.",
    "inputs": "minimum propagation time t_min = 3.333333×10^{-9} s, timestep Δt = 3.333333×10^{-10} s",
    "formula": "N_steps = t_min / Δt"
  },
  {
    "id": "Q9",
    "statement": "Under the fixed‑timestep alternative for L = 1.0 m, the number of timesteps is approximately 1.0×10^4.",
    "inputs": "minimum propagation time t_min = 3.333333×10^{-9} s, fixed timestep Δt_fixed = 3.333333×10^{-13} s",
    "formula": "N_steps = t_min / Δt_fixed"
  }
]

## Script
```python
import math

def fmt(val, sig_digits):
    """Format val to the given number of significant digits."""
    if val == 0:
        return "0"
    # Determine order of magnitude
    order = int(math.floor(math.log10(abs(val))))
    digits = sig_digits - 1 - order
    if digits > 0:
        fmt_str = "{:." + str(digits) + "f}"
    else:
        fmt_str = "{:." + "0" + "f}"
    return fmt_str.format(round(val, digits))

claims = [
    {
        "id": "Q1",
        "computed": 4 / 2,
        "expected": "2",
        "sig": 1,
    },
    {
        "id": "Q2",
        "computed": (2 * math.sqrt(2)) / 2,
        "expected": "1.414214",
        "sig": 7,  # 1 digit before decimal + 6 after = 7 significant
    },
    {
        "id": "Q3",
        "computed": (1.0e-3) / (3.0e8) / 10,
        "expected": "3.333333e-13",
        "sig": 7,
    },
    {
        "id": "Q4",
        "computed": (1.0e-3) / (3.0e8),
        "expected": "3.333333e-12",
        "sig": 7,
    },
    {
        "id": "Q5",
        "computed": ((1.0e-3) / (3.0e8)) / ((1.0e-3) / (3.0e8) / 10),
        "expected": "10",
        "sig": 2,
    },
    {
        "id": "Q6",
        "computed": (1.0) / (3.0e8),
        "expected": "3.333333e-9",
        "sig": 7,
    },
    {
        "id": "Q7",
        "computed": ((1.0) / (3.0e8)) / 10,
        "expected": "3.333333e-10",
        "sig": 7,
    },
    {
        "id": "Q8",
        "computed": ((1.0) / (3.0e8)) / ((1.0) / (3.0e8) / 10),
        "expected": "10",
        "sig": 2,
    },
    {
        "id": "Q9",
        "computed": ((1.0) / (3.0e8)) / (3.333333e-13),
        "expected": "1.0e4",
        "sig": 2,
    },
]

for c in claims:
    comp = c["computed"]
    exp = float(c["expected"])
    # Determine match by rounding to the number of significant digits of expected
    comp_rounded = float(fmt(comp, c["sig"]))
    match = "yes" if abs(comp_rounded - exp) < 1e-12 * max(1.0, abs(exp)) else "no"
    # Print with full precision for computed value
    print(f"CLAIM {c['id']}: computed={comp:.12g} expected={c['expected']} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for c in claims if abs(float(fmt(c['computed'], c['sig'])) - float(c['expected'])) < 1e-12 * max(1.0, float(c['expected']))) } match, {len(claims) - sum(1 for c in claims if abs(float(fmt(c['computed'], c['sig'])) - float(c['expected'])) < 1e-12 * max(1.0, float(c['expected']))) } mismatch")

```

## Execution output
```
CLAIM Q1: computed=2 expected=2 match=yes
CLAIM Q2: computed=1.41421356237 expected=1.414214 match=yes
CLAIM Q3: computed=3.33333333333e-13 expected=3.333333e-13 match=yes
CLAIM Q4: computed=3.33333333333e-12 expected=3.333333e-12 match=yes
CLAIM Q5: computed=10 expected=10 match=yes
CLAIM Q6: computed=3.33333333333e-09 expected=3.333333e-9 match=yes
CLAIM Q7: computed=3.33333333333e-10 expected=3.333333e-10 match=yes
CLAIM Q8: computed=10 expected=10 match=yes
CLAIM Q9: computed=10000.001 expected=1.0e4 match=yes
VERIFICATION SUMMARY: 9 claims, 9 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2 | 2 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 1.41421356237 | 1.414214 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q3 | 3.33333333333e-13 | 3.333333e-13 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q4 | 3.33333333333e-12 | 3.333333e-12 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q5 | 10 | 10 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 3.33333333333e-09 | 3.333333e-9 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q7 | 3.33333333333e-10 | 3.333333e-10 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q8 | 10 | 10 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 10000.001 | 1.0e4 | yes | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 9.
