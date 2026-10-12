# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Normal-approximation z-score for the confidence-floor count: z ≈ 38.45",
    "inputs": "N=60, p0=0.025, x=48",
    "formula": "z = (x - N*p0) / sqrt(N*p0*(1-p0))"
  },
  {
    "id": "Q2",
    "statement": "Exact binomial point probability P(X=48) ≈ 1.3e-65 under Binomial(60, 0.025)",
    "inputs": "N=60, p0=0.025, k=48, C(60,12)=1399353840075",
    "formula": "P(X=48) = C(60,48) * 0.025^48 * 0.975^12"
  },
  {
    "id": "Q3",
    "statement": "Sensitivity z-score at p0=0.05: z ≈ 26.66",
    "inputs": "N=60, p0=0.05, x=48",
    "formula": "z = (x - N*p0) / sqrt(N*p0*(1-p0))"
  },
  {
    "id": "Q4",
    "statement": "z-score for distillation-baseline count: z ≈ 0.25820",
    "inputs": "N=60, p0=0.5, x=31",
    "formula": "z = (x - N*p0) / sqrt(N*p0*(1-p0))"
  },
  {
    "id": "Q5",
    "statement": "95% Wald interval for p1 = 0.8 is [0.6988, 0.9012]",
    "inputs": "x=48, N=60",
    "formula": "p_hat ± 1.96*sqrt(p_hat*(1-p_hat)/N)"
  },
  {
    "id": "Q6",
    "statement": "95% Wald interval for p2 = 0.516667 is [0.3902, 0.6431]",
    "inputs": "x=31, N=60",
    "formula": "p_hat ± 1.96*sqrt(p_hat*(1-p_hat)/N)"
  },
  {
    "id": "Q7",
    "statement": "Quality-cost product vs direct querying: B_Opus = 538.74",
    "inputs": "rho=0.82, c_L/c_A=657",
    "formula": "B = rho * (c_L/c_A)"
  },
  {
    "id": "Q8",
    "statement": "Quality-cost product vs Jev: B_Jev = 3.76",
    "inputs": "rho'=0.94, r'=0.25",
    "formula": "B = rho'/r'"
  },
  {
    "id": "Q9",
    "statement": "Minimum retention threshold vs direct querying: rho_min ≈ 0.001522",
    "inputs": "c_L/c_A=657",
    "formula": "rho_min = 1/(c_L/c_A)"
  },
  {
    "id": "Q10",
    "statement": "Raw break-even workload n* ≈ 1.00152 * C0/c_L",
    "inputs": "c_L/c_A=657",
    "formula": "n* = (C0/c_L)/(1 - 1/657)"
  },
  {
    "id": "Q11",
    "statement": "Quality-adjusted break-even workload n*_rho ≈ 1.2218 * C0/c_L",
    "inputs": "rho=0.82, c_L/c_A=657",
    "formula": "n*_rho = (C0/c_L)/(rho - 1/657)"
  },
  {
    "id": "Q12",
    "statement": "Break-even ratio inflation factor ≈ 1.22",
    "inputs": "n*_rho=1.2218, n*=1.00152",
    "formula": "n*_rho / n*"
  },
  {
    "id": "Q13",
    "statement": "Sensitivity: at rho=0.5, n*_rho ≈ 2.006 * C0/c_L",
    "inputs": "rho=0.5, c_L/c_A=657",
    "formula": "n*_rho = (C0/c_L)/(rho - 1/657)"
  },
  {
    "id": "Q14",
    "statement": "Sensitivity: at rho=0.25, n*_rho ≈ 4.025 * C0/c_L",
    "inputs": "rho=0.25, c_L/c_A=657",
    "formula": "n*_rho = (C0/c_L)/(rho - 1/657)"
  },
  {
    "id": "Q15",
    "statement": "Break-even against Jev at rho'=0.94: ≈ 1.449 * C0/c_L",
    "inputs": "rho'=0.94, r'=0.25",
    "formula": "n*' = (C0/c_L)/(rho' - 0.25)"
  },
  {
    "id": "Q16",
    "statement": "Projected raw break-even ≈ 10,015 instances",
    "inputs": "C0=100 dollars, c_L=0.01 dollars, c_L/c_A=657",
    "formula": "n* = C0/(c_L*(1 - 1/657))"
  }
]

