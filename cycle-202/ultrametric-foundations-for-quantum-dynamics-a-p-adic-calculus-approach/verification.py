import math

def round_to_str(value, fmt):
    """Round value to the number of decimal places in fmt string and return as string."""
    if '.' in fmt:
        decimals = len(fmt.split('.')[1])
        return f"{round(value, decimals):.{decimals}f}"
    else:
        return str(int(round(value)))

# Inputs
sigma2 = 0.122
mu = 0.693
N = 1000

# Expected values as strings from the paper
expected = {
    "Q1": "0.349",
    "Q2": "0.503",
    "Q3": "0.176",
    "Q4": "31.62",
    "Q5": "45.6",
    "Q6": "0.158",
    "Q7": "0.194",
    "Q8": "True",   # Boolean window inclusion
    "Q9": "0.176"
}

# Computations
sigma = math.sqrt(sigma2)                     # Q1
cv = sigma / mu                               # Q2
R = sigma2 / mu                               # Q3
sqrtN = math.sqrt(N)                         # Q4
factor = sqrtN / mu                           # Q5
lower = 0.9 * R                               # Q6
upper = 1.1 * R                               # Q7
window_ok = lower <= R <= upper               # Q8
cv2_mu = (cv ** 2) * mu                       # Q9

# Prepare computed strings
computed = {
    "Q1": round_to_str(sigma, expected["Q1"]),
    "Q2": round_to_str(cv, expected["Q2"]),
    "Q3": round_to_str(R, expected["Q3"]),
    "Q4": round_to_str(sqrtN, expected["Q4"]),
    "Q5": round_to_str(factor, expected["Q5"]),
    "Q6": round_to_str(lower, expected["Q6"]),
    "Q7": round_to_str(upper, expected["Q7"]),
    "Q8": str(window_ok),
    "Q9": round_to_str(cv2_mu, expected["Q9"])
}

# Print results
for qid in ["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9"]:
    comp = computed[qid]
    exp = expected[qid]
    match = "yes" if comp == exp else "no"
    print(f"CLAIM {qid}: computed={comp} expected={exp} match={match}")

print(f"VERIFICATION SUMMARY: {len(expected)} claims, {sum(1 for q in expected if computed[q]==expected[q])} match, {sum(1 for q in expected if computed[q]!=expected[q])} mismatch")
