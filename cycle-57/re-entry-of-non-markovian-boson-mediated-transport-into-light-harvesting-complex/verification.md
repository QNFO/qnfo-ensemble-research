# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Optimal dephasing rate Gamma* = Delta = 100 cm^-1",
    "inputs": "Delta = 100 cm^-1",
    "formula": "Gamma* = Delta"
  },
  {
    "id": "Q2",
    "statement": "Optimal hopping rate k* = 9 cm^-1",
    "inputs": "V = 30 cm^-1, Delta = 100 cm^-1",
    "formula": "k* = V^2 / Delta"
  },
  {
    "id": "Q3",
    "statement": "Angular frequency omega* = 1.6952e12 rad/s",
    "inputs": "c = 2.9979e10 cm/s, k* = 9 cm^-1",
    "formula": "omega* = 2*pi*c*k*"
  },
  {
    "id": "Q4",
    "statement": "Transfer time tau_T = 5.899e-13 s (0.5899 ps)",
    "inputs": "omega* = 1.6952e12 rad/s",
    "formula": "tau_T = 1 / omega*"
  },
  {
    "id": "Q5",
    "statement": "Trapping-limited efficiency eta = 0.999001",
    "inputs": "kappa = 1 ps^-1, tau_e = 1000 ps",
    "formula": "eta = kappa / (kappa + 1/tau_e)"
  },
  {
    "id": "Q6",
    "statement": "Fast-limit memory ratio R_fast = 0.1695",
    "inputs": "tau_B = 0.1 ps, tau_T = 0.5899 ps",
    "formula": "R_fast = tau_B / tau_T"
  },
  {
    "id": "Q7",
    "statement": "Slow-limit memory ratio R_slow = 1.6953",
    "inputs": "tau_B = 1 ps, tau_T = 0.5899 ps",
    "formula": "R_slow = tau_B / tau_T"
  },
  {
    "id": "Q8",
    "statement": "Sensitivity: for V = 20 cm^-1, tau_T = 1.3272 ps, R_fast = 0.0753, R_slow = 0.7535",
    "inputs": "V = 20 cm^-1, Delta = 100 cm^-1, c = 2.9979e10 cm/s, tau_B = 0.1 ps and 1 ps",
    "formula": "k* = V^2/Delta; omega* = 2*pi*c*k*; tau_T = 1/omega*; R = tau_B/tau_T"
  }
]

## Script
```python
import math

c = 2.9979e10  # cm/s

def tau_T_ps(V, Delta):
    k = V**2 / Delta          # cm^-1
    omega = 2 * math.pi * c * k  # rad/s
    tau = 1 / omega           # s
    return k, omega, tau * 1e12  # ps

results = []

# Q1
g = 100.0
results.append(("Q1", g, 100.0, g == 100.0))

# Q2
k2 = 30**2 / 100
results.append(("Q2", k2, 9.0, math.isclose(k2, 9.0, rel_tol=1e-6)))

# Q3
omega3 = 2 * math.pi * c * 9
results.append(("Q3", omega3, 1.6952e12, math.isclose(omega3, 1.6952e12, rel_tol=1e-3)))

# Q4
tau4 = 1 / omega3
results.append(("Q4", tau4, 5.899e-13, math.isclose(tau4, 5.899e-13, rel_tol=1e-3)))

# Q5
eta5 = 1 / (1 + 1/1000)
results.append(("Q5", eta5, 0.999001, math.isclose(eta5, 0.999001, rel_tol=1e-6)))

# Q6, Q7
_, _, tau_ps = tau_T_ps(30, 100)
R6 = 0.1 / tau_ps
R7 = 1.0 / tau_ps
results.append(("Q6", R6, 0.1695, math.isclose(R6, 0.1695, rel_tol=1e-3)))
results.append(("Q7", R7, 1.6953, math.isclose(R7, 1.6953, rel_tol=1e-3)))

# Q8
_, _, tau8 = tau_T_ps(20, 100)
R8f = 0.1 / tau8
R8s = 1.0 / tau8
ok8 = (math.isclose(tau8, 1.3272, rel_tol=1e-3)
       and math.isclose(R8f, 0.0753, rel_tol=1e-2)
       and math.isclose(R8s, 0.7535, rel_tol=1e-2))
results.append(("Q8", (tau8, R8f, R8s), (1.3272, 0.0753, 0.7535), ok8))

for cid, comp, exp, match in results:
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={'yes' if match else 'no'}")

n = len(results)
m = sum(1 for r in results if r[3])
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=100.0 expected=100.0 match=yes
CLAIM Q2: computed=9.0 expected=9.0 match=yes
CLAIM Q3: computed=1695272510915.4314 expected=1695200000000.0 match=yes
CLAIM Q4: computed=5.898756651578154e-13 expected=5.899e-13 match=yes
CLAIM Q5: computed=0.9990009990009991 expected=0.999001 match=yes
CLAIM Q6: computed=0.16952725109154315 expected=0.1695 match=yes
CLAIM Q7: computed=1.6952725109154314 expected=1.6953 match=yes
CLAIM Q8: computed=(1.3272202466050846, 0.07534544492957473, 0.7534544492957473) expected=(1.3272, 0.0753, 0.7535) match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
