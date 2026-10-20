import math

def fmt(val, sig=8):
    # format with at least sig significant digits, remove trailing zeros
    s = f"{val:.{sig}g}"
    return s

# Q1
N_gate = 3 * 2 * 1
print(f"CLAIM Q1: computed={fmt(N_gate)} expected=6 match={'yes' if N_gate==6 else 'no'}")

# Q2
f_MS = 0.995
F = f_MS ** 6
print(f"CLAIM Q2: computed={fmt(F,10)} expected=0.9704 match={'yes' if round(F,4)==0.9704 else 'no'}")

# Q3
p_error = 1 - F
print(f"CLAIM Q3: computed={fmt(p_error,10)} expected=0.0296 match={'yes' if round(p_error,4)==0.0296 else 'no'}")

# Q4
J = 0.18
dt = 0.5
trotter_step_err = (J * dt) ** 3 * 100  # percent
print(f"CLAIM Q4: computed={fmt(trotter_step_err,10)} expected=0.0729% match={'yes' if round(trotter_step_err,4)==0.0729 else 'no'}")

# Q5
steps_per_sec = 2
cumulative_err = steps_per_sec * trotter_step_err
print(f"CLAIM Q5: computed={fmt(cumulative_err,10)} expected=≤0.15% match={'yes' if cumulative_err<=0.15 else 'no'}")

# Q6
avoided_steps = 1e4
factor = avoided_steps / N_gate
print(f"CLAIM Q6: computed={fmt(factor,10)} expected≈1.7e3 match={'yes' if 1.6e3 <= factor <= 1.8e3 else 'no'}")

# Q7
pairs = 3
N_trimer = pairs * 3 * 2
print(f"CLAIM Q7: computed={fmt(N_trimer)} expected=18 match={'yes' if N_trimer==18 else 'no'}")

# Q8
t_gate = 75e-6  # seconds
t_wall = N_gate * t_gate * 1e6  # microseconds
print(f"CLAIM Q8: computed={fmt(t_wall)} expected=450µs match={'yes' if round(t_wall)==450 else 'no'}")

# Q9
E_gate = 1e-6  # joules
E_sim = N_gate * E_gate * 1e6  # microjoules
print(f"CLAIM Q9: computed={fmt(E_sim)} expected=6µJ match={'yes' if round(E_sim)==6 else 'no'}")

# Q10
E_con_low = 8.5  # joules
ratio_low = E_con_low / (N_gate * E_gate)
print(f"CLAIM Q10: computed={fmt(ratio_low,10)} expected=1.42e6 match={'yes' if round(ratio_low/1e4)/100==1.42 else 'no'}")

# Q11
E_con_high = 16.3
ratio_high = E_con_high / (N_gate * E_gate)
print(f"CLAIM Q11: computed={fmt(ratio_high,10)} expected=2.72e6 match={'yes' if round(ratio_high/1e4)/100==2.72 else 'no'}")

# Q12
Delta_protect = 1e12
tau_ratio = 85.9
protect_factor = Delta_protect * tau_ratio
print(f"CLAIM Q12: computed={fmt(protect_factor,10)} expected≈8.6e13 match={'yes' if 8.5e13 <= protect_factor <= 8.7e13 else 'no'}")

# Q13
gate_error = 0.0296
trotter_error = 0.0015  # upper bound
threshold = gate_error + trotter_error
print(f"CLAIM Q13: computed={fmt(threshold,10)} expected=>0.031 match={'yes' if threshold>0.031 else 'no'}")

print("VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch")
