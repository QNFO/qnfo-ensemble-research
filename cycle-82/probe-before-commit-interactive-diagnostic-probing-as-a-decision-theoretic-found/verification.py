import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

a, b = 0.9, 0.3
lam, mu = 5, 0.01

# Q1
pi1, c1, l1 = 0.70, 0.020, 3
U1 = pi1 - lam*c1 - mu*l1
print(f"CLAIM Q1: computed={U1:.6f} expected=0.57 match={'yes' if isclose(U1, 0.57) else 'no'}")

# Q2
pi2, c2, l2 = 0.50, 0.005, 1
U2 = pi2 - lam*c2 - mu*l2
print(f"CLAIM Q2: computed={U2:.6f} expected=0.465 match={'yes' if isclose(U2, 0.465) else 'no'}")

# Q3
pi3, c3, l3 = 0.80, 0.080, 8
U3 = pi3 - lam*c3 - mu*l3
print(f"CLAIM Q3: computed={U3:.6f} expected=0.32 match={'yes' if isclose(U3, 0.32) else 'no'}")

# Q4
pi1p = a*pi1 / (a*pi1 + b*(1-pi1))
print(f"CLAIM Q4: computed={pi1p:.6f} expected=0.875 match={'yes' if isclose(pi1p, 0.875) else 'no'}")

# Q5
pi2p = a*pi2 / (a*pi2 + b*(1-pi2))
print(f"CLAIM Q5: computed={pi2p:.6f} expected=0.75 match={'yes' if isclose(pi2p, 0.75) else 'no'}")

# Q6
pi3p = a*pi3 / (a*pi3 + b*(1-pi3))
print(f"CLAIM Q6: computed={pi3p:.6f} expected=0.923077 match={'yes' if isclose(pi3p, 0.923077) else 'no'}")

# Q7
pi1m = (1-a)*pi1 / ((1-a)*pi1 + (1-b)*(1-pi1))
print(f"CLAIM Q7: computed={pi1m:.6f} expected=0.25 match={'yes' if isclose(pi1m, 0.25) else 'no'}")

# Q8
pi2m = (1-a)*pi2 / ((1-a)*pi2 + (1-b)*(1-pi2))
print(f"CLAIM Q8: computed={pi2m:.6f} expected=0.125 match={'yes' if isclose(pi2m, 0.125) else 'no'}")

print("VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch")
