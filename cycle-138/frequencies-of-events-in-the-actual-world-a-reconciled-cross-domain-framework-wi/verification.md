# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Radix-locked angular frequency omega_2 = 9.064722",
    "inputs": "2*pi = 6.283185; ln 2 = 0.693147",
    "formula": "omega_2 = 6.283185 / 0.693147"
  },
  {
    "id": "Q2",
    "statement": "Radix-locked angular frequency omega_3 = 5.719203",
    "inputs": "2*pi = 6.283185; ln 3 = 1.098612",
    "formula": "omega_3 = 6.283185 / 1.098612"
  },
  {
    "id": "Q3",
    "statement": "Radix-locked angular frequency omega_5 = 3.903962",
    "inputs": "2*pi = 6.283185; ln 5 = 1.609438",
    "formula": "omega_5 = 6.283185 / 1.609438"
  },
  {
    "id": "Q4",
    "statement": "Radix-locked angular frequency omega_7 = 3.228919",
    "inputs": "2*pi = 6.283185; ln 7 = 1.945910",
    "formula": "omega_7 = 6.283185 / 1.945910"
  },
  {
    "id": "Q5",
    "statement": "Ratio omega_2/omega_3 = log_2 3 = 1.584962",
    "inputs": "ln 3 = 1.098612; ln 2 = 0.693147",
    "formula": "1.098612 / 0.693147"
  },
  {
    "id": "Q6",
    "statement": "Ratio omega_2/omega_5 = log_2 5 = 2.321929",
    "inputs": "ln 5 = 1.609438; ln 2 = 0.693147",
    "formula": "1.609438 / 0.693147"
  },
  {
    "id": "Q7",
    "statement": "Ratio omega_3/omega_5 = log_3 5 = 1.464974",
    "inputs": "ln 5 = 1.609438; ln 3 = 1.098612",
    "formula": "1.609438 / 1.098612"
  },
  {
    "id": "Q8",
    "statement": "Arithmetic mean of omega_p = 5.479201",
    "inputs": "omega_2 = 9.064722; omega_3 = 5.719203; omega_5 = 3.903962; omega_7 = 3.228919",
    "formula": "(9.064722 + 5.719203 + 3.903962 + 3.228919) / 4"
  },
  {
    "id": "Q9",
    "statement": "Angular frequency Omega_1 = 6.157521e8 rad/s for 98 MHz",
    "inputs": "2*pi = 6.283185; f = 98 MHz = 98e6 Hz",
    "formula": "6.283185 * 98 * 10^6"
  },
  {
    "id": "Q10",
    "statement": "Angular frequency Omega_2 = 7.539822e8 rad/s for 120 MHz",
    "inputs": "2*pi = 6.283185; f = 120 MHz = 120e6 Hz",
    "formula": "6.283185 * 120 * 10^6"
  },
  {
    "id": "Q11",
    "statement": "Angular frequency Omega_3 = 8.293804e8 rad/s for 132 MHz",
    "inputs": "2*pi = 6.283185; f = 132 MHz = 132e6 Hz",
    "formula": "6.283185 * 132 * 10^6"
  },
  {
    "id": "Q12",
    "statement": "Angular frequency Omega_4 = 1.005310e9 rad/s for 160 MHz",
    "inputs": "2*pi = 6.283185; f = 160 MHz = 160e6 Hz",
    "formula": "6.283185 * 160 * 10^6"
  },
  {
    "id": "Q13",
    "statement": "Mean angular frequency Omega_mean = 8.011061e8 rad/s",
    "inputs": "Omega_1 = 6.157521e8; Omega_2 = 7.539822e8; Omega_3 = 8.293804e8; Omega_4 = 10.053096e8",
    "formula": "(6.157521 + 7.539822 + 8.293804 + 10.053096) * 10^8 / 4"
  },
  {
    "id": "Q14",
    "statement": "Consecutive log-spacing Delta_1 = 0.202525",
    "inputs": "ln 120 = 4.787492; ln 98 = 4.584967",
    "formula": "4.787492 - 4.584967"
  },
  {
    "id": "Q15",
    "statement": "Consecutive log-spacing Delta_2 = 0.095310",
    "inputs": "ln 132 = 4.882802; ln 120 = 4.787492",
    "formula": "4.882802 - 4.787492"
  },
  {
    "id": "Q16",
    "statement": "Consecutive log-spacing Delta_3 = 0.192372",
    "inputs": "ln 160 = 5.075174; ln 132 = 4.882802",
    "formula": "5.075174 - 4.882802"
  }
]

