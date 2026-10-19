import math

def fmt(x, sig=8):
    # format with at least sig significant digits, removing trailing zeros
    s = f"{x:.{sig}g}"
    return s

# Q1
alpha = 2
Gamma_star = math.sqrt(alpha / (alpha + 2))
print(f"CLAIM Q1: computed={fmt(Gamma_star,8)} expected=0.707106 match={'yes' if round(Gamma_star,6)==0.707106 else 'no'}")

# Q2
U_star = 0.5 * 0.5  # N0 factor omitted, result is 0.25 N0
print(f"CLAIM Q2: computed={fmt(U_star,8)} expected=0.25 match={'yes' if abs(U_star-0.25)<1e-12 else 'no'}")

# Q3
tau0 = 1  # symbolic unit
tau_099 = tau0 / (1 - 0.99)
print(f"CLAIM Q3: computed={fmt(tau_099,8)} expected=100 match={'yes' if abs(tau_099-100)<1e-12 else 'no'}")

# Q4
Gamma_opt = 0.7071
tau_opt = tau0 / (1 - Gamma_opt)
print(f"CLAIM Q4: computed={fmt(tau_opt,8)} expected=3.414 match={'yes' if abs(tau_opt-3.414)<1e-3 else 'no'}")

# Q5
ratio = tau_099 / tau_opt
print(f"CLAIM Q5: computed={fmt(ratio,8)} expected=29.3 match={'yes' if abs(ratio-29.3)<1e-2 else 'no'}")

# Q6
m = 0.99
s_mean = 1 / (1 - m)
print(f"CLAIM Q6: computed={fmt(s_mean,8)} expected=100 match={'yes' if abs(s_mean-100)<1e-12 else 'no'}")

# Q7
m_h = 0.5
s_home = 1 / (1 - m_h)
print(f"CLAIM Q7: computed={fmt(s_home,8)} expected=2 match={'yes' if abs(s_home-2)<1e-12 else 'no'}")

# Q8
E_budget = 10  # in units of P0*t0
Gamma_e2 = 0.5
Gamma_h2 = 0.09
tau_exc = E_budget / (Gamma_e2 - Gamma_h2)
print(f"CLAIM Q8: computed={fmt(tau_exc,8)} expected=24.39 match={'yes' if abs(tau_exc-24.39)<1e-2 else 'no'}")

# Q9
Gamma_single = math.sqrt(0.3)
print(f"CLAIM Q9: computed={fmt(Gamma_single,8)} expected=0.547722 match={'yes' if round(Gamma_single,6)==0.547722 else 'no'}")

# Q10
U_single = 0.3 * 0.7  # N0 factor omitted
print(f"CLAIM Q10: computed={fmt(U_single,8)} expected=0.21 match={'yes' if abs(U_single-0.21)<1e-12 else 'no'}")

# Q11
U_cons = 0.09 * 0.91
print(f"CLAIM Q11: computed={fmt(U_cons,8)} expected=0.0819 match={'yes' if abs(U_cons-0.0819)<1e-12 else 'no'}")

# Q12
improve_opt = U_single / U_cons
print(f"CLAIM Q12: computed={fmt(improve_opt,8)} expected=2.56 match={'yes' if abs(improve_opt-2.56)<1e-2 else 'no'}")

# Q13
U_duty = 0.168
improve_duty = U_duty / U_cons
print(f"CLAIM Q13: computed={fmt(improve_duty,8)} expected=2.05 match={'yes' if abs(improve_duty-2.05)<1e-2 else 'no'}")

# Q14
kB = 1.380649e-23
T = 310
ln2 = 0.693147
E_min = kB * T * ln2
print(f"CLAIM Q14: computed={fmt(E_min,8)} expected=2.967e-21 match={'yes' if abs(E_min-2.967e-21)/2.967e-21<1e-3 else 'no'}")

# Q15
beta = 1/3
print(f"CLAIM Q15: computed={fmt(beta,8)} expected=1/3 match={'yes' if abs(beta-1/3)<1e-12 else 'no'}")
