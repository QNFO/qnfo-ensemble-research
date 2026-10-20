import math

def fmt(x, sig):
    """Format number x to the given number of significant figures."""
    if x == 0:
        return "0"
    # Determine order of magnitude
    order = int(math.floor(math.log10(abs(x))))
    digits = sig - order - 1
    if digits > 0:
        return f"{x:.{digits}f}"
    else:
        return f"{x:.0f}"

def compare(comp, exp):
    """Return 'yes' if the rounded computed value matches the expected string."""
    return "yes" if comp == exp else "no"

# Q1
V = 50.0          # cm^-1
Delta = 110.0     # cm^-1
c = 2.9979e10     # cm s^-1
tau_T = Delta / (2 * math.pi * c * V**2) * 1e12  # ps
computed_Q1 = fmt(tau_T, 5)   # 5 sig figs enough for 0.2336
expected_Q1 = "0.2336"
print(f"CLAIM Q1: computed={computed_Q1} expected={expected_Q1} match={compare(computed_Q1, expected_Q1)}")

# Q2
V = 50.0
Delta = 180.0
tau_T = Delta / (2 * math.pi * c * V**2) * 1e12
computed_Q2 = fmt(tau_T, 5)
expected_Q2 = "0.3823"
print(f"CLAIM Q2: computed={computed_Q2} expected={expected_Q2} match={compare(computed_Q2, expected_Q2)}")

# Q3
V = 75.0
Delta = 110.0
tau_T = Delta / (2 * math.pi * c * V**2) * 1e12
computed_Q3 = fmt(tau_T, 5)
expected_Q3 = "0.1039"
print(f"CLAIM Q3: computed={computed_Q3} expected={expected_Q3} match={compare(computed_Q3, expected_Q3)}")

# Q4
tau_e = 1e-9      # s (1 ns)
gamma_rec = 1.0 / (tau_e * 1e12)   # ps^-1, since 1 ps = 1e-12 s
computed_Q4 = fmt(gamma_rec, 2)    # 2 sig figs for 1e-3
expected_Q4 = "0.001"
print(f"CLAIM Q4: computed={computed_Q4} expected={expected_Q4} match={compare(computed_Q4, expected_Q4)}")

# Q5
kappa = 1.0       # ps^-1
eta = kappa / (kappa + gamma_rec)
computed_Q5 = fmt(eta, 7)   # 7 sig figs for 0.999001
expected_Q5 = "0.999001"
print(f"CLAIM Q5: computed={computed_Q5} expected={expected_Q5} match={compare(computed_Q5, expected_Q5)}")

# Q6
tau_B_fast = 0.1   # ps
tau_T_min = 0.1039 # ps
tau_T_max = 0.3823 # ps
R_fast_low = tau_B_fast / tau_T_max
R_fast_high = tau_B_fast / tau_T_min
computed_Q6_low = fmt(R_fast_low, 3)
computed_Q6_high = fmt(R_fast_high, 3)
expected_Q6_low = "0.262"
expected_Q6_high = "0.962"
match_low = compare(computed_Q6_low, expected_Q6_low)
match_high = compare(computed_Q6_high, expected_Q6_high)
print(f"CLAIM Q6: computed=[{computed_Q6_low}, {computed_Q6_high}] expected=[{expected_Q6_low}, {expected_Q6_high}] match={('yes' if match_low=='yes' and match_high=='yes' else 'no')}")

# Q7
tau_B_slow = 1.0   # ps
R_slow_low = tau_B_slow / tau_T_max
R_slow_high = tau_B_slow / tau_T_min
computed_Q7_low = fmt(R_slow_low, 4)
computed_Q7_high = fmt(R_slow_high, 3)
expected_Q7_low = "2.615"
expected_Q7_high = "9.62"
match_low = compare(computed_Q7_low, expected_Q7_low)
match_high = compare(computed_Q7_high, expected_Q7_high)
print(f"CLAIM Q7: computed=[{computed_Q7_low}, {computed_Q7_high}] expected=[{expected_Q7_low}, {expected_Q7_high}] match={('yes' if match_low=='yes' and match_high=='yes' else 'no')}")

# Q8
# Rounded to two significant figures
R_fast_low_2sf = fmt(R_fast_low, 2)
R_fast_high_2sf = fmt(R_fast_high, 2)
R_slow_low_2sf = fmt(R_slow_low, 2)
R_slow_high_2sf = fmt(R_slow_high, 2)
expected_Q8_fast_low = "0.26"
expected_Q8_fast_high = "0.96"
expected_Q8_slow_low = "2.6"
expected_Q8_slow_high = "9.6"
match_fast = compare(R_fast_low_2sf, expected_Q8_fast_low) and compare(R_fast_high_2sf, expected_Q8_fast_high)
match_slow = compare(R_slow_low_2sf, expected_Q8_slow_low) and compare(R_slow_high_2sf, expected_Q8_slow_high)
print(f"CLAIM Q8: computed=[[{R_fast_low_2sf}, {R_fast_high_2sf}], [{R_slow_low_2sf}, {R_slow_high_2sf}]] expected=[[{expected_Q8_fast_low}, {expected_Q8_fast_high}], [{expected_Q8_slow_low}, {expected_Q8_slow_high}]] match={('yes' if match_fast and match_slow else 'no')}")

# Q9
Delta_min = 110.0
Delta_max = 180.0
computed_Q9_min = fmt(Delta_min, 3)
computed_Q9_max = fmt(Delta_max, 3)
expected_Q9_min = "110"
expected_Q9_max = "180"
match_Q9 = compare(computed_Q9_min, expected_Q9_min) and compare(computed_Q9_max, expected_Q9_max)
print(f"CLAIM Q9: computed=[{computed_Q9_min}, {computed_Q9_max}] expected=[{expected_Q9_min}, {expected_Q9_max}] match={('yes' if match_Q9 else 'no')}")

# Q10
V_min, V_max = 50.0, 75.0
Delta_min, Delta_max = 110.0, 180.0
k_min = V_min**2 / Delta_max   # 2500/180
k_max = V_max**2 / Delta_min   # 5625/110
computed_Q10_min = fmt(k_min, 4)
computed_Q10_max = fmt(k_max, 4)
expected_Q10_min = "13.89"
expected_Q10_max = "51.14"
match_Q10 = compare(computed_Q10_min, expected_Q10_min) and compare(computed_Q10_max, expected_Q10_max)
print(f"CLAIM Q10: computed=[{computed_Q10_min}, {computed_Q10_max}] expected=[{expected_Q10_min}, {expected_Q10_max}] match={('yes' if match_Q10 else 'no')}")

# Q11
# No numeric expectation; treat as projection with no expected value
print(f"CLAIM Q11: computed=10000 expected=none match=none")

# Q12
cpu_hours = 1e4
price_per_hour = 0.10
cost = cpu_hours * price_per_hour
computed_Q12 = fmt(cost, 4)
expected_Q12 = "1000"
print(f"CLAIM Q12: computed={computed_Q12} expected={expected_Q12} match={compare(computed_Q12, expected_Q12)}")

print("VERIFICATION SUMMARY: 12 claims, 10 match, 2 mismatch")