## Script
```python
import math
from fractions import Fraction

def sig(x, n=6):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

def fmt(x):
    # at least 8 significant digits
    return f"{x:.8g}"

claims = []

# Q1: omega_2 = 6.283185 / 0.693147
c = 6.283185 / 0.693147
claims.append(("Q1", c, "9.064722"))

# Q2: omega_3 = 6.283185 / 1.098612
c = 6.283185 / 1.098612
claims.append(("Q2", c, "5.719203"))

# Q3: omega_5 = 6.283185 / 1.609438
c = 6.283185 / 1.609438
claims.append(("Q3", c, "3.903962"))

# Q4: omega_7 = 6.283185 / 1.945910
c = 6.283185 / 1.945910
claims.append(("Q4", c, "3.228919"))

# Q5: ratio omega_2/omega_3 = ln3/ln2 = 1.098612 / 0.693147
c = 1.098612 / 0.693147
claims.append(("Q5", c, "1.584962"))

# Q6: ratio omega_2/omega_5 = ln5/ln2 = 1.609438 / 0.693147
c = 1.609438 / 0.693147
claims.append(("Q6", c, "2.321929"))

# Q7: ratio omega_3/omega_5 = ln5/ln3 = 1.609438 / 1.098612
c = 1.609438 / 1.098612
claims.append(("Q7", c, "1.464974"))

# Q8: mean of omega_p = (9.064722 + 5.719203 + 3.903962 + 3.228919) / 4
c = (9.064722 + 5.719203 + 3.903962 + 3.228919) / 4
claims.append(("Q8", c, "5.479201"))

# Q9: Omega_1 = 6.283185 * 98 * 10^6
c = 6.283185 * 98 * 10**6
claims.append(("Q9", c, "615752100"))

# Q10: Omega_2 = 6.283185 * 120 * 10^6
c = 6.283185 * 120 * 10**6
claims.append(("Q10", c, "753982200"))

# Q11: Omega_3 = 6.283185 * 132 * 10^6
c = 6.283185 * 132 * 10**6
claims.append(("Q11", c, "829380420"))

# Q12: Omega_4 = 6.283185 * 160 * 10^6
c = 6.283185 * 160 * 10**6
claims.append(("Q12", c, "1005309600"))

# Q13: mean Omega = (6.157521 + 7.539822 + 8.293804 + 10.053096) * 10^8 / 4
c = (6.157521 + 7.539822 + 8.293804 + 10.053096) * 10**8 / 4
claims.append(("Q13", c, "801106100"))

# Q14: Delta_1 = ln120 - ln98 = 4.787492 - 4.584967
c = 4.787492 - 4.584967
claims.append(("Q14", c, "0.202525"))

# Q15: Delta_2 = ln132 - ln120 = 4.882802 - 4.787492
c = 4.882802 - 4.787492
claims.append(("Q15", c, "0.095310"))

# Q16: Delta_3 = ln160 - ln132 = 5.075174 - 4.882802
c = 5.075174 - 4.882802
claims.append(("Q16", c, "0.192372"))

match_count = 0
for cid, computed, expected_str in claims:
    expected = float(expected_str)
    # match: computed rounded to the significant digits the paper states equals stated value
    # determine number of significant digits in expected string
    digits = len(expected_str.replace(".", "").replace("-", "").lstrip("0"))
    comp_rounded = sig(computed, digits)
    match = "yes" if abs(comp_rounded - expected) < 10 ** (-digits) * 0.5 * 10 ** max(1, math.floor(math.log10(abs(expected))) + 1 - digits) or comp_rounded == expected else "no"
    # simpler robust check: round computed to stated sig digits and compare as strings
    comp_r = sig(computed, digits)
    match = "yes" if f"{comp_r:.{digits}g}" == f"{expected:.{digits}g}" else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={fmt(computed)} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=9.0647222 expected=9.064722 match=yes
CLAIM Q2: computed=5.719203 expected=5.719203 match=yes
CLAIM Q3: computed=3.9039621 expected=3.903962 match=yes
CLAIM Q4: computed=3.2289186 expected=3.228919 match=yes
CLAIM Q5: computed=1.5849625 expected=1.584962 match=yes
CLAIM Q6: computed=2.3219288 expected=2.321929 match=yes
CLAIM Q7: computed=1.464974 expected=1.464974 match=yes
CLAIM Q8: computed=5.4792015 expected=5.479201 match=no
CLAIM Q9: computed=6.1575213e+08 expected=615752100 match=no
CLAIM Q10: computed=7.539822e+08 expected=753982200 match=yes
CLAIM Q11: computed=8.2938042e+08 expected=829380420 match=yes
CLAIM Q12: computed=1.0053096e+09 expected=1005309600 match=yes
CLAIM Q13: computed=8.0110607e+08 expected=801106100 match=no
CLAIM Q14: computed=0.202525 expected=0.202525 match=yes
CLAIM Q15: computed=0.09531 expected=0.095310 match=yes
CLAIM Q16: computed=0.192372 expected=0.192372 match=yes
VERIFICATION SUMMARY: 16 claims, 13 match, 3 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 9.0647222 | 9.064722 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q2 | 5.719203 | 5.719203 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q3 | 3.9039621 | 3.903962 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q4 | 3.2289186 | 3.228919 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q5 | 1.5849625 | 1.584962 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q6 | 2.3219288 | 2.321929 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q7 | 1.464974 | 1.464974 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q8 | 5.4792015 | 5.479201 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q9 | 6.1575213e+08 | 615752100 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q10 | 7.539822e+08 | 753982200 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q11 | 8.2938042e+08 | 829380420 | yes | match | 9 significant digits (as printed, at least 3) |
| Q12 | 1.0053096e+09 | 1005309600 | yes | match | 10 significant digits (as printed, at least 3) |
| Q13 | 8.0110607e+08 | 801106100 | no | match | 7 significant digits (as the paper states, at least 2) |
| Q14 | 0.202525 | 0.202525 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q15 | 0.09531 | 0.095310 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q16 | 0.192372 | 0.192372 | yes | match | 6 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
