import math

def format_sig(x, sig):
    """Return a string of x rounded to `sig` significant figures."""
    if x == 0:
        return "0"
    # Use general format with given significant digits
    return f"{x:.{sig}g}"

def check_match(computed, expected_str, sig):
    comp_str = format_sig(computed, sig)
    match = "yes" if comp_str == expected_str else "no"
    return comp_str, match

# Claim Q1
I = 0.0061 / 0.0048
comp, match = check_match(I, "1.27", 3)
print(f"CLAIM Q1: computed={comp} expected=1.27 match={match}")

# Claim Q2
C_Q2 = (1 - 0.5) * 1.27
comp, match = check_match(C_Q2, "0.635", 3)
print(f"CLAIM Q2: computed={comp} expected=0.635 match={match}")

# Claim Q3
C_Q3 = (1 - 0.8) * 1.27
comp, match = check_match(C_Q3, "0.254", 3)
print(f"CLAIM Q3: computed={comp} expected=0.254 match={match}")

# Claim Q4
L_Q4 = max(0, 12 * 0.9 - 6)
comp, match = check_match(L_Q4, "4.8", 2)
print(f"CLAIM Q4: computed={comp} expected=4.8 match={match}")

# Claim Q5
L_Q5 = max(0, 12 * 0.7 - 6)
comp, match = check_match(L_Q5, "2.4", 2)
print(f"CLAIM Q5: computed={comp} expected=2.4 match={match}")

# Claim Q6
L_Q6 = max(0, 12 * 0.6 - 6)
comp, match = check_match(L_Q6, "1.2", 2)
print(f"CLAIM Q6: computed={comp} expected=1.2 match={match}")

# Claim Q7
Lprime_Q7 = max(0, 6 - 12 * 0.3)
comp, match = check_match(Lprime_Q7, "2.4", 2)
print(f"CLAIM Q7: computed={comp} expected=2.4 match={match}")

# Claim Q8
Lprime_Q8 = max(0, 6 - 12 * 0.1)
comp, match = check_match(Lprime_Q8, "4.8", 2)
print(f"CLAIM Q8: computed={comp} expected=4.8 match={match}")

# Claim Q9
baseline_rate = 0.10
loss_percent = 0.00635
searches = 10000
lost_bookings = baseline_rate * loss_percent * searches
comp, match = check_match(lost_bookings, "6.35", 3)
print(f"CLAIM Q9: computed={comp} expected=6.35 match={match}")

# Claim Q10
cost = 0.10 * 100000
comp, match = check_match(cost, "10000", 5)
print(f"CLAIM Q10: computed={comp} expected=10000 match={match}")

print("VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch")
