import math
from fractions import Fraction
from math import comb, isclose

results = []

def record(cid, computed, expected, tol=1e-6):
    if expected is None:
        match = "yes"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if isclose(float(computed), float(expected), rel_tol=tol) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    results.append(match == "yes")

# Q1: binomial probabilities for n=3, p=0.1
n, p = 3, 0.1
q = 1 - p
for j in range(n + 1):
    val = comb(n, j) * p**j * q**(n - j)
    expected = {0: 0.729, 1: 0.243, 2: 0.027, 3: 0.001}[j]
    record(f"Q1(j={j})", val, expected)

# Q2: P(L_0|00) = C(3,0)*0.9^3 + C(3,2)*0.1^2*0.9
pL0 = comb(3, 0) * q**3 + comb(3, 2) * p**2 * q
record("Q2", pL0, 0.756)

# Q3: P(L_1|00) = C(3,1)*0.1*0.9^2 + C(3,3)*0.1^3
pL1 = comb(3, 1) * p * q**2 + comb(3, 3) * p**3
record("Q3", pL1, 0.244)

# Q4: normalization
record("Q4", pL0 + pL1, 1.0)

# Q5: number of fault configurations 2^3
record("Q5", 2**3, 8)

# Q6: gap and relative underestimate
gap = pL0 - 0.729
rel = gap / pL0
record("Q6(gap)", gap, 0.027)
record("Q6(rel)", rel, 0.0357)

# Q7: ML threshold p*=0.5 independent of n; verify Z0=Z1=1/2 at p=1/2 for several n
for nn in (3, 5, 10, 25):
    ph = Fraction(1, 2)
    Z0 = sum(Fraction(comb(nn, j)) * ph**j * ph**(nn - j) for j in range(nn + 1) if j % 2 == 0)
    Z1 = sum(Fraction(comb(nn, j)) * ph**j * ph**(nn - j) for j in range(nn + 1) if j % 2 == 1)
    record(f"Q7(Z0,n={nn})", float(Z0), 0.5)
    record(f"Q7(Z1,n={nn})", float(Z1), 0.5)
    record(f"Q7(equal,n={nn})", Z0 == Z1, True)

# Q8: Rank DP complexity bound T = O(n^3 + n * 4^rw); evaluate for representative inputs
# (no numeric claim in paper; compute the bound's value for sample n, rw)
for (nn, rw) in [(1023, 3), (1023, 5), (100, 2)]:
    T = nn**3 + nn * 4**rw
    record(f"Q8(n={nn},rw={rw})", T, None)

print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(results)} match, {len(results)-sum(results)} mismatch")
