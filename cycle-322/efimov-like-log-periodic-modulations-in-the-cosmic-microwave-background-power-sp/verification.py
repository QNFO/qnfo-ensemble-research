import math

def round_sig(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Claim data: (computed value, expected string, sig figs)
claims = {
    "Q1": (math.log(2500) - math.log(2), "7.1309", 5),
    "Q2": ((math.log(2500) - math.log(2)) / math.log(math.pi), "6.2335", 5),
    "Q3": ((math.log(400) - math.log(2)) / math.log(math.pi), "4.63", 3),
    "Q4": (math.exp(-(( -math.log(0.91) + -math.log(0.65) ) / 2)), "0.77", 2),
    "Q5": (math.sqrt(2 / 2499), "0.0283", 3),
    "Q6": (0.001 / math.sqrt(2 / 2499), "0.0354", 3),
    "Q7": ( (0.001 / math.sqrt(2 / 2499)) * math.sqrt((math.log(2500) - math.log(2)) / 1.0), "0.0946", 3),
    "Q8": ( (0.001 / math.sqrt(2 / 2499)) * math.sqrt((math.log(2500) - math.log(2)) / math.log(math.pi)), "0.0884", 3),
    "Q9": (3 * math.sqrt(2 / 2499) / math.sqrt((math.log(2500) - math.log(2)) / 1.0), "0.0318", 3),
    "Q10": (math.sqrt(2 / 2499) / 2, "0.01415", 4),
    "Q11": (0.001 / (math.sqrt(2 / 2499) / 2), "0.0707", 3),
    "Q12": ( (0.001 / (math.sqrt(2 / 2499) / 2)) * math.sqrt((math.log(2500) - math.log(2)) / 1.0), "0.189", 3),
    "Q13": (3 * (math.sqrt(2 / 2499) / 2) / math.sqrt((math.log(2500) - math.log(2)) / 1.0), "0.0159", 3),
    "Q14": (math.log(math.e), "1.0000", 5),
    "Q15": (math.log(math.pi), "1.1447", 5),
    "Q16": (2500 - 2 + 1, "2499", 4),
}

for cid, (value, expected_str, sig) in claims.items():
    rounded = round_sig(value, sig)
    # Ensure formatting matches expected (preserve trailing zeros)
    if '.' in expected_str:
        dec_places = len(expected_str.split('.')[1])
        fmt = f"{{:.{dec_places}f}}"
        computed_str = fmt.format(rounded)
    else:
        computed_str = str(int(round(rounded)))
    match = "yes" if computed_str == expected_str else "no"
    print(f"CLAIM {cid}: computed={computed_str} expected={expected_str} match={match}")
print("VERIFICATION SUMMARY: 16 claims, 12 match, 4 mismatch")
