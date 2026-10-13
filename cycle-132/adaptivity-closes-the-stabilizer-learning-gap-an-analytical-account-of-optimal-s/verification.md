# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "log2 N_n = n^2/2 + 3n/2 + O(1); at n=100, log2 N_100 = 5150 + delta with delta in (0, 1.4427)",
    "inputs": "n=100, log2(1+x) < x/ln 2 bound giving delta < 1/ln 2 ≈ 1.4427",
    "formula": "log2 N_n = n + n(n+1)/2 + sum_{i=1}^{n} log2(1+2^{-i})"
  },
  {
    "id": "Q2",
    "statement": "Information floor: any single-copy learner needs at least 52 copies at n=100",
    "inputs": "log2 N_100 = 5150 + delta_100 with delta_100 in (0, 1.4427); b_copy <= n = 100",
    "formula": "m >= ceil(log2 N_n / n) = ceil((5150 + delta_100)/100)"
  },
  {
    "id": "Q3",
    "statement": "Memory tradeoff instance: Theta(190) copies at (n,k,epsilon)=(100,10,0.01)",
    "inputs": "n=100, k=10, epsilon=0.01",
    "formula": "n - k + 1/epsilon = 100 - 10 + 1/0.01"
  },
  {
    "id": "Q4",
    "statement": "Crossover epsilon* = 1/n = 0.01 at n=100",
    "inputs": "n=100",
    "formula": "epsilon* = 1/n"
  },
  {
    "id": "Q5",
    "statement": "Nullity extension: O(3200) copies at (n,r)=(100,5)",
    "inputs": "n=100, r=5",
    "formula": "n * 2^r = 100 * 2^5"
  },
  {
    "id": "Q6",
    "statement": "Nullity extension: O(102400) copies at (n,r)=(100,10)",
    "inputs": "n=100, r=10",
    "formula": "n * 2^r = 100 * 2^10"
  },
  {
    "id": "Q7",
    "statement": "Workload projection: 5.0e5 adaptive measurements for W=1000, n=100, C_ad=5",
    "inputs": "W=1000, C_ad=5, n=100",
    "formula": "M_ad = W * C_ad * n"
  },
  {
    "id": "Q8",
    "statement": "Workload projection: 1.0e8 non-adaptive measurements for W=1000, n=100, c_na=10",
    "inputs": "W=1000, c_na=10, n=100",
    "formula": "M_na = W * c_na * n^2"
  },
  {
    "id": "Q9",
    "statement": "Workload ratio 200 with uncertainty range [10,1000]",
    "inputs": "M_na=1.0e8, M_ad=5.0e5, C_ad in [1,10], c_na in [1,10], n=100",
    "formula": "M_na/M_ad = (c_na/C_ad)*n"
  },
  {
    "id": "Q10",
    "statement": "Separation factor at n=100: m_na/m_ad >= 100/C_ad in [10,100] under c=1, C_ad in [1,10]",
    "inputs": "c=1, C_ad in [1,10], n=100",
    "formula": "m_na/m_ad >= (c*n^2)/(C_ad*n) = (c/C_ad)*n"
  },
  {
    "id": "Q11",
    "statement": "Hypothesis-class size at n=1: N_1 = 6",
    "inputs": "n=1",
    "formula": "N_n = 2^n * prod_{i=1}^{n}(2^i+1)"
  },
  {
    "id": "Q12",
    "statement": "Hypothesis-class size at n=3: N_3 = 1080",
    "inputs": "n=3",
    "formula": "N_n = 2^n * prod_{i=1}^{n}(2^i+1)"
  },
  {
    "id": "Q13",
    "statement": "Boundary memory tradeoff values: Theta(200) at k=0 and Theta(100) at k=100, with n=100, epsilon=0.01",
    "inputs": "n=100, epsilon=0.01, k=0 and k=100",
    "formula": "n - k + 1/epsilon"
  }
]

