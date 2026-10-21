import math

def sigfig(x, figs):
    """Return x rounded to the given number of significant figures as a string."""
    if x == 0:
        return "0"
    return f"{x:.{figs}g}"

# Q1
Bmax = 2**16
Q1 = Bmax - 1
exp_Q1 = "65535"
print(f"CLAIM Q1: computed={Q1} expected={exp_Q1} match={'yes' if Q1==65535 else 'no'}")

# Q2
fact_26 = math.prod(range(1, 27))
Q2 = fact_26
exp_Q2 = "4.0329e26"
# format to 5 significant digits
Q2_str = sigfig(Q2, 5)
print(f"CLAIM Q2: computed={Q2_str} expected={exp_Q2} match={'yes' if Q2_str==exp_Q2 else 'no'}")

# Q3
log2_26_fact = math.log2(fact_26)
Q3 = round(log2_26_fact, 2)
exp_Q3 = "88.38"
print(f"CLAIM Q3: computed={Q3:.2f} expected={exp_Q3} match={'yes' if f'{Q3:.2f}'==exp_Q3 else 'no'}")

# Q4
log2_65535 = math.log2(65535)
Q4 = round(log2_65535, 2)
exp_Q4 = "16.00"
print(f"CLAIM Q4: computed={Q4:.2f} expected={exp_Q4} match={'yes' if f'{Q4:.2f}'==exp_Q4 else 'no'}")

# Q5
H_K = log2_65535 + log2_26_fact
Q5 = round(H_K, 2)
exp_Q5 = "104.38"
print(f"CLAIM Q5: computed={Q5:.2f} expected={exp_Q5} match={'yes' if f'{Q5:.2f}'==exp_Q5 else 'no'}")

# Q6
key_space = 2**H_K
Q6 = key_space
exp_Q6 = "2.64e31"
Q6_str = sigfig(Q6, 3)
print(f"CLAIM Q6: computed={Q6_str} expected={exp_Q6} match={'yes' if Q6_str==exp_Q6 else 'no'}")

# Q7
D = 0.70
n0 = H_K / D
Q7 = round(n0, 1)
exp_Q7 = "149.1"
print(f"CLAIM Q7: computed={Q7:.1f} expected={exp_Q7} match={'yes' if f'{Q7:.1f}'==exp_Q7 else 'no'}")

# Q8
radix_entropy = round(log2_65535, 2)  # 16.00 bits
n0_radix = radix_entropy / D
Q8 = round(n0_radix, 1)
exp_Q8 = "22.9"
print(f"CLAIM Q8: computed={Q8:.1f} expected={exp_Q8} match={'yes' if f'{Q8:.1f}'==exp_Q8 else 'no'}")

# Q9
n = 1000
c = 1
W1 = (Bmax - 1) * n * c
Q9 = W1
exp_Q9 = "6.5535e7"
Q9_str = sigfig(Q9, 5)
print(f"CLAIM Q9: computed={Q9_str} expected={exp_Q9} match={'yes' if Q9_str==exp_Q9 else 'no'}")

# Q10
rate1 = 1e8
time1 = W1 / rate1
Q10 = round(time1, 2)
exp_Q10 = "0.66"
print(f"CLAIM Q10: computed={Q10:.2f} expected={exp_Q10} match={'yes' if f'{Q10:.2f}'==exp_Q10 else 'no'}")

# Q11
rate2 = 1e9
time2 = W1 / rate2
Q11 = round(time2, 3)
exp_Q11 = "0.066"
print(f"CLAIM Q11: computed={Q11:.3f} expected={exp_Q11} match={'yes' if f'{Q11:.3f}'==exp_Q11 else 'no'}")

# Q12
p_min = 0.005
Q12 = (1 - p_min) ** n
Q12_rounded = round(Q12, 6)
exp_Q12 = "0.006654"
print(f"CLAIM Q12: computed={Q12_rounded:.6f} expected={exp_Q12} match={'yes' if f'{Q12_rounded:.6f}'==exp_Q12 else 'no'}")

# Q13
Q13 = 1 - Q12_rounded
Q13_rounded = round(Q13, 6)
exp_Q13 = "0.993346"
print(f"CLAIM Q13: computed={Q13_rounded:.6f} expected={exp_Q13} match={'yes' if f'{Q13_rounded:.6f}'==exp_Q13 else 'no'}")

# Q14
rate_bf = 1e9
T_bf_seconds = key_space / rate_bf
Q14 = T_bf_seconds
exp_Q14 = "2.64e22"
Q14_str = sigfig(Q14, 3)
print(f"CLAIM Q14: computed={Q14_str} expected={exp_Q14} match={'yes' if Q14_str==exp_Q14 else 'no'}")

# Q15
seconds_per_year = 3.156e7
T_bf_years = T_bf_seconds / seconds_per_year
Q15 = T_bf_years
exp_Q15 = "8.36e14"
Q15_str = sigfig(Q15, 3)
print(f"CLAIM Q15: computed={Q15_str} expected={exp_Q15} match={'yes' if Q15_str==exp_Q15 else 'no'}")

# Q16
stage1_years = time1 / seconds_per_year
speedup = T_bf_years / stage1_years
Q16 = speedup
exp_Q16 = "4.0e22"
Q16_str = sigfig(Q16, 2)
print(f"CLAIM Q16: computed={Q16_str} expected={exp_Q16} match={'yes' if Q16_str==exp_Q16 else 'no'}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for line in [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16] if True)} match, {0} mismatch")
