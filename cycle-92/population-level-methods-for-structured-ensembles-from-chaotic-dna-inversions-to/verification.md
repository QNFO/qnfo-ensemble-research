# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Average segment length of a uniformly chosen contiguous segment of a length-10 binary sequence is 4.0",
    "inputs": "L=10; total length over all segments S=220 (sum of k*(10-k+1) for k=1..10); number of segments 55",
    "formula": "S = sum_{k=1}^{10} k*(10-k+1); average = S / (L*(L+1)/2) = 220/55"
  },
  {
    "id": "Q2",
    "statement": "Saturation time of expected Hamming distance under projection P0 is 3 steps",
    "inputs": "L=10; average segment length 4.0",
    "formula": "t_sat = ceil(L / 4.0) = ceil(10/4)"
  },
  {
    "id": "Q3",
    "statement": "First moment of the gain-weighted population moves at rate 1/3 per unit input",
    "inputs": "uniform gain density rho(omega)=1/2 on [-1,1]",
    "formula": "integral_{-1}^{1} omega^2 * rho(omega) domega = (1/2)*[omega^3/3]_{-1}^{1} = 1/3"
  },
  {
    "id": "Q4",
    "statement": "Mean advance is identically zero for the sign-symmetric uniform gain distribution",
    "inputs": "uniform rho(omega)=1/2 on [-1,1]; x_omega = omega*U(t)",
    "formula": "integral_{-1}^{1} omega * rho(omega) domega = (1/2)*[omega^2/2]_{-1}^{1} = 0"
  },
  {
    "id": "Q5",
    "statement": "Population variance at t=0.3 with u=+1 is 0.03 (sigma approximately 0.1732)",
    "inputs": "U(0.3)=0.3; uniform rho",
    "formula": "sigma^2 = U(t)^2 * (1/3) = 0.09/3 = 0.03; sigma = sqrt(0.03)"
  },
  {
    "id": "Q6",
    "statement": "Minimum steering time to first moment 0.1 is 0.3 time units",
    "inputs": "M1_target=0.1; rate 1/3; |U(T)| <= T",
    "formula": "U(T) = 3*0.1 = 0.3; T_min = 0.3/1 = 0.3; check M1(0.3) = (1/3)*0.3 = 0.1"
  },
  {
    "id": "Q7",
    "statement": "For the skewed right-triangular density, the second-moment coefficient is 7/18 and the minimum steering time to 0.1 is 1.8/7 ≈ 0.2571",
    "inputs": "rho_s(omega)=(2/3)(omega+1) on [0,1]; M1_target=0.1",
    "formula": "c2 = (2/3)*integral_0^1 (omega^3+omega^2) domega = (2/3)*(1/4+1/3) = 7/18; T_min = 0.1/(7/18) = 1.8/7"
  },
  {
    "id": "Q8",
    "statement": "Baseline (best single leg, alpha=0.7, gamma=4) expected tokens per cycle is 2.7731",
    "inputs": "alpha=0.7; gamma=4; alpha^5=0.16807",
    "formula": "E[N] = (1 - alpha^(gamma+1))/(1 - alpha) = (1 - 0.16807)/0.3 = 0.83193/0.3"
  }
]

## Script
```python
import math

def isclose(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: average segment length for L=10
L = 10
S = sum(k * (10 - k + 1) for k in range(1, L + 1))
n_seg = L * (L + 1) // 2
avg = S / n_seg
results.append(("Q1", avg, 4.0))

# Q2: saturation time under projection P0
t_sat = math.ceil(L / 4.0)
results.append(("Q2", t_sat, 3))

# Q3: first-moment rate for uniform density on [-1,1]
# integral of omega^2 * (1/2) domega from -1 to 1
rate = 0.5 * (1/3 - (-1/3))
results.append(("Q3", rate, 1/3))

# Q4: mean advance integral = 0
mean_int = 0.5 * (0.5**2/2 - (-0.5)**2/2)
results.append(("Q4", mean_int, 0.0))

# Q5: variance at t=0.3, u=+1
U = 0.3
var = U**2 * (1/3)
sigma = math.sqrt(var)
results.append(("Q5", var, 0.03))
results.append(("Q5-sigma", sigma, math.sqrt(0.03)))  # paper states sigma ~ 0.1732

# Q6: minimum steering time to M1 target 0.1
M1_target = 0.1
U_req = M1_target / (1/3)
T_min = U_req / 1.0
check = (1/3) * 0.3
results.append(("Q6", T_min, 0.3))
results.append(("Q6-check", check, 0.1))

# Q7: skewed density c2 and steering time
# rho_s(omega) = (2/3)(omega+1) on [0,1]
c2 = (2/3) * (1/4 + 1/3)
T_min_s = 0.1 / c2
results.append(("Q7-c2", c2, 7/18))
results.append(("Q7-Tmin", T_min_s, 1.8/7))

# Q8: baseline tokens per cycle, alpha=0.7, gamma=4
alpha = 0.7
gamma = 4
EN = (1 - alpha**(gamma + 1)) / (1 - alpha)
results.append(("Q8", EN, 2.7731))

for cid, computed, expected in results:
    if isinstance(expected, (int, float)) and isinstance(computed, (int, float)):
        match = isclose(float(computed), float(expected))
    else:
        match = computed == expected
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={'yes' if match else 'no'}")

n = len(results)
m = sum(1 for _, c, e in results if (math.isclose(float(c), float(e), rel_tol=1e-6) if isinstance(c, (int, float)) and isinstance(e, (int, float)) else c == e))
k = n - m
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {k} mismatch")

```

## Execution output
```
CLAIM Q1: computed=4.0 expected=4.0 match=yes
CLAIM Q2: computed=3 expected=3 match=yes
CLAIM Q3: computed=0.3333333333333333 expected=0.3333333333333333 match=yes
CLAIM Q4: computed=0.0 expected=0.0 match=yes
CLAIM Q5: computed=0.03 expected=0.03 match=yes
CLAIM Q5-sigma: computed=0.17320508075688773 expected=0.17320508075688773 match=yes
CLAIM Q6: computed=0.30000000000000004 expected=0.3 match=yes
CLAIM Q6-check: computed=0.09999999999999999 expected=0.1 match=yes
CLAIM Q7-c2: computed=0.38888888888888884 expected=0.3888888888888889 match=yes
CLAIM Q7-Tmin: computed=0.2571428571428572 expected=0.2571428571428572 match=yes
CLAIM Q8: computed=2.7731 expected=2.7731 match=yes
VERIFICATION SUMMARY: 11 claims, 11 match, 0 mismatch

[exit 0]
```
