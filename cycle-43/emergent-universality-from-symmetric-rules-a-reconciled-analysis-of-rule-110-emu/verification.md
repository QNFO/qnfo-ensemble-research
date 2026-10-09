# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Steady-state wall fraction rho* = sqrt(a*eps/b); with a=1, b=1, eps=1e-2 gives rho*=0.1",
    "inputs": "a=1, b=1, eps=0.01",
    "formula": "rho* = sqrt(a*eps/b)"
  },
  {
    "id": "Q2",
    "statement": "With a=1, b=1, eps=1e-4, rho* = 0.01",
    "inputs": "a=1, b=1, eps=0.0001",
    "formula": "rho* = sqrt(a*eps/b)"
  },
  {
    "id": "Q3",
    "statement": "With a=1, b=1, eps=0.25, rho* = 0.5",
    "inputs": "a=1, b=1, eps=0.25",
    "formula": "rho* = sqrt(a*eps/b)"
  },
  {
    "id": "Q4",
    "statement": "Relaxation time tau = 1/sqrt(a*b*eps); with a=b=1, eps=1e-2, tau = 10 steps",
    "inputs": "a=1, b=1, eps=0.01",
    "formula": "tau = 1/sqrt(a*b*eps)"
  },
  {
    "id": "Q5",
    "statement": "With a=b=1, eps=1e-4, tau = 100 steps",
    "inputs": "a=1, b=1, eps=0.0001",
    "formula": "tau = 1/sqrt(a*b*eps)"
  },
  {
    "id": "Q6",
    "statement": "Noiseless coarsening law rho(t) = rho0/(1 + b*rho0*t)",
    "inputs": "rho0, b, t (symbolic)",
    "formula": "rho(t) = rho0/(1 + b*rho0*t)"
  },
  {
    "id": "Q7",
    "statement": "Lock-on threshold rho0 >= 1/(2*v*T) = 5e-4 walls per site for v=1, T=1000",
    "inputs": "v=1, T=1000",
    "formula": "rho0 = 1/(2*v*T)"
  },
  {
    "id": "Q8",
    "statement": "For v=0.1, threshold rises to rho0 >= 5e-3",
    "inputs": "v=0.1, T=1000",
    "formula": "rho0 = 1/(2*v*T)"
  }
]

## Script
```python
import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: rho* = sqrt(a*eps/b), a=1, b=1, eps=0.01 -> 0.1
a, b, eps = 1.0, 1.0, 0.01
rho = math.sqrt(a * eps / b)
results.append(("Q1", rho, 0.1))

# Q2: a=1, b=1, eps=1e-4 -> 0.01
eps = 0.0001
rho = math.sqrt(a * eps / b)
results.append(("Q2", rho, 0.01))

# Q3: a=1, b=1, eps=0.25 -> 0.5
eps = 0.25
rho = math.sqrt(a * eps / b)
results.append(("Q3", rho, 0.5))

# Q4: tau = 1/sqrt(a*b*eps), a=b=1, eps=0.01 -> 10
a, b, eps = 1.0, 1.0, 0.01
tau = 1.0 / math.sqrt(a * b * eps)
results.append(("Q4", tau, 10.0))

# Q5: a=b=1, eps=1e-4 -> 100
eps = 0.0001
tau = 1.0 / math.sqrt(a * b * eps)
results.append(("Q5", tau, 100.0))

# Q6: symbolic coarsening law rho(t) = rho0/(1 + b*rho0*t); verify numerically
# pick rho0=0.01, b=1, t=1000 -> rho = 0.01/(1+10) = 0.0009090909...
rho0, b, t = 0.01, 1.0, 1000.0
rho_t = rho0 / (1 + b * rho0 * t)
# independent check: integrate d rho/dt = -b rho^2 analytically via ODE step (RK4, small dt)
def drho(rho, b):
    return -b * rho * rho
r, dt = rho0, 0.01
steps = int(round(t / dt))
for _ in range(steps):
    k1 = drho(r, b)
    k2 = drho(r + dt/2 * k1, b)
    k3 = drho(r + dt/2 * k2, b)
    k4 = drho(r + dt * k3, b)
    r += dt / 6 * (k1 + 2*k2 + 2*k3 + k4)
results.append(("Q6", rho_t, r))

# Q7: rho0 = 1/(2*v*T), v=1, T=1000 -> 5e-4
v, T = 1.0, 1000.0
thr = 1.0 / (2 * v * T)
results.append(("Q7", thr, 5e-4))

# Q8: v=0.1, T=1000 -> 5e-3
v = 0.1
thr = 1.0 / (2 * v * T)
results.append(("Q8", thr, 5e-3))

match_count = 0
for qid, computed, expected in results:
    m = isclose(computed, expected)
    if m:
        match_count += 1
    print(f"CLAIM {qid}: computed={computed} expected={expected} match={'yes' if m else 'no'}")

print(f"VERIFICATION SUMMARY: {len(results)} claims, {match_count} match, {len(results) - match_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.1 expected=0.1 match=yes
CLAIM Q2: computed=0.01 expected=0.01 match=yes
CLAIM Q3: computed=0.5 expected=0.5 match=yes
CLAIM Q4: computed=10.0 expected=10.0 match=yes
CLAIM Q5: computed=100.0 expected=100.0 match=yes
CLAIM Q6: computed=0.0009090909090909091 expected=0.0009090909090909143 match=yes
CLAIM Q7: computed=0.0005 expected=0.0005 match=yes
CLAIM Q8: computed=0.005 expected=0.005 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
