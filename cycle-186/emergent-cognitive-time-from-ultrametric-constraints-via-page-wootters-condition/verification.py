import math

def fmt(v, sig=6):
    # format number with given significant digits, removing trailing zeros
    s = f"{v:.{sig}g}"
    return s

# Claim Q1
f_theta = 8.0  # Hz
M = 10.0
delta_t_sec = (1.0 / f_theta) / M
delta_t_ms = delta_t_sec * 1000.0
print(f"CLAIM Q1: computed={fmt(delta_t_ms)} ms expected=12.5 ms match={'yes' if abs(delta_t_ms-12.5)<1e-9 else 'no'}")

# Claim Q2
T_theta_sec = 1.0 / f_theta
T_theta_ms = T_theta_sec * 1000.0
print(f"CLAIM Q2: computed={fmt(T_theta_ms)} ms expected=125 ms match={'yes' if abs(T_theta_ms-125.0)<1e-9 else 'no'}")

# Claim Q3
N = 64
N_f = N * (N - 1) // 2
print(f"CLAIM Q3: computed={N_f} expected=2016 match={'yes' if N_f==2016 else 'no'}")

# Claim Q4
L = 6
N_c = (N**3 / 6.0) * (1 - 4**(-L))
N_c_int = int(round(N_c))
print(f"CLAIM Q4: computed={N_c_int} expected=43680 match={'yes' if N_c_int==43680 else 'no'}")

# Claim Q5
rho = N_c_int / N_f
expected_rho = 65/3
print(f"CLAIM Q5: computed={fmt(rho)} expected=65/3 ≈ 21.6667 match={'yes' if abs(rho-expected_rho)<1e-9 else 'no'}")

# Claim Q6
N_c_alt = N * (N - 1) * (N - 2) // 6
print(f"CLAIM Q6: computed={N_c_alt} expected=41664 match={'yes' if N_c_alt==41664 else 'no'}")

# Claim Q7
N_PW = (M * (M - 1) / 2) * N**2
N_PW_int = int(N_PW)
print(f"CLAIM Q7: computed={N_PW_int} expected=184320 match={'yes' if N_PW_int==184320 else 'no'}")

# Claim Q8
t0 = 100.0  # ms
delta_t = 12.5  # ms
rt_k8 = t0 + 8 * delta_t
rt_k12 = t0 + 12 * delta_t
print(f"CLAIM Q8: computed={fmt(rt_k8)} ms and {fmt(rt_k12)} ms expected=200 ms and 250 ms match={'yes' if (abs(rt_k8-200)<1e-9 and abs(rt_k12-250)<1e-9) else 'no'}")

# Claim Q9
for f in (6.0, 10.0):
    dt = (1.0 / f) / M * 1000.0
    print(f"CLAIM Q9 (f={int(f)} Hz): computed={fmt(dt)} ms expected={'16.67 ms' if f==6 else '10 ms'} match={'yes' if (abs(dt-16.6666667)<1e-3 if f==6 else abs(dt-10.0)<1e-9) else 'no'}")

# Claim Q10
histories = 4**10
print(f"CLAIM Q10: computed={histories} expected=1048576 match={'yes' if histories==1048576 else 'no'}")

# Claim Q11
orderings = math.factorial(3)
print(f"CLAIM Q11: computed={orderings} expected=6 match={'yes' if orderings==6 else 'no'}")

# Claim Q12
rho_alt = N_c_alt / N_f
expected_rho_alt = 62/3
print(f"CLAIM Q12: computed={fmt(rho_alt)} expected=62/3 ≈ 20.6667 match={'yes' if abs(rho_alt-expected_rho_alt)<1e-9 else 'no'}")
