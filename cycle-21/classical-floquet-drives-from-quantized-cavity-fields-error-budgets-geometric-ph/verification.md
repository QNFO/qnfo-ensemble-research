# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Cavity angular frequency for a 5 GHz cavity",
    "inputs": "omega_c/2pi = 5e9 Hz",
    "formula": "omega_c = 2*pi*5e9 = 3.141592654e10 rad/s"
  },
  {
    "id": "Q2",
    "statement": "Bare coupling at g/omega_c = 0.01",
    "inputs": "g/omega_c = 0.01, omega_c = 3.141592654e10 rad/s",
    "formula": "g = 0.01 * omega_c = 3.141592654e8 rad/s"
  },
  {
    "id": "Q3",
    "statement": "Effective drive amplitude Omega = 2g sqrt(n_bar)",
    "inputs": "g = 3.141592654e8 rad/s, n_bar = 1e4",
    "formula": "Omega = 2*g*sqrt(n_bar) = 2*3.141592654e8*100 = 6.283185307e10 rad/s"
  },
  {
    "id": "Q4",
    "statement": "Effective drive ordinary frequency is 10 GHz",
    "inputs": "Omega = 6.283185307e10 rad/s",
    "formula": "nu = Omega/(2*pi) = 6.283185307e10/6.283185307 = 1.0e10 Hz = 10 GHz"
  },
  {
    "id": "Q5",
    "statement": "Relative uncertainty on drive frequency is 11.18%",
    "inputs": "delta_g/g = 0.10, delta_nbar/nbar = 0.10",
    "formula": "delta_Omega/Omega = sqrt(0.10^2 + (0.5*0.10)^2) = sqrt(0.0125) = 0.1118033988749895"
  },
  {
    "id": "Q6",
    "statement": "Drive frequency uncertainty is 1.1 GHz",
    "inputs": "delta_Omega/Omega = 0.1118033988749895, nu = 10 GHz",
    "formula": "delta_nu = 0.1118033988749895 * 10 = 1.118033988749895 GHz"
  },
  {
    "id": "Q7",
    "statement": "Relative amplitude correction is 0.5% at n_bar = 1e4",
    "inputs": "n_bar = 1e4",
    "formula": "delta|alpha|/|alpha| = 1/(2*sqrt(n_bar)) = 1/(2*100) = 0.005"
  },
  {
    "id": "Q8",
    "statement": "Conservative relative correction (fluctuation fraction) is 1%",
    "inputs": "n_bar = 1e4",
    "formula": "Delta_n/n_bar = 1/sqrt(n_bar) = 0.01"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1
omega_c = 2 * math.pi * 5e9
results.append(check("Q1", omega_c, 3.141592654e10))

# Q2
g = 0.01 * omega_c
results.append(check("Q2", g, 3.141592654e8))

# Q3
n_bar = 1e4
Omega = 2 * g * math.sqrt(n_bar)
results.append(check("Q3", Omega, 6.283185307e10))

# Q4
nu = Omega / (2 * math.pi)
results.append(check("Q4", nu, 1.0e10))

# Q5
rel_unc = math.sqrt(0.10**2 + (0.5 * 0.10)**2)
results.append(check("Q5", rel_unc, 0.1118033988749895))

# Q6
delta_nu = rel_unc * 10.0
results.append(check("Q6", delta_nu, 1.118033988749895))

# Q7
amp_corr = 1 / (2 * math.sqrt(n_bar))
results.append(check("Q7", amp_corr, 0.005))

# Q8
fluct = 1 / math.sqrt(n_bar)
results.append(check("Q8", fluct, 0.01))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=31415926535.89793 expected=31415926540.0 match=yes
CLAIM Q2: computed=314159265.3589793 expected=314159265.4 match=yes
CLAIM Q3: computed=62831853071.79586 expected=62831853070.0 match=yes
CLAIM Q4: computed=10000000000.0 expected=10000000000.0 match=yes
CLAIM Q5: computed=0.1118033988749895 expected=0.1118033988749895 match=yes
CLAIM Q6: computed=1.118033988749895 expected=1.118033988749895 match=yes
CLAIM Q7: computed=0.005 expected=0.005 match=yes
CLAIM Q8: computed=0.01 expected=0.01 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
