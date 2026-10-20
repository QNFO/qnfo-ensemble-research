# Verification report

## Extracted claims
[
  {
    "id": "Q1",
    "statement": "Unordered pairwise translation maps count is \\(\\binom{29}{2}=406\\).",
    "inputs": "Number of schisms N=29",
    "formula": "C(N,2)=N*(N-1)/2"
  },
  {
    "id": "Q2",
    "statement": "Unordered composition constraints count is \\(\\binom{29}{3}=3654\\).",
    "inputs": "Number of schisms N=29",
    "formula": "C(N,3)=N*(N-1)*(N-2)/6"
  },
  {
    "id": "Q3",
    "statement": "Constraint‑to‑map ratio is exactly 9.0.",
    "inputs": "Counts from Q1 and Q2",
    "formula": "(3654)/(406)=9.0"
  },
  {
    "id": "Q4",
    "statement": "For a candidate family of size n=7, unordered pairs are \\(\\binom{7}{2}=21\\).",
    "inputs": "Family size n=7",
    "formula": "C(n,2)=n*(n-1)/2"
  },
  {
    "id": "Q5",
    "statement": "At least 8 schisms remain unassigned under the one‑schism‑per‑pair assumption (29‑21=8).",
    "inputs": "Total schisms N=29, pairs P=21",
    "formula": "N - P"
  },
  {
    "id": "Q6",
    "statement": "For the Feynman–Shor bifurcation with m=2 ontologies, there are zero composition constraints (\\(\\binom{2}{3}=0\\)).",
    "inputs": "m=2",
    "formula": "C(m,3)=m*(m-1)*(m-2)/6"
  },
  {
    "id": "Q7",
    "statement": "Three‑framework closure bound is \\(\\Delta_{\\gamma}\\le3.4965\\times10^{-3}\\) for edge errors \\(10^{-3},2\\times10^{-3},5\\times10^{-4}\\).",
    "inputs": "ε1=1e-3, ε2=2e-3, ε3=5e-4",
    "formula": "1-(1-ε1)*(1-ε2)*(1-ε3)"
  },
  {
    "id": "Q8",
    "statement": "Chain‑length bound is \\(k\\le\\frac{\\ln(1-\\tau)}{\\ln(1-\\varepsilon_{\\min})}\\) with \\(\\tau=10^{-3}\\) and \\(\\varepsilon_{\\min}=10^{-2}\\), giving \\(k\\le0.0995\\).",
    "inputs": "τ=1e-3, ε_min=1e-2",
    "formula": "k <= ln(1-τ)/ln(1-ε_min)"
  },
  {
    "id": "Q9",
    "statement": "For a chain of four edges with \\(\\varepsilon_{\\min}=10^{-2}\\), the closure error is \\(\\Delta\\approx3.94\\times10^{-2}\\).",
    "inputs": "ε_min=1e-2, k=4",
    "formula": "Δ = 1-(1-ε_min)^k"
  },
  {
    "id": "Q10",
    "statement": "Genericity projection success probability is \\(P_{\\text{master}} = 0.9^{3654} \\approx 6.34\\times10^{-168}\\).",
    "inputs": "p=0.9, number of constraints m=3654",
    "formula": "P = p^m"
  },
  {
    "id": "Q11",
    "statement": "Requiring \\(P_{\\text{master}}\\ge0.01\\) yields the inequality \\(\\binom{n}{3}\\le43.71\\), giving maximal family size \\(n_{\\max}=7\\).",
    "inputs": "p=0.9, threshold 0.01",
    "formula": "binom(n,3) <= ln(0.01)/ln(p)"
  },
  {
    "id": "Q12",
    "statement": "Energy‑window factor from abstract is 2 (1 TeV / 0.5 TeV).",
    "inputs": "E_max=1 TeV, E_min=0.5 TeV",
    "formula": "E_max / E_min"
  },
  {
    "id": "Q13",
    "statement": "Energy‑window factor from preface is 3 (1.5 TeV / 0.5 TeV).",
    "inputs": "E_max=1.5 TeV, E_min=0.5 TeV",
    "formula": "E_max / E_min"
  },
  {
    "id": "Q14",
    "statement": "Mean schisms per domain under uniform assumption is \\(29/7 \\approx 4.14\\).",
    "inputs": "N=29, n=7",
    "formula": "N / n"
  },
  {
    "id": "Q15",
    "statement": "Mediated translation error for \\(\\varepsilon=10^{-2}\\) is \\(1-(1-\\varepsilon)^2 = 0.0199\\).",
    "inputs": "ε=1e-2",
    "formula": "1-(1-ε)^2"
  },
  {
    "id": "Q16",
    "statement": "Halving all edge errors (factor f=0.5) yields new closure bound \\(\\Delta'_{\\gamma}=1.7491\\times10^{-3}\\).",
    "inputs": "ε1=1e-3, ε2=2e-3, ε3=5e-4, f=0.5",
    "formula": "1-(1-f*ε1)*(1-f*ε2)*(1-f*ε3)"
  }
]

