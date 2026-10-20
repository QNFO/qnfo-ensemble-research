# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "For depth d = 5 the total number of leaves is L = 32.",
    "inputs": "d = 5",
    "formula": "L = 2^d"
  },
  {
    "id": "Q2",
    "statement": "Amplitude a equals sqrt(20/32) which is approximately 0.790569415.",
    "inputs": "n_A = 20, L = 32",
    "formula": "a = sqrt(n_A / L)"
  },
  {
    "id": "Q3",
    "statement": "Amplitude b equals sqrt(12/32) which is approximately 0.612372436.",
    "inputs": "n_B = 12, L = 32",
    "formula": "b = sqrt(n_B / L)"
  },
  {
    "id": "Q4",
    "statement": "Probability P_A equals 0.625.",
    "inputs": "a = sqrt(0.625)",
    "formula": "P_A = a^2"
  },
  {
    "id": "Q5",
    "statement": "Complementary probability P_B equals 0.375.",
    "inputs": "P_A = 0.625",
    "formula": "P_B = 1 - P_A"
  },
  {
    "id": "Q6",
    "statement": "Circuit capacity D_C for N = 4 qubits is 30.",
    "inputs": "N = 4",
    "formula": "D_C = 2^(N+1) - 2"
  },
  {
    "id": "Q7",
    "statement": "For depth d = 10 the total number of leaves is L = 1024.",
    "inputs": "d = 10",
    "formula": "L = 2^d"
  },
  {
    "id": "Q8",
    "statement": "For d = 10 with n_A = 640 and n_B = 384 the probabilities are P_A = 0.625 and P_B = 0.375.",
    "inputs": "n_A = 640, n_B = 384, L = 1024",
    "formula": "P_A = n_A / L, P_B = n_B / L"
  },
  {
    "id": "Q9",
    "statement": "With one non‑branching level in a depth‑5 tree the irregular leaf count is L_irr = 16.",
    "inputs": "depth d = 5, branching factors β_l = 2 for four levels and β = 1 for one level",
    "formula": "L_irr = product_{l=1}^{d} β_l"
  },
  {
    "id": "Q10",
    "statement": "For the irregular tree with L_irr = 16 and n_A = 10, n_B = 6 the probabilities are P_A = 0.625 and P_B = 0.375.",
    "inputs": "n_A = 10, n_B = 6, L_irr = 16",
    "formula": "P_A = n_A / L_irr, P_B = n_B / L_irr"
  },
  {
    "id": "Q11",
    "statement": "For the irregular tree with L_irr = 16 and n_A = 9, n_B = 7 the probabilities are P_A = 0.5625 and P_B = 0.4375.",
    "inputs": "n_A = 9, n_B = 7, L_irr = 16",
    "formula": "P_A = n_A / L_irr, P_B = n_B / L_irr"
  },
  {
    "id": "Q12",
    "statement": "Projected simulation cost for depth d = 10 is C_sim ≈ 1.024.",
    "inputs": "c_leaf = 0.001, L = 1024",
    "formula": "C_sim = c_leaf * L"
  }
]

