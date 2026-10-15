import math

k = 1.380649e-23
T = 300.0
ln2 = math.log(2)  # use exact ln 2; paper states 0.6931472

kTln2 = k * T * ln2

claims = []

# Q1
computed = k * T * ln2
claims.append(("Q1", computed, "2.871e-21"))

# Q2
computed = 100 * kTln2
claims.append(("Q2", computed, "2.871e-19"))

# Q3
computed = 1000 * kTln2
claims.append(("Q3", computed, "2.871e-18"))

# Q4
computed = 21 * kTln2
claims.append(("Q4", computed, "6.029e-20"))

# Q5
computed = (1000000 * 100) / 21
claims.append(("Q5", computed, "4.762e6"))

# Q6
computed = (1000000 * 1) / 21
claims.append(("Q6", computed, "4.76e4"))

# Q7
computed = 1000 * 6.029e-20
claims.append(("Q7", computed, "6.0e-17"))

sig = {"Q1": 4, "Q2": 4, "Q3": 4, "Q4": 4, "Q5": 4, "Q6": 3, "Q7": 2}

def round_sig(x, n):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

match_count = 0
for cid, computed, expected_str in claims:
    expected = float(expected_str)
    c_rounded = round_sig(computed, sig[cid])
    match = "yes" if abs(c_rounded - expected) <= abs(expected) * 1e-3 + 1e-300 else "no"
    if match == "yes":
        match_count += 1
    print(f"CLAIM {cid}: computed={computed:.8e} expected={expected_str} match={match}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")
