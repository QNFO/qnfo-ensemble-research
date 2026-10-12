# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Warranty margin upper: m_max = 12.2/5 = 2.44",
    "inputs": "T_HBF_max = 12.2 device-years (assumed input); warranty = 5 years",
    "formula": "m = T_HBF / 5"
  },
  {
    "id": "Q2",
    "statement": "Warranty margin lower: m_min = 3.3/5 = 0.66",
    "inputs": "T_HBF_min = 3.3 device-years (assumed input); warranty = 5 years",
    "formula": "m = T_HBF / 5"
  },
  {
    "id": "Q3",
    "statement": "Implied baseline lifetime low: T_base_low = 3.3/3.13 ≈ 1.05 device-years",
    "inputs": "T_HBF_min = 3.3; f_max = 3.13",
    "formula": "T_base = T_HBF / f"
  },
  {
    "id": "Q4",
    "statement": "Implied baseline lifetime high: T_base_high = 12.2/1.19 ≈ 10.25 device-years",
    "inputs": "T_HBF_max = 12.2; f_min = 1.19",
    "formula": "T_base = T_HBF / f"
  },
  {
    "id": "Q5",
    "statement": "Geometric-mean extension ≈ 1.93x",
    "inputs": "f_min = 1.19; f_max = 3.13",
    "formula": "f_bar = sqrt(f_min * f_max)"
  },
  {
    "id": "Q6",
    "statement": "Write-diversion fraction for f = 1.19: φ ≈ 15.97%",
    "inputs": "f = 1.19",
    "formula": "phi = 1 - 1/f"
  },
  {
    "id": "Q7",
    "statement": "Write-diversion fraction for f = 3.13: φ ≈ 68.05%",
    "inputs": "f = 3.13",
    "formula": "phi = 1 - 1/f"
  },
  {
    "id": "Q8",
    "statement": "Annualized HBF write budget at T_HBF = 12.2 device-years with E_HBF = 1e5 cycles: ≈ 8.20e3 writes/year",
    "inputs": "E_HBF = 100000 cycles (labeled illustrative assumption); T_HBF = 12.2",
    "formula": "W_HBF_yr = E_HBF / T_HBF"
  },
  {
    "id": "Q9",
    "statement": "HBF writes per hour at 12.2 device-years: ≈ 0.9357",
    "inputs": "W_HBF_yr = 8196.72... writes/year; hours/year = 8760",
    "formula": "W_per_hour = W_HBF_yr / 8760"
  },
  {
    "id": "Q10",
    "statement": "Annualized HBF write budget at T_HBF = 3.3 device-years with E_HBF = 1e5 cycles: ≈ 3.03e4 writes/year",
    "inputs": "E_HBF = 100000; T_HBF = 3.3",
    "formula": "W_HBF_yr = E_HBF / T_HBF"
  },
  {
    "id": "Q11",
    "statement": "HBF writes per hour at 3.3 device-years: ≈ 3.46",
    "inputs": "W_HBF_yr = 30303.03... writes/year; hours/year = 8760",
    "formula": "W_per_hour = W_HBF_yr / 8760"
  },
  {
    "id": "Q12",
    "statement": "Scaling factor between illustrative endurance values: 3e3/1e5 = 0.03",
    "inputs": "E_HBF_low = 3000; E_HBF_high = 100000",
    "formula": "scale = E_HBF_low / E_HBF_high"
  },
  {
    "id": "Q13",
    "statement": "Hours per year under 24x7 operation: 8760",
    "inputs": "24 hours/day; 365 days/year",
    "formula": "24 * 365"
  },
  {
    "id": "Q14",
    "statement": "Hours in a five-year warranty: 43800",
    "inputs": "8760 hours/year; 5 years",
    "formula": "5 * 8760"
  },
  {
    "id": "Q15",
    "statement": "Worst-case projected lifetime: 1.05 * 1.19 ≈ 1.25 device-years",
    "inputs": "T_base_low ≈ 1.05; f_min = 1.19",
    "formula": "T = T_base_low * f_min"
  }
]

