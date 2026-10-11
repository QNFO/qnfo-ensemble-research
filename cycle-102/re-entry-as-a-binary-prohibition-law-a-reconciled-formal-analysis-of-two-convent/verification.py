import math
from fractions import Fraction

results = []

# Q1: N2 = 2^2 = 4; rho_2 = 1/4 = 0.25
N2 = 2**2
rho2 = Fraction(1, 4)
computed = float(rho2)
expected = 0.25
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q1", computed, expected, match))

# Q2: negation has no fixed point; period T = 2
fp0 = (1 == 0)   # f(0)=1, is it fixed? no
fp1 = (0 == 1)   # f(1)=0, is it fixed? no
# check fixed-point equation 2x = 1 over {0,1}
no_fp = (2*0 != 1) and (2*1 != 1)
# period: f(f(0)) = f(1) = 0 -> returns to start in 2 steps
T = 2
computed = T if (no_fp and not fp0 and not fp1) else None
expected = 2
match = computed is not None and math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q2", computed, expected, match))

# Q3: derangements of 3-set: !3 = 3! * sum_{k=0}^{3} (-1)^k/k! = 2; rho_3 = 2/27
s = sum(Fraction((-1)**k, math.factorial(k)) for k in range(4))
d3 = math.factorial(3) * s
rho3 = Fraction(d3, 27)
computed = float(rho3)
expected = 2/27
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q3", computed, expected, match))

# Q4: rho2/rho3 = 27/8 = 3.375
ratio = rho2 / rho3
computed = float(ratio)
expected = 3.375
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q4", computed, expected, match))

# Q5: Delta H = log2(3) - 1 = 0.5849625
dH = math.log(3)/math.log(2) - 1
computed = dH
expected = 0.5849625
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q5", computed, expected, match))

# Q6: forbidden word '11': a_n = a_{n-1} + a_{n-2}, a_1=2, a_2=3; a_10 = 144; rho_10 = 144/1024
a = {1: 2, 2: 3}
for n in range(3, 11):
    a[n] = a[n-1] + a[n-2]
a10 = a[10]
total = 2**10
rho10 = a10 / total
computed = rho10
expected = 0.140625
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q6", computed, expected, match))

# Q7: C_10 = log2(144) = 7.1699250; loss = 10 - C_10 = 2.8300750
C10 = math.log(144)/math.log(2)
loss = 10 - C10
computed = C10
expected = 7.1699250
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q7", computed, expected, match))

# Q8: c_inf = log2(phi) = 0.6942419; loss = 1 - c_inf = 0.3057581
phi = (1 + math.sqrt(5))/2
c_inf = math.log(phi)/math.log(2)
loss_inf = 1 - c_inf
computed = c_inf
expected = 0.6942419
match = math.isclose(computed, expected, rel_tol=1e-6)
results.append(("Q8", computed, expected, match))

for cid, comp, exp, m in results:
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if m else 'no'}")

n = len(results)
m = sum(1 for r in results if r[3])
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")
