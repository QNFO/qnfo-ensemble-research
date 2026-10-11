import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

# Q1: E_T(1 K)
k_B = 8.617333e-5  # eV/K
E1 = k_B * 1.0
print(f"CLAIM Q1: computed={E1:.6e} expected=8.617333e-05 match={'yes' if isclose(E1, 8.617333e-5) else 'no'}")

# Q2: E_T(0.1 K)
E2 = k_B * 0.1
print(f"CLAIM Q2: computed={E2:.6e} expected=8.617333e-06 match={'yes' if isclose(E2, 8.617333e-6) else 'no'}")

# Q3: E_T(20 K)
E3 = k_B * 20.0
print(f"CLAIM Q3: computed={E3:.6e} expected=1.7234666e-03 match={'yes' if isclose(E3, 1.7234666e-3) else 'no'}")

# Q4: ratio E_T(1K)/E_T(0.1K)
ratio = E1 / E2
print(f"CLAIM Q4: computed={ratio:.6f} expected=10.0 match={'yes' if isclose(ratio, 10.0) else 'no'}")

# Q5: solve tanh(x/2) - 2/x = 0 by bisection
def g(x):
    return math.tanh(x / 2.0) - 2.0 / x

lo, hi = 2.0, 3.0
for _ in range(200):
    mid = (lo + hi) / 2.0
    if g(lo) * g(mid) <= 0:
        hi = mid
    else:
        lo = mid
x_star = (lo + hi) / 2.0
print(f"CLAIM Q5: computed={x_star:.6f} expected=2.3993 match={'yes' if isclose(x_star, 2.3993, ) or abs(x_star-2.3993)<5e-4 else 'no'}")

# Q6: C_max/R at x*
C_over_R = x_star**2 / (4.0 * math.cosh(x_star / 2.0)**2)
print(f"CLAIM Q6: computed={C_over_R:.6f} expected=0.439 match={'yes' if isclose(C_over_R, 0.439) or abs(C_over_R-0.439)<5e-4 else 'no'}")

# Q7: C_max = (C_max/R)*R
R = 8.314  # J/mol/K
C_max = C_over_R * R
print(f"CLAIM Q7: computed={C_max:.6f} expected=3.65 match={'yes' if abs(C_max-3.65)<5e-3 else 'no'}")

# Q8: coefficient 1/x*
coeff = 1.0 / x_star
print(f"CLAIM Q8: computed={coeff:.6f} expected=0.4168 match={'yes' if abs(coeff-0.4168)<5e-4 else 'no'}")

n = 8
m = sum([
    isclose(E1, 8.617333e-5),
    isclose(E2, 8.617333e-6),
    isclose(E3, 1.7234666e-3),
    isclose(ratio, 10.0),
    abs(x_star - 2.3993) < 5e-4,
    abs(C_over_R - 0.439) < 5e-4,
    abs(C_max - 3.65) < 5e-3,
    abs(coeff - 0.4168) < 5e-4,
])
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
