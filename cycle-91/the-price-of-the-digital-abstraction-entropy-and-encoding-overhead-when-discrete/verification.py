import math
from fractions import Fraction

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: log2(12)
computed = math.log2(12)
expected = 3.584963
results.append(("Q1", computed, expected, isclose(computed, expected)))

# Q2: ln(6) nats and in bits
computed_nats = math.log(6)
expected_nats = 1.791759
results.append(("Q2", computed_nats, expected_nats, isclose(computed_nats, expected_nats)))
computed_bits = computed_nats * math.log2(math.e)
expected_bits = 2.584963
results.append(("Q2b", computed_bits, expected_bits, isclose(computed_bits, expected_bits)))

# Q3: m = ceil(log2(12)), overhead = 2^m / d
d = 12
m = math.ceil(math.log2(d))
overhead = (2 ** m) / d
results.append(("Q3", overhead, 4 / 3, isclose(overhead, 4 / 3)))

# Q4: eta = log2(d)/m, idle = 1 - eta
eta = math.log2(d) / m
idle = 1 - eta
results.append(("Q4", eta, 0.896241, isclose(eta, 0.896241)))
results.append(("Q4b", idle, 0.1037594, isclose(idle, 0.1037594)))

# Q5: h2(gamma)
gamma = 1e-3
h2 = -gamma * math.log2(gamma) - (1 - gamma) * math.log2(1 - gamma)
results.append(("Q5", h2, 1.140776e-2, isclose(h2, 1.140776e-2)))

# Q6: twirled probabilities
pX = gamma / 4
pY = gamma / 4
pZ = gamma / 2
pI = 1 - gamma
ok6 = isclose(pX, 2.5e-4) and isclose(pY, 2.5e-4) and isclose(pZ, 5e-4) and isclose(pI, 0.999)
results.append(("Q6", pX, 2.5e-4, ok6))

# Q7: twirled entropy
H_twirl = -(pI * math.log2(pI) + pX * math.log2(pX) + pY * math.log2(pY) + pZ * math.log2(pZ))
results.append(("Q7", H_twirl, 1.290776e-2, isclose(H_twirl, 1.290776e-2)))

# Q8: Delta H and ratio
H_phys = h2
Delta = H_twirl - H_phys
ratio = H_twirl / H_phys
results.append(("Q8", Delta, 1.500e-3, isclose(Delta, 1.500e-3)))
results.append(("Q8b", ratio, 1.131489, isclose(ratio, 1.131489)))

for cid, computed, expected, match in results:
    print(f"CLAIM {cid}: computed={computed:.9g} expected={expected:.9g} match={'yes' if match else 'no'}")

n = len(results)
mcount = sum(1 for r in results if r[3])
print(f"VERIFICATION SUMMARY: {n} claims, {mcount} match, {n - mcount} mismatch")
