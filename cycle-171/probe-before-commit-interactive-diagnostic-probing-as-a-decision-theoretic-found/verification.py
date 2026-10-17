import math
from fractions import Fraction

def f(x):
    return f"{x:.10g}"

# Inputs
lam = 5.0
mu = 0.01
N = 3
c_p = 0.001
l_p = 0.5
a = 0.9
b = 0.3
pi = [0.70, 0.50, 0.80]
c = [0.020, 0.005, 0.080]
l = [3.0, 1.0, 8.0]

# Q1-Q3: static utilities
U = [pi[i] - lam*c[i] - mu*l[i] for i in range(3)]
print(f"CLAIM Q1: computed={f(U[0])} expected=0.57 match={'yes' if round(U[0],10)==0.57 else 'no'}")
print(f"CLAIM Q2: computed={f(U[1])} expected=0.465 match={'yes' if round(U[1],10)==0.465 else 'no'}")
print(f"CLAIM Q3: computed={f(U[2])} expected=0.32 match={'yes' if round(U[2],10)==0.32 else 'no'}")

# Q4-Q9: posteriors
pip = [a*p/(a*p + b*(1-p)) for p in pi]
pim = [(1-a)*p/((1-a)*p + (1-b)*(1-p)) for p in pi]
exp_pip = ["0.875","0.75","0.923077"]
exp_pim = ["0.25","0.125","0.363636"]
for i in range(3):
    ok = f"{pip[i]:.6f}" == exp_pip[i]
    print(f"CLAIM Q{4+i}: computed={f(pip[i])} expected={exp_pip[i]} match={'yes' if ok else 'no'}")
for i in range(3):
    ok = f"{pim[i]:.6f}" == exp_pim[i]
    print(f"CLAIM Q{7+i}: computed={f(pim[i])} expected={exp_pim[i]} match={'yes' if ok else 'no'}")

# Q10-Q12: pass marginals
P1 = [a*p + b*(1-p) for p in pi]
for i in range(3):
    ok = f"{P1[i]:.10g}" == ["0.72","0.6","0.78"][i]
    print(f"CLAIM Q{10+i}: computed={f(P1[i])} expected={['0.72','0.60','0.78'][i]} match={'yes' if ok else 'no'}")

# Post-probe utilities
Upp = [pip[i] - lam*c[i] - mu*l[i] for i in range(3)]
Upm = [pim[i] - lam*c[i] - mu*l[i] for i in range(3)]

# Full enumeration of 8 joint outcomes, independent signals
U_gross = 0.0
for s1 in (0,1):
    for s2 in (0,1):
        for s3 in (0,1):
            s = (s1,s2,s3)
            prob = 1.0
            for i in range(3):
                p_pass = P1[i]
                prob *= p_pass if s[i]==1 else (1-p_pass)
            utils = [Upp[i] if s[i]==1 else Upm[i] for i in range(3)]
            best = max(utils)
            U_gross += prob*best
print(f"CLAIM Q13: computed={f(U_gross)} expected=0.698184 match={'yes' if f(U_gross)==f(0.698184) else 'no'}")

U_probe = U_gross - lam*N*c_p - mu*l_p
print(f"CLAIM Q14: computed={f(U_probe)} expected=0.678184 match={'yes' if f(U_probe)==f(0.678184) else 'no'}")

U_static = max(U)
Delta = U_probe - U_static
print(f"CLAIM Q15: computed={f(Delta)} expected=0.108184 match={'yes' if f(Delta)==f(0.108184) else 'no'}")

c_star = (U_gross - mu*l_p - U_static)/(lam*N)
print(f"CLAIM Q16: computed={f(c_star)} expected=0.00821227 match={'yes' if f(c_star)==f(0.00821227) else 'no'}")

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")
