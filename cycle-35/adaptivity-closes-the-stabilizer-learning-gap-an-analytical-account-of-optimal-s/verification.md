# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Number of n-qubit stabilizer states satisfies log2 N_n = n^2/2 + O(n); at n=100, N_100 ≈ 2^5000.",
    "inputs": "n=100",
    "formula": "log2 N_n = n^2/2 + O(n); log2 N_100 = 100^2/2 = 5000"
  },
  {
    "id": "Q2",
    "statement": "Information-theoretic floor on copies: m_floor(n) >= log2 N_n / b_copy.",
    "inputs": "log2 N_100=5000, b_copy(ad)=n=100",
    "formula": "m_floor(100) >= 5000/100 = 50"
  },
  {
    "id": "Q3",
    "statement": "Non-adaptive lower bound at n=100: m_na_tight(100) = c * 100^2 = 10^4 c copies; >= 10^4 under assumption c >= 1; range [10^3, 10^5] if c in [0.1,10].",
    "inputs": "n=100, c in [0.1,10]",
    "formula": "m_na_tight(100) = c * 100^2 = 10^4 * c"
  },
  {
    "id": "Q4",
    "statement": "Separation factor at n=100: m_na_tight(100)/m_ad(100) >= 100c/C, roughly 10–1000x under c in [0.1,10], C in [1,10].",
    "inputs": "m_na_tight(100)=10^4 c, m_ad(100)=C*100",
    "formula": "ratio >= (10^4 c)/(C*100) = 100c/C"
  },
  {
    "id": "Q5",
    "statement": "Tolerant testing cost m_test(n,k,eps) = Theta(n - k + 1/eps); at n=100, k=10, eps=0.01 gives Theta(190).",
    "inputs": "n=100, k=10, eps=0.01",
    "formula": "n - k + 1/eps = 100 - 10 + 100 = 190"
  },
  {
    "id": "Q6",
    "statement": "With k=0 memory, testing cost is Theta(200); with k=100, Theta(1/eps)=Theta(100).",
    "inputs": "n=100, eps=0.01, k=0 or k=100",
    "formula": "n - k + 1/eps: 100-0+100=200; 100-100+100=100"
  },
  {
    "id": "Q7",
    "statement": "Crossover infidelity where memory term and eps term balance: eps* = 1/n = 0.01 for n=100.",
    "inputs": "n=100",
    "formula": "eps* = 1/n = 1/100 = 0.01"
  },
  {
    "id": "Q8",
    "statement": "Nullity-r states learnable with O(n*2^r) measurements: O(3200) at (n,r)=(100,5); O(102400) at (100,10).",
    "inputs": "n=100, r=5 and r=10",
    "formula": "n * 2^r = 100*32 = 3200; 100*1024 = 102400"
  }
]

## Script
```python
import math

def check(id, computed, expected):
    if expected is None:
        match = "no"
    elif isinstance(computed, float) or isinstance(expected, float):
        match = "yes" if math.isclose(float(computed), float(expected), rel_tol=1e-6) else "no"
    else:
        match = "yes" if computed == expected else "no"
    print(f"CLAIM {id}: computed={computed} expected={expected} match={match}")
    return match == "yes"

results = []

# Q1: log2 N_n = n^2/2 + O(n); at n=100, log2 N_100 = 5000
n = 100
log2N = n**2 / 2
results.append(check("Q1", log2N, 5000))

# Q2: m_floor(100) >= log2 N_100 / b_copy = 5000/100 = 50
b_copy = n
m_floor = log2N / b_copy
results.append(check("Q2", m_floor, 50))

# Q3: m_na_tight(100) = c * 100^2; with c=1 -> 10^4
c = 1.0
m_na = c * n**2
results.append(check("Q3", m_na, 1e4))

# Q4: ratio >= (10^4 c)/(C*100) = 100c/C; with c=1, C=1 -> 100
C = 1.0
ratio = (c * n**2) / (C * n)
results.append(check("Q4", ratio, 100))

# Q5: m_test = n - k + 1/eps = 100 - 10 + 100 = 190
k = 10
eps = 0.01
m_test = n - k + 1/eps
results.append(check("Q5", m_test, 190))

# Q6: k=0 -> 200; k=100 -> 100
m_test_k0 = n - 0 + 1/eps
m_test_k100 = n - 100 + 1/eps
results.append(check("Q6a", m_test_k0, 200))
results.append(check("Q6b", m_test_k100, 100))

# Q7: eps* = 1/n = 0.01
eps_star = 1/n
results.append(check("Q7", eps_star, 0.01))

# Q8: n * 2^r: r=5 -> 3200; r=10 -> 102400
r5 = n * 2**5
r10 = n * 2**10
results.append(check("Q8a", r5, 3200))
results.append(check("Q8b", r10, 102400))

N = len(results)
M = sum(results)
K = N - M
print(f"VERIFICATION SUMMARY: {N} claims, {M} match, {K} mismatch")

```

## Execution output
```
CLAIM Q1: computed=5000.0 expected=5000 match=yes
CLAIM Q2: computed=50.0 expected=50 match=yes
CLAIM Q3: computed=10000.0 expected=10000.0 match=yes
CLAIM Q4: computed=100.0 expected=100 match=yes
CLAIM Q5: computed=190.0 expected=190 match=yes
CLAIM Q6a: computed=200.0 expected=200 match=yes
CLAIM Q6b: computed=100.0 expected=100 match=yes
CLAIM Q7: computed=0.01 expected=0.01 match=yes
CLAIM Q8a: computed=3200 expected=3200 match=yes
CLAIM Q8b: computed=102400 expected=102400 match=yes
VERIFICATION SUMMARY: 10 claims, 10 match, 0 mismatch

[exit 0]
```
