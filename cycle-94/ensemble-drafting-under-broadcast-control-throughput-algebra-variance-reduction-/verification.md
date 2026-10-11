# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Expected accepted length E[L] = (1 - alpha^K)/(1 - alpha) = 2.533 at alpha = 0.7, K = 4",
    "inputs": "alpha = 0.7, K = 4",
    "formula": "E[L] = (1 - alpha^K)/(1 - alpha)"
  },
  {
    "id": "Q2",
    "statement": "Per-cycle cost C = K*c_d + 1 = 1.4 at K = 4, c_d = 0.1",
    "inputs": "K = 4, c_d = 0.1",
    "formula": "C = K*c_d + 1"
  },
  {
    "id": "Q3",
    "statement": "Throughput T = E[L]/C = 2.533/1.4 ≈ 1.8093",
    "inputs": "E[L] = 2.533, C = 1.4",
    "formula": "T = E[L]/C"
  },
  {
    "id": "Q4",
    "statement": "Throughput at K = 3: T ≈ 1.6846",
    "inputs": "alpha = 0.7, K = 3, c_d = 0.1",
    "formula": "T = ((1 - alpha^K)/(1 - alpha))/(K*c_d + 1)"
  },
  {
    "id": "Q5",
    "statement": "Throughput at K = 5: T ≈ 1.8487 (grid optimum K* = 5)",
    "inputs": "alpha = 0.7, K = 5, c_d = 0.1",
    "formula": "T = ((1 - alpha^K)/(1 - alpha))/(K*c_d + 1)"
  },
  {
    "id": "Q6",
    "statement": "Throughput at K = 6: T ≈ 1.8382",
    "inputs": "alpha = 0.7, K = 6, c_d = 0.1",
    "formula": "T = ((1 - alpha^K)/(1 - alpha))/(K*c_d + 1)"
  },
  {
    "id": "Q7",
    "statement": "Standard error of equal-weight aggregate SE = sigma/sqrt(N) ≈ 0.1342 at sigma = 0.3, N = 5",
    "inputs": "sigma = 0.3, N = 5",
    "formula": "SE = sigma/sqrt(N)"
  },
  {
    "id": "Q8",
    "statement": "Reduction factor relative to a single drafter = 1/sqrt(N) ≈ 0.4472 at N = 5",
    "inputs": "N = 5",
    "formula": "factor = 1/sqrt(N)"
  }
]

## Script
```python
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

```

## Execution output
```
CLAIM Q1: computed=2.533000 expected=2.533 match=True
CLAIM Q2: computed=1.400000 expected=1.4 match=True
CLAIM Q3: computed=1.809286 expected=1.8093 match=False
CLAIM Q4: computed=1.684615 expected=1.6846 match=False
CLAIM Q5: computed=1.848733 expected=1.8487 match=False
CLAIM Q6: computed=1.838231 expected=1.8382 match=False
CLAIM Q7: computed=0.134164 expected=0.1342 match=False
CLAIM Q8: computed=0.447214 expected=0.4472 match=False
VERIFICATION SUMMARY: 8 claims, 2 match, 6 mismatch

[exit 0]
```
