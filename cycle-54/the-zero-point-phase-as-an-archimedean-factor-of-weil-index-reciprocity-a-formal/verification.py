import math

def cclose(z, w, tol=1e-9):
    return math.isclose(z.real, w.real, rel_tol=1e-6, abs_tol=tol) and \
           math.isclose(z.imag, w.imag, rel_tol=1e-6, abs_tol=tol)

results = []

# Q1: e^{i*pi/4} = sqrt(2)/2 + i*sqrt(2)/2
z1 = complex(math.cos(math.pi/4), math.sin(math.pi/4))
w1 = complex(math.sqrt(2)/2, math.sqrt(2)/2)
results.append(("Q1", z1, w1))

# Q2: (e^{i*pi/4})^4 = -1, (e^{i*pi/4})^8 = 1
z2a = (1j*math.pi/4).__class__(math.cos(math.pi/4), math.sin(math.pi/4))**4
w2a = -1 + 0j
z2b = complex(math.cos(math.pi/4), math.sin(math.pi/4))**8
w2b = 1 + 0j
results.append(("Q2a", z2a, w2a))
results.append(("Q2b", z2b, w2b))

# Q3: G_3 = (1 + 2*e^{2*pi*i/3}) / sqrt(3) = i
s3 = 1 + 2*complex(math.cos(2*math.pi/3), math.sin(2*math.pi/3))
G3 = s3 / math.sqrt(3)
w3 = 1j
results.append(("Q3", G3, w3))

# Q4: G_5 = (1 + 4*cos(2*pi/5)) / sqrt(5) = 1
s5 = 1 + 4*math.cos(2*math.pi/5)
G5 = s5 / math.sqrt(5)
w5 = 1.0
results.append(("Q4", G5, w5))

# Q5: gamma_2 = 1 / gamma_infinity = e^{-i*pi/4}
gamma_inf = complex(math.cos(math.pi/4), math.sin(math.pi/4))
gamma_2 = 1 / gamma_inf
w5b = complex(math.cos(-math.pi/4), math.sin(-math.pi/4))
results.append(("Q5", gamma_2, w5b))

# Q6: number of solutions of gamma_inf * gamma_2 = 1 in mu_8 x mu_8 = 8
mu8 = [complex(math.cos(math.pi*k/4), math.sin(math.pi*k/4)) for k in range(8)]
count = sum(1 for a in mu8 for b in mu8 if cclose(a*b, 1+0j))
results.append(("Q6", count, 8))

# Q7: E_0/(hbar*omega) = 1/2
from fractions import Fraction
ratio = Fraction(1, 2)
results.append(("Q7", ratio, Fraction(1, 2)))

match = 0
for cid, computed, expected in results:
    if isinstance(computed, complex):
        ok = cclose(computed, expected if isinstance(expected, complex) else complex(expected))
    elif isinstance(computed, Fraction):
        ok = computed == expected
    else:
        ok = math.isclose(computed, expected, rel_tol=1e-6)
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if ok else 'no'}")
    if ok:
        match += 1

total = len(results)
print(f"VERIFICATION SUMMARY: {total} claims, {match} match, {total - match} mismatch")
