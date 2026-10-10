# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Rate ratio Gamma_infty/Gamma_3 = 4",
    "inputs": "lambda_infty = 2*lambda_3",
    "formula": "Gamma_infty/Gamma_3 = (lambda_infty/lambda_3)^2"
  },
  {
    "id": "Q2",
    "statement": "Gamma_infty3 = 6.25e-2",
    "inputs": "lambda_infty = 1e-12, N_b = 1e23, sigma_A^2 = 1, lambda_3 = lambda_infty/2",
    "formula": "Gamma_infty3 = 0.5*(lambda_infty^2 + lambda_3^2)*N_b*sigma_A^2"
  },
  {
    "id": "Q3",
    "statement": "Coherence timescale T_x = 16 model units",
    "inputs": "Gamma_infty3 = 6.25e-2",
    "formula": "T_x = 1/Gamma_infty3"
  },
  {
    "id": "Q4",
    "statement": "Residual coherence at t = 5*T_x is e^-5 ≈ 6.738e-3 of initial value",
    "inputs": "t = 80, T_x = 16",
    "formula": "exp(-t/T_x)"
  },
  {
    "id": "Q5",
    "statement": "Born-rule deviation delta = 3.3009e-3 at t = 80 for |alpha|^2 = 0.6, |beta|^2 = 0.4",
    "inputs": "|alpha|^2 = 0.6, |beta|^2 = 0.4, t = 80, Gamma_infty3 = 6.25e-2",
    "formula": "delta = sqrt(0.6*0.4)*exp(-Gamma_infty3*t)"
  },
  {
    "id": "Q6",
    "statement": "Consistency bound t >= 58.41 model units",
    "inputs": "epsilon = 1.3e-2, worst case sqrt(|alpha|^2|beta|^2) = 0.5, Gamma_infty3 = 6.25e-2",
    "formula": "t = ln(0.5/epsilon)/Gamma_infty3"
  },
  {
    "id": "Q7",
    "statement": "Physical-time projection T_x ≈ 1.6e-12 s (labeled projection)",
    "inputs": "T_x = 16 model units, tau = 1e-13 s",
    "formula": "T_x_phys = 16*tau"
  },
  {
    "id": "Q8",
    "statement": "Full suppression time ≈ 5.84e-12 s (labeled projection)",
    "inputs": "t = 58.41 model units, tau = 1e-13 s",
    "formula": "t_phys = 58.41*tau"
  }
]

## Script
```python
import math

def check(cid, computed, expected, tol=1e-6):
    if expected is None:
        match = None
    else:
        match = math.isclose(computed, expected, rel_tol=tol)
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")

# Q1: rate ratio
lam_ratio = 2.0
q1 = lam_ratio**2
check("Q1", q1, 4.0)

# Q2: Gamma_infty3
lam_inf = 1e-12
lam_3 = lam_inf / 2.0
N_b = 1e23
sigma2 = 1.0
q2 = 0.5 * (lam_inf**2 + lam_3**2) * N_b * sigma2
check("Q2", q2, 6.25e-2)

# Q3: T_x
q3 = 1.0 / q2
check("Q3", q3, 16.0)

# Q4: residual coherence at t = 5*T_x
t4 = 5 * q3
q4 = math.exp(-t4 / q3)
check("Q4", q4, math.exp(-5.0))

# Q5: Born-rule deviation at t = 80
a2, b2 = 0.6, 0.4
t5 = 80.0
q5 = math.sqrt(a2 * b2) * math.exp(-q2 * t5)
check("Q5", q5, 3.3009e-3)

# Q6: consistency bound
eps = 1.3e-2
worst = 0.5
q6 = math.log(worst / eps) / q2
check("Q6", q6, 58.41)

# Q7: physical-time projection
tau = 1e-13
q7 = q3 * tau
check("Q7", q7, 1.6e-12)

# Q8: full suppression time projection
q8 = q6 * tau
check("Q8", q8, 5.84e-12)

# summary
results = [q1, q2, q3, q4, q5, q6, q7, q8]
expected = [4.0, 6.25e-2, 16.0, math.exp(-5.0), 3.3009e-3, 58.41, 1.6e-12, 5.84e-12]
mism = sum(1 for c, e in zip(results, expected) if not math.isclose(c, e, rel_tol=1e-6))
print(f"VERIFICATION SUMMARY: {len(results)} claims, {len(results)-mism} match, {mism} mismatch")

```

## Execution output
```
CLAIM Q1: computed=4.0 expected=4.0 match=True
CLAIM Q2: computed=0.06249999999999999 expected=0.0625 match=True
CLAIM Q3: computed=16.000000000000004 expected=16.0 match=True
CLAIM Q4: computed=0.006737946999085467 expected=0.006737946999085467 match=True
CLAIM Q5: computed=0.0033009064123353123 expected=0.0033009 match=False
CLAIM Q6: computed=58.39453985537049 expected=58.41 match=False
CLAIM Q7: computed=1.6000000000000005e-12 expected=1.6e-12 match=True
CLAIM Q8: computed=5.839453985537049e-12 expected=5.84e-12 match=False
VERIFICATION SUMMARY: 8 claims, 5 match, 3 mismatch

[exit 0]
```
