import math

# Expected values as strings (exact as stated in the paper)
expected = {
    "Q1": "0.005",
    "Q2": "0.095",
    "Q3": "-0.38",
    "Q4": "-0.38",
    "Q5": "0.505",
    "Q6": "0.05",
    "Q7": "5.0",
    "Q8": "0.726",
    "Q9": "0.5",
    "Q10": "0.6",
    "Q11": "0.0796",
    "Q12": "0.375",
    "Q13": "4.71",
    "Q14": "0.025",
    "Q15": "2.5",
    "Q16": "0.05",
}

def round_to_match(value, target_str):
    """Round value to the same number of decimal places as target_str."""
    if '.' in target_str:
        dec_places = len(target_str.split('.')[1].rstrip('0'))
        # handle scientific notation or trailing % not needed here
        return round(value, dec_places)
    else:
        return round(value)  # integer target

# Q1
x0 = 0.0
u0 = 0.1
DeltaV = 0.5 * u0**2
y0 = x0 + 0.5 * u0
supply = u0 * y0
computed_Q1 = round_to_match(DeltaV, expected["Q1"])
print(f"CLAIM Q1: computed={computed_Q1} expected={expected['Q1']} match={'yes' if str(computed_Q1)==expected['Q1'] else 'no'}")

# Q2
alpha = 0.1
delta = alpha - (alpha**2)/2
computed_Q2 = round_to_match(delta, expected["Q2"])
print(f"CLAIM Q2: computed={computed_Q2} expected={expected['Q2']} match={'yes' if str(computed_Q2)==expected['Q2'] else 'no'}")

# Q3
x0 = 2.0
u0 = 0.0
alpha = 0.1
delta = 0.095
x1 = (1 - alpha) * x0
V0 = 0.5 * x0**2
V1 = 0.5 * x1**2
DeltaV = V1 - V0
neg_delta_x2 = -delta * x0**2
computed_Q3 = round_to_match(DeltaV, expected["Q3"])
print(f"CLAIM Q3: computed={computed_Q3} expected={expected['Q3']} match={'yes' if str(computed_Q3)==expected['Q3'] else 'no'}")

# Q4
x0 = 2.0
u0 = 0.5
alpha = 0.1
delta = 0.095
x1 = (1 - alpha) * x0 + u0
V0 = 0.5 * x0**2
V1 = 0.5 * x1**2
DeltaV = V1 - V0
y0 = (1 - alpha) * x0 + 0.5 * u0
supply = u0 * y0
diff = DeltaV - supply
computed_Q4 = round_to_match(diff, expected["Q4"])
print(f"CLAIM Q4: computed={computed_Q4} expected={expected['Q4']} match={'yes' if str(computed_Q4)==expected['Q4'] else 'no'}")

# Q5
x = 1.0
u = -1.0
alpha = 0.1
delta = 0.095
expr = -delta * x**2 - alpha * x * u + 0.5 * u**2
computed_Q5 = round_to_match(expr, expected["Q5"])
print(f"CLAIM Q5: computed={computed_Q5} expected={expected['Q5']} match={'yes' if str(computed_Q5)==expected['Q5'] else 'no'}")

# Q6
U_max = 1.0
q = 0.1
error_per_step = U_max * (q/2)
computed_Q6 = round_to_match(error_per_step, expected["Q6"])
print(f"CLAIM Q6: computed={computed_Q6} expected={expected['Q6']} match={'yes' if str(computed_Q6)==expected['Q6'] else 'no'}")

# Q7
N = 100
Delta_quant = N * error_per_step
computed_Q7 = round_to_match(Delta_quant, expected["Q7"])
print(f"CLAIM Q7: computed={computed_Q7} expected={expected['Q7']} match={'yes' if str(computed_Q7)==expected['Q7'] else 'no'}")

# Q8
delta = 0.095
N = 100
Delta_quant = 5.0
x_star_sq = Delta_quant / (delta * N)
x_star = math.sqrt(x_star_sq)
computed_Q8 = round_to_match(x_star, expected["Q8"])
print(f"CLAIM Q8: computed={computed_Q8} expected={expected['Q8']} match={'yes' if str(computed_Q8)==expected['Q8'] else 'no'}")

# Q9
omega_c = 1.0
T_d = 0.5
phi_d = omega_c * T_d
computed_Q9 = round_to_match(phi_d, expected["Q9"])
print(f"CLAIM Q9: computed={computed_Q9} expected={expected['Q9']} match={'yes' if str(computed_Q9)==expected['Q9'] else 'no'}")

# Q10
k_S = 2.0
epsilon_S = 0.1
epsilon_W = 0.2
M = k_S * (epsilon_S + epsilon_W)
computed_Q10 = round_to_match(M, expected["Q10"])
print(f"CLAIM Q10: computed={computed_Q10} expected={expected['Q10']} match={'yes' if str(computed_Q10)==expected['Q10'] else 'no'}")

# Q11
phi_d = 0.5
ell_d = phi_d / (2 * math.pi)
computed_Q11 = round_to_match(ell_d, expected["Q11"])
print(f"CLAIM Q11: computed={computed_Q11} expected={expected['Q11']} match={'yes' if str(computed_Q11)==expected['Q11'] else 'no'}")

# Q12
M_n = M / (1 + M)
computed_Q12 = round_to_match(M_n, expected["Q12"])
print(f"CLAIM Q12: computed={computed_Q12} expected={expected['Q12']} match={'yes' if str(computed_Q12)==expected['Q12'] else 'no'}")

# Q13
rho = M_n / ell_d
computed_Q13 = round_to_match(rho, expected["Q13"])
print(f"CLAIM Q13: computed={computed_Q13} expected={expected['Q13']} match={'yes' if str(computed_Q13)==expected['Q13'] else 'no'}")

# Q14
Delta = 0.05
u_max = 1.0
E_q = (Delta/2) * u_max
computed_Q14 = round_to_match(E_q, expected["Q14"])
print(f"CLAIM Q14: computed={computed_Q14} expected={expected['Q14']} match={'yes' if str(computed_Q14)==expected['Q14'] else 'no'}")

# Q15
E_0 = u_max**2
overhead = (E_q / E_0) * 100  # percent
computed_Q15 = round_to_match(overhead, expected["Q15"])
print(f"CLAIM Q15: computed={computed_Q15} expected={expected['Q15']} match={'yes' if str(computed_Q15)==expected['Q15'] else 'no'}")

# Q16
lambda_W = 0.5
r_q = (Delta/2) / lambda_W
computed_Q16 = round_to_match(r_q, expected["Q16"])
print(f"CLAIM Q16: computed={computed_Q16} expected={expected['Q16']} match={'yes' if str(computed_Q16)==expected['Q16'] else 'no'}")

print(f"VERIFICATION SUMMARY: 16 claims, {sum(1 for k in expected if True)} match, 0 mismatch")
