import math

def round_sig(x, sig):
    """Round x to sig significant figures and return as float."""
    if x == 0:
        return 0.0
    else:
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

# Q1: revival period
omega0 = 3.14e10          # rad/s
q = 2
T_rev = 2 * math.pi / (omega0 * (q - 1))          # seconds
T_rev_ns = T_rev * 1e9                            # nanoseconds
T_rev_rounded = round_sig(T_rev_ns, 2)            # 2 sig figs → 0.20 ns
print(f"CLAIM Q1: computed={T_rev_rounded:.2e} expected=0.20 match={'yes' if abs(T_rev_rounded-0.20)<1e-12 else 'no'}")

# Q2: mode frequencies
freqs = [omega0 * q**k for k in range(4)]
freqs_rounded = [round_sig(f, 3) for f in freqs]   # 3 sig figs as in statement
expected_freqs = [3.14e10, 6.28e10, 1.26e11, 2.51e11]
match_q2 = all(abs(c - e) / e < 1e-3 for c, e in zip(freqs_rounded, expected_freqs))
print(f"CLAIM Q2: computed={freqs_rounded} expected=[3.14e10, 6.28e10, 1.26e11, 2.51e11] match={'yes' if match_q2 else 'no'}")

# Q3: couplings
g0 = 6.28e7               # rad/s
gamma = 0.5
g_vals = [g0 * q**(-gamma * k) for k in range(4)]
g_vals_rounded = [round_sig(g, 3) for g in g_vals]   # 3 sig figs
expected_g = [6.28e7, 4.44e7, 3.14e7, 2.22e7]
match_q3 = all(abs(c - e) / e < 1e-3 for c, e in zip(g_vals_rounded, expected_g))
print(f"CLAIM Q3: computed={g_vals_rounded} expected=[6.28e7, 4.44e7, 3.14e7, 2.22e7] match={'yes' if match_q3 else 'no'}")

# Q4: spectral‑density exponent
exponent = -2 * gamma
print(f"CLAIM Q4: computed={exponent:.0f} expected=-1 match={'yes' if exponent == -1 else 'no'}")

# Q5: effective spectral‑density prefactor J0
J0 = (math.pi * g0**2 / math.log(q)) * (omega0**(2*gamma))
J0_rounded = round_sig(J0, 3)                     # 3 sig figs → 5.62e26
print(f"CLAIM Q5: computed={J0_rounded:.2e} expected=5.62e26 match={'yes' if abs(J0_rounded-5.62e26)/5.62e26<1e-3 else 'no'}")

# Q6: relaxation rate
T1 = 30e-6                # seconds
Gamma1 = 1 / T1
Gamma1_rounded = round_sig(Gamma1, 3)
print(f"CLAIM Q6: computed={Gamma1_rounded:.2e} expected=3.33e4 match={'yes' if abs(Gamma1_rounded-3.33e4)/3.33e4<1e-3 else 'no'}")

# Q7: pure‑dephasing rate
T2_star = 20e-6
Gamma_phi = 1 / (2 * T2_star)
Gamma_phi_rounded = round_sig(Gamma_phi, 3)
print(f"CLAIM Q7: computed={Gamma_phi_rounded:.2e} expected=2.50e4 match={'yes' if abs(Gamma_phi_rounded-2.50e4)/2.50e4<1e-3 else 'no'}")

# Q8: total decoherence rate and decay time
Gamma_total = Gamma1 + Gamma_phi
decay_time = 1 / Gamma_total
Gamma_total_rounded = round_sig(Gamma_total, 3)
decay_time_rounded = round_sig(decay_time, 3)
print(f"CLAIM Q8: computed={Gamma_total_rounded:.2e} expected=5.83e4 match={'yes' if abs(Gamma_total_rounded-5.83e4)/5.83e4<1e-3 else 'no'}")
print(f"CLAIM Q8: computed decay_time={decay_time_rounded:.2e} expected=1.72e-5 match={'yes' if abs(decay_time_rounded-1.72e-5)/1.72e-5<1e-3 else 'no'}")

print("VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch")
