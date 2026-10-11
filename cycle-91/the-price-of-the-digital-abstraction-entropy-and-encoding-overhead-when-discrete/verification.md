# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Register entropy of digitization at d=12 is 3.584963 bits",
    "inputs": "d=12",
    "formula": "log2(d)"
  },
  {
    "id": "Q2",
    "statement": "Base truncation entropy S_Base(12) = 1.791759 nats = 2.584963 bits",
    "inputs": "d=12",
    "formula": "ln(d/2)"
  },
  {
    "id": "Q3",
    "statement": "Binary encoding of a d=12 qudit requires m=4 qubits with dimension overhead 16/12 = 1.333333",
    "inputs": "d=12",
    "formula": "m = ceil(log2(d)); overhead = 2^m / d"
  },
  {
    "id": "Q4",
    "statement": "Encoding efficiency eta = 0.896241 and idle fraction 0.1037594",
    "inputs": "d=12, m=4",
    "formula": "eta = log2(d)/m; idle = 1 - eta"
  },
  {
    "id": "Q5",
    "statement": "Physical environment entropy of amplitude damping at gamma=1e-3 is 1.140776e-2 bits",
    "inputs": "gamma=0.001",
    "formula": "h2(gamma) = -gamma*log2(gamma) - (1-gamma)*log2(1-gamma)"
  },
  {
    "id": "Q6",
    "statement": "Twirled Pauli probabilities p_X = p_Y = 2.5e-4, p_Z = 5e-4, p_I = 0.999",
    "inputs": "gamma=0.001",
    "formula": "p_X = p_Y = gamma/4; p_Z = gamma/2; p_I = 1 - gamma"
  },
  {
    "id": "Q7",
    "statement": "Twirled environment entropy is 1.290776e-2 bits",
    "inputs": "p_I=0.999, p_X=2.5e-4, p_Y=2.5e-4, p_Z=5e-4",
    "formula": "-sum_i p_i*log2(p_i)"
  },
  {
    "id": "Q8",
    "statement": "Entropy distortion Delta H = 1.500e-3 bits per use, ratio 1.131489",
    "inputs": "H_twirl=1.290776e-2, H_phys=1.140776e-2",
    "formula": "Delta = H_twirl - H_phys; ratio = H_twirl / H_phys"
  }
]

## Script
```python
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

```

## Execution output
```
CLAIM Q1: computed=3.5849625 expected=3.584963 match=yes
CLAIM Q2: computed=1.79175947 expected=1.791759 match=yes
CLAIM Q2b: computed=2.5849625 expected=2.584963 match=yes
CLAIM Q3: computed=1.33333333 expected=1.33333333 match=yes
CLAIM Q4: computed=0.896240625 expected=0.896241 match=yes
CLAIM Q4b: computed=0.103759375 expected=0.1037594 match=yes
CLAIM Q5: computed=0.0114077577 expected=0.01140776 match=yes
CLAIM Q6: computed=0.00025 expected=0.00025 match=yes
CLAIM Q7: computed=0.0129077577 expected=0.01290776 match=yes
CLAIM Q8: computed=0.0015 expected=0.0015 match=yes
CLAIM Q8b: computed=1.13148947 expected=1.131489 match=yes
VERIFICATION SUMMARY: 11 claims, 11 match, 0 mismatch

[exit 0]
```
