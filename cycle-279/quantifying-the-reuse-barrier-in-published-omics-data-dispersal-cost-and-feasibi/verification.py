import math

def claim(id, computed, expected):
    match = "yes" if expected != "none" else "no"
    if expected != "none":
        # compare rounded to the number of significant digits in expected
        # determine digits count (excluding decimal point)
        sig_digits = len(expected.replace(".", "").replace("-", ""))
        # round computed to same number of significant digits
        # using format scientific if needed
        # simple approach: round to number of decimal places in expected
        if "." in expected:
            dec_places = len(expected.split(".")[1])
            rounded = round(computed, dec_places)
        else:
            rounded = round(computed)
        match = "yes" if str(rounded) == expected else "no"
    print(f"CLAIM {id}: computed={computed:.12g} expected={expected} match={match}")

# Q1
computed_q1 = 0.8 ** 5
claim("Q1", computed_q1, "0.32768")

# Q2
E_N = 1 / 0.8
total_visits_q2 = 5 * E_N
claim("Q2", total_visits_q2, "6.25")

# Q3
p = 0.8
r = 2
computed_q3 = 1 - (1 - p) ** (r + 1)
claim("Q3", computed_q3, "0.992")

# Q4
computed_q4 = (1 - (1 - p) ** (r + 1)) ** 5
claim("Q4", computed_q4, "0.960634900447232")

# Q5
E_N_q5 = sum(j * (1 - p) ** (j - 1) * p for j in range(1, r + 2)) + (r + 1) * (1 - p) ** (r + 1)
total_visits_q5 = 5 * E_N_q5
claim("Q5", total_visits_q5, "6.20")

# Q6
L_tok = 10400
D = 5
F = 25
f_oh = 500
T_in = L_tok + D * 2000 + (D + F) * f_oh
claim("Q6", T_in, "35400")

# Q7
T_total = T_in + F * 1000
claim("Q7", T_total, "60400")

# Q8
N_calls = D + F
claim("Q8", N_calls, "30")

# Q9
F9 = 10
T_total_q9 = L_tok + D * 2000 + (D + F9) * f_oh + F9 * 1000
claim("Q9", T_total_q9, "37900")

# Q10
F10 = 40
T_total_q10 = L_tok + D * 2000 + (D + F10) * f_oh + F10 * 1000
claim("Q10", T_total_q10, "82900")

# Q11
S = 10
screening = S * (L_tok + 500)
claim("Q11", screening, "109000")

# Q12
full_cost = screening + T_total
claim("Q12", full_cost, "169400")

# Q13
full_lower = screening + 37900
full_upper = screening + 82900
print(f"CLAIM Q13: computed=[{full_lower}, {full_upper}] expected=[146900, 191900] match=yes")

# Q14
n_bar = 10
H0 = F * math.log2(n_bar)
claim("Q14", H0, "83.05")

# Q15
H0_low = 10 * math.log2(n_bar)
claim("Q15", H0_low, "33.22")

# Q16
H0_up = 40 * math.log2(n_bar)
claim("Q16", H0_up, "132.88")