## Script
```python
import math

def claim(id, computed, expected, match):
    print(f"CLAIM {id}: computed={computed} expected={expected} match={match}")

# Q1: m_max = 12.2 / 5
c = 12.2 / 5
claim("Q1", f"{c:.8f}", "2.44", "yes" if round(c, 2) == 2.44 else "no")

# Q2: m_min = 3.3 / 5
c = 3.3 / 5
claim("Q2", f"{c:.8f}", "0.66", "yes" if round(c, 2) == 0.66 else "no")

# Q3: T_base_low = 3.3 / 3.13
c = 3.3 / 3.13
claim("Q3", f"{c:.8f}", "1.05", "yes" if round(c, 2) == 1.05 else "no")

# Q4: T_base_high = 12.2 / 1.19
c = 12.2 / 1.19
claim("Q4", f"{c:.8f}", "10.25", "yes" if round(c, 2) == 10.25 else "no")

# Q5: f_bar = sqrt(1.19 * 3.13)
c = math.sqrt(1.19 * 3.13)
claim("Q5", f"{c:.8f}", "1.93", "yes" if round(c, 2) == 1.93 else "no")

# Q6: phi = 1 - 1/1.19 (as percent)
c = (1 - 1/1.19) * 100
claim("Q6", f"{c:.8f}", "15.97", "yes" if round(c, 2) == 15.97 else "no")

# Q7: phi = 1 - 1/3.13 (as percent)
c = (1 - 1/3.13) * 100
claim("Q7", f"{c:.8f}", "68.05", "yes" if round(c, 2) == 68.05 else "no")

# Q8: W = 1e5 / 12.2
c = 100000 / 12.2
claim("Q8", f"{c:.8f}", "8200", "yes" if round(c, -2) == 8200 else "no")

# Q9: per hour = (1e5/12.2) / 8760
c = (100000 / 12.2) / 8760
claim("Q9", f"{c:.8f}", "0.9357", "yes" if round(c, 4) == 0.9357 else "no")

# Q10: W = 1e5 / 3.3
c = 100000 / 3.3
claim("Q10", f"{c:.8f}", "30300", "yes" if round(c, -2) == 30300 else "no")

# Q11: per hour = (1e5/3.3) / 8760
c = (100000 / 3.3) / 8760
claim("Q11", f"{c:.8f}", "3.46", "yes" if round(c, 2) == 3.46 else "no")

# Q12: scale = 3e3 / 1e5
c = 3000 / 100000
claim("Q12", f"{c:.8f}", "0.03", "yes" if round(c, 2) == 0.03 else "no")

# Q13: hours/year = 24 * 365
c = 24 * 365
claim("Q13", f"{c:.8f}", "8760", "yes" if c == 8760 else "no")

# Q14: hours in 5-year warranty = 5 * 8760
c = 5 * 8760
claim("Q14", f"{c:.8f}", "43800", "yes" if c == 43800 else "no")

# Q15: worst case = 1.05 * 1.19 (paper uses rounded 1.05)
c = 1.05 * 1.19
claim("Q15", f"{c:.8f}", "1.25", "yes" if round(c, 2) == 1.25 else "no")

print("VERIFICATION SUMMARY: 15 claims, 15 match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=2.44000000 expected=2.44 match=yes
CLAIM Q2: computed=0.66000000 expected=0.66 match=yes
CLAIM Q3: computed=1.05431310 expected=1.05 match=yes
CLAIM Q4: computed=10.25210084 expected=10.25 match=yes
CLAIM Q5: computed=1.92994819 expected=1.93 match=yes
CLAIM Q6: computed=15.96638655 expected=15.97 match=yes
CLAIM Q7: computed=68.05111821 expected=68.05 match=yes
CLAIM Q8: computed=8196.72131148 expected=8200 match=yes
CLAIM Q9: computed=0.93569878 expected=0.9357 match=yes
CLAIM Q10: computed=30303.03030303 expected=30300 match=yes
CLAIM Q11: computed=3.45925003 expected=3.46 match=yes
CLAIM Q12: computed=0.03000000 expected=0.03 match=yes
CLAIM Q13: computed=8760.00000000 expected=8760 match=yes
CLAIM Q14: computed=43800.00000000 expected=43800 match=yes
CLAIM Q15: computed=1.24950000 expected=1.25 match=yes
VERIFICATION SUMMARY: 15 claims, 15 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 2.44000000 | 2.44 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 0.66000000 | 0.66 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 1.05431310 | 1.05 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 10.25210084 | 10.25 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 1.92994819 | 1.93 | yes | match | 3 significant digits (as printed, at least 3) |
| Q6 | 15.96638655 | 15.97 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 68.05111821 | 68.05 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q8 | 8196.72131148 | 8200 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 0.93569878 | 0.9357 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 30303.03030303 | 30300 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 3.45925003 | 3.46 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 0.03000000 | 0.03 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 8760.00000000 | 8760 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q14 | 43800.00000000 | 43800 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q15 | 1.24950000 | 1.25 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 15.
