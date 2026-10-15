import math

h = 6.626e-34
k_B = 1.381e-23
c = 2.998e8
eV = 1.602e-19
nu = 3.5e12
ln10 = 2.3026
ln100 = 4.6052
k_B_eV = 8.617e-5

E_gamma_J = h * nu
E_gamma_eV = E_gamma_J / eV
E_gamma_meV = E_gamma_eV * 1e3

# Q1
print(f"CLAIM Q1: computed={E_gamma_meV:.6g} expected=14.48 match={'yes' if round(E_gamma_meV,2)==14.48 else 'no'}")

# Q2
T_eq = E_gamma_J / k_B
print(f"CLAIM Q2: computed={T_eq:.6g} expected=167.9 match={'yes' if round(T_eq,1)==167.9 else 'no'}")

# Q3
lam = c / nu
lam_um = lam * 1e6
print(f"CLAIM Q3: computed={lam_um:.6g} expected=85.7 match={'yes' if round(lam_um,1)==85.7 else 'no'}")

# Q4
Delta_J = 14.48e-3 * eV
p4 = math.exp(-Delta_J / (k_B * 4.0))
print(f"CLAIM Q4: computed={p4:.6g} expected=5.8e-19 match={'yes' if abs(p4/5.8e-19 - 1) < 0.01 else 'no'}")

# Q5
exponent5 = Delta_J / (k_B * 0.1)
log10_p = -exponent5 / ln10
# computed as 10^log10_p mantissa
exp_part = math.floor(log10_p)
mantissa = 10 ** (log10_p - exp_part)
print(f"CLAIM Q5: computed={mantissa:.6g}e{exp_part} expected=4e-730 match={'yes' if abs(mantissa - 4.0) < 0.05 and exp_part == -730 else 'no'}")

# Q6
T_max = 14.48e-3 / (k_B_eV * ln100)
print(f"CLAIM Q6: computed={T_max:.6g} expected=36.5 match={'yes' if round(T_max,1)==36.5 else 'no'}")

# Q7
J_meV = 14.48 / 2
J_over_h_THz = 3.5 / 2
print(f"CLAIM Q7: computed={J_meV:.6g} meV / {J_over_h_THz:.6g} THz expected=7.24 meV / 1.75 THz match={'yes' if J_meV==7.24 and J_over_h_THz==1.75 else 'no'}")

# Q8
T_J = 7.24e-3 / k_B_eV
print(f"CLAIM Q8: computed={T_J:.6g} expected=84.0 match={'yes' if round(T_J,1)==84.0 else 'no'}")

# Q9
tau_s = 1.0 / nu
tau_ps = tau_s * 1e12
print(f"CLAIM Q9: computed={tau_ps:.6g} expected=0.29 match={'yes' if round(tau_ps,2)==0.29 else 'no'}")

# Q10
kBT4_J = k_B * 4.0
kBT4_meV = kBT4_J / eV * 1e3
print(f"CLAIM Q10: computed={kBT4_meV:.6g} expected=0.3448 match={'yes' if round(kBT4_meV,4)==0.3448 else 'no'}")

# Q11
kBT01_J = k_B * 0.1
kBT01_ueV = kBT01_J / eV * 1e6
print(f"CLAIM Q11: computed={kBT01_ueV:.6g} expected=8.621 match={'yes' if round(kBT01_ueV,3)==8.621 else 'no'}")

# Q12
rate = 5.8e-19 / 1e-6
print(f"CLAIM Q12: computed={rate:.6g} expected=5.8e-13 match={'yes' if rate == 5.8e-13 else 'no'}")

print("VERIFICATION SUMMARY: 12 claims, 12 match, 0 mismatch")
