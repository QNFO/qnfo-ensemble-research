import math
from decimal import Decimal, getcontext

# Set high precision for very small numbers
getcontext().prec = 30

def fmt_sig(x, sig):
    """Format number x with sig significant digits in scientific notation."""
    if x == 0:
        return "0e0"
    # Use Decimal for consistent formatting
    d = Decimal(x)
    # Normalize to scientific notation
    exponent = d.adjusted()  # exponent in base 10
    mantissa = d.scaleb(-exponent).normalize()
    # Round mantissa to required sig digits
    mantissa = mantissa.quantize(Decimal(1) / (Decimal(10) ** (sig - 1)))
    # Remove trailing zeros in mantissa
    mant_str = format(mantissa, 'f').rstrip('0').rstrip('.')
    return f"{mant_str}e{exponent}"

# Claim Q1
P_q = 1e-12 * 1e6
expected_Q1 = "1e-6"
computed_Q1 = P_q
match_Q1 = fmt_sig(computed_Q1, 1) == expected_Q1
print(f"CLAIM Q1: computed={computed_Q1:.8g} expected={expected_Q1} match={'yes' if match_Q1 else 'no'}")

# Claim Q2
alpha = 0.1
p_th = 1e-2
p0 = 1e-3
DeltaT_crit = (1/alpha) * math.log(p_th / p0)
expected_Q2 = "23.03"
computed_Q2 = DeltaT_crit
match_Q2 = fmt_sig(computed_Q2, 4) == expected_Q2
print(f"CLAIM Q2: computed={computed_Q2:.5f} expected={expected_Q2} match={'yes' if match_Q2 else 'no'}")

# Claim Q3
R_th = 5.0
P_q_max = DeltaT_crit / R_th
expected_Q3 = "4.61"
computed_Q3 = P_q_max
match_Q3 = fmt_sig(computed_Q3, 3) == expected_Q3
print(f"CLAIM Q3: computed={computed_Q3:.5f} expected={expected_Q3} match={'yes' if match_Q3 else 'no'}")

# Claim Q4
P_c = 1.0
N_max = P_c / P_q
expected_Q4 = "1e6"
computed_Q4 = N_max
match_Q4 = fmt_sig(computed_Q4, 1) == expected_Q4
print(f"CLAIM Q4: computed={computed_Q4:.5g} expected={expected_Q4} match={'yes' if match_Q4 else 'no'}")

# Claim Q5
d_max = math.sqrt(N_max)
expected_Q5 = "1e3"
computed_Q5 = d_max
match_Q5 = fmt_sig(computed_Q5, 1) == expected_Q5
print(f"CLAIM Q5: computed={computed_Q5:.5g} expected={expected_Q5} match={'yes' if match_Q5 else 'no'}")

# Claim Q6
A = 0.1
p = 1e-3
p_th = 1e-2
d = 1000
exponent = (d + 1) / 2
p_L = A * (p / p_th) ** exponent
expected_Q6 = "1e-501"
computed_Q6 = p_L
# Use 1 significant digit for comparison
match_Q6 = fmt_sig(computed_Q6, 1) == expected_Q6
print(f"CLAIM Q6: computed={computed_Q6:.5e} expected={expected_Q6} match={'yes' if match_Q6 else 'no'}")

# Claim Q7
q_tot = 1.5e-12
c = 2e-3
v = 1e-12
DeltaT = q_tot / (c * v)
expected_Q7 = "7.5e2"
computed_Q7 = DeltaT
match_Q7 = fmt_sig(computed_Q7, 2) == expected_Q7
print(f"CLAIM Q7: computed={computed_Q7:.5g} expected={expected_Q7} match={'yes' if match_Q7 else 'no'}")

# Claim Q8
T0 = 0.02
T = T0 + DeltaT
expected_Q8 = "750"
computed_T = T
match_Q8 = fmt_sig(computed_T, 3) == expected_Q8
print(f"CLAIM Q8: computed={computed_T:.5g} expected={expected_Q8} match={'yes' if match_Q8 else 'no'}")

# Claim Q9
DeltaE = 5e-20
kB = 1.38e-23
ratio = DeltaE / (kB * T)
expected_Q9 = "4.830"
computed_Q9 = ratio
match_Q9 = fmt_sig(computed_Q9, 4) == expected_Q9
print(f"CLAIM Q9: computed={computed_Q9:.5f} expected={expected_Q9} match={'yes' if match_Q9 else 'no'}")

# Claim Q10
p0 = 1e-4
exponent = ratio
p_heat = p0 * math.exp(exponent)
expected_Q10 = "1.25e-2"
computed_Q10 = p_heat
match_Q10 = fmt_sig(computed_Q10, 3) == expected_Q10
print(f"CLAIM Q10: computed={computed_Q10:.5g} expected={expected_Q10} match={'yes' if match_Q10 else 'no'}")

# Claim Q11
eta = 0.5
beta = 10
gamma = 2
P_q_eff = eta * P_q / (beta * gamma)
expected_Q11 = "2.5e-8"
computed_Q11 = P_q_eff
match_Q11 = fmt_sig(computed_Q11, 2) == expected_Q11
print(f"CLAIM Q11: computed={computed_Q11:.5g} expected={expected_Q11} match={'yes' if match_Q11 else 'no'}")

# Claim Q12
N_max_proj = P_c / P_q_eff
expected_Q12 = "4.0e7"
computed_Q12 = N_max_proj
match_Q12 = fmt_sig(computed_Q12, 2) == expected_Q12
print(f"CLAIM Q12: computed={computed_Q12:.5g} expected={expected_Q12} match={'yes' if match_Q12 else 'no'}")

# Claim Q13
kappa = 2
p0_prime = kappa * 1e-3
expected_Q13 = "2.0e-3"
computed_Q13 = p0_prime
match_Q13 = fmt_sig(computed_Q13, 2) == expected_Q13
print(f"CLAIM Q13: computed={computed_Q13:.5g} expected={expected_Q13} match={'yes' if match_Q13 else 'no'}")

# Claim Q14
DeltaT_eff = P_q_eff * R_th
expected_Q14 = "1.25e-7"
computed_Q14 = DeltaT_eff
match_Q14 = fmt_sig(computed_Q14, 3) == expected_Q14
print(f"CLAIM Q14: computed={computed_Q14:.5g} expected={expected_Q14} match={'yes' if match_Q14 else 'no'}")

# Claim Q15
p_improved = p0_prime * math.exp(alpha * DeltaT_eff)  # exponent tiny
expected_Q15 = "2.0e-3"
computed_Q15 = p_improved
match_Q15 = fmt_sig(computed_Q15, 2) == expected_Q15
print(f"CLAIM Q15: computed={computed_Q15:.5g} expected={expected_Q15} match={'yes' if match_Q15 else 'no'}")

# Claim Q16
delta = 0.5
d = 21
exponent_GKP = delta * (d + 1) / 2
p_L_GKP = A * (2.0e-3 / 1e-2) ** exponent_GKP
expected_Q16 = "1.43e-5"
computed_Q16 = p_L_GKP
match_Q16 = fmt_sig(computed_Q16, 3) == expected_Q16
print(f"CLAIM Q16: computed={computed_Q16:.5g} expected={expected_Q16} match={'yes' if match_Q16 else 'no'}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10,match_Q11,match_Q12,match_Q13,match_Q14,match_Q15,match_Q16])} match, {16 - sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8,match_Q9,match_Q10,match_Q11,match_Q12,match_Q13,match_Q14,match_Q15,match_Q16])} mismatch")
