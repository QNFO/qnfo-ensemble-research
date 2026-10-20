# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Continuous operation provides 8760 hours per year.",
    "inputs": "24 hours per day, 365 days per year",
    "formula": "24 * 365"
  },
  {
    "id": "Q2",
    "statement": "A five‑year warranty corresponds to 43800 hours.",
    "inputs": "5 years, 8760 hours per year",
    "formula": "5 * 8760"
  },
  {
    "id": "Q3",
    "statement": "The maximum warranty‑margin factor is 2.44×.",
    "inputs": "Maximum HBF lifetime 12.2 years, warranty period 5 years",
    "formula": "12.2 / 5"
  },
  {
    "id": "Q4",
    "statement": "The minimum warranty‑margin factor is 0.66×.",
    "inputs": "Minimum HBF lifetime 3.3 years, warranty period 5 years",
    "formula": "3.3 / 5"
  },
  {
    "id": "Q5",
    "statement": "The implied HBM‑first baseline lifetime at the low endpoint is approximately 1.05 device‑years.",
    "inputs": "Low HBF lifetime 3.3 years, high extension factor 3.13",
    "formula": "3.3 / 3.13"
  },
  {
    "id": "Q6",
    "statement": "The implied HBM‑first baseline lifetime at the high endpoint is approximately 10.25 device‑years.",
    "inputs": "High HBF lifetime 12.2 years, low extension factor 1.19",
    "formula": "12.2 / 1.19"
  },
  {
    "id": "Q7",
    "statement": "The geometric‑mean extension factor is about 1.93×.",
    "inputs": "Extension factors 1.19 and 3.13",
    "formula": "sqrt(1.19 * 3.13)"
  },
  {
    "id": "Q8",
    "statement": "For an extension factor f = 1.19, the write‑diversion fraction is 15.97 %.",
    "inputs": "f = 1.19",
    "formula": "1 - 1/1.19"
  },
  {
    "id": "Q9",
    "statement": "For an extension factor f = 3.13, the write‑diversion fraction is 68.05 %.",
    "inputs": "f = 3.13",
    "formula": "1 - 1/3.13"
  },
  {
    "id": "Q10",
    "statement": "With a HBF endurance rating of 10⁵ cycles and a lifetime of 12.2 years, the annual per‑cell write budget is about 8.20×10³ writes per year.",
    "inputs": "Endurance E = 10^5 cycles, lifetime T = 12.2 years",
    "formula": "10^5 / 12.2"
  },
  {
    "id": "Q11",
    "statement": "The corresponding write rate is approximately 0.936 writes per hour.",
    "inputs": "Annual writes 8196.72 writes/year, hours per year 8760",
    "formula": "8196.72 / 8760"
  },
  {
    "id": "Q12",
    "statement": "With a HBF endurance rating of 10⁵ cycles and a lifetime of 3.3 years, the annual per‑cell write budget is about 3.03×10⁴ writes per year.",
    "inputs": "Endurance E = 10^5 cycles, lifetime T = 3.3 years",
    "formula": "10^5 / 3.3"
  },
  {
    "id": "Q13",
    "statement": "The corresponding write rate is approximately 3.46 writes per hour.",
    "inputs": "Annual writes 30303.03 writes/year, hours per year 8760",
    "formula": "30303.03 / 8760"
  }
]

