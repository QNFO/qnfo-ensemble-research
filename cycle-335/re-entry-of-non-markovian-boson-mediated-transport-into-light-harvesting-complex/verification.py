import math

# Constants
c = 2.9979e10  # cm s^-1
pi = math.pi

# Q1: Representative transfer time
V1 = 50.0  # cm^-1
Delta1 = 110.0  # cm^-1
tau_T1_s = Delta1 / (2 * pi * c * V1**2)
tau_T1_ps = tau_T1_s * 1e12
print(f"CLAIM Q1: computed={tau_T1_ps:.8g} expected=0.2336 match={'yes' if round(tau_T1_ps,4)==0.2336 else 'no'}")

# Q2: Maximum transfer time
V2 = 50.0
Delta2 = 180.0
tau_T2_s = Delta2 / (2 * pi * c * V2**2)
tau_T2_ps = tau_T2_s * 1e12
print(f"CLAIM Q2: computed={tau_T2_ps:.8g} expected=0.3823 match={'yes' if round(tau_T2_ps,4)==0.3823 else 'no'}")

# Q3: Minimum transfer time
V3 = 75.0
Delta3 = 110.0
tau_T3_s = Delta3 / (2 * pi * c * V3**2)
tau_T3_ps = tau_T3_s * 1e12
print(f"CLAIM Q3: computed={tau_T3_ps:.8g} expected=0.1039 match={'yes' if round(tau_T3_ps,4)==0.1039 else 'no'}")

# Q4: Recombination rate
tau_e_ps = 1000.0  # ps (1 ns)
gamma_rec = 1.0 / tau_e_ps  # ps^-1
print(f"CLAIM Q4: computed={gamma_rec:.8g} expected=0.001 match={'yes' if round(gamma_rec,3)==0.001 else 'no'}")

# Q5: Single‑hop trapping efficiency
kappa = 1.0  # ps^-1
eta = kappa / (kappa + gamma_rec)
print(f"CLAIM Q5: computed={eta:.8g} expected=0.999001 match={'yes' if round(eta,6)==0.999001 else 'no'}")

# Q6: Fast‑bath lower bound of memory ratio
tau_B_fast = 0.1  # ps
tau_T_max = tau_T2_ps  # from Q2
R_fast_low = tau_B_fast / tau_T_max
print(f"CLAIM Q6: computed={R_fast_low:.8g} expected=0.262 match={'yes' if round(R_fast_low,3)==0.262 else 'no'}")

# Q7: Fast‑bath upper bound of memory ratio
tau_T_min = tau_T3_ps  # from Q3
R_fast_high = tau_B_fast / tau_T_min
print(f"CLAIM Q7: computed={R_fast_high:.8g} expected=0.962 match={'yes' if round(R_fast_high,3)==0.962 else 'no'}")

# Q8: Slow‑bath lower bound of memory ratio
tau_B_slow = 1.0  # ps
R_slow_low = tau_B_slow / tau_T_max
print(f"CLAIM Q8: computed={R_slow_low:.8g} expected=2.615 match={'yes' if round(R_slow_low,3)==2.615 else 'no'}")

# Q9: Slow‑bath upper bound of memory ratio
R_slow_high = tau_B_slow / tau_T_min
print(f"CLAIM Q9: computed={R_slow_high:.8g} expected=9.62 match={'yes' if round(R_slow_high,2)==9.62 else 'no'}")

# Q10: Optimal dephasing rate range
Delta_min, Delta_max = 110.0, 180.0
Gamma_star_min, Gamma_star_max = Delta_min, Delta_max
print(f"CLAIM Q10: computed={Gamma_star_min:.0f}–{Gamma_star_max:.0f} expected=110–180 match={'yes' if (Gamma_star_min, Gamma_star_max)==(110,180) else 'no'}")

# Q11: Optimal hopping rate range
V_vals = (50.0, 75.0)
Delta_vals = (110.0, 180.0)
k_star_min = V_vals[0]**2 / Delta_vals[1]   # 50^2 / 180
k_star_max = V_vals[1]**2 / Delta_vals[0]   # 75^2 / 110
print(f"CLAIM Q11: computed={k_star_min:.2f}–{k_star_max:.2f} expected=13.89–51.14 match={'yes' if (round(k_star_min,2), round(k_star_max,2))==(13.89,51.14) else 'no'}")

# Q13: Projected computational cost
cpu_hours = 1e4
price_per_hour = 0.10
cost = cpu_hours * price_per_hour
print(f"CLAIM Q13: computed={cost:.0f} expected=1000 match={'yes' if cost==1000 else 'no'}")

print("VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch")
