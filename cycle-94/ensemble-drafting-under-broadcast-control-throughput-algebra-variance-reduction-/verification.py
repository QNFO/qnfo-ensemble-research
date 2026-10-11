import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

alpha = 0.7
c_d = 0.1
sigma = 0.3
N = 5

# Q1: E[L] at K=4
K = 4
EL = (1 - alpha**K) / (1 - alpha)
print(f"CLAIM Q1: computed={EL:.6f} expected=2.533 match={isclose(EL, 2.533)}")

# Q2: C at K=4
C = K * c_d + 1
print(f"CLAIM Q2: computed={C:.6f} expected=1.4 match={isclose(C, 1.4)}")

# Q3: T at K=4
T = EL / C
print(f"CLAIM Q3: computed={T:.6f} expected=1.8093 match={isclose(T, 1.8093)}")

# Q4: T at K=3
K = 3
EL3 = (1 - alpha**K) / (1 - alpha)
T3 = EL3 / (K * c_d + 1)
print(f"CLAIM Q4: computed={T3:.6f} expected=1.6846 match={isclose(T3, 1.6846)}")

# Q5: T at K=5
K = 5
EL5 = (1 - alpha**K) / (1 - alpha)
T5 = EL5 / (K * c_d + 1)
print(f"CLAIM Q5: computed={T5:.6f} expected=1.8487 match={isclose(T5, 1.8487)}")

# Q6: T at K=6
K = 6
EL6 = (1 - alpha**K) / (1 - alpha)
T6 = EL6 / (K * c_d + 1)
print(f"CLAIM Q6: computed={T6:.6f} expected=1.8382 match={isclose(T6, 1.8382)}")

# Q7: SE
SE = sigma / math.sqrt(N)
print(f"CLAIM Q7: computed={SE:.6f} expected=0.1342 match={isclose(SE, 0.1342)}")

# Q8: reduction factor
factor = 1 / math.sqrt(N)
print(f"CLAIM Q8: computed={factor:.6f} expected=0.4472 match={isclose(factor, 0.4472)}")

claims = [Q1 := None] # placeholder no-op
results = [
    isclose(EL, 2.533),
    isclose(C, 1.4),
    isclose(T, 1.8093),
    isclose(T3, 1.6846),
    isclose(T5, 1.8487),
    isclose(T6, 1.8382),
    isclose(SE, 0.1342),
    isclose(factor, 0.4472),
]
m = sum(results)
print(f"VERIFICATION SUMMARY: 8 claims, {m} match, {8 - m} mismatch")
