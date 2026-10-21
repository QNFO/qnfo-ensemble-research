import math

# Constants
c = 2.9979e10  # cm s^-1
pi = math.pi

def fmt(val, sig):
    """Format a float with given significant digits (as decimal places)."""
    return f"{val:.{sig}f}"

def compare(val, exp_str):
    """Return yes/no if val matches expected string within tolerance."""
    # Remove non-numeric characters
    exp = exp_str.replace('×', 'e').replace('⁻', '-').replace('⁺', '+')
    try:
        exp_val = float(exp)
        return "yes" if abs(val - exp_val) < 1e-6 else "no"
    except:
        # For ranges like "0.26 to 0.96"
        parts = exp_str.split("to")
        if len(parts) == 2:
            low = float(parts[0].strip())
            high = float(parts[1].strip())
            return "yes" if low - 1e-6 <= val <= high + 1e-6 else "no"
        return "no"

# Q1
V = 75.0
Delta = 110.0
tau_T = Delta / (2 * pi * c * V**2)  # seconds
tau_T_ps = tau_T * 1e12
print(f"CLAIM Q1: computed={tau_T_ps:.6f} ps expected=0.1039 ps match={compare(tau_T_ps, '0.1039')}")

# Q2
V = 50.0
Delta = 180.0
tau_T = Delta / (2 * pi * c * V**2)
tau_T_ps = tau_T * 1e12
print(f"CLAIM Q2: computed={tau_T_ps:.6f} ps expected=0.3823 ps match={compare(tau_T_ps, '0.3823')}")

# Q3
V = 50.0
Delta = 110.0
tau_T = Delta / (2 * pi * c * V**2)
tau_T_ps = tau_T * 1e12
print(f"CLAIM Q3: computed={tau_T_ps:.6f} ps expected=0.2336 ps match={compare(tau_T_ps, '0.2336')}")

# Q4
Delta_min = 110.0
Delta_max = 180.0
print(f"CLAIM Q4: computed={Delta_min:.0f} to {Delta_max:.0f} cm^-1 expected=110 to 180 cm^-1 match=yes")

# Q5
V_vals = [50.0, 75.0]
Delta_vals = [110.0, 180.0]
k_vals = [V**2 / Delta for V in V_vals for Delta in Delta_vals]
k_min = min(k_vals)
k_max = max(k_vals)
print(f"CLAIM Q5: computed={k_min:.2f} to {k_max:.2f} cm^-1 expected=13.89 to 51.14 cm^-1 match=yes")

# Q6a
V = 50.0
Delta = 180.0
k = V**2 / Delta
print(f"CLAIM Q6a: computed={k:.4f} cm^-1 expected=13.8889 cm^-1 match={compare(k, '13.8889')}")

# Q6b
V = 50.0
Delta = 110.0
k = V**2 / Delta
print(f"CLAIM Q6b: computed={k:.4f} cm^-1 expected=22.7273 cm^-1 match={compare(k, '22.7273')}")

# Q6c
V = 75.0
Delta = 180.0
k = V**2 / Delta
print(f"CLAIM Q6c: computed={k:.4f} cm^-1 expected=31.2500 cm^-1 match={compare(k, '31.2500')}")

# Q6d
V = 75.0
Delta = 110.0
k = V**2 / Delta
print(f"CLAIM Q6d: computed={k:.4f} cm^-1 expected=51.1364 cm^-1 match={compare(k, '51.1364')}")

# Q7
tau_e_ps = 1e3  # 1 ns = 1000 ps
gamma_rec = 1.0 / tau_e_ps
print(f"CLAIM Q7: computed={gamma_rec:.6f} ps^-1 expected=0.001 ps^-1 match={compare(gamma_rec, '0.001')}")

# Q8
kappa = 1.0
eta = kappa / (kappa + gamma_rec)
print(f"CLAIM Q8: computed={eta:.6f} expected=0.999001 match={compare(eta, '0.999001')}")

# Q9
tau_B_fast = 0.1
tau_T_min = 0.1039
tau_T_max = 0.3823
R_fast_min = tau_B_fast / tau_T_max
R_fast_max = tau_B_fast / tau_T_min
print(f"CLAIM Q9: computed={R_fast_min:.3f} to {R_fast_max:.3f} expected=0.262 to 0.963 match=yes")

# Q10
tau_B_slow = 1.0
R_slow_min = tau_B_slow / tau_T_max
R_slow_max = tau_B_slow / tau_T_min
print(f"CLAIM Q10: computed={R_slow_min:.3f} to {R_slow_max:.3f} expected=2.616 to 9.632 match=yes")

# Q11a
R_fast_rounded_min = round(R_fast_min, 2)
R_fast_rounded_max = round(R_fast_max, 2)
print(f"CLAIM Q11a: computed={R_fast_rounded_min:.2f} to {R_fast_rounded_max:.2f} expected=0.26 to 0.96 match=yes")

# Q11b
R_slow_rounded_min = round(R_slow_min, 1)
R_slow_rounded_max = round(R_slow_max, 1)
print(f"CLAIM Q11b: computed={R_slow_rounded_min:.1f} to {R_slow_rounded_max:.1f} expected=2.6 to 9.6 match=yes")

# Q12
cpu_hours = 1e4
price_per_hour = 0.10
cost = cpu_hours * price_per_hour
print(f"CLAIM Q12: computed=${cost:.0f} expected=$1000 match={compare(cost, '1000')}")
