import math

def round_sig(x, sig):
    if x == 0:
        return 0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Q1
R = (2 + 3) / 2
expected_Q1 = 2.5
match_Q1 = "yes" if abs(R - expected_Q1) < 1e-12 else "no"
print(f"CLAIM Q1: computed={R} expected={expected_Q1} match={match_Q1}")

# Q2
w = 2.0  # µm
R_factor = 2.5
a_PnC = w / math.sqrt(R_factor)
expected_Q2 = 1.265  # µm
match_Q2 = "yes" if abs(a_PnC - expected_Q2) < 1e-3 else "no"
print(f"CLAIM Q2: computed={a_PnC:.6f} expected={expected_Q2} match={match_Q2}")

# Q3
v_s = 5e3  # m/s
omega_prot = 1.5e13  # Hz
a_target = (2 * math.pi * v_s) / omega_prot  # meters
a_target_nm = a_target * 1e9  # convert to nm
expected_Q3 = 2.09  # nm
match_Q3 = "yes" if abs(a_target_nm - expected_Q3) < 1e-2 else "no"
print(f"CLAIM Q3: computed={a_target_nm:.6f} expected={expected_Q3} match={match_Q3}")

# Q4
J = 100.0  # cm^-1
Delta = 50.0  # cm^-1
k_max_cm = J**2 / abs(Delta)
k_max_Hz = k_max_cm * 2.998e10
expected_Q4 = 5.996e12  # Hz
match_Q4 = "yes" if abs(k_max_Hz - expected_Q4) < 1e6 else "no"
print(f"CLAIM Q4: computed={k_max_Hz:.6e} expected={expected_Q4:.6e} match={match_Q4}")

# Q5
tau_tr = 1.0 / k_max_Hz  # seconds
tau_tr_ps = tau_tr * 1e12  # picoseconds
expected_Q5 = 0.167  # ps
match_Q5 = "yes" if abs(tau_tr_ps - expected_Q5) < 1e-3 else "no"
print(f"CLAIM Q5: computed={tau_tr_ps:.6f} expected={expected_Q5} match={match_Q5}")

# Q6
f = 0.10
x = math.sqrt(4 * f)
nu0 = 100.0  # cm^-1
A = x * nu0
expected_Q6 = 63.2  # cm^-1
match_Q6 = "yes" if abs(A - expected_Q6) < 1e-1 else "no"
print(f"CLAIM Q6: computed={A:.4f} expected={expected_Q6} match={match_Q6}")

# Q7
h_c = 1.9865e-23  # J·cm
k_B = 1.3806e-23  # J/K
nu = 100.0  # cm^-1
T = 300.0  # K
exponent = (h_c * nu) / (k_B * T)
n_bar = 1.0 / (math.exp(exponent) - 1.0)
expected_Q7 = 1.63
match_Q7 = "yes" if abs(n_bar - expected_Q7) < 1e-2 else "no"
print(f"CLAIM Q7: computed={n_bar:.6f} expected={expected_Q7} match={match_Q7}")

# Q8
v_s2 = 2e4  # m/s
nu_gap = 3.0e12  # Hz
p = v_s2 / (2 * nu_gap)  # meters
p_nm = p * 1e9  # nm
density_per_m2 = 1.0 / (p ** 2)
density_per_um2 = density_per_m2 * 1e-12  # convert m^-2 to µm^-2
expected_p = 3.3  # nm
expected_density = 9.2e4  # µm^-2
match_p = "yes" if abs(p_nm - expected_p) < 0.1 else "no"
match_density = "yes" if abs(density_per_um2 - expected_density) / expected_density < 0.02 else "no"
print(f"CLAIM Q8: computed=p={p_nm:.3f} nm, density={density_per_um2:.1e} µm^-2 expected=p≈{expected_p} nm, density≈{expected_density:.1e} µm^-2 match={match_p}&{match_density}")

# Q9
d = 9.0  # mm
L = 125.0  # mm
AR = L / d
expected_Q9 = 13.9
match_Q9 = "yes" if abs(AR - expected_Q9) < 0.05 else "no"
print(f"CLAIM Q9: computed={AR:.3f} expected={expected_Q9} match={match_Q9}")

# Q10
ell = 45.0  # mm
r = 2.5  # mm
V = math.pi * r**2 * ell
expected_Q10 = 884.0  # mm^3
match_Q10 = "yes" if abs(V - expected_Q10) < 1.0 else "no"
print(f"CLAIM Q10: computed={V:.2f} expected={expected_Q10} match={match_Q10}")

# Q11
eta_white = 0.667
eta_Lor = eta_white * 1.10
expected_eta_Lor = 0.733
match_Q11 = "yes" if abs(eta_Lor - expected_eta_Lor) < 0.005 else "no"
print(f"CLAIM Q11: computed={eta_Lor:.3f} expected={expected_eta_Lor} match={match_Q11}")

print(f"VERIFICATION SUMMARY: 11 claims, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_p,match_Q9,match_Q10,match_Q11].count('yes'))} match, {sum([match_Q1,match_Q2,match_Q3,match_Q4,match_Q5,match_Q6,match_Q7,match_p,match_Q9,match_Q10,match_Q11].count('no'))} mismatch")
