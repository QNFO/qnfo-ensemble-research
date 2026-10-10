# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "S_Base = ln(6) = 1.791759 nats for d=12",
    "inputs": "d=12",
    "formula": "ln(d/2)"
  },
  {
    "id": "Q2",
    "statement": "S_Base = 2.584963 bits",
    "inputs": "S_Base=1.791759 nats, ln2=0.693147",
    "formula": "S_Base/ln(2)"
  },
  {
    "id": "Q3",
    "statement": "ln 12 = 2.484906 nats",
    "inputs": "d=12",
    "formula": "ln(12)"
  },
  {
    "id": "Q4",
    "statement": "f_disc = 0.721125 (72.1% discarded)",
    "inputs": "S_Base=1.791759, ln12=2.484906",
    "formula": "S_Base/ln(12)"
  },
  {
    "id": "Q5",
    "statement": "retained fraction 0.278875 (27.9%)",
    "inputs": "f_disc=0.721125",
    "formula": "1 - f_disc"
  },
  {
    "id": "Q6",
    "statement": "log2(12) = 3.584963",
    "inputs": "d=12",
    "formula": "ln(12)/ln(2)"
  },
  {
    "id": "Q7",
    "statement": "radix efficiency eta = 0.278942",
    "inputs": "log2(12)=3.584963",
    "formula": "1/log2(12)"
  },
  {
    "id": "Q8",
    "statement": "ceil(log2 12) = 4 qubits",
    "inputs": "d=12",
    "formula": "ceil(log2(12))"
  }
]

## Script
```python
import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: S_Base = ln(6) = 1.791759 nats
computed = math.log(12 / 2)
results.append(("Q1", computed, 1.791759))

# Q2: S_Base in bits = 1.791759 / ln(2)
computed = 1.791759 / math.log(2)
results.append(("Q2", computed, 2.584963))

# Q3: ln(12) = 2.484906 nats
computed = math.log(12)
results.append(("Q3", computed, 2.484906))

# Q4: f_disc = S_Base / ln(12)
computed = 1.791759 / math.log(12)
results.append(("Q4", computed, 0.721125))

# Q5: retained fraction = 1 - f_disc
computed = 1 - (1.791759 / math.log(12))
results.append(("Q5", computed, 0.278875))

# Q6: log2(12) = ln(12)/ln(2)
computed = math.log(12) / math.log(2)
results.append(("Q6", computed, 3.584963))

# Q7: eta = 1 / log2(12)
computed = 1 / (math.log(12) / math.log(2))
results.append(("Q7", computed, 0.278942))

# Q8: ceil(log2(12)) = 4
computed = math.ceil(math.log(12) / math.log(2))
results.append(("Q8", computed, 4))

for cid, comp, exp in results:
    match = isclose(comp, exp) if exp is not None else "n/a"
    print(f"CLAIM {cid}: computed={comp:.6f} expected={exp} match={match}")

n = len(results)
m = sum(1 for _, c, e in results if e is not None and isclose(c, e))
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.791759 expected=1.791759 match=True
CLAIM Q2: computed=2.584962 expected=2.584963 match=True
CLAIM Q3: computed=2.484907 expected=2.484906 match=True
CLAIM Q4: computed=0.721057 expected=0.721125 match=False
CLAIM Q5: computed=0.278943 expected=0.278875 match=False
CLAIM Q6: computed=3.584963 expected=3.584963 match=True
CLAIM Q7: computed=0.278943 expected=0.278942 match=False
CLAIM Q8: computed=4.000000 expected=4 match=True
VERIFICATION SUMMARY: 8 claims, 5 match, 3 mismatch

[exit 0]
```
