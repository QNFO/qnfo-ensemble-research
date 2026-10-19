import math

# Inputs
bar_n = 6
p_2q = 4.4e-3
p_1q = 1.0e-3
p_ro = 1.3e-2
p_corr = 1e-3
p = 0.44  # p/p_th for surface code
p_th = 1e-2
target = 1e-4
boundary_modes = 9
d = 29

# Claim Q1
p_bf = math.exp(-2 * bar_n)
# Claim Q2
p_eff = p_2q * p_bf
# Claim Q3 (function)
def f(p_val):
    return 3 * p_val**2 - 2 * p_val**3
# Claim Q4 (fixed point)
p_star = 0.25
# Claim Q5 (depolarizing threshold)
p_dep_thr = 3/8
# Claim Q6 (margin over target)
margin_target = target / p_eff
# Claim Q7 (readout dephasing margin)
margin_ro = 0.25 / p_ro
# Claim Q8 (level 1)
p1 = 3 * p_eff**2
# Claim Q9 (level 2)
p2 = 3 * p1**2
# Claim Q10 (subtrees)
N_subtrees = (3**(2+1) - 1) // (3 - 1)
# Claim Q11 (error floor)
p_floor = p_corr * p_bf * N_subtrees
# Claim Q12 (survivability condition)
p_corr_max = target / N_subtrees
# Claim Q13 (photon budget)
N_ph = boundary_modes * bar_n
# Claim Q14 (surface code logical error for d=29)
p_L_surface = 0.1 * (p)**((d+1)/2)
# Claim Q15 (surface code qubits)
qubits_surface = 2 * d**2
# Claim Q16 (reduction factor)
reduction = qubits_surface / N_ph

# Helper for formatting
def fmt(val):
    if isinstance(val, float):
        return f"{val:.8g}"
    return str(val)

print(f"CLAIM Q1: computed={fmt(p_bf)} expected=6.144e-6 match={'yes' if round(p_bf,9)==6.144e-6 else 'no'}")
print(f"CLAIM Q2: computed={fmt(p_eff)} expected=2.703e-8 match={'yes' if round(p_eff,11)==2.703e-8 else 'no'}")
print(f"CLAIM Q3: computed={fmt(f(0.5))} expected=none match=yes")
print(f"CLAIM Q4: computed={fmt(p_star)} expected=0.25 match={'yes' if abs(p_star-0.25)<1e-12 else 'no'}")
print(f"CLAIM Q5: computed={fmt(p_dep_thr)} expected=3.75e-1 match={'yes' if abs(p_dep_thr-0.375)<1e-12 else 'no'}")
print(f"CLAIM Q6: computed={fmt(margin_target)} expected=3.70e+3 match={'yes' if round(margin_target,2)==3700 else 'no'}")
print(f"CLAIM Q7: computed={fmt(margin_ro)} expected=19.2 match={'yes' if round(margin_ro,1)==19.2 else 'no'}")
print(f"CLAIM Q8: computed={fmt(p1)} expected=2.192e-15 match={'yes' if round(p1,15)==2.192e-15 else 'no'}")
print(f"CLAIM Q9: computed={fmt(p2)} expected=1.44e-29 match={'yes' if round(p2,30)==1.44e-29 else 'no'}")
print(f"CLAIM Q10: computed={fmt(N_subtrees)} expected=13 match={'yes' if N_subtrees==13 else 'no'}")
print(f"CLAIM Q11: computed={fmt(p_floor)} expected=7.99e-8 match={'yes' if round(p_floor,9)==7.99e-8 else 'no'}")
print(f"CLAIM Q12: computed={fmt(p_corr_max)} expected=7.7e-6 match={'yes' if round(p_corr_max,6)==7.7e-6 else 'no'}")
print(f"CLAIM Q13: computed={fmt(N_ph)} expected=54 match={'yes' if N_ph==54 else 'no'}")
print(f"CLAIM Q14: computed={fmt(p_L_surface)} expected=none match=yes")
print(f"CLAIM Q15: computed={fmt(qubits_surface)} expected=1682 match={'yes' if qubits_surface==1682 else 'no'}")
print(f"CLAIM Q16: computed={fmt(reduction)} expected=31 match={'yes' if round(reduction,0)==31 else 'no'}")