## Script
```python
import math

def fmt_scientific(val, sig):
    # format with given significant digits, strip unnecessary zeros and leading zeros in exponent
    s = f"{val:.{sig}e}"
    mantissa, exp = s.split('e')
    mantissa = mantissa.rstrip('0').rstrip('.')
    # remove leading zeros in exponent, e.g., -03 -> -3, +04 -> 4
    exp = exp.lstrip('+').lstrip('0')
    if exp.startswith('-') and exp[1:] == '':
        exp = '-0'
    return f"{mantissa}e{exp}"

def compare(comp, exp):
    return "yes" if comp == exp else "no"

results = []

# Q1
val = 29 * 28 // 2
exp = "406"
comp = str(val)
results.append(("Q1", comp, exp, compare(comp, exp)))

# Q2
val = 29 * 28 * 27 // 6
exp = "3654"
comp = str(val)
results.append(("Q2", comp, exp, compare(comp, exp)))

# Q3
val = 3654 / 406
exp = "9.0"
comp = f"{val:.1f}"
results.append(("Q3", comp, exp, compare(comp, exp)))

# Q4
val = 7 * 6 // 2
exp = "21"
comp = str(val)
results.append(("Q4", comp, exp, compare(comp, exp)))

# Q5
val = 29 - 21
exp = "8"
comp = str(val)
results.append(("Q5", comp, exp, compare(comp, exp)))

# Q6
val = 0  # C(2,3)=0
exp = "0"
comp = str(val)
results.append(("Q6", comp, exp, compare(comp, exp)))

# Q7
e1, e2, e3 = 1e-3, 2e-3, 5e-4
val = 1 - (1 - e1) * (1 - e2) * (1 - e3)
exp = "3.4965e-3"
comp = fmt_scientific(val, 5)
results.append(("Q7", comp, exp, compare(comp, exp)))

# Q8
tau, eps_min = 1e-3, 1e-2
val = math.log(1 - tau) / math.log(1 - eps_min)
exp = "0.0995"
comp = f"{val:.4f}"
results.append(("Q8", comp, exp, compare(comp, exp)))

# Q9
k = 4
val = 1 - (1 - eps_min) ** k
exp = "3.94e-2"
comp = fmt_scientific(val, 3)
results.append(("Q9", comp, exp, compare(comp, exp)))

# Q10
p = 0.9
m = 3654
val = p ** m
exp = "6.34e-168"
comp = fmt_scientific(val, 3)
results.append(("Q10", comp, exp, compare(comp, exp)))

# Q11
threshold = 0.01
max_n = 0
for n in range(1, 20):
    if math.comb(n, 3) <= math.log(threshold) / math.log(p):
        max_n = n
exp = "7"
comp = str(max_n)
results.append(("Q11", comp, exp, compare(comp, exp)))

# Q12
exp = "2"
comp = str(1.0 / 0.5)  # 1 TeV / 0.5 TeV
results.append(("Q12", comp, exp, compare(comp, exp)))

# Q13
exp = "3"
comp = str(1.5 / 0.5)
results.append(("Q13", comp, exp, compare(comp, exp)))

# Q14
val = 29 / 7
exp = "4.14"
comp = f"{val:.2f}"
results.append(("Q14", comp, exp, compare(comp, exp)))

# Q15
eps = 1e-2
val = 1 - (1 - eps) ** 2
exp = "0.0199"
comp = f"{val:.4f}"
results.append(("Q15", comp, exp, compare(comp, exp)))

# Q16
f = 0.5
val = 1 - (1 - f * e1) * (1 - f * e2) * (1 - f * e3)
exp = "1.7491e-3"
comp = fmt_scientific(val, 5)
results.append(("Q16", comp, exp, compare(comp, exp)))

# Output
match_count = sum(1 for _, _, _, m in results if m == "yes")
total = len(results)
mismatch_count = total - match_count

for cid, comp, exp, m in results:
    print(f"CLAIM {cid}: computed={comp} expected={exp} match={m}")

print(f"VERIFICATION SUMMARY: {total} claims, {match_count} match, {mismatch_count} mismatch")

```

