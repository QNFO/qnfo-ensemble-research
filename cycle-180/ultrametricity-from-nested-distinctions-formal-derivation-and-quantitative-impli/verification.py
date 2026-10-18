import math

def round_sig(x, sig):
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

def format_sig(x, sig):
    # Use general format with specified significant figures
    fmt = "{{:.{}g}}".format(sig)
    return fmt.format(x)

claims = []

# Q1
N0 = 2.0e5
f = 0.17
delta_N = f * N0
computed_Q1 = delta_N
expected_Q1 = "3.4e4"
sig_Q1 = 2
match_Q1 = format_sig(round_sig(computed_Q1, sig_Q1), sig_Q1) == expected_Q1
claims.append(("Q1", computed_Q1, expected_Q1, match_Q1))

# Q2
N1 = N0 - delta_N
computed_Q2 = N1
expected_Q2 = "1.66e5"
sig_Q2 = 3
match_Q2 = format_sig(round_sig(computed_Q2, sig_Q2), sig_Q2) == expected_Q2
claims.append(("Q2", computed_Q2, expected_Q2, match_Q2))

# Q3
n = 1e6
E = n ** 1.5
computed_Q3 = E
expected_Q3 = "1.0e9"
sig_Q3 = 2
match_Q3 = format_sig(round_sig(computed_Q3, sig_Q3), sig_Q3) == expected_Q3
claims.append(("Q3", computed_Q3, expected_Q3, match_Q3))

# Q4
v = 9
R = 1e4
p = v / R
computed_Q4 = p
expected_Q4 = "9e-4"
sig_Q4 = 1
match_Q4 = format_sig(round_sig(computed_Q4, sig_Q4), sig_Q4) == expected_Q4
claims.append(("Q4", computed_Q4, expected_Q4, match_Q4))

# Q5
P = 10
T = 1000
total_trials = P * T
computed_Q5 = total_trials
expected_Q5 = "1e4"
sig_Q5 = 1
match_Q5 = format_sig(round_sig(computed_Q5, sig_Q5), sig_Q5) == expected_Q5
claims.append(("Q5", computed_Q5, expected_Q5, match_Q5))

# Q6
t = 0.5
total_time = total_trials * t
computed_Q6 = total_time
expected_Q6 = "5000"
# For a plain integer we treat sig figs as full precision
match_Q6 = int(round(computed_Q6)) == int(expected_Q6)
claims.append(("Q6", computed_Q6, expected_Q6, match_Q6))

# Output results
match_count = 0
for cid, comp, exp, ok in claims:
    print(f"CLAIM {cid}: computed={format_sig(comp, 8)} expected={exp} match={'yes' if ok else 'no'}")
    if ok:
        match_count += 1

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims)-match_count} mismatch")
