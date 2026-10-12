import math

hbar = 1.055e-34
m_e = 9.109e-31
gamma = 1e9
k = 1e7

# Q1: Q_q(x) = hbar*omega/2 - m*omega^2*x^2/2, check at a sample x with omega=1, m=1, hbar=1
omega = 1.0
m = 1.0
x = 0.7
sigma2 = hbar / (m * omega)  # symbolic; use dimensionless hbar=m=omega=1 for check
hbar_d, m_d, omega_d = 1.0, 1.0, 1.0
sigma2_d = hbar_d / (m_d * omega_d)
sqrt_rho = math.exp(-x**2 / (2 * sigma2_d))
d2_sqrt_rho = (x**2 / sigma2_d**2 - 1.0 / sigma2_d) * sqrt_rho
Qq_computed = -(hbar_d**2 / (2 * m_d)) * d2_sqrt_rho / sqrt_rho
Qq_expected = hbar_d * omega_d / 2 - m_d * omega_d**2 * x**2 / 2
match1 = math.isclose(Qq_computed, Qq_expected, rel_tol=1e-6)
print(f"CLAIM Q1: computed={Qq_computed:.6f} expected={Qq_expected:.6f} match={'yes' if match1 else 'no'}")

# Q2: Omega = -i*gamma/2 ± sqrt(hbar^2 k^4/(4m^2) - gamma^2/4); check decay rate = gamma/2
# Solve quadratic Omega^2 + i*gamma*Omega - hbar^2 k^4/(4 m^2) = 0 numerically (complex)
A = 1.0
B = 1j * gamma
C = -(hbar**2 * k**4) / (4 * m_e**2)
disc = B * B - 4 * A * C
O1 = (-B + math.sqrt(complex(disc).real if abs(complex(disc).imag) < 1e-30 else 0) * 1j) / 2 if False else (-B + complex(disc) ** 0.5) / 2
O2 = (-B - complex(disc) ** 0.5) / 2
decay1 = -O1.imag
decay2 = -O2.imag
match2 = math.isclose(decay1, gamma / 2, rel_tol=1e-6) and math.isclose(decay2, gamma / 2, rel_tol=1e-6)
print(f"CLAIM Q2: computed={decay1:.6e} expected={gamma/2:.6e} match={'yes' if match2 else 'no'}")

# Q3: tau_lin = 2/gamma
tau = 2 / gamma
expected3 = 2.0e-9
match3 = math.isclose(tau, expected3, rel_tol=1e-6)
print(f"CLAIM Q3: computed={tau:.6e} expected={expected3:.6e} match={'yes' if match3 else 'no'}")

# Q4: crossover = hbar*k^2/m
cross = hbar * k**2 / m_e
expected4 = 1.16e10
match4 = math.isclose(cross, expected4, rel_tol=1e-2)
print(f"CLAIM Q4: computed={cross:.6e} expected={expected4:.6e} match={'yes' if match4 else 'no'}")

# Q5: omega_k = hbar*k^2/(2m)
wk = hbar * k**2 / (2 * m_e)
expected5 = 5.8e9
match5 = math.isclose(wk, expected5, rel_tol=1e-2)
print(f"CLAIM Q5: computed={wk:.6e} expected={expected5:.6e} match={'yes' if match5 else 'no'}")

# Q6: E(t) = E0 exp(-2 gamma t); verify dE/dt = -2 gamma E at t=1
t = 1.0
E0 = 1.0
dEdt = -2 * gamma * E0 * math.exp(-2 * gamma * t)
E_t = E0 * math.exp(-2 * gamma * t)
match6 = math.isclose(dEdt, -2 * gamma * E_t, rel_tol=1e-6)
print(f"CLAIM Q6: computed={dEdt:.6e} expected={-2*gamma*E_t:.6e} match={'yes' if match6 else 'no'}")

# Q7: t_1->0 = ln(3)/(2 gamma)
t10 = math.log(3) / (2 * gamma)
expected7 = 0.549306 / gamma
match7 = math.isclose(t10, expected7, rel_tol=1e-6)
print(f"CLAIM Q7: computed={t10:.6e} expected={expected7:.6e} match={'yes' if match7 else 'no'}")

# Q8: t_2->1 = ln(5/3)/(2 gamma)
t21 = math.log(5 / 3) / (2 * gamma)
expected8 = 0.255413 / gamma
match8 = math.isclose(t21, expected8, rel_tol=1e-6)
print(f"CLAIM Q8: computed={t21:.6e} expected={expected8:.6e} match={'yes' if match8 else 'no'}")

n_match = sum([match1, match2, match3, match4, match5, match6, match7, match8])
print(f"VERIFICATION SUMMARY: 8 claims, {n_match} match, {8 - n_match} mismatch")