## Script
```python
import math

def fmt_sig(value, sig_digits):
    """Return a string with the given number of significant digits."""
    if value == 0:
        return "0"
    # Determine order of magnitude
    order = int(math.floor(math.log10(abs(value))))
    # Scale to get the desired sig digits
    scale = 10 ** (sig_digits - 1 - order)
    rounded = round(value * scale) / scale
    # Use plain decimal representation
    fmt_str = f"{{:.{max(sig_digits - order - 1, 0)}f}}".format(rounded)
    # Strip trailing zeros and possible trailing dot
    return fmt_str.rstrip('0').rstrip('.') if '.' in fmt_str else fmt_str

def fmt_scientific(value, mantissa_digits):
    """Return a string like 8.20e3 with the given mantissa digits."""
    if value == 0:
        return "0e0"
    exponent = int(math.floor(math.log10(abs(value))))
    mantissa = value / (10 ** exponent)
    mantissa_str = f"{mantissa:.{mantissa_digits}f}"
    # Strip trailing zeros
    mantissa_str = mantissa_str.rstrip('0').rstrip('.')
    return f"{mantissa_str}e{exponent}"

# Claim computations
claims = [
    # Q1
    ("Q1", 24 * 365, "8760"),
    # Q2
    ("Q2", 5 * 8760, "43800"),
    # Q3
    ("Q3", 12.2 / 5, "2.44"),
    # Q4
    ("Q4", 3.3 / 5, "0.66"),
    # Q5
    ("Q5", 3.3 / 3.13, "1.05"),
    # Q6
    ("Q6", 12.2 / 1.19, "10.25"),
    # Q7
    ("Q7", math.sqrt(1.19 * 3.13), "1.93"),
    # Q8
    ("Q8", 1 - 1 / 1.19, "15.97"),
    # Q9
    ("Q9", 1 - 1 / 3.13, "68.05"),
    # Q10
    ("Q10", 1e5 / 12.2, "8.20e3"),
    # Q11
    ("Q11", 8196.72 / 8760, "0.936"),
    # Q12
    ("Q12", 1e5 / 3.3, "3.03e4"),
    # Q13
    ("Q13", 30303.03 / 8760, "3.46"),
]

for cid, computed, expected in claims:
    # Determine formatting for comparison
    # For percentages we keep the raw fraction and compare after scaling
    if cid in ("Q8", "Q9"):
        # Convert to percent for display
        computed_display = fmt_sig(computed * 100, 4)  # e.g., 15.97
    elif cid in ("Q10", "Q12"):
        # Scientific notation with two mantissa digits
        computed_display = fmt_scientific(computed, 2)
    else:
        # Use appropriate significant digits based on expected string length
        # Count digits before decimal to decide sig digits
        if "." in expected:
            int_part, frac_part = expected.split(".")
            sig = len(int_part) + len(frac_part)
        else:
            sig = len(expected)
        computed_display = fmt_sig(computed, sig)

    match = "yes" if computed_display == expected else "no"
    print(f"CLAIM {cid}: computed={computed_display} expected={expected} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,c,e in claims if (fmt_sig(c, len(e)) if not (c in (8196.72/8760,30303.03/8760)) else fmt_sig(c*100,4)) == e) } match, {len(claims) - sum(1 for _,c,e in claims if (fmt_sig(c, len(e)) if not (c in (8196.72/8760,30303.03/8760)) else fmt_sig(c*100,4)) == e)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=8760 expected=8760 match=yes
CLAIM Q2: computed=43800 expected=43800 match=yes
CLAIM Q3: computed=2.44 expected=2.44 match=yes
CLAIM Q4: computed=0.66 expected=0.66 match=yes
CLAIM Q5: computed=1.05 expected=1.05 match=yes
CLAIM Q6: computed=10.25 expected=10.25 match=yes
CLAIM Q7: computed=1.93 expected=1.93 match=yes
CLAIM Q8: computed=15.97 expected=15.97 match=yes
CLAIM Q9: computed=68.05 expected=68.05 match=yes
CLAIM Q10: computed=8.2e3 expected=8.20e3 match=no
CLAIM Q11: computed=0.9357 expected=0.936 match=no
CLAIM Q12: computed=3.03e4 expected=3.03e4 match=yes
CLAIM Q13: computed=3.46 expected=3.46 match=yes
VERIFICATION SUMMARY: 13 claims, 5 match, 8 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 8760 | 8760 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 43800 | 43800 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q3 | 2.44 | 2.44 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.66 | 0.66 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 1.05 | 1.05 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 10.25 | 10.25 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 1.93 | 1.93 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 15.97 | 15.97 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q9 | 68.05 | 68.05 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 8.2e3 | 8.20e3 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 0.9357 | 0.936 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 3.03e4 | 3.03e4 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 3.46 | 3.46 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 13.
