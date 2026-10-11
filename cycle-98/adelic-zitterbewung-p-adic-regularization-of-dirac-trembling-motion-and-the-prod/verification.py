import math

def check(cid, computed, expected):
    if expected is None:
        print(f"CLAIM {cid}: computed={computed:.6e} expected=None match=no")
        return False
    ok = math.isclose(computed, expected, rel_tol=1e-6)
    print(f"CLAIM {cid}: computed={computed:.6e} expected={expected:.6e} match={'yes' if ok else 'no'}")
    return ok

results = []

# Q1: m_e c^2
m_e = 9.109e-31
c = 2.998e8
E = m_e * c**2
results.append(check("Q1", E, 8.187173e-14))

# Q2: omega_inf = 2 m_e c^2 / hbar
hbar = 1.055e-34
omega = 2 * m_e * c**2 / hbar
results.append(check("Q2", omega, 1.552071e21))

# Q3: f_inf = omega / (2 pi)
f = omega / (2 * math.pi)
results.append(check("Q3", f, 2.470197e20))

# Q4: lambda_C = hbar / (m_e c)
lam = hbar / (m_e * c)
results.append(check("Q4", lam, 3.863226e-13))

# Q5: l_P = sqrt(hbar G / c^3)
G = 6.674e-11
lP = math.sqrt(hbar * G / c**3)
results.append(check("Q5", lP, 1.616486e-35))

# Q6: product formula for x = 6
x = 6
val6 = abs(x) * (0.5) * (1/3)
results.append(check("Q6", val6, 1.0))

# Q7: product formula for x = 12
x = 12
val12 = abs(x) * (0.25) * (1/3)
results.append(check("Q7", val12, 1.0))

# Q8: product formula for x = 10
x = 10
val10 = abs(x) * (0.5) * (0.2)
results.append(check("Q8", val10, 1.0))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")