## Execution output
```
CLAIM Q1: computed=406 expected=406 match=yes
CLAIM Q2: computed=3654 expected=3654 match=yes
CLAIM Q3: computed=9.0 expected=9.0 match=yes
CLAIM Q4: computed=21 expected=21 match=yes
CLAIM Q5: computed=8 expected=8 match=yes
CLAIM Q6: computed=0 expected=0 match=yes
CLAIM Q7: computed=3.4965e-03 expected=3.4965e-3 match=no
CLAIM Q8: computed=0.0995 expected=0.0995 match=yes
CLAIM Q9: computed=3.94e-02 expected=3.94e-2 match=no
CLAIM Q10: computed=6.341e-168 expected=6.34e-168 match=no
CLAIM Q11: computed=7 expected=7 match=yes
CLAIM Q12: computed=2.0 expected=2 match=no
CLAIM Q13: computed=3.0 expected=3 match=no
CLAIM Q14: computed=4.14 expected=4.14 match=yes
CLAIM Q15: computed=0.0199 expected=0.0199 match=yes
CLAIM Q16: computed=1.74913e-03 expected=1.7491e-3 match=no
VERIFICATION SUMMARY: 16 claims, 10 match, 6 mismatch

[exit 0]
```

## Adjudication

Each line is decided from its two printed numbers at the precision the paper states: the stated value matches when the computed value agrees with it to half a unit in the last stated digit, or to one unit when that is within one percent. The script's own match column is kept for reference.

| claim | computed | stated | script | decision | basis |
|---|---|---|---|---|---|
| Q1 | 406 | 406 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q2 | 3654 | 3654 | yes | match | 4 significant digits (as the paper states, at least 2) |
| Q3 | 9.0 | 9.0 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q4 | 21 | 21 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q5 | 8 | 8 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q6 | 0 | 0 | yes | match | stated value is zero |
| Q7 | 3.4965e-03 | 3.4965e-3 | no | match | 5 significant digits (as the paper states, at least 2) |
| Q8 | 0.0995 | 0.0995 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q9 | 3.94e-02 | 3.94e-2 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q10 | 6.341e-168 | 6.34e-168 | no | match | 3 significant digits (as the paper states, at least 2) |
| Q11 | 7 | 7 | yes | match | 2 significant digits (as the paper states, at least 2) |
| Q12 | 2.0 | 2 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q13 | 3.0 | 3 | no | match | 2 significant digits (as the paper states, at least 2) |
| Q14 | 4.14 | 4.14 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q15 | 0.0199 | 0.0199 | yes | match | 3 significant digits (as the paper states, at least 2) |
| Q16 | 1.74913e-03 | 1.7491e-3 | no | match | 5 significant digits (as the paper states, at least 2) |

Mismatches: 0 of 16.
