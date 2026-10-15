# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Number of vertices at depth d is N_d = (p+1)p^{d-1} for d >= 1, N_0 = 1",
    "inputs": "p = 2, d = 10",
    "formula": "N_d = (p+1)*p^(d-1)"
  },
  {
    "id": "Q2",
    "statement": "Total vertices up to depth D: V_10 = 3070 for p = 2",
    "inputs": "p = 2, D = 10",
    "formula": "V_D = 1 + (p+1)*(p^D - 1)/(p - 1)"
  },
  {
    "id": "Q3",
    "statement": "Total comparable pairs up to depth D: C_10 = 27651 for p = 2",
    "inputs": "p = 2, D = 10",
    "formula": "C_D = (p+1)*(D*p^(D+1) - (D+1)*p^D + 1)/(p-1)^2"
  },
  {
    "id": "Q4",
    "statement": "Total unordered pairs in the depth-10 ball: binom(3070,2) = 4710915",
    "inputs": "V = 3070",
    "formula": "binom(V,2) = V*(V-1)/2"
  },
  {
    "id": "Q5",
    "statement": "Comparability fraction f_10 = 27651/4710915 ≈ 5.8696e-3",
    "inputs": "C_10 = 27651, binom(3070,2) = 4710915",
    "formula": "f = C / binom(V,2)"
  },
  {
    "id": "Q6",
    "statement": "Asymptotic comparability fraction f_D ~ 2(p-1)D/((p+1)p^D); at p=2, D=10 gives ≈ 6.5104e-3",
    "inputs": "p = 2, D = 10",
    "formula": "f_asym = 2*(p-1)*D/((p+1)*p^D)"
  },
  {
    "id": "Q7",
    "statement": "Mean depth bar(d) = 27651/3070 ≈ 9.0068",
    "inputs": "C_10 = 27651, V_10 = 3070",
    "formula": "bar_d = C_D / V_D"
  },
  {
    "id": "Q8",
    "statement": "Fraction of ball at outermost shell: 1536/3070 ≈ 0.50033 (50.03%)",
    "inputs": "N_10 = 1536, V_10 = 3070",
    "formula": "fraction = N_D / V_D"
  },
  {
    "id": "Q9",
    "statement": "Future-cone count C(5) = 62 for p = 2, Delta = 5",
    "inputs": "p = 2, Delta = 5",
    "formula": "C = (p^(Delta+1) - p)/(p - 1)"
  },
  {
    "id": "Q10",
    "statement": "Future-cone count C(5) = 363 for p = 3, Delta = 5",
    "inputs": "p = 3, Delta = 5",
    "formula": "C = (p^(Delta+1) - p)/(p - 1)"
  },
  {
    "id": "Q11",
    "statement": "Cone counts at Delta=5 differ by factor ≈ 5.85 between p=3 and p=2",
    "inputs": "C(5) = 363 (p=3), C(5) = 62 (p=2)",
    "formula": "ratio = 363 / 62"
  },
  {
    "id": "Q12",
    "statement": "Gap between cutoff and mean depth: (10 - 9.0068)/10 ≈ 9.932%",
    "inputs": "D = 10, bar_d = 9.0068",
    "formula": "gap = (D - bar_d)/D"
  },
  {
    "id": "Q13",
    "statement": "Asymptotic overestimate factor at D=10: 6.5104/5.8696 ≈ 1.109",
    "inputs": "f_asym = 6.5104e-3, f_exact = 5.8696e-3",
    "formula": "factor = f_asym / f_exact"
  },
  {
    "id": "Q14",
    "statement": "Decimal digits of 2^(10^20): ≈ 3.01e19",
    "inputs": "exponent E = 10^20, log10(2) ≈ 0.30103",
    "formula": "digits = E * log10(2)"
  }
]

