import math
from fractions import Fraction

def report(cid, computed, expected, tol=1e-6):
    if expected is None:
        match = "no"
    else:
        match = "yes" if math.isclose(computed, expected, rel_tol=tol) else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match

results = []

# Q1: R = (1/N) * sum s_i, N=10, s=[1]*8+[0]*2
s = [1,1,1,1,1,1,1,1,0,0]
N = 10
R = sum(s) / N
results.append(report("Q1", R, 0.80))

# Q2: P(X=8) = C(10,8) * 0.5^10
p0 = 0.5
P8 = math.comb(10, 8) * p0**8 * (1-p0)**2
results.append(report("Q2", P8, 45/1024))

# Q3: P(X>=8) = (C(10,8)+C(10,9)+C(10,10)) / 2^10
tail = (math.comb(10,8) + math.comb(10,9) + math.comb(10,10)) / 2**10
results.append(report("Q3", tail, 56/1024))

# Q4: Emax/Emin = 1000/500
ratio = 1000 / 500
results.append(report("Q4", ratio, 2.0))

# Q5: dE_J = (1000-500) GeV * 1e9 eV/GeV * 1.602e-19 J/eV
dE_J = (1000 - 500) * 1e9 * 1.602e-19
results.append(report("Q5", dE_J, 8.01e-8))

# Q6: p_fail = 1 - (1-1e-3)^4
n, eps = 4, 1e-3
p_fail = 1 - (1 - eps)**n
results.append(report("Q6", p_fail, 0.003994001999))

# Q7: eps_max = 1 - (1-0.01)^(1/4)
p_star = 0.01
eps_max = 1 - (1 - p_star)**(1/n)
results.append(report("Q7", eps_max, 0.00250943))

# Q8: eps_single / eps_max = 0.01 / eps_max
eps_single = 0.01
tight = eps_single / eps_max
results.append(report("Q8", tight, 3.98497))

n_match = sum(1 for r in results if r == "yes")
n_mismatch = len(results) - n_match
print(f"VERIFICATION SUMMARY: {len(results)} claims, {n_match} match, {n_mismatch} mismatch")
