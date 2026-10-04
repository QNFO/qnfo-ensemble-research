# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "25% fewer logical failures corresponds to improvement factor F1 = 0.75",
    "inputs": "reduction X1 = 25%",
    "formula": "F1 = 1 - X1/100 = 1 - 0.25 = 0.75"
  },
  {
    "id": "Q2",
    "statement": "16% fewer logical failures corresponds to improvement factor F2 = 0.84",
    "inputs": "reduction X2 = 16%",
    "formula": "F2 = 1 - X2/100 = 1 - 0.16 = 0.84"
  },
  {
    "id": "Q3",
    "statement": "Equivalent relative pseudo-threshold improvement at d = 5 is ≈10.06%",
    "inputs": "F1 = 0.75, d = 5, m = ceil(d/2) = 3",
    "formula": "p_th^POLY / p_th^MWPM = (1/F1)^(1/m) = (4/3)^(1/3) = e^(ln(4/3)/3) = e^(0.287682/3) = e^0.095894 = 1.100642416298209"
  },
  {
    "id": "Q4",
    "statement": "Equivalent relative pseudo-threshold improvement at d = 7 is ≈7.46%",
    "inputs": "F1 = 0.75, d = 7, m = ceil(d/2) = 4",
    "formula": "(1/F1)^(1/m) = e^(0.287682/4) = e^0.0719206 = 1.074569931823542"
  },
  {
    "id": "Q5",
    "statement": "Equivalent relative pseudo-threshold improvement at d = 9 is ≈5.92%",
    "inputs": "F1 = 0.75, d = 9, m = ceil(d/2) = 5",
    "formula": "(1/F1)^(1/m) = e^(0.287682/5) = e^0.0575364 = 1.0592238410488122"
  },
  {
    "id": "Q6",
    "statement": "Distance-equivalent exponent gain at p/p_th = 0.5 is 0.4150374992788438, roughly half of one odd-distance step",
    "inputs": "F1 = 0.75, r = 0.5",
    "formula": "Δm = ln(F1)/ln(r) = ln(0.75)/ln(0.5) = (-0.287682)/(-0.693147) = 0.4150374992788438"
  },
  {
    "id": "Q7",
    "statement": "qLDPC equivalent threshold improvement factor is ≈1.0598398329483265 (≈5.98%)",
    "inputs": "F2 = 0.84, d = 6, m = ceil(6/2) = 3",
    "formula": "(1/F2)^(1/m) = (1/0.84)^(1/3) = e^(ln(1.190476)/3) = e^(0.174353/3) = e^0.0581177 = 1.0598398329483265"
  },
  {
    "id": "Q8",
    "statement": "Encoding rate of [[130,4,6]] is ≈3.08%",
    "inputs": "k = 4, n = 130",
    "formula": "k/n = 4/130 = 0.03076923076923077"
  }
]

## Script
```python
import math

def check(cid, computed, expected, is_float=True):
    if expected is None:
        match = "no"
    elif is_float:
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1
F1 = 1 - 25/100
results.append(check("Q1", F1, 0.75))

# Q2
F2 = 1 - 16/100
results.append(check("Q2", F2, 0.84))

# Q3
m3 = math.ceil(5/2)
v3 = (1/F1)**(1/m3)
results.append(check("Q3", v3, 1.100642416298209))

# Q4
m4 = math.ceil(7/2)
v4 = (1/F1)**(1/m4)
results.append(check("Q4", v4, 1.074569931823542))

# Q5
m5 = math.ceil(9/2)
v5 = (1/F1)**(1/m5)
results.append(check("Q5", v5, 1.0592238410488122))

# Q6
v6 = math.log(F1)/math.log(0.5)
results.append(check("Q6", v6, 0.4150374992788438))

# Q7
m7 = math.ceil(6/2)
v7 = (1/F2)**(1/m7)
results.append(check("Q7", v7, 1.0598398329483265))

# Q8
v8 = 4/130
results.append(check("Q8", v8, 0.03076923076923077))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n-m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.75 expected=0.75 match=yes
CLAIM Q2: computed=0.84 expected=0.84 match=yes
CLAIM Q3: computed=1.100642416298209 expected=1.100642416298209 match=yes
CLAIM Q4: computed=1.074569931823542 expected=1.074569931823542 match=yes
CLAIM Q5: computed=1.0592238410488122 expected=1.0592238410488122 match=yes
CLAIM Q6: computed=0.4150374992788438 expected=0.4150374992788438 match=yes
CLAIM Q7: computed=1.0598398329483265 expected=1.0598398329483265 match=yes
CLAIM Q8: computed=0.03076923076923077 expected=0.03076923076923077 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