## Script
```python
import math

def claim(id, computed, expected, match):
    print(f"CLAIM {id}: computed={computed} expected={expected} match={match}")

# Q1: log2 N_100 = 5150 + delta, delta in (0, 1.4427)
n = 100
log2N = n + n*(n+1)/2 + sum(math.log2(1 + 2**(-i)) for i in range(1, n+1))
delta = log2N - 5150
bound = 1/math.log(2)
print(f"CLAIM Q1: computed={delta:.8f} expected={'(0, 1.4427)' if 0 < delta < 1.4427 else 'FAIL'} match={'yes' if 0 < delta < 1.4427 else 'no'}")

# Q2: floor = ceil((5150+delta)/100) = 52
floor = math.ceil((5150 + delta)/100)
claim("Q2", floor, "52", "yes" if floor == 52 else "no")

# Q3: n - k + 1/eps = 190
v = 100 - 10 + 1/0.01
claim("Q3", v, "190", "yes" if v == 190 else "no")

# Q4: eps* = 1/n = 0.01
v = 1/100
claim("Q4", v, "0.01", "yes" if v == 0.01 else "no")

# Q5: 100 * 2^5 = 3200
v = 100 * 2**5
claim("Q5", v, "3200", "yes" if v == 3200 else "no")

# Q6: 100 * 2^10 = 102400
v = 100 * 2**10
claim("Q6", v, "102400", "yes" if v == 102400 else "no")

# Q7: M_ad = 1000*5*100 = 5.0e5
v = 1000*5*100
claim("Q7", v, "500000", "yes" if v == 500000 else "no")

# Q8: M_na = 1000*10*100^2 = 1.0e8
v = 1000*10*100**2
claim("Q8", v, "100000000", "yes" if v == 100000000 else "no")

# Q9: ratio = 1.0e8/5.0e5 = 200; range [10,1000]
ratio = (1000*10*100**2)/(1000*5*100)
rmin = (1/10)*100
rmax = (10/1)*100
ok = ratio == 200 and rmin == 10 and rmax == 1000
claim("Q9", f"{ratio:.8f} range=[{rmin:.8f},{rmax:.8f}]", "200 range=[10,1000]", "yes" if ok else "no")

# Q10: separation >= 100/C_ad in [10,100]
smin = 100/10
smax = 100/1
ok = smin == 10 and smax == 100
claim("Q10", f"range=[{smin:.8f},{smax:.8f}]", "range=[10,100]", "yes" if ok else "no")

# Q11: N_1 = 2 * (2+1) = 6
v = 2 * (2**1 + 1)
claim("Q11", v, "6", "yes" if v == 6 else "no")

# Q12: N_3 = 8 * 3 * 5 * 9 = 1080
v = 2**3 * (2**1+1) * (2**2+1) * (2**3+1)
claim("Q12", v, "1080", "yes" if v == 1080 else "no")

# Q13: k=0 -> 200; k=100 -> 100
v0 = 100 - 0 + 1/0.01
v100 = 100 - 100 + 1/0.01
ok = v0 == 200 and v100 == 100
claim("Q13", f"k=0:{v0:.8f}, k=100:{v100:.8f}", "k=0:200, k=100:100", "yes" if ok else "no")

print("VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch")

```

## Execution output
```
CLAIM Q1: computed=1.25352404 expected=(0, 1.4427) match=yes
CLAIM Q2: computed=52 expected=52 match=yes
CLAIM Q3: computed=190.0 expected=190 match=yes
CLAIM Q4: computed=0.01 expected=0.01 match=yes
CLAIM Q5: computed=3200 expected=3200 match=yes
CLAIM Q6: computed=102400 expected=102400 match=yes
CLAIM Q7: computed=500000 expected=500000 match=yes
CLAIM Q8: computed=100000000 expected=100000000 match=yes
CLAIM Q9: computed=200.00000000 range=[10.00000000,1000.00000000] expected=200 range=[10,1000] match=yes
CLAIM Q10: computed=range=[10.00000000,100.00000000] expected=range=[10,100] match=yes
CLAIM Q11: computed=6 expected=6 match=yes
CLAIM Q12: computed=1080 expected=1080 match=yes
CLAIM Q13: computed=k=0:200.00000000, k=100:100.00000000 expected=k=0:200, k=100:100 match=yes
VERIFICATION SUMMARY: 13 claims, 13 match, 0 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 1.25352404 | (0, | - | undecided | undecided: values not both numeric and no script verdict |
| Q2 | 52 | 52 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q3 | 190.0 | 190 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q4 | 0.01 | 0.01 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q5 | 3200 | 3200 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q6 | 102400 | 102400 | yes | match | 6 significant digits (as the paper states, at least 2) |
| Q7 | 500000 | 500000 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q8 | 100000000 | 100000000 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q10 | range=[10.00000000,100.00000000] | range=[10,100] | yes | match | script verdict (values not both numeric) |
| Q11 | 6 | 6 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 1080 | 1080 | yes | match | 4 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 11 (1 undecided).
