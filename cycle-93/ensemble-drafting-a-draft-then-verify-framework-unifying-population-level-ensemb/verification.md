# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Expected accepted units for a single drafter: E_k[A] = (1-alpha^k)/(1-alpha); at alpha=0.8, k=7 gives 3.951424",
    "inputs": "alpha=0.8, k=7",
    "formula": "(1 - 0.8**7) / (1 - 0.8)"
  },
  {
    "id": "Q2",
    "statement": "Throughput gain S(k) = E_k[A]/(rho*k + nu); at alpha=0.8, rho=0.1, nu=1, k=7 gives S=2.324367",
    "inputs": "alpha=0.8, rho=0.1, nu=1, k=7",
    "formula": "((1 - 0.8**7)/(1 - 0.8)) / (0.1*7 + 1)"
  },
  {
    "id": "Q3",
    "statement": "Discrete optimum for single strong drafter is k*=7 with S_max=2.324367 (S(6)=2.305800, S(8)=2.311744 are lower)",
    "inputs": "alpha=0.8, rho=0.1, nu=1, k in {4,...,9}",
    "formula": "argmax over k of ((1 - 0.8**k)/0.2)/(0.1*k + 1)"
  },
  {
    "id": "Q4",
    "statement": "Single weak drafter (alpha=0.5, rho=0.1, nu=1) optimum k*=3 with S_single=1.346154",
    "inputs": "alpha=0.5, rho=0.1, nu=1",
    "formula": "argmax over k of ((1 - 0.5**k)/0.5)/(0.1*k + 1)"
  },
  {
    "id": "Q5",
    "statement": "Two-drafter pooled acceptance alpha_2 = 1-(1-alpha)^2 = 0.75 for alpha=0.5",
    "inputs": "alpha=0.5, m=2",
    "formula": "1 - (1 - 0.5)**2"
  },
  {
    "id": "Q6",
    "statement": "Two-drafter ensemble (alpha_2=0.75, rho_2=0.2, nu=1) optimum k*=5 with S_ens=1.525391",
    "inputs": "alpha_2=0.75, rho_2=0.2, nu=1",
    "formula": "argmax over k of ((1 - 0.75**k)/0.25)/(0.2*k + 1)"
  },
  {
    "id": "Q7",
    "statement": "Relative gain of two weak drafters over one weak drafter: S_rel = 1.525391/1.346154 = 1.133147 (13.3%)",
    "inputs": "S_ens=1.525391, S_single=1.346154",
    "formula": "1.525391 / 1.346154"
  },
  {
    "id": "Q8",
    "statement": "Three-drafter pooled acceptance alpha_3 = 1-(1-0.6)^3 = 0.936",
    "inputs": "alpha=0.6, m=3",
    "formula": "1 - (1 - 0.6)**3"
  }
]

## Script
```python
import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1
alpha, k = 0.8, 7
val = (1 - alpha**k) / (1 - alpha)
results.append(("Q1", val, 3.951424))

# Q2
rho, nu = 0.1, 1
val = ((1 - alpha**k) / (1 - alpha)) / (rho * k + nu)
results.append(("Q2", val, 2.324367))

# Q3: discrete optimum over k in 4..9
best_k, best_s = None, -1.0
for kk in range(4, 10):
    s = ((1 - alpha**kk) / (1 - alpha)) / (rho * kk + nu)
    if s > best_s:
        best_s, best_k = s, kk
results.append(("Q3", best_s, 2.324367))
print(f"CLAIM Q3: computed={best_s:.6f} expected=2.324367 match={'yes' if isclose(best_s, 2.324367) and best_k == 7 else 'no'} (k*={best_k})")

# Q4: single weak drafter alpha=0.5
alpha_w = 0.5
best_k, best_s = None, -1.0
for kk in range(1, 20):
    s = ((1 - alpha_w**kk) / (1 - alpha_w)) / (rho * kk + nu)
    if s > best_s:
        best_s, best_k = s, kk
results.append(("Q4", best_s, 1.346154))
print(f"CLAIM Q4: computed={best_s:.6f} expected=1.346154 match={'yes' if isclose(best_s, 1.346154) and best_k == 3 else 'no'} (k*={best_k})")

# Q5
val = 1 - (1 - 0.5)**2
results.append(("Q5", val, 0.75))

# Q6: two-drafter ensemble
alpha2, rho2 = 0.75, 0.2
best_k, best_s = None, -1.0
for kk in range(1, 20):
    s = ((1 - alpha2**kk) / (1 - alpha2)) / (rho2 * kk + nu)
    if s > best_s:
        best_s, best_k = s, kk
results.append(("Q6", best_s, 1.525391))
print(f"CLAIM Q6: computed={best_s:.6f} expected=1.525391 match={'yes' if isclose(best_s, 1.525391) and best_k == 5 else 'no'} (k*={best_k})")

# Q7
val = 1.525391 / 1.346154
results.append(("Q7", val, 1.133147))

# Q8
val = 1 - (1 - 0.6)**3
results.append(("Q8", val, 0.936))

for cid, comp, exp in results:
    match = "yes" if isclose(comp, exp) else "no"
    print(f"CLAIM {cid}: computed={comp:.6f} expected={exp} match={match}")

n = len(results)
m = sum(1 for _, c, e in results if isclose(c, e))
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q3: computed=2.324367 expected=2.324367 match=yes (k*=7)
CLAIM Q4: computed=1.346154 expected=1.346154 match=yes (k*=3)
CLAIM Q6: computed=1.525391 expected=1.525391 match=yes (k*=5)
CLAIM Q1: computed=3.951424 expected=3.951424 match=yes
CLAIM Q2: computed=2.324367 expected=2.324367 match=yes
CLAIM Q3: computed=2.324367 expected=2.324367 match=yes
CLAIM Q4: computed=1.346154 expected=1.346154 match=yes
CLAIM Q5: computed=0.750000 expected=0.75 match=yes
CLAIM Q6: computed=1.525391 expected=1.525391 match=yes
CLAIM Q7: computed=1.133147 expected=1.133147 match=yes
CLAIM Q8: computed=0.936000 expected=0.936 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
