# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Electron rest energy m_e c^2 = 8.187173e-14 J",
    "inputs": "m_e = 9.109e-31 kg, c = 2.998e8 m/s",
    "formula": "m_e * c^2"
  },
  {
    "id": "Q2",
    "statement": "ZBW angular frequency omega_inf = 1.552071e21 rad/s",
    "inputs": "m_e = 9.109e-31 kg, c = 2.998e8 m/s, hbar = 1.055e-34 J s",
    "formula": "omega_inf = 2*m_e*c^2/hbar"
  },
  {
    "id": "Q3",
    "statement": "Cyclic frequency f_inf = 2.470197e20 Hz",
    "inputs": "omega_inf = 1.552071e21 rad/s",
    "formula": "f_inf = omega_inf/(2*pi)"
  },
  {
    "id": "Q4",
    "statement": "Compton wavelength lambda_C = 3.863226e-13 m",
    "inputs": "hbar = 1.055e-34 J s, m_e = 9.109e-31 kg, c = 2.998e8 m/s",
    "formula": "lambda_C = hbar/(m_e*c)"
  },
  {
    "id": "Q5",
    "statement": "Planck length l_P = 1.616486e-35 m",
    "inputs": "hbar = 1.055e-34 J s, G = 6.674e-11 m^3 kg^-1 s^-2, c = 2.998e8 m/s",
    "formula": "l_P = sqrt(hbar*G/c^3)"
  },
  {
    "id": "Q6",
    "statement": "Product formula holds for x=6: 6*0.5*(1/3)=1",
    "inputs": "x = 6",
    "formula": "|x|_inf * prod_p |x|_p"
  },
  {
    "id": "Q7",
    "statement": "Product formula holds for x=12: 12*0.25*(1/3)=1",
    "inputs": "x = 12",
    "formula": "|x|_inf * prod_p |x|_p"
  },
  {
    "id": "Q8",
    "statement": "Product formula holds for x=10: 10*0.5*0.2=1",
    "inputs": "x = 10",
    "formula": "|x|_inf * prod_p |x|_p"
  }
]

## Script
```python
import math

def check(cid, computed, expected):
    if expected is None:
        print(f"CLAIM {cid}: computed={computed:.6e} expected=None match=no")
        return False
    ok = math.isclose(computed, expected, rel_tol=1e-6)
    print(f"CLAIM {cid}: computed={computed:.6e} expected={expected:.6e} match={'yes' if ok else 'no'}")
    return ok

results = []

# Q1: m_e c^2
m_e = 9.109e-31
c = 2.998e8
E = m_e * c**2
results.append(check("Q1", E, 8.187173e-14))

# Q2: omega_inf = 2 m_e c^2 / hbar
hbar = 1.055e-34
omega = 2 * m_e * c**2 / hbar
results.append(check("Q2", omega, 1.552071e21))

# Q3: f_inf = omega / (2 pi)
f = omega / (2 * math.pi)
results.append(check("Q3", f, 2.470197e20))

# Q4: lambda_C = hbar / (m_e c)
lam = hbar / (m_e * c)
results.append(check("Q4", lam, 3.863226e-13))

# Q5: l_P = sqrt(hbar G / c^3)
G = 6.674e-11
lP = math.sqrt(hbar * G / c**3)
results.append(check("Q5", lP, 1.616486e-35))

# Q6: product formula for x = 6
x = 6
val6 = abs(x) * (0.5) * (1/3)
results.append(check("Q6", val6, 1.0))

# Q7: product formula for x = 12
x = 12
val12 = abs(x) * (0.25) * (1/3)
results.append(check("Q7", val12, 1.0))

# Q8: product formula for x = 10
x = 10
val10 = abs(x) * (0.5) * (0.2)
results.append(check("Q8", val10, 1.0))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=8.187173e-14 expected=8.187173e-14 match=yes
CLAIM Q2: computed=1.552071e+21 expected=1.552071e+21 match=yes
CLAIM Q3: computed=2.470197e+20 expected=2.470197e+20 match=yes
CLAIM Q4: computed=3.863226e-13 expected=3.863226e-13 match=yes
CLAIM Q5: computed=1.616486e-35 expected=1.616486e-35 match=yes
CLAIM Q6: computed=1.000000e+00 expected=1.000000e+00 match=yes
CLAIM Q7: computed=1.000000e+00 expected=1.000000e+00 match=yes
CLAIM Q8: computed=1.000000e+00 expected=1.000000e+00 match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
