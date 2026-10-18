# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "The energy barrier at depth seven is B(7)=128 leaf flips.",
    "inputs": "d = 7",
    "formula": "B(d) = 2^d"
  },
  {
    "id": "Q2",
    "statement": "For p=3 and t=1 the code contains n_1 = 5 physical qudits.",
    "inputs": "p = 3, t = 1",
    "formula": "n_t = 1 + ((p+1)*(p^t - 1))/(p-1)"
  },
  {
    "id": "Q3",
    "statement": "For p=3 and t=2 the code contains n_2 = 17 physical qudits.",
    "inputs": "p = 3, t = 2",
    "formula": "n_t = 1 + ((p+1)*(p^t - 1))/(p-1)"
  },
  {
    "id": "Q4",
    "statement": "The corresponding code distances are d_1 = 3 and d_2 = 5.",
    "inputs": "t = 1 gives d = 2*t + 1; t = 2 gives d = 2*t + 1",
    "formula": "d = 2*t + 1"
  },
  {
    "id": "Q5",
    "statement": "The logical failure probability for n=5, ε=10^{-3} and t=1 is P_pass ≈ 9.98×10^{-6}.",
    "inputs": "n = 5, ε = 1e-3, t = 1",
    "formula": "P_pass = sum_{w=t+1}^{n} C(n,w) * ε^w * (1-ε)^{n-w}"
  },
  {
    "id": "Q6",
    "statement": "The suppression factor ε / P_pass is approximately 100.2.",
    "inputs": "ε = 1e-3, P_pass = 9.98e-6",
    "formula": "ε / P_pass"
  },
  {
    "id": "Q7",
    "statement": "After one level of eight‑fold majority voting with physical error rate p=0.4, the error probability is p^{(1)} = 0.1736704.",
    "inputs": "p = 0.4",
    "formula": "p^{(1)} = sum_{k=5}^{8} C(8,k) * p^k * (1-p)^{8-k}"
  },
  {
    "id": "Q8",
    "statement": "After two concatenated levels the error probability is p^{(2)} ≈ 0.005548945525.",
    "inputs": "p^{(1)} = 0.1736704",
    "formula": "p^{(2)} = sum_{k=5}^{8} C(8,k) * (p^{(1)})^k * (1-p^{(1)})^{8-k}"
  },
  {
    "id": "Q9",
    "statement": "After three concatenated levels the error probability is p^{(3)} ≈ 2.905×10^{-10}.",
    "inputs": "p^{(2)} ≈ 0.005548945525",
    "formula": "p^{(3)} = sum_{k=5}^{8} C(8,k) * (p^{(2)})^k * (1-p^{(2)})^{8-k}"
  },
  {
    "id": "Q10",
    "statement": "With N = 10^5 independent trials and no observed logical errors, the 95% confidence upper bound on the logical error probability is p_L ≤ 3×10^{-5}.",
    "inputs": "N = 100000",
    "formula": "p_L ≤ 3 / N"
  },
  {
    "id": "Q11",
    "statement": "Assuming a qubit cost of $5,000 and a depth‑5 ternary tree with 243 qubits, the hardware cost estimate is approximately $1.2 million.",
    "inputs": "cost_per_qubit = 5000, number_of_qubits = 243",
    "formula": "total_cost = cost_per_qubit * number_of_qubits"
  },
  {
    "id": "Q12",
    "statement": "The projected logical error per million logical operations after three concatenated majority‑vote layers is about 2.9×10^{-4}.",
    "inputs": "logical_error_probability = 2.905e-10",
    "formula": "errors_per_million = logical_error_probability * 1_000_000"
  }
]

