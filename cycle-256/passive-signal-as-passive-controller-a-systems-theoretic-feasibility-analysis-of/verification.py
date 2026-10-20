import math

def round_to_sig(value, expected_str):
    """Round value to the same number of decimal places as expected_str."""
    if '.' in expected_str:
        dec_places = len(expected_str.split('.')[-1])
        return round(value, dec_places)
    else:
        return round(value)

def print_claim(id_, computed, expected):
    rounded = round_to_sig(computed, expected)
    match = "yes" if str(rounded) == expected else "no"
    print(f"CLAIM {id_}: computed={computed:.10g} expected={expected} match={match}")

# Q1
x0 = 0.0
u0 = 0.1
deltaV = 0.5 * ((x0 + u0) ** 2 - x0 ** 2)
y0 = x0 + 0.5 * u0
supply = u0 * y0
print_claim("Q1", deltaV, "0.005")  # ΔV and supply are both 0.005

# Q2
alpha = 0.1
x0 = 2.0
u0 = 0.0
delta = alpha - alpha ** 2 / 2
x1 = (1 - alpha) * x0 + u0
V0 = 0.5 * x0 ** 2
V1 = 0.5 * x1 ** 2
deltaV = V1 - V0
neg_delta_x2 = -delta * x0 ** 2
print_claim("Q2", deltaV, "-0.38")

# Q3
alpha = 0.1
x0 = 2.0
u0 = 0.5
delta = alpha - alpha ** 2 / 2
x1 = (1 - alpha) * x0 + u0
V0 = 0.5 * x0 ** 2
V1 = 0.5 * x1 ** 2
deltaV = V1 - V0
y0 = (1 - alpha) * x0 + 0.5 * u0
supply = u0 * y0
diff = deltaV - supply
print_claim("Q3", deltaV, "0.645")

# Q4
alpha = 0.1
delta = alpha - alpha ** 2 / 2
x = 1.0
u = -1.0
expr = -delta * x ** 2 - alpha * x * u + 0.5 * u ** 2
print_claim("Q4", expr, "0.505")

# Q5
q = 0.1
U_max = 1.0
N = 100
delta_quant = N * U_max * q / 2
print_claim("Q5", delta_quant, "5.0")

# Q6
delta = 0.095
N = 100
delta_quant = 5.0
x_star = math.sqrt(delta_quant / (delta * N))
print_claim("Q6", x_star, "0.726")

# Q7
omega_c = 1.0
T_d = 0.5
phi_d = omega_c * T_d
print_claim("Q7", phi_d, "0.5")

# Q8
k_S = 2.0
epsilon_S = 0.1
epsilon_W = 0.2
M = k_S * (epsilon_S + epsilon_W)
print_claim("Q8", M, "0.6")

# Q9
phi_d = 0.5
ell_d = phi_d / (2 * math.pi)
print_claim("Q9", ell_d, "0.0796")

# Q10
M = 0.6
M_n = M / (1 + M)
print_claim("Q10", M_n, "0.375")

# Q11
M_n = 0.375
ell_d = 0.5 / (2 * math.pi)  # same as in Q9
rho = M_n / ell_d
print_claim("Q11", rho, "4.71")

# Q12
Delta = 0.05
u_max = 1.0
E_q = (Delta / 2) * u_max
print_claim("Q12", E_q, "0.025")

# Q13
E_0 = u_max ** 2
overhead = E_q / E_0
print_claim("Q13", overhead, "0.025")

# Q14
Delta = 0.05
lambda_W = 0.5
r_q = (Delta / 2) / lambda_W
print_claim("Q14", r_q, "0.05")

# Q15
delta = 0.1
M = 0.6
fraction = delta / M
print_claim("Q15", fraction, "0.1667")

# Q16
# Show the maximum δ at α=1
alpha = 1.0
delta_max = alpha - alpha ** 2 / 2
print_claim("Q16", delta_max, "0.5")
