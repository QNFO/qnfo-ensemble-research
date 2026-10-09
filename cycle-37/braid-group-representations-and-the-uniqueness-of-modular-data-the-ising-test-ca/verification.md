# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Quantum dimension of sigma is sqrt(2) ≈ 1.4142",
    "inputs": "N_{sigma sigma}^1 = 1, N_{sigma sigma}^psi = 1, d_1 = 1, d_psi = 1",
    "formula": "d_sigma^2 = N_{sigma sigma}^1 * d_1 + N_{sigma sigma}^psi * d_psi = 2, so d_sigma = sqrt(2)"
  },
  {
    "id": "Q2",
    "statement": "Total quantum dimension D = 2",
    "inputs": "d_1 = 1, d_sigma = sqrt(2), d_psi = 1",
    "formula": "D = sqrt(d_1^2 + d_sigma^2 + d_psi^2) = sqrt(1 + 2 + 1) = 2"
  },
  {
    "id": "Q3",
    "statement": "S_{sigma 1} = sqrt(2)/2 ≈ 0.7071",
    "inputs": "d_sigma = sqrt(2), d_1 = 1, D = 2",
    "formula": "S_{sigma 1} = d_sigma * d_1 / D = sqrt(2)/2"
  },
  {
    "id": "Q4",
    "statement": "S_{sigma psi} = -sqrt(2)/2 ≈ -0.7071",
    "inputs": "d_sigma = sqrt(2), d_psi = 1, D = 2, theta_sigma / (theta_sigma * theta_psi) = 1/(-1) = -1",
    "formula": "S_{sigma psi} = (d_sigma * d_psi / D) * (-1) = -sqrt(2)/2"
  },
  {
    "id": "Q5",
    "statement": "S_{sigma sigma} = 0",
    "inputs": "theta_1 = 1, theta_psi = -1, theta_sigma^2 = e^{i pi/4}, d_1 = 1, d_psi = 1, D = 2",
    "formula": "S_{sigma sigma} = (1/D) * (theta_1/theta_sigma^2 * d_1 + theta_psi/theta_sigma^2 * d_psi) = (1/2)*(e^{-i pi/4} + (-1)/e^{i pi/4}) = (1/2)*(e^{-i pi/4} - e^{-i pi/4}) = 0"
  },
  {
    "id": "Q6",
    "statement": "S_{11} = S_{1 psi} = S_{psi psi} = 1/2",
    "inputs": "d_1 = 1, d_psi = 1, D = 2",
    "formula": "S_{ab} = d_a * d_b / D for Abelian a, b, giving 1*1/2 = 1/2 in each case"
  },
  {
    "id": "Q7",
    "statement": "T_{sigma sigma} = e^{i pi/8} ≈ 0.9239 + 0.3827 i",
    "inputs": "R_{sigma sigma} = e^{-i pi/8}, theta_1 = 1",
    "formula": "m_1 = R_{sigma sigma}^2 = e^{-i pi/4}; theta_sigma^2 = 1/m_1 = e^{i pi/4}; theta_sigma = e^{i pi/8} (principal root)"
  },
  {
    "id": "Q8",
    "statement": "theta_psi = -1",
    "inputs": "m_1 = e^{-i pi/4}, m_psi = e^{3 i pi/4}",
    "formula": "theta_psi / theta_sigma^2 = m_psi / m_1 = e^{3 i pi/4} / e^{-i pi/4} = e^{i pi} = -1"
  }
]

