# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Raw depth ratio for q=2: 13.815511 / 0.693147 = 19.931574",
    "inputs": "lnN = 13.815511, ln2 = 0.693147",
    "formula": "ratio = lnN / ln2"
  },
  {
    "id": "Q2",
    "statement": "Raw depth ratio for q=3: 13.815511 / 1.098612 = 12.575423",
    "inputs": "lnN = 13.815511, ln3 = 1.098612",
    "formula": "ratio = lnN / ln3"
  },
  {
    "id": "Q3",
    "statement": "Raw depth ratio for q=4: 13.815511 / 1.386294 = 9.965787",
    "inputs": "lnN = 13.815511, ln4 = 1.386294",
    "formula": "ratio = lnN / ln4"
  },
  {
    "id": "Q4",
    "statement": "Raw depth ratio for q=5: 13.815511 / 1.609438 = 8.584059",
    "inputs": "lnN = 13.815511, ln5 = 1.609438",
    "formula": "ratio = lnN / ln5"
  },
  {
    "id": "Q5",
    "statement": "Depth values after ceiling: n(2)=20, n(3)=13, n(4)=10, n(5)=9",
    "inputs": "ratios from Q1‑Q4",
    "formula": "n(q) = ceil(ratio)"
  },
  {
    "id": "Q6",
    "statement": "Traversal costs: T(2)=40, T(3)=39, T(4)=40, T(5)=45",
    "inputs": "q values {2,3,4,5}, n values from Q5",
    "formula": "T(q) = q * n(q)"
  },
  {
    "id": "Q7",
    "statement": "Normalized traversal for q=2: 40 / 13.815511 = 2.8953",
    "inputs": "T(2)=40, T_ref = lnN = 13.815511",
    "formula": "T(q)/T_ref"
  },
  {
    "id": "Q8",
    "statement": "Normalized traversal for q=3: 39 / 13.815511 = 2.8229",
    "inputs": "T(3)=39, T_ref = 13.815511",
    "formula": "T(q)/T_ref"
  },
  {
    "id": "Q9",
    "statement": "Normalized traversal for q=5: 45 / 13.815511 = 3.2572",
    "inputs": "T(5)=45, T_ref = 13.815511",
    "formula": "T(q)/T_ref"
  },
  {
    "id": "Q10",
    "statement": "q^{-n} for q=2, n=20: 2^{-20} ≈ 9.54×10^{-7}",
    "inputs": "q=2, n=20",
    "formula": "q^{-n} = e^{-n * ln q}"
  },
  {
    "id": "Q11",
    "statement": "q^{-n} for q=3, n=13: 3^{-13} ≈ 6.27×10^{-7}",
    "inputs": "q=3, n=13",
    "formula": "q^{-n} = e^{-n * ln q}"
  },
  {
    "id": "Q12",
    "statement": "q^{-n} for q=4, n=10: 4^{-10} ≈ 9.54×10^{-7}",
    "inputs": "q=4, n=10",
    "formula": "q^{-n} = e^{-n * ln q}"
  },
  {
    "id": "Q13",
    "statement": "q^{-n} for q=5, n=9: 5^{-9} ≈ 5.12×10^{-7}",
    "inputs": "q=5, n=9",
    "formula": "q^{-n} = e^{-n * ln q}"
  },
  {
    "id": "Q14",
    "statement": "Storage per item S(q)/N for q=2: 2.0000",
    "inputs": "q=2, q^{-n} from Q10",
    "formula": "S/N = q*(1 - q^{-n})/(q-1)"
  },
  {
    "id": "Q15",
    "statement": "Storage per item S(q)/N for q=3: 1.5000",
    "inputs": "q=3, q^{-n} from Q11",
    "formula": "S/N = q*(1 - q^{-n})/(q-1)"
  },
  {
    "id": "Q16",
    "statement": "Storage per item S(q)/N for q=4: 1.3333",
    "inputs": "q=4, q^{-n} from Q12",
    "formula": "S/N = q*(1 - q^{-n})/(q-1)"
  }
]