## Script
```python
import math

def sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

results = []

# Q1: N_10 = (p+1)*p^(d-1), p=2, d=10
p, d = 2, 10
N10 = (p + 1) * p ** (d - 1)
results.append(("Q1", N10, "1536", 4))

# Q2: V_10 = 1 + (p+1)*(p^D - 1)/(p-1), p=2, D=10
p, D = 2, 10
V10 = 1 + (p + 1) * (p ** D - 1) // (p - 1)
results.append(("Q2", V10, "3070", 4))

# Q3: C_10 = (p+1)*(D*p^(D+1) - (D+1)*p^D + 1)/(p-1)^2, p=2, D=10
p, D = 2, 10
num = D * p ** (D + 1) - (D + 1) * p ** D + 1
C10 = (p + 1) * num // (p - 1) ** 2
results.append(("Q3", C10, "27651", 5))

# Q4: binom(3070,2) = 3070*3069/2
V = 3070
pairs = V * (V - 1) // 2
results.append(("Q4", pairs, "4710915", 7))

# Q5: f_10 = 27651/4710915
f10 = 27651 / 4710915
results.append(("Q5", f10, "0.0058696", 5))

# Q6: f_asym = 2*(p-1)*D/((p+1)*p^D), p=2, D=10
p, D = 2, 10
f_asym = 2 * (p - 1) * D / ((p + 1) * p ** D)
results.append(("Q6", f_asym, "0.0065104", 5))

# Q7: bar_d = 27651/3070
bar_d = 27651 / 3070
results.append(("Q7", bar_d, "9.0068", 5))

# Q8: fraction = 1536/3070
frac = 1536 / 3070
results.append(("Q8", frac, "0.50033", 5))

# Q9: C(5) = (2^6 - 2)/(2-1), p=2, Delta=5
p, Delta = 2, 5
C5_p2 = (p ** (Delta + 1) - p) // (p - 1)
results.append(("Q9", C5_p2, "62", 2))

# Q10: C(5) = (3^6 - 3)/2, p=3, Delta=5
p, Delta = 3, 5
C5_p3 = (p ** (Delta + 1) - p) // (p - 1)
results.append(("Q10", C5_p3, "363", 3))

# Q11: ratio = 363/62
ratio = 363 / 62
results.append(("Q11", ratio, "5.85", 3))

# Q12: gap = (10 - 9.0068)/10
gap = (10 - 27651 / 3070) / 10
results.append(("Q12", gap, "0.09932", 4))

# Q13: factor = f_asym / f_exact
factor = (2 * 1 * 10 / (3 * 2 ** 10)) / (27651 / 4710915)
results.append(("Q13", factor, "1.109", 4))

# Q14: digits = 10^20 * log10(2)
E = 10 ** 20
digits = E * math.log10(2)
results.append(("Q14", digits, "3.01e19", 3))

for cid, computed, expected, n in results:
    c = sig(computed, n)
    match = "yes" if float(expected) == c else "no"
    print(f"CLAIM {cid}: computed={c:.8g} expected={expected} match={match}")

print("VERIFICATION SUMMARY: 14 claims, " + str(sum(1 for _, _, e, n in results if float(e) == sig(dict((r[0], r[1]) for r in results)[_], n)) if False else "") , end="")

```

## Execution output
```
CLAIM Q1: computed=1536 expected=1536 match=yes
CLAIM Q2: computed=3070 expected=3070 match=yes
CLAIM Q3: computed=27651 expected=27651 match=yes
CLAIM Q4: computed=4710915 expected=4710915 match=yes
CLAIM Q5: computed=0.0058696 expected=0.0058696 match=yes
CLAIM Q6: computed=0.0065104 expected=0.0065104 match=yes
CLAIM Q7: computed=9.0068 expected=9.0068 match=yes
CLAIM Q8: computed=0.50033 expected=0.50033 match=yes
CLAIM Q9: computed=62 expected=62 match=yes
CLAIM Q10: computed=363 expected=363 match=yes
CLAIM Q11: computed=5.85 expected=5.85 match=yes
CLAIM Q12: computed=0.09932 expected=0.09932 match=yes
CLAIM Q13: computed=1.109 expected=1.109 match=yes
CLAIM Q14: computed=3.01e+19 expected=3.01e19 match=yes
VERIFICATION SUMMARY: 14 claims, 
[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1536 | 1536 | yes | match | 4 significant digits (as printed, at least 3) |
| Q2 | 3070 | 3070 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 27651 | 27651 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q4 | 4710915 | 4710915 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q5 | 0.0058696 | 0.0058696 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q6 | 0.0065104 | 0.0065104 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q7 | 9.0068 | 9.0068 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 0.50033 | 0.50033 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 62 | 62 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q10 | 363 | 363 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 5.85 | 5.85 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 0.09932 | 0.09932 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q13 | 1.109 | 1.109 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q14 | 3.01e+19 | 3.01e19 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 14.
