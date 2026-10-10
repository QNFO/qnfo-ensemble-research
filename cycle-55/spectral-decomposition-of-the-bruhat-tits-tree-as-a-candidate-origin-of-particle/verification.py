import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: B_2(n) = 3*2^n - 2, check n=1,2
b2 = lambda n: 1 + (2+1)*(2**n - 1)//(2-1)
computed = [b2(1), b2(2)]
expected = [3*2**1 - 2, 3*2**2 - 2]
match = all(close(c, e) for c, e in zip(computed, expected))
results.append(("Q1", computed, expected, match))

# Q2: B_3(n) = 2*3^n - 1, check n=1,2
b3 = lambda n: 1 + (3+1)*(3**n - 1)/(3-1)
computed = [b3(1), b3(2)]
expected = [2*3**1 - 1, 2*3**2 - 1]
match = all(close(c, e) for c, e in zip(computed, expected))
results.append(("Q2", computed, expected, match))

# Q3: rho_p = 2*sqrt(p)
rho = lambda p: 2*math.sqrt(p)
computed = [rho(2), rho(3), rho(5)]
expected = [2.82842712, 3.46410162, 4.47213595]
match = all(close(c, e) for c, e in zip(computed, expected))
results.append(("Q3", computed, expected, match))

# Q4: cross-prime ratios
computed = [rho(3)/rho(2), rho(5)/rho(3), rho(5)/rho(2)]
expected = [1.22474487, 1.29099445, 1.58113883]
match = all(close(c, e) for c, e in zip(computed, expected))
results.append(("Q4", computed, expected, match))

# Q5: Laplacian continuous spectrum p=2
lo = 3 - 2*math.sqrt(2); hi = 3 + 2*math.sqrt(2)
match = close(lo, 0.17157288) and close(hi, 5.82842712)
results.append(("Q5", [lo, hi], [0.17157288, 5.82842712], match))

# Q6: Laplacian continuous spectrum p=5
lo = 6 - 2*math.sqrt(5); hi = 6 + 2*math.sqrt(5)
match = close(lo, 1.52786405) and close(hi, 10.47213595)
results.append(("Q6", [lo, hi], [1.52786405, 10.47213595], match))

# Q7: finite radial quotient eigenvalues p=5
lam = lambda p, k: 2*math.sqrt(p)*math.cos(2*math.pi*k/(p+1))
computed = [lam(5, k) for k in range(4)]
expected = [4.47213595, 2.23606798, -2.23606798, -4.47213595]
match = all(close(c, e) for c, e in zip(computed, expected))
results.append(("Q7", computed, expected, match))

# Q8: finite radial quotient eigenvalues p=2
computed = [lam(2, k) for k in range(3)]
expected = [2.82842712, -1.41421356, -1.41421356]
match = all(close(c, e) for c, e in zip(computed, expected))
results.append(("Q8", computed, expected, match))

n_match = 0
for qid, comp, exp, match in results:
    print(f"CLAIM {qid}: computed={comp} expected={exp} match={'yes' if match else 'no'}")
    if match:
        n_match += 1
print(f"VERIFICATION SUMMARY: {len(results)} claims, {n_match} match, {len(results)-n_match} mismatch")
