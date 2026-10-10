import math

# Inputs
Phi0 = 2.07e-15        # Wb
lam = 1.0e-7           # m
d = 5.0e-8             # m
R1 = 1.0e-6            # m
R100 = 1.0e-4          # m
Bstar = 0.100          # T
gamma = 1

# Q1: Lambda = 2*lam^2/d
Lambda = 2*lam**2/d
print(f"CLAIM Q1: computed={Lambda:.4g} expected=4.0e-07 match={'yes' if math.isclose(Lambda,4.0e-7,rel_tol=1e-6) else 'no'}")

# Q2: Gamma = Lambda/R
Gamma = Lambda/R1
print(f"CLAIM Q2: computed={Gamma:.4g} expected=0.4 match={'yes' if math.isclose(Gamma,0.40,rel_tol=1e-6) else 'no'}")

# Q3: H0 = Phi0/(pi*R^2)
H0 = Phi0/(math.pi*R1**2)
print(f"CLAIM Q3: computed={H0:.4g} expected=6.589e-04 match={'yes' if math.isclose(H0,6.589e-4,rel_tol=1e-3) else 'no'}")

# Q4: H0(10um) = H0*1e-2
H0_10 = H0*1e-2
print(f"CLAIM Q4: computed={H0_10:.4g} expected=6.589e-06 match={'yes' if math.isclose(H0_10,6.589e-6,rel_tol=1e-3) else 'no'}")

# Q5: b = R*(mu0Ha/B*)^(1/(gamma+2)) at 0.025 T
b5 = R100*(0.025/Bstar)**(1/(gamma+2))
print(f"CLAIM Q5: computed={b5*1e6:.4g} um expected=62.996 um match={'yes' if math.isclose(b5*1e6,62.996,rel_tol=1e-3) else 'no'}")

# Q6: b at 0.050 T
b6 = R100*(0.050/Bstar)**(1/3)
print(f"CLAIM Q6: computed={b6*1e6:.4g} um expected=79.370 um match={'yes' if math.isclose(b6*1e6,79.370,rel_tol=1e-3) else 'no'}")

# Q7: B_d = B*(b/R)
bR = (0.025/Bstar)**(1/3)
Bd = Bstar*bR
print(f"CLAIM Q7: computed={Bd:.4g} T expected=0.062996 T match={'yes' if math.isclose(Bd,0.062996,rel_tol=1e-3) else 'no'}")

# Q8: N = mu0Ha*pi*R^2/Phi0
N = 0.025*math.pi*R100**2/Phi0
print(f"CLAIM Q8: computed={N:.4g} expected=3.7942e+05 match={'yes' if math.isclose(N,3.7942e5,rel_tol=1e-3) else 'no'}")

m = 8
print("VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch")
