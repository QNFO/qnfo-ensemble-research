# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Mixture hazard at baseline pi=0.2 is 0.028",
    "inputs": "h_BPP=0.10, h_HARD=0.01, pi=0.2",
    "formula": "h_bar = pi*h_BPP + (1-pi)*h_HARD"
  },
  {
    "id": "Q2",
    "statement": "Expected discounted loss of remaining exposed for L=10 is approximately 3.589744",
    "inputs": "L=10, h_bar=0.028, r=0.05",
    "formula": "E_exposed = L*h_bar/(h_bar+r)"
  },
  {
    "id": "Q3",
    "statement": "Loss threshold L*(pi=0.2) is approximately 2.785714",
    "inputs": "r=0.05, h_bar=0.028",
    "formula": "L* = 1 + r/h_bar"
  },
  {
    "id": "Q4",
    "statement": "At pi=0 the loss threshold is 6",
    "inputs": "r=0.05, h_HARD=0.01",
    "formula": "L* = 1 + r/h_HARD"
  },
  {
    "id": "Q5",
    "statement": "At pi=1 the loss threshold is 1.5",
    "inputs": "r=0.05, h_BPP=0.10",
    "formula": "L* = 1 + r/h_BPP"
  },
  {
    "id": "Q6",
    "statement": "Critical prior for a two-unit asset is pi* = 0.444444...",
    "inputs": "r=0.05, L=2, h_HARD=0.01, h_BPP=0.10",
    "formula": "pi* = (r/(L-1) - h_HARD)/(h_BPP - h_HARD)"
  },
  {
    "id": "Q7",
    "statement": "Scenario D discount factor d = e^{-0.5} is approximately 0.606531",
    "inputs": "r=0.05, T=10",
    "formula": "d = exp(-r*T)"
  },
  {
    "id": "Q8",
    "statement": "Scenario D expected discounted breach cost when waiting is approximately $6,065,310",
    "inputs": "p=0.05, C_b=200000000, d=0.606531",
    "formula": "p*C_b*d"
  }
]

## Script
```python
import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: mixture hazard
h_BPP, h_HARD, pi = 0.10, 0.01, 0.2
h_bar = pi * h_BPP + (1 - pi) * h_HARD
results.append(("Q1", h_bar, 0.028))

# Q2: expected discounted loss for L=10
L, r = 10, 0.05
E_exposed = L * h_bar / (h_bar + r)
results.append(("Q2", E_exposed, 3.589744))

# Q3: loss threshold at pi=0.2
L_star = 1 + r / h_bar
results.append(("Q3", L_star, 2.785714))

# Q4: loss threshold at pi=0
h_bar0 = 0 * h_BPP + 1 * h_HARD
L_star0 = 1 + r / h_bar0
results.append(("Q4", L_star0, 6))

# Q5: loss threshold at pi=1
h_bar1 = 1 * h_BPP + 0 * h_HARD
L_star1 = 1 + r / h_bar1
results.append(("Q5", L_star1, 1.5))

# Q6: critical prior for L=2
L_asset = 2
pi_star = (r / (L_asset - 1) - h_HARD) / (h_BPP - h_HARD)
results.append(("Q6", pi_star, 0.444444))

# Q7: Scenario D discount factor
T = 10
d = math.exp(-r * T)
results.append(("Q7", d, 0.606531))

# Q8: Scenario D expected discounted breach cost
p, C_b = 0.05, 200000000
E_wait_breach = p * C_b * d
results.append(("Q8", E_wait_breach, 6065310))

match_count = 0
for qid, computed, expected in results:
    match = close(computed, expected)
    if match:
        match_count += 1
    print(f"CLAIM {qid}: computed={computed:.6f} expected={expected} match={'yes' if match else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.028000 expected=0.028 match=yes
CLAIM Q2: computed=3.589744 expected=3.589744 match=yes
CLAIM Q3: computed=2.785714 expected=2.785714 match=yes
CLAIM Q4: computed=6.000000 expected=6 match=yes
CLAIM Q5: computed=1.500000 expected=1.5 match=yes
CLAIM Q6: computed=0.444444 expected=0.444444 match=yes
CLAIM Q7: computed=0.606531 expected=0.606531 match=yes
CLAIM Q8: computed=6065306.597126 expected=6065310 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