## Script
```python
import math

# Input constants
lnN = 13.815511
ln2 = 0.693147
ln3 = 1.098612
ln4 = 1.386294
ln5 = 1.609438

# Helper to format expected values
def fmt(val, digits=4):
    return f"{val:.4f}"

# CLAIM Q1
ratio_q2 = lnN / ln2
print(f"CLAIM Q1: computed={ratio_q2:.6f} expected=19.931574 match={'yes' if round(ratio_q2,6)==19.931574 else 'no'}")

# CLAIM Q2
ratio_q3 = lnN / ln3
print(f"CLAIM Q2: computed={ratio_q3:.6f} expected=12.575423 match={'yes' if round(ratio_q3,6)==12.575423 else 'no'}")

# CLAIM Q3
ratio_q4 = lnN / ln4
print(f"CLAIM Q3: computed={ratio_q4:.6f} expected=9.965787 match={'yes' if round(ratio_q4,6)==9.965787 else 'no'}")

# CLAIM Q4
ratio_q5 = lnN / ln5
print(f"CLAIM Q4: computed={ratio_q5:.6f} expected=8.584059 match={'yes' if round(ratio_q5,6)==8.584059 else 'no'}")

# CLAIM Q5
n2 = math.ceil(ratio_q2)
n3 = math.ceil(ratio_q3)
n4 = math.ceil(ratio_q4)
n5 = math.ceil(ratio_q5)
print(f"CLAIM Q5: computed={n2},{n3},{n4},{n5} expected=20,13,10,9 match={'yes' if (n2,n3,n4,n5)==(20,13,10,9) else 'no'}")

# CLAIM Q6
T2 = 2 * n2
T3 = 3 * n3
T4 = 4 * n4
T5 = 5 * n5
print(f"CLAIM Q6: computed={T2},{T3},{T4},{T5} expected=40,39,40,45 match={'yes' if (T2,T3,T4,T5)==(40,39,40,45) else 'no'}")

# CLAIM Q7
norm_T2 = T2 / lnN
print(f"CLAIM Q7: computed={norm_T2:.4f} expected=2.8953 match={'yes' if round(norm_T2,4)==2.8953 else 'no'}")

# CLAIM Q8
norm_T3 = T3 / lnN
print(f"CLAIM Q8: computed={norm_T3:.4f} expected=2.8229 match={'yes' if round(norm_T3,4)==2.8229 else 'no'}")

# CLAIM Q9
norm_T5 = T5 / lnN
print(f"CLAIM Q9: computed={norm_T5:.4f} expected=3.2572 match={'yes' if round(norm_T5,4)==3.2572 else 'no'}")

# CLAIM Q10
q2_n20 = math.exp(-20 * ln2)
print(f"CLAIM Q10: computed={q2_n20:.2e} expected=9.54e-07 match={'yes' if abs(q2_n20-9.54e-07)/9.54e-07<1e-2 else 'no'}")

# CLAIM Q11
q3_n13 = math.exp(-13 * ln3)
print(f"CLAIM Q11: computed={q3_n13:.2e} expected=6.27e-07 match={'yes' if abs(q3_n13-6.27e-07)/6.27e-07<1e-2 else 'no'}")

# CLAIM Q12
q4_n10 = math.exp(-10 * ln4)
print(f"CLAIM Q12: computed={q4_n10:.2e} expected=9.54e-07 match={'yes' if abs(q4_n10-9.54e-07)/9.54e-07<1e-2 else 'no'}")

# CLAIM Q13
q5_n9 = math.exp(-9 * ln5)
print(f"CLAIM Q13: computed={q5_n9:.2e} expected=5.12e-07 match={'yes' if abs(q5_n9-5.12e-07)/5.12e-07<1e-2 else 'no'}")

# CLAIM Q14
S2_N = 2 * (1 - q2_n20) / (2 - 1)
print(f"CLAIM Q14: computed={S2_N:.4f} expected=2.0000 match={'yes' if round(S2_N,4)==2.0000 else 'no'}")

# CLAIM Q15
S3_N = 3 * (1 - q3_n13) / (3 - 1)
print(f"CLAIM Q15: computed={S3_N:.4f} expected=1.5000 match={'yes' if round(S3_N,4)==1.5000 else 'no'}")

# CLAIM Q16
S4_N = 4 * (1 - q4_n10) / (4 - 1)
print(f"CLAIM Q16: computed={S4_N:.4f} expected=1.3333 match={'yes' if round(S4_N,4)==1.3333 else 'no'}")

print("VERIFICATION SUMMARY: 16 claims, "
      f"{sum(1 for line in open(__file__) if 'match=yes' in line)} match, "
      f"{sum(1 for line in open(__file__) if 'match=no' in line)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=19.931574 expected=19.931574 match=yes
CLAIM Q2: computed=12.575423 expected=12.575423 match=yes
CLAIM Q3: computed=9.965787 expected=9.965787 match=yes
CLAIM Q4: computed=8.584059 expected=8.584059 match=yes
CLAIM Q5: computed=20,13,10,9 expected=20,13,10,9 match=yes
CLAIM Q6: computed=40,39,40,45 expected=40,39,40,45 match=yes
CLAIM Q7: computed=2.8953 expected=2.8953 match=yes
CLAIM Q8: computed=2.8229 expected=2.8229 match=yes
CLAIM Q9: computed=3.2572 expected=3.2572 match=yes
CLAIM Q10: computed=9.54e-07 expected=9.54e-07 match=yes
CLAIM Q11: computed=6.27e-07 expected=6.27e-07 match=yes
CLAIM Q12: computed=9.54e-07 expected=9.54e-07 match=yes
CLAIM Q13: computed=5.12e-07 expected=5.12e-07 match=yes
CLAIM Q14: computed=2.0000 expected=2.0000 match=yes
CLAIM Q15: computed=1.5000 expected=1.5000 match=yes
CLAIM Q16: computed=1.3333 expected=1.3333 match=yes

[stderr]
Traceback (most recent call last):
  File "<string>", line 85, in <module>
NameError: name '__file__' is not defined. Did you mean: '__name__'?

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 19.931574 | 19.931574 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q2 | 12.575423 | 12.575423 | yes | match | 8 significant digits (as the paper states, at least 2) |
| Q3 | 9.965787 | 9.965787 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q4 | 8.584059 | 8.584059 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q5 | 20,13,10,9 | 20,13,10,9 | yes | match | script verdict (values not both numeric) |
| Q6 | 40,39,40,45 | 40,39,40,45 | yes | match | script verdict (values not both numeric) |
| Q7 | 2.8953 | 2.8953 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 2.8229 | 2.8229 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q9 | 3.2572 | 3.2572 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q10 | 9.54e-07 | 9.54e-07 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 6.27e-07 | 6.27e-07 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 9.54e-07 | 9.54e-07 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 5.12e-07 | 5.12e-07 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 2.0000 | 2.0000 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q15 | 1.5000 | 1.5000 | yes | match | 5 significant digits (as the paper states, at least 2) |
| Q16 | 1.3333 | 1.3333 | yes | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
