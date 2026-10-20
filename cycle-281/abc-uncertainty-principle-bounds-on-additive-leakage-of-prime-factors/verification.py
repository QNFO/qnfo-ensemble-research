import math

def round_to_match(value, expected_str):
    """Round value to the same number of decimal places as in expected_str."""
    if '.' in expected_str:
        dec_places = len(expected_str.split('.')[1])
        fmt = f"{{:.{dec_places}f}}"
        return fmt.format(value)
    else:
        # integer expected
        return str(int(round(value)))

def check_match(computed, expected_str):
    """Return 'yes' if rounded computed matches expected string, else 'no'."""
    rounded = round_to_match(computed, expected_str)
    return 'yes' if rounded == expected_str else 'no', rounded

claims = [
    # Q1
    ("Q1", lambda: math.log2(1/(0.5)), "1"),
    # Q2
    ("Q2", lambda: 1 - 0.40, "0.60"),
    # Q3
    ("Q3", lambda: math.log2(1/(0.5)), "1"),
    # Q4
    ("Q4", lambda: math.log2(1/(0.5)) * 0.60, "0.60"),
    # Q5
    ("Q5", lambda: 0.60, "0.60"),
    # Q6
    ("Q6", lambda: math.log2(1/0.8), "0.321928"),
    # Q7
    ("Q7", lambda: 0.60 * math.log2(1/0.8), "0.193157"),
    # Q8
    ("Q8", lambda: 0.60 * math.log2(1/0.9), "0.091202"),
    # Q9
    ("Q9", lambda: 0.60 * math.log2(1/0.99), "0.008613"),
    # Q10
    ("Q10", lambda: 0.60 * 1 + 0.2, "0.80"),
    # Q11
    ("Q11", lambda: (2 * math.pi) / math.log(2), "9.06"),
    # Q12
    ("Q12", lambda: 0.60 * ((2 * math.pi) / math.log(2)), "5.44"),
    # Q13
    ("Q13", lambda: 8 * (0.05 ** 2) * 1, "0.02"),
    # Q14
    ("Q14", lambda: -0.02 * math.log2(0.02) - 0.98 * math.log2(0.98), "0.112"),
    # Q15
    ("Q15", lambda: 15000 + 10000, "25000"),
]

for cid, func, expected in claims:
    computed = func()
    match, rounded = check_match(computed, expected)
    print(f"CLAIM {cid}: computed={rounded} expected={expected} match={match}")
print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,_,e in claims if check_match(_, e)[0]=='yes') } match, {sum(1 for _,_,e in claims if check_match(_, e)[0]=='no') } mismatch")