## Script
```python
import math

def zscore(N, p0, x):
    mu = N * p0
    sigma = math.sqrt(N * p0 * (1 - p0))
    return (x - mu) / sigma

# Q1
z1 = zscore(60, 0.025, 48)
print(f"CLAIM Q1: computed={z1:.6f} expected=38.45 match={'yes' if round(z1,2)==38.45 else 'no'}")

# Q2
C = math.comb(60, 48)
p48 = C * (0.025**48) * (0.975**12)
print(f"CLAIM Q2: computed={p48:.8e} expected=1.3e-65 match={'yes' if abs(math.log10(p48) - math.log10(1.3e-65)) < 0.05 else 'no'}")

# Q3
z3 = zscore(60, 0.05, 48)
print(f"CLAIM Q3: computed={z3:.6f} expected=26.66 match={'yes' if round(z3,2)==26.66 else 'no'}")

# Q4
z4 = zscore(60, 0.5, 31)
print(f"CLAIM Q4: computed={z4:.6f} expected=0.25820 match={'yes' if round(z4,5)==0.25820 else 'no'}")

# Q5
ph1 = 48/60
se1 = math.sqrt(ph1*(1-ph1)/60)
lo1, hi1 = ph1 - 1.96*se1, ph1 + 1.96*se1
print(f"CLAIM Q5: computed=[{lo1:.6f},{hi1:.6f}] expected=[0.6988,0.9012] match={'yes' if round(lo1,4)==0.6988 and round(hi1,4)==0.9012 else 'no'}")

# Q6
ph2 = 31/60
se2 = math.sqrt(ph2*(1-ph2)/60)
lo2, hi2 = ph2 - 1.96*se2, ph2 + 1.96*se2
print(f"CLAIM Q6: computed=[{lo2:.6f},{hi2:.6f}] expected=[0.3902,0.6431] match={'yes' if round(lo2,4)==0.3902 and round(hi2,4)==0.6431 else 'no'}")

# Q7
B7 = 0.82 * 657
print(f"CLAIM Q7: computed={B7:.8f} expected=538.74 match={'yes' if round(B7,2)==538.74 else 'no'}")

# Q8
B8 = 0.94 / 0.25
print(f"CLAIM Q8: computed={B8:.8f} expected=3.76 match={'yes' if round(B8,2)==3.76 else 'no'}")

# Q9
r9 = 1/657
print(f"CLAIM Q9: computed={r9:.8f} expected=0.001522 match={'yes' if round(r9,6)==0.001522 else 'no'}")

# Q10
n10 = 1/(1 - 1/657)
print(f"CLAIM Q10: computed={n10:.8f} expected=1.00152 match={'yes' if round(n10,5)==1.00152 else 'no'}")

# Q11
n11 = 1/(0.82 - 1/657)
print(f"CLAIM Q11: computed={n11:.8f} expected=1.2218 match={'yes' if round(n11,4)==1.2218 else 'no'}")

# Q12
n12 = n11 / n10
print(f"CLAIM Q12: computed={n12:.8f} expected=1.22 match={'yes' if round(n12,2)==1.22 else 'no'}")

# Q13
n13 = 1/(0.5 - 1/657)
print(f"CLAIM Q13: computed={n13:.8f} expected=2.006 match={'yes' if round(n13,3)==2.006 else 'no'}")

# Q14
n14 = 1/(0.25 - 1/657)
print(f"CLAIM Q14: computed={n14:.8f} expected=4.025 match={'yes' if round(n14,3)==4.025 else 'no'}")

# Q15
n15 = 1/(0.94 - 0.25)
print(f"CLAIM Q15: computed={n15:.8f} expected=1.449 match={'yes' if round(n15,3)==1.449 else 'no'}")

# Q16
n16 = 100/(0.01*(1 - 1/657))
print(f"CLAIM Q16: computed={n16:.8f} expected=10015 match={'yes' if round(n16)==10015 else 'no'}")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=38.450768 expected=38.45 match=yes
CLAIM Q2: computed=1.30348159e-65 expected=1.3e-65 match=yes
CLAIM Q3: computed=26.655699 expected=26.66 match=yes
CLAIM Q4: computed=0.258199 expected=0.25820 match=yes
CLAIM Q5: computed=[0.698786,0.901214] expected=[0.6988,0.9012] match=yes
CLAIM Q6: computed=[0.390220,0.643114] expected=[0.3902,0.6431] match=yes
CLAIM Q7: computed=538.74000000 expected=538.74 match=yes
CLAIM Q8: computed=3.76000000 expected=3.76 match=yes
CLAIM Q9: computed=0.00152207 expected=0.001522 match=yes
CLAIM Q10: computed=1.00152439 expected=1.00152 match=yes
CLAIM Q11: computed=1.22178004 expected=1.2218 match=yes
CLAIM Q12: computed=1.21992041 expected=1.22 match=yes
CLAIM Q13: computed=2.00610687 expected=2.006 match=yes
CLAIM Q14: computed=4.02450230 expected=4.025 match=yes
CLAIM Q15: computed=1.44927536 expected=1.449 match=yes
CLAIM Q16: computed=10015.24390244 expected=10015 match=yes
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 38.450768 | 38.45 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q2 | 1.30348159e-65 | 1.3e-65 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 26.655699 | 26.66 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q4 | 0.258199 | 0.25820 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q5 | [0.698786,0.901214] | [0.6988,0.9012] | yes | match | script verdict (values not both numeric) |
| Q6 | [0.390220,0.643114] | [0.3902,0.6431] | yes | match | script verdict (values not both numeric) |
| Q7 | 538.74000000 | 538.74 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 3.76000000 | 3.76 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 0.00152207 | 0.001522 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 1.00152439 | 1.00152 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q11 | 1.22178004 | 1.2218 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q12 | 1.21992041 | 1.22 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 2.00610687 | 2.006 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q14 | 4.02450230 | 4.025 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q15 | 1.44927536 | 1.449 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q16 | 10015.24390244 | 10015 | yes | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
