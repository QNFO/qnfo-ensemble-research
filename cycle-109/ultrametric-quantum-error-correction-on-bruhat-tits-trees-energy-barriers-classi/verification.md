# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Single-level eight-fold majority vote failure probability at p=0.4 is 0.1736704",
    "inputs": "n=8, p=0.4, 1-p=0.6",
    "formula": "f(p) = sum_{k=5}^{8} C(8,k) p^k (1-p)^(8-k)"
  },
  {
    "id": "Q2",
    "statement": "Two concatenated levels of majority vote give p^(2) ≈ 0.0055485",
    "inputs": "p^(1)=0.1736704, n=8",
    "formula": "p^(2) = sum_{k=5}^{8} C(8,k) (p^(1))^k (1-p^(1))^(8-k)"
  },
  {
    "id": "Q3",
    "statement": "Three concatenated levels give p^(3) ≈ 2.905e-10",
    "inputs": "p^(2)=0.0055485, n=8",
    "formula": "p^(3) = sum_{k=5}^{8} C(8,k) (p^(2))^k (1-p^(2))^(8-k)"
  },
  {
    "id": "Q4",
    "statement": "95% one-sided confidence bound p_L <= 2.9957e-4 for N=10^4 trials",
    "inputs": "N=10^4, zero errors, confidence 0.95 (i.e. (1-p_L)^N >= 0.05)",
    "formula": "p_L <= 1 - 0.05^(1/N) ≈ ln(20)/N"
  },
  {
    "id": "Q5",
    "statement": "95% one-sided confidence bound p_L <= 2.9957e-5 for N=10^5 trials",
    "inputs": "N=10^5, zero errors, confidence 0.95",
    "formula": "p_L <= 1 - 0.05^(1/N) ≈ ln(20)/N"
  },
  {
    "id": "Q6",
    "statement": "Thermal-activation bound p_L(3) <= e^-8 = 3.3553e-4",
    "inputs": "d=3, E_barrier(d)=2^d, k_B T=1",
    "formula": "p_L(d) <= e^(-2^d)"
  },
  {
    "id": "Q7",
    "statement": "Thermal-activation bound p_L(5) <= e^-32 = 1.2664e-14",
    "inputs": "d=5, E_barrier(d)=2^d, k_B T=1",
    "formula": "p_L(d) <= e^(-2^d)"
  },
  {
    "id": "Q8",
    "statement": "Thermal-activation bound p_L(10) <= 10^-444.7",
    "inputs": "d=10, E_barrier(d)=2^d, k_B T=1, ln(10)=2.302585 (1/ln10=0.434294)",
    "formula": "p_L(10) = e^(-1024) = 10^(-1024/ln(10)) = 10^(-1024*0.434294)"
  }
]

## Script
```python
import math

def maj_fail(p, n=8, kmin=5):
    total = 0.0
    for k in range(kmin, n + 1):
        total += math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    return total

results = []

# Q1: single-level majority vote at p=0.4
q1 = maj_fail(0.4)
expected_q1 = 0.1736704
results.append(("Q1", q1, expected_q1))

# Q2: two concatenated levels
p1 = maj_fail(0.4)
q2 = maj_fail(p1)
expected_q2 = 0.0055485
results.append(("Q2", q2, expected_q2))

# Q3: three concatenated levels
p2 = maj_fail(p1)
q3 = maj_fail(p2)
expected_q3 = 2.905e-10
results.append(("Q3", q3, expected_q3))

# Q4: 95% one-sided confidence bound for N=10^4
N4 = 10 ** 4
q4 = 1 - 0.05 ** (1.0 / N4)
expected_q4 = 2.9957e-4
results.append(("Q4", q4, expected_q4))

# Q5: 95% one-sided confidence bound for N=10^5
N5 = 10 ** 5
q5 = 1 - 0.05 ** (1.0 / N5)
expected_q5 = 2.9957e-5
results.append(("Q5", q5, expected_q5))

# Q6: thermal activation bound at d=3
q6 = math.exp(-2 ** 3)
expected_q6 = 3.3553e-4
results.append(("Q6", q6, expected_q6))

# Q7: thermal activation bound at d=5
q7 = math.exp(-2 ** 5)
expected_q7 = 1.2664e-14
results.append(("Q7", q7, expected_q7))

# Q8: thermal activation bound at d=10, expressed as power of ten
q8 = 1024 / math.log(10)
expected_q8 = 444.7
results.append(("Q8", q8, expected_q8))

mismatch = 0
for cid, computed, expected in results:
    if isinstance(expected, float) and abs(expected) < 1:
        match = math.isclose(computed, expected, rel_tol=1e-2)
    else:
        match = math.isclose(computed, expected, rel_tol=1e-2)
    if not match:
        mismatch += 1
    print(f"CLAIM {cid}: computed={computed:.10g} expected={expected} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results) - mismatch} match, {mismatch} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.1736704 expected=0.1736704 match=yes
CLAIM Q2: computed=0.005548945525 expected=0.0055485 match=yes
CLAIM Q3: computed=2.90537686e-10 expected=2.905e-10 match=yes
CLAIM Q4: computed=0.0002995283598 expected=0.00029957 match=yes
CLAIM Q5: computed=2.995687402e-05 expected=2.9957e-05 match=yes
CLAIM Q6: computed=0.0003354626279 expected=0.00033553 match=yes
CLAIM Q7: computed=1.266416555e-14 expected=1.2664e-14 match=yes
CLAIM Q8: computed=444.7175495 expected=444.7 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
