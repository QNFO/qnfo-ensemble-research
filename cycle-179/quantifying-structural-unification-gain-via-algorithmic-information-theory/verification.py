import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    else:
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

claims = {
    "Q1": {"inputs": (3.1, 2.9), "formula": lambda a,b: (a + b) / 2, "expected": "3.0", "sig": 2},
    "Q2": {"inputs": (65.9, 62.0), "formula": lambda p1,p2: ((100 - p1) + (100 - p2)) / 2, "expected": "36.05", "sig": 4},
    "Q3": {"inputs": (3.3, 0.1, 9.1, 9.6, 9.6), "formula": lambda *vals: sum(vals) / len(vals), "expected": "6.34", "sig": 3},
    "Q4": {"inputs": (0.45, 1.20), "formula": lambda a,b: a / b, "expected": "0.375", "sig": 3},
    "Q5": {"inputs": (0.10, 10), "formula": lambda rate, hrs: rate * hrs, "expected": "1.00", "sig": 3},
}

for cid, data in claims.items():
    computed = data["formula"](*data["inputs"])
    # high-precision display (at least 8 significant digits)
    computed_str = f"{computed:.10g}"
    # round to required significant figures for comparison
    rounded = round_sig(computed, data["sig"])
    # format rounded to match expected string length (preserve trailing zeros)
    if '.' in data["expected"]:
        # determine number of decimal places in expected
        dec_places = len(data["expected"].split('.')[1])
        rounded_str = f"{rounded:.{dec_places}f}"
    else:
        rounded_str = str(int(round(rounded)))
    match = "yes" if rounded_str == data["expected"] else "no"
    print(f"CLAIM {cid}: computed={computed_str} expected={data['expected']} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for d in claims.values() if round_sig(d['formula'](*d['inputs']), d['sig']) == float(d['expected']))} match, {len(claims) - sum(1 for d in claims.values() if round_sig(d['formula'](*d['inputs']), d['sig']) == float(d['expected']))} mismatch")
