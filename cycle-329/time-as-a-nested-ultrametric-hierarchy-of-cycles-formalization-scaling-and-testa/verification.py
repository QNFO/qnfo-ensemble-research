import math

def round_sig(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Inputs
m_e = 9.10938356e-31          # kg
c = 2.99792458e8              # m/s
hbar = 1.054571817e-34        # J·s
alpha = 7.2973525693e-3
alpha_inv = 1/alpha           # ≈137.035999084
T_target = 1.0                # s
tau0 = 8.1e-21                # s
Delta = 10.0
sigma_t = 1.0e-22             # s

# Claim Q1
omega_C = (m_e * c**2) / hbar
computed_Q1 = omega_C
expected_Q1 = 7.763e20
match_Q1 = round_sig(computed_Q1, 4) == round_sig(expected_Q1, 4)

# Claim Q2
T_Z = 2 * math.pi / omega_C
computed_Q2 = T_Z
expected_Q2 = 8.1e-21
match_Q2 = round_sig(computed_Q2, 2) == round_sig(expected_Q2, 2)

# Claim Q3
T_alpha = alpha_inv / omega_C
computed_Q3 = T_alpha
expected_Q3 = 1.77e-19
match_Q3 = round_sig(computed_Q3, 3) == round_sig(expected_Q3, 3)

# Claim Q4
lam = alpha_inv
k = math.log(T_target / T_Z) / math.log(lam)
computed_Q4 = k
expected_Q4 = 9.403
match_Q4 = round_sig(computed_Q4, 4) == round_sig(expected_Q4, 4)

# Claim Q5
t2_decrease = tau0 * Delta**-2
computed_Q5 = t2_decrease
expected_Q5 = 8.1e-23
match_Q5 = round_sig(computed_Q5, 2) == round_sig(expected_Q5, 2)

# Claim Q6
t2_increase = tau0 * Delta**2
computed_Q6 = t2_increase
expected_Q6 = 8.1e-19
match_Q6 = round_sig(computed_Q6, 2) == round_sig(expected_Q6, 2)

# Claim Q7
tau_jump = alpha_inv / omega_C
computed_Q7 = tau_jump
expected_Q7 = 1.77e-19
match_Q7 = round_sig(computed_Q7, 3) == round_sig(expected_Q7, 3)

# Claim Q8
SNR = t2_increase / sigma_t
computed_Q8 = SNR
expected_Q8 = 8.1e3
match_Q8 = round_sig(computed_Q8, 2) == round_sig(expected_Q8, 2)

# Output
print(f"CLAIM Q1: computed={computed_Q1:.8e} expected={expected_Q1:.8e} match={'yes' if match_Q1 else 'no'}")
print(f"CLAIM Q2: computed={computed_Q2:.8e} expected={expected_Q2:.8e} match={'yes' if match_Q2 else 'no'}")
print(f"CLAIM Q3: computed={computed_Q3:.8e} expected={expected_Q3:.8e} match={'yes' if match_Q3 else 'no'}")
print(f"CLAIM Q4: computed={computed_Q4:.8e} expected={expected_Q4:.8e} match={'yes' if match_Q4 else 'no'}")
print(f"CLAIM Q5: computed={computed_Q5:.8e} expected={expected_Q5:.8e} match={'yes' if match_Q5 else 'no'}")
print(f"CLAIM Q6: computed={computed_Q6:.8e} expected={expected_Q6:.8e} match={'yes' if match_Q6 else 'no'}")
print(f"CLAIM Q7: computed={computed_Q7:.8e} expected={expected_Q7:.8e} match={'yes' if match_Q7 else 'no'}")
print(f"CLAIM Q8: computed={computed_Q8:.8e} expected={expected_Q8:.8e} match={'yes' if match_Q8 else 'no'}")
print(f"VERIFICATION SUMMARY: 8 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8])} match, {8 - sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_Q8])} mismatch")
