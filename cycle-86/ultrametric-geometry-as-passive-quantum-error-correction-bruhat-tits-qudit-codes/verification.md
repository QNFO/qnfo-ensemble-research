# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "n_1 for p=3 equals 5",
    "inputs": "p=3, t=1",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q2",
    "statement": "n_2 for p=3 equals 17",
    "inputs": "p=3, t=2",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q3",
    "statement": "n_3 for p=3 equals 53",
    "inputs": "p=3, t=3",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q4",
    "statement": "n_1 for p=2 equals 4",
    "inputs": "p=2, t=1",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q5",
    "statement": "n_2 for p=2 equals 10",
    "inputs": "p=2, t=2",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q6",
    "statement": "n_3 for p=2 equals 22",
    "inputs": "p=2, t=3",
    "formula": "n_t = 1 + (p+1)*(p^t - 1)/(p-1)"
  },
  {
    "id": "Q7",
    "statement": "Passive logical failure probability for p=3, t=1, eps=1e-3 is approximately 9.98e-6",
    "inputs": "n=5, eps=0.001",
    "formula": "P_pass = 1 - (1-eps)^5 - 5*eps*(1-eps)^4"
  },
  {
    "id": "Q8",
    "statement": "Suppression factor eps/P_pass is approximately 100.2",
    "inputs": "eps=0.001, P_pass=9.98e-6",
    "formula": "suppression = eps / P_pass"
  }
]

## Script
```python
import math

def n_t(p, t):
    return 1 + (p + 1) * (p**t - 1) // (p - 1)

def p_pass(n, eps, t):
    total = 0.0
    for k in range(0, t + 1):
        total += math.comb(n, k) * (eps**k) * ((1 - eps)**(n - k))
    return 1 - total

claims = []

# Q1-Q6: ball sizes
expected_n = {
    (3, 1): 5, (3, 2): 17, (3, 3): 53,
    (2, 1): 4, (2, 2): 10, (2, 3): 22,
}
ids = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]
i = 0
for (p, t) in [(3, 1), (3, 2), (3, 3), (2, 1), (2, 2), (2, 3)]:
    computed = n_t(p, t)
    expected = expected_n[(p, t)]
    match = "yes" if computed == expected else "no"
    print(f"CLAIM {ids[i]}: computed={computed} expected={expected} match={match}")
    claims.append(match)
    i += 1

# Q7: passive failure probability, p=3, t=1, eps=1e-3
eps = 1e-3
n = 5
computed_q7 = p_pass(n, eps, 1)
expected_q7 = 9.98e-6
match_q7 = "yes" if math.isclose(computed_q7, expected_q7, rel_tol=1e-2) else "no"
print(f"CLAIM Q7: computed={computed_q7:.6e} expected={expected_q7:.6e} match={match_q7}")
claims.append(match_q7)

# Q8: suppression factor eps / P_pass
# Use the paper's stated P_pass value as the input for this claim
p_pass_input = 9.98e-6
computed_q8 = eps / p_pass_input
expected_q8 = 100.2
match_q8 = "yes" if math.isclose(computed_q8, expected_q8, rel_tol=1e-2) else "no"
print(f"CLAIM Q8: computed={computed_q8:.6f} expected={expected_q8:.6f} match={match_q8}")
claims.append(match_q8)

n_claims = len(claims)
n_match = sum(1 for m in claims if m == "yes")
n_mismatch = n_claims - n_match
print(f"VERIFICATION SUMMARY: {n_claims} claims, {n_match} match, {n_mismatch} mismatch")

```

## Execution output
```
CLAIM Q1: computed=5 expected=5 match=yes
CLAIM Q2: computed=17 expected=17 match=yes
CLAIM Q3: computed=53 expected=53 match=yes
CLAIM Q4: computed=4 expected=4 match=yes
CLAIM Q5: computed=10 expected=10 match=yes
CLAIM Q6: computed=22 expected=22 match=yes
CLAIM Q7: computed=9.980015e-06 expected=9.980000e-06 match=yes
CLAIM Q8: computed=100.200401 expected=100.200000 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
