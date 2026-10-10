# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Tail entropy at generation g is H_tail(g) = 12 * 0.85^g bits; e.g., 5.32 bits at g=5 and 2.36 bits at g=10",
    "inputs": "H_tail(0)=12 bits (assumption), epsilon=0.15 (assumption), retention factor 1-epsilon=0.85",
    "formula": "H_tail(g) = H_tail(0) * (1-epsilon)^g"
  },
  {
    "id": "Q2",
    "statement": "Tail entropy drops below one bit at generation g=16",
    "inputs": "H_tail(0)=12 bits, epsilon=0.15",
    "formula": "g = ceil( ln(12) / ln(1/0.85) )"
  },
  {
    "id": "Q3",
    "statement": "Break-even coupling kappa* = 64.29",
    "inputs": "epsilon=0.15, H_tail(0)=12 bits, beta*V_0=1, p_bridge=0.028",
    "formula": "kappa* = epsilon * H_tail(0) / (beta * V_0 * p_bridge)"
  },
  {
    "id": "Q4",
    "statement": "kappa* is linear in epsilon with slope 428.57; kappa*=21.43 at epsilon=0.05 and 128.57 at epsilon=0.30",
    "inputs": "H_tail(0)=12, p_bridge=0.028, beta*V_0=1",
    "formula": "kappa*(epsilon) = 12 * epsilon / 0.028"
  },
  {
    "id": "Q5",
    "statement": "Re-anchoring every m=5 generations with r=1 sustains average tail entropy of 8.90 bits, a 67.1% uplift over the un-anchored end-of-cycle value of 5.32 bits",
    "inputs": "H_tail(0)=12, epsilon=0.15, m=5, r=1",
    "formula": "H_bar = (H_tail(0) * r / m) * (1 - (1-epsilon)^m) / epsilon; uplift = H_bar / (H_tail(0)*(1-epsilon)^m) - 1"
  },
  {
    "id": "Q6",
    "statement": "After 16 un-anchored generations, 7.43% of technical-vocabulary mass survives",
    "inputs": "epsilon=0.15, g=16",
    "formula": "(1-epsilon)^16 = 0.85^16"
  },
  {
    "id": "Q7",
    "statement": "Secondary model: with rho=0.95, beta_c=1.5, N_0=10^4, pi_0=10^-6, expected links grow from E_0=49.995 to E_10 ≈ 99,524 over ten generations",
    "inputs": "rho=0.95, beta_c=1.5, gamma=1, N_0=10000, pi_0=1e-6, g=10",
    "formula": "E_0 = C(N_0,2)*pi_0; E_10 = E_0 * (beta_c^2 * rho)^10"
  },
  {
    "id": "Q8",
    "statement": "p_bridge = 0.028 from the 97.2% single-discipline finding",
    "inputs": "single-discipline fraction = 0.972 (from [14])",
    "formula": "p_bridge = 1 - 0.972"
  }
]

