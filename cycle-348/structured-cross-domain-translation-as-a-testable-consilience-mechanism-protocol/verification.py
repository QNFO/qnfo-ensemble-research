# Compute and verify quantitative claims from the paper

def fmt(val, digits):
    """Format a number with given significant digits (as string)."""
    if isinstance(val, int):
        return str(val)
    # round to the specified number of decimal places
    return f"{round(val, digits):.{digits}f}".rstrip('0').rstrip('.') if digits > 0 else str(val)

# Claim Q1
N_rend = 10 * 4
exp_Q1 = "40"
calc_Q1 = fmt(N_rend, 0)
match_Q1 = calc_Q1 == exp_Q1

# Claim Q2
binom = 4 * (4 - 1) // 2
exp_Q2 = "6"
calc_Q2 = fmt(binom, 0)
match_Q2 = calc_Q2 == exp_Q2

# Claim Q3
N_hyp = 10 * binom
exp_Q3 = "60"
calc_Q3 = fmt(N_hyp, 0)
match_Q3 = calc_Q3 == exp_Q3

# Claim Q4
E_total = N_hyp * 3
exp_Q4 = "180"
calc_Q4 = fmt(E_total, 0)
match_Q4 = calc_Q4 == exp_Q4

# Claim Q5
T_rate_min = N_hyp * 5          # minutes
T_rate_h = T_rate_min / 60.0    # hours
exp_Q5 = "5.0"
calc_Q5 = fmt(T_rate_h, 1)
match_Q5 = calc_Q5 == exp_Q5

# Claim Q6
T_rate_3 = 3 * T_rate_h
exp_Q6 = "15.0"
calc_Q6 = fmt(T_rate_3, 1)
match_Q6 = calc_Q6 == exp_Q6

# Claim Q7
N0 = 10 * 2
exp_Q7 = "20"
calc_Q7 = fmt(N0, 0)
match_Q7 = calc_Q7 == exp_Q7

# Claim Q8
T_base_min = N0 * 5
T_base_h = T_base_min / 60.0
exp_Q8 = "1.67"
calc_Q8 = fmt(T_base_h, 2)
match_Q8 = calc_Q8 == exp_Q8

# Claim Q9
T_syn_min = 10 * 3 * 10
T_syn_h = T_syn_min / 60.0
exp_Q9 = "5.0"
calc_Q9 = fmt(T_syn_h, 1)
match_Q9 = calc_Q9 == exp_Q9

# Claim Q10
T_total = T_rate_3 + T_syn_h
exp_Q10 = "20.0"
calc_Q10 = fmt(T_total, 1)
match_Q10 = calc_Q10 == exp_Q10

# Claim Q11
N_rated = 0.4 * N_hyp
exp_Q11 = "24"
calc_Q11 = fmt(N_rated, 0)
match_Q11 = calc_Q11 == exp_Q11

# Claim Q12
T_rated_min = N_rated * 5 * 3
T_rated_h = T_rated_min / 60.0
exp_Q12 = "6.0"
calc_Q12 = fmt(T_rated_h, 1)
match_Q12 = calc_Q12 == exp_Q12

# Claim Q13
T_total_filt = T_rated_h + T_syn_h
exp_Q13 = "11.0"
calc_Q13 = fmt(T_total_filt, 1)
match_Q13 = calc_Q13 == exp_Q13

# Claim Q14
s = 4 / (4 + 1 + 2)
exp_Q14 = "0.571"
calc_Q14 = fmt(s, 3)
match_Q14 = calc_Q14 == exp_Q14

# Claim Q15
p0 = 0.05
m = 6
P_any = 1 - (1 - p0) ** m
exp_Q15 = "0.265"
calc_Q15 = fmt(P_any, 3)
match_Q15 = calc_Q15 == exp_Q15

# Claim Q16
sensitivity = 0.8
residual = p0 * (1 - sensitivity)
P_any_tested = 1 - (1 - residual) ** m
exp_Q16 = "0.059"
calc_Q16 = fmt(P_any_tested, 3)
match_Q16 = calc_Q16 == exp_Q16

# Print results
claims = [
    ("Q1", calc_Q1, exp_Q1, match_Q1),
    ("Q2", calc_Q2, exp_Q2, match_Q2),
    ("Q3", calc_Q3, exp_Q3, match_Q3),
    ("Q4", calc_Q4, exp_Q4, match_Q4),
    ("Q5", calc_Q5, exp_Q5, match_Q5),
    ("Q6", calc_Q6, exp_Q6, match_Q6),
    ("Q7", calc_Q7, exp_Q7, match_Q7),
    ("Q8", calc_Q8, exp_Q8, match_Q8),
    ("Q9", calc_Q9, exp_Q9, match_Q9),
    ("Q10", calc_Q10, exp_Q10, match_Q10),
    ("Q11", calc_Q11, exp_Q11, match_Q11),
    ("Q12", calc_Q12, exp_Q12, match_Q12),
    ("Q13", calc_Q13, exp_Q13, match_Q13),
    ("Q14", calc_Q14, exp_Q14, match_Q14),
    ("Q15", calc_Q15, exp_Q15, match_Q15),
    ("Q16", calc_Q16, exp_Q16, match_Q16),
]

for cid, comp, exp, ok in claims:
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if ok else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {sum(1 for _,_,_,ok in claims if ok)} match, {sum(1 for _,_,_,ok in claims if not ok)} mismatch")
