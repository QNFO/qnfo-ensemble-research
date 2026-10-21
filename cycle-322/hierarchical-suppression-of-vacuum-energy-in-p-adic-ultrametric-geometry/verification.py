import math
from decimal import Decimal, getcontext

getcontext().prec = 50  # high precision for tiny numbers

def sci(val, sig=3):
    """Return scientific notation string with given significant digits."""
    if val == 0:
        return f"0e0"
    exponent = int(math.floor(math.log10(abs(val))))
    mantissa = val / (10 ** exponent)
    fmt = f"{{:.{sig-1}f}}e{{:+d}}"
    return fmt.format(mantissa, exponent)

def compare_numeric(comp, exp, tol=1e-3):
    """Return True if relative difference <= tol."""
    if exp == 0:
        return abs(comp) < tol
    return abs(comp - exp) / abs(exp) <= tol

# Claim Q1
N_q1 = 120 / math.log10(3)
expected_q1 = 251.5
match_q1 = compare_numeric(N_q1, expected_q1, tol=5e-2)  # tolerance 0.05
print(f"CLAIM Q1: computed={N_q1:.8g} expected={expected_q1} match={'yes' if match_q1 else 'no'}")

# Claim Q2
p = Decimal(3)
N = Decimal(252)
supp_q2 = p ** (-N)  # Decimal power
computed_q2 = float(supp_q2)  # may underflow to 0, use Decimal string instead
expected_q2 = 5.83e-121
# compare using Decimal
match_q2 = compare_numeric(float(supp_q2), expected_q2, tol=1e-2)
print(f"CLAIM Q2: computed={sci(float(supp_q2),3)} expected=5.83e-121 match={'yes' if match_q2 else 'no'}")

# Claim Q3
exp_q3 = -252 * math.log10(3)
expected_q3 = -120.2346
match_q3 = compare_numeric(exp_q3, expected_q3, tol=1e-4)
print(f"CLAIM Q3: computed={exp_q3:.6f} expected={expected_q3} match={'yes' if match_q3 else 'no'}")

# Claim Q4
N_q4 = 120 / math.log10(2)
N_q4_rounded = round(N_q4)  # 399
supp_q4 = 2 ** (-N_q4_rounded)
exp_q4 = -N_q4_rounded * math.log10(2)
expected_exp_q4 = -120.111
expected_supp_q4 = 7.8e-121
match_q4 = compare_numeric(exp_q4, expected_exp_q4, tol=1e-3) and compare_numeric(supp_q4, expected_supp_q4, tol=1e-2)
print(f"CLAIM Q4: computed={exp_q4:.6f} expected={expected_exp_q4} match={'yes' if match_q4 else 'no'}")

# Claim Q5
N_q5 = 120 / math.log10(5)
N_q5_rounded = round(N_q5)  # 172
supp_q5 = 5 ** (-N_q5_rounded)
exp_q5 = -N_q5_rounded * math.log10(5)
expected_exp_q5 = -120.222
expected_supp_q5 = 6.0e-121
match_q5 = compare_numeric(exp_q5, expected_exp_q5, tol=1e-3) and compare_numeric(supp_q5, expected_supp_q5, tol=1e-2)
print(f"CLAIM Q5: computed={exp_q5:.6f} expected={expected_exp_q5} match={'yes' if match_q5 else 'no'}")

# Claim Q6
N_q6 = 120 / math.log10(7)
N_q6_rounded = round(N_q6)  # 142
supp_q6 = 7 ** (-N_q6_rounded)
exp_q6 = -N_q6_rounded * math.log10(7)
expected_exp_q6 = -120.004
expected_supp_q6 = 9.9e-121
match_q6 = compare_numeric(exp_q6, expected_exp_q6, tol=1e-3) and compare_numeric(supp_q6, expected_supp_q6, tol=1e-2)
print(f"CLAIM Q6: computed={exp_q6:.6f} expected={expected_exp_q6} match={'yes' if match_q6 else 'no'}")

# Claim Q7
sum_q7 = sum(3 ** (-n) for n in range(-5, 1))  # n from -5 to 0
rho_q7 = 0.5 * sum_q7
expected_sum = 364
expected_rho = 182
match_q7 = (abs(sum_q7 - expected_sum) < 1e-9) and (abs(rho_q7 - expected_rho) < 1e-9)
print(f"CLAIM Q7: computed={rho_q7:.6f} expected={expected_rho} match={'yes' if match_q7 else 'no'}")

# Claim Q8
logp_min = 120 / 121
logp_max = 120 / 119
p_min = 10 ** logp_min
p_max = 10 ** logp_max
expected_logp_min = 0.9917
expected_logp_max = 1.0084
match_q8 = (abs(logp_min - expected_logp_min) < 1e-4) and (abs(logp_max - expected_logp_max) < 1e-4)
print(f"CLAIM Q8: computed_min={logp_min:.4f} computed_max={logp_max:.4f} expected_min={expected_logp_min} expected_max={expected_logp_max} match={'yes' if match_q8 else 'no'}")

# Claim Q9
exp_q9 = -172 * math.log10(5) - 80 * math.log10(3)
expected_exp_q9 = -158.39
match_q9 = compare_numeric(exp_q9, expected_exp_q9, tol=1e-3)
print(f"CLAIM Q9: computed={exp_q9:.3f} expected={expected_exp_q9} match={'yes' if match_q9 else 'no'}")

print(f"VERIFICATION SUMMARY: 9 claims, {sum([match_q1, match_q2, match_q3, match_q4, match_q5, match_q6, match_q7, match_q8, match_q9])} match, {9 - sum([match_q1, match_q2, match_q3, match_q4, match_q5, match_q6, match_q7, match_q8, match_q9])} mismatch")