## Script
```python
import math
from fractions import Fraction

def isclose(a, b, rel_tol=1e-6):
    return math.isclose(a, b, rel_tol=rel_tol)

results = []

# Q1: H_tail(g) = 12 * 0.85^g
H0 = 12.0
eps = 0.15
rho = 1 - eps
H5 = H0 * rho**5
H10 = H0 * rho**10
q1_ok = isclose(H5, 5.32446375) and isclose(H10, 2.36249285)
results.append(("Q1", H5, 5.32446375, q1_ok))
results.append(("Q1b", H10, 2.36249285, isclose(H10, 2.36249285)))

# Q2: g = ceil(ln(12)/ln(1/0.85))
g_star = math.ceil(math.log(12.0) / math.log(1.0 / 0.85))
q2_ok = (g_star == 16)
results.append(("Q2", g_star, 16, q2_ok))

# Q3: kappa* = eps * H0 / (beta*V0 * p_bridge), beta*V0 = 1
p_bridge = 1 - 0.972
kappa_star = eps * H0 / (1.0 * p_bridge)
q3_ok = isclose(kappa_star, 64.29, rel_tol=1e-4)
results.append(("Q3", kappa_star, 64.29, q3_ok))

# Q4: slope = 12/0.028; kappa*(0.05), kappa*(0.30)
slope = H0 / p_bridge
k05 = 0.05 * H0 / p_bridge
k30 = 0.30 * H0 / p_bridge
q4_ok = isclose(slope, 428.57, rel_tol=1e-4) and isclose(k05, 21.43, rel_tol=1e-4) and isclose(k30, 128.57, rel_tol=1e-4)
results.append(("Q4", slope, 428.57, q4_ok))
results.append(("Q4b", k05, 21.43, isclose(k05, 21.43, rel_tol=1e-4)))
results.append(("Q4c", k30, 128.57, isclose(k30, 128.57, rel_tol=1e-4)))

# Q5: re-anchoring m=5, r=1
m = 5
r = 1.0
H_bar = (H0 * r / m) * (1 - rho**m) / eps
H_end = H0 * rho**m
uplift = H_bar / H_end - 1
q5_ok = isclose(H_bar, 8.90, rel_tol=1e-3) and isclose(uplift, 0.671, rel_tol=1e-3)
results.append(("Q5", H_bar, 8.90, isclose(H_bar, 8.90, rel_tol=1e-3)))
results.append(("Q5b", uplift, 0.671, isclose(uplift, 0.671, rel_tol=1e-3)))

# Q6: 0.85^16
surv16 = rho**16
q6_ok = isclose(surv16, 0.0743, rel_tol=1e-3)
results.append(("Q6", surv16, 0.0743, q6_ok))

# Q7: secondary model
rho2 = 0.95
beta_c = 1.5
N0 = 10000
pi0 = 1e-6
gamma = 1
E0 = math.comb(N0, 2) * pi0
growth = (beta_c**2 * rho2**gamma)**10
E10 = E0 * growth
q7_ok = isclose(E0, 49.995, rel_tol=1e-6) and isclose(E10, 99524, rel_tol=1e-2)
results.append(("Q7", E0, 49.995, isclose(E0, 49.995, rel_tol=1e-6)))
results.append(("Q7b", E10, 99524, isclose(E10, 99524, rel_tol=1e-2)))

# Q8: p_bridge = 1 - 0.972
q8_ok = isclose(p_bridge, 0.028, rel_tol=1e-6)
results.append(("Q8", p_bridge, 0.028, q8_ok))

for cid, computed, expected, ok in results:
    print(f"CLAIM {cid}: computed={computed:.6g} expected={expected:.6g} match={'yes' if ok else 'no'}")

n = len(results)
m_ok = sum(1 for r_ in results if r_[3])
k = n - m_ok
print(f"VERIFICATION SUMMARY: {n} claims, {m_ok} match, {k} mismatch")

```

## Execution output
```
CLAIM Q1: computed=5.32446 expected=5.32446 match=yes
CLAIM Q1b: computed=2.36249 expected=2.36249 match=yes
CLAIM Q2: computed=16 expected=16 match=yes
CLAIM Q3: computed=64.2857 expected=64.29 match=yes
CLAIM Q4: computed=428.571 expected=428.57 match=yes
CLAIM Q4b: computed=21.4286 expected=21.43 match=yes
CLAIM Q4c: computed=128.571 expected=128.57 match=yes
CLAIM Q5: computed=8.90072 expected=8.9 match=yes
CLAIM Q5b: computed=0.671664 expected=0.671 match=yes
CLAIM Q6: computed=0.0742511 expected=0.0743 match=yes
CLAIM Q7: computed=49.995 expected=49.995 match=yes
CLAIM Q7b: computed=99537.7 expected=99524 match=yes
CLAIM Q8: computed=0.028 expected=0.028 match=yes
VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch

[exit 0]
```
