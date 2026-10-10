import math

def is_close(a, b):
    return math.isclose(a, b, rel_tol=1e-6, abs_tol=0.0)

def claim_line(cid, computed, expected, match):
    return f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}"

# Q1
x0 = 0.0
u0 = 0.1
deltaV = 0.5 * (x0 + u0) ** 2 - 0.5 * x0 ** 2
supply = u0 * (x0 + 0.5 * u0)
expected_q1 = 0.005
match_q1 = is_close(deltaV, expected_q1) and is_close(supply, expected_q1)
print(claim_line("Q1", deltaV, expected_q1, match_q1))

# Q2
alpha = 0.1
margin_coeff = alpha ** 2 / 2 - alpha
expected_q2 = -0.095
match_q2 = is_close(margin_coeff, expected_q2)
print(claim_line("Q2", margin_coeff, expected_q2, match_q2))

# Q3
x0 = 2.0
u0 = 0.0
deltaV_q3 = 0.5 * ((1 - alpha) * x0 + u0) ** 2 - 0.5 * x0 ** 2
margin_q3 = alpha ** 2 / 2 - alpha
expected_q3 = -0.38
match_q3 = is_close(deltaV_q3, expected_q3) and is_close(margin_q3 * x0 ** 2, expected_q3)
print(claim_line("Q3", deltaV_q3, expected_q3, match_q3))

# Q4
x0 = 2.0
u0 = 0.5
y0 = (1 - alpha) * x0 + 0.5 * u0
deltaV_q4 = 0.5 * ((1 - alpha) * x0 + u0) ** 2 - 0.5 * x0 ** 2
margin_q4 = deltaV_q4 - u0 * y0
expected_q4 = -0.38
match_q4 = is_close(margin_q4, expected_q4)
print(claim_line("Q4", margin_q4, expected_q4, match_q4))

# Q5
x = 1.0
u = -1.0
expr_q5 = (alpha ** 2 / 2 - alpha) * x ** 2 + (1 - alpha - 1) * x * u + 0.5 * u ** 2
expected_q5 = 0.505
match_q5 = is_close(expr_q5, expected_q5)
print(claim_line("Q5", expr_q5, expected_q5, match_q5))

# Q6
q = 0.1
Umax = 1.0
N = 100
delta_quant = N * Umax * q / 2
expected_q6 = 5.0
match_q6 = is_close(delta_quant, expected_q6)
print(claim_line("Q6", delta_quant, expected_q6, match_q6))

# Q7
omega_c = 1.0
T_d = 0.5
phi = omega_c * T_d           # radians
degrees = phi * 180.0 / math.pi
expected_rad = 0.5
expected_deg = 28.65
match_q7 = is_close(phi, expected_rad) and is_close(degrees, expected_deg, rel_tol=1e-4)
print(claim_line("Q7", f"{phi} rad, {degrees} deg", f"{expected_rad} rad, {expected_deg} deg", match_q7))

# Q8
k_S = 2.0
eps_S = 0.1
eps_W = 0.2
M = k_S * (eps_S + eps_W)
expected_q8 = 0.6
match_q8 = is_close(M, expected_q8)
print(claim_line("Q8", M, expected_q8, match_q8))

print(f"VERIFICATION SUMMARY: 8 claims, {sum([match_q1, match_q2, match_q3, match_q4, match_q5, match_q6, match_q7, match_q8])} match, {8 - sum([match_q1, match_q2, match_q3, match_q4, match_q5, match_q6, match_q7, match_q8])} mismatch")
