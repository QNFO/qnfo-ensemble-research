# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Per-run speedup for a resumed task is S_run = 1/(1-f+α)",
    "inputs": "f (shared-prefix fraction), α (materialization overhead fraction)",
    "formula": "S_run = 1/(1 - f + α)"
  },
  {
    "id": "Q2",
    "statement": "Amortized workload speedup over R tasks with one prefix group: S_R = R / [1+α + (R-1)(1-f+α)]",
    "inputs": "R (number of tasks), f, α",
    "formula": "S_R = R / (1 + α + (R-1)*(1 - f + α))"
  },
  {
    "id": "Q3",
    "statement": "Break-even condition for reuse is f ≥ α",
    "inputs": "f, α",
    "formula": "1 - f + α <= 1  ⟺  f >= α"
  },
  {
    "id": "Q4",
    "statement": "A 2.95× speedup at α = 0.05 requires f ≈ 0.711017",
    "inputs": "S = 2.95, α = 0.05",
    "formula": "f = 1 - 1/S + α = 1 - 0.33898 + 0.05 = 0.711017"
  },
  {
    "id": "Q5",
    "statement": "A 32.84× speedup at α = 0.05 gives f = 1.019549, which is infeasible (f > 1)",
    "inputs": "S = 32.84, α = 0.05",
    "formula": "f = 1 - 1/32.84 + 0.05 = 1 - 0.030451 + 0.05 = 1.019549"
  },
  {
    "id": "Q6",
    "statement": "The 32.84× result requires materialization overhead α ≤ 1/32.84 ≈ 0.0304507 (~3.05%)",
    "inputs": "S = 32.84, f ≤ 1",
    "formula": "α_max = 1/S = 1/32.84 = 0.0304507"
  },
  {
    "id": "Q7",
    "statement": "A 32.84× speedup at α = 0.01 requires f ≈ 0.979549",
    "inputs": "S = 32.84, α = 0.01",
    "formula": "f = 1 - 1/32.84 + 0.01 = 0.979549"
  },
  {
    "id": "Q8",
    "statement": "A 2.95× speedup at α = 0.01 requires f ≈ 0.671017",
    "inputs": "S = 2.95, α = 0.01",
    "formula": "f = 1 - 1/2.95 + 0.01 = 0.671017"
  }
]

## Script
```python
import math

def close(a, b):
    if a is None or b is None:
        return a == b
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(a, b, rel_tol=1e-6)
    return a == b

results = []

# Q1: S_run = 1/(1-f+α), with representative inputs f=0.90, α=0.02
f, alpha = 0.90, 0.02
computed = 1.0 / (1.0 - f + alpha)
expected = 1.0 / (1.0 - f + alpha)
results.append(("Q1", computed, expected))

# Q2: S_R = R / (1 + α + (R-1)(1-f+α)), R=100, f=0.90, α=0.02
R = 100
computed = R / (1 + alpha + (R - 1) * (1 - f + alpha))
expected = 100 / 12.90
results.append(("Q2", computed, expected))

# Q3: break-even f >= α; test f=0.05, α=0.02 -> True; f=0.01, α=0.02 -> False
f3, a3 = 0.05, 0.02
computed = (1 - f3 + a3) <= 1
expected = f3 >= a3
results.append(("Q3", computed, expected))

# Q4: S=2.95, α=0.05 -> f = 1 - 1/S + α
S, a4 = 2.95, 0.05
computed = 1 - 1 / S + a4
expected = 0.711017
results.append(("Q4", computed, expected))

# Q5: S=32.84, α=0.05 -> f = 1.019549, infeasible (f > 1)
S, a5 = 32.84, 0.05
computed = 1 - 1 / S + a5
expected = 1.019549
results.append(("Q5", computed, expected))
infeasible = computed > 1.0
results.append(("Q5-infeasible", infeasible, True))

# Q6: α_max = 1/S = 1/32.84
computed = 1 / 32.84
expected = 0.0304507
results.append(("Q6", computed, expected))

# Q7: S=32.84, α=0.01 -> f ≈ 0.979549
computed = 1 - 1 / 32.84 + 0.01
expected = 0.979549
results.append(("Q7", computed, expected))

# Q8: S=2.95, α=0.01 -> f ≈ 0.671017
computed = 1 - 1 / 2.95 + 0.01
expected = 0.671017
results.append(("Q8", computed, expected))

match_count = 0
for cid, comp, exp in results:
    m = close(comp, exp)
    if m:
        match_count += 1
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if m else 'no'}")

n = len(results)
print(f"VERIFICATION SUMMARY: {n} claims, {match_count} match, {n - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=8.333333333333334 expected=8.333333333333334 match=yes
CLAIM Q2: computed=7.7519379844961245 expected=7.751937984496124 match=yes
CLAIM Q3: computed=True expected=True match=yes
CLAIM Q4: computed=0.7110169491525424 expected=0.711017 match=yes
CLAIM Q5: computed=1.0195493300852618 expected=1.019549 match=yes
CLAIM Q5-infeasible: computed=True expected=True match=yes
CLAIM Q6: computed=0.03045066991473812 expected=0.0304507 match=yes
CLAIM Q7: computed=0.9795493300852619 expected=0.979549 match=yes
CLAIM Q8: computed=0.6710169491525424 expected=0.671017 match=yes
VERIFICATION SUMMARY: 9 claims, 9 match, 0 mismatch

[exit 0]
```
