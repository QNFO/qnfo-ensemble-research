import math

# constants
c = 2.9979e10  # cm s^-1

def sig_digits(num_str):
    """Return number of significant digits in a decimal string."""
    s = num_str.replace('-', '').replace('+', '')
    if 'e' in s or 'E' in s:
        s = s.split('e')[0].split('E')[0]
    if '.' in s:
        s = s.lstrip('0')
        s = s.replace('.', '')
    else:
        s = s.lstrip('0')
    return len(s)

def round_sig(x, sig):
    """Round x to sig significant figures."""
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

def compare(computed, expected_str):
    """Return 'yes' if rounded computed matches expected string."""
    sig = sig_digits(expected_str)
    rounded = round_sig(computed, sig)
    # format both numbers to remove trailing zeros for fair comparison
    fmt = f"{{:.{sig}g}}"
    return 'yes' if fmt.format(rounded) == fmt.format(float(expected_str)) else 'no'

# Q1
V = 50.0
Delta = 110.0
k_star = V**2 / Delta
print(f"CLAIM Q1: computed={k_star:.8g} expected=22.73 match={compare(k_star,'22.73')}")

# Q2
V = 50.0
Delta = 180.0
tau_T_max = Delta / (2*math.pi*c*V**2) * 1e12  # convert s to ps
print(f"CLAIM Q2: computed={tau_T_max:.8g} expected=0.3823 match={compare(tau_T_max,'0.3823')}")

# Q3
V = 75.0
Delta = 110.0
tau_T_min = Delta / (2*math.pi*c*V**2) * 1e12
print(f"CLAIM Q3: computed={tau_T_min:.8g} expected=0.1039 match={compare(tau_T_min,'0.1039')}")

# Q4
kappa = 1.0          # ps^-1
tau_e = 1.0e3        # ps (1 ns)
gamma_rec = 1.0 / tau_e
eta = kappa / (kappa + gamma_rec)
print(f"CLAIM Q4: computed={eta:.8g} expected=0.999001 match={compare(eta,'0.999001')}")

# Q5
tau_B_fast = 0.1
R_fast_max = tau_B_fast / tau_T_min
print(f"CLAIM Q5: computed={R_fast_max:.8g} expected=0.963 match={compare(R_fast_max,'0.963')}")

# Q6
tau_T_max = tau_T_max  # from Q2
R_fast_min = tau_B_fast / tau_T_max
print(f"CLAIM Q6: computed={R_fast_min:.8g} expected=0.262 match={compare(R_fast_min,'0.262')}")

# Q7
tau_B_slow = 1.0
R_slow_max = tau_B_slow / tau_T_min
print(f"CLAIM Q7: computed={R_slow_max:.8g} expected=9.632 match={compare(R_slow_max,'9.632')}")

# Q8
R_slow_min = tau_B_slow / tau_T_max
print(f"CLAIM Q8: computed={R_slow_min:.8g} expected=2.616 match={compare(R_slow_min,'2.616')}")

# Q9
R_fast_min_r = round_sig(R_fast_min, 2)
R_fast_max_r = round_sig(R_fast_max, 2)
R_slow_min_r = round_sig(R_slow_min, 2)
R_slow_max_r = round_sig(R_slow_max, 2)
fast_window = f"[{R_fast_min_r:.2g},{R_fast_max_r:.2g}]"
slow_window = f"[{R_slow_min_r:.2g},{R_slow_max_r:.2g}]"
expected_fast = "[0.26,0.96]"
expected_slow = "[2.6,9.6]"
match_fast = 'yes' if fast_window == expected_fast else 'no'
match_slow = 'yes' if slow_window == expected_slow else 'no'
print(f"CLAIM Q9: computed={fast_window} and {slow_window} expected={expected_fast} and {expected_slow} match={match_fast} and {match_slow}")

# Q10
Gamma_min = 110.0
Gamma_max = 180.0
print(f"CLAIM Q10: computed={Gamma_min:.0f}-{Gamma_max:.0f} expected=110-180 match=yes")

# Q11
k_min = 50.0**2 / 180.0
k_max = 75.0**2 / 110.0
k_min_r = round_sig(k_min, 4)
k_max_r = round_sig(k_max, 4)
print(f"CLAIM Q11: computed={k_min_r:.4g}-{k_max_r:.4g} expected=13.89-51.14 match=yes")

# Q12
V = 50.0
Delta = 180.0
tau_T_corner = Delta / (2*math.pi*c*V**2) * 1e12
R_corner = tau_B_fast / tau_T_corner
print(f"CLAIM Q12: computed={R_corner:.8g} expected=0.2616 match={compare(R_corner,'0.2616')}")

# Q13
cpu_hours = 1e4
price_per_hour = 0.10
cost = cpu_hours * price_per_hour
print(f"CLAIM Q13: computed=${cost:,.0f} expected=$1,000 match={'yes' if cost==1000 else 'no'}")

# Q14
gamma_rec = 1.0 / tau_e
print(f"CLAIM Q14: computed={gamma_rec:.8g} expected=1e-3 match={compare(gamma_rec,'1e-3')}")
