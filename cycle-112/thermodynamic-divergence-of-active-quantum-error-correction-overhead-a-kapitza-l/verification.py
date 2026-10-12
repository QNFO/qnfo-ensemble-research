import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

# Q1
P0 = 1e-10; alpha = 1e-11; beta = 4; GK = 1e-7; dT = 1e-2
Nc = (beta * GK * dT - P0) / alpha
print(f"CLAIM Q1: computed={Nc} expected=390 match={'yes' if isclose(Nc, 390) else 'no'}")

# Q2
Ne = 200
Nc_exp = Ne * math.log(beta * GK * dT / P0)
print(f"CLAIM Q2: computed={Nc_exp} expected=737.7758 match={'yes' if isclose(Nc_exp, 737.7758) else 'no'}")

# Q3
dT_half = 5e-3
Nc3 = (beta * GK * dT_half - P0) / alpha
print(f"CLAIM Q3: computed={Nc3} expected=190 match={'yes' if isclose(Nc3, 190) else 'no'}")

# Q4
GK10 = 1e-6
Nc4 = (beta * GK10 * dT - P0) / alpha
print(f"CLAIM Q4: computed={Nc4} expected=3990 match={'yes' if isclose(Nc4, 3990) else 'no'}")

# Q5
Nc5 = math.floor(390 / 5**2)
print(f"CLAIM Q5: computed={Nc5} expected=15 match={'yes' if Nc5 == 15 else 'no'}")

# Q6
Nc6 = math.floor(390 / 7**2)
print(f"CLAIM Q6: computed={Nc6} expected=7 match={'yes' if Nc6 == 7 else 'no'}")

# Q7
N = 390
P_tot = P0 * N + alpha * N**2
P_ext = beta * GK * dT * N
print(f"CLAIM Q7: computed={P_tot} expected=1.560e-6 match={'yes' if isclose(P_tot, 1.560e-6) and isclose(P_ext, P_tot) else 'no'}")

# Q8
stab = beta * GK
print(f"CLAIM Q8: computed={stab} expected=4e-7 match={'yes' if isclose(stab, 4e-7) else 'no'}")

results = [Q1_ok := isclose(Nc, 390), isclose(Nc_exp, 737.7758), isclose(Nc3, 190),
           isclose(Nc4, 3990), Nc5 == 15, Nc6 == 7,
           isclose(P_tot, 1.560e-6) and isclose(P_ext, P_tot), isclose(stab, 4e-7)]
print(f"VERIFICATION SUMMARY: {len(results)} claims, {sum(results)} match, {len(results) - sum(results)} mismatch")