## Script
```python
import math
from math import comb

def approx_equal(a, b, sig=6):
    """Return True if a and b match to the given number of significant digits."""
    if b == 0:
        return abs(a) < 10**(-sig)
    return round(a / b, sig) == 1

# Q1
B7 = 2**7
print(f"CLAIM Q1: computed={B7:.0f} expected=128 match={'yes' if B7==128 else 'no'}")

# Q2
p=3; t=1
n1 = 1 + ((p+1)*(p**t - 1))//(p-1)  # integer division works because result is integer
print(f"CLAIM Q2: computed={n1} expected=5 match={'yes' if n1==5 else 'no'}")

# Q3
t=2
n2 = 1 + ((p+1)*(p**t - 1))//(p-1)
print(f"CLAIM Q3: computed={n2} expected=17 match={'yes' if n2==17 else 'no'}")

# Q4
d1 = 2*1 + 1
d2 = 2*2 + 1
expected_d1d2 = (3,5)
match_q4 = (d1==3 and d2==5)
print(f"CLAIM Q4: computed={d1},{d2} expected=3 and 5 match={'yes' if match_q4 else 'no'}")

# Q5
n=5; eps=1e-3; t=1
P_pass = sum(comb(n,w)*(eps**w)*((1-eps)**(n-w)) for w in range(t+1, n+1))
print(f"CLAIM Q5: computed={P_pass:.8e} expected=9.98e-6 match={'yes' if approx_equal(P_pass,9.98e-6,6) else 'no'}")

# Q6
suppression = eps / P_pass
print(f"CLAIM Q6: computed={suppression:.4f} expected=100.2 match={'yes' if approx_equal(suppression,100.2,4) else 'no'}")

# Q7
p0=0.4
p1 = sum(comb(8,k)*(p0**k)*((1-p0)**(8-k)) for k in range(5,9))
print(f"CLAIM Q7: computed={p1:.7f} expected=0.1736704 match={'yes' if approx_equal(p1,0.1736704,7) else 'no'}")

# Q8
p2 = sum(comb(8,k)*(p1**k)*((1-p1)**(8-k)) for k in range(5,9))
print(f"CLAIM Q8: computed={p2:.12f} expected=0.005548945525 match={'yes' if approx_equal(p2,0.005548945525,12) else 'no'}")

# Q9
p3 = sum(comb(8,k)*(p2**k)*((1-p2)**(8-k)) for k in range(5,9))
print(f"CLAIM Q9: computed={p3:.3e} expected=2.905e-10 match={'yes' if approx_equal(p3,2.905e-10,3) else 'no'}")

# Q10
N=100000
pL = 3/N
print(f"CLAIM Q10: computed={pL:.5e} expected=3e-5 match={'yes' if abs(pL-3e-5)<1e-12 else 'no'}")

# Q11
cost_per_qubit=5000
num_qubits=243
total_cost = cost_per_qubit * num_qubits
print(f"CLAIM Q11: computed=${total_cost:,} expected=$1.2 million match={'yes' if abs(total_cost-1_200_000)/1_200_000<0.05 else 'no'}")

# Q12
logical_error=2.905e-10
errors_per_million = logical_error * 1_000_000
print(f"CLAIM Q12: computed={errors_per_million:.3e} expected=2.9e-4 match={'yes' if approx_equal(errors_per_million,2.9e-4,3) else 'no'}")

print("VERIFICATION SUMMARY: 12 claims, "
      f"{sum(1 for line in open(__file__) if 'match=yes' in line)} match, "
      f"{12 - sum(1 for line in open(__file__) if 'match=yes' in line)} mismatch")

```

## Execution output
```
CLAIM Q1: computed=128 expected=128 match=yes
CLAIM Q2: computed=5 expected=5 match=yes
CLAIM Q3: computed=17 expected=17 match=yes
CLAIM Q4: computed=3,5 expected=3 and 5 match=yes
CLAIM Q5: computed=9.98001500e-06 expected=9.98e-6 match=no
CLAIM Q6: computed=100.2003 expected=100.2 match=yes
CLAIM Q7: computed=0.1736704 expected=0.1736704 match=yes
CLAIM Q8: computed=0.005548945525 expected=0.005548945525 match=no
CLAIM Q9: computed=2.905e-10 expected=2.905e-10 match=yes
CLAIM Q10: computed=3.00000e-05 expected=3e-5 match=yes
CLAIM Q11: computed=$1,215,000 expected=$1.2 million match=yes
CLAIM Q12: computed=2.905e-04 expected=2.9e-4 match=no

[stderr]
Traceback (most recent call last):
  File "<string>", line 70, in <module>
NameError: name '__file__' is not defined. Did you mean: '__name__'?

[exit 1]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 128 | 128 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 5 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 17 | 17 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 3,5 | 3 | - | undecided | undecided: values not both numeric and no script verdict |
| Q5 | 9.98001500e-06 | 9.98e-6 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 100.2003 | 100.2 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q7 | 0.1736704 | 0.1736704 | yes | match | 7 significant digits (as the paper states, at least 2) |
| Q8 | 0.005548945525 | 0.005548945525 | no | match | 10 significant digits (as the paper states, at least 2) |
| Q9 | 2.905e-10 | 2.905e-10 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 3.00000e-05 | 3e-5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | $1,215,000 | $1.2 | - | undecided | undecided: values not both numeric and no script verdict |
| Q12 | 2.905e-04 | 2.9e-4 | no | match | 2 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 12 (2 undecided).
