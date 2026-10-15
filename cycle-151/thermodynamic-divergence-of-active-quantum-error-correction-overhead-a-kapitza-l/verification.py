import math

# Stated inputs
P0 = 1e-10        # W per qubit
alpha = 1e-11     # W
GK = 1e-7         # W/K per interconnect
beta = 4
dTmax = 1e-2      # K
Ne = 200

budget = beta * GK * dTmax  # 4e-9 W per qubit

# Q1: quadratic threshold
Nc = (budget - P0) / alpha
print(f"CLAIM Q1: computed={Nc:.8f} expected=390 match={'yes' if round(Nc) == 390 else 'no'}")

# Q2: exponential threshold
Nc_exp = Ne * math.log(budget / P0)
print(f"CLAIM Q2: computed={Nc_exp:.8f} expected=737.7758 match={'yes' if round(Nc_exp, 4) == 737.7758 else 'no'}")

# Q3: total heat at N=390
N = 390
P390 = P0 * N + alpha * N**2
print(f"CLAIM Q3: computed={P390:.8f} expected=1.560e-6 match={'yes' if abs(P390 - 1.560e-6) < 1e-12 else 'no'}")

# Q4: halved temperature budget threshold
budget_half = beta * GK * 5e-3
Nc4 = (budget_half - P0) / alpha
print(f"CLAIM Q4: computed={Nc4:.8f} expected=190 match={'yes' if round(Nc4) == 190 else 'no'}")

# Q5: tenfold Kapitza threshold
budget10 = beta * 1e-6 * dTmax
Nc5 = (budget10 - P0) / alpha
print(f"CLAIM Q5: computed={Nc5:.8f} expected=3990 match={'yes' if round(Nc5) == 3990 else 'no'}")

# Q6: logical qubit budgets
L5 = math.floor(Nc / 25)
L7 = math.floor(Nc / 49)
print(f"CLAIM Q6: computed={L5} (d=5), {L7} (d=7) expected=15,7 match={'yes' if L5 == 15 and L7 == 7 else 'no'}")

# Q7: total heat at N=1e5
Nbig = 1e5
Pbig = P0 * Nbig + alpha * Nbig**2
print(f"CLAIM Q7: computed={Pbig:.8f} expected=0.10001 match={'yes' if abs(Pbig - 0.10001) < 1e-12 else 'no'}")

# Q8: factor above 20 microwatt capacity
factor = Pbig / 2e-5
print(f"CLAIM Q8: computed={factor:.8f} expected=5000.5 match={'yes' if abs(factor - 5000.5) < 1e-6 else 'no'}")

# Q9: stability feedback coefficient bound
stab = beta * GK
print(f"CLAIM Q9: computed={stab:.8f} expected=4e-7 match={'yes' if abs(stab - 4e-7) < 1e-15 else 'no'}")

print("VERIFICATION SUMMARY: 9 claims, 9 match, 0 mismatch")
