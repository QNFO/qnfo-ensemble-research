import math

def fmt(val, sig=6):
    """Format a float to the given number of significant digits."""
    if val == 0:
        return "0"
    # Determine order of magnitude
    order = int(math.floor(math.log10(abs(val))))
    digits = sig - order - 1
    fmt_str = "{:." + str(max(digits, 0)) + "f}"
    return fmt_str.format(val)

# Q1
R_10 = 2**10
expected_Q1 = 1024
match_Q1 = fmt(R_10) == fmt(expected_Q1)
print(f"CLAIM Q1: computed={R_10} expected={expected_Q1} match={'yes' if match_Q1 else 'no'}")

# Q2
n = 10
bytes_per_complex = 16
storage_pure = (2**n) * bytes_per_complex
expected_Q2 = 16384
match_Q2 = fmt(storage_pure) == fmt(expected_Q2)
print(f"CLAIM Q2: computed={storage_pure} expected={expected_Q2} match={'yes' if match_Q2 else 'no'}")

# Q3
storage_density = (4**n) * bytes_per_complex
expected_Q3 = 16777216
match_Q3 = fmt(storage_density) == fmt(expected_Q3)
print(f"CLAIM Q3: computed={storage_density} expected={expected_Q3} match={'yes' if match_Q3 else 'no'}")

# Q4
p = 0.5
E_F_0_5 = -p*math.log2(p) - (1-p)*math.log2(1-p)
expected_Q4 = 1.000000
match_Q4 = fmt(E_F_0_5, sig=7) == fmt(expected_Q4, sig=7)
print(f"CLAIM Q4: computed={E_F_0_5:.6f} expected={expected_Q4:.6f} match={'yes' if match_Q4 else 'no'}")

# Q5
p = 0.25
E_F_0_25 = -p*math.log2(p) - (1-p)*math.log2(1-p)
expected_Q5 = 0.811278
match_Q5 = fmt(E_F_0_25, sig=7) == fmt(expected_Q5, sig=7)
print(f"CLAIM Q5: computed={E_F_0_25:.6f} expected={expected_Q5:.6f} match={'yes' if match_Q5 else 'no'}")

# Q6
p = 0.9
E_F_0_9 = -p*math.log2(p) - (1-p)*math.log2(1-p)
expected_Q6 = 0.468996
match_Q6 = fmt(E_F_0_9, sig=7) == fmt(expected_Q6, sig=7)
print(f"CLAIM Q6: computed={E_F_0_9:.6f} expected={expected_Q6:.6f} match={'yes' if match_Q6 else 'no'}")

# Q7
p = 0.5
dE_dp = math.log2((1-p)/p)
expected_Q7 = 0.0
match_Q7 = fmt(dE_dp) == fmt(expected_Q7)
print(f"CLAIM Q7: computed={dE_dp} expected={expected_Q7} match={'yes' if match_Q7 else 'no'}")

# Q8
K = 21
M_sweep = K * (4**n) * bytes_per_complex
expected_Q8 = 352321536
match_Q8 = fmt(M_sweep) == fmt(expected_Q8)
print(f"CLAIM Q8: computed={M_sweep} expected={expected_Q8} match={'yes' if match_Q8 else 'no'}")

# Q9
E_F_vals = [0.811278, 1.000000, 0.468996]
E_F_avg = sum(E_F_vals) / 3.0
expected_Q9 = 0.760091
match_Q9 = fmt(E_F_avg, sig=7) == fmt(expected_Q9, sig=7)
print(f"CLAIM Q9: computed={E_F_avg:.6f} expected={expected_Q9:.6f} match={'yes' if match_Q9 else 'no'}")

# Q10
Sigma = R_10 * E_F_avg
expected_Q10 = 778.333
# compare with 6 significant digits as in the paper
match_Q10 = fmt(Sigma, sig=6) == fmt(expected_Q10, sig=6)
print(f"CLAIM Q10: computed={Sigma:.6f} expected={expected_Q10:.6f} match={'yes' if match_Q10 else 'no'}")

# Q11
e_DRAM = 1e-10
f_orch = 2
E_step = (4**n) * bytes_per_complex * e_DRAM * f_orch
expected_Q11 = 3.3554432e-3
match_Q11 = fmt(E_step, sig=8) == fmt(expected_Q11, sig=8)
print(f"CLAIM Q11: computed={E_step:.9f} expected={expected_Q11:.9f} match={'yes' if match_Q11 else 'no'}")

# Q12
S = 10000
E_workload = S * E_step
expected_Q12 = 33.554432
match_Q12 = fmt(E_workload, sig=8) == fmt(expected_Q12, sig=8)
print(f"CLAIM Q12: computed={E_workload:.6f} expected={expected_Q12:.6f} match={'yes' if match_Q12 else 'no'}")

# Q13
R_5 = 2**5
expected_Q13 = 32
match_Q13 = fmt(R_5) == fmt(expected_Q13)
print(f"CLAIM Q13: computed={R_5} expected={expected_Q13} match={'yes' if match_Q13 else 'no'}")

# Q14
factor = 3
E_lower = E_workload / factor
E_upper = E_workload * factor
# Expected range "11–101" (approximate). We'll compare rounded integers.
match_Q14 = (round(E_lower) == 11) and (round(E_upper) == 101)
print(f"CLAIM Q14: computed={E_lower:.6f}–{E_upper:.6f} expected=11–101 match={'yes' if match_Q14 else 'no'}")
