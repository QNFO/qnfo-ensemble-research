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