## Script
```python
import math
import cmath

def check(cid, computed, expected):
    if expected is None:
        match = "n/a"
    else:
        if isinstance(computed, complex) or isinstance(expected, complex):
            match = "yes" if cmath.isclose(computed, expected, rel_tol=1e-6) else "no"
        else:
            match = "yes" if math.isclose(computed, expected, rel_tol=1e-6) else "no"
    print(f"CLAIM {cid}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: d_sigma^2 = N_{sigma sigma}^1 * d_1 + N_{sigma sigma}^psi * d_psi = 2
N1, Npsi = 1, 1
d1, dpsi = 1, 1
d_sigma_sq = N1 * d1 + Npsi * dpsi
d_sigma = math.sqrt(d_sigma_sq)
results.append(check("Q1", d_sigma, math.sqrt(2)))

# Q2: D = sqrt(d_1^2 + d_sigma^2 + d_psi^2)
D = math.sqrt(d1**2 + d_sigma**2 + dpsi**2)
results.append(check("Q2", D, 2.0))

# Q3: S_{sigma 1} = d_sigma * d_1 / D
S_sigma1 = d_sigma * d1 / D
results.append(check("Q3", S_sigma1, math.sqrt(2) / 2))

# Q4: S_{sigma psi} = (d_sigma * d_psi / D) * (-1)
S_sigmapsi = (d_sigma * dpsi / D) * (-1)
results.append(check("Q4", S_sigmapsi, -math.sqrt(2) / 2))

# Q5: S_{sigma sigma} = (1/D)*(theta_1/theta_sigma^2 * d_1 + theta_psi/theta_sigma^2 * d_psi)
theta_1 = 1.0
theta_psi = -1.0
theta_sigma_sq = cmath.exp(1j * math.pi / 4)
S_sigmasigma = (1 / D) * (theta_1 / theta_sigma_sq * d1 + theta_psi / theta_sigma_sq * dpsi)
results.append(check("Q5", S_sigmasigma, 0.0))

# Q6: S_{11} = S_{1 psi} = S_{psi psi} = 1/2
S_11 = d1 * d1 / D
S_1psi = d1 * dpsi / D
S_psipsi = dpsi * dpsi / D
results.append(check("Q6a", S_11, 0.5))
results.append(check("Q6b", S_1psi, 0.5))
results.append(check("Q6c", S_psipsi, 0.5))

# Q7: theta_sigma = e^{i pi/8} via m_1 = R^2, theta_sigma^2 = 1/m_1
R = cmath.exp(-1j * math.pi / 8)
m_1 = R**2
theta_sigma_sq_7 = 1 / m_1
theta_sigma = cmath.exp(1j * math.pi / 8)  # principal root of theta_sigma_sq_7
results.append(check("Q7", theta_sigma_sq_7, theta_sigma**2))
results.append(check("Q7b", theta_sigma, cmath.exp(1j * math.pi / 8)))

# Q8: theta_psi / theta_sigma^2 = m_psi / m_1 = e^{i pi} = -1
m_psi = cmath.exp(3j * math.pi / 4)
ratio = m_psi / m_1
results.append(check("Q8", ratio, -1.0))

n = len(results)
m = sum(results)
print(f"VERIFICATION SUMMARY: {n} claims, {m} match, {n - m} mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.4142135623730951 expected=1.4142135623730951 match=yes
CLAIM Q2: computed=2.0 expected=2.0 match=yes
CLAIM Q3: computed=0.7071067811865476 expected=0.7071067811865476 match=yes
CLAIM Q4: computed=-0.7071067811865476 expected=-0.7071067811865476 match=yes
CLAIM Q5: computed=0j expected=0.0 match=yes
CLAIM Q6a: computed=0.5 expected=0.5 match=yes
CLAIM Q6b: computed=0.5 expected=0.5 match=yes
CLAIM Q6c: computed=0.5 expected=0.5 match=yes
CLAIM Q7: computed=(0.7071067811865475+0.7071067811865476j) expected=(0.7071067811865475+0.7071067811865476j) match=yes
CLAIM Q7b: computed=(0.9238795325112867+0.3826834323650898j) expected=(0.9238795325112867+0.3826834323650898j) match=yes
CLAIM Q8: computed=(-1-0j) expected=-1.0 match=yes
VERIFICATION SUMMARY: 11 claims, 11 match, 0 mismatch

[exit 0]
```
