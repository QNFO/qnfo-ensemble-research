# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "For p=3 and t=1 the code size n_t equals 5.",
    "inputs": "p=3, t=1",
    "formula": "n = 1 + ((p+1)*(p^t - 1))/(p-1)"
  },
  {
    "id": "Q2",
    "statement": "The conditional distance for t=1 is d = 3.",
    "inputs": "t=1",
    "formula": "d = 2*t + 1"
  },
  {
    "id": "Q3",
    "statement": "The passive logical failure probability for p=3, t=1, ε=10^{-3} is approximately 9.98×10^{-6}.",
    "inputs": "n=5, t=1, ε=10^{-3}",
    "formula": "P = sum_{k=t+1}^{n} C(n,k) * ε^k * (1-ε)^{n-k}"
  },
  {
    "id": "Q4",
    "statement": "The logical error suppression factor for the same parameters is approximately 100.2.",
    "inputs": "ε=10^{-3}, P=9.98×10^{-6}",
    "formula": "S = ε / P"
  },
  {
    "id": "Q5",
    "statement": "For p=3 and t=2 the code size n_t equals 17.",
    "inputs": "p=3, t=2",
    "formula": "n = 1 + ((p+1)*(p^t - 1))/(p-1)"
  },
  {
    "id": "Q6",
    "statement": "The passive logical failure probability for p=3, t=2, ε=10^{-3} is approximately 6.73×10^{-7}.",
    "inputs": "n=17, t=2, ε=10^{-3}",
    "formula": "P = sum_{k=t+1}^{n} C(n,k) * ε^k * (1-ε)^{n-k}"
  },
  {
    "id": "Q7",
    "statement": "The decoder depth for n=5 is approximately log_4 5 ≈ 1.16, requiring at most two parallel steps.",
    "inputs": "n=5, base=4",
    "formula": "L = log_{base}(n)"
  },
  {
    "id": "Q8",
    "statement": "The decoder depth for n=17 is approximately log_4 17 ≈ 2.04, requiring at most three parallel steps.",
    "inputs": "n=17, base=4",
    "formula": "L = log_{base}(n)"
  }
]

## Script
```python
import math

def fmt(x):
    # format with at least 8 significant digits
    return f"{x:.8g}"

# Q1: code size for p=3, t=1
p = 3
t = 1
n = 1 + ((p + 1) * (p**t - 1)) / (p - 1)
print(f"CLAIM Q1: computed={fmt(n)} expected=5 match={'yes' if abs(n - 5) < 1e-12 else 'no'}")

# Q2: conditional distance for t=1
d = 2 * t + 1
print(f"CLAIM Q2: computed={fmt(d)} expected=3 match={'yes' if d == 3 else 'no'}")

# Q3: passive logical failure probability for p=3, t=1, ε=10⁻³
n = 5
eps = 1e-3
P = 0.0
for k in range(t + 1, n + 1):
    P += math.comb(n, k) * (eps**k) * ((1 - eps)**(n - k))
print(f"CLAIM Q3: computed={fmt(P)} expected=9.98×10^{-6} match={'yes' if abs(P - 9.98e-6) / 9.98e-6 < 1e-3 else 'no'}")

# Q4: logical error suppression factor
S = eps / P
print(f"CLAIM Q4: computed={fmt(S)} expected=100.2 match={'yes' if abs(S - 100.2) / 100.2 < 1e-3 else 'no'}")

# Q5: code size for p=3, t=2
t = 2
n2 = 1 + ((p + 1) * (p**t - 1)) / (p - 1)
print(f"CLAIM Q5: computed={fmt(n2)} expected=17 match={'yes' if n2 == 17 else 'no'}")

# Q6: passive logical failure probability for p=3, t=2, ε=10⁻³
n = int(n2)
P2 = 0.0
for k in range(t + 1, n + 1):
    P2 += math.comb(n, k) * (eps**k) * ((1 - eps)**(n - k))
print(f"CLAIM Q6: computed={fmt(P2)} expected=6.73×10^{-7} match={'yes' if abs(P2 - 6.73e-7) / 6.73e-7 < 1e-2 else 'no'}")

# Q7: decoder depth for n=5 (log_4 5)
L = math.log(5, 4)
print(f"CLAIM Q7: computed={fmt(L)} expected=1.16 match={'yes' if abs(L - 1.16) / 1.16 < 1e-2 else 'no'}")

# Q8: decoder depth for n=17 (log_4 17)
L2 = math.log(17, 4)
print(f"CLAIM Q8: computed={fmt(L2)} expected=2.04 match={'yes' if abs(L2 - 2.04) / 2.04 < 1e-2 else 'no'}")

```

## Execution output
```
CLAIM Q1: computed=5 expected=5 match=yes
CLAIM Q2: computed=3 expected=3 match=yes
CLAIM Q3: computed=9.980015e-06 expected=9.98×10^-6 match=yes
CLAIM Q4: computed=100.20025 expected=100.2 match=yes
CLAIM Q5: computed=17 expected=17 match=yes
CLAIM Q6: computed=6.72897e-07 expected=6.73×10^-7 match=yes
CLAIM Q7: computed=1.160964 expected=1.16 match=yes
CLAIM Q8: computed=2.0437314 expected=2.04 match=yes

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 5 | 5 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q2 | 3 | 3 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 9.980015e-06 | 9.98×10^-6 | yes | match | script verdict (values not both numeric) |
| Q4 | 100.20025 | 100.2 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q5 | 17 | 17 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 6.72897e-07 | 6.73×10^-7 | yes | match | script verdict (values not both numeric) |
| Q7 | 1.160964 | 1.16 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q8 | 2.0437314 | 2.04 | yes | match | 3 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 8.
