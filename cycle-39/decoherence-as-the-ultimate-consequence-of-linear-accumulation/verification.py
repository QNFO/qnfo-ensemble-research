import math

claims = []

# Q1: C = exp(-N*sigma_phi^2/2), sigma_phi=1e-3, N=1e6
sigma_phi = 1e-3
N = 1e6
C = math.exp(-N * sigma_phi**2 / 2)
claims.append(("Q1", C, math.exp(-0.5)))

# Q2: T2 = 2/(Gamma_kick * sigma_phi^2), Gamma_kick=1e4
Gamma_kick = 1e4
T2 = 2 / (Gamma_kick * sigma_phi**2)
claims.append(("Q2", T2, 200.0))

# Q3: T2' = 2/(Gamma_kick' * sigma_phi^2), Gamma_kick'=1e3
Gamma_kick_p = 1e3
T2p = 2 / (Gamma_kick_p * sigma_phi**2)
claims.append(("Q3", T2p, 2000.0))

# Q4: t_cycle = 1/f, f=40e6
f = 40e6
t_cycle = 1 / f
claims.append(("Q4", t_cycle, 2.5e-8))

# Q5: ratio = t_cycle / t_Z, t_Z=1e-15
t_Z = 1e-15
ratio = t_cycle / t_Z
claims.append(("Q5", ratio, 2.5e7))

# Q6: T2 = 1/(N1*Gamma_k), N1=1e5, Gamma_k=1e-10
N1 = 1e5
Gamma_k = 1e-10
T2_1 = 1 / (N1 * Gamma_k)
claims.append(("Q6", T2_1, 1e5))

# Q7: T2 = 1/(N2*Gamma_k), N2=1e9
N2 = 1e9
T2_2 = 1 / (N2 * Gamma_k)
claims.append(("Q7", T2_2, 10.0))

# Q8: ratio = N2/N1
ratio_T = N2 / N1
claims.append(("Q8", ratio_T, 1e4))

match_count = 0
for cid, computed, expected in claims:
    match = math.isclose(computed, expected, rel_tol=1e-6)
    if match:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(claims)} claims, {match_count} match, {len(claims) - match_count} mismatch")
