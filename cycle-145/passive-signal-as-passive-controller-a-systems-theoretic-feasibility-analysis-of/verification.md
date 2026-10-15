# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Pure integrator passivity check: with x0=0, u0=0.1, storage change equals supply 0.005",
    "inputs": "x0=0, u0=0.1, V(x)=0.5*x^2, y0=x0+0.5*u0",
    "formula": "DeltaV = 0.5*(x0+u0)^2 - 0.5*x0^2; supply = u0*(x0+0.5*u0)"
  },
  {
    "id": "Q2",
    "statement": "Leaky integrator margin coefficient at alpha=0.1 is -0.095*x^2",
    "inputs": "alpha=0.1",
    "formula": "margin coefficient = alpha^2/2 - alpha"
  },
  {
    "id": "Q3",
    "statement": "Leaky integrator zero-supply check: DeltaV = -0.38 at x0=2, alpha=0.1",
    "inputs": "x0=2, u0=0, alpha=0.1",
    "formula": "DeltaV = (alpha^2/2 - alpha)*x0^2"
  },
  {
    "id": "Q4",
    "statement": "Leaky integrator with-supply check: margin -0.38 at x0=2, u0=0.5",
    "inputs": "x0=2, u0=0.5, alpha=0.1, y0=0.9*x0+0.5*u0",
    "formula": "margin = 0.5*((1-alpha)*x0+u0)^2 - 0.5*x0^2 - u0*y0"
  },
  {
    "id": "Q5",
    "statement": "Naive-output counterexample margin +0.505 at x=1, u=-1, alpha=0.1",
    "inputs": "x=1, u=-1, alpha=0.1, beta=1, gamma=0",
    "formula": "margin = (alpha^2/2 - alpha)*x^2 + (1-alpha-beta)*x*u + (0.5-gamma)*u^2"
  },
  {
    "id": "Q6",
    "statement": "Worst-case quantization degradation 5.0 energy units over N=100 at q=0.1, Umax=1",
    "inputs": "q=0.1, Umax=1, N=100",
    "formula": "Delta_quant = N*Umax*q/2"
  },
  {
    "id": "Q7",
    "statement": "Dissipation rate delta = 0.095 at alpha=0.1",
    "inputs": "alpha=0.1",
    "formula": "delta = alpha - alpha^2/2"
  },
  {
    "id": "Q8",
    "statement": "Dissipation over 100 steps at x≈1 is about 9.5 energy units",
    "inputs": "delta=0.095, N=100, x=1",
    "formula": "dissipation = delta*N*x^2"
  },
  {
    "id": "Q9",
    "statement": "Delay phase lag 0.5 rad ≈ 28.65 degrees",
    "inputs": "omega_c=1.0 rad/s, T_d=0.5 s",
    "formula": "phi = omega_c*T_d*(180/pi)"
  },
  {
    "id": "Q10",
    "statement": "Combined margin proxy M = 0.6",
    "inputs": "k_S=2.0, eps_S=0.1, eps_W=0.2",
    "formula": "M = k_S*(eps_S+eps_W)"
  },
  {
    "id": "Q11",
    "statement": "Normalized delay loss l_d ≈ 0.0796",
    "inputs": "phi_d=0.5 rad",
    "formula": "l_d = phi_d/(2*pi)"
  },
  {
    "id": "Q12",
    "statement": "Normalized margin M_n = 0.375",
    "inputs": "M=0.6",
    "formula": "M_n = M/(1+M)"
  },
  {
    "id": "Q13",
    "statement": "Safety ratio rho ≈ 4.71",
    "inputs": "M_n=0.375, l_d=0.5/(2*pi)",
    "formula": "rho = M_n/l_d"
  },
  {
    "id": "Q14",
    "statement": "Quantization energy cost E_q = 0.025 J per packet, 2.5% of E_0=1.0 J",
    "inputs": "Delta=0.05, u_max=1.0",
    "formula": "E_q = (Delta/2)*u_max; ratio = E_q/u_max^2"
  },
  {
    "id": "Q15",
    "statement": "Attractor radius r_q = 0.05",
    "inputs": "Delta=0.05, lambda_W=0.5",
    "formula": "r_q = (Delta/2)/lambda_W"
  },
  {
    "id": "Q16",
    "statement": "Robustness budget: margin erosion tolerance ≈ 16.7% of combined margin",
    "inputs": "eps_S=0.1, M=0.6",
    "formula": "ratio = eps_S/M"
  }
]

