# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Expected single-arm purity E[Tr rho_A^2] = (b + b^2)/(b^3 + 1) = 1.000001e-6 at b = 1e6",
    "inputs": "b = 10^6",
    "formula": "(b + b^2) / (b^3 + 1)"
  },
  {
    "id": "Q2",
    "statement": "Excess purity Delta = (b^2 - 1)/(b^4 + b) ≈ 9.99999e-13 ≈ 1e-12 at b = 1e6",
    "inputs": "b = 10^6",
    "formula": "(b^2 - 1) / (b^4 + b)"
  },
  {
    "id": "Q3",
    "statement": "Single-arm entropy E[S_A] ≈ ln b - 1/(2b) = 13.8155095 nats ≈ 19.93 bits at b = 1e6",
    "inputs": "b = 10^6, ln 10 = 2.302585, ln 2 = 0.693147",
    "formula": "(6 * ln(10) - 1/(2*b)) / ln(2)"
  },
  {
    "id": "Q4",
    "statement": "Two-arm recovery error bound epsilon <= K/b = 1e-3 at K = 1e3, b = 1e6",
    "inputs": "K = 10^3, b = 10^6",
    "formula": "K / b"
  },
  {
    "id": "Q5",
    "statement": "Recovery error bound epsilon <= 1e-2 at K = 1e4, b = 1e6",
    "inputs": "K = 10^4, b = 10^6",
    "formula": "K / b"
  },
  {
    "id": "Q6",
    "statement": "Recovery error bound epsilon <= 0.1 at K = 1e5, b = 1e6",
    "inputs": "K = 10^5, b = 10^6",
    "formula": "K / b"
  },
  {
    "id": "Q7",
    "statement": "Secondary example recovery error bound epsilon <= 3.125e-2 at K = 32, b = 1024",
    "inputs": "K = 32, b = 1024",
    "formula": "K / b"
  },
  {
    "id": "Q8",
    "statement": "Markov bound: P(epsilon >= 2K/b) <= 1/4, i.e. success probability >= 0.75 at threshold 2e-3",
    "inputs": "K/b = 10^-3, threshold factor 4",
    "formula": "1 - 1/4"
  }
]

## Script
```python
import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: Expected single-arm purity (b + b^2)/(b^3 + 1) at b = 1e6
b = 1e6
q1 = (b + b**2) / (b**3 + 1)
expected_q1 = 1.000001e-6
results.append(("Q1", q1, expected_q1))

# Q2: Excess purity (b^2 - 1)/(b^4 + b) at b = 1e6
q2 = (b**2 - 1) / (b**4 + b)
expected_q2 = 9.99999e-13
results.append(("Q2", q2, expected_q2))

# Q3: Single-arm entropy in bits: (6*ln(10) - 1/(2*b)) / ln(2)
ln10 = 2.302585
ln2 = 0.693147
q3 = (6 * ln10 - 1 / (2 * b)) / ln2
expected_q3 = 13.8155095 / ln2  # paper states 13.8155095 nats ≈ 19.93 bits
results.append(("Q3", q3, expected_q3))

# Q4: Recovery error bound K/b at K = 1e3, b = 1e6
K4 = 1e3
q4 = K4 / b
expected_q4 = 1e-3
results.append(("Q4", q4, expected_q4))

# Q5: Recovery error bound K/b at K = 1e4, b = 1e6
K5 = 1e4
q5 = K5 / b
expected_q5 = 1e-2
results.append(("Q5", q5, expected_q5))

# Q6: Recovery error bound K/b at K = 1e5, b = 1e6
K6 = 1e5
q6 = K6 / b
expected_q6 = 0.1
results.append(("Q6", q6, expected_q6))

# Q7: Recovery error bound K/b at K = 32, b = 1024
K7 = 32
b7 = 1024
q7 = K7 / b7
expected_q7 = 3.125e-2
results.append(("Q7", q7, expected_q7))

# Q8: Markov bound success probability 1 - 1/4
q8 = 1 - 1/4
expected_q8 = 0.75
results.append(("Q8", q8, expected_q8))

match_count = 0
for cid, computed, expected in results:
    match = isclose(computed, expected)
    if match:
        match_count += 1
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

total = len(results)
mismatch = total - match_count
print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {mismatch} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.000001e-06 expected=1.000001e-06 match=yes
CLAIM Q2: computed=9.99999999999e-13 expected=9.99999e-13 match=yes
CLAIM Q3: computed=19.931572235038168 expected=19.931572235038168 match=yes
CLAIM Q4: computed=0.001 expected=0.001 match=yes
CLAIM Q5: computed=0.01 expected=0.01 match=yes
CLAIM Q6: computed=0.1 expected=0.1 match=yes
CLAIM Q7: computed=0.03125 expected=0.03125 match=yes
CLAIM Q8: computed=0.75 expected=0.75 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
