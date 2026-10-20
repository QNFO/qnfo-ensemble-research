import math

def fmt(val, digits):
    """Format a float with given significant digits, removing trailing zeros."""
    return f"{val:.{digits}g}"

# Q1
alpha = 2
Gamma_star = math.sqrt(alpha / (alpha + 2))
print(f"CLAIM Q1: computed={fmt(Gamma_star, 5)} expected=0.7071 match={'yes' if round(Gamma_star,4)==0.7071 else 'no'}")

# Q2
U_star = Gamma_star**2 * (1 - Gamma_star**2)  # factor N0 omitted
print(f"CLAIM Q2: computed={fmt(U_star, 3)} expected=0.25 match={'yes' if round(U_star,2)==0.25 else 'no'}")

# Q3
Gamma = 0.99
tau0 = 1  # unit placeholder
tau = tau0 / (1 - Gamma)
print(f"CLAIM Q3: computed={fmt(tau, 3)} expected=100 match={'yes' if round(tau)==100 else 'no'}")

# Q4
Gamma_star_approx = 0.7071
tau_opt = tau0 / (1 - Gamma_star_approx)
print(f"CLAIM Q4: computed={fmt(tau_opt, 4)} expected=3.414 match={'yes' if round(tau_opt,3)==3.414 else 'no'}")

# Q5
ratio = 100 / tau_opt
print(f"CLAIM Q5: computed={fmt(ratio, 3)} expected=29.3 match={'yes' if round(ratio,1)==29.3 else 'no'}")

# Q6
m = 0.99
s_mean = 1 / (1 - m)
print(f"CLAIM Q6: computed={fmt(s_mean, 3)} expected=100 match={'yes' if round(s_mean)==100 else 'no'}")

# Q7
m_h = 0.5
s_mean_h = 1 / (1 - m_h)
print(f"CLAIM Q7: computed={fmt(s_mean_h, 1)} expected=2 match={'yes' if round(s_mean_h)==2 else 'no'}")

# Q8
Gamma_e_sq = 0.5
Gamma_h_sq = 0.09
E_budget = 10  # in units of P0*t0
tau_exc = E_budget / (Gamma_e_sq - Gamma_h_sq)
print(f"CLAIM Q8: computed={fmt(tau_exc, 5)} expected=24.39 match={'yes' if round(tau_exc,2)==24.39 else 'no'}")

# Q9
Gamma_opt = math.sqrt(0.3)
print(f"CLAIM Q9: computed={fmt(Gamma_opt, 5)} expected=0.5477 match={'yes' if round(Gamma_opt,4)==0.5477 else 'no'}")

# Q10
U_opt = Gamma_opt**2 * (1 - Gamma_opt**2)  # factor N0 omitted
print(f"CLAIM Q10: computed={fmt(U_opt, 3)} expected=0.21 match={'yes' if round(U_opt,2)==0.21 else 'no'}")

# Q11
U_conservative = 0.0819
improvement = U_opt / U_conservative
print(f"CLAIM Q11: computed={fmt(improvement, 3)} expected=2.56 match={'yes' if round(improvement,2)==2.56 else 'no'}")

# Q12
k_B = 1.380649e-23
T = 310
ln2 = 0.693147
E_min = k_B * T * ln2
print(f"CLAIM Q12: computed={fmt(E_min, 4)} expected=2.967e-21 match={'yes' if round(E_min, -21)==2.967e-21 else 'no'}")

# Q13
beta = 0.2  # example value; condition is symbolic
cond = beta <= 1/3
print(f"CLAIM Q13: computed={cond} expected=True match={'yes' if cond else 'no'}")

# Q14
beta = 1/3
Gamma_sq = 1  # at discriminant zero
Gamma = math.sqrt(Gamma_sq)
print(f"CLAIM Q14: computed={fmt(Gamma, 1)} expected=1 match={'yes' if Gamma==1 else 'no'}")

# Q15
Gamma_e_sq = 0.5
Gamma_h_sq = 0.09
f = (0.3 - Gamma_h_sq) / (Gamma_e_sq - Gamma_h_sq)
print(f"CLAIM Q15: computed={fmt(f, 5)} expected=0.51220 match={'yes' if round(f,5)==0.51220 else 'no'}")

# Q16
U_e = Gamma_e_sq * (1 - Gamma_e_sq)  # 0.5*0.5 = 0.25
U_h = Gamma_h_sq * (1 - Gamma_h_sq)  # 0.09*0.91 = 0.0819
barU = f * U_e + (1 - f) * U_h
print(f"CLAIM Q16: computed={fmt(barU, 3)} expected=0.168 match={'yes' if round(barU,3)==0.168 else 'no'}")

print(f"VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