## Script
```python
import math

# Expected values as strings
expected = {
    "Q1": "32",
    "Q2": "0.790569415",
    "Q3": "0.612372436",
    "Q4": "0.625",
    "Q5": "0.375",
    "Q6": "30",
    "Q7": "1024",
    "Q8_A": "0.625",
    "Q8_B": "0.375",
    "Q9": "16",
    "Q10_A": "0.625",
    "Q10_B": "0.375",
    "Q11_A": "0.5625",
    "Q11_B": "0.4375",
    "Q12": "1.024",
}

def fmt(val, exp_str):
    """Format val to the same number of decimal places as exp_str."""
    if "." in exp_str:
        nd = len(exp_str.split(".")[1])
        return f"{val:.{nd}f}"
    else:
        return str(int(round(val)))

def compare(comp_str, exp_str):
    return comp_str == exp_str

# Compute claims
results = {}

# Q1
L5 = 2**5
results["Q1"] = fmt(L5, expected["Q1"])

# Q2
a = math.sqrt(20/32)
results["Q2"] = fmt(a, expected["Q2"])

# Q3
b = math.sqrt(12/32)
results["Q3"] = fmt(b, expected["Q3"])

# Q4
P_A = a**2
results["Q4"] = fmt(P_A, expected["Q4"])

# Q5
P_B = 1 - P_A
results["Q5"] = fmt(P_B, expected["Q5"])

# Q6
D_C = 2**(4+1) - 2
results["Q6"] = fmt(D_C, expected["Q6"])

# Q7
L10 = 2**10
results["Q7"] = fmt(L10, expected["Q7"])

# Q8
P_A10 = 640/1024
P_B10 = 384/1024
results["Q8_A"] = fmt(P_A10, expected["Q8_A"])
results["Q8_B"] = fmt(P_B10, expected["Q8_B"])

# Q9
L_irr = (2**4) * 1  # four binary branches, one non‑branching level
results["Q9"] = fmt(L_irr, expected["Q9"])

# Q10
P_A_irr = 10/16
P_B_irr = 6/16
results["Q10_A"] = fmt(P_A_irr, expected["Q10_A"])
results["Q10_B"] = fmt(P_B_irr, expected["Q10_B"])

# Q11
P_A_irr2 = 9/16
P_B_irr2 = 7/16
results["Q11_A"] = fmt(P_A_irr2, expected["Q11_A"])
results["Q11_B"] = fmt(P_B_irr2, expected["Q11_B"])

# Q12
C_sim = 0.001 * 1024
results["Q12"] = fmt(C_sim, expected["Q12"])

# Print verification lines
print(f"CLAIM Q1: computed={results['Q1']} expected={expected['Q1']} match={compare(results['Q1'], expected['Q1'])}")
print(f"CLAIM Q2: computed={results['Q2']} expected={expected['Q2']} match={compare(results['Q2'], expected['Q2'])}")
print(f"CLAIM Q3: computed={results['Q3']} expected={expected['Q3']} match={compare(results['Q3'], expected['Q3'])}")
print(f"CLAIM Q4: computed={results['Q4']} expected={expected['Q4']} match={compare(results['Q4'], expected['Q4'])}")
print(f"CLAIM Q5: computed={results['Q5']} expected={expected['Q5']} match={compare(results['Q5'], expected['Q5'])}")
print(f"CLAIM Q6: computed={results['Q6']} expected={expected['Q6']} match={compare(results['Q6'], expected['Q6'])}")
print(f"CLAIM Q7: computed={results['Q7']} expected={expected['Q7']} match={compare(results['Q7'], expected['Q7'])}")
print(f"CLAIM Q8_A: computed={results['Q8_A']} expected={expected['Q8_A']} match={compare(results['Q8_A'], expected['Q8_A'])}")
print(f"CLAIM Q8_B: computed={results['Q8_B']} expected={expected['Q8_B']} match={compare(results['Q8_B'], expected['Q8_B'])}")
print(f"CLAIM Q9: computed={results['Q9']} expected={expected['Q9']} match={compare(results['Q9'], expected['Q9'])}")
print(f"CLAIM Q10_A: computed={results['Q10_A']} expected={expected['Q10_A']} match={compare(results['Q10_A'], expected['Q10_A'])}")
print(f"CLAIM Q10_B: computed={results['Q10_B']} expected={expected['Q10_B']} match={compare(results['Q10_B'], expected['Q10_B'])}")
print(f"CLAIM Q11_A: computed={results['Q11_A']} expected={expected['Q11_A']} match={compare(results['Q11_A'], expected['Q11_A'])}")
print(f"CLAIM Q11_B: computed={results['Q11_B']} expected={expected['Q11_B']} match={compare(results['Q11_B'], expected['Q11_B'])}")
print(f"CLAIM Q12: computed={results['Q12']} expected={expected['Q12']} match={compare(results['Q12'], expected['Q12'])}")

# Summary
total = len(expected)
matches = sum(1 for k in expected if compare(results.get(k.split('_')[0], ""), expected[k]))
print(f"VERIFICATION SUMMARY: {total} claims, {matches} match, {total - matches} mismatch")

```

## Execution output
```
CLAIM Q1: computed=32 expected=32 match=True
CLAIM Q2: computed=0.790569415 expected=0.790569415 match=True
CLAIM Q3: computed=0.612372436 expected=0.612372436 match=True
CLAIM Q4: computed=0.625 expected=0.625 match=True
CLAIM Q5: computed=0.375 expected=0.375 match=True
CLAIM Q6: computed=30 expected=30 match=True
CLAIM Q7: computed=1024 expected=1024 match=True
CLAIM Q8_A: computed=0.625 expected=0.625 match=True
CLAIM Q8_B: computed=0.375 expected=0.375 match=True
CLAIM Q9: computed=16 expected=16 match=True
CLAIM Q10_A: computed=0.625 expected=0.625 match=True
CLAIM Q10_B: computed=0.375 expected=0.375 match=True
CLAIM Q11_A: computed=0.5625 expected=0.5625 match=True
CLAIM Q11_B: computed=0.4375 expected=0.4375 match=True
CLAIM Q12: computed=1.024 expected=1.024 match=True
VERIFICATION SUMMARY: 15 claims, 9 match, 6 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 32 | 32 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 0.790569415 | 0.790569415 | - | match | 9 significant digits (as the paper states, at least 2) |
| Q3 | 0.612372436 | 0.612372436 | - | match | 9 significant digits (as the paper states, at least 2) |
| Q4 | 0.625 | 0.625 | - | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 0.375 | 0.375 | - | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 30 | 30 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 1024 | 1024 | - | match | 4 significant digits (as the paper states, at least 2) |
| Q8_A | 0.625 | 0.625 | - | match | 3 significant digits (as printed, at least 3) |
| Q8_B | 0.375 | 0.375 | - | match | 3 significant digits (as printed, at least 3) |
| Q9 | 16 | 16 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q10_A | 0.625 | 0.625 | - | match | 3 significant digits (as printed, at least 3) |
| Q10_B | 0.375 | 0.375 | - | match | 3 significant digits (as printed, at least 3) |
| Q11_A | 0.5625 | 0.5625 | - | match | 4 significant digits (as printed, at least 3) |
| Q11_B | 0.4375 | 0.4375 | - | match | 4 significant digits (as printed, at least 3) |
| Q12 | 1.024 | 1.024 | - | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 15.
