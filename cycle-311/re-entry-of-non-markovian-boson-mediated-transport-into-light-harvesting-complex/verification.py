import math

def fmt(val, digits):
    """Format a float with a given number of decimal places, removing trailing zeros."""
    fmt_str = f"{{:.{digits}f}}".format(val)
    # Strip trailing zeros and possible trailing decimal point
    if '.' in fmt_str:
        fmt_str = fmt_str.rstrip('0').rstrip('.')
    return fmt_str

# Q1: Transfer time for representative parameters
V = 50.0          # cm^-1
Delta = 110.0     # cm^-1
c = 2.9979e10     # cm s^-1
tau_T = Delta / (2 * math.pi * c * V**2)   # seconds
tau_T_ps = tau_T * 1e12                    # convert to picoseconds
computed_Q1 = fmt(tau_T_ps, 4)
expected_Q1 = "0.2336"
match_Q1 = "yes" if computed_Q1 == expected_Q1 else "no"
print(f"CLAIM Q1: computed={computed_Q1} expected={expected_Q1} match={match_Q1}")

# Q2: Single‑hop trapping‑limited efficiency
kappa = 1.0                     # ps^-1
tau_e = 1.0                     # ns
gamma_rec = 1.0 / (tau_e * 1e3) # convert ns to ps => 1e-3 ps^-1
eta = kappa / (kappa + gamma_rec)
computed_Q2 = fmt(eta, 6)
expected_Q2 = "0.999001"
match_Q2 = "yes" if computed_Q2 == expected_Q2 else "no"
print(f"CLAIM Q2: computed={computed_Q2} expected={expected_Q2} match={match_Q2}")

# Q3: Memory‑ratio for fast baths interval
tau_B_fast = 0.1                # ps
# bounds from τ_T_max = 0.2336 ps, τ_T_min = 0.1699 ps (as given in the paper)
R_fast_low = tau_B_fast / 0.2336
R_fast_high = tau_B_fast / 0.1699
computed_Q3 = f"[{fmt(R_fast_low,3)},{fmt(R_fast_high,3)}]"
expected_Q3 = "[0.428,0.589]"
match_Q3 = "yes" if computed_Q3 == expected_Q3 else "no"
print(f"CLAIM Q3: computed={computed_Q3} expected={expected_Q3} match={match_Q3}")

# Q4: Memory‑ratio for slow baths interval
tau_B_slow = 1.0                # ps
R_slow_low = tau_B_slow / 0.2336
R_slow_high = tau_B_slow / 0.1699
computed_Q4 = f"[{fmt(R_slow_low,2)},{fmt(R_slow_high,2)}]"
expected_Q4 = "[4.28,5.89]"
match_Q4 = "yes" if computed_Q4 == expected_Q4 else "no"
print(f"CLAIM Q4: computed={computed_Q4} expected={expected_Q4} match={match_Q4}")

# Q5: Optimal hopping rate across experimental box
V_min, V_max = 50.0, 75.0
Delta_min, Delta_max = 110.0, 180.0
k_star_min = V_min**2 / Delta_max   # minimum k*
k_star_max = V_max**2 / Delta_min   # maximum k*
computed_Q5 = f"[{fmt(k_star_min,2)},{fmt(k_star_max,2)}]"
expected_Q5 = "[13.89,51.14]"
match_Q5 = "yes" if computed_Q5 == expected_Q5 else "no"
print(f"CLAIM Q5: computed={computed_Q5} expected={expected_Q5} match={match_Q5}")

# Q6: Projected computational cost
cpu_hours = 1e4
price_per_hour = 0.10
cost = cpu_hours * price_per_hour
computed_Q6 = fmt(cost,0)
expected_Q6 = "1000"
match_Q6 = "yes" if computed_Q6 == expected_Q6 else "no"
print(f"CLAIM Q6: computed={computed_Q6} expected={expected_Q6} match={match_Q6}")

# Q7: Transfer‑time range across experimental box
# max τ_T using V=50, Δ=110 (as in paper)
tau_T_max = 110.0 / (2 * math.pi * c * 50.0**2) * 1e12  # ps
# min τ_T using V=75, Δ=180 (as in paper)
tau_T_min = 180.0 / (2 * math.pi * c * 75.0**2) * 1e12  # ps
computed_Q7 = f"[{fmt(tau_T_min,4)},{fmt(tau_T_max,4)}]"
expected_Q7 = "[0.1699,0.2336]"
match_Q7 = "yes" if computed_Q7 == expected_Q7 else "no"
print(f"CLAIM Q7: computed={computed_Q7} expected={expected_Q7} match={match_Q7}")

print(f"VERIFICATION SUMMARY: 7 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7].count('yes'))} match, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7].count('no'))} mismatch")
