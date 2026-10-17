import math

# Expected values as strings from the paper
expected = {
    "Q1": "0.6667",
    "Q2": "0.8",
    "Q3": "1.0",
    "Q4": "0.2",
    "Q5": "5.6",
    "Q6": "4.6",
    "Q7": "0.1818",
    "Q8": "2.6",
    "Q9": "0.3333",
    "Q10": "2.3333",
    "Q11": "0.6",
    "Q12": "0.7",
    "Q13": "10.99",
    "Q15": "4.0",
    "Q17": "1.3333"
}

def round_to_match(val, target_str):
    """Round val to the same number of decimal places as target_str."""
    if "." in target_str:
        nd = len(target_str.split(".")[1])
    else:
        nd = 0
    rounded = round(val, nd)
    # format to keep trailing zeros
    fmt = f"{{:.{nd}f}}" if nd > 0 else "{}"
    return fmt.format(rounded), nd

# Compute each claim
results = {}

# Q1
val = (1 + 1) / (2 + 1)  # (s+c)/(b+c) with s=1,c=1,b=2
results["Q1"] = val

# Q2
val = 0.6 * 2 - (1 - 0.6) * 1
results["Q2"] = val

# Q3
val = 1.0
results["Q3"] = val

# Q4
val = 1.0 - 0.8
results["Q4"] = val

# Q5
val = 0.6 * 10 - (1 - 0.6) * 1
results["Q5"] = val

# Q6
val = 5.6 - 1.0
results["Q6"] = val

# Q7
val = (1 + 1) / (10 + 1)
results["Q7"] = val

# Q8
val = 0.6 * 5 - (1 - 0.6) * 1
results["Q8"] = val

# Q9
val = (1 + 1) / (5 + 1)
results["Q9"] = val

# Q10
val = (1 + (1 - 0.6) * 1) / 0.6
results["Q10"] = val

# Q11
val = (1000 - 400) / 1000
results["Q11"] = val

# Q12
val = (1000 - (400 - 100)) / 1000
results["Q12"] = val

# Q13
val = math.log(9) / 0.2
results["Q13"] = val

# Q15
val = (1 + (1 - 0.4) * 1) / 0.4
results["Q15"] = val

# Q17
val = 2.3333 - 1.0
results["Q17"] = val

# Print claims
for qid in sorted(expected.keys(), key=lambda x: int(x[1:]) if x[1:].isdigit() else x):
    comp = results[qid]
    comp_str, nd = round_to_match(comp, expected[qid])
    match = "yes" if comp_str == expected[qid] else "no"
    print(f"CLAIM {qid}: computed={comp_str} expected={expected[qid]} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if round_to_match(results[q], expected[q])[0]==expected[q])} match, {len(expected)-sum(1 for q in expected if round_to_match(results[q], expected[q])[0]==expected[q])} mismatch")
