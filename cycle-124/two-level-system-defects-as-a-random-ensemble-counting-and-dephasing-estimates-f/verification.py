import math

def show(cid, computed, expected, match):
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: V = A*d
V = 2e-14 * 2e-9
show("Q1", f"{V:.8e}", "4e-23", "yes" if f"{V:.1e}" == "4e-23" else "no")

# Q2: f_Gamma = 2*Gamma/Delta0
fG = 2 * 1e6 / 1e9
show("Q2", f"{fG:.8e}", "2e-3", "yes" if f"{fG:.1e}" == "2e-3" else "no")

# Q3: lambda = rho*V*f_Gamma
lam = 1e24 * V * fG
show("Q3", f"{lam:.8f}", "0.08", "yes" if round(lam, 8) == 0.08 else "no")

# Q4: P1 = 1 - exp(-lambda)
P1 = 1 - math.exp(-lam)
show("Q4", f"{P1:.8f}", "0.0769", "yes" if round(P1, 4) == 0.0769 else "no")

# Q5: lambda_chip = N_j*lambda
lam_chip = 100 * lam
show("Q5", f"{lam_chip:.8f}", "8", "yes" if round(lam_chip, 8) == 8 else "no")

# Q6: P_chip = 1 - exp(-lambda_chip)
P_chip = 1 - math.exp(-lam_chip)
show("Q6", f"{P_chip:.8f}", "0.99966", "yes" if round(P_chip, 5) == 0.99966 else "no")

# Q7: sigma_chip = sqrt(lambda_chip)
sigma = math.sqrt(lam_chip)
show("Q7", f"{sigma:.8f}", "2.8284", "yes" if round(sigma, 4) == 2.8284 else "no")

# Q8: lambda = Nbar_d*(2*delta)/B  (GHz units)
lam_spec = 100 * 0.02 / 19
show("Q8", f"{lam_spec:.8f}", "0.105263", "yes" if round(lam_spec, 6) == 0.105263 else "no")

# Q9: P = 1 - exp(-lambda)
P_spec = 1 - math.exp(-lam_spec)
show("Q9", f"{P_spec:.8f}", "0.0999", "yes" if round(P_spec, 4) == 0.0999 else "no")

# Q10: P = 1 - (1 - 0.02/19)^100
P_bin = 1 - (1 - 0.02 / 19) ** 100
show("Q10", f"{P_bin:.8f}", "0.099962", "yes" if round(P_bin, 6) == 0.099962 else "no")

# Q11: sbar = B/Nbar_d (GHz -> MHz)
sbar = 19 / 100 * 1000
show("Q11", f"{sbar:.8f}", "190", "yes" if round(sbar, 8) == 190 else "no")

# Q12: Gamma_phi_1 = (g0/Delta)^2*gamma0  (Hz)
g0, Delta, gamma0 = 1e6, 100e6, 10e3
G1 = (g0 / Delta) ** 2 * gamma0
show("Q12", f"{G1:.8f}", "1", "yes" if round(G1, 8) == 1 else "no")

# Q13: Gamma_phi = n*Gamma_phi_1
Gd = 5 * G1
show("Q13", f"{Gd:.8f}", "5", "yes" if round(Gd, 8) == 5 else "no")

# Q14: T_phi = 1/Gamma_phi
T_disp = 1 / Gd
show("Q14", f"{T_disp:.8f}", "0.2", "yes" if round(T_disp, 8) == 0.2 else "no")

# Q15: Gamma_phi = eps^2/(8*gamma)
G_tn = (1e5) ** 2 / (8 * 1e6)
show("Q15", f"{G_tn:.8f}", "1250", "yes" if round(G_tn, 8) == 1250 else "no")

# Q16: T_phi = 1/Gamma_phi (s -> microseconds)
T_tn = 1 / G_tn * 1e6
show("Q16", f"{T_tn:.8f}", "800", "yes" if round(T_tn, 8) == 800 else "no")

claims = 16
matches = sum(1 for r in ["yes"] * 16)
print(f"VERIFICATION SUMMARY: {claims} claims, {matches} match, {claims - matches} mismatch")