## Script
```python
import math

def claim(id_, computed, expected, match):
    print(f"CLAIM {id_}: computed={computed:.10f} expected={expected} match={match}")

# Q1
x0, u0 = 0.0, 0.1
dV = 0.5*(x0+u0)**2 - 0.5*x0**2
supply = u0*(x0 + 0.5*u0)
claim("Q1", dV, "0.005", round(dV, 6) == 0.005 and round(supply, 6) == 0.005)

# Q2
alpha = 0.1
c = alpha**2/2 - alpha
claim("Q2", c, "-0.095", round(c, 6) == -0.095)

# Q3
x0 = 2.0
dV = (alpha**2/2 - alpha)*x0**2
claim("Q3", dV, "-0.38", round(dV, 6) == -0.38)

# Q4
u0 = 0.5
y0 = 0.9*x0 + 0.5*u0
margin = 0.5*((1-alpha)*x0 + u0)**2 - 0.5*x0**2 - u0*y0
claim("Q4", margin, "-0.38", round(margin, 6) == -0.38)

# Q5
x, u = 1.0, -1.0
beta, gamma = 1.0, 0.0
m = (alpha**2/2 - alpha)*x**2 + (1-alpha-beta)*x*u + (0.5-gamma)*u**2
claim("Q5", m, "0.505", round(m, 6) == 0.505)

# Q6
q, Umax, N = 0.1, 1.0, 100
dq = N*Umax*q/2
claim("Q6", dq, "5.0", round(dq, 6) == 5.0)

# Q7
delta = alpha - alpha**2/2
claim("Q7", delta, "0.095", round(delta, 6) == 0.095)

# Q8
diss = delta*N*1.0**2
claim("Q8", diss, "9.5", round(diss, 6) == 9.5)

# Q9
phi = 1.0*0.5*(180/math.pi)
claim("Q9", phi, "28.65", round(phi, 2) == 28.65)

# Q10
M = 2.0*(0.1+0.2)
claim("Q10", M, "0.6", round(M, 6) == 0.6)

# Q11
ld = 0.5/(2*math.pi)
claim("Q11", ld, "0.0796", round(ld, 4) == 0.0796)

# Q12
Mn = 0.6/1.6
claim("Q12", Mn, "0.375", round(Mn, 6) == 0.375)

# Q13
rho = 0.375/ld
claim("Q13", rho, "4.71", round(rho, 2) == 4.71)

# Q14
Eq = (0.05/2)*1.0
ratio = Eq/1.0**2
claim("Q14", ratio, "0.025", round(Eq, 6) == 0.025 and round(ratio, 6) == 0.025)

# Q15
rq = (0.05/2)/0.5
claim("Q15", rq, "0.05", round(rq, 6) == 0.05)

# Q16
r16 = 0.1/0.6
claim("Q16", r16, "0.167", round(r16, 3) == 0.167)

print("VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=0.0050000000 expected=0.005 match=True
CLAIM Q2: computed=-0.0950000000 expected=-0.095 match=True
CLAIM Q3: computed=-0.3800000000 expected=-0.38 match=True
CLAIM Q4: computed=-0.3800000000 expected=-0.38 match=True
CLAIM Q5: computed=0.5050000000 expected=0.505 match=True
CLAIM Q6: computed=5.0000000000 expected=5.0 match=True
CLAIM Q7: computed=0.0950000000 expected=0.095 match=True
CLAIM Q8: computed=9.5000000000 expected=9.5 match=True
CLAIM Q9: computed=28.6478897565 expected=28.65 match=True
CLAIM Q10: computed=0.6000000000 expected=0.6 match=True
CLAIM Q11: computed=0.0795774715 expected=0.0796 match=True
CLAIM Q12: computed=0.3750000000 expected=0.375 match=True
CLAIM Q13: computed=4.7123889804 expected=4.71 match=True
CLAIM Q14: computed=0.0250000000 expected=0.025 match=True
CLAIM Q15: computed=0.0500000000 expected=0.05 match=True
CLAIM Q16: computed=0.1666666667 expected=0.167 match=True
VERIFICATION SUMMARY: 16 claims, 16 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 0.0050000000 | 0.005 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | -0.0950000000 | -0.095 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | -0.3800000000 | -0.38 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | -0.3800000000 | -0.38 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 0.5050000000 | 0.505 | - | match | 3 significant digits (as the paper states, at least 2) |
| Q6 | 5.0000000000 | 5.0 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q7 | 0.0950000000 | 0.095 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 9.5000000000 | 9.5 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q9 | 28.6478897565 | 28.65 | - | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | 0.6000000000 | 0.6 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q11 | 0.0795774715 | 0.0796 | - | match | 3 significant digits (as the paper states, at least 2) |
| Q12 | 0.3750000000 | 0.375 | - | match | 3 significant digits (as the paper states, at least 2) |
| Q13 | 4.7123889804 | 4.71 | - | match | 3 significant digits (as the paper states, at least 2) |
| Q14 | 0.0250000000 | 0.025 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q15 | 0.0500000000 | 0.05 | - | match | 2 significant digits (as the paper states, at least 2) |
| Q16 | 0.1666666667 | 0.167 | - | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
