import math

def boltz(n):
    return math.exp(-0.25 * n * n)

# Q1: partition function Z = 1 + 2*sum_{n=1}^{inf} exp(-0.25 n^2)
inner = sum(boltz(n) for n in range(1, 200))
Z = 1 + 2 * inner
Z_expected = 3.544908
match1 = math.isclose(Z, Z_expected, rel_tol=1e-6)
print(f"CLAIM Q1: computed={Z:.6f} expected={Z_expected} match={'yes' if match1 else 'no'}")

# Q2: epsilon_tr(3) = 2 * sum_{n=4}^{inf} exp(-0.25 n^2) / Z
tail3 = sum(boltz(n) for n in range(4, 200))
eps3 = 2 * tail3 / Z
eps3_expected = 1.150e-2
match2 = math.isclose(eps3, eps3_expected, rel_tol=1e-3)
print(f"CLAIM Q2: computed={eps3:.6e} expected={eps3_expected} match={'yes' if match2 else 'no'}")

# Q3: epsilon_tr(5) = 2 * sum_{n=6}^{inf} exp(-0.25 n^2) / Z
tail5 = sum(boltz(n) for n in range(6, 200))
eps5 = 2 * tail5 / Z
eps5_expected = 7.242e-5
match3 = math.isclose(eps5, eps5_expected, rel_tol=1e-3)
print(f"CLAIM Q3: computed={eps5:.6e} expected={eps5_expected} match={'yes' if match3 else 'no'}")

# Q4: epsilon_tr(7) = 2 * sum_{n=8}^{inf} exp(-0.25 n^2) / Z
tail7 = sum(boltz(n) for n in range(8, 200))
eps7 = 2 * tail7 / Z
eps7_expected = 6.44e-8
match4 = math.isclose(eps7, eps7_expected, rel_tol=1e-2)
print(f"CLAIM Q4: computed={eps7:.6e} expected={eps7_expected} match={'yes' if match4 else 'no'}")

# Q5: delta_E(n_max) = (2*sum_{n=n_max+1}^{inf} n^2 exp(-0.25 n^2)) / (2*sum_{n=1}^{inf} n^2 exp(-0.25 n^2))
denom = 2 * sum(n * n * boltz(n) for n in range(1, 200))
for n_max in (3, 5, 7):
    numer = 2 * sum(n * n * boltz(n) for n in range(n_max + 1, 200))
    dE = numer / denom
    print(f"CLAIM Q5(n_max={n_max}): computed={dE:.6e} expected=None match=n/a")

total = 5
matched = sum([match1, match2, match3, match4])
print(f"VERIFICATION SUMMARY: {total} claims, {matched} match, {total - matched} mismatch")
