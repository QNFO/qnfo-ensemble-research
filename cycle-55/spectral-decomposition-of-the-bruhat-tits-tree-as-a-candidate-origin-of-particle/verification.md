# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Ball size for p=2: B_2(n) = 3*2^n - 2",
    "inputs": "p=2, formula B_p(n)=1+(p+1)(p^n-1)/(p-1)",
    "formula": "1 + (p+1)*(p^n - 1)/(p - 1)"
  },
  {
    "id": "Q2",
    "statement": "Ball size for p=3: B_3(n) = 2*3^n - 1",
    "inputs": "p=3, formula B_p(n)=1+(p+1)(p^n-1)/(p-1)",
    "formula": "1 + (p+1)*(p^n - 1)/(p - 1)"
  },
  {
    "id": "Q3",
    "statement": "Adjacency spectral radius rho_p = 2*sqrt(p); rho_2 = 2.82842712, rho_3 = 3.46410162, rho_5 = 4.47213595",
    "inputs": "p in {2,3,5}",
    "formula": "2*sqrt(p)"
  },
  {
    "id": "Q4",
    "statement": "Cross-prime spectral radius ratios: rho_3/rho_2 = 1.22474487, rho_5/rho_3 = 1.29099445, rho_5/rho_2 = 1.58113883",
    "inputs": "rho_p = 2*sqrt(p)",
    "formula": "rho(p2)/rho(p1)"
  },
  {
    "id": "Q5",
    "statement": "Laplacian continuous spectrum for p=2 is [0.17157288, 5.82842712]",
    "inputs": "p=2, p+1=3, 2*sqrt(2)=2.82842712",
    "formula": "(p+1) - 2*sqrt(p), (p+1) + 2*sqrt(p)"
  },
  {
    "id": "Q6",
    "statement": "Laplacian continuous spectrum for p=5 is [1.52786405, 10.47213595]",
    "inputs": "p=5, p+1=6, 2*sqrt(5)=4.47213595",
    "formula": "(p+1) - 2*sqrt(p), (p+1) + 2*sqrt(p)"
  },
  {
    "id": "Q7",
    "statement": "Finite radial quotient eigenvalues for p=5: lambda_0 = 4.47213595, lambda_1 = sqrt(5) = 2.23606798, lambda_2 = -2.23606798, lambda_3 = -4.47213595",
    "inputs": "p=5, 2*sqrt(5)=4.47213595, angles 2*pi*k/6",
    "formula": "2*sqrt(p)*cos(2*pi*k/(p+1))"
  },
  {
    "id": "Q8",
    "statement": "Finite radial quotient eigenvalues for p=2: lambda_0 = 2.82842712, lambda_1 = lambda_2 = -1.41421356",
    "inputs": "p=2, 2*sqrt(2)=2.82842712, angles 2*pi*k/3",
    "formula": "2*sqrt(p)*cos(2*pi*k/(p+1))"
  }
]

## Script
```python
import math

def close(a, b):
    return math.isclose(a, b, rel_tol=1e-6)

results = []

# Q1: B_2(n) = 3*2^n - 2, check n=1,2
b2 = lambda n: 1 + (2+1)*(2**n - 1)//(2-1)
computed = [b2(1), b2(2)]
expected = [3*2**1 - 2, 3*2**2 - 2]
match = all(close(c, e) for c, e in zip(computed, expected))
results.append(("Q1", computed, expected, match))

# Q2: B_3(n) = 2*3^n - 1, check n=1,2
b3 = lambda n: 1 + (3+1)*(3**n - 1)/(3-1)
computed = [b3(1), b3(2)]
expected = [2*3**1 - 1, 2*3**2 - 1]
match = all(close(c, e) for c, e in zip(computed, expected))
results.append(("Q2", computed, expected, match))

# Q3: rho_p = 2*sqrt(p)
rho = lambda p: 2*math.sqrt(p)
computed = [rho(2), rho(3), rho(5)]
expected = [2.82842712, 3.46410162, 4.47213595]
match = all(close(c, e) for c, e in zip(computed, expected))
results.append(("Q3", computed, expected, match))

# Q4: cross-prime ratios
computed = [rho(3)/rho(2), rho(5)/rho(3), rho(5)/rho(2)]
expected = [1.22474487, 1.29099445, 1.58113883]
match = all(close(c, e) for c, e in zip(computed, expected))
results.append(("Q4", computed, expected, match))

# Q5: Laplacian continuous spectrum p=2
lo = 3 - 2*math.sqrt(2); hi = 3 + 2*math.sqrt(2)
match = close(lo, 0.17157288) and close(hi, 5.82842712)
results.append(("Q5", [lo, hi], [0.17157288, 5.82842712], match))

# Q6: Laplacian continuous spectrum p=5
lo = 6 - 2*math.sqrt(5); hi = 6 + 2*math.sqrt(5)
match = close(lo, 1.52786405) and close(hi, 10.47213595)
results.append(("Q6", [lo, hi], [1.52786405, 10.47213595], match))

# Q7: finite radial quotient eigenvalues p=5
lam = lambda p, k: 2*math.sqrt(p)*math.cos(2*math.pi*k/(p+1))
computed = [lam(5, k) for k in range(4)]
expected = [4.47213595, 2.23606798, -2.23606798, -4.47213595]
match = all(close(c, e) for c, e in zip(computed, expected))
results.append(("Q7", computed, expected, match))

# Q8: finite radial quotient eigenvalues p=2
computed = [lam(2, k) for k in range(3)]
expected = [2.82842712, -1.41421356, -1.41421356]
match = all(close(c, e) for c, e in zip(computed, expected))
results.append(("Q8", computed, expected, match))

n_match = 0
for qid, comp, exp, match in results:
    print(f"CLAIM {qid}: computed={comp} expected={exp} match={'yes' if match else 'no'}")
    if match:
        n_match += 1
print(f"VERIFICATION SUMMARY: {len(results)} claims, {n_match} match, {len(results)-n_match} mismatch")

```

## Execution output
```
CLAIM Q1: computed=[4, 10] expected=[4, 10] match=yes
CLAIM Q2: computed=[5.0, 17.0] expected=[5, 17] match=yes
CLAIM Q3: computed=[2.8284271247461903, 3.4641016151377544, 4.47213595499958] expected=[2.82842712, 3.46410162, 4.47213595] match=yes
CLAIM Q4: computed=[1.224744871391589, 1.2909944487358058, 1.5811388300841895] expected=[1.22474487, 1.29099445, 1.58113883] match=yes
CLAIM Q5: computed=[0.1715728752538097, 5.82842712474619] expected=[0.17157288, 5.82842712] match=yes
CLAIM Q6: computed=[1.5278640450004204, 10.47213595499958] expected=[1.52786405, 10.47213595] match=yes
CLAIM Q7: computed=[4.47213595499958, 2.2360679774997902, -2.236067977499789, -4.47213595499958] expected=[4.47213595, 2.23606798, -2.23606798, -4.47213595] match=yes
CLAIM Q8: computed=[2.8284271247461903, -1.4142135623730945, -1.4142135623730965] expected=[2.82842712, -1.41421356, -1.41421356] match=yes
VERIFICATION SUMMARY: 8 claims, 8 match, 0 mismatch

[exit 0]
```
